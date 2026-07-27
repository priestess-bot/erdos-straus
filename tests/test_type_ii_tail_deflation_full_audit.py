import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_full_audit",
    ROOT / "reproductions" / "type_ii_tail_deflation_full_audit.py",
)
assert SPEC and SPEC.loader
tail_deflation_full_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tail_deflation_full_audit
SPEC.loader.exec_module(tail_deflation_full_audit)


class TypeIITailDeflationFullAuditTests(unittest.TestCase):
    def test_first_witness_is_the_first_scan_witness(self):
        spf = tail_deflation_full_audit.short_certificate.smallest_prime_factors(100_000)
        for prime in (73, 97, 193, 67_369):
            full = tail_deflation_full_audit.short_certificate.type_ii_tail_deflation_scan(
                prime, spf
            )
            first = (
                tail_deflation_full_audit.short_certificate.first_type_ii_tail_deflation_witness(
                    prime, spf
                )
            )
            self.assertEqual(first, full[0] if full else None)

    def test_million_scale_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-tail-deflation-1m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 9_732)
        self.assertEqual(result["tail_deflation_hit_count"], 9_717)
        self.assertEqual(result["tail_deflation_miss_count"], 15)
        self.assertEqual(result["largest_minimum_gap"], 695)
        self.assertEqual(result["record_holders"][-1]["prime"], 565_849)
        self.assertEqual(result["misses"][0]["prime"], 67_369)
