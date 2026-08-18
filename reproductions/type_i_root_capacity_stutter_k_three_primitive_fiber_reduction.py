#!/usr/bin/env python3
"""Verify the exact k=3 proper-root primitive-fiber reduction.

The stored controls are arithmetic shadows, deliberately not actual recursive
states. This program checks the fixed-d, fixed-gap, fixed-j, and fixed-t
reductions, the shared A=1/d=1 boundary, and the core-congruent/non-proper
distinction.
It does not scan fibers, primes, sources, certificates, or selector history.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class KThreeFiber:
    """One integral k=3 stutter-curve point after primitive reduction."""

    A: int
    B: int
    H: int
    e: int
    M: int
    m: int
    p: int
    h: int
    a: int
    b: int
    D: int
    k: int
    d: int
    c: int


def factor(value: int) -> dict[int, int]:
    """Return the factorization of one positive fixed-fiber integer."""
    if value < 1:
        raise ValueError("value must be positive")
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


def divisors(value: int) -> tuple[int, ...]:
    """Enumerate positive divisors of one fixed finite-fiber constant."""
    result = [1]
    for prime, exponent in factor(value).items():
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return tuple(sorted(result))


def reconstruct(A: int, B: int) -> KThreeFiber | None:
    """Recover an integral k=3 curve point, or reject a failed gate."""
    if A <= 0 or B <= 0 or gcd(A, B) != 1:
        return None

    H = A * A - A * B + B * B
    e = 3 * B + 1
    if (A + H) % e:
        return None
    M = (A + H) // e
    numerator_p = e * H - B
    if numerator_p % A:
        return None
    p = numerator_p // A

    m, h, a, b = 3 * M, 3 * H, 3 * A, 3 * B
    D = m * p + 1 - h
    norm = a * a - a * b + b * b
    if norm % h:
        return None
    k = norm // h
    numerator_d = (3 * A + 2) ** 2 - 3
    if numerator_d % e:
        return None
    d = numerator_d // e
    F = 3 * B * B + B - 1
    if F % A:
        return None
    c = F // A

    data = KThreeFiber(A, B, H, e, M, m, p, h, a, b, D, k, d, c)
    verify_reduction(data)
    return data


def verify_reduction(data: KThreeFiber) -> None:
    """Check all exact identities used by the k=3 fiber reduction."""
    A, B, H, e, M, m, p, h, a, b, D, k, d, c = (
        data.A,
        data.B,
        data.H,
        data.e,
        data.M,
        data.m,
        data.p,
        data.h,
        data.a,
        data.b,
        data.D,
        data.k,
        data.d,
        data.c,
    )
    norm = a * a - a * b + b * b
    C_d = 3 * d * d + d - 1
    pell_left = (6 * B + 1) ** 2 - 12 * A * c
    pell_right = (3 * A + 2) ** 2 - e * d

    if not (
        H == A * A - A * B + B * B
        and e == 3 * B + 1
        and A + H == e * M
        and p * A + B == e * H
        and a == 3 * A
        and b == 3 * B
        and h == 3 * H
        and m == 3 * M
        and a == e * m - h
        and p * a + b == e * h
        and D == m * p + 1 - h
        and e * D == p * h + 1
        and norm == h * k
        and k == 3
        and gcd(A, B) == 1
        and A * c == 3 * B * B + B - 1
        and e * d == (3 * A + 2) ** 2 - 3
        and 9 * (A + H)
        == (3 * A + 2) ** 2 - 3 - e * (3 * A - 3 * B + 1)
        and pell_left == 13
        and pell_right == 3
        and gcd(A, d) == 1
        and C_d % A == 0
        and 3 * d * d * (3 * B * B + B - 1) + C_d
        == 3 * A * (3 * A + 4) * (9 * A * A + 12 * A - d + 2)
        and p == c * (B - A) + 3 * A * B + A - 1
    ):
        raise AssertionError("k=3 primitive-fiber identities changed")


def fixed_d_fiber(d: int) -> tuple[KThreeFiber, ...]:
    """Enumerate the necessary finite A-divisor fiber for one fixed d only."""
    if d <= 0:
        raise ValueError("d must be positive")
    candidates: list[KThreeFiber] = []
    for A in divisors(3 * d * d + d - 1):
        numerator_e = (3 * A + 2) ** 2 - 3
        if numerator_e % d:
            continue
        e = numerator_e // d
        if (e - 1) % 3:
            continue
        B = (e - 1) // 3
        data = reconstruct(A, B)
        if data is not None and data.d == d and data.A < data.B:
            candidates.append(data)
    return tuple(candidates)


def verify_gap_reduction(data: KThreeFiber) -> None:
    """Check the dual finite fiber indexed by rho=B-A for a proper curve point."""
    if not data.A < data.B:
        raise ValueError("gap reduction requires the proper A<B branch")
    rho = data.B - data.A
    e = 3 * (data.A + rho) + 1
    F_rho = 9 * rho * rho - 6 * rho - 2
    G_rho = 3 * rho * rho + rho - 1
    if F_rho <= 0 or F_rho % e:
        raise AssertionError("gap fiber lost its M-integrality divisor gate")
    s = F_rho // e
    if not (
        rho >= 2
        and data.H == data.A * data.A + data.A * rho + rho * rho
        and data.e == e
        and G_rho % data.A == 0
        and gcd(data.A, rho) == 1
        and s % 3 == 1
        and 9 * data.M == 3 * data.A + 2 + s
        and data.m == data.A + (s + 2) // 3
        and data.d == 3 * (data.m - rho) + 1
    ):
        raise AssertionError("k=3 dual gap-fiber identities changed")


def fixed_gap_fiber(rho: int) -> tuple[KThreeFiber, ...]:
    """Enumerate the exact finite primitive fiber for one fixed gap rho=B-A."""
    if rho <= 0:
        raise ValueError("rho must be positive")
    F_rho = 9 * rho * rho - 6 * rho - 2
    if F_rho <= 0:
        return ()
    G_rho = 3 * rho * rho + rho - 1
    candidates: list[KThreeFiber] = []
    for e in divisors(F_rho):
        if e <= 3 * rho + 1 or (e - 3 * rho - 1) % 3:
            continue
        A = (e - 3 * rho - 1) // 3
        if A <= 0 or gcd(A, rho) != 1 or G_rho % A:
            continue
        data = reconstruct(A, A + rho)
        if data is not None and data.A < data.B:
            verify_gap_reduction(data)
            candidates.append(data)
    return tuple(candidates)


def verify_defect_reduction(data: KThreeFiber) -> None:
    """Check the third finite fiber indexed by j=m-(B-A)."""
    if not data.A < data.B:
        raise ValueError("defect reduction requires the proper A<B branch")
    rho = data.B - data.A
    j = data.m - rho
    d = 3 * j + 1
    L_j = 9 * j * j + 7 * j + 1
    if not (
        j >= 0
        and data.d == d
        and rho * d + j == 3 * data.A * (data.A - j + 1)
        and L_j % data.A == 0
        and gcd(d, L_j) == 1
    ):
        raise AssertionError("k=3 fixed-j fiber identities changed")


def fixed_j_fiber(j: int) -> tuple[KThreeFiber, ...]:
    """Enumerate the exact finite primitive fiber for one fixed j=m-(B-A)."""
    if j < 0:
        raise ValueError("j must be nonnegative")
    d = 3 * j + 1
    L_j = 9 * j * j + 7 * j + 1
    candidates: list[KThreeFiber] = []
    for A in divisors(L_j):
        numerator_rho = 3 * A * (A - j + 1) - j
        if numerator_rho <= 0 or numerator_rho % d:
            continue
        rho = numerator_rho // d
        if gcd(A, rho) != 1:
            continue
        data = reconstruct(A, A + rho)
        if data is not None and data.A < data.B and data.m - rho == j:
            verify_defect_reduction(data)
            candidates.append(data)
    return tuple(candidates)


def verify_vieta_gap_reduction(data: KThreeFiber) -> None:
    """Check the fourth finite fiber indexed by the actual gap t=B-m."""
    if not data.A < data.B:
        raise ValueError("Vieta-gap reduction requires the proper A<B branch")
    A, B, e, m = data.A, data.B, data.e, data.m
    rho = B - A
    t = B - m
    j = m - rho
    d = 3 * j + 1
    C_t = 9 * t * t - 7 * t + 1
    P_t = 9 * t * t + 6 * t - 2
    if not (
        A < m < B
        and t >= 1
        and t == A - j
        and data.d == d
        and C_t % A == 0
        and P_t % d == 0
        and rho * d + j == 3 * A * (t + 1)
        and e * d == d * (3 * A + 3 * t + 3) + P_t
    ):
        raise AssertionError("k=3 fixed-t Vieta-gap identities changed")


def fixed_vieta_gap_fiber(t: int) -> tuple[KThreeFiber, ...]:
    """Enumerate the exact finite primitive fiber for one fixed t=B-m."""
    if t <= 0:
        raise ValueError("t must be positive")
    P_t = 9 * t * t + 6 * t - 2
    C_t = 9 * t * t - 7 * t + 1
    candidates: list[KThreeFiber] = []
    for d in divisors(P_t):
        if d % 3 != 1:
            continue
        j = (d - 1) // 3
        A = t + j
        if C_t % A:
            continue
        numerator_rho = 3 * A * (t + 1) - j
        if numerator_rho <= 0 or numerator_rho % d:
            continue
        rho = numerator_rho // d
        if gcd(A, rho) != 1:
            continue
        data = reconstruct(A, A + rho)
        if data is not None and data.A < data.B and data.B - data.m == t:
            verify_vieta_gap_reduction(data)
            candidates.append(data)
    return tuple(candidates)


def vieta_companion_second_gate_numerator(A: int, j: int) -> int:
    """Return the second primitive gate numerator at the B-Vieta companion."""
    e_j = 3 * j + 1
    H_j = A * A - A * j + j * j
    return e_j * H_j - j


def verify_vieta_companion(data: KThreeFiber) -> tuple[int, int]:
    """Check the same-M B-Vieta companion and its second-gate numerator."""
    if not data.A < data.B:
        raise ValueError("Vieta companion requires the proper A<B branch")
    A, B, M = data.A, data.B, data.M
    j = data.m - (B - A)
    e_j = 3 * j + 1
    H_j = A * A - A * j + j * j
    polynomial_at_B = B * B - (A + 3 * M) * B + A * A + A - M
    polynomial_at_j = j * j - (A + 3 * M) * j + A * A + A - M
    numerator = vieta_companion_second_gate_numerator(A, j)
    second_gate = 3 * j * j + j - 1
    L_j = 9 * j * j + 7 * j + 1
    if not (
        j >= 0
        and A + H_j == e_j * M
        and polynomial_at_B == 0
        and polynomial_at_j == 0
        and gcd(A, j) == 1
        and L_j % A == 0
        and numerator == j * second_gate + A * (3 * j + 1) * (A - j)
    ):
        raise AssertionError("k=3 Vieta companion identities changed")
    return j, numerator


def verify_d_one_boundary() -> None:
    """Replay the sole d=1 curve point and its core-congruence failure."""
    rows = fixed_d_fiber(1)
    if len(rows) != 1:
        raise AssertionError("d=1 fiber no longer has one primitive proper curve point")
    data = rows[0]
    cyclotomic = data.p * data.p + data.p + 1
    if not (
        (data.A, data.B, data.H, data.e, data.M, data.p, data.h, data.d)
        == (1, 7, 43, 22, 2, 939, 129, 1)
        and data.A < data.B
        and data.a < data.e
        and data.p % 24 == 3
        and cyclotomic % data.h == 43
    ):
        raise AssertionError("d=1 core-boundary control changed")


def verify_gap_boundary() -> None:
    """Replay the dual gap fiber and the exact A=1 boundary without a scan."""
    if fixed_gap_fiber(1):
        raise AssertionError("rho=1 cannot carry a positive primitive curve point")
    rows = fixed_gap_fiber(6)
    if len(rows) != 1:
        raise AssertionError("rho=6 gap fiber no longer has one curve point")
    data = rows[0]
    if not (
        (data.A, data.B, data.M, data.m, data.p, data.d)
        == (1, 7, 2, 6, 939, 1)
        and 9 * 6 * 6 - 6 * 6 - 2 == data.e * 13
        and (3 * 6 * 6 + 6 - 1) % data.A == 0
    ):
        raise AssertionError("A=1 dual gap boundary changed")


def verify_defect_boundary() -> None:
    """Replay the same d=1 boundary in the fixed-j coordinate."""
    rows = fixed_j_fiber(0)
    if len(rows) != 1:
        raise AssertionError("j=0 fiber no longer has one primitive proper curve point")
    data = rows[0]
    if not (
        (data.A, data.B, data.M, data.m, data.p, data.d)
        == (1, 7, 2, 6, 939, 1)
        and not fixed_j_fiber(1)
    ):
        raise AssertionError("fixed-j boundary controls changed")


def verify_vieta_gap_boundary() -> None:
    """Replay the same d=1 boundary through t=B-m without a scan."""
    rows = fixed_vieta_gap_fiber(1)
    if len(rows) != 1:
        raise AssertionError("t=1 fiber no longer has one primitive proper curve point")
    data = rows[0]
    if not (
        (data.A, data.B, data.M, data.m, data.p, data.d)
        == (1, 7, 2, 6, 939, 1)
        and data.B - data.m == 1
    ):
        raise AssertionError("fixed-t Vieta-gap boundary changed")


def verify_vieta_companion_boundary() -> None:
    """Check the excluded j=0 endpoint and the sole forced core residue case."""
    data = fixed_d_fiber(1)[0]
    j, numerator = verify_vieta_companion(data)
    A_core_residue, j_core_residue = 3, 2
    L_core_residue = 9 * j_core_residue**2 + 7 * j_core_residue + 1
    second_gate = 3 * j_core_residue**2 + j_core_residue - 1
    if not (
        (j, numerator) == (0, 1)
        and L_core_residue % A_core_residue == 0
        and second_gate % A_core_residue != 0
        and vieta_companion_second_gate_numerator(
            A_core_residue, j_core_residue
        )
        % A_core_residue
        != 0
    ):
        raise AssertionError("Vieta companion second-gate obstruction changed")


def verify_core_congruent_shadow() -> None:
    """Keep root divisibility distinct from the actual proper-root guards."""
    data = reconstruct(991, 87)
    if data is None:
        raise AssertionError("core-congruent k=3 shadow stopped reconstructing")
    cyclotomic = data.p * data.p + data.p + 1
    if not (
        data.p == 238_849
        and data.p % 24 == 1
        and cyclotomic % data.h == 0
        and data.A > data.B
        and data.a > data.e
        and data.h > data.p
        and data.d == 33_781
        and data.k == 3
    ):
        raise AssertionError("cyclotomic/proper-root boundary changed")


def verify() -> None:
    verify_d_one_boundary()
    verify_gap_boundary()
    verify_defect_boundary()
    verify_vieta_gap_boundary()
    verify_vieta_companion_boundary()
    verify_core_congruent_shadow()
    print(
        "verified k=3 primitive fibers, the Vieta-gap ordering, and the "
        "same-M Vieta companion gate: the shared A=1,d=1 point is non-core, "
        "and a core-congruent shadow still fails the proper-root guard"
    )
    print("no fiber, prime, source, certificate, or selector search is performed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
