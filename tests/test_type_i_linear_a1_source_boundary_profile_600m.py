from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_a1_source_boundary_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-linear-a1-source-boundary-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("linear_a1_source_boundary", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearAOneSourceBoundaryProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.captured = {
            int(record["prime"]): record["selected_witness"]
            for record in cls.payload["captured_records"]
        }

    def test_reproducible_artifact_and_exact_boundary_totals(self):
        self.assertEqual(self.payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(
            {
                key: self.payload[key]
                for key in (
                    "input_prime_count",
                    "a_eq_1_source_state_count",
                    "target_R_audits_until_first_hit_or_exhaustion",
                    "captured_count",
                    "miss_count",
                )
            },
            profile.EXPECTED_TOTALS,
        )
        self.assertEqual(
            self.payload["misses"][: len(profile.EXPECTED_MISS_PREFIX)],
            profile.EXPECTED_MISS_PREFIX,
        )
        self.assertIn(214_729, self.payload["misses"])
        self.assertIn(297_049, self.payload["misses"])
        self.assertIn(878_089, self.payload["misses"])

    def test_every_stored_a_one_witness_replays_exactly(self):
        for prime, witness in self.captured.items():
            assert isinstance(witness, dict)
            a = int(witness["a"])
            s = int(witness["s"])
            R = int(witness["R"])
            E = int(witness["E"])
            source = int(witness["source_denominator"])
            K = int(witness["K"])
            divisor = int(witness["matched_square_divisor"])
            A = int(witness["A"])
            B = int(witness["B"])
            C = int(witness["C"])
            H = int(witness["H"])
            gap = int(witness["gap"])

            self.assertEqual(a, 1)
            self.assertEqual(prime - 1, s * (R + 1))
            self.assertEqual(prime, 1 + s + s * R)
            self.assertEqual(E, source)
            self.assertEqual(E, s * R + 1)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(divisor, B * B * C)
            self.assertEqual(K, B * C * H)
            self.assertEqual(math.gcd(B, H), 1)
            self.assertEqual((K * K) % divisor, 0)
            self.assertEqual((4 * divisor + 1) % R, 0)
            self.assertEqual(A * R, B + H)
            self.assertEqual(gap * R, 4 * divisor + 1)
            self.assertEqual(prime, 4 * A * B * C - gap)
            self.assertEqual(
                Fraction(4, prime),
                sum((Fraction(1, value) for value in witness["target_solution"]), Fraction()),
            )
            self.assertEqual(
                Fraction(4, source),
                sum((Fraction(1, value) for value in witness["source_solution"]), Fraction()),
            )

    def test_key_misses_exhaust_their_entire_a_one_state_lists(self):
        for prime in (214_729, 878_089):
            states = profile.enumerate_a_eq_1_sources(prime)
            self.assertTrue(states)
            for R, _ in states:
                audit = profile.linear.audit_target_R(prime, R)
                self.assertFalse(audit["target_residue_reachable"])


if __name__ == "__main__":
    unittest.main()
