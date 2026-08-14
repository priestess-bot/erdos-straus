#!/usr/bin/env python3
"""Verify the inverse full-product normal form for the q=1 canonical root.

This is a focused algebraic verifier.  It classifies the legal d < p factor
pairs that would fold to the canonical root, the p-only d = g pre-root seed,
and the q=1 carrier separation from standard factor-pair descent parameters.
It deliberately does not search raw reachability or create an E1/E3-qualified
state.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt


CONTROLS = (73, 97, 193, 433, 673, 1033)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factorization(value).items():
        base = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in base)
    return sorted(result)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def canonical_root(prime: int) -> dict[str, int]:
    if not is_prime(prime) or prime % 24 != 1:
        raise AssertionError("control is not a core prime")
    p = prime
    t = (p - 1) // 24
    g = (p + 1) // 2
    T = p * p * t - g
    A = g * T
    n = (4 * A + 1) // p
    K = A * (p - 1)
    R = 4 * A - n
    B = (p - 1) ** 2 // 4
    if not (
        t >= 3
        and T > p * p
        and p * n == 4 * A + 1
        and n == 2 * p * t * (p + 1) - p - 2
        and p * R + 1 == 4 * K
        and A > B
    ):
        raise AssertionError("canonical root identities changed")
    return {"p": p, "t": t, "g": g, "T": T, "A": A, "n": n, "K": K, "R": R, "B": B}


def inverse_predecessor(root: dict[str, int], d: int) -> dict[str, int]:
    p = root["p"]
    A = root["A"]
    n = root["n"]
    B = root["B"]
    if not (1 <= d < p and A % d == 0):
        raise AssertionError("d is not a legal inverse full-product divisor")
    M = A // d
    C = p - d
    K = M * C
    R = 4 * M - n
    target_R = (p - 1) * n - 1
    target_K = M * d * (p - 1)
    if not (
        p * n == 4 * M * d + 1
        and p * R + 1 == 4 * K
        and M * d == A
        and M > B
        and R > p
        and target_R == root["R"]
        and target_K == root["K"]
    ):
        raise AssertionError("inverse full-product predecessor changed")
    return {"d": d, "M": M, "C": C, "K": K, "R": R}


def verify_pre_root(root: dict[str, int]) -> dict[str, int]:
    p = root["p"]
    t = root["t"]
    g = root["g"]
    T = root["T"]
    C = (p - 1) // 2
    b = 2 * t * (p - 1) - 1
    R = p * b
    K = T * C
    predecessor = inverse_predecessor(root, g)
    source_rank = (root["B"], K)
    target_rank = (0, p - 1)
    if not (
        predecessor == {"d": g, "M": T, "C": C, "K": K, "R": R}
        and 4 * T - R == root["n"]
        and p * R + 1 == 4 * K
        and p * root["n"] == 4 * T * g + 1
        and R % C == C - 1
        and gcd(C, R - C) == 1
        and gcd(C, K) == C
        and K // C == T
        and source_rank > target_rank
    ):
        raise AssertionError("canonical g pre-root seed changed")
    return {"d": g, "C": C, "M": T, "R": R, "K": K, "b": b}


def verify_whole_carrier_obstruction(
    root: dict[str, int], legal_divisors: list[int]
) -> dict[str, int]:
    """Check the exact X-intersection formula and its three symbolic cases."""
    p = root["p"]
    t = root["t"]
    A = root["A"]
    X = (p + 3) // 4
    if not (
        X == 6 * t + 1
        and gcd(X, A) == 1
        and p == 4 * X - 3
        and A % t == t - 1
    ):
        raise AssertionError("q=1 carrier setup changed")

    for d in legal_divisors:
        predecessor = inverse_predecessor(root, d)
        if not (
            gcd(X, predecessor["K"]) == gcd(X, d + 3)
            and gcd(X, predecessor["K"]) < X
        ):
            raise AssertionError("whole q=1 carrier reached an inverse predecessor")

    d_one = X - 3
    e = 3 * t - 1
    d_two = 2 * X - 3
    d_three = 3 * X - 3
    g = root["g"]
    T = root["T"]
    if not (
        d_one == 2 * e == 6 * t - 2
        and A % d_one == (5 * e + 110) % d_one
        and d_two == 12 * t - 1
        and gcd(d_two, g) == 1
        and (4 * T + 5) % d_two == 0
        and d_three == 18 * t
        and A % t == t - 1
        and all(A % candidate != 0 for candidate in (d_one, d_two, d_three))
    ):
        raise AssertionError("three-case whole-carrier obstruction changed")
    return {"X": X, "d_one": d_one, "d_two": d_two, "d_three": d_three}


def verify_factor_pair_parameter_separation(
    root: dict[str, int], legal_divisors: list[int]
) -> dict[str, object]:
    """Check every standard factor-pair a | (p - 1)/4 is q=1-carrier-coprime."""
    p = root["p"]
    X = (p + 3) // 4
    U = (p - 1) // 4
    parameters = divisors(U)
    retained_carriers = [
        gcd(X, inverse_predecessor(root, d)["K"]) for d in legal_divisors
    ]
    if not (
        U == X - 1
        and p - 1 == 4 * U
        and all(X % retained == 0 for retained in retained_carriers)
        and all(gcd(parameter, X) == 1 for parameter in parameters)
        and all(
            gcd(parameter, retained) == 1
            for parameter in parameters
            for retained in retained_carriers
        )
    ):
        raise AssertionError("factor-pair q=1 parameter separation changed")
    return {
        "X": X,
        "U": U,
        "factor_pair_parameter_count": len(parameters),
        "all_parameters_coprime_to_X": True,
        "all_parameters_coprime_to_retained_carriers": True,
    }


def verify_q_one_g_source_loss(
    root: dict[str, int], legal_divisors: list[int]
) -> dict[str, int]:
    """Check the sharp >= 7 loss of a q=1 G source carrier at a pre-root."""
    p = root["p"]
    X = (p + 3) // 4
    if not all(prime % 3 == 1 for prime in factorization(X)):
        raise AssertionError("control is not a q=1 G endpoint")

    losses: list[int] = []
    for d in legal_divisors:
        predecessor = inverse_predecessor(root, d)
        retained = gcd(X, predecessor["K"])
        loss = X // retained
        if not (
            retained == gcd(X, d + 3)
            and X % retained == 0
            and loss > 1
            and loss >= 7
            and all(prime % 3 == 1 for prime in factorization(loss))
        ):
            raise AssertionError("q=1 G source-loss profile changed")
        losses.append(loss)
    return {"X": X, "minimum_source_loss": min(losses)}


def verify() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for prime in CONTROLS:
        root = canonical_root(prime)
        legal_divisors = [d for d in divisors(root["A"]) if d < prime]
        predecessors = [inverse_predecessor(root, d) for d in legal_divisors]
        if not (
            root["g"] in legal_divisors
            and predecessors[0]["d"] == 1
            and predecessors[0]["M"] == root["A"]
            and predecessors[0]["R"] == root["R"]
            and all(row["M"] > root["B"] and row["R"] > prime for row in predecessors)
        ):
            raise AssertionError("inverse divisor classification changed")
        row: dict[str, object] = {
            "p": prime,
            "legal_divisor_count": len(legal_divisors),
            "pre_root": verify_pre_root(root),
            "whole_carrier_obstruction": verify_whole_carrier_obstruction(
                root, legal_divisors
            ),
            "factor_pair_parameter_separation": verify_factor_pair_parameter_separation(
                root, legal_divisors
            ),
        }
        if all(value % 3 == 1 for value in factorization((prime + 3) // 4)):
            row["q_one_g_source_loss"] = verify_q_one_g_source_loss(
                root, legal_divisors
            )
        rows.append(row)
    p673 = next(row for row in rows if row["p"] == 673)
    root673 = canonical_root(673)
    predecessor673 = inverse_predecessor(root673, 75)
    if not (
        factorization((673 + 3) // 4) == {13: 2}
        and all(prime % 3 == 1 for prime in factorization((673 + 3) // 4))
        and root673["A"] % 75 == 0
        and gcd((673 + 3) // 4, predecessor673["K"]) == 13
        and valuation(predecessor673["K"], 13) == 1
        and p673["factor_pair_parameter_separation"]["U"] == 168
    ):
        raise AssertionError("p=673 partial-overlap control changed")
    p673["partial_overlap"] = {
        "d": 75,
        "shared_prime_power": 13,
        "q_one_source_power": 13**2,
        "target_q_height": valuation(predecessor673["K"], 13),
    }
    p1033 = next(row for row in rows if row["p"] == 1033)
    root1033 = canonical_root(1033)
    predecessor1033 = inverse_predecessor(root1033, 330)
    if not (
        factorization((1033 + 3) // 4) == {7: 1, 37: 1}
        and root1033["A"] % 330 == 0
        and gcd((1033 + 3) // 4, predecessor1033["K"]) == 37
        and (1033 + 3) // 4 // 37 == 7
        and p1033["q_one_g_source_loss"] == {"X": 259, "minimum_source_loss": 7}
        and p1033["factor_pair_parameter_separation"]["U"] == 258
    ):
        raise AssertionError("sharp q=1 G source-loss control changed")
    p1033["sharp_source_loss_control"] = {"d": 330, "retained": 37, "loss": 7}
    return {
        "status": "verified",
        "controls": rows,
        "scope": (
            "Six fixed core primes; all d < p divisors of each canonical root support; "
            "no prime-range, denominator-range, selector-history, or raw-reach search."
        ),
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
