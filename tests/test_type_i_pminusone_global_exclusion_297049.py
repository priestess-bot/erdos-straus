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
    "type_i_pminusone_global_exclusion_297049",
    ROOT / "reproductions" / "type_i_pminusone_global_exclusion_297049.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIPMinusOneGlobalExclusion297049Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit.run_audit()

    def test_checked_artifact_matches_complete_run(self):
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-I-pminusone-global-exclusion-297049.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.result, expected)

    def test_all_forced_states_and_general_BCH_candidates_are_exhausted(self):
        result = self.result
        states = result["p_minus_one_states"]
        totals = result["candidate_totals"]
        self.assertEqual(
            totals,
            {
                "forced_r_state_count": 27,
                "normalized_square_divisor_candidate_count": 37_557,
                "ordered_BCH_candidate_count": 61_851,
                "reachable_residue_count_sum": 34_222,
                "ordered_residue_hit_count": 0,
                "normalized_residue_hit_count": 0,
                "valid_normal_form_hit_count": 0,
                "orientation_swapped_count": 0,
                "natural_gap_verified_count": 0,
            },
        )
        self.assertEqual(
            [state["r"] for state in states],
            audit.divisors_from_factorization([(2, 1), (3, 1), (12_377, 1)], 2),
        )
        for state in states:
            K = math.prod(
                int(item["prime"]) ** int(item["exponent"])
                for item in state["K_factorization"]
            )
            self.assertEqual(K, state["K"])
            self.assertEqual(4 * K, result["prime"] * state["R"] + 1)
            self.assertEqual(state["R"], 4 * state["r"] - 1)
            self.assertEqual(state["target_residue"], (-state["r"]) % state["R"])
            self.assertFalse(state["target_residue_reachable"])
            self.assertEqual(state["ordered_residue_hit_count"], 0)
            self.assertEqual(state["normalized_residue_hit_count"], 0)
            self.assertEqual(state["valid_normal_form_hit_count"], 0)
            self.assertEqual(state["orientation_swapped_count"], 0)
            self.assertEqual(state["natural_gap_verified_count"], 0)
            self.assertEqual(state["natural_witnesses"], [])

    def test_sympy_small_state_cross_check_exercises_orientation_swap(self):
        prime = 73
        t = (prime - 1) // 4
        r = 1
        R = 4 * r - 1
        K = prime * r - t

        # Deliberately avoid the audit's factor and divisor enumerators here.
        square_divisors = [int(value) for value in sympy.divisors(K * K)]
        square_hits = [
            divisor for divisor in square_divisors if divisor % R == (-r) % R
        ]
        ordered_hits = []
        ordered_count = 0
        for B in map(int, sympy.divisors(K)):
            quotient = K // B
            for C in map(int, sympy.divisors(quotient)):
                H = quotient // C
                ordered_count += 1
                if (B * B * C) % R == (-r) % R:
                    ordered_hits.append((B, C, H, B * B * C))

        self.assertEqual(square_hits, [5, 11, 275, 605])
        self.assertEqual(
            ordered_hits,
            [
                (1, 5, 11, 5),
                (1, 11, 5, 11),
                (5, 11, 1, 275),
                (11, 5, 1, 605),
            ],
        )
        state = audit.audit_pminusone_state(prime, t, r)
        self.assertEqual(
            state["normalized_square_divisor_candidate_count"],
            len(square_divisors),
        )
        self.assertEqual(state["ordered_BCH_candidate_count"], ordered_count)
        self.assertEqual(state["normalized_residue_hit_count"], 4)
        self.assertEqual(state["ordered_residue_hit_count"], 4)
        self.assertEqual(state["valid_normal_form_hit_count"], 4)
        self.assertEqual(state["orientation_swapped_count"], 2)
        self.assertEqual(state["natural_gap_verified_count"], 4)
        self.assertTrue(
            all(
                witness["natural_gap"] and all(witness["conditions"].values())
                for witness in state["natural_witnesses"]
            )
        )

        control = self.result["orientation_swap_positive_control_p73"]
        self.assertEqual(control["matched_square_divisor"], 275)
        self.assertEqual(control["normalized_before_orientation"], [5, 11, 1])
        self.assertTrue(control["orientation_swapped"])
        self.assertEqual(control["normal_form"], [2, 1, 11])
        self.assertEqual(control["H"], 5)
        self.assertEqual(control["gap"], 15)
        self.assertTrue(control["natural_gap"])
        self.assertTrue(all(control["conditions"].values()))

    def test_tail_miss_and_shifted_B1_bridge_replay_exactly(self):
        result = self.result
        tail = result["ordinary_type_ii_p_minus_one_tail"]
        self.assertEqual(tail["witness_count"], 0)
        self.assertEqual(
            tail["eligible_gaps"],
            [3, 7, 11, 23, 49_507, 99_015, 148_523, 297_047],
        )

        shifted = result["shifted_B_eq_1_terminal_bridge"]
        self.assertEqual(
            (
                shifted["shift"],
                shifted["source_denominator"],
                shifted["R"],
                shifted["E"],
                shifted["K"],
                shifted["normal_form"],
                shifted["gap"],
            ),
            (25, 297_024, 19, 476, 1_410_983, [1046, 1, 71], 15),
        )
        certificate = audit.short_certificate.GapCertificate(
            **shifted["target_certificate"]
        )
        self.assertTrue(audit.short_certificate.verify_certificate(certificate))
        self.assertTrue(all(shifted["conditions"].values()))
        self.assertEqual(
            Fraction(4, result["prime"]),
            sum(
                (
                    Fraction(1, denominator)
                    for denominator in shifted["target_solution"]
                ),
                Fraction(),
            ),
        )
        self.assertEqual(
            Fraction(4, shifted["source_denominator"]),
            sum(
                (
                    Fraction(1, denominator)
                    for denominator in shifted["source_solution"]
                ),
                Fraction(),
            ),
        )


if __name__ == "__main__":
    unittest.main()
