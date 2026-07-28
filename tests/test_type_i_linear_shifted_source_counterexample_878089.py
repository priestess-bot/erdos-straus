import importlib.util
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_shifted_source_counterexample_878089",
    ROOT / "reproductions" / "type_i_linear_shifted_source_counterexample_878089.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def direct_shift_oracle(prime):
    """Scan every admissible odd s and every E|(p-s), without sqrt symmetry."""
    spf = audit.short_certificate.smallest_prime_factors(prime)
    states = set()
    for shift in range(1, (prime - 1) // 2 + 1, 2):
        source = prime - shift
        for bridge in audit.short_certificate.positive_divisors_from_spf(source, spf):
            if (bridge - 1) % shift:
                continue
            R = (bridge - 1) // shift
            if R < 3 or R % 4 != 3:
                continue
            a = source // bridge
            if prime != a + shift + a * shift * R:
                raise AssertionError("direct shift oracle did not reconstruct p")
            states.add((a, shift, R, bridge, source))
    return states


class TypeILinearShiftedSourceCounterexample878089Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit.run_audit()

    def test_checked_artifact_matches_complete_run(self):
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-I-linear-shifted-source-counterexample-878089.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.result, expected)

    def test_direct_s_scan_independently_recovers_all_54_states(self):
        prime = self.result["prime"]
        direct = direct_shift_oracle(prime)
        square_root_states = {
            (
                int(state["a"]),
                int(state["s"]),
                int(state["R"]),
                int(state["E"]),
                int(state["n"]),
            )
            for state in self.result["oriented_linear_source_states"]
        }
        self.assertEqual(len(range(1, (prime - 1) // 2 + 1, 2)), 219_522)
        self.assertEqual(len(direct), 54)
        self.assertEqual(direct, square_root_states)
        self.assertEqual(
            self.result["candidate_totals"]["unordered_parameter_pair_count"],
            42,
        )
        self.assertEqual(
            self.result["candidate_totals"]["distinct_R_count"],
            24,
        )

    def test_every_target_factorization_exhausts_the_missing_residue(self):
        prime = self.result["prime"]
        divisor_total = 0
        residue_total = 0
        for target in self.result["target_modulus_audits"]:
            R = int(target["R"])
            K = int(target["K"])
            factors = {
                int(item["prime"]): int(item["exponent"])
                for item in target["K_factorization"]
            }
            self.assertEqual(math.prod(q**e for q, e in factors.items()), K)
            self.assertTrue(all(sympy.isprime(q) for q in factors))
            self.assertEqual(4 * K, prime * R + 1)
            divisors = [int(divisor) for divisor in sympy.divisors(K)]
            residues = sorted({divisor % R for divisor in divisors})
            target_C = (-pow(4, -1, R)) % R
            self.assertEqual(residues, target["reachable_divisor_residues"])
            self.assertNotIn(target_C, residues)
            self.assertNotIn(R - 1, residues)
            self.assertFalse(target["target_reachable"])
            self.assertEqual(target["target_C_hit_count"], 0)
            self.assertEqual(target["target_H_hit_count"], 0)
            divisor_total += len(divisors)
            residue_total += len(residues)
        self.assertEqual(divisor_total, 1_655)
        self.assertEqual(residue_total, 1_244)

    def test_target_is_first_failure_in_the_stored_tail_miss_prefix(self):
        prefix = self.result["ordinary_type_ii_tail_and_stored_prefix"]
        self.assertEqual(
            prefix["stored_miss_prefix_primes"],
            [
                67_369,
                85_369,
                163_249,
                214_729,
                225_289,
                297_049,
                372_409,
                454_969,
                521_929,
                532_249,
                629_689,
                784_249,
                852_889,
                878_089,
            ],
        )
        self.assertEqual(prefix["smaller_stored_miss_count"], 13)
        self.assertEqual(len(prefix["smaller_linear_B_eq_1_witnesses"]), 13)
        self.assertTrue(
            prefix["target_is_first_strict_linear_failure_in_stored_prefix"]
        )
        for witness in prefix["smaller_linear_B_eq_1_witnesses"]:
            self.assertEqual(witness["n"], witness["a"] * witness["E"])
            self.assertEqual(
                witness["prime"],
                witness["a"]
                + witness["s"]
                + witness["a"] * witness["s"] * witness["R"],
            )
            self.assertEqual((4 * witness["C"] + 1) % witness["R"], 0)

    def test_ordinary_tail_miss_and_nonlinear_B1_bridge_replay(self):
        prime = self.result["prime"]
        tail = self.result["ordinary_type_ii_tail_and_stored_prefix"]
        self.assertEqual(tail["ordinary_type_ii_tail_witness_count"], 0)
        self.assertEqual(
            tail["eligible_gaps"],
            [3, 7, 11, 23, 146_347, 292_695, 439_043, 878_087],
        )

        bridge = self.result["successful_nonlinear_upper_B_eq_1_bridge"]
        self.assertEqual(
            (
                bridge["shift"],
                bridge["source_denominator"],
                bridge["R"],
                bridge["E"],
                bridge["K"],
                bridge["normal_form"],
                bridge["gap"],
            ),
            (2_065, 876_024, 83, 171_396, 18_220_347, [74, 1, 2_967], 143),
        )
        self.assertEqual(bridge["E_mod_n_remainder"], 19_044)
        self.assertEqual(
            bridge["source_normalization"],
            {
                "lambda": 4,
                "u": 219_006,
                "D": 42_849,
                "g": 4_761,
                "alpha": 46,
                "beta": 9,
                "gamma": 529,
                "eta": 1,
                "L": 3_827,
            },
        )
        self.assertTrue(all(bridge["conditions"].values()))
        certificate = audit.short_certificate.GapCertificate(
            **bridge["target_certificate"]
        )
        self.assertTrue(audit.short_certificate.verify_certificate(certificate))
        self.assertEqual(
            Fraction(4, prime),
            sum(
                (Fraction(1, denominator) for denominator in bridge["target_solution"]),
                Fraction(),
            ),
        )
        self.assertEqual(
            Fraction(4, bridge["source_denominator"]),
            sum(
                (Fraction(1, denominator) for denominator in bridge["source_solution"]),
                Fraction(),
            ),
        )

    def test_general_B_linear_positive_control_replays_exactly(self):
        prime = self.result["prime"]
        bridge = self.result["successful_general_B_linear_bridge"]
        self.assertEqual(
            (
                bridge["a"],
                bridge["shift"],
                bridge["source_denominator"],
                bridge["R"],
                bridge["E"],
                bridge["K"],
                bridge["normal_form"],
                bridge["H"],
                bridge["gap"],
                bridge["square_divisor"],
            ),
            (
                4,
                3_705,
                874_384,
                59,
                218_596,
                12_951_813,
                [2, 7, 16_669],
                111,
                55_375,
                816_781,
            ),
        )
        self.assertEqual(bridge["source_normalization"]["beta"], 1)
        self.assertTrue(all(bridge["conditions"].values()))
        certificate = audit.short_certificate.GapCertificate(
            **bridge["target_certificate"]
        )
        self.assertTrue(audit.short_certificate.verify_certificate(certificate))
        self.assertEqual(
            Fraction(4, prime),
            sum(
                (Fraction(1, denominator) for denominator in bridge["target_solution"]),
                Fraction(),
            ),
        )
        self.assertEqual(
            Fraction(4, bridge["source_denominator"]),
            sum(
                (Fraction(1, denominator) for denominator in bridge["source_solution"]),
                Fraction(),
            ),
        )


if __name__ == "__main__":
    unittest.main()
