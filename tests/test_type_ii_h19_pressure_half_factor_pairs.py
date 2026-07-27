import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pressure_half_factor_pairs",
    ROOT / "reproductions" / "type_ii_h19_pressure_half_factor_pairs.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19PressureHalfFactorPairsTests(unittest.TestCase):
    def test_checked_one_billion_pressure_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-pressure-half-factor-pairs-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["pressure_state_count"], 4)
        self.assertTrue(result["all_selected_r_are_7_mod_8"])
        self.assertEqual(
            [
                (row["prime"], row["r"], row["half_factor_residue"])
                for row in result["records"]
            ],
            [
                (35_840_809, 103, 52),
                (132_285_169, 31, 16),
                (141_326_089, 31, 16),
                (640_775_689, 15, 8),
            ],
        )
        for row in result["records"]:
            for pair in row["oriented_half_factor_pairs"]:
                self.assertEqual(pair["a"] * pair["b"], row["m"])
                self.assertEqual(pair["a_mod_r"], row["half_factor_residue"])
                self.assertEqual(pair["b_mod_r"], row["half_factor_residue"])
                self.assertEqual(pair["b"] % 2, 0)
                self.assertEqual(pair["r_mod_8"], 7)

    def test_rejects_incompatible_ray(self):
        with self.assertRaises(ValueError):
            audit.half_factor_pair(73, 3, 3, 5)

    def test_rejects_the_empty_r_three_mod_eight_class(self):
        with self.assertRaises(ValueError):
            audit.half_factor_pair(73, 3, 1, 23)


if __name__ == "__main__":
    unittest.main()
