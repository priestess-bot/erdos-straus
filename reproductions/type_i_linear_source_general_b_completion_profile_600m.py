#!/usr/bin/env python3
"""Audit linear-source, general-B Type I bridges on 1,964 tail misses.

The two hash-frozen inputs contain the 1,717 ordinary Type II p-1 double-tail
misses at p<=500M and the 247 misses in 500M<p<=600M.  For each input prime,
all linear sources

    p = a + s + a*s*R,  s odd,  R>=3,  R=3 (mod 4)

are enumerable by u=min(a,s)<=sqrt((p-2)/3).  At a fixed u, the factor
1+u*R divides p-u.  The program scans u and those divisors in increasing
order, and it decides every new R by a complete balanced meet-in-the-middle
test of d|K^2, 4d=-1 (mod R), where K=(pR+1)/4.

Every hit is normalized to coprime B,H, oriented to H>B, checked for a
natural Type I gap, and replayed on both the target p and the even source
n=p-s with exact Fraction arithmetic.  A failed prime would retain every R
audit through the theoretical square-root bound.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT_500M = (
    ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json"
)
INPUT_500M_600M = (
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-source-general-b-completion-profile-600m-results.json"
)

EXPECTED_INPUT_500M_FILE_SHA256 = (
    "426ef578d796c7307505e87d16794d28569a91d8297693ec742bcf21873d4f77"
)
EXPECTED_INPUT_500M_600M_FILE_SHA256 = (
    "beca2d981fbccd4313f14f5f5ba81459afaae368bf377db066f26a8bbdc77ce0"
)
EXPECTED_INPUT_500M_PRIME_LIST_SHA256 = (
    "f3553871ba8b5e9ad256d1f647bd034dd305b9c192ea0295034da1585082252e"
)
EXPECTED_INPUT_500M_600M_PRIME_LIST_SHA256 = (
    "1856761ddad705b94e02a9ed62aa59c384b84597ff3ec193714abeb76c6257f2"
)
EXPECTED_COMBINED_PRIME_LIST_SHA256 = (
    "c6f389dc599898b9bfe182c10d3260033e6ebc2ad9061251b7fb8a7e1ef5ce40"
)

EXPECTED_TOTALS = {
    "input_prime_count": 1_964,
    "u_values_scanned": 3_597,
    "p_minus_u_divisors_materialized": 99_394,
    "unordered_linear_source_candidates": 6_968,
    "directed_linear_source_candidates": 9_485,
    "unique_R_audits": 6_656,
    "square_divisor_candidate_space": 3_638_456,
    "square_divisor_candidates_checked_until_first_hit": 3_060_069,
    "mitm_candidate_entries": 202_644,
    "captured_count": 1_964,
    "failure_count": 0,
    "selected_B_eq_1_count": 1_764,
    "selected_B_gt_1_count": 200,
    "selected_s_eq_1_count": 1_091,
    "selected_s_gt_1_count": 873,
    "fraction_replayed_count": 1_964,
}
EXPECTED_MAXIMUM_LEAST_U = 587
EXPECTED_MAXIMUM_LEAST_U_PRIME = 283_319_689
WITNESS_TUPLE_FIELDS = [
    "prime",
    "a",
    "s",
    "R",
    "K",
    "matched_square_divisor",
    "A",
    "B",
    "C",
    "H",
    "gap",
]
EXPECTED_SELECTED_WITNESS_TUPLES_SHA256 = (
    "461b9c7a816500fd9dc5ebff4e86f38352a0998667caf0f3a49b2f4270aadb7a"
)


def file_sha256(path: Path) -> str:
    """Hash the exact bytes of an input artifact."""
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
    """Factor a positive integer and verify its prime-power product."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value or any(
        not sympy.isprime(prime) for prime, _ in factors
    ):
        raise AssertionError("factorization did not reconstruct into primes")
    return factors


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Serialize a factorization in canonical ascending-prime order."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def parse_factorization(
    payload: list[dict[str, int]],
) -> list[tuple[int, int]]:
    """Parse and validate a serialized factorization."""
    factors = [(int(item["prime"]), int(item["exponent"])) for item in payload]
    if factors != sorted(factors) or any(exponent < 1 for _, exponent in factors):
        raise AssertionError("serialized factorization is not canonical")
    return factors


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


def balanced_factor_split(
    factors: list[tuple[int, int]],
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """Balance the two complete K^2 prime-power menus deterministically."""
    if not factors:
        return [], []
    choices = [2 * exponent + 1 for _, exponent in factors]
    full_count = math.prod(choices)
    best_key: tuple[int, int, int] | None = None
    best_mask = 0
    # Fix the first prime on the left to quotient left/right symmetry.
    for mask in range(1 << (len(factors) - 1)):
        left_count = choices[0]
        for index in range(1, len(factors)):
            if mask & (1 << (index - 1)):
                left_count *= choices[index]
        right_count = full_count // left_count
        key = (left_count + right_count, max(left_count, right_count), mask)
        if best_key is None or key < best_key:
            best_key = key
            best_mask = mask
    left = [factors[0]]
    right: list[tuple[int, int]] = []
    for index, factor in enumerate(factors[1:], start=1):
        if best_mask & (1 << (index - 1)):
            left.append(factor)
        else:
            right.append(factor)
    return left, right


def exact_fraction_identity(numerator: int, denominators: list[int]) -> bool:
    """Check a three-term unit-fraction identity exactly."""
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def load_authoritative_primes(
    input_500m: Path = INPUT_500M,
    input_500m_600m: Path = INPUT_500M_600M,
) -> tuple[dict[str, object], dict[str, object], list[int], list[int]]:
    """Load, validate, and hash-freeze the two authoritative pressure sets."""
    if file_sha256(input_500m) != EXPECTED_INPUT_500M_FILE_SHA256:
        raise AssertionError("p<=500M authoritative artifact hash changed")
    if file_sha256(input_500m_600m) != EXPECTED_INPUT_500M_600M_FILE_SHA256:
        raise AssertionError("500M<p<=600M authoritative artifact hash changed")
    first = json.loads(input_500m.read_text(encoding="utf-8"))
    second = json.loads(input_500m_600m.read_text(encoding="utf-8"))
    first_primes = [int(record["prime"]) for record in first["records"]]
    second_primes = [
        int(record["prime"]) for record in second["type_i_even_terminal_bridge_records"]
    ]
    if (
        int(first["prime_limit"]) != 500_000_000
        or int(first["ordinary_tail_miss_count"]) != 1_717
        or int(first["even_source_captured_count"]) != 1_717
        or first["even_source_misses"]
        or len(first_primes) != 1_717
        or first_primes != sorted(first_primes)
        or len(set(first_primes)) != len(first_primes)
        or integer_list_sha256(first_primes) != EXPECTED_INPUT_500M_PRIME_LIST_SHA256
    ):
        raise AssertionError("p<=500M authoritative pressure-set guard failed")
    if (
        [int(value) for value in second["prime_interval"]] != [500_000_001, 600_000_000]
        or int(second["ordinary_type_ii_tail_miss_count"]) != 247
        or int(second["type_i_even_terminal_bridge_count"]) != 247
        or second["even_source_misses"]
        or len(second_primes) != 247
        or second_primes != sorted(second_primes)
        or len(set(second_primes)) != len(second_primes)
        or integer_list_sha256(second_primes)
        != EXPECTED_INPUT_500M_600M_PRIME_LIST_SHA256
    ):
        raise AssertionError("500M<p<=600M authoritative pressure-set guard failed")
    if set(first_primes) & set(second_primes):
        raise AssertionError("the two authoritative pressure sets overlap")
    combined = [*first_primes, *second_primes]
    if integer_list_sha256(combined) != EXPECTED_COMBINED_PRIME_LIST_SHA256:
        raise AssertionError("combined authoritative prime sequence changed")
    if any(prime % 24 != 1 or not sympy.isprime(prime) for prime in combined):
        raise AssertionError("authoritative input contains a non-core prime")
    return first, second, first_primes, second_primes


def audit_target_R(prime: int, R: int) -> dict[str, object]:
    """Completely decide one R by a balanced K^2 divisor MITM."""
    K = (prime * R + 1) // 4
    if R < 3 or R % 4 != 3 or 4 * K != prime * R + 1:
        raise AssertionError("invalid target modulus")
    if math.gcd(K, R) != 1:
        raise AssertionError("K must be invertible modulo R")
    factors = exact_factorization(K)
    left_factors, right_factors = balanced_factor_split(factors)
    left_divisors = divisors_from_factorization(left_factors, 2)
    right_divisors = divisors_from_factorization(right_factors, 2)
    right_by_residue: dict[int, int] = {}
    for divisor in right_divisors:
        right_by_residue.setdefault(divisor % R, divisor)

    target_residue = (-pow(4, -1, R)) % R
    if target_residue != (-K) % R:
        raise AssertionError("the two target-residue formulas disagree")
    required_right_residues: set[int] = set()
    matched_divisor: int | None = None
    for left_divisor in left_divisors:
        required = (target_residue * pow(left_divisor, -1, R)) % R
        required_right_residues.add(required)
        right_divisor = right_by_residue.get(required)
        if right_divisor is None:
            continue
        candidate = left_divisor * right_divisor
        if matched_divisor is None or candidate < matched_divisor:
            matched_divisor = candidate

    right_residues = set(right_by_residue)
    intersection = right_residues & required_right_residues
    if bool(intersection) != (matched_divisor is not None):
        raise AssertionError("MITM intersection and witness recovery disagree")
    all_square_divisors = divisors_from_factorization(factors, 2)
    if matched_divisor is None:
        logically_checked = len(all_square_divisors)
    else:
        logically_checked = sum(
            divisor <= matched_divisor for divisor in all_square_divisors
        )
        if (
            matched_divisor not in all_square_divisors
            or 4 * matched_divisor % R != R - 1
            or matched_divisor > K
        ):
            raise AssertionError("least MITM hit failed canonical guards")
    return {
        "R": R,
        "K": K,
        "K_factorization": factorization_payload(factors),
        "target_residue": target_residue,
        "square_divisor_candidate_space": len(all_square_divisors),
        "square_divisor_candidates_checked_until_first_hit": logically_checked,
        "matched_square_divisor": matched_divisor,
        "target_residue_reachable": matched_divisor is not None,
        "mitm": {
            "left_factorization": factorization_payload(left_factors),
            "right_factorization": factorization_payload(right_factors),
            "left_divisor_count": len(left_divisors),
            "right_divisor_count": len(right_divisors),
            "candidate_entry_count": len(left_divisors) + len(right_divisors),
            "right_distinct_residue_count": len(right_residues),
            "required_right_residue_count": len(required_right_residues),
            "residue_intersection_count": len(intersection),
            "right_residue_sha256": integer_list_sha256(sorted(right_residues)),
            "required_right_residue_sha256": integer_list_sha256(
                sorted(required_right_residues)
            ),
        },
    }


def build_witness(
    prime: int,
    a: int,
    s: int,
    R: int,
    target_audit: dict[str, object],
) -> dict[str, object]:
    """Normalize a target hit and replay both exact identities."""
    K = int(target_audit["K"])
    matched = int(target_audit["matched_square_divisor"])
    common = math.gcd(matched, K)
    initial_B = matched // common
    if common * common % matched:
        raise AssertionError("square divisor did not normalize to integral C")
    C = common * common // matched
    initial_H = K // common
    if (
        initial_B * C * initial_H != K
        or initial_B * initial_B * C != matched
        or math.gcd(initial_B, initial_H) != 1
    ):
        raise AssertionError("square-divisor normalization failed")
    if initial_B == initial_H:
        raise AssertionError("target residue unexpectedly allowed B=H")
    orientation_swapped = initial_H < initial_B
    B, H = (initial_H, initial_B) if orientation_swapped else (initial_B, initial_H)
    oriented_divisor = B * B * C
    A, A_remainder = divmod(B + H, R)
    gap, gap_remainder = divmod(4 * oriented_divisor + 1, R)

    E = s * R + 1
    source = prime - s
    source_term, source_remainder = divmod(source * K, E)
    lambda_value = 4 if s % 4 == 1 else 2
    source_u, source_u_remainder = divmod(source, lambda_value)
    D, D_remainder = divmod(E, lambda_value)
    source_common = math.gcd(source_u, D)
    beta, beta_remainder = divmod(D, source_common)
    gamma, gamma_remainder = divmod(source_common, beta)
    alpha, alpha_remainder = divmod(source_u, source_common)

    x = A * B * C
    y = A * C * H
    z = prime * K
    target_solution = [x, y, z]
    source_solution = [source_term, x, y]
    certificate_divisor = A * A * C
    conditions = {
        "linear_source_equation": prime == a + s + a * s * R,
        "source_factorization": source == a * E,
        "source_is_even": source % 2 == 0,
        "source_is_strictly_smaller": 2 <= source < prime,
        "source_is_in_top_quarter": 4 * source >= 3 * prime + 1,
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
        "source_normalization_reconstructs": (
            source_u == alpha * beta * gamma
            and D == beta * beta * gamma
            and math.gcd(alpha, beta) == 1
        ),
        "source_beta_eq_1": beta == 1,
        "matched_square_divisor_divides_K_squared": K * K % matched == 0,
        "matched_target_residue": (4 * matched + 1) % R == 0,
        "oriented_square_divisor_divides_K_squared": (K * K % oriented_divisor == 0),
        "orientation_preserves_target_residue": ((4 * oriented_divisor + 1) % R == 0),
        "B_C_H_reconstruct_K": B * C * H == K,
        "B_H_are_coprime": math.gcd(B, H) == 1,
        "H_is_greater_than_B": H > B,
        "A_is_integral": A_remainder == 0,
        "A_B_are_coprime": math.gcd(A, B) == 1,
        "gap_is_integral": gap_remainder == 0,
        "gap_is_natural": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "normal_form_reconstructs_prime": 4 * A * B * C - gap == prime,
        "target_certificate_divides_x_squared": x * x % certificate_divisor == 0,
        "target_certificate_congruence": ((prime * x + certificate_divisor) % gap == 0),
        "target_solution_is_ordered": x < y < z,
        "target_fraction_identity": exact_fraction_identity(prime, target_solution),
        "source_fraction_identity": exact_fraction_identity(source, source_solution),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"linear-source witness failed: {failed}")
    return {
        "a": a,
        "s": s,
        "least_coordinate_u": min(a, s),
        "R": R,
        "E": E,
        "source_denominator": source,
        "source_distance": s,
        "source_normalization": {
            "lambda": lambda_value,
            "u": source_u,
            "D": D,
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma,
        },
        "K": K,
        "matched_square_divisor": matched,
        "normalized_before_orientation": [initial_B, C, initial_H],
        "orientation_swapped": orientation_swapped,
        "oriented_square_divisor": oriented_divisor,
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "normal_form": [A, B, C],
        "gap": gap,
        "target_certificate_divisor": certificate_divisor,
        "source_term": source_term,
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def audit_prime(prime: int) -> tuple[dict[str, object], bool]:
    """Search one prime, exhausting the sqrt bound if no target hit exists."""
    theoretical_bound = math.isqrt((prime - 2) // 3)
    seen_R: set[int] = set()
    target_audits: list[dict[str, object]] = []
    stats = {
        "u_values_scanned": 0,
        "p_minus_u_divisors_materialized": 0,
        "unordered_linear_source_candidates": 0,
        "directed_linear_source_candidates": 0,
        "unique_R_audits": 0,
        "square_divisor_candidate_space": 0,
        "square_divisor_candidates_checked_until_first_hit": 0,
        "mitm_candidate_entries": 0,
    }
    for u in range(1, theoretical_bound + 1):
        stats["u_values_scanned"] += 1
        p_minus_u = prime - u
        p_minus_u_factors = exact_factorization(p_minus_u)
        divisors = divisors_from_factorization(p_minus_u_factors)
        stats["p_minus_u_divisors_materialized"] += len(divisors)
        for source_factor in divisors:
            if (source_factor - 1) % u:
                continue
            R = (source_factor - 1) // u
            if R < 3 or R % 4 != 3:
                continue
            other = p_minus_u // source_factor
            if other < u:
                continue
            if prime != u + other + u * other * R:
                raise AssertionError("divisor recovery failed")
            stats["unordered_linear_source_candidates"] += 1
            directed_sources: list[tuple[int, int]] = []
            # This order is part of the deterministic witness contract.
            if other % 2:
                directed_sources.append((u, other))
            if u % 2 and other != u:
                directed_sources.append((other, u))
            if not directed_sources:
                raise AssertionError("odd p produced no odd-s orientation")
            stats["directed_linear_source_candidates"] += len(directed_sources)
            if R in seen_R:
                continue
            seen_R.add(R)
            target_audit = audit_target_R(prime, R)
            target_audits.append(target_audit)
            stats["unique_R_audits"] += 1
            stats["square_divisor_candidate_space"] += int(
                target_audit["square_divisor_candidate_space"]
            )
            stats["square_divisor_candidates_checked_until_first_hit"] += int(
                target_audit["square_divisor_candidates_checked_until_first_hit"]
            )
            stats["mitm_candidate_entries"] += int(
                target_audit["mitm"]["candidate_entry_count"]
            )
            if not target_audit["target_residue_reachable"]:
                continue
            a, s = directed_sources[0]
            witness = build_witness(prime, a, s, R, target_audit)
            return (
                {
                    "prime": prime,
                    "theoretical_u_bound": theoretical_bound,
                    "search_exhausted_theoretical_bound": False,
                    "search_statistics": stats,
                    "all_R_audits_sha256": canonical_json_sha256(target_audits),
                    "selected_R_audit": target_audit,
                    "selected_witness": witness,
                },
                True,
            )
    return (
        {
            "prime": prime,
            "theoretical_u_bound": theoretical_bound,
            "search_exhausted_theoretical_bound": True,
            "search_statistics": stats,
            "all_R_audits_sha256": canonical_json_sha256(target_audits),
            "R_audits": target_audits,
        },
        False,
    )


def selected_witness_tuple(record: dict[str, object]) -> list[int]:
    """Return the explicitly frozen compact witness tuple."""
    witness = record["selected_witness"]
    values = {
        "prime": int(record["prime"]),
        **{field: int(witness[field]) for field in WITNESS_TUPLE_FIELDS[1:]},
    }
    return [values[field] for field in WITNESS_TUPLE_FIELDS]


def maximum_witness_parameter(
    records: list[dict[str, object]], field: str
) -> dict[str, int]:
    """Return a deterministic maximum with its least-prime location."""
    negative_value, prime = min(
        (
            (-int(record["selected_witness"][field]), int(record["prime"]))
            for record in records
        ),
        key=lambda item: (item[0], item[1]),
    )
    return {"value": -negative_value, "prime": prime}


def run_audit(
    input_500m: Path = INPUT_500M,
    input_500m_600m: Path = INPUT_500M_600M,
) -> dict[str, object]:
    """Run the complete finite 1,964-prime pressure-set audit."""
    first, second, first_primes, second_primes = load_authoritative_primes(
        input_500m, input_500m_600m
    )
    combined = [*first_primes, *second_primes]
    captured: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for prime in combined:
        record, found = audit_prime(prime)
        (captured if found else failures).append(record)

    all_records = [*captured, *failures]
    totals = {
        "input_prime_count": len(combined),
        **{
            key: sum(int(record["search_statistics"][key]) for record in all_records)
            for key in (
                "u_values_scanned",
                "p_minus_u_divisors_materialized",
                "unordered_linear_source_candidates",
                "directed_linear_source_candidates",
                "unique_R_audits",
                "square_divisor_candidate_space",
                "square_divisor_candidates_checked_until_first_hit",
                "mitm_candidate_entries",
            )
        },
        "captured_count": len(captured),
        "failure_count": len(failures),
        "selected_B_eq_1_count": sum(
            int(record["selected_witness"]["B"]) == 1 for record in captured
        ),
        "selected_B_gt_1_count": sum(
            int(record["selected_witness"]["B"]) > 1 for record in captured
        ),
        "selected_s_eq_1_count": sum(
            int(record["selected_witness"]["s"]) == 1 for record in captured
        ),
        "selected_s_gt_1_count": sum(
            int(record["selected_witness"]["s"]) > 1 for record in captured
        ),
        "fraction_replayed_count": sum(
            record["selected_witness"]["conditions"]["target_fraction_identity"]
            and record["selected_witness"]["conditions"]["source_fraction_identity"]
            for record in captured
        ),
    }
    if totals != EXPECTED_TOTALS:
        raise AssertionError(f"linear-source audit totals changed: {totals}")
    max_u_value = max(
        int(record["selected_witness"]["least_coordinate_u"]) for record in captured
    )
    max_u_primes = [
        int(record["prime"])
        for record in captured
        if int(record["selected_witness"]["least_coordinate_u"]) == max_u_value
    ]
    if max_u_value != EXPECTED_MAXIMUM_LEAST_U or max_u_primes != [
        EXPECTED_MAXIMUM_LEAST_U_PRIME
    ]:
        raise AssertionError("maximum least linear-source coordinate changed")

    witness_tuples = [selected_witness_tuple(record) for record in captured]
    witness_hash = canonical_json_sha256(witness_tuples)
    if witness_hash != EXPECTED_SELECTED_WITNESS_TUPLES_SHA256:
        raise AssertionError("selected witness tuple sequence changed")

    maxima = {
        "least_coordinate_u": {
            "value": max_u_value,
            "prime": max_u_primes[0],
        },
        "theoretical_u_bound": {
            "value": max(int(record["theoretical_u_bound"]) for record in all_records),
            "prime": max(
                all_records,
                key=lambda record: (
                    int(record["theoretical_u_bound"]),
                    -int(record["prime"]),
                ),
            )["prime"],
        },
        **{
            field: maximum_witness_parameter(captured, field)
            for field in ("a", "s", "R", "K", "A", "B", "C", "H", "gap")
        },
    }
    return {
        "arithmetic": (
            "for each of the 1,964 hash-frozen ordinary Type II p-1 tail "
            "misses, scan u=min(a,s)<=floor(sqrt((p-2)/3)); factor p-u and "
            "recover linear sources in a complete order until the first hit "
            "(or the bound if none); for each first occurrence of R, completely "
            "decide 4d=-1 mod R over d|K^2 with a balanced "
            "MITM; select the first reachable source in the documented order, "
            "normalize d by gcd(d,K) to B,C,H, orient H>B, and replay the "
            "source and target identities exactly"
        ),
        "scope_note": (
            "This is a finite completion profile on exactly 1,964 stored "
            "ordinary Type II p-1 double-tail misses: 1,717 at p<=500M and "
            "247 at 500M<p<=600M. It is not a scan of all core primes in that "
            "range and does not prove the universal linear-source general-B "
            "selector or the Erdos-Straus conjecture."
        ),
        "input": {
            "first_artifact": input_500m.name,
            "first_artifact_file_sha256": file_sha256(input_500m),
            "first_prime_count": len(first_primes),
            "first_prime_list_sha256": integer_list_sha256(first_primes),
            "first_prime_limit": int(first["prime_limit"]),
            "second_artifact": input_500m_600m.name,
            "second_artifact_file_sha256": file_sha256(input_500m_600m),
            "second_prime_count": len(second_primes),
            "second_prime_list_sha256": integer_list_sha256(second_primes),
            "second_prime_interval": [int(value) for value in second["prime_interval"]],
            "input_intersection_count": len(set(first_primes) & set(second_primes)),
            "combined_prime_count": len(combined),
            "combined_prime_list_sha256": integer_list_sha256(combined),
        },
        "completeness": {
            "least_coordinate_bound": "u<=floor(sqrt((p-2)/3))",
            "source_recovery": (
                "enumerate every q|(p-u); retain q=1 (mod u), "
                "R=(q-1)/u>=3 with R=3 (mod 4), and v=(p-u)/q>=u"
            ),
            "orientation_order": (
                "for each unordered (u,v,R), first (a,s)=(u,v) when v is "
                "odd, then (a,s)=(v,u) when u is odd and u!=v"
            ),
            "R_deduplication": (
                "target reachability depends only on (p,R), so repeated R for "
                "one prime reuses its already complete miss; a hit stops that prime"
            ),
            "failure_rule": (
                "a failed prime is accepted only after every u through the "
                "theoretical bound and every recovered unique R is audited; "
                "its result record retains the complete R_audits array"
            ),
            "mitm_rule": (
                "split the full prime-power menu of K^2 into two balanced "
                "blocks; enumerate every divisor on both sides and intersect "
                "the exact required and attained residue sets modulo R"
            ),
        },
        "witness_selection": {
            "rule": (
                "in increasing u and increasing q|(p-u), select the first new "
                "R whose complete MITM is reachable; use the first legal "
                "directed source and the least matching d, then orient H>B"
            ),
            "tuple_fields": WITNESS_TUPLE_FIELDS,
            "tuple_serialization": (
                "JSON array of arrays, ensure_ascii=true, sort_keys=true, "
                "separators=(',',':')"
            ),
            "selected_witness_tuples_sha256": witness_hash,
        },
        "totals": totals,
        "maxima": maxima,
        "failure_primes": [int(record["prime"]) for record in failures],
        "captured_records": captured,
        "failure_records": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-500m", type=Path, default=INPUT_500M)
    parser.add_argument("--input-500m-600m", type=Path, default=INPUT_500M_600M)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input_500m, args.input_500m_600m)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        key: value
        for key, value in result.items()
        if key not in {"captured_records", "failure_records"}
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
