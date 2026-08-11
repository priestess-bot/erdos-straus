#!/usr/bin/env python3
"""Verify the exact R=11, gap-7, gap-11 terminal/descent dispatch."""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the four fixed controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factor(value: int) -> tuple[tuple[int, int], ...]:
    """Factor only the small fixed-control integers."""
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check a positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def divisor_box_residues(factors: tuple[tuple[int, int], ...], modulus: int) -> set[int]:
    """Return all residues of divisors of the square of a factored integer."""
    residues = {1}
    for prime, exponent in factors:
        residues = {
            residue * pow(prime, power, modulus) % modulus
            for residue in residues
            for power in range(2 * exponent + 1)
        }
    return residues


def square_divisors(factors: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    """Enumerate divisors of a fixed small square for a terminal control."""
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(2 * exponent + 1)
        ]
    return tuple(divisors)


def signed_ratio_residues(factors: tuple[tuple[int, int], ...], modulus: int) -> set[int]:
    """Return the full signed-ratio box of a factored modulus unit."""
    residues = {1}
    for prime, exponent in factors:
        residues = {
            residue * pow(prime, signed_power, modulus) % modulus
            for residue in residues
            for signed_power in range(-exponent, exponent + 1)
        }
    return residues


def r11_fixed_tail_miss(factors: tuple[tuple[int, int], ...]) -> bool:
    """Apply the exact two-pattern R=11 fixed-tail residual theorem."""
    residues = [prime % 11 for prime, exponent in factors for _ in range(exponent)]
    if any(residue in {7, 8, 10} for residue in residues):
        return False
    all_qr = all(residue in {1, 3, 4, 5, 9} for residue in residues)
    paired = (
        residues.count(2) == 1
        and residues.count(6) == 1
        and all(residue in {1, 2, 6} for residue in residues)
    )
    actual_miss = not divisor_box_residues(factors, 11).intersection({7, 8, 10})
    if actual_miss != (all_qr or paired):
        raise AssertionError("R=11 fixed-tail residual classification changed")
    return actual_miss


def r11_terminal(*, p: int, h: int, factors: tuple[tuple[int, int], ...]) -> dict[str, int] | None:
    """Construct the fixed pK terminal from an actual divisor of N squared."""
    N = 22 * h + 1
    K = 3 * N
    multipliers = {8: 1, 10: 3, 7: 9}
    for divisor in square_divisors(factors):
        if divisor % 11 not in multipliers:
            continue
        e = multipliers[divisor % 11] * divisor
        first = (K + e) // 11
        second = (K + K * K // e) // 11
        if not (
            K * K % e == 0
            and (K + e) % 11 == 0
            and (K + K * K // e) % 11 == 0
            and (11 * first - K) * (11 * second - K) == K * K
        ):
            raise AssertionError("R=11 fixed-tail reconstruction failed")
        assert_egyptian_identity(p, (first, second, p * K))
        return {"d": divisor, "e": e, "u": first, "v": second, "K": K}
    return None


def gap7_descent(*, p: int, h: int) -> dict[str, int] | None:
    """Build the explicit gap-7 two-tail descent from one nonresidue factor."""
    u = 3 * h + 1
    for prime, _ in factor(u):
        if prime % 7 in {3, 5, 6}:
            choices = {1: (1, 1), 2: (2, 1), 4: (1, 2)}
            a, b = choices[(-prime) % 7]
            A, B = a, b * prime
            x = 2 * u
            C = x // (A * B)
            K = (A + B) // 7
            if not (
                x % (A * B) == 0
                and (A + B) % 7 == 0
                and gcd(A, B) == 1
                and A <= B
            ):
                raise AssertionError("gap-7 factor-pair construction failed")
            n = (p + 7) // 8
            small_terms = (x, A * C * K, B * C * K)
            lifted_terms = (x, p * A * C * K, p * B * C * K)
            assert_egyptian_identity(n, small_terms)
            assert_egyptian_identity(p, lifted_terms)
            return {"r": prime, "A": A, "B": B, "C": C, "K": K, "n": n}
    return None


def gap11_descent(*, p: int, h: int) -> dict[str, int] | None:
    """Find and replay one complete signed-ratio gap-11 factor-pair descent."""
    q = 2 * h + 1
    x = 3 * q
    factors = factor(x)
    states = [(1, 1, 1)]
    for prime, exponent in factors:
        next_states = []
        for A, B, C in states:
            for alpha, beta in product(range(exponent + 1), repeat=2):
                if alpha + beta <= exponent:
                    next_states.append(
                        (A * prime**alpha, B * prime**beta, C * prime ** (exponent - alpha - beta))
                    )
        states = next_states
    for A, B, C in states:
        if A * pow(B, -1, 11) % 11 != 10:
            continue
        if A > B:
            A, B = B, A
        K = (A + B) // 11
        if not ((A + B) % 11 == 0 and gcd(A, B) == 1):
            raise AssertionError("gap-11 signed-ratio reconstruction failed")
        small_terms = (x, A * C * K, B * C * K)
        lifted_terms = (x, p * A * C * K, p * B * C * K)
        assert_egyptian_identity(q, small_terms)
        assert_egyptian_identity(p, lifted_terms)
        return {"A": A, "B": B, "C": C, "K": K, "n": q}
    return None


def dispatch(*, p: int) -> dict[str, object]:
    """Replay the terminal-first R11, gap-7, gap-11 order for one core prime."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime")
    h = (p - 1) // 24
    N = 22 * h + 1
    u = 3 * h + 1
    q = 2 * h + 1
    n_factors = factor(N)
    r11_miss = r11_fixed_tail_miss(n_factors)
    r11 = r11_terminal(p=p, h=h, factors=n_factors)
    gap7 = gap7_descent(p=p, h=h)
    gap11 = gap11_descent(p=p, h=h)
    if (r11 is None) != r11_miss:
        raise AssertionError("R=11 terminal and residual branches disagreed")
    if not r11_miss:
        branch = "r11_terminal"
    elif gap7 is not None:
        branch = "gap7_strict_descent"
    elif gap11 is not None:
        branch = "gap11_strict_descent"
    else:
        branch = "joint_residual"
    return {
        "p": p,
        "h": h,
        "N": N,
        "N_factors": n_factors,
        "u": u,
        "u_factors": factor(u),
        "q": q,
        "x11_factors": factor(3 * q),
        "r11_fixed_tail_miss": r11_miss,
        "r11": r11,
        "gap7": gap7,
        "gap11": gap11,
        "branch": branch,
    }


def build_result() -> dict[str, object]:
    """Verify one control for each branch without a coverage scan."""
    records = {p: dispatch(p=p) for p in (313, 241, 337, 1201)}
    if not (
        records[313]["branch"] == "r11_terminal"
        and records[313]["r11"]["d"] % 11 in {7, 8, 10}
        and records[241]["branch"] == "gap7_strict_descent"
        and records[241]["gap7"]["n"] == 31
        and records[337]["branch"] == "gap11_strict_descent"
        and records[337]["gap11"] == {"A": 1, "B": 87, "C": 1, "K": 8, "n": 29}
        and records[1201]["branch"] == "joint_residual"
    ):
        raise AssertionError("joint dispatch controls changed")
    return {
        "certificate_type": "r11_gap7_gap11_terminal_descent_dispatch_v1",
        "scope": "A terminal-first subselector; joint residual is explicitly retained.",
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified R=11, gap-7, gap-11 joint dispatch controls")


if __name__ == "__main__":
    main()
