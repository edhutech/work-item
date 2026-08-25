import json
import unittest
from pathlib import Path

from research.tools.review_pipeline import (
    EXCLUSION_REASONS,
    MatchClass,
    ScreeningDecision,
    ScreeningState,
    build_retrieved_record,
    build_version_family,
    classify_match,
    deduplicate,
    link_version,
    normalize_doi,
    normalize_title,
    normalization_audit_event,
    second_pass_queue,
    validate_decision_log,
    validate_screening_decision,
)


FIXTURE = Path(__file__).parent / "fixtures" / "review_pipeline_synthetic.json"


class ReviewPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = json.loads(FIXTURE.read_text())
        cls.records = [build_retrieved_record(item) for item in cls.raw]

    def test_fixtures_are_synthetic_and_ids_are_deterministic(self):
        self.assertTrue(all(item["source_database"].startswith("Synthetic") for item in self.raw))
        self.assertEqual(build_retrieved_record(self.raw[0]).record_id, self.records[0].record_id)
        self.assertTrue(self.records[0].record_id.startswith("REC-"))

    def test_normalization(self):
        self.assertEqual(normalize_doi(" DOI: https://doi.org/10.5555/X.1. "), "10.5555/x.1")
        self.assertEqual(normalize_title("A Safe  Work-Unit!"), "a safe work unit")

    def test_title_punctuation_case_duplicate_without_doi(self):
        left = build_retrieved_record({**self.raw[0], "doi": None, "source_record_id": "A-006", "title": "A Punctuation: Study", "authors": ["Title Author"], "publication_year": 2024})
        right = build_retrieved_record({**self.raw[0], "doi": None, "source_record_id": "A-007", "title": "a punctuation study", "authors": ["Title Author"], "publication_year": 2024})
        decision = classify_match(left, right)
        self.assertEqual(decision.classification, MatchClass.EXACT_DUPLICATE)

    def test_exact_doi_duplicate_and_cross_database_provenance(self):
        decision = classify_match(self.records[0], self.records[1])
        self.assertEqual(decision.classification, MatchClass.EXACT_DUPLICATE)
        result = deduplicate(self.records)
        group = next(group for group in result.groups if len(group.record_ids) == 2)
        self.assertTrue(group.source_id.startswith("SRC-"))
        self.assertEqual(len(group.record_ids), 2)
        self.assertNotEqual(self.records[0].source_database, self.records[1].source_database)
        self.assertEqual(normalization_audit_event(self.records[0])["query_id"], "SYN-F1-A")

    def test_same_title_different_year_needs_human_review(self):
        decision = classify_match(self.records[0], self.records[3])
        self.assertEqual(decision.classification, MatchClass.HUMAN_REVIEW)
        self.assertTrue(decision.requires_human_confirmation)

    def test_probable_title_match_is_not_automatic(self):
        left = build_retrieved_record({**self.raw[0], "doi": None, "source_record_id": "A-005", "title": "A Safe Work Unit With Flexible Contexts", "authors": ["Different Author"]})
        decision = classify_match(left, self.records[4])
        self.assertIn(decision.classification, {MatchClass.PROBABLE_DUPLICATE, MatchClass.HUMAN_REVIEW})
        self.assertTrue(decision.requires_human_confirmation)

    def test_version_relationship_is_not_duplicate(self):
        result = deduplicate(self.records)
        groups = {record_id for group in result.groups for record_id in group.record_ids}
        preprint = next(group.source_id for group in result.groups if any(record_id == self.records[5].record_id for record_id in group.record_ids))
        published = next(group.source_id for group in result.groups if any(record_id == self.records[6].record_id for record_id in group.record_ids))
        relation = link_version(preprint, published, "PREPRINT_OF", "Synthetic human confirmation", human_confirmed=True)
        self.assertEqual(relation.relationship, "PREPRINT_OF")
        self.assertNotEqual(preprint, published)
        self.assertEqual(len(groups), 7)
        family = build_version_family([relation])
        self.assertTrue(family.version_family_id.startswith("VER-"))
        self.assertEqual(set(family.source_ids), {preprint, published})

    def test_screening_and_second_pass_queue(self):
        decisions = [
            ScreeningDecision("SRC-a", "TITLE_ABSTRACT", ScreeningState.UNCERTAIN, "agent_recommendation", uncertainty_reason="missing abstract", decision_id="D-1"),
            ScreeningDecision("SRC-b", "TITLE_ABSTRACT", ScreeningState.EXCLUDE, "human", exclusion_reason="out of scope", rationale="Synthetic scope mismatch", decision_id="D-2"),
            ScreeningDecision("SRC-b", "TITLE_ABSTRACT", ScreeningState.UNCERTAIN, "second_pass_human", uncertainty_reason="consequential exclusion", rationale="Synthetic second pass", supersedes_decision_id="D-2", decision_id="D-4"),
            ScreeningDecision("SRC-c", "TITLE_ABSTRACT", ScreeningState.INCLUDE, "human", decision_id="D-3"),
        ]
        validate_decision_log(decisions)
        self.assertEqual({item.decision_id for item in second_pass_queue(decisions)}, {"D-1", "D-2", "D-4"})

    def test_invalid_and_contradictory_exclusions_rejected(self):
        self.assertIn("not evidence for the claimed use", EXCLUSION_REASONS)
        with self.assertRaises(ValueError):
            validate_screening_decision(ScreeningDecision("SRC-a", "TITLE_ABSTRACT", ScreeningState.EXCLUDE, "human", exclusion_reason="contradictory evidence", decision_id="D-4"))
        with self.assertRaises(ValueError):
            validate_screening_decision(ScreeningDecision("SRC-a", "TITLE_ABSTRACT", ScreeningState.EXCLUDE, "agent_recommendation", exclusion_reason="out of scope", decision_id="D-5"))


if __name__ == "__main__":
    unittest.main()
