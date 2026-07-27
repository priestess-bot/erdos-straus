import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_scaled_source_candidate_profile",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_scaled_source_candidate_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRScaledSourceCandidateProfileTests(unittest.TestCase):
    def test_checked_one_billion_candidate_artifact(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-bounded-r-scaled-source-candidates-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertEqual(result["source_ray_count"], 245)
        self.assertEqual(result["scaled_source_candidate_count"], 3_519)
        self.assertEqual(result["unique_scaled_source_candidate_count"], 1_025)
        self.assertEqual(result["candidate_denominator_histogram"], {"2": 456, "4": 3063})

    def test_candidate_reduction_on_a_small_source(self):
        candidates = audit.scaled_candidates(3_361, 3_360)
        self.assertTrue(candidates)
        for candidate in candidates:
            self.assertEqual(candidate["source_first_denominator"] % candidate["shift"], 0)


if __name__ == "__main__":
    unittest.main()
