#!/usr/bin/env python3
"""Verify the provenance dispatch for root-stutter norm factors."""

from __future__ import annotations

import argparse
import math

import sympy


def capacity_menu(p: int, r: int, q: int) -> tuple[int, list[int]]:
    m0 = (p * p + p + 1) // 3
    u = math.gcd(2 * r + 1, m0)
    if q == 3 or u % q:
        raise AssertionError("q is not a non-3 capacity factor")
    rho = p % q
    if not (0 < rho < q):
        raise AssertionError("capacity residue is not a unit")
    i = q - rho
    if not (0 < i < q and (p * p + p + 1) % q == 0):
        raise AssertionError("capacity order/source residue failed")
    source_quotient = (p + i) // q
    modulus = 4 * i
    target = (-p * pow(q, -1, modulus)) % modulus
    menu = [t for t in sympy.divisors(source_quotient) if t % modulus == target]
    return i, menu


def check_menu_certificate(p: int, q: int, r: int, expected: list[int]) -> None:
    i, menu = capacity_menu(p, r, q)
    if menu != expected:
        raise AssertionError(f"unexpected q-menu: {menu} != {expected}")
    for t in menu:
        m = q * t
        if (p + m) % 4:
            raise AssertionError("source gap has wrong parity")
        x = (p + m) // 4
        d = i * x
        if x <= 0 or x * x % d or (p * x + d) % m:
            raise AssertionError("menu item did not reconstruct Type I certificate")


def check_stutter_case(p: int, h: int, m: int, e: int) -> None:
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b
    d = m * p + 1 - h
    if not (2 <= h < p and a > 0 and p * a == e * (h - 1) + 1):
        raise AssertionError("stutter identities failed")
    if (p * p + p + 1) % h or norm % h:
        raise AssertionError("cyclotomic/norm divisibility failed")
    if d <= 0 or (p * h + 1) % d or e * d != p * h + 1:
        raise AssertionError("stutter divisor identity failed")


def verify() -> None:
    # Positive and empty capacity menus have exact finite proofs.
    check_menu_certificate(2137, 7, 3, [9])
    check_menu_certificate(457, 7, 3, [])

    # Abstract curve controls: q=3 is degenerate; q=4021 is non-degenerate;
    # q=61 occurs only in the norm quotient for the second control.
    check_stutter_case(25957, 9327, 3, 3532)
    p, h, m, e = 54481, 12063, 13, 944
    check_stutter_case(p, h, m, e)
    a, b = e * m - h, e - 1
    norm = a * a - a * b + b * b
    if not (a % 4021 and (p * a + b) % 4021 == 0):
        raise AssertionError("non-degenerate h-factor bridge changed")
    if h % 61 == 0 or norm % 61 or (p * a + b) % 61 == 0:
        raise AssertionError("quotient-only factor was misclassified")

    # A degenerate h factor has no inverse bridge, but the common-factor implication holds.
    p, h, m, e = 25957, 9327, 3, 3532
    a, b = e * m - h, e - 1
    if not (a % 3 == b % 3 == m % 3 == 0):
        raise AssertionError("degenerate h-factor implication changed")
    print("verified root-stutter provenance dispatch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
