import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_SPEC = importlib.util.spec_from_file_location(
    "shared_divisor_short_certificate",
    ROOT / "reproductions" / "short_certificate.py",
)
assert SHORT_SPEC and SHORT_SPEC.loader
short_certificate = importlib.util.module_from_spec(SHORT_SPEC)
sys.modules[SHORT_SPEC.name] = short_certificate
SHORT_SPEC.loader.exec_module(short_certificate)


class TypeIISharedDivisorTailTests(unittest.TestCase):
    def test_direct_divisor_scan_removes_the_first_scale_cutoff(self):
        prime = 6_569_161
        spf = short_certificate.smallest_prime_factors(prime + 100)
        witness = short_certificate.type_ii_shared_divisor_tail_deflation_scan(
            prime, 100, spf
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            (witness.gap, witness.first_scale, witness.source_denominator),
            (55, 7_465, 119_440),
        )
        self.assertGreater(witness.first_scale, 2_000)

    def test_ten_million_residual_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-shared-divisor-tail-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_residual_count"], 84)
        self.assertEqual(result["shared_divisor_hit_count"], 84)
        self.assertEqual(result["shared_divisor_miss_count"], 0)
        record = next(item for item in result["records"] if item["prime"] == 6_569_161)
        self.assertEqual(
            (
                record["witness"]["gap"],
                record["witness"]["first_scale"],
                record["witness"]["source_denominator"],
            ),
            (55, 7_465, 119_440),
        )
