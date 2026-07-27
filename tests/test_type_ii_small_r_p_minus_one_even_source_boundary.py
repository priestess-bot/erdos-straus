import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_r_p_minus_one_even_source_boundary",
    ROOT / "reproductions" / "type_ii_small_r_p_minus_one_even_source_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIISmallRPMinusOneEvenSourceBoundaryTests(unittest.TestCase):
    def test_all_odd_distances_on_the_joint_boundary(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-small-r-p-minus-one-even-source-boundary-100k-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000)
        self.assertEqual(result["joint_small_r_p_minus_one_residual_count"], 7)
        self.assertEqual(result["odd_distance_test_count"], 91_538)
        self.assertEqual(result["even_source_strict_lift_count"], 2)
        self.assertEqual(
            result["fully_even_source_unclosed_primes"],
            [5_209, 21_169, 27_481, 48_409, 80_809],
        )
        hits = {
            record["prime"]: record["first_even_source_witness"]
            for record in result["records"]
            if record["first_even_source_witness"] is not None
        }
        self.assertEqual(hits[12_601]["source_denominator"], 12_600)
        self.assertEqual(hits[97_561]["source_denominator"], 97_560)


if __name__ == "__main__":
    unittest.main()
