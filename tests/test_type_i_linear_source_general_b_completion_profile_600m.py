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
    "type_i_linear_source_general_b_completion_profile_600m",
    ROOT
    / "reproductions"
    / "type_i_linear_source_general_b_completion_profile_600m.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


GLOBAL_P_MINUS_ONE_MISSES = [
    297_049,
    3_942_409,
    13_782_409,
    36_583_369,
    40_944_649,
    62_588_089,
    64_214_329,
    72_148_729,
    96_530_569,
    171_292_489,
    222_416_329,
    257_483_209,
    259_423_609,
    297_640_249,
    319_207_849,
    335_420_089,
    357_834_409,
    401_991_529,
    405_660_649,
    459_147_049,
    477_015_289,
]
B1_LINEAR_FAILURES_AMONG_GLOBAL_P_MINUS_ONE_MISSES = {
    3_942_409,
    62_588_089,
    297_640_249,
    477_015_289,
}


def factorization_product(payload):
    return math.prod(int(item["prime"]) ** int(item["exponent"]) for item in payload)


def oracle_directed_states_at_u(prime, least_coordinate):
    """Recover sources through two directed divisor channels."""
    states = set()

    # Channel 1 fixes the smaller a and enumerates odd s|(p-a).
    a = least_coordinate
    for s in sympy.divisors(prime - a):
        s = int(s)
        if s < least_coordinate or s % 2 == 0:
            continue
        quotient = (prime - a) // s
        if (quotient - 1) % a:
            continue
        R = (quotient - 1) // a
        if R >= 3 and R % 4 == 3:
            states.add((a, s, R))

    # Channel 2 fixes the smaller odd s and enumerates a|(p-s).
    s = least_coordinate
    if s % 2:
        for a in sympy.divisors(prime - s):
            a = int(a)
            if a < least_coordinate:
                continue
            quotient = (prime - s) // a
            if (quotient - 1) % s:
                continue
            R = (quotient - 1) // s
            if R >= 3 and R % 4 == 3:
                states.add((a, s, R))

    for a, s, R in states:
        if min(a, s) != least_coordinate or prime != a + s + a * s * R:
            raise AssertionError("independent source oracle recovered bad state")
    return states


def oracle_target_divisors(prime, R):
    """Directly enumerate K^2 divisors without using the production MITM."""
    K = (prime * R + 1) // 4
    return [
        int(divisor)
        for divisor in sympy.divisors(K * K)
        if (4 * int(divisor) + 1) % R == 0
    ]


class TypeILinearSourceGeneralBCompletionProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-source-general-b-completion-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        cls.records = {
            int(record["prime"]): record for record in cls.result["captured_records"]
        }
        _, _, first_primes, second_primes = audit.load_authoritative_primes()
        cls.combined_primes = [*first_primes, *second_primes]

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.result, self.expected)

    def test_hash_frozen_disjoint_inputs_and_exact_totals(self):
        _, _, first_primes, second_primes = audit.load_authoritative_primes()
        self.assertEqual(len(first_primes), 1_717)
        self.assertEqual(len(second_primes), 247)
        self.assertFalse(set(first_primes) & set(second_primes))
        self.assertEqual(
            audit.integer_list_sha256(first_primes),
            audit.EXPECTED_INPUT_500M_PRIME_LIST_SHA256,
        )
        self.assertEqual(
            audit.integer_list_sha256(second_primes),
            audit.EXPECTED_INPUT_500M_600M_PRIME_LIST_SHA256,
        )
        self.assertEqual(
            audit.integer_list_sha256([*first_primes, *second_primes]),
            audit.EXPECTED_COMBINED_PRIME_LIST_SHA256,
        )
        self.assertEqual(self.result["totals"], audit.EXPECTED_TOTALS)
        self.assertEqual(self.result["failure_primes"], [])
        self.assertEqual(self.result["failure_records"], [])
        self.assertEqual(
            self.result["maxima"]["least_coordinate_u"],
            {"value": 587, "prime": 283_319_689},
        )

    def test_all_1964_witnesses_replay_independently_with_fractions(self):
        self.assertEqual(list(self.records), self.combined_primes)
        tuples = []
        for prime, record in self.records.items():
            witness = record["selected_witness"]
            target_audit = record["selected_R_audit"]
            a = int(witness["a"])
            s = int(witness["s"])
            R = int(witness["R"])
            E = int(witness["E"])
            source = int(witness["source_denominator"])
            K = int(witness["K"])
            matched = int(witness["matched_square_divisor"])
            A = int(witness["A"])
            B = int(witness["B"])
            C = int(witness["C"])
            H = int(witness["H"])
            gap = int(witness["gap"])

            self.assertEqual(prime, a + s + a * s * R)
            self.assertEqual(min(a, s), witness["least_coordinate_u"])
            self.assertEqual(E, s * R + 1)
            self.assertEqual(source, prime - s)
            self.assertEqual(source, a * E)
            self.assertEqual(source % 2, 0)
            self.assertGreaterEqual(4 * source, 3 * prime + 1)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(K, factorization_product(target_audit["K_factorization"]))
            self.assertEqual(K * K % matched, 0)
            self.assertEqual((4 * matched + 1) % R, 0)

            common = math.gcd(matched, K)
            initial_B = matched // common
            initial_C = common * common // matched
            initial_H = K // common
            self.assertEqual(
                witness["normalized_before_orientation"],
                [initial_B, initial_C, initial_H],
            )
            if initial_H < initial_B:
                self.assertEqual((B, H), (initial_H, initial_B))
            else:
                self.assertEqual((B, H), (initial_B, initial_H))
            self.assertEqual(C, initial_C)
            self.assertEqual(B * C * H, K)
            self.assertEqual(math.gcd(B, H), 1)
            self.assertGreater(H, B)
            self.assertEqual(A * R, B + H)
            self.assertEqual(math.gcd(A, B), 1)
            self.assertEqual(gap * R, 4 * B * B * C + 1)
            self.assertEqual(gap % 4, 3)
            self.assertLessEqual(3, gap)
            self.assertLessEqual(gap, prime - 2)
            self.assertEqual(prime, 4 * A * B * C - gap)
            self.assertEqual(witness["source_normalization"]["beta"], 1)
            self.assertTrue(all(witness["conditions"].values()))

            target_solution = [int(value) for value in witness["target_solution"]]
            source_solution = [int(value) for value in witness["source_solution"]]
            self.assertEqual(
                Fraction(4, prime),
                sum(
                    (Fraction(1, value) for value in target_solution),
                    Fraction(),
                ),
            )
            self.assertEqual(
                Fraction(4, source),
                sum(
                    (Fraction(1, value) for value in source_solution),
                    Fraction(),
                ),
            )
            tuples.append(audit.selected_witness_tuple(record))

        self.assertEqual(
            audit.canonical_json_sha256(tuples),
            audit.EXPECTED_SELECTED_WITNESS_TUPLES_SHA256,
        )

    def test_selected_R_mitm_summaries_represent_complete_products(self):
        for record in self.result["captured_records"]:
            state = record["selected_R_audit"]
            R = int(state["R"])
            matched = int(state["matched_square_divisor"])
            left_factors = audit.parse_factorization(
                state["mitm"]["left_factorization"]
            )
            right_factors = audit.parse_factorization(
                state["mitm"]["right_factorization"]
            )
            left = audit.divisors_from_factorization(left_factors, 2)
            right = audit.divisors_from_factorization(right_factors, 2)
            target = int(state["target_residue"])
            attained = {value % R for value in right}
            required = {target * pow(value, -1, R) % R for value in left}
            direct_min = min(
                left_value * right_value
                for left_value in left
                for right_value in right
                if left_value * right_value % R == target
            )
            self.assertEqual(matched, direct_min)
            self.assertEqual(
                state["mitm"]["residue_intersection_count"],
                len(attained & required),
            )
            self.assertGreater(len(attained & required), 0)

    def test_independent_direct_oracle_on_required_pressure_points(self):
        required = {
            878_089,
            283_319_689,
            *self.combined_primes[:13],
            *GLOBAL_P_MINUS_ONE_MISSES,
        }
        for prime in sorted(required):
            record = self.records[prime]
            witness = record["selected_witness"]
            selected_u = int(witness["least_coordinate_u"])
            selected_state = (
                int(witness["a"]),
                int(witness["s"]),
                int(witness["R"]),
            )
            target_cache = {}
            hits_at_selected_u = []
            for u in range(1, selected_u + 1):
                states = oracle_directed_states_at_u(prime, u)
                hits = []
                for a, s, R in states:
                    target_cache.setdefault(R, oracle_target_divisors(prime, R))
                    if target_cache[R]:
                        hits.append((a, s, R))
                if u < selected_u:
                    self.assertEqual(hits, [], (prime, u))
                else:
                    hits_at_selected_u = hits
            self.assertIn(selected_state, hits_at_selected_u)
            selected_R = selected_state[2]
            self.assertEqual(
                int(witness["matched_square_divisor"]),
                min(target_cache[selected_R]),
            )

    def test_878089_has_no_B1_linear_hit_but_has_general_B_hit(self):
        prime = 878_089
        bound = math.isqrt((prime - 2) // 3)
        all_states = set()
        for u in range(1, bound + 1):
            all_states.update(oracle_directed_states_at_u(prime, u))
        all_R = {R for _, _, R in all_states}
        self.assertEqual(len(all_states), 54)
        self.assertEqual(len(all_R), 24)
        for R in all_R:
            K = (prime * R + 1) // 4
            self.assertFalse(
                any((4 * int(divisor) + 1) % R == 0 for divisor in sympy.divisors(K))
            )
        self.assertGreater(self.records[prime]["selected_witness"]["B"], 1)

    def test_four_linear_B1_failures_are_captured_by_general_B(self):
        for prime in B1_LINEAR_FAILURES_AMONG_GLOBAL_P_MINUS_ONE_MISSES:
            with self.subTest(prime=prime):
                bound = math.isqrt((prime - 2) // 3)
                all_R = set()
                for u in range(1, bound + 1):
                    all_R.update(R for _, _, R in oracle_directed_states_at_u(prime, u))
                self.assertGreater(len(all_R), 0)
                for R in all_R:
                    K = (prime * R + 1) // 4
                    self.assertFalse(
                        any(
                            (4 * int(divisor) + 1) % R == 0
                            for divisor in sympy.divisors(K)
                        )
                    )
                self.assertGreater(self.records[prime]["selected_witness"]["B"], 1)


if __name__ == "__main__":
    unittest.main()
