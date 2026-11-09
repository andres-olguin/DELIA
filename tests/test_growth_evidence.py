"""Verifica evidencia trazable y evita publicar claims sin revisión."""
from copy import deepcopy
import json
import tempfile
import unittest
from pathlib import Path
from tools.validate_growth_evidence import CLAIMS, CALENDAR, validate


class GrowthEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.claims = json.loads(CLAIMS.read_text(encoding="utf-8"))
        self.calendar = json.loads(CALENDAR.read_text(encoding="utf-8"))

    def check(self, e=None, p=None):
        with tempfile.TemporaryDirectory() as tmp:
            ed = Path(tmp) / "claims.json"
            ca = Path(tmp) / "calendar.json"
            ed.write_text(json.dumps(e if e is not None else self.claims), encoding="utf-8")
            ca.write_text(json.dumps(p if p is not None else self.calendar), encoding="utf-8")
            return validate(ed, ca)

    def test_registry_is_valid(self):
        d = self.check()
        self.assertEqual(d["claim_count"], 12)
        self.assertEqual(d["calendar_items"], 10)
        self.assertEqual(d["published"], 0)

    def test_unverified_video_cannot_be_used_as_fact(self):
        e = deepcopy(self.claims)
        e["claims"][0]["public_use"] = "RESEARCH_REPORT"
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_unverified_video_cannot_be_added_to_calendar(self):
        p = deepcopy(self.calendar)
        p["items"][0]["claim_refs"].append("C-01")
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_legal_allegation_requires_attribution(self):
        e = deepcopy(self.claims)
        e["claims"][2]["public_use"] = "RESEARCH_REPORT"
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_hypothesis_cannot_be_reported_as_result(self):
        e = deepcopy(self.claims)
        e["claims"][8]["public_use"] = "RESEARCH_REPORT"
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_reported_event_requires_source(self):
        e = deepcopy(self.claims)
        e["claims"][1]["sources"] = []
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_source_url_must_be_https(self):
        e = deepcopy(self.claims)
        e["sources"][0]["url"] = "http://not-secure.local/example"
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_unregistered_source_fails(self):
        e = deepcopy(self.claims)
        e["claims"][1]["sources"].append("S-NOTHING")
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_duplicate_source_url_fails(self):
        e = deepcopy(self.claims)
        e["sources"][0]["url"] = e["sources"][1]["url"]
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_source_cannot_postdate_review(self):
        e = deepcopy(self.claims)
        e["sources"][0]["published"] = "2027-01-01"
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_draft_cannot_be_approved(self):
        p = deepcopy(self.calendar)
        p["items"][0]["approved"] = True
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_draft_cannot_have_publication_url(self):
        p = deepcopy(self.calendar)
        p["items"][0]["publication_url"] = "https://example.com/post"
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_published_requires_review(self):
        p = deepcopy(self.calendar)
        p["items"][0]["status"] = "PUBLISHED"
        p["items"][0]["publication_url"] = "https://example.com/post"
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_published_requires_url(self):
        p = deepcopy(self.calendar)
        p["items"][0]["status"] = "PUBLISHED"
        p["items"][0]["approved"] = True
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_published_with_review_and_url_is_accepted(self):
        p = deepcopy(self.calendar)
        p["items"][0]["status"] = "PUBLISHED"
        p["items"][0]["approved"] = True
        p["items"][0]["publication_url"] = "https://example.org/post/reviewed"
        self.assertEqual(self.check(p=p)["published"], 1)

    def test_sensational_claim_in_title_rejected(self):
        p = deepcopy(self.calendar)
        p["items"][0]["topic"] = "ChatGPT mató a una persona"
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_claim_id_duplicate_fails(self):
        e = deepcopy(self.claims)
        e["claims"].append(deepcopy(e["claims"][0]))
        with self.assertRaises(ValueError):
            self.check(e=e)

    def test_calendar_duplicated_id_fails(self):
        p = deepcopy(self.calendar)
        p["items"].append(deepcopy(p["items"][0]))
        with self.assertRaises(ValueError):
            self.check(p=p)

    def test_no_calendar_post_after_date_review_mismatch(self):
        p = deepcopy(self.calendar)
        p["review_date"] = "2026-11-10"
        with self.assertRaises(ValueError):
            self.check(p=p)


if __name__ == "__main__":
    unittest.main()
