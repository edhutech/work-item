import json
import tempfile
import unittest
from pathlib import Path

from research.tools.scopus_search import (
    DEFAULT_COUNT,
    RetrievalError,
    artifact_path,
    cursor_artifact_path,
    dry_run,
    equivalence_report,
    retrieve,
)


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode()

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


def response(entries, total=3, cursor_next=None):
    result = {"opensearch:totalResults": str(total), "entry": entries}
    if cursor_next is not None:
        result["cursor"] = {"@next": cursor_next}
    return {"search-results": result}


class ScopusSearchTests(unittest.TestCase):
    def test_pagination_and_reconciliation_preserve_raw_json(self):
        payloads = [response([{"eid": "1"}, {"eid": "2"}]), response([{"eid": "3"}])]
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(payloads.pop(0))

        with tempfile.TemporaryDirectory() as directory:
            summary = retrieve(query_id="S1-F1-SCOPUS-01-v1", query="TITLE-ABS-KEY(candidate)", api_key="secret", raw_dir=Path(directory), count=2, pagination="offset", pace_seconds=0, run_timestamp="20260821T000000Z", opener=opener, sleeper=lambda _seconds: None)
            self.assertTrue(summary.reconciled)
            self.assertEqual([request.full_url.split("start=")[1].split("&")[0] for request in requests], ["0", "2"])
            self.assertEqual(json.loads(summary.artifacts[0].read_text()), {"search-results": {"opensearch:totalResults": "3", "entry": [{"eid": "1"}, {"eid": "2"}]}})
            self.assertNotIn("secret", summary.artifacts[0].read_text())

    def test_incomplete_short_page_fails(self):
        def opener(_request, timeout):
            return FakeResponse(response([{"eid": "1"}]))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "short page"):
                    retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=2, pagination="offset", pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_filename_generation(self):
        self.assertEqual(artifact_path(Path("raw"), "S1-F1-SCOPUS-01-v1", "20260821T000000Z", 0).name, "S1-F1-SCOPUS-01-v1__run-20260821T000000Z__api-start-000000.json")
        self.assertEqual(cursor_artifact_path(Path("raw"), "S1-F1-SCOPUS-01-v1", "20260821T000000Z", 1).name, "S1-F1-SCOPUS-01-v1__run-20260821T000000Z__api-page-000001.json")

    def test_equivalence_gate_never_approves(self):
        report = equivalence_report(query_id="Q", web_query_id="Q", web_query="exact", api_query="exact", web_count=2, api_total_results=2, web_identifiers=["E1", "D1"], api_identifiers=["E1", "D1"])
        self.assertTrue(report["exact_query_match"])
        self.assertFalse(report["api_retrieval_approved"])

    def test_secret_is_not_in_request_url_and_header_is_used(self):
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(response([] , total=0))

        with tempfile.TemporaryDirectory() as directory:
            retrieve(query_id="S1-F1-SCOPUS-01-v1", query="exact", api_key="secret", raw_dir=Path(directory), pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)
            for artifact in Path(directory).iterdir():
                self.assertNotIn("secret", artifact.read_text())
        self.assertNotIn("secret", requests[0].full_url)
        self.assertEqual(requests[0].get_header("X-els-apikey"), "secret")

    def test_default_request_uses_standard_route_without_complete_view(self):
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(response([], total=0))

        with tempfile.TemporaryDirectory() as directory:
            retrieve(query_id="S1-F1-SCOPUS-01-v1", query="exact", api_key="secret", raw_dir=Path(directory), pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)
        self.assertNotIn("view=", requests[0].full_url)
        self.assertIn(f"count={DEFAULT_COUNT}", requests[0].full_url)
        self.assertEqual(requests[0].get_header("X-els-apikey"), "secret")

    def test_default_pagination_is_offset_and_cursor_is_unavailable(self):
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(response([], total=0))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "cursor pagination is unavailable"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="exact", api_key="secret", raw_dir=Path(directory), pagination="cursor", pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)
        self.assertEqual(requests, [])

    def test_default_page_size_is_empirically_safe_value(self):
        self.assertEqual(DEFAULT_COUNT, 25)

    def test_complete_view_is_explicit_opt_in(self):
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(response([], total=0))

        with tempfile.TemporaryDirectory() as directory:
            retrieve(query_id="S1-F1-SCOPUS-01-v1", query="exact", api_key="secret", raw_dir=Path(directory), view="COMPLETE", count=25, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)
        self.assertIn("view=COMPLETE", requests[0].full_url)
        self.assertIn("count=25", requests[0].full_url)

    def test_large_result_set_uses_cursor_and_reconciles(self):
        total = 5001
        requests = []

        def opener(request, timeout):
            requests.append(request)
            cursor = request.full_url.split("cursor=")[1].split("&")[0]
            page = 0 if cursor == "%2A" else int(cursor)
            start = page * 200
            returned = min(200, total - start)
            next_cursor = str(page + 1) if start + returned < total else None
            return FakeResponse(response([{"eid": str(index)} for index in range(start, start + returned)], total, next_cursor))

        with tempfile.TemporaryDirectory() as directory:
            summary = retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), view="STANDARD", count=200, pagination="cursor", cursor_available=True, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)
            self.assertEqual(summary.raw_captured_records, total)
            self.assertTrue(summary.reconciled)
            self.assertEqual(summary.api_calls, 26)
            self.assertEqual(len(summary.artifacts), 26)
            self.assertIn("cursor=", requests[1].full_url)
            self.assertTrue(all(request.get_header("X-els-apikey") == "secret" for request in requests))
            self.assertTrue(all(request.get_header("Accept") == "application/json" for request in requests))
            metadata = json.loads(summary.artifacts[0].with_suffix(".metadata.json").read_text())
            self.assertEqual(metadata["cursor"], "*")
            self.assertEqual(metadata["cursor_next"], "1")

    def test_repeated_cursor_fails(self):
        calls = []

        def opener(_request, timeout):
            calls.append(True)
            if len(calls) == 1:
                return FakeResponse(response([{"eid": "1"}, {"eid": "2"}], 5, "a"))
            return FakeResponse(response([{"eid": "3"}, {"eid": "4"}], 5, "a"))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "repeated Scopus cursor"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=2, pagination="cursor", cursor_available=True, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_premature_empty_cursor_page_fails(self):
        calls = []

        def opener(_request, timeout):
            calls.append(True)
            if len(calls) == 1:
                return FakeResponse(response([{"eid": "1"}, {"eid": "2"}], 3, "a"))
            return FakeResponse(response([], 3))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "short page or empty page"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=2, pagination="cursor", cursor_available=True, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_cursor_without_next_token_fails_reconciliation(self):
        def opener(_request, timeout):
            return FakeResponse(response([{"eid": "1"}, {"eid": "2"}], 3))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "no next cursor"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=2, pagination="cursor", cursor_available=True, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_offset_rejects_result_sets_over_boundary(self):
        def opener(_request, timeout):
            return FakeResponse(response([{"eid": "1"}], 5001))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "offset boundary"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=25, pagination="offset", pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_dry_run_does_not_access_network(self):
        output = dry_run(query_id="S1-F1-SCOPUS-01-v1", query_reference="frozen query reference", count=25, raw_dir=Path("raw"))
        self.assertIn("network not accessed", output)
        self.assertNotIn("ELSEVIER_API_KEY", output)


if __name__ == "__main__":
    unittest.main()
