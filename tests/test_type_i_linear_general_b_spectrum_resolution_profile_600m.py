from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_general_b_spectrum_resolution_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-linear-general-b-spectrum-resolution-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("linear_general_b_spectrum_resolution", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearGeneralBSpectrumResolutionProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.records = {
            int(record["prime"]): record for record in cls.payload["records"]
        }

    def test_hash_frozen_input_and_reproducible_artifact(self):
        self.assertEqual(self.payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(profile.load_residual(), profile.EXPECTED_RESIDUAL)
        self.assertEqual(
            (
                self.payload["input_residual_count"],
                self.payload["spectrum_resolved_count"],
                self.payload["spectrum_unresolved_count"],
                self.payload["linear_source_coordinate_bound_max"],
                self.payload["linear_R_exhaustively_checked"],
                self.payload["directed_linear_source_state_count"],
                self.payload["K_square_divisors_exhaustively_checked"],
                self.payload["target_divisor_hits"],
                self.payload["target_normal_forms_exhaustively_checked"],
                self.payload["direct_terminal_candidate_count"],
            ),
            (7, 7, 0, 13_378, 278, 490, 340_842, 158, 79, 119),
        )

    def test_every_selected_witness_replays_without_profile_helpers(self):
        for prime, record in self.records.items():
            witness = record["selected_witness"]
            a = int(witness["a"])
            s = int(witness["s"])
            R = int(witness["R"])
            K = int(witness["K"])
            E = int(witness["E"])
            source = int(witness["source_denominator"])
            divisor = int(witness["matched_square_divisor"])
            A = int(witness["A"])
            B = int(witness["B"])
            C = int(witness["C"])
            H = int(witness["H"])
            gap = int(witness["gap"])

            self.assertEqual(prime, a + s + a * s * R)
            self.assertEqual(E, s * R + 1)
            self.assertEqual(source, a * E)
            self.assertGreaterEqual(source, 2)
            self.assertEqual(source % 2, 0)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(4 * K, (a * R + 1) * E)
            self.assertEqual(source, (4 * K - E) // R)
            self.assertEqual((4 * K - E) % R, 0)
            self.assertEqual(E % R, 1)
            self.assertEqual((4 * K * K) % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)

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
            self.assertTrue(all(witness["conditions"].values()))

    def test_direct_divisor_oracle_recovers_every_target_hit_R(self):
        expected_hit_Rs = {
            214_729: [39, 131, 203],
            878_089: [59],
            2_210_569: [23, 39, 391],
            13_782_409: [131],
            64_214_329: [19, 43, 119, 131],
            105_295_129: [15, 35, 119, 143],
            536_944_489: [19, 23, 47, 51],
        }
        for prime, record in self.records.items():
            _, states_by_R = profile.sources.enumerate_linear_source_states(prime)
            direct_hit_Rs = []
            direct_hit_count = 0
            for R in states_by_R:
                K = (prime * R + 1) // 4
                divisors = [
                    int(divisor)
                    for divisor in sympy.divisors(K * K)
                    if (4 * int(divisor) + 1) % R == 0
                ]
                if divisors:
                    direct_hit_Rs.append(R)
                    direct_hit_count += len(divisors)
            self.assertEqual(direct_hit_Rs, expected_hit_Rs[prime])
            self.assertEqual(direct_hit_count, record["target_divisor_hits"])


if __name__ == "__main__":
    unittest.main()
