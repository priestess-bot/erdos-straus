import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPTIONAL_AUDIT_65536 = (
    ROOT / "reproductions" / "h19-k23-shared-selector-audit-65536.json"
)
OPTIONAL_AUDIT_131072 = (
    ROOT / "reproductions" / "h19-k23-shared-selector-audit-131072.json"
)
OPTIONAL_AUDIT_262144 = (
    ROOT / "reproductions" / "h19-k23-shared-selector-audit-262144.json"
)
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_shared_selector_tail_descent_closure",
    ROOT / "reproductions" / "h19_k23_shared_selector_tail_descent_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)

AUDIT_SPEC = importlib.util.spec_from_file_location(
    "h19_k23_shared_selector_audit_for_closure",
    ROOT / "reproductions" / "h19_k23_shared_selector_audit.py",
)
assert AUDIT_SPEC and AUDIT_SPEC.loader
selector_audit = importlib.util.module_from_spec(AUDIT_SPEC)
sys.modules[AUDIT_SPEC.name] = selector_audit
AUDIT_SPEC.loader.exec_module(selector_audit)


class H19K23SharedSelectorTailDescentClosureTests(unittest.TestCase):
    def test_compact_selector_fixture_closes_without_full_witness_fields(self):
        result = closure.run_audit(selector_audit.run_audit(8, 59, compact=True))
        self.assertEqual(result["input_prime_count"], 29)
        self.assertEqual(result["ordinary_tail_descent_count"], 29)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])

    def test_full_artifact_has_direct_or_alternative_tail_exit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-16384.json"
        ).open(encoding="utf-8") as handle:
            result = closure.run_audit(json.load(handle))
        self.assertEqual(result["input_parameter_limit_exclusive"], 16_384)
        self.assertEqual(result["input_prime_count"], 39_658)
        self.assertEqual(result["record_count"], 39_658)
        self.assertEqual(result["ordinary_tail_descent_count"], 39_658)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        self.assertEqual(
            result["route_counts"],
            {"alternative-p-minus-one-gap": 106, "shared-gap": 39_552},
        )
        alternative_gaps = {
            row["shared_selector_gap"]
            for row in result["records"]
            if row["route"] == "alternative-p-minus-one-gap"
        }
        self.assertEqual(alternative_gaps, {27, 43, 55})

    def test_extended_artifact_has_direct_or_alternative_tail_exit(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-32768.json"
        ).open(encoding="utf-8") as handle:
            result = closure.run_audit(json.load(handle))
        self.assertEqual(result["input_parameter_limit_exclusive"], 32_768)
        self.assertEqual(result["input_prime_count"], 77_823)
        self.assertEqual(result["record_count"], 77_823)
        self.assertEqual(result["ordinary_tail_descent_count"], 77_823)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        self.assertEqual(
            result["route_counts"],
            {"alternative-p-minus-one-gap": 208, "shared-gap": 77_615},
        )
        alternative_gaps = {
            row["shared_selector_gap"]
            for row in result["records"]
            if row["route"] == "alternative-p-minus-one-gap"
        }
        self.assertEqual(alternative_gaps, {27, 43, 51, 55, 87})

    @unittest.skipUnless(
        OPTIONAL_AUDIT_65536.is_file(), "optional 65536-layer raw artifact is not tracked"
    )
    def test_sixty_five_thousand_layer_artifact_has_tail_exit(self):
        with OPTIONAL_AUDIT_65536.open(encoding="utf-8") as handle:
            result = closure.run_audit(json.load(handle))
        self.assertEqual(result["input_parameter_limit_exclusive"], 65_536)
        self.assertEqual(result["input_prime_count"], 152_893)
        self.assertEqual(result["record_count"], 152_893)
        self.assertEqual(result["ordinary_tail_descent_count"], 152_893)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        self.assertEqual(
            result["route_counts"],
            {"alternative-p-minus-one-gap": 419, "shared-gap": 152_474},
        )
        alternative_gaps = {
            row["shared_selector_gap"]
            for row in result["records"]
            if row["route"] == "alternative-p-minus-one-gap"
        }
        self.assertEqual(alternative_gaps, {27, 43, 51, 55, 83, 87})

    @unittest.skipUnless(
        OPTIONAL_AUDIT_131072.is_file(), "optional 131072-layer raw artifact is not tracked"
    )
    def test_one_hundred_thirty_one_thousand_layer_artifact_has_tail_exit(self):
        with OPTIONAL_AUDIT_131072.open(encoding="utf-8") as handle:
            result = closure.run_audit(json.load(handle))
        self.assertEqual(result["input_parameter_limit_exclusive"], 131_072)
        self.assertEqual(result["input_prime_count"], 299_782)
        self.assertEqual(result["record_count"], 299_782)
        self.assertEqual(result["ordinary_tail_descent_count"], 299_782)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        self.assertEqual(
            result["route_counts"],
            {"alternative-p-minus-one-gap": 795, "shared-gap": 298_987},
        )
        alternative_gaps = {
            row["shared_selector_gap"]
            for row in result["records"]
            if row["route"] == "alternative-p-minus-one-gap"
        }
        self.assertEqual(alternative_gaps, {27, 43, 51, 55, 63, 83, 87})

    @unittest.skipUnless(
        OPTIONAL_AUDIT_262144.is_file(), "optional 262144-layer raw artifact is not tracked"
    )
    def test_two_hundred_sixty_two_thousand_layer_artifact_has_tail_exit(self):
        with OPTIONAL_AUDIT_262144.open(encoding="utf-8") as handle:
            result = closure.run_audit(json.load(handle))
        self.assertEqual(result["input_parameter_limit_exclusive"], 262_144)
        self.assertEqual(result["input_prime_count"], 588_526)
        self.assertEqual(result["record_count"], 588_526)
        self.assertEqual(result["ordinary_tail_descent_count"], 588_526)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        self.assertEqual(
            result["route_counts"],
            {"alternative-p-minus-one-gap": 1_531, "shared-gap": 586_995},
        )
        alternative_gaps = {
            row["shared_selector_gap"]
            for row in result["records"]
            if row["route"] == "alternative-p-minus-one-gap"
        }
        self.assertEqual(alternative_gaps, {27, 43, 51, 55, 63, 83, 87})


if __name__ == "__main__":
    unittest.main()
