#!/usr/bin/env python3
"""Globally audit p-1 Type I terminal bridges on the 185 box misses.

The input is the exact 185-prime residual from the stored p<=500M, m<=215
normal-form profile.  For each prime p, every p-1 source state is forced by

    t = (p-1)/4,  r | t^2,  R = 4r-1,  K = pr-t.

The audit enumerates every such r.  It factors K through the normalized split
K=beta*gamma*(beta*p-alpha), then uses an exact meet-in-the-middle divisor
residue test on d|K^2.  A hit is normalized to coprime B,H and oriented so that
H>B, which enforces the natural Type I gap 3<=m<=p-2.  Every retained witness
is replayed with exact Fraction identities on both p and p-1.
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
INPUT = (
    ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-pminusone-box-miss-global-audit-500m-results.json"
)

EXPECTED_INPUT_PRIME_COUNT = 185
EXPECTED_INPUT_PRIME_LIST_SHA256 = (
    "e4a723da32b70ee8aed0236f66a6d61803181e0e1db1fd8767b830e81a0f7ccf"
)
EXPECTED_FORCED_STATE_COUNT = 15_411
EXPECTED_SQUARE_DIVISOR_CANDIDATE_COUNT = 112_657_233
EXPECTED_ORDERED_BCH_CANDIDATE_COUNT = 178_245_405
EXPECTED_MITM_ENTRY_COUNT = 1_417_964
EXPECTED_TARGET_REACHABLE_STATE_COUNT = 511
EXPECTED_CAPTURED_COUNT = 164
EXPECTED_GLOBAL_MISS_COUNT = 21
EXPECTED_GLOBAL_MISS_PRIME_LIST_SHA256 = (
    "e578d380be25c8fc1455b842b23997f66cfc3f69d5e2894fd2a8ea13c8a6ba84"
)
EXPECTED_ALL_PRIME_STATE_HASHES_SHA256 = (
    "20f90ca67914c813a37debb3cc2bed4506c5350b6d3fab084fde68005862dace"
)


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor a positive integer and verify the prime-power product."""
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
    """Serialize a factorization in the repository's standard shape."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def parse_factorization(payload: list[dict[str, int]]) -> list[tuple[int, int]]:
    """Parse and validate a serialized factorization."""
    factors = [(int(item["prime"]), int(item["exponent"])) for item in payload]
    if factors != sorted(factors) or any(exponent < 1 for _, exponent in factors):
        raise AssertionError("serialized factorization is not canonical")
    return factors


def merge_factorizations(
    left: Iterable[tuple[int, int]], right: Iterable[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Multiply two factorizations, combining shared prime exponents."""
    merged: dict[int, int] = {}
    for factors in (left, right):
        for prime, exponent in factors:
            merged[prime] = merged.get(prime, 0) + exponent
    return sorted(merged.items())


def supported_factorization(
    value: int, support: Iterable[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Factor a known divisor using an already verified prime support."""
    remainder = value
    factors: list[tuple[int, int]] = []
    for prime, _ in support:
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
    if remainder != 1:
        raise AssertionError("known factor block escaped the t support")
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


def integer_list_sha256(values: Iterable[int]) -> str:
    """Hash a canonical newline-delimited integer sequence."""
    data = "".join(f"{int(value)}\n" for value in values).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def canonical_json_sha256(value: object) -> str:
    """Hash a JSON value with stable key and separator choices."""
    data = json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def load_authoritative_primes(
    path: Path = INPUT,
) -> tuple[dict[str, object], list[int]]:
    """Load and freeze the exact 185-prime bounded-box residual."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    primes = [int(prime) for prime in payload["p_minus_one_misses"]]
    prime_hash = integer_list_sha256(primes)
    if (
        int(payload["prime_limit"]) != 500_000_000
        or int(payload["gap_cap"]) != 215
        or int(payload["ordinary_tail_residual_count"]) != 1_717
        or int(payload["p_minus_one_captured_count"]) != 1_532
        or len(primes) != EXPECTED_INPUT_PRIME_COUNT
        or len(set(primes)) != len(primes)
        or primes != sorted(primes)
        or prime_hash != EXPECTED_INPUT_PRIME_LIST_SHA256
    ):
        raise AssertionError("authoritative 185-prime input guard failed")
    if any(prime % 24 != 1 or not sympy.isprime(prime) for prime in primes):
        raise AssertionError("authoritative input contains a non-core prime")
    return payload, primes


def balanced_factor_split(
    factors: list[tuple[int, int]],
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """Split K^2 prime-power menus to minimize the two MITM list sizes."""
    if not factors:
        return [], []
    choices = [2 * exponent + 1 for _, exponent in factors]
    full_count = math.prod(choices)
    best_key: tuple[int, int, int] | None = None
    best_mask = 0
    # Fix the first factor on the left to remove the left/right symmetry.
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


def divisor_residue_map(
    factors: list[tuple[int, int]], modulus: int
) -> tuple[list[int], dict[int, int]]:
    """Return the divisors and the least representative of each residue."""
    divisors = divisors_from_factorization(factors, 2)
    residues: dict[int, int] = {}
    for divisor in divisors:
        residues.setdefault(divisor % modulus, divisor)
    return divisors, residues


def residue_hit_summary(
    factors: list[tuple[int, int]], modulus: int, target_residue: int
) -> tuple[dict[str, object], int | None]:
    """Exactly decide whether a divisor of K^2 reaches the target residue."""
    left_factors, right_factors = balanced_factor_split(factors)
    left_divisors = divisors_from_factorization(left_factors, 2)
    right_divisors, right_by_residue = divisor_residue_map(right_factors, modulus)
    required_right_residues: set[int] = set()
    matched_divisor: int | None = None
    for left_divisor in left_divisors:
        if math.gcd(left_divisor, modulus) != 1:
            raise AssertionError("a K divisor was not invertible modulo R")
        required = (target_residue * pow(left_divisor, -1, modulus)) % modulus
        required_right_residues.add(required)
        right_divisor = right_by_residue.get(required)
        if right_divisor is None:
            continue
        candidate = left_divisor * right_divisor
        if matched_divisor is None or candidate < matched_divisor:
            matched_divisor = candidate
    right_residues = set(right_by_residue)
    intersection = required_right_residues & right_residues
    if bool(intersection) != (matched_divisor is not None):
        raise AssertionError("MITM intersection and witness recovery disagree")
    summary = {
        "left_factorization": factorization_payload(left_factors),
        "right_factorization": factorization_payload(right_factors),
        "left_divisor_count": len(left_divisors),
        "right_divisor_count": len(right_divisors),
        "mitm_candidate_entry_count": len(left_divisors) + len(right_divisors),
        "right_distinct_residue_count": len(right_residues),
        "required_right_residue_count": len(required_right_residues),
        "residue_intersection_count": len(intersection),
        "right_residue_sha256": integer_list_sha256(sorted(right_residues)),
        "required_right_residue_sha256": integer_list_sha256(
            sorted(required_right_residues)
        ),
    }
    return summary, matched_divisor


def exact_fraction_identity(numerator: int, denominators: list[int]) -> bool:
    """Check a three-term unit-fraction identity exactly."""
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def build_natural_witness(
    prime: int,
    t: int,
    r: int,
    R: int,
    K: int,
    matched_divisor: int,
) -> dict[str, object]:
    """Normalize a square-divisor hit and orient it to a natural Type I gap."""
    common = math.gcd(matched_divisor, K)
    initial_B = matched_divisor // common
    if common * common % matched_divisor:
        raise AssertionError("square divisor did not normalize to integral C")
    C = common * common // matched_divisor
    initial_H = K // common
    if (
        initial_B * C * initial_H != K
        or initial_B * initial_B * C != matched_divisor
        or math.gcd(initial_B, initial_H) != 1
    ):
        raise AssertionError("square-divisor normalization failed")
    if initial_B == initial_H:
        raise AssertionError("target residue unexpectedly allowed B=H")

    orientation_swapped = initial_H < initial_B
    B, H = (initial_H, initial_B) if orientation_swapped else (initial_B, initial_H)
    oriented_divisor = B * B * C
    if (H + B) % R:
        raise AssertionError("target congruence did not recover integral A")
    A = (H + B) // R
    gap_numerator = 4 * oriented_divisor + 1
    gap, remainder = divmod(gap_numerator, R)
    if remainder:
        raise AssertionError("oriented target divisor did not recover integral gap")

    E = R + 1
    source = prime - 1
    source_term, source_remainder = divmod(source * K, E)
    x = A * B * C
    y = A * C * H
    z = prime * K
    target_solution = [x, y, z]
    source_solution = [source_term, x, y]
    certificate_divisor = A * A * C
    conditions = {
        "matched_square_divisor_divides_K_squared": (K * K) % matched_divisor == 0,
        "matched_target_residue": (4 * matched_divisor + 1) % R == 0,
        "oriented_square_divisor_divides_K_squared": (K * K) % oriented_divisor == 0,
        "orientation_preserves_target_residue": (4 * oriented_divisor + 1) % R == 0,
        "B_C_H_reconstruct_K": B * C * H == K,
        "B_H_are_coprime": math.gcd(B, H) == 1,
        "H_is_greater_than_B": H > B,
        "A_is_integral": A * R == H + B,
        "A_B_are_coprime": math.gcd(A, B) == 1,
        "normal_form_reconstructs_prime": 4 * A * B * C - gap == prime,
        "gap_is_natural": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "target_certificate_divides_x_squared": (x * x) % certificate_divisor == 0,
        "target_certificate_congruence": (prime * x + certificate_divisor) % gap == 0,
        "p_minus_one_square_condition": (t * t) % r == 0,
        "source_square_compatible": (source * source // math.gcd(E, 4)) % E == 0,
        "E_divides_4K_squared": (4 * K * K) % E == 0,
        "source_term_is_integral": source_remainder == 0,
        "target_solution_is_ordered": x < y < z,
        "target_fraction_identity": exact_fraction_identity(prime, target_solution),
        "source_fraction_identity": exact_fraction_identity(source, source_solution),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"natural p-1 witness failed: {failed}")
    return {
        "r": r,
        "R": R,
        "K": K,
        "E": E,
        "source_denominator": source,
        "source_distance": 1,
        "matched_square_divisor": matched_divisor,
        "normalized_before_orientation": [initial_B, C, initial_H],
        "orientation_swapped": orientation_swapped,
        "oriented_square_divisor": oriented_divisor,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "target_certificate_divisor": certificate_divisor,
        "source_term": source_term,
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def audit_forced_state(
    prime: int, t: int, t_factors: list[tuple[int, int]], r: int
) -> tuple[dict[str, object], dict[str, object] | None]:
    """Audit one forced r|t^2 state without directly factoring its full K."""
    R = 4 * r - 1
    K = prime * r - t
    if R < 3 or R % 4 != 3 or 4 * K != prime * R + 1:
        raise AssertionError("forced p-1 state did not reconstruct")
    common = math.gcd(t, r)
    beta = r // common
    gamma, remainder = divmod(common, beta)
    alpha, alpha_remainder = divmod(t, common)
    if (
        remainder
        or alpha_remainder
        or t != alpha * beta * gamma
        or r != beta * beta * gamma
        or math.gcd(alpha, beta) != 1
    ):
        raise AssertionError("source-square normalization failed")
    known_factor_block = beta * gamma
    affine_factor = beta * prime - alpha
    if affine_factor >= 1 << 56:
        raise AssertionError("affine K factor escaped the verified 56-bit range")
    if K != known_factor_block * affine_factor:
        raise AssertionError("K factor split failed")
    block_factors = supported_factorization(known_factor_block, t_factors)
    affine_factors = exact_factorization(affine_factor)
    K_factors = merge_factorizations(block_factors, affine_factors)
    if math.prod(q**exponent for q, exponent in K_factors) != K:
        raise AssertionError("split K factorization did not reconstruct")
    if math.gcd(K, R) != 1:
        raise AssertionError("K and R must be coprime")

    square_divisor_count = math.prod(2 * exponent + 1 for _, exponent in K_factors)
    ordered_BCH_count = math.prod(
        (exponent + 1) * (exponent + 2) // 2 for _, exponent in K_factors
    )
    target_residue = (-r) % R
    mitm, matched_divisor = residue_hit_summary(K_factors, R, target_residue)
    reachable = matched_divisor is not None
    state = {
        "r": r,
        "R": R,
        "K": K,
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "known_factor_block": known_factor_block,
        "known_factor_block_factorization": factorization_payload(block_factors),
        "affine_factor": affine_factor,
        "affine_factorization": factorization_payload(affine_factors),
        "K_factorization": factorization_payload(K_factors),
        "square_divisor_candidate_count": square_divisor_count,
        "ordered_BCH_candidate_count": ordered_BCH_count,
        "target_residue": target_residue,
        "target_residue_reachable": reachable,
        "matched_square_divisor": matched_divisor,
        "mitm": mitm,
    }
    witness = (
        build_natural_witness(prime, t, r, R, K, int(matched_divisor))
        if matched_divisor is not None
        else None
    )
    return state, witness


def audit_prime(prime: int) -> tuple[dict[str, object], bool]:
    """Audit every forced p-1 state of one authoritative input prime."""
    t = (prime - 1) // 4
    t_factors = exact_factorization(t)
    r_values = divisors_from_factorization(t_factors, 2)
    expected_state_count = math.prod(2 * exponent + 1 for _, exponent in t_factors)
    if len(r_values) != expected_state_count:
        raise AssertionError("forced r divisor enumeration is incomplete")

    states: list[dict[str, object]] = []
    witnesses: list[dict[str, object]] = []
    for r in r_values:
        state, witness = audit_forced_state(prime, t, t_factors, r)
        states.append(state)
        if witness is not None:
            witnesses.append(witness)
    state_hash = canonical_json_sha256(states)
    square_count = sum(int(state["square_divisor_candidate_count"]) for state in states)
    ordered_count = sum(int(state["ordered_BCH_candidate_count"]) for state in states)
    mitm_count = sum(
        int(state["mitm"]["mitm_candidate_entry_count"]) for state in states
    )
    reachable_state_count = sum(
        bool(state["target_residue_reachable"]) for state in states
    )
    common = {
        "prime": prime,
        "t": t,
        "t_factorization": factorization_payload(t_factors),
        "forced_r_state_count": len(r_values),
        "states_checked": len(states),
        "square_divisor_candidate_count": square_count,
        "ordered_BCH_candidate_count": ordered_count,
        "mitm_candidate_entry_count": mitm_count,
        "target_reachable_state_count": reachable_state_count,
        "all_state_summaries_sha256": state_hash,
    }
    if not witnesses:
        return {**common, "p_minus_one_states": states}, False
    selected = min(
        witnesses,
        key=lambda witness: (int(witness["r"]), int(witness["matched_square_divisor"])),
    )
    return {**common, "selected_p_minus_one_witness": selected}, True


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the complete 185-point global p-1 audit."""
    input_payload, primes = load_authoritative_primes(input_path)
    captured: list[dict[str, object]] = []
    global_misses: list[dict[str, object]] = []
    per_prime_hashes: list[dict[str, object]] = []
    for prime in primes:
        record, has_witness = audit_prime(prime)
        per_prime_hashes.append(
            {
                "prime": prime,
                "all_state_summaries_sha256": record["all_state_summaries_sha256"],
            }
        )
        if has_witness:
            captured.append(record)
        else:
            global_misses.append(record)

    all_records = [*captured, *global_misses]
    totals = {
        "input_box_miss_count": len(primes),
        "forced_r_state_count": sum(
            int(record["forced_r_state_count"]) for record in all_records
        ),
        "states_checked": sum(int(record["states_checked"]) for record in all_records),
        "square_divisor_candidate_count": sum(
            int(record["square_divisor_candidate_count"]) for record in all_records
        ),
        "ordered_BCH_candidate_count": sum(
            int(record["ordered_BCH_candidate_count"]) for record in all_records
        ),
        "mitm_candidate_entry_count": sum(
            int(record["mitm_candidate_entry_count"]) for record in all_records
        ),
        "target_reachable_state_count": sum(
            int(record["target_reachable_state_count"]) for record in all_records
        ),
        "p_minus_one_captured_count": len(captured),
        "global_p_minus_one_miss_count": len(global_misses),
        "orientation_swapped_count": sum(
            bool(record["selected_p_minus_one_witness"]["orientation_swapped"])
            for record in captured
        ),
        "natural_gap_verified_count": sum(
            bool(record["selected_p_minus_one_witness"]["conditions"]["gap_is_natural"])
            for record in captured
        ),
    }
    expected = {
        "input_box_miss_count": EXPECTED_INPUT_PRIME_COUNT,
        "forced_r_state_count": EXPECTED_FORCED_STATE_COUNT,
        "states_checked": EXPECTED_FORCED_STATE_COUNT,
        "square_divisor_candidate_count": (EXPECTED_SQUARE_DIVISOR_CANDIDATE_COUNT),
        "ordered_BCH_candidate_count": EXPECTED_ORDERED_BCH_CANDIDATE_COUNT,
        "mitm_candidate_entry_count": EXPECTED_MITM_ENTRY_COUNT,
        "target_reachable_state_count": EXPECTED_TARGET_REACHABLE_STATE_COUNT,
        "p_minus_one_captured_count": EXPECTED_CAPTURED_COUNT,
        "global_p_minus_one_miss_count": EXPECTED_GLOBAL_MISS_COUNT,
        "natural_gap_verified_count": EXPECTED_CAPTURED_COUNT,
    }
    if any(totals[key] != value for key, value in expected.items()):
        raise AssertionError("global p-1 audit totals changed")

    global_miss_primes = [int(record["prime"]) for record in global_misses]
    if (
        integer_list_sha256(global_miss_primes)
        != EXPECTED_GLOBAL_MISS_PRIME_LIST_SHA256
    ):
        raise AssertionError("global p-1 miss set changed")
    all_prime_state_hashes = canonical_json_sha256(per_prime_hashes)
    if all_prime_state_hashes != EXPECTED_ALL_PRIME_STATE_HASHES_SHA256:
        raise AssertionError("complete forced-state audit changed")

    return {
        "arithmetic": (
            "load the hash-frozen 185 misses from the p<=500M, m<=215 p-1 "
            "normal-form profile; for each p factor t=(p-1)/4 and exhaust "
            "every r|t^2; normalize r=beta^2*gamma and "
            "t=alpha*beta*gamma so K=beta*gamma*(beta*p-alpha); factor only "
            "the known block and the <2^56 affine factor; decide the target "
            "d=-r mod R among all d|K^2 by exact balanced meet-in-the-middle; "
            "normalize each hit to coprime B,H, orient H>B, and replay both "
            "unit-fraction identities with Fraction"
        ),
        "scope_note": (
            "The input consists only of the 185 p-1 misses in the stored "
            "p<=500M, m<=215 normal-form box. The audit removes the gap and B "
            "bounds for the repository's maximum-tail p-1 Type I bridge on "
            "those 185 primes. It is not an audit of every p<=500M and does "
            "not exclude other Type I transformations or Type II coordinates."
        ),
        "input": {
            "artifact": input_path.name,
            "prime_limit": int(input_payload["prime_limit"]),
            "source_gap_cap": int(input_payload["gap_cap"]),
            "ordinary_tail_residual_count": int(
                input_payload["ordinary_tail_residual_count"]
            ),
            "box_p_minus_one_captured_count": int(
                input_payload["p_minus_one_captured_count"]
            ),
            "box_p_minus_one_miss_count": len(primes),
            "prime_list_sha256": integer_list_sha256(primes),
        },
        "witness_selection_rule": (
            "after auditing every forced state, select the least r with a hit; "
            "within that state select the least reconstructed d|K^2; then orient "
            "the normalized coprime pair so H>B"
        ),
        "totals": totals,
        "all_prime_state_hashes_sha256": all_prime_state_hashes,
        "global_p_minus_one_miss_primes": global_miss_primes,
        "captured_records": captured,
        "global_miss_records": global_misses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        key: value
        for key, value in result.items()
        if key not in {"captured_records", "global_miss_records"}
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
