#!/usr/bin/env python3
"""Verify Eisenstein ideal quotients for fixed strict root-carry receipts."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_root_capacity_general_endpoint_divisor_gate import chart


Pair = tuple[int, int]


def multiply(left: Pair, right: Pair) -> Pair:
    """Multiply pairs representing a + b*omega, with omega^2 + omega + 1 = 0."""
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


def conjugate(value: Pair) -> Pair:
    a, b = value
    return a - b, -b


def norm(value: Pair) -> int:
    a, b = value
    return a * a - a * b + b * b


def factor(value: int) -> dict[int, int]:
    out: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            out[divisor] = out.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def ideal_generator(p: int, h: int) -> Pair:
    """Find gamma with N(gamma)=h and gamma(omega=p)=0 modulo h."""
    bound = 2 * isqrt(h) + 2
    for b in range(-bound, bound + 1):
        for a in range(-bound, bound + 1):
            candidate = a, b
            if norm(candidate) == h and (a + b * p) % h == 0:
                return candidate
    raise AssertionError("failed to find the principal ideal generator")


def divide_by_generator(alpha: Pair, gamma: Pair, h: int) -> Pair | None:
    """Return alpha/gamma when it is integral in Z[omega]."""
    numerator = multiply(alpha, conjugate(gamma))
    if numerator[0] % h or numerator[1] % h:
        return None
    return numerator[0] // h, numerator[1] // h


def strict_data(p: int, r: int) -> dict[str, int | Pair]:
    receipt = chart(p, r)
    h = receipt["h"]
    d_value = receipt["D"]
    c = (d_value * pow(h - 1, -1, p)) % p
    if not (
        p % 24 == 1
        and receipt["u"] < receipt["M"]
        and receipt["E"] % p != 0
        and 1 <= c <= p - 2
    ):
        raise AssertionError("control is outside the actual strict proper-root domain")

    n = c if c % 2 == 0 else p - c
    delta = p - n
    tau = 1 if c % 2 else -1
    numerator = d_value - tau * delta * (h - 1)
    if numerator % p:
        raise AssertionError("pre-cofactor coordinate is not integral")
    s = numerator // p
    v = (p * p + p + 1) // h
    t = v * s * s + tau * (2 * p + 1) * s * delta + h * delta * delta
    alpha = d_value + tau * delta, -s
    if not (
        n % 2 == 0
        and delta % 2 == 1
        and (c - tau * delta) % p == 0
        and norm(alpha) == h * t
        and t > 0
    ):
        raise AssertionError("strict Eisenstein norm identities changed")
    return {
        "p": p,
        "r": r,
        "h": h,
        "D": d_value,
        "c": c,
        "n": n,
        "delta": delta,
        "tau": tau,
        "s": s,
        "v": v,
        "t": t,
        "alpha": alpha,
    }


def verify_control(
    p: int, r: int, expected: tuple[int, int, int, int, int, int]
) -> dict[str, int | Pair]:
    data = strict_data(p, r)
    expected_data = (
        data["h"],
        data["D"],
        data["c"],
        data["delta"],
        data["s"],
        data["t"],
    )
    if expected_data != expected:
        raise AssertionError(f"fixed strict receipt changed: {expected_data}")

    gamma = ideal_generator(p, int(data["h"]))
    beta = divide_by_generator(data["alpha"], gamma, int(data["h"]))
    if beta is None:
        raise AssertionError("alpha is not divisible by its Eisenstein ideal generator")
    if not (
        norm(gamma) == data["h"]
        and (gamma[0] + gamma[1] * p) % int(data["h"]) == 0
        and multiply(gamma, beta) == data["alpha"]
        and norm(beta) == data["t"]
    ):
        raise AssertionError("Eisenstein ideal quotient changed")

    for prime, exponent in factor(int(data["t"])).items():
        if prime % 3 == 2:
            if exponent % 2:
                raise AssertionError("an inert prime has odd norm valuation")
            if not (
                int(data["D"]) % prime == 0
                and int(data["delta"]) % prime == 0
                and int(data["s"]) % prime == 0
            ):
                raise AssertionError("inert norm factor lost its exact receipt location")
    return data


def verify() -> None:
    low = verify_control(73, 3, (3, 220, 37, 37, 2, 22_189))
    shared = verify_control(193, 3, (21, 2, 58, 135, 14, 763))
    unit = verify_control(313, 271, (543, 8, 298, 15, 26, 1))
    inert = verify_control(577, 66, (57, 10, 62, 515, 50, 4_075))

    if not (
        gcd(int(shared["h"]), int(shared["t"])) == 7
        and int(unit["t"]) == 1
        and factor(int(inert["t"])) == {5: 2, 163: 1}
        and all(int(inert[key]) % 5 == 0 for key in ("D", "delta", "s"))
        and low["tau"] == 1
        and unit["tau"] == inert["tau"] == -1
    ):
        raise AssertionError("sharp Eisenstein quotient boundaries changed")

    gamma = ideal_generator(313, int(unit["h"]))
    wrong_alpha = int(unit["alpha"][0]) + 1, int(unit["alpha"][1])
    if divide_by_generator(wrong_alpha, gamma, int(unit["h"])) is not None:
        raise AssertionError("one-unit receipt perturbation still lies in the ideal")

    print(
        "verified strict-root Eisenstein ideal quotients, inert-factor localization, "
        "the unit fiber, and the non-coprime boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
