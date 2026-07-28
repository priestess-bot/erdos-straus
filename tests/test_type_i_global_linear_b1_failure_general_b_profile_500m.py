import importlib.util
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
import unittest

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_global_linear_b1_failure_general_b_profile_500m",
    ROOT
    / "reproductions"
    / "type_i_global_linear_b1_failure_general_b_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def factorization_product(payload):
    return math.prod(int(item["prime"]) ** int(item["exponent"]) for item in payload)


def oracle_linear_source_states(prime):
    """Recover directed linear sources through two distinct divisor channels."""
    states_by_R = {}
    bound = math.isqrt((prime - 2) // 3)
    for least_coordinate in range(1, bound + 1):
        # Channel one makes a the least coordinate and enumerates odd s.
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
                states_by_R.setdefault(R, set()).add((a, s))

        # Channel two makes the odd s the least coordinate and enumerates a.
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
                    states_by_R.setdefault(R, set()).add((a, s))

    result = {R: sorted(states) for R, states in sorted(states_by_R.items())}
    for R, states in result.items():
        for a, s in states:
            if (
                prime != a + s + a * s * R
                or s % 2 != 1
                or prime - s != a * (s * R + 1)
                or min(a, s) > bound
            ):
                raise AssertionError("independent source oracle found a bad state")
    return result


def direct_generated_subgroup(modulus, generators):
    """Small-modulus BFS oracle independent from component coordinates."""
    reached = {1 % modulus}
    pending = [1 % modulus]
    while pending:
        residue = pending.pop()
        for generator in generators:
            next_residue = residue * generator % modulus
            if next_residue not in reached:
                reached.add(next_residue)
                pending.append(next_residue)
    return reached


def independent_component_membership(factors, modulus):
    """Reconstruct the finite unit-group membership test from raw arithmetic."""
    R_factors = sorted((int(p), int(e)) for p, e in sympy.factorint(modulus).items())
    components = [p**e for p, e in R_factors]
    orders = [int(sympy.totient(component)) for component in components]
    roots = [int(sympy.primitive_root(component)) for component in components]
    generator_vectors = [
        [
            int(sympy.discrete_log(component, prime % component, root))
            for component, root in zip(components, roots)
        ]
        for prime in factors
    ]
    dimension = len(components)
    columns = [*generator_vectors]
    columns.extend(
        [
            [orders[row] if row == column else 0 for row in range(dimension)]
            for column in range(dimension)
        ]
    )
    lattice = Matrix(
        dimension,
        len(columns),
        lambda row, column: columns[column][row],
    )
    hnf = hermite_normal_form(lattice)
    target = Matrix([order // 2 for order in orders])
    coordinates = hnf.inv() * target
    return (
        all(value.q == 1 for value in coordinates),
        [
            [int(hnf[row, column]) for column in range(dimension)]
            for row in range(dimension)
        ],
        [int(value) for value in coordinates]
        if all(value.q == 1 for value in coordinates)
        else None,
    )


class TypeIGlobalLinearB1FailureGeneralBProfile500MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        cls.b1_records = {
            int(record["prime"]): record for record in cls.actual["B_eq_1_records"]
        }
        cls.general_profiles = {
            int(record["prime"]): record
            for record in cls.actual["general_B_failure_profiles"]
        }

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["input_sha256"], profile.EXPECTED_INPUT_SHA256)

    def test_hash_frozen_input_and_exact_global_partition(self):
        primes = profile.load_global_p_minus_one_misses()
        self.assertEqual(len(primes), 21)
        self.assertEqual(
            profile.integer_list_sha256(primes),
            profile.EXPECTED_GLOBAL_MISS_PRIME_LIST_SHA256,
        )
        self.assertEqual(self.actual["B_eq_1_totals"], profile.EXPECTED_B1_TOTALS)
        self.assertEqual(
            self.actual["global_linear_B_eq_1_failure_primes"],
            profile.EXPECTED_B1_FAILURE_PRIMES,
        )
        self.assertEqual(
            self.actual["aggregate_general_B_classification_counts"],
            {"hit": 12, "finite_exponent": 53, "subgroup_character": 126},
        )

    def test_B1_boundary_samples_use_independent_two_channel_enumeration(self):
        required = {
            297_049,
            405_660_649,
            *profile.EXPECTED_B1_FAILURE_PRIMES,
        }
        for prime in sorted(required):
            record = self.b1_records[prime]
            with self.subTest(prime=prime):
                states_by_R = oracle_linear_source_states(prime)
                payload = profile.source_state_payload(states_by_R)
                self.assertEqual(
                    int(record["theoretical_u_bound"]),
                    math.isqrt((prime - 2) // 3),
                )
                self.assertEqual(
                    int(record["directed_linear_source_state_count"]),
                    sum(len(states) for states in states_by_R.values()),
                )
                self.assertEqual(int(record["distinct_R_count"]), len(states_by_R))
                self.assertEqual(
                    record["linear_source_states_sha256"],
                    profile.canonical_json_sha256(payload),
                )
                direct_hits = []
                for R, states in states_by_R.items():
                    K = (prime * R + 1) // 4
                    matches = [
                        int(divisor)
                        for divisor in sympy.divisors(K)
                        if (4 * int(divisor) + 1) % R == 0
                    ]
                    if matches:
                        direct_hits.append((R, min(matches), states))
                stored_hits = record["B_eq_1_hits"]
                self.assertEqual(len(stored_hits), len(direct_hits))
                self.assertEqual(
                    [
                        (int(hit["R"]), int(hit["least_B_eq_1_divisor"]))
                        for hit in stored_hits
                    ],
                    [(R, divisor) for R, divisor, _ in direct_hits],
                )
                for stored, (_, _, states) in zip(stored_hits, direct_hits):
                    a, s = (int(value) for value in stored["selected_source_state"])
                    self.assertIn((a, s), states)

    def test_every_B1_witness_replays_with_exact_fractions(self):
        for record in self.b1_records.values():
            prime = int(record["prime"])
            for hit in record["B_eq_1_hits"]:
                witness = hit["witness"]
                A, B, C = (int(value) for value in witness["normal_form"])
                H = int(witness["H"])
                R = int(witness["R"])
                K = int(witness["K"])
                E = int(witness["E"])
                source = int(witness["source_denominator"])
                a, s = int(witness["a"]), int(witness["s"])
                self.assertEqual(B, 1)
                self.assertEqual(prime, a + s + a * s * R)
                self.assertEqual(source, a * E)
                self.assertEqual(K, (prime * R + 1) // 4)
                self.assertEqual(A * R, B + H)
                self.assertEqual(B * C * H, K)
                self.assertEqual((4 * B * B * C + 1) // R, witness["gap"])
                self.assertTrue(all(witness["conditions"].values()))
                self.assertEqual(
                    Fraction(4, prime),
                    sum(
                        (
                            Fraction(1, int(value))
                            for value in witness["target_solution"]
                        ),
                        Fraction(),
                    ),
                )
                self.assertEqual(
                    Fraction(4, source),
                    sum(
                        (
                            Fraction(1, int(value))
                            for value in witness["source_solution"]
                        ),
                        Fraction(),
                    ),
                )

    def test_general_B_profiles_are_directly_complete_and_component_certified(self):
        for prime, prime_profile in self.general_profiles.items():
            oracle_states = oracle_linear_source_states(prime)
            records = prime_profile["records"]
            with self.subTest(prime=prime):
                self.assertEqual(
                    [int(record["R"]) for record in records], list(oracle_states)
                )
            for record in records:
                R = int(record["R"])
                with self.subTest(prime=prime, R=R):
                    K = (prime * R + 1) // 4
                    factors = sympy.factorint(K)
                    square_divisors = [int(value) for value in sympy.divisors(K * K)]
                    matches = [
                        value for value in square_divisors if value % R == (-K) % R
                    ]
                    centered = {value * pow(K, -1, R) % R for value in square_divisors}
                    self.assertEqual(
                        factorization_product(record["K_factorization"]), K
                    )
                    self.assertEqual(
                        int(record["square_divisor_count"]), len(square_divisors)
                    )
                    self.assertEqual(
                        int(record["centered_spectrum_residue_count"]), len(centered)
                    )
                    self.assertEqual(
                        bool(matches), bool(record["minus_one_in_centered_spectrum"])
                    )
                    self.assertEqual(
                        min(matches) if matches else None,
                        record["least_matching_square_divisor"],
                    )
                    self.assertFalse(
                        any(
                            (4 * int(value) + 1) % R == 0 for value in sympy.divisors(K)
                        )
                    )

                    subgroup = record["unit_group_subgroup_certificate"]
                    target_in_group, hnf, coordinates = (
                        independent_component_membership(
                            sorted(int(q) for q in factors), R
                        )
                    )
                    self.assertEqual(
                        subgroup["column_lattice_hermite_normal_form"], hnf
                    )
                    self.assertEqual(
                        subgroup["target_in_generated_subgroup"], target_in_group
                    )
                    self.assertEqual(
                        subgroup["target_lattice_coordinates"], coordinates
                    )
                    expected_class = (
                        "hit"
                        if matches
                        else "finite_exponent"
                        if target_in_group
                        else "subgroup_character"
                    )
                    self.assertEqual(record["classification"], expected_class)
                    self.assertEqual(
                        record["source_states"],
                        [[a, s] for a, s in oracle_states[R]],
                    )

                    # This direct closure is independent of component logs and HNF.
                    if R <= 10_000:
                        generated = direct_generated_subgroup(R, factors)
                        self.assertEqual((R - 1) in generated, target_in_group)

    def test_selected_general_B_witnesses_are_non_B1_and_replay(self):
        for prime, record in self.general_profiles.items():
            witness = record["selected_general_B_witness"]
            A, B, C = (int(value) for value in witness["normal_form"])
            H = int(witness["H"])
            R = int(witness["R"])
            K = int(witness["K"])
            source = int(witness["source_denominator"])
            self.assertGreater(B, 1)
            self.assertEqual(A * R, B + H)
            self.assertEqual(B * C * H, K)
            self.assertEqual(prime, 4 * A * B * C - int(witness["gap"]))
            self.assertTrue(all(witness["conditions"].values()))
            self.assertEqual(
                Fraction(4, prime),
                sum(
                    (Fraction(1, int(value)) for value in witness["target_solution"]),
                    Fraction(),
                ),
            )
            self.assertEqual(
                Fraction(4, source),
                sum(
                    (Fraction(1, int(value)) for value in witness["source_solution"]),
                    Fraction(),
                ),
            )


if __name__ == "__main__":
    unittest.main()
