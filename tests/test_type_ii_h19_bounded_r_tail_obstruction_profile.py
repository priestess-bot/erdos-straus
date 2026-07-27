import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_tail_obstruction_profile",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_tail_obstruction_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRTailObstructionProfileTests(unittest.TestCase):
    def test_checked_one_billion_r_capped_residual_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertEqual(result["compatible_state_count"], 156)
        self.assertEqual(
            result["classification_counts"],
            {"finite-product-set": 40, "subgroup-character": 116},
        )
        self.assertTrue(result["all_subgroup_character_states_quadratically_separated"])
        self.assertEqual(result["records"][0]["prime"], 3_361)
        self.assertEqual(result["records"][-1]["prime"], 749_224_921)

    def test_requires_a_selected_stage(self):
        with self.assertRaises(ValueError):
            audit.residual_primes({"stages": []}, 9_999)


if __name__ == "__main__":
    unittest.main()
