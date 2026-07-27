import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_finite_product_exponent_profile",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_finite_product_exponent_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRFiniteProductExponentProfileTests(unittest.TestCase):
    def test_checked_one_billion_finite_product_artifact(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-bounded-r-finite-product-exponent-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["power_cap"], 9)
        self.assertEqual(result["finite_product_state_count"], 40)
        self.assertEqual(
            result["first_cover_power_histogram"],
            {"3": 26, "4": 2, "5": 7, "6": 2, "7": 1, "9": 2},
        )

    def test_power_cap_must_exceed_the_square_tail(self):
        with self.assertRaises(ValueError):
            audit.run_audit({"records": []}, 2)


if __name__ == "__main__":
    unittest.main()
