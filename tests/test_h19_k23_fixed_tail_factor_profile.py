import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPTIONAL_SHARED = (
    ROOT / "reproductions" / "h19-k23-shared-selector-audit-262144.json"
)
OPTIONAL_CLOSURE = (
    ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
)
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_fixed_tail_factor_profile",
    ROOT / "reproductions" / "h19_k23_fixed_tail_factor_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23FixedTailFactorProfileTests(unittest.TestCase):
    @unittest.skipUnless(
        OPTIONAL_SHARED.is_file() and OPTIONAL_CLOSURE.is_file(),
        "optional 262144-layer raw artifacts are not tracked",
    )
    def test_common_factor_explains_the_fixed_gap_tail_routes(self):
        with OPTIONAL_SHARED.open(encoding="utf-8") as handle:
            shared = json.load(handle)
        with OPTIONAL_CLOSURE.open(encoding="utf-8") as handle:
            closure = json.load(handle)
        result = profile.run_profile(shared, closure)
        self.assertEqual(result["common_p_minus_one_factor"], 165_600)
        self.assertEqual(result["record_count"], 588_526)
        self.assertEqual(result["fixed_factor_direct_tail_count"], 586_992)
        self.assertEqual(result["residual_count"], 1_534)
        self.assertEqual(result["residual_accidental_direct_count"], 3)
        self.assertEqual(result["residual_alternative_tail_count"], 1_531)
        self.assertEqual(result["m27_to_m31_q8_factor_square_count"], 247)
        self.assertEqual(
            result["m27_to_m31_q8_divisor_histogram"],
            {"1": 53, "2": 55, "4": 36, "8": 55, "16": 48},
        )
        self.assertEqual(result["remaining_new_factor_alternative_count"], 1_284)
        self.assertEqual(
            result["residual_gap_histogram"],
            {"27": 1_490, "43": 22, "51": 8, "55": 7, "63": 4, "83": 1, "87": 2},
        )
        self.assertEqual(
            result["fixed_factor_gaps"],
            [3, 7, 11, 15, 19, 23, 31, 35, 39, 47, 59, 71, 95, 99],
        )
