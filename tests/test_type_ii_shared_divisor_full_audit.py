import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_shared_divisor_full_audit",
    ROOT / "reproductions" / "type_ii_shared_divisor_full_audit.py",
)
assert SPEC and SPEC.loader
shared_divisor_full_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = shared_divisor_full_audit
SPEC.loader.exec_module(shared_divisor_full_audit)


class TypeIISharedDivisorFullAuditTests(unittest.TestCase):
    def test_ten_million_gap_239_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-shared-divisor-10m-gap239-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["captured_count"], 82_887)
        self.assertEqual(result["miss_count"], 0)
        self.assertEqual(result["largest_minimum_gap"], 239)
        self.assertEqual(result["largest_first_scale"], 664_185)
        self.assertEqual(result["scale_record_holders"][-1]["prime"], 9_962_761)
