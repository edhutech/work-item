import json
import tempfile
import unittest
from pathlib import Path

from research.tools.scopus_search import (
    RetrievalError,
    artifact_path,
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


def response(entries, total=3):
    return {"search-results": {"opensearch:totalResults": str(total), "entry": entries}}


class ScopusSearchTests(unittest.TestCase):
    def test_pagination_and_reconciliation_preserve_raw_json(self):
        payloads = [response([{"eid": "1"}, {"eid": "2"}]), response([{"eid": "3"}])]
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return FakeResponse(payloads.pop(0))

        with tempfile.TemporaryDirectory() as directory:
            summary = retrieve(query_id="S1-F1-SCOPUS-01-v1", query="TITLE-ABS-KEY(candidate)", api_key="secret", raw_dir=Path(directory), count=2, pace_seconds=0, run_timestamp="20260821T000000Z", opener=opener, sleeper=lambda _seconds: None)
            self.assertTrue(summary.reconciled)
            self.assertEqual([request.full_url.split("start=")[1].split("&")[0] for request in requests], ["0", "2"])
            self.assertEqual(json.loads(summary.artifacts[0].read_text()), {"search-results": {"opensearch:totalResults": "3", "entry": [{"eid": "1"}, {"eid": "2"}]}})
            self.assertNotIn("secret", summary.artifacts[0].read_text())

    def test_incomplete_short_page_fails(self):
        def opener(_request, timeout):
            return FakeResponse(response([{"eid": "1"}]))

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "short page"):
                retrieve(query_id="S1-F1-SCOPUS-01-v1", query="candidate", api_key="secret", raw_dir=Path(directory), count=2, pace_seconds=0, opener=opener, sleeper=lambda _seconds: None)

    def test_filename_generation(self):
        self.assertEqual(artifact_path(Path("raw"), "S1-F1-SCOPUS-01-v1", "20260821T000000Z", 0).name, "S1-F1-SCOPUS-01-v1__run-20260821T000000Z__api-start-000000.json")

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
        self.assertNotIn("secret", requests[0].full_url)
        self.assertEqual(requests[0].get_header("X-els-apikey"), "secret")

    def test_dry_run_does_not_access_network(self):
        output = dry_run(query_id="S1-F1-SCOPUS-01-v1", query_reference="frozen query reference", count=25, raw_dir=Path("raw"))
        self.assertIn("network not accessed", output)
        self.assertNotIn("ELSEVIER_API_KEY", output)


if __name__ == "__main__":
    unittest.main()
