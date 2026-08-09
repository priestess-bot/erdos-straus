#!/usr/bin/env python3
"""Verify high-capacity small-d routes and arithmetic fold candidates."""

from __future__ import annotations

import argparse


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def divisors(value: int) -> list[int]:
    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append((remaining, 1))

    values = [1]
    for prime, exponent in factors:
        values = [
            base * prime**power
            for base in values
            for power in range(exponent + 1)
        ]
    return sorted(values)


def floor_shell_threshold(B: int, A: int) -> int:
    """Least bounded carrier that strictly lowers floor(B / A)."""
    level = B // A
    assert level >= 1
    threshold = B // level + 1
    assert A < threshold <= 2 * A
    return threshold


def factor_route(p: int, n: int, M: int, d: int, A: int, b: int, g: int) -> dict[str, int]:
    assert 1 < g and b % g == 0 and d * g < p
    target_M, target_d = M // g, d * g
    assert target_M < M and target_M % A == 0
    assert p * n == 4 * target_M * target_d + 1
    R = 4 * target_M - n
    K = target_M * (p - target_d)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": target_M, "d": target_d, "n": n, "g": g}


def exchange_route(p: int, n: int, M: int, d: int, A: int, b: int) -> dict[str, int]:
    assert d < b < p
    target_M, target_d = A * d, b
    assert target_M < M and target_M % A == 0
    assert p * n == 4 * target_M * target_d + 1
    R = 4 * target_M - n
    K = target_M * (p - target_d)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": target_M, "d": target_d, "n": n}


def fold_route(p: int, n: int, M: int, d: int, A: int, carrier: int) -> dict[str, int]:
    B = (p - 1) ** 2 // 4
    threshold = floor_shell_threshold(B, A)
    assert threshold <= carrier <= B
    assert (M * d) % carrier == 0 and B // carrier < B // A
    quotient, remainder = divmod(M * d // carrier, p)
    assert 1 <= remainder < p
    target_n = n - 4 * carrier * quotient
    assert target_n > 0 and p * target_n == 4 * carrier * remainder + 1
    R = 4 * carrier - target_n
    K = carrier * (p - remainder)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": carrier, "d": remainder, "n": target_n, "h": quotient}


def total_cofactor_fold_route(
    p: int, n: int, M: int, d: int, A: int, b: int
) -> dict[str, int]:
    """Fold the full support cofactor, preserving A and strictly lowering R."""
    assert b > 1 and M == A * b
    h, delta = divmod(b * d, p)
    assert 1 <= delta < p and b * (p - d) > p
    target_M = A
    target_n = n - 4 * target_M * h
    target_R = 4 * target_M - target_n
    target_K = target_M * (p - delta)
    source_R = 4 * M - n
    assert target_n > 0 and p * target_n == 4 * target_M * delta + 1
    assert target_R > 0 and target_R % 4 == 3 and target_K % A == 0
    assert p * target_R + 1 == 4 * target_K
    assert target_R < source_R
    return {
        "M": target_M,
        "d": delta,
        "n": target_n,
        "R": target_R,
        "K": target_K,
        "h": h,
    }


def dual_route(p: int, M: int, d: int, A: int) -> dict[str, int]:
    B = (p - 1) ** 2 // 4
    threshold = floor_shell_threshold(B, A)
    r = M % p
    P = r * d
    s, remainder = divmod(4 * P + 1, p)
    assert remainder == 0 and threshold <= P < B
    assert B // P < B // A
    R, K = 4 * P - s, P * (p - 1)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": P, "R": R, "K": K, "s": s}


def classify(p: int, n: int, M: int, d: int, A: int) -> str:
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4
    assert is_prime(p) and p % 24 == 1 and p >= 73
    assert B < M and M >= 2 * B and c <= A <= B and M % A == 0
    assert 1 <= d < p and d * d < p and p * n == 4 * M * d + 1
    r = M % p
    assert 1 <= r < p
    s, remainder = divmod(4 * r * d + 1, p)
    assert remainder == 0 and 1 <= s <= 4 * d - 1
    P = r * d
    assert c <= P < B
    b = M // A
    assert b > 1 and b != p
    threshold = floor_shell_threshold(B, A)

    if P >= threshold:
        dual_route(p, M, d, A)
        return "dual"

    movable = [candidate for candidate in divisors(b) if candidate > 1 and d * candidate < p]
    if movable:
        factor_route(p, n, M, d, A, b, max(movable))
        return "factor"
    if d < b < p:
        exchange_route(p, n, M, d, A, b)
        return "exchange"
    shell_divisors = [candidate for candidate in divisors(b * d) if threshold <= candidate <= B]
    if shell_divisors:
        carrier = max(shell_divisors)
        fold_route(p, n, M, d, A, carrier)
        return "cofactor_divisor_fold"

    assert P < threshold and b > p and not shell_divisors
    assert not movable
    assert b > B or b < threshold
    total_cofactor_fold_route(p, n, M, d, A, b)
    return "total_cofactor_candidate"


def verify() -> None:
    fixtures = {
        "dual": (73, 1129, 5151, 4, 51),
        "sharp_dual": (73, 28361, 129397, 4, 83),
        "factor": (73, 145, 2646, 1, 49),
        "exchange": (73, 337, 3075, 2, 75),
        "cofactor_divisor_fold": (73, 161, 2938, 1, 26),
        "intermediate_divisor_fold": (73, 27505, 501966, 1, 18),
        "sub_double_cofactor_fold": (73, 317, 5785, 1, 65),
        "composite_shell_fold": (73, 23381, 426703, 1, 53),
        "dilated_cofactor_fold": (73, 7553, 68921, 2, 41),
        "floor_shell_residual": (73, 645, 11771, 1, 149),
        "ultra_prime_residual": (73, 1585, 28926, 1, 18),
        "composite_gap_residual": (73, 37617, 686510, 1, 110),
    }
    routes = {name: classify(*fixture) for name, fixture in fixtures.items()}
    assert routes == {
        "dual": "dual",
        "sharp_dual": "dual",
        "factor": "factor",
        "exchange": "exchange",
        "cofactor_divisor_fold": "cofactor_divisor_fold",
        "intermediate_divisor_fold": "cofactor_divisor_fold",
        "sub_double_cofactor_fold": "cofactor_divisor_fold",
        "composite_shell_fold": "cofactor_divisor_fold",
        "dilated_cofactor_fold": "cofactor_divisor_fold",
        "floor_shell_residual": "total_cofactor_candidate",
        "ultra_prime_residual": "total_cofactor_candidate",
        "composite_gap_residual": "total_cofactor_candidate",
    }
    print("verified high-capacity small-d routes and arithmetic cofactor fold candidates")
    for name, fixture in fixtures.items():
        p, n, M, d, A = fixture
        B = (p - 1) ** 2 // 4
        r = M % p
        P = r * d
        b = M // A
        threshold = floor_shell_threshold(B, A)
        shell_divisors = [candidate for candidate in divisors(b * d) if threshold <= candidate <= B]
        print(
            name,
            "p", p,
            "n", n,
            "M", M,
            "d", d,
            "A", A,
            "r", r,
            "P", P,
            "b", b,
            "threshold", threshold,
            "shell", shell_divisors,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
