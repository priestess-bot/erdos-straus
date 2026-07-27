import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_SPEC = importlib.util.spec_from_file_location(
    "scaled_first_short_certificate",
    ROOT / "reproductions" / "short_certificate.py",
)
assert SHORT_SPEC and SHORT_SPEC.loader
short_certificate = importlib.util.module_from_spec(SHORT_SPEC)
sys.modules[SHORT_SPEC.name] = short_certificate
SHORT_SPEC.loader.exec_module(short_certificate)


class TypeIIScaledFirstTailDeflationTests(unittest.TestCase):
    def test_scaled_first_witness_reconstructs_both_identities(self):
        spf = short_certificate.smallest_prime_factors(100_000)
        witness = short_certificate.type_ii_scaled_first_tail_deflation_witness(
            67_369, 35, 7, spf
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.source_denominator, 1_918)
        self.assertLess(witness.source_denominator, witness.prime)
        self.assertEqual(
            Fraction(4, witness.source_denominator),
            sum(
                (Fraction(1, denominator) for denominator in witness.source_solution),
                Fraction(),
            ),
        )
        self.assertEqual(
            (
                witness.source_solution[0] // witness.first_scale,
                witness.source_solution[1] * witness.prime,
                witness.source_solution[2] * witness.prime,
            ),
            witness.target_solution,
        )

    def test_scaled_first_integrality_condition_is_exact(self):
        spf = short_certificate.smallest_prime_factors(100_000)
        self.assertIsNone(
            short_certificate.type_ii_scaled_first_tail_deflation_witness(
                67_369, 35, 6, spf
            )
        )
        witness = short_certificate.type_ii_scaled_first_tail_deflation_witness(
            67_369, 35, 7, spf
        )
        assert witness is not None
        self.assertEqual(
            (witness.first_scale * witness.prime - 1)
            % (witness.first_scale * witness.gap + 1),
            0,
        )

    def test_three_million_residual_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-scaled-first-tail-deflation-3m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_residual_count"], 41)
        self.assertEqual(result["scaled_first_hit_count"], 41)
        self.assertEqual(result["scaled_first_miss_count"], 0)
        record = next(item for item in result["records"] if item["prime"] == 2_978_089)
        self.assertEqual(
            (record["witness"]["first_scale"], record["witness"]["gap"]),
            (1_081, 95),
        )
