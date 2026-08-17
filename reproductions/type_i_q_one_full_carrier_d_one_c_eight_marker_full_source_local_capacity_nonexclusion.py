#!/usr/bin/env python3
"""Verify the full-source local-capacity barrier for the c=8 marker.

This is a finite arithmetic verifier.  It checks the local count formula and
two formal controls, one for each possible location of the distinguished 47.
The controls establish only the full M congruence projection, not q | V,
primality, positive endpoints, or an actual marker.
"""

from __future__ import annotations

import argparse
from math import gcd


FORMAL_CONTROLS = ((141, 367), (67, 1423))


def source_data(s: int) -> tuple[int, int, int, int, int]:
    """Return p, L, E, M, V for a c=8 source."""
    p = 48 * s + 1
    linear = 176 * s + 5
    quadratic = 3168 * s * s + 24 * s - 1
    support = 9 * s * linear * quadratic
    value = (121 * p**4 - 396 * p**3 + 346 * p**2 + 4 * p - 79) // 4
    return p, linear, quadratic, support, value


def raw_q_modulus(p: int, rho: int, modulus: int) -> int:
    """Evaluate Q(rho) modulo an odd source modulus."""
    numerator = 32 * p * p + 32 * p - 79 - 47 * p * rho
    return numerator * pow(32, -1, modulus) % modulus


def local_capacity_formula(p: int, prime: int, exponent: int) -> int:
    """Return the exact number of allowed rho residues modulo prime**exponent."""
    if prime == 47:
        return 46 * 47 ** (exponent - 1)
    roots_to_exclude = 1 + int((p * p + p - 1) % prime != 0)
    return prime ** (exponent - 1) * (prime - roots_to_exclude)


def count_local_capacity(p: int, prime: int, exponent: int) -> int:
    """Count the two unit conditions directly for one fixed prime power."""
    modulus = prime**exponent
    return sum(
        gcd(1 + p * rho, modulus) == 1
        and gcd(raw_q_modulus(p, rho, modulus), modulus) == 1
        for rho in range(modulus)
    )


def crt(left: int, left_modulus: int, right: int, right_modulus: int) -> int:
    """Return the least nonnegative CRT solution for coprime moduli."""
    if gcd(left_modulus, right_modulus) != 1:
        raise AssertionError("CRT moduli must be coprime")
    return (
        left
        + left_modulus
        * ((right - left) * pow(left_modulus, -1, right_modulus) % right_modulus)
    ) % (left_modulus * right_modulus)


def odd_part(value: int) -> int:
    """Remove the dyadic part of a positive integer."""
    while value % 2 == 0:
        value //= 2
    return value


def verify_local_capacity_formula() -> None:
    """Replay both ordinary and 47-primary local count cases."""
    rows = (
        (6769, 3, 3),
        (6769, 13, 1),
        (6769, 1669, 1),
        (106033, 47, 1),
    )
    for p, prime, exponent in rows:
        actual = count_local_capacity(p, prime, exponent)
        expected = local_capacity_formula(p, prime, exponent)
        if actual != expected or expected <= 0:
            raise AssertionError("local marker capacity formula changed")

    # For p = 1 modulo 3, the two excluded classes are rho = 0 and 2;
    # the surviving class is exactly the marker's rho = 1 modulo 3 ray.
    surviving_mod_three = tuple(
        rho
        for rho in range(3)
        if gcd(1 + 6769 * rho, 3) == 1
        and gcd(raw_q_modulus(6769, rho, 3), 3) == 1
    )
    if surviving_mod_three != (1,):
        raise AssertionError("marker mod-three local capacity changed")

    # This is a fixed CRT composition of two prime-power factors of M/47
    # for the first formal control, not a source or factor search.
    composite_modulus = 3**3 * 13
    composite_count = sum(
        gcd(1 + 6769 * rho, composite_modulus) == 1
        and gcd(raw_q_modulus(6769, rho, composite_modulus), composite_modulus)
        == 1
        for rho in range(composite_modulus)
    )
    expected_composite = (
        local_capacity_formula(6769, 3, 3)
        * local_capacity_formula(6769, 13, 1)
    )
    if composite_count != expected_composite:
        raise AssertionError("prime-power capacity CRT product changed")


def verify_formal_controls() -> None:
    """Check full M/47 projection on both possible 47 source locations."""
    expected_branches = ((0, 1, 1), (20, 21, 38))
    branches = []
    for s, rho in FORMAL_CONTROLS:
        p, linear, quadratic, support, value = source_data(s)
        reduced_support, remainder = divmod(support, 47)
        if remainder or s % 2 == 0 or gcd(value, support) != 1:
            raise AssertionError("formal control no longer has the marker source shape")

        affine = 1 + p * rho
        n, remainder = divmod(affine, 32)
        if remainder:
            raise AssertionError("formal rho no longer gives an integral lift")
        q_numerator = 32 * p * p + 32 * p - 79 - 47 * p * rho
        q, remainder = divmod(q_numerator, 32)
        if remainder:
            raise AssertionError("formal rho no longer gives an integral q")
        if not (
            p * rho % 512 == 511
            and rho % 3 == 1
            and q % 16 == 1
            and gcd(n, reduced_support) == 1
            and gcd(q, support) == 1
            and gcd(support, p * p + p - 1 - q) == 47
        ):
            raise AssertionError("formal marker source-unit lift changed")

        a_mod_support = value * pow(q, -1, support) % support
        t_mod_support = (a_mod_support - 8) * pow(p, -1, support) % support
        t = crt(t_mod_support, support, 7, 16)
        a = 8 + p * t
        r_value, remainder = divmod(32 * support - 1, p)
        if remainder:
            raise AssertionError("c=8 source R reconstruction changed")
        if not (
            (q * a - value) % support == 0
            and gcd(a, support) == 1
            and (r_value - a) % 47 == 0
            and t % 3 == 2
            and t % 16 == 7
            and a % 16 == 15
        ):
            raise AssertionError("q/a full-M local projection changed")

        in_s = s % 47 == 0
        in_linear = linear % 47 == 0
        if not (in_s ^ in_linear):
            raise AssertionError("47 source placement changed")
        reduced_s = s // 47 if in_s else s
        reduced_linear = linear // 47 if in_linear else linear
        source_odd = odd_part(reduced_s)
        if not (
            gcd(source_odd, rho + 1) == 1
            and gcd(reduced_linear, 4 * rho - 11) == 1
            and gcd(quadratic, affine) == 1
        ):
            raise AssertionError("source allocation projection changed")
        branches.append((s % 47, p % 47, q % 47))
    if tuple(branches) != expected_branches:
        raise AssertionError("the two formal 47 branches changed")


def verify() -> None:
    verify_local_capacity_formula()
    verify_formal_controls()
    print(
        "verified c=8 marker full-source local capacity: positive prime-power "
        "counts, CRT composition, and both formal 47-placement projections"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
