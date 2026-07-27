import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_mixed_short_or_descent",
    ROOT / "reproductions" / "type_ii_h19_mixed_short_or_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19MixedShortOrDescentTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_checked_ac_and_descent_profiles(self):
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            ac_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json").open(encoding="utf-8") as handle:
            descent_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(ac_payload, descent_payload), checked)

    def test_radius_six_or_mixed_factor_descent_closes_every_h19_residual(self):
        with (ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["direct_ac_short_count"], 647)
        self.assertEqual(result["mixed_factor_descent_count"], 656)
        self.assertEqual(result["both_count"], 639)
        self.assertEqual(result["direct_ac_only_count"], 8)
        self.assertEqual(result["mixed_factor_only_count"], 17)
        self.assertEqual(result["unclosed_primes"], [])

    def test_mixed_only_branch_has_bounded_stored_scales(self):
        with (ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        records = result["mixed_factor_only_records"]
        self.assertEqual(len(records), 17)
        self.assertEqual(
            {record["mixed_factor_descent"]["k"] for record in records},
            {1, 2, 3, 5, 10, 14},
        )
        self.assertEqual(max(record["mixed_factor_descent"]["k"] for record in records), 14)
        self.assertEqual(
            [record["prime"] for record in result["direct_ac_only_records"]],
            [35_840_809, 85_192_969, 132_285_169, 141_326_089, 283_163_161, 325_045_249, 640_775_689, 985_076_569],
        )


if __name__ == "__main__":
    unittest.main()
