import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_tail_exponent_rigidity",
    ROOT / "reproductions" / "type_ii_h19_tail_exponent_rigidity.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19TailExponentRigidityTests(unittest.TestCase):
    def test_checked_one_billion_higher_power_candidates_fail_the_original_tail(self):
        path = ROOT / "reproductions" / "type-ii-h19-tail-exponent-rigidity-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["state_count"], 40)
        self.assertEqual(result["target_candidate_count"], 338)
        self.assertEqual(result["target_candidate_at_most_m_count"], 32)
        self.assertEqual(result["integral_v_count"], 0)
        self.assertTrue(result["all_higher_power_candidates_fail_original_tail"])

    def test_factorization_reconstruction(self):
        self.assertEqual(audit.m_from_factorization({"2": 1, "3": 2}), 18)


if __name__ == "__main__":
    unittest.main()
