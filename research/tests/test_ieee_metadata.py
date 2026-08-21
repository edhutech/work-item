import json
import tempfile
import unittest
from pathlib import Path

from research.tools.ieee_metadata import (
    DEFAULT_MAX_RECORDS,
    RetrievalError,
    api_artifact_path,
    evaluate_equivalence,
    planned_call_count,
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


class IeeeMetadataTests(unittest.TestCase):
    def test_pagination_and_raw_reconciliation(self):
        payloads = [
            {"totalfound": 3, "articles": [{"article_number": "1"}, {"article_number": "2"}]},
            {"totalfound": 3, "articles": [{"article_number": "3"}]},
        ]
        requests = []

        def opener(request, timeout):
            requests.append((request.full_url, timeout))
            return FakeResponse(payloads.pop(0))

        with tempfile.TemporaryDirectory() as directory:
            summary = retrieve(
                query_id="S1-F2A-IEEE-01-v1.1",
                query="candidate API representation",
                api_key="local-test-secret",
                raw_dir=Path(directory),
                max_records=2,
                daily_call_limit=200,
                pace_seconds=0,
                run_timestamp="20260821T000000Z",
                opener=opener,
                sleeper=lambda _seconds: None,
            )
            self.assertEqual(summary.raw_captured_records, 3)
            self.assertEqual(len(summary.artifacts), 2)
            self.assertIn("start_record=1", requests[0][0])
            self.assertIn("start_record=3", requests[1][0])
            for artifact in summary.artifacts:
                self.assertNotIn(b"local-test-secret", artifact.read_bytes())

    def test_short_page_is_incomplete(self):
        def opener(_request, timeout):
            return FakeResponse({"totalfound": 3, "articles": [{"article_number": "1"}]})

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "short page"):
                retrieve(
                    query_id="S1-F2A-IEEE-01-v1.1",
                    query="candidate",
                    api_key="secret",
                    raw_dir=Path(directory),
                    max_records=2,
                    pace_seconds=0,
                    opener=opener,
                    sleeper=lambda _seconds: None,
                )

    def test_daily_call_preflight(self):
        calls = []

        def opener(_request, timeout):
            calls.append(True)
            return FakeResponse({"totalfound": 401, "articles": []})

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "above daily limit"):
                retrieve(
                    query_id="S1-F2A-IEEE-01-v1.1",
                    query="candidate",
                    api_key="secret",
                    raw_dir=Path(directory),
                    max_records=200,
                    daily_call_limit=2,
                    expected_totalfound=401,
                    pace_seconds=0,
                    opener=opener,
                    sleeper=lambda _seconds: None,
                )
        self.assertEqual(len(calls), 0)

    def test_filename_generation(self):
        path = api_artifact_path(Path("raw"), "S1-F2A-IEEE-01-v1.1", "20260821T000000Z", 1)
        self.assertEqual(path.name, "S1-F2A-IEEE-01-v1.1__run-20260821T000000Z__api-start-000001.json")

    def test_equivalence_requires_all_gates(self):
        result = evaluate_equivalence(
            web_query_id="S1-F2A-IEEE-01-v1.1",
            web_field_strategy="Document Title; Abstract; Author Keywords",
            api_representation="candidate",
            api_totalfound=4798,
            known_web_count=4798,
            web_identifiers=["1", "2"],
            api_identifiers=["1", "2"],
            api_author_keywords_supported=False,
        )
        self.assertFalse(result["equivalence"])
        self.assertTrue(result["count_match"])

    def test_key_is_required_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RetrievalError, "IEEE_API_KEY"):
                retrieve(
                    query_id="S1-F2A-IEEE-01-v1.1",
                    query="candidate",
                    api_key="",
                    raw_dir=Path(directory),
                )


if __name__ == "__main__":
    unittest.main()
