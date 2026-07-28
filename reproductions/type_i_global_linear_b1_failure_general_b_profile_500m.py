#!/usr/bin/env python3
"""Profile all linear sources on the 21 global p-1 terminal-bridge misses.

The hash-frozen p-1 audit leaves 21 primes for which no maximum-tail bridge
with source p-1 exists in any Type I normal form.  This program completely
enumerates their linear shifted sources E | n, decides the B=1 target divisor
at every induced R, and then gives a full general-B centered-spectrum profile
for the four primes on which every linear B=1 state fails.

For large R, subgroup membership is decided in a product of cyclic unit-group
components with an integer Hermite normal form.  This avoids materializing a
possibly enormous subgroup while retaining an exact finite certificate.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT / "reproductions" / "type-i-pminusone-box-miss-global-audit-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "0eb8073c91b674176af3863e57369f0afdaecccfeb80e1ff5b2f57474a5e3ea6"
)
EXPECTED_GLOBAL_MISS_PRIME_LIST_SHA256 = (
    "e578d380be25c8fc1455b842b23997f66cfc3f69d5e2894fd2a8ea13c8a6ba84"
)
EXPECTED_B1_FAILURE_PRIMES = [
    3_942_409,
    62_588_089,
    297_640_249,
    477_015_289,
]
EXPECTED_B1_TOTALS = {
    "global_p_minus_one_miss_count": 21,
    "directed_linear_source_state_count": 1_790,
    "distinct_R_count": 1_015,
    "B_eq_1_captured_prime_count": 17,
    "B_eq_1_failure_prime_count": 4,
    "B_eq_1_target_hit_R_count": 31,
}
EXPECTED_GENERAL_B_PROFILES = {
    3_942_409: {
        "distinct_R_count": 38,
        "classification_counts": {
            "hit": 4,
            "finite_exponent": 6,
            "subgroup_character": 28,
        },
        "subgroup_character_two_power_depth_counts": {"0": 27, "1": 1},
        "hit_R": [171, 199, 391, 10_951],
    },
    62_588_089: {
        "distinct_R_count": 52,
        "classification_counts": {
            "hit": 2,
            "finite_exponent": 20,
            "subgroup_character": 30,
        },
        "subgroup_character_two_power_depth_counts": {"0": 30},
        "hit_R": [103, 495],
    },
    297_640_249: {
        "distinct_R_count": 55,
        "classification_counts": {
            "hit": 4,
            "finite_exponent": 17,
            "subgroup_character": 34,
        },
        "subgroup_character_two_power_depth_counts": {"0": 34},
        "hit_R": [55, 231, 1_751, 6_431],
    },
    477_015_289: {
        "distinct_R_count": 46,
        "classification_counts": {
            "hit": 2,
            "finite_exponent": 10,
            "subgroup_character": 34,
        },
        "subgroup_character_two_power_depth_counts": {"0": 33, "1": 1},
        "hit_R": [43, 51],
    },
}


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of an exact input artifact."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_list_sha256(values: Iterable[int]) -> str:
    """Hash a canonical newline-delimited integer sequence."""
    data = "".join(f"{int(value)}\n" for value in values).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def canonical_json_sha256(value: object) -> str:
    """Hash canonical compact ASCII JSON."""
    data = json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor a positive integer and check the resulting prime powers."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value or any(
        not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors
    ):
        raise AssertionError("factorization did not reconstruct into primes")
    return factors


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Serialize an ascending prime-power factorization."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def divisors_from_factorization(
    factors: Iterable[tuple[int, int]], exponent_multiplier: int = 1
) -> list[int]:
    """Return all positive divisors after scaling every exponent."""
    if exponent_multiplier < 1:
        raise ValueError("exponent multiplier must be positive")
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent_multiplier * exponent + 1)
        ]
    return sorted(divisors)


def exact_fraction_identity(numerator: int, denominators: list[int]) -> bool:
    """Check a three-term unit-fraction identity exactly."""
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def load_global_p_minus_one_misses(path: Path = INPUT) -> list[int]:
    """Load and freeze the 21 global p-1 misses from the prior audit."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("global p-1 audit input hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    primes = [int(value) for value in payload["global_p_minus_one_miss_primes"]]
    if (
        int(payload["totals"]["global_p_minus_one_miss_count"]) != 21
        or len(primes) != 21
        or primes != sorted(primes)
        or len(set(primes)) != len(primes)
        or integer_list_sha256(primes) != EXPECTED_GLOBAL_MISS_PRIME_LIST_SHA256
        or any(prime % 24 != 1 or not sympy.isprime(prime) for prime in primes)
    ):
        raise AssertionError("global p-1 miss input guard failed")
    return primes


def source_state_payload(
    states_by_R: dict[int, list[tuple[int, int]]],
) -> list[dict[str, object]]:
    """Encode all directed source states in canonical R, a, s order."""
    return [
        {
            "R": R,
            "states": [[a, s] for a, s in states_by_R[R]],
        }
        for R in sorted(states_by_R)
    ]


def enumerate_linear_source_states(
    prime: int,
) -> tuple[int, dict[int, list[tuple[int, int]]]]:
    """Exhaust all directed linear E|n sources by the min(a,s) bound."""
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise ValueError("prime must be a core prime")
    bound = math.isqrt((prime - 2) // 3)
    by_R: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for least_coordinate in range(1, bound + 1):
        factors = exact_factorization(prime - least_coordinate)
        for source_factor in divisors_from_factorization(factors):
            if (source_factor - 1) % least_coordinate:
                continue
            R = (source_factor - 1) // least_coordinate
            if R < 3 or R % 4 != 3:
                continue
            other_coordinate = (prime - least_coordinate) // source_factor
            if other_coordinate < least_coordinate or (
                prime
                != least_coordinate
                + other_coordinate
                + least_coordinate * other_coordinate * R
            ):
                continue
            if other_coordinate % 2:
                by_R[R].add((least_coordinate, other_coordinate))
            if least_coordinate % 2 and other_coordinate != least_coordinate:
                by_R[R].add((other_coordinate, least_coordinate))

    result = {R: sorted(states) for R, states in sorted(by_R.items())}
    if not result:
        raise AssertionError("the universal s=1, R=3 linear source disappeared")
    for R, states in result.items():
        for a, s in states:
            E = s * R + 1
            source = prime - s
            if (
                s % 2 != 1
                or prime != a + s + a * s * R
                or source != a * E
                or source % 2
                or min(a, s) > bound
            ):
                raise AssertionError("invalid linear source state")
    return bound, result


def b1_matches(prime: int, R: int) -> tuple[int, list[tuple[int, int]], list[int]]:
    """Return K, its factors, and every B=1 target divisor at this R."""
    K = (prime * R + 1) // 4
    if R < 3 or R % 4 != 3 or 4 * K != prime * R + 1:
        raise AssertionError("invalid target modulus")
    factors = exact_factorization(K)
    matches = [
        divisor
        for divisor in divisors_from_factorization(factors)
        if (4 * divisor + 1) % R == 0
    ]
    return K, factors, matches


def solve_upper_hnf_membership(
    hnf: Matrix, target: list[int]
) -> tuple[bool, dict[str, object]]:
    """Solve H*x=target in integers for a square upper-triangular HNF."""
    dimension = len(target)
    if hnf.shape != (dimension, dimension):
        raise AssertionError("HNF has the wrong full-rank shape")
    if any(int(hnf[row, column]) for row in range(dimension) for column in range(row)):
        raise AssertionError("HNF is not upper triangular")
    coordinates = [0] * dimension
    for row in range(dimension - 1, -1, -1):
        diagonal = int(hnf[row, row])
        if diagonal <= 0:
            raise AssertionError("HNF diagonal must be positive")
        numerator = target[row] - sum(
            int(hnf[row, column]) * coordinates[column]
            for column in range(row + 1, dimension)
        )
        if numerator % diagonal:
            return False, {
                "target_lattice_coordinates": None,
                "first_nondivisible_row": row,
                "numerator": numerator,
                "diagonal": diagonal,
                "remainder": numerator % diagonal,
            }
        coordinates[row] = numerator // diagonal
    return True, {
        "target_lattice_coordinates": coordinates,
        "first_nondivisible_row": None,
    }


def component_lattice_hnf(
    generator_log_vectors: list[list[int]],
    component_orders: list[int],
    two_power_saturation_depth: int | None = None,
) -> Matrix:
    """Return the coordinate lattice for a support subgroup and optional powers."""
    if not component_orders:
        raise ValueError("a unit group needs at least one cyclic component")
    if two_power_saturation_depth is not None and two_power_saturation_depth < 0:
        raise ValueError("two-power saturation depth must be nonnegative")
    dimension = len(component_orders)
    if any(len(vector) != dimension for vector in generator_log_vectors):
        raise AssertionError("generator coordinate vectors have the wrong dimension")
    columns = [*generator_log_vectors]
    if two_power_saturation_depth is not None:
        power = 1 << two_power_saturation_depth
        columns.extend(
            [
                [power if row == column else 0 for row in range(dimension)]
                for column in range(dimension)
            ]
        )
    columns.extend(
        [
            [component_orders[row] if row == column else 0 for row in range(dimension)]
            for column in range(dimension)
        ]
    )
    lattice = Matrix(
        dimension,
        len(columns),
        lambda row, column: columns[column][row],
    )
    return hermite_normal_form(lattice)


def two_power_character_depth(
    certificate: dict[str, object],
) -> dict[str, int]:
    """Find the last 2-power saturation containing -1 outside the support."""
    component_orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    generator_log_vectors = [
        [int(value) for value in vector]
        for vector in certificate["generator_log_vectors"]
    ]
    target_vector = [
        int(value) for value in certificate["target_log_vector_for_minus_one"]
    ]
    if len(component_orders) != len(target_vector):
        raise AssertionError("component orders and target vector disagree")
    max_two_adic_order = max(
        (order & -order).bit_length() - 1 for order in component_orders
    )
    last_member_depth: int | None = None
    for depth in range(max_two_adic_order + 2):
        hnf = component_lattice_hnf(
            generator_log_vectors,
            component_orders,
            two_power_saturation_depth=depth,
        )
        target_in_saturation, _ = solve_upper_hnf_membership(hnf, target_vector)
        if target_in_saturation:
            last_member_depth = depth
            continue
        if last_member_depth is None:
            raise AssertionError("the depth-zero saturation must be the whole group")
        return {
            "two_power_saturation_depth": last_member_depth,
            "minimal_separating_two_power_character_order": 1
            << (last_member_depth + 1),
        }
    raise AssertionError("two-power saturation did not exclude -1")


def unit_group_subgroup_certificate(
    factors: list[tuple[int, int]], R: int
) -> dict[str, object]:
    """Certify whether -1 lies in the subgroup generated by K's prime support."""
    R_factors = exact_factorization(R)
    component_moduli = [prime**exponent for prime, exponent in R_factors]
    component_orders = [int(sympy.totient(modulus)) for modulus in component_moduli]
    primitive_roots = [
        int(sympy.primitive_root(modulus)) for modulus in component_moduli
    ]
    target_vector = [order // 2 for order in component_orders]
    if any(
        pow(root, target, modulus) != modulus - 1
        for root, target, modulus in zip(
            primitive_roots, target_vector, component_moduli
        )
    ):
        raise AssertionError("the component target vector does not represent -1")

    generator_primes = [prime for prime, _ in factors]
    if any(math.gcd(prime, R) != 1 for prime in generator_primes):
        raise AssertionError("K's prime support must be made of R-units")
    generator_log_vectors = []
    for prime in generator_primes:
        logs = [
            int(sympy.discrete_log(modulus, prime % modulus, root))
            for modulus, root in zip(component_moduli, primitive_roots)
        ]
        if any(
            pow(root, logarithm, modulus) != prime % modulus
            for root, logarithm, modulus in zip(primitive_roots, logs, component_moduli)
        ):
            raise AssertionError("discrete logarithm did not reconstruct a generator")
        generator_log_vectors.append(logs)

    dimension = len(component_moduli)
    hnf = component_lattice_hnf(generator_log_vectors, component_orders)
    target_in_subgroup, membership = solve_upper_hnf_membership(hnf, target_vector)
    return {
        "R_factorization": factorization_payload(R_factors),
        "components": [
            {
                "modulus": modulus,
                "order": order,
                "primitive_root": root,
            }
            for modulus, order, root in zip(
                component_moduli, component_orders, primitive_roots
            )
        ],
        "generator_primes": generator_primes,
        "generator_log_vectors": generator_log_vectors,
        "target_log_vector_for_minus_one": target_vector,
        "column_lattice_hermite_normal_form": [
            [int(hnf[row, column]) for column in range(dimension)]
            for row in range(dimension)
        ],
        "target_in_generated_subgroup": target_in_subgroup,
        **membership,
    }


def build_general_B_witness(
    prime: int, a: int, s: int, R: int, matched_divisor: int
) -> dict[str, object]:
    """Recover and exactly replay a natural linear-source Type I bridge."""
    K = (prime * R + 1) // 4
    E = s * R + 1
    source = prime - s
    common = math.gcd(matched_divisor, K)
    initial_B = matched_divisor // common
    if common * common % matched_divisor:
        raise AssertionError("square divisor did not normalize to an integral C")
    C = common * common // matched_divisor
    initial_H = K // common
    if (
        initial_B * C * initial_H != K
        or initial_B * initial_B * C != matched_divisor
        or math.gcd(initial_B, initial_H) != 1
        or initial_B == initial_H
    ):
        raise AssertionError("square-divisor normalization failed")
    orientation_swapped = initial_H < initial_B
    B, H = (initial_H, initial_B) if orientation_swapped else (initial_B, initial_H)
    oriented_divisor = B * B * C
    A, A_remainder = divmod(B + H, R)
    gap, gap_remainder = divmod(4 * oriented_divisor + 1, R)
    source_term, source_remainder = divmod(source * K, E)
    lambda_value = 4 if s % 4 == 1 else 2
    source_u, source_u_remainder = divmod(source, lambda_value)
    D, D_remainder = divmod(E, lambda_value)
    source_common = math.gcd(source_u, D)
    beta, beta_remainder = divmod(D, source_common)
    gamma, gamma_remainder = divmod(source_common, beta)
    alpha, alpha_remainder = divmod(source_u, source_common)
    x, y, z = A * B * C, A * C * H, prime * K
    conditions = {
        "linear_source_equation": prime == a + s + a * s * R,
        "source_factorization": source == a * E,
        "source_is_even": source % 2 == 0,
        "source_square_condition": (source * source // math.gcd(E, 4)) % E == 0,
        "source_term_is_integral": source_remainder == 0,
        "source_term_equals_aK": source_term == a * K,
        "source_normalization_is_integral": not any(
            (
                source_u_remainder,
                D_remainder,
                beta_remainder,
                gamma_remainder,
                alpha_remainder,
            )
        ),
        "source_beta_eq_1": beta == 1,
        "matched_divisor_divides_K_squared": K * K % matched_divisor == 0,
        "matched_target_residue": (4 * matched_divisor + 1) % R == 0,
        "oriented_divisor_divides_K_squared": K * K % oriented_divisor == 0,
        "orientation_preserves_target_residue": (4 * oriented_divisor + 1) % R == 0,
        "B_C_H_reconstruct_K": B * C * H == K,
        "B_H_are_coprime": math.gcd(B, H) == 1,
        "H_is_greater_than_B": H > B,
        "A_is_integral": A_remainder == 0,
        "A_B_are_coprime": math.gcd(A, B) == 1,
        "gap_is_integral": gap_remainder == 0,
        "gap_is_natural": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "normal_form_reconstructs_prime": 4 * A * B * C - gap == prime,
        "target_solution_is_ordered": x < y < z,
        "target_fraction_identity": exact_fraction_identity(prime, [x, y, z]),
        "source_fraction_identity": exact_fraction_identity(
            source, [source_term, x, y]
        ),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"linear-source witness failed: {failed}")
    return {
        "a": a,
        "s": s,
        "R": R,
        "E": E,
        "source_denominator": source,
        "K": K,
        "matched_square_divisor": matched_divisor,
        "source_normalization": {
            "lambda": lambda_value,
            "u": source_u,
            "D": D,
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma,
        },
        "normalized_before_orientation": [initial_B, C, initial_H],
        "orientation_swapped": orientation_swapped,
        "oriented_square_divisor": oriented_divisor,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "source_term": source_term,
        "target_solution": [x, y, z],
        "source_solution": [source_term, x, y],
        "conditions": conditions,
    }


def audit_B1_prime(
    prime: int,
) -> tuple[dict[str, object], dict[int, list[tuple[int, int]]]]:
    """Exhaust every linear source and retain every B=1 hit for one prime."""
    bound, states_by_R = enumerate_linear_source_states(prime)
    hits = []
    for R, states in states_by_R.items():
        _, _, matches = b1_matches(prime, R)
        if not matches:
            continue
        a, s = states[0]
        witness = build_general_B_witness(prime, a, s, R, min(matches))
        if int(witness["normal_form"][1]) != 1:
            raise AssertionError("a B=1 target divisor did not recover B=1")
        hits.append(
            {
                "R": R,
                "source_state_count": len(states),
                "selected_source_state": [a, s],
                "least_B_eq_1_divisor": min(matches),
                "witness": witness,
            }
        )
    states_payload = source_state_payload(states_by_R)
    return (
        {
            "prime": prime,
            "theoretical_u_bound": bound,
            "directed_linear_source_state_count": sum(
                len(states) for states in states_by_R.values()
            ),
            "distinct_R_count": len(states_by_R),
            "linear_source_states_sha256": canonical_json_sha256(states_payload),
            "B_eq_1_target_hit_R_count": len(hits),
            "B_eq_1_hits": hits,
        },
        states_by_R,
    )


def classify_general_B_modulus(
    prime: int, R: int, states: list[tuple[int, int]]
) -> dict[str, object]:
    """Directly classify one complete K^2 target spectrum."""
    K, factors, B1_matches = b1_matches(prime, R)
    square_divisors = divisors_from_factorization(factors, 2)
    target_divisor_residue = (-K) % R
    matches = [
        divisor for divisor in square_divisors if divisor % R == target_divisor_residue
    ]
    centered_residues = {divisor * pow(K, -1, R) % R for divisor in square_divisors}
    subgroup_certificate = unit_group_subgroup_certificate(factors, R)
    target_in_centered = (R - 1) in centered_residues
    if bool(matches) != target_in_centered:
        raise AssertionError("centered spectrum and direct target divisors disagree")
    if B1_matches:
        raise AssertionError("a declared global linear B=1 failure has a B=1 hit")
    target_in_subgroup = bool(subgroup_certificate["target_in_generated_subgroup"])
    classification = (
        "hit"
        if matches
        else "finite_exponent"
        if target_in_subgroup
        else "subgroup_character"
    )
    two_power_depth = (
        two_power_character_depth(subgroup_certificate)
        if classification == "subgroup_character"
        else None
    )
    least_match = min(matches) if matches else None
    if least_match is not None:
        complement = K * K // least_match
        if (
            least_match > K
            or K * K % least_match
            or complement % R != target_divisor_residue
        ):
            raise AssertionError("square-divisor complement normalization failed")
    return {
        "R": R,
        "source_state_count": len(states),
        "source_states": [[a, s] for a, s in states],
        "K": K,
        "K_factorization": factorization_payload(factors),
        "B_eq_1_target_reachable": False,
        "square_divisor_count": len(square_divisors),
        "centered_spectrum_residue_count": len(centered_residues),
        "target_divisor_residue": target_divisor_residue,
        "minus_one_in_centered_spectrum": target_in_centered,
        "classification": classification,
        "subgroup_character_two_power_depth": (
            two_power_depth["two_power_saturation_depth"]
            if two_power_depth is not None
            else None
        ),
        "minimal_separating_two_power_character_order": (
            two_power_depth["minimal_separating_two_power_character_order"]
            if two_power_depth is not None
            else None
        ),
        "least_matching_square_divisor": least_match,
        "unit_group_subgroup_certificate": subgroup_certificate,
    }


def audit_general_B_failure_prime(
    prime: int, states_by_R: dict[int, list[tuple[int, int]]]
) -> dict[str, object]:
    """Profile every induced linear modulus for a global B=1 failure prime."""
    records = [
        classify_general_B_modulus(prime, R, states)
        for R, states in states_by_R.items()
    ]
    classification_counts = {
        name: sum(record["classification"] == name for record in records)
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    hit_records = [record for record in records if record["classification"] == "hit"]
    two_power_depth_counts = {
        str(depth): sum(
            record["classification"] == "subgroup_character"
            and int(record["subgroup_character_two_power_depth"]) == depth
            for record in records
        )
        for depth in sorted(
            {
                int(record["subgroup_character_two_power_depth"])
                for record in records
                if record["classification"] == "subgroup_character"
            }
        )
    }
    if not hit_records:
        raise AssertionError("general B failed at every linear state")
    selected = hit_records[0]
    a, s = (int(value) for value in selected["source_states"][0])
    witness = build_general_B_witness(
        prime,
        a,
        s,
        int(selected["R"]),
        int(selected["least_matching_square_divisor"]),
    )
    if int(witness["normal_form"][1]) <= 1:
        raise AssertionError("a global B=1 failure unexpectedly selected B=1")
    expected = EXPECTED_GENERAL_B_PROFILES[prime]
    hit_R = [int(record["R"]) for record in hit_records]
    if (
        len(records) != expected["distinct_R_count"]
        or classification_counts != expected["classification_counts"]
        or two_power_depth_counts
        != expected["subgroup_character_two_power_depth_counts"]
        or hit_R != expected["hit_R"]
    ):
        raise AssertionError("general-B obstruction profile changed")
    return {
        "prime": prime,
        "distinct_R_count": len(records),
        "general_B_classification_counts": classification_counts,
        "subgroup_character_two_power_depth_counts": two_power_depth_counts,
        "general_B_hit_R": hit_R,
        "selected_general_B_witness": witness,
        "records": records,
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Run the complete finite 21-prime and four-profile audit."""
    primes = load_global_p_minus_one_misses(path)
    B1_records = []
    source_states_by_prime: dict[int, dict[int, list[tuple[int, int]]]] = {}
    for prime in primes:
        record, states_by_R = audit_B1_prime(prime)
        B1_records.append(record)
        source_states_by_prime[prime] = states_by_R

    B1_failure_primes = [
        int(record["prime"])
        for record in B1_records
        if not record["B_eq_1_target_hit_R_count"]
    ]
    totals = {
        "global_p_minus_one_miss_count": len(primes),
        "directed_linear_source_state_count": sum(
            int(record["directed_linear_source_state_count"]) for record in B1_records
        ),
        "distinct_R_count": sum(
            int(record["distinct_R_count"]) for record in B1_records
        ),
        "B_eq_1_captured_prime_count": sum(
            bool(record["B_eq_1_target_hit_R_count"]) for record in B1_records
        ),
        "B_eq_1_failure_prime_count": len(B1_failure_primes),
        "B_eq_1_target_hit_R_count": sum(
            int(record["B_eq_1_target_hit_R_count"]) for record in B1_records
        ),
    }
    if totals != EXPECTED_B1_TOTALS or B1_failure_primes != EXPECTED_B1_FAILURE_PRIMES:
        raise AssertionError("global linear B=1 audit changed")

    general_B_profiles = [
        audit_general_B_failure_prime(prime, source_states_by_prime[prime])
        for prime in B1_failure_primes
    ]
    aggregate_classification_counts = {
        name: sum(
            int(profile["general_B_classification_counts"][name])
            for profile in general_B_profiles
        )
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    if aggregate_classification_counts != {
        "hit": 12,
        "finite_exponent": 53,
        "subgroup_character": 126,
    }:
        raise AssertionError("aggregate general-B obstruction totals changed")
    aggregate_two_power_depth_counts = {
        str(depth): sum(
            int(profile["subgroup_character_two_power_depth_counts"].get(str(depth), 0))
            for profile in general_B_profiles
        )
        for depth in (0, 1)
    }
    if aggregate_two_power_depth_counts != {"0": 124, "1": 2}:
        raise AssertionError("aggregate two-power character depths changed")
    return {
        "arithmetic": (
            "hash-freeze the 21 global p-1 maximum-tail misses; exhaust every "
            "linear source p=a+s+asR by min(a,s)<=sqrt((p-2)/3); directly test "
            "B=1 divisors of K=(pR+1)/4; then, for each global linear-B=1 "
            "failure, enumerate every d|K^2 and decide -1 membership in the "
            "prime-support subgroup through component discrete logs and a column "
            "Hermite normal form"
        ),
        "scope_note": (
            "This is a complete finite audit only on the 21 primes already "
            "known to lack a p-1 maximum-tail bridge in the repository's "
            "normal-form architecture. It neither covers all core primes nor "
            "proves the universal mixed terminal selector."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "global_p_minus_one_miss_prime_list_sha256": integer_list_sha256(primes),
        "B_eq_1_totals": totals,
        "global_linear_B_eq_1_failure_primes": B1_failure_primes,
        "B_eq_1_records": B1_records,
        "general_B_failure_profiles": general_B_profiles,
        "aggregate_general_B_classification_counts": aggregate_classification_counts,
        "aggregate_subgroup_character_two_power_depth_counts": (
            aggregate_two_power_depth_counts
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key
                in {
                    "B_eq_1_totals",
                    "global_linear_B_eq_1_failure_primes",
                    "aggregate_general_B_classification_counts",
                    "aggregate_subgroup_character_two_power_depth_counts",
                }
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
