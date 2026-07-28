import importlib.util
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_box_miss_global_audit_500m",
    ROOT / "reproductions" / "type_i_pminusone_box_miss_global_audit_500m.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


EXPECTED_GLOBAL_MISSES = [
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


def factorization_product(payload):
    return math.prod(int(item["prime"]) ** int(item["exponent"]) for item in payload)


class TypeIPMinusOneBoxMissGlobalAudit500MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-pminusone-box-miss-global-audit-500m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.result, self.expected)

    def test_hash_frozen_input_and_exact_partition(self):
        source, source_primes = audit.load_authoritative_primes()
        result = self.result
        captured = result["captured_records"]
        misses = result["global_miss_records"]
        captured_primes = [int(record["prime"]) for record in captured]
        miss_primes = [int(record["prime"]) for record in misses]

        self.assertEqual(len(source_primes), 185)
        self.assertEqual(
            audit.integer_list_sha256(source_primes),
            audit.EXPECTED_INPUT_PRIME_LIST_SHA256,
        )
        self.assertEqual(
            result["input"]["prime_list_sha256"], audit.EXPECTED_INPUT_PRIME_LIST_SHA256
        )
        self.assertEqual(source["p_minus_one_misses"], source_primes)
        self.assertEqual(miss_primes, EXPECTED_GLOBAL_MISSES)
        self.assertEqual(len(captured_primes), 164)
        self.assertEqual(len(miss_primes), 21)
        self.assertFalse(set(captured_primes) & set(miss_primes))
        self.assertEqual(set(captured_primes) | set(miss_primes), set(source_primes))

        totals = result["totals"]
        self.assertEqual(totals["input_box_miss_count"], 185)
        self.assertEqual(totals["forced_r_state_count"], 15_411)
        self.assertEqual(totals["states_checked"], 15_411)
        self.assertEqual(totals["square_divisor_candidate_count"], 112_657_233)
        self.assertEqual(totals["ordered_BCH_candidate_count"], 178_245_405)
        self.assertEqual(totals["mitm_candidate_entry_count"], 1_417_964)
        self.assertEqual(totals["target_reachable_state_count"], 511)
        self.assertEqual(totals["p_minus_one_captured_count"], 164)
        self.assertEqual(totals["global_p_minus_one_miss_count"], 21)
        self.assertEqual(totals["natural_gap_verified_count"], 164)

    def test_all_164_stored_witnesses_replay_exactly(self):
        for record in self.result["captured_records"]:
            prime = int(record["prime"])
            t = int(record["t"])
            t_factors = audit.parse_factorization(record["t_factorization"])
            witness = record["selected_p_minus_one_witness"]
            A, B, C = (int(value) for value in witness["normal_form"])
            initial_B, initial_C, initial_H = (
                int(value) for value in witness["normalized_before_orientation"]
            )
            H = int(witness["H"])
            R = int(witness["R"])
            K = int(witness["K"])
            r = int(witness["r"])
            gap = int(witness["gap"])
            matched = int(witness["matched_square_divisor"])

            self.assertEqual(t, (prime - 1) // 4)
            self.assertEqual(math.prod(q**e for q, e in t_factors), t)
            self.assertEqual(
                record["forced_r_state_count"],
                math.prod(2 * exponent + 1 for _, exponent in t_factors),
            )
            self.assertEqual(record["states_checked"], record["forced_r_state_count"])
            self.assertGreater(record["target_reachable_state_count"], 0)
            self.assertEqual(R, 4 * r - 1)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(int(witness["E"]), R + 1)
            self.assertEqual(int(witness["source_denominator"]), prime - 1)
            self.assertEqual(initial_C, C)
            self.assertEqual(initial_B * C * initial_H, K)
            self.assertEqual(initial_B * initial_B * C, matched)
            self.assertEqual(math.gcd(initial_B, initial_H), 1)

            if witness["orientation_swapped"]:
                self.assertEqual((B, H), (initial_H, initial_B))
            else:
                self.assertEqual((B, H), (initial_B, initial_H))
            self.assertGreater(H, B)
            self.assertEqual(A * R, B + H)
            self.assertEqual(math.gcd(A, B), 1)
            self.assertEqual(B * C * H, K)
            self.assertEqual(4 * A * B * C - gap, prime)
            self.assertEqual(gap % 4, 3)
            self.assertLessEqual(3, gap)
            self.assertLessEqual(gap, prime - 2)
            self.assertTrue(all(witness["conditions"].values()))
            self.assertEqual(
                Fraction(4, prime),
                sum(
                    (
                        Fraction(1, denominator)
                        for denominator in witness["target_solution"]
                    ),
                    Fraction(),
                ),
            )
            self.assertEqual(
                Fraction(4, prime - 1),
                sum(
                    (
                        Fraction(1, denominator)
                        for denominator in witness["source_solution"]
                    ),
                    Fraction(),
                ),
            )

    def test_all_21_global_misses_have_complete_replayable_state_absence(self):
        total_miss_states = 0
        for record in self.result["global_miss_records"]:
            prime = int(record["prime"])
            t_factors = audit.parse_factorization(record["t_factorization"])
            expected_r_values = audit.divisors_from_factorization(t_factors, 2)
            states = record["p_minus_one_states"]
            total_miss_states += len(states)

            self.assertEqual([int(state["r"]) for state in states], expected_r_values)
            self.assertEqual(len(states), record["forced_r_state_count"])
            self.assertEqual(len(states), record["states_checked"])
            self.assertEqual(record["target_reachable_state_count"], 0)
            self.assertEqual(
                record["all_state_summaries_sha256"],
                audit.canonical_json_sha256(states),
            )

            for state in states:
                r = int(state["r"])
                R = int(state["R"])
                K = int(state["K"])
                mitm = state["mitm"]
                left_factors = audit.parse_factorization(mitm["left_factorization"])
                right_factors = audit.parse_factorization(mitm["right_factorization"])
                K_factors = audit.parse_factorization(state["K_factorization"])
                left_divisors = audit.divisors_from_factorization(left_factors, 2)
                right_divisors = audit.divisors_from_factorization(right_factors, 2)
                right_residues = {divisor % R for divisor in right_divisors}
                required_residues = {
                    int(state["target_residue"]) * pow(divisor, -1, R) % R
                    for divisor in left_divisors
                }

                self.assertEqual(r * 4 - 1, R)
                self.assertEqual(4 * K, prime * R + 1)
                self.assertEqual(factorization_product(state["K_factorization"]), K)
                self.assertEqual(
                    factorization_product(state["known_factor_block_factorization"]),
                    state["known_factor_block"],
                )
                self.assertEqual(
                    factorization_product(state["affine_factorization"]),
                    state["affine_factor"],
                )
                self.assertEqual(
                    state["known_factor_block"] * state["affine_factor"], K
                )
                self.assertEqual(
                    state["square_divisor_candidate_count"],
                    math.prod(2 * exponent + 1 for _, exponent in K_factors),
                )
                self.assertFalse(state["target_residue_reachable"])
                self.assertIsNone(state["matched_square_divisor"])
                self.assertFalse(right_residues & required_residues)
                self.assertEqual(mitm["residue_intersection_count"], 0)
                self.assertEqual(
                    mitm["right_residue_sha256"],
                    audit.integer_list_sha256(sorted(right_residues)),
                )
                self.assertEqual(
                    mitm["required_right_residue_sha256"],
                    audit.integer_list_sha256(sorted(required_residues)),
                )
        self.assertEqual(total_miss_states, 1_323)

    def test_orientation_swap_preserves_the_certificate_and_naturalizes_gap(self):
        record = self.result["captured_records"][0]
        witness = record["selected_p_minus_one_witness"]
        prime = int(record["prime"])
        t = int(record["t"])
        A, B, C = (int(value) for value in witness["normal_form"])
        H = int(witness["H"])
        reverse_divisor = H * H * C
        swapped = audit.build_natural_witness(
            prime,
            t,
            int(witness["r"]),
            int(witness["R"]),
            int(witness["K"]),
            reverse_divisor,
        )

        self.assertTrue(swapped["orientation_swapped"])
        self.assertEqual(swapped["normal_form"], [A, B, C])
        self.assertEqual(swapped["H"], H)
        self.assertEqual(swapped["gap"], witness["gap"])
        self.assertEqual(swapped["target_solution"], witness["target_solution"])
        self.assertEqual(swapped["source_solution"], witness["source_solution"])
        self.assertTrue(all(swapped["conditions"].values()))


if __name__ == "__main__":
    unittest.main()
