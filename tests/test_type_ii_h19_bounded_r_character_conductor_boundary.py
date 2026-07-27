import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_character_conductor_boundary",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_character_conductor_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRCharacterConductorBoundaryTests(unittest.TestCase):
    def test_checked_one_billion_character_conductor_artifact(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-bounded-r-character-conductor-boundary-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertTrue(result["all_common_state_moduli_are_one"])
        self.assertTrue(
            all(row["common_state_modulus"] == 1 for row in result["records"])
        )

    def test_empty_modulus_list_is_rejected(self):
        with self.assertRaises(ValueError):
            audit.common_modulus([])


if __name__ == "__main__":
    unittest.main()
