#!/usr/bin/env python3
"""Verify two fixed controls for the c=3 adaptive factor-block normal form.

The positive control replays every raw edge of the h=105/u=3 factor word.
The negative control exhausts only the finite divisor normal form for h=42,
where the two relevant numbers are already factored.  This program performs
no range scan and does not create a selector edge.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_c3_affine_prime_even_tail_root_entry as prime_entry
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks
import type_i_high_r_chart_two_anchor as shared


def prime_word(value: int) -> list[int]:
    """Return the ordered prime-factor word of a positive integer."""
    word: list[int] = []
    for prime, exponent in shared.factorization(value):
        word.extend([prime] * exponent)
    return word


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def positive_divisors(value: int) -> list[int]:
    """Enumerate the divisors of one fixed factored control integer."""
    divisors = [1]
    for prime, exponent in shared.factorization(value):
        divisors = [
            divisor * prime_power
            for divisor in divisors
            for prime_power in (prime**power for power in range(exponent + 1))
        ]
    return sorted(divisors)


def c3_parameters(*, h: int, a: int, b: int) -> dict[str, int]:
    """Check the exact arithmetic normal-form and reserve predicates."""
    p = 24 * h + 1
    R = 104 * h - 9
    M = 26 * h + 1
    x = p - 3
    K = M * x
    S = (R - 1) // 2

    if not shared.is_prime(p) or p % 24 != 1:
        raise AssertionError("control is not a core prime")
    if h % 3 == 2 or h % 13 == 12:
        raise AssertionError("control is outside the declared c=3 tail branch")
    if b % 2 or S % (b // 2) or (R - b) % a or a % 8 != 7:
        raise AssertionError("adaptive divisor normal form failed")

    alpha = (R - 1) // b
    beta = (R - b) // a
    gamma = (R - a) // 8
    if min(alpha, beta, gamma) <= 0:
        raise AssertionError("factor-block labels must be positive")

    capacity_blocks = (
        ("alpha", b, alpha),
        ("beta", a, beta),
        ("gamma", 4, gamma),
    )
    for name, endpoint, label in capacity_blocks:
        for prime in prime_word(label):
            if valuation(endpoint, prime) < valuation(K, prime):
                raise AssertionError(f"{name} endpoint reserve failed at {prime}")

    if gcd(a, b) != 1 or gcd(a, R) != 1 or gcd(b, R) != 1:
        raise AssertionError("automatic primitive/unit consequences failed")
    if 13 * x != 3 * R + 1 or K % 13 == 0:
        raise AssertionError("fixed c=3 thirteen-tail condition failed")

    return {
        "h": h,
        "p": p,
        "R": R,
        "M": M,
        "x": x,
        "K": K,
        "S": S,
        "a": a,
        "b": b,
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
    }


def replay_positive_control(parameters: dict[str, int]) -> list[dict[str, object]]:
    """Replay the declared factor word using the existing raw-step contract."""
    p = parameters["p"]
    R = parameters["R"]
    K = parameters["K"]
    x = parameters["x"]
    a = parameters["a"]
    b = parameters["b"]
    alpha = parameters["alpha"]
    beta = parameters["beta"]
    gamma = parameters["gamma"]

    source = (p, R * (p - 1) - p, p - 1)
    canonical_anchor = (1, R - 1, 1)
    source_step = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=source,
        selected_coordinate_index=0,
        q=p,
        expected_destination=canonical_anchor,
        name="adaptive_family_universal_p_edge",
    )
    _, alpha_rows = factor_blocks.replay_block(
        modulus=R,
        K=K,
        source=(R - 1, 1, 1),
        selected_coordinate_index=0,
        word=prime_word(alpha),
        endpoint=(b, R - b, 1),
        name="adaptive_family_alpha",
    )
    _, beta_rows = factor_blocks.replay_block(
        modulus=R,
        K=K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=prime_word(beta),
        endpoint=(a, R - a, 1),
        name="adaptive_family_beta",
    )
    entry = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(a, R - a, 1),
        selected_coordinate_index=1,
        q=2,
        expected_destination=(4 * gamma, R - 4 * gamma, 1),
        name="adaptive_family_gamma_entry",
    )
    _, gamma_rows = factor_blocks.replay_block(
        modulus=R,
        K=K,
        source=(4 * gamma, R - 4 * gamma, 1),
        selected_coordinate_index=0,
        word=prime_word(gamma),
        endpoint=(4, R - 4, 1),
        name="adaptive_family_gamma",
    )
    tail_13 = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(4, R - 4, 1),
        selected_coordinate_index=1,
        q=13,
        expected_destination=(R - 4 * x, 4 * x, 1),
        name="adaptive_family_tail_13",
    )
    tail_2a = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(R - 4 * x, 4 * x, 1),
        selected_coordinate_index=1,
        q=2,
        expected_destination=(2 * x, R - 2 * x, 1),
        name="adaptive_family_tail_2a",
    )
    tail_2b = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(2 * x, R - 2 * x, 1),
        selected_coordinate_index=0,
        q=2,
        expected_destination=(x, R - x, 1),
        name="adaptive_family_tail_2b",
    )
    rows = [source_step, *alpha_rows, *beta_rows, entry, *gamma_rows, tail_13, tail_2a, tail_2b]
    if len(rows) != 11:
        raise AssertionError("positive control raw-word length changed")
    if any(not row["strict_capacity"] or not row["unit_condition"] or row["gcd_reduction"] != 1 for row in rows):
        raise AssertionError("positive control raw step failed")
    if rows[-1]["destination"] != [x, R - x, 1]:
        raise AssertionError("positive control reached the wrong seed")
    return rows


def verify_adaptive_family_control() -> dict[str, object]:
    """Check u=3, including the displayed family identities and raw replay."""
    u = 3
    h = 35 * u
    a = 416 * u - 1
    b = 728 * u - 2
    parameters = c3_parameters(h=h, a=a, b=b)

    expected = {
        "p": 2521,
        "R": 10911,
        "K": 2 * 1259 * 2731,
        "a": 1247,
        "b": 2182,
        "alpha": 5,
        "beta": 7,
        "gamma": 1208,
    }
    for key, value in expected.items():
        if parameters[key] != value:
            raise AssertionError(f"adaptive family control changed: {key}")

    P = 2 * parameters["alpha"] * parameters["beta"] * parameters["gamma"]
    W = 13 * P
    if (
        4 * P != 31 * parameters["R"] - 1
        or W + parameters["M"] != 101 * parameters["R"]
        or 4 * W != 403 * parameters["R"] - 13
    ):
        raise AssertionError("adaptive family phase identities failed")

    rows = replay_positive_control(parameters)
    return {
        "parameters": parameters,
        "raw_step_count": len(rows),
        "final_destination": rows[-1]["destination"],
        "phase": {"P": P, "W": W},
    }


def verify_h42_topology_counterexample() -> dict[str, object]:
    """Exhaust only the divisor normal form at h=42 before capacity testing."""
    h = 42
    p = 24 * h + 1
    R = 104 * h - 9
    S = (R - 1) // 2
    if not shared.is_prime(p) or shared.factorization(S) != [(2179, 1)]:
        raise AssertionError("h=42 control factorization changed")
    if shared.factorization(R - 2) != [(4357, 1)] or (R - 2) % 8 != 5:
        raise AssertionError("h=42 second divisor factorization changed")

    candidates: list[tuple[int, int]] = []
    for d in positive_divisors(S):
        b = 2 * d
        for a in positive_divisors(R - b):
            if a % 8 == 7:
                candidates.append((d, a))
    if candidates:
        raise AssertionError("h=42 unexpectedly admitted the fixed normal form")
    return {
        "h": h,
        "p": p,
        "R": R,
        "S_factorization": shared.factorization(S),
        "R_minus_2_factorization": shared.factorization(R - 2),
        "normal_form_candidates": candidates,
    }


def build_result() -> dict[str, object]:
    """Replay the two fixed theorem controls without a coverage scan."""
    return {
        "certificate_type": "c3_adaptive_divisor_factor_block_normal_form_v1",
        "scope": (
            "One positive raw replay and one finite topology counterexample only; "
            "this does not register a root or selector edge."
        ),
        "positive_control": verify_adaptive_family_control(),
        "negative_control": verify_h42_topology_counterexample(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified c=3 adaptive factor-block controls: h=105 and h=42")


if __name__ == "__main__":
    main()
