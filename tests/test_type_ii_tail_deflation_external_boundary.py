import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_external_boundary",
    ROOT / "reproductions" / "type_ii_tail_deflation_external_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationExternalBoundaryTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_ten_million_tail_misses(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-10m-full-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-10m-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(input_payload), checked)

    def test_tail_failure_does_not_force_any_stored_external_source_family(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-10m-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["tail_deflation_miss_count"], 84)
        self.assertEqual(result["adaptive_external_descent_count"], 70)
        self.assertEqual(result["mixed_factor_descent_count"], 77)
        self.assertEqual(result["quadratic_factor_descent_count"], 77)
        self.assertEqual(
            result["shared_external_misses"],
            [214_729, 297_049, 878_089, 1_511_449, 3_942_409, 5_478_169, 6_294_649],
        )
        self.assertEqual(result["mixed_factor_misses"], result["quadratic_factor_misses"])

    def test_hundred_million_external_boundary_rebuilds_and_has_forty_one_misses(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-100m-full-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-100m-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(input_payload), checked)
        self.assertEqual(checked["tail_deflation_miss_count"], 500)
        self.assertEqual(checked["quadratic_factor_descent_count"], 459)
        self.assertEqual(len(checked["quadratic_factor_misses"]), 41)


if __name__ == "__main__":
    unittest.main()
