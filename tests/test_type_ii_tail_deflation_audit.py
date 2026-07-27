import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_audit",
    ROOT / "reproductions" / "type_ii_tail_deflation_audit.py",
)
assert SPEC and SPEC.loader
tail_deflation_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tail_deflation_audit
SPEC.loader.exec_module(tail_deflation_audit)


class TypeIITailDeflationAuditTests(unittest.TestCase):
    def test_three_million_escape_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-tail-deflation-3m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_escape_count"], 215)
        self.assertEqual(result["tail_deflation_hit_count"], 215)
        self.assertEqual(result["tail_deflation_miss_count"], 0)
        record = next(
            item for item in result["records"] if item["prime"] == 2_451_289
        )
        self.assertEqual(
            [
                (
                    witness["gap"],
                    witness["source_denominator"],
                    witness["certificate"]["divisor"],
                )
                for witness in record["witnesses"]
            ],
            [(83, 29_183, 693)],
        )
