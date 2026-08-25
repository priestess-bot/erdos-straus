#!/usr/bin/env python3
"""Independent arithmetic control for the genuine two-sided p^2 boundary.

This verifier intentionally does not import the selector, source serializer, or the
existing p2 verifier.  The fixture is an arithmetic control, not an actual
m=3, 5|D_star persistent witness.
"""

from __future__ import annotations

import argparse
import json
from math import gcd


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise AssertionError("factorization expects a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return Q_K(value) and the charged residual beta."""
    value_factors = factorization(value)
    capacity_factors = factorization(capacity)
    block = 1
    for prime, exponent in value_factors.items():
        if exponent > capacity_factors.get(prime, 0):
            block *= prime**exponent
    return block, value // block


def chart(prime: int, parameter: int) -> dict[str, int]:
    g = (prime + 1) // 2
    T = prime * prime * parameter - g
    support = g * T
    capacity = support * (prime - 1)
    residual = (4 * capacity - 1) // prime
    if not (
        prime % 24 == 1
        and T > 0
        and 4 * capacity == prime * residual + 1
    ):
        raise AssertionError("root chart control changed")
    return {
        "p": prime,
        "rho": parameter,
        "g": g,
        "T": T,
        "A": support,
        "K": capacity,
        "R": residual,
    }


def validate_endpoint(prime: int, residual: int, left: int, right: int) -> None:
    if not (
        left > 0
        and right > 0
        and left + right == residual
        and gcd(left, right) == 1
        and prime * residual + 1 > 0
        and left % prime != 0
        and right % prime != 0
    ):
        raise AssertionError("endpoint is not primitive and p-free")


def factor_endpoint(data: dict[str, int], left: int, right: int) -> dict[str, int]:
    prime, support, capacity, residual = (
        data["p"],
        data["A"],
        data["K"],
        data["R"],
    )
    validate_endpoint(prime, residual, left, right)
    q_left, beta_left = complete_excess(left, capacity)
    q_right, beta_right = complete_excess(right, capacity)
    g_left = gcd(support, q_left)
    g_right = gcd(support, q_right)
    e_left, e_right = q_left // g_left, q_right // g_right
    d_left, d_right = beta_left * g_left, beta_right * g_right
    if not (
        d_left * e_left == left
        and d_right * e_right == right
        and capacity % d_left == 0
        and capacity % d_right == 0
        and gcd(d_left, d_right) == 1
        and capacity % (d_left * d_right) == 0
        and (prime * e_right * d_right + 1) % d_left == 0
        and (prime * e_left * d_left + 1) % d_right == 0
    ):
        raise AssertionError("two-sided divisor-source gates changed")
    multiplier = e_left * e_right
    joined_support = support * multiplier
    cofactor = pow((4 * joined_support) % prime, -1, prime)
    return {
        "left": left,
        "right": right,
        "Q_left": q_left,
        "Q_right": q_right,
        "E_left": e_left,
        "E_right": e_right,
        "D_left": d_left,
        "D_right": d_right,
        "multiplier": multiplier,
        "cofactor": cofactor,
    }


def two_sided_control() -> dict[str, int]:
    data = chart(73, 57)
    # This is the fixed arithmetic two-sided control used to test the boundary.
    right = (data["R"] - (data["p"] + 1)) // data["p"]
    left = data["R"] - right
    endpoint = factor_endpoint(data, left, right)
    p = data["p"]
    multiplier = endpoint["multiplier"]
    if not (
        endpoint["E_left"] > 1
        and endpoint["E_right"] > 1
        and multiplier > 1
        and (multiplier - 1) % (p * p) == 0
        and endpoint["cofactor"] == p - 1
    ):
        raise AssertionError("two-sided p2 control changed")
    chi = (multiplier - 1) // (p * p)
    rho_prime = data["rho"] + chi * data["T"]
    T_prime = p * p * rho_prime - data["g"]
    if not (
        chi > 0
        and rho_prime > data["rho"]
        and T_prime == multiplier * data["T"]
        and data["A"] * multiplier == data["g"] * T_prime
    ):
        raise AssertionError("increasing root rechart identity changed")
    return {
        "p": p,
        "rho": data["rho"],
        "T": data["T"],
        "A": data["A"],
        "K": data["K"],
        "R": data["R"],
        "left": left,
        "right": right,
        "E_left": endpoint["E_left"],
        "E_right": endpoint["E_right"],
        "D_left": endpoint["D_left"],
        "D_right": endpoint["D_right"],
        "multiplier": multiplier,
        "chi": chi,
        "cofactor": endpoint["cofactor"],
        "rho_prime": rho_prime,
        "T_prime": T_prime,
        "direct_rechart_is_strict": False,
        "fixture_is_actual_persistent_m3_q5": False,
    }


def object_separation_control() -> dict[str, int]:
    data = chart(73, 57)
    endpoint = factor_endpoint(data, 3, data["R"] - 3)
    if not (
        endpoint["multiplier"] % data["p"] != 1
        and endpoint["cofactor"] < data["p"] - 1
    ):
        raise AssertionError("L1/L_omega object separation control changed")
    return {
        "p": data["p"],
        "same_chart_left": 3,
        "same_chart_multiplier_mod_p": endpoint["multiplier"] % data["p"],
        "same_chart_cofactor": endpoint["cofactor"],
    }


def malformed_endpoint_control() -> bool:
    data = chart(73, 57)
    try:
        factor_endpoint(data, 2, 2)
    except AssertionError:
        return True
    raise AssertionError("malformed endpoint was accepted")


def verify() -> dict[str, object]:
    return {
        "two_sided": two_sided_control(),
        "object_separation": object_separation_control(),
        "malformed_rejected": malformed_endpoint_control(),
        "status": "ARITHMETIC_CONTROL_ONLY_P2_RECHART_UNPAID",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
