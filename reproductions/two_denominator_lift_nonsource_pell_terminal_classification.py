#!/usr/bin/env python3
"""Focused checks for the non-source D-only Pell classification."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, isqrt


def positive_divisors(value: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        low.append(divisor)
        partner = value // divisor
        if partner != divisor:
            high.append(partner)
    return low + high[::-1]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def unit_fraction_sum(denominators: tuple[int, int, int]) -> Fraction:
    return sum((Fraction(1, item) for item in denominators), Fraction(0, 1))


def derive_state(p: int, n: int, d_only: int) -> dict[str, object]:
    assert is_prime(p)
    assert 2 <= n < p
    rank_gap = p - n
    modulus = 4 * rank_gap
    product = n * p

    assert product * product % d_only == 0
    assert 0 < d_only < n * n
    assert (d_only - product) % modulus == 0
    assert (product * product // d_only - product) % modulus == 0
    assert d_only % p == 0

    delta = d_only // p
    assert n * n % delta == 0
    h_carrier = n * n // delta
    source_first = (product - d_only) // modulus
    target_first = (product * product // d_only - product) // modulus
    assert target_first % p == 0
    lam = target_first // p
    mu = 4 * lam - 1
    assert h_carrier == p + mu * rank_gap
    assert 4 * lam * lam % h_carrier == 0
    s_value = 4 * lam * lam // h_carrier
    t_value = lam - rank_gap * s_value
    assert source_first == p * t_value
    assert t_value > 0

    gamma = gcd(h_carrier, s_value)
    a_squared = h_carrier // gamma
    b_squared = s_value // gamma
    carrier_a = isqrt(a_squared)
    carrier_b = isqrt(b_squared)
    assert carrier_a * carrier_a == a_squared
    assert carrier_b * carrier_b == b_squared
    assert gcd(carrier_a, carrier_b) == 1
    assert 2 * lam == gamma * carrier_a * carrier_b
    w_value = carrier_a - 2 * rank_gap * carrier_b
    assert w_value > 0
    assert n == gamma * carrier_a * w_value
    assert p == gamma * carrier_a * w_value + rank_gap
    assert d_only == p * gamma * w_value * w_value
    assert 2 * t_value == gamma * carrier_b * w_value

    normalized = [item for item in positive_divisors(lam * lam) if item < lam]
    targets = {
        "e0": [item for item in normalized if (item + p * lam) % mu == 0],
        "e1": [item for item in normalized if (item + lam) % mu == 0],
        "e2": [item for item in normalized if (p * item + lam) % mu == 0],
    }

    return {
        "p": p,
        "n": n,
        "rank_gap": rank_gap,
        "D": d_only,
        "lambda": lam,
        "mu": mu,
        "H": h_carrier,
        "s": s_value,
        "t": t_value,
        "gamma": gamma,
        "A": carrier_a,
        "B": carrier_b,
        "w": w_value,
        "targets": targets,
    }


def verify_hit(state: dict[str, object], hit: int) -> dict[str, object]:
    p = int(state["p"])
    n = int(state["n"])
    rank_gap = int(state["rank_gap"])
    lam = int(state["lambda"])
    mu = int(state["mu"])
    s_value = int(state["s"])
    t_value = int(state["t"])
    gamma = int(state["gamma"])
    carrier_a = int(state["A"])
    carrier_b = int(state["B"])

    assert hit in state["targets"]["e0"]
    complement = lam * lam // hit
    assert (complement + s_value) % mu == 0
    h_value = (complement + s_value) // mu
    x_value = (p * lam + hit) // mu
    gap = 4 * x_value - p
    assert p + 4 * hit == gap * mu
    l_value = rank_gap + gap
    assert 4 * hit + gamma * carrier_a * carrier_a == l_value * mu
    assert complement + gamma * carrier_b * carrier_b == h_value * mu
    assert Fraction(2 * carrier_a * carrier_b, 1) == (
        Fraction(carrier_a * carrier_a, l_value)
        + Fraction(carrier_b * carrier_b, h_value)
        + Fraction(1, gamma)
    )

    target_tail = p * h_value - t_value
    assert target_tail > 0
    source = (p * t_value, x_value, p * target_tail)
    target = (p * lam, x_value, p * target_tail)
    assert unit_fraction_sum(source) == Fraction(4, n)
    assert unit_fraction_sum(target) == Fraction(4, p)
    assert hit == gap * lam - x_value
    assert x_value * x_value % hit == 0
    shared = gcd(lam, x_value)
    assert hit % shared == 0
    assert shared * shared % hit == 0

    return {
        "z": hit,
        "v": complement,
        "h": h_value,
        "m": gap,
        "x": x_value,
        "L": l_value,
        "source": source,
        "target": target,
        "shared_square_root": shared,
    }


def verify_pell_case(a_value: int, b_value: int) -> dict[str, object]:
    assert b_value * b_value - 2 * a_value * a_value == -1
    p = 4 * a_value * (a_value + b_value) - 1
    assert is_prime(p)
    n = p - 1
    d_only = 2 * p * b_value * b_value
    state = derive_state(p, n, d_only)
    expected_lambda = a_value * (b_value + 2 * a_value)
    assert state["lambda"] == expected_lambda
    assert state["s"] == 2 * a_value * a_value
    assert state["t"] == a_value * b_value
    assert state["gamma"] == 2
    assert state["A"] == b_value + 2 * a_value
    assert state["B"] == a_value
    assert state["w"] == b_value
    assert state["targets"]["e1"] == []
    assert state["targets"]["e2"] == []
    assert a_value * a_value in state["targets"]["e0"]
    hit = verify_hit(state, a_value * a_value)
    assert hit["m"] == 1
    assert hit["h"] == 1
    assert hit["L"] == 2
    assert p % 8 == 7
    return {"state": state, "hit": hit}


def verify_core_empty_case(
    p: int,
    n: int,
    d_only: int,
    expected_lambda: int,
    expected_s: int,
) -> dict[str, object]:
    assert p % 4 == 1
    state = derive_state(p, n, d_only)
    assert state["lambda"] == expected_lambda
    assert state["s"] == expected_s
    assert state["targets"] == {"e0": [], "e1": [], "e2": []}
    return state


def run_verification() -> dict[str, object]:
    pell_cases = [
        verify_pell_case(1, 1),
        verify_pell_case(5, 7),
    ]
    core_empty_cases = [
        verify_core_empty_case(73, 70, 730, 35, 10),
        verify_core_empty_case(457, 455, 79975, 91, 28),
        verify_core_empty_case(1801, 1776, 1037376, 37, 1),
    ]
    return {
        "claim": "two-denominator-lift-nonsource-pell-terminal-classification",
        "pell_positive_cases": pell_cases,
        "core_empty_cases": core_empty_cases,
        "checks": {
            "three_target_to_one_target": True,
            "square_carrier_normal_form": True,
            "cross_square_type_ii_capacity": True,
            "pell_boundary_maps": True,
            "previously_open_n_mod_4_equals_3_control": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.parse_args()
    result = run_verification()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
