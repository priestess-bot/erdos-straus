import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_adaptive_multiscale_audit",
    ROOT / "reproductions" / "h19_k23_adaptive_multiscale_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19K23AdaptiveMultiscaleAuditTests(unittest.TestCase):
    def test_small_parameter_fixture_is_fully_classified(self):
        result = audit.run_audit(8)
        self.assertEqual(result["prime_count"], 29)
        self.assertEqual(result["uncovered_records"], [])
        self.assertEqual(result["largest_first_success_scale"], 8)
        self.assertEqual(
            result["first_success_scale_histogram"],
            {"1": 11, "2": 8, "3": 7, "4": 1, "6": 1, "8": 1},
        )

    def test_checked_artifact_summary(self):
        with (
            ROOT / "reproductions" / "h19-k23-adaptive-multiscale-audit.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parameter_limit_exclusive"], 1024)
        self.assertEqual(result["prime_count"], 2687)
        self.assertEqual(result["uncovered_records"], [])
        self.assertEqual(result["largest_first_success_scale"], 15)


if __name__ == "__main__":
    unittest.main()
