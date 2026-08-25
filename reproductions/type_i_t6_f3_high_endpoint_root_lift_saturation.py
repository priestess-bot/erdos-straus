#!/usr/bin/env python3
"""Verify the high-stutter root-lift saturation boundary."""

from __future__ import annotations

import argparse
from math import gcd


def crt_pair(a: int, modulus_a: int, b: int, modulus_b: int) -> int:
    """Return the least nonnegative simultaneous residue for compatible congruences."""
    common = gcd(modulus_a, modulus_b)
    if (b - a) % common:
        raise AssertionError("incompatible CRT constraints")
    reduced_b = modulus_b // common
    if reduced_b == 1:
        return a % modulus_a
    factor = ((b - a) // common) * pow(modulus_a // common, -1, reduced_b)
    return (a + modulus_a * (factor % reduced_b)) % (modulus_a * reduced_b)


def root_lift_data(p: int, h: int, D: int, omega: int) -> dict[str, int]:
    if p % 24 != 1 or h % 3:
        raise AssertionError("outside the core high-stutter static scope")
    M = (p * p + p + 1) // 3
    u = h // 3
    if not (h > p and M % u == 0 and gcd(D, M) == 1):
        raise AssertionError("invalid high static datum")
    if (p * h + 1) % D or D % p != (1 - h) % p:
        raise AssertionError("missing stutter divisor conditions")
    v = M // u
    A0 = u * (p * p - 1) // 4
    D_K = D // gcd(D, A0)
    if omega <= 0 or omega % 2 == 0 or gcd(omega, v) != 1:
        raise AssertionError("omega is not an odd primitive root lift")
    if (p * p * omega - 3 * v) % D_K:
        raise AssertionError("omega misses the exact capacity residue")
    r = (u * omega - 1) // 2
    K = A0 * (p * p * omega - 3 * v)
    if (4 * K - 1) % p:
        raise AssertionError("root chart is not integral")
    R = (4 * K - 1) // p
    root_formula = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    if R != root_formula:
        raise AssertionError("root chart no longer matches the source formula")
    if gcd(2 * r + 1, M) != u or K % D or (R - h) % D:
        raise AssertionError("root-lift invariants changed")
    return {
        "M": M,
        "u": u,
        "v": v,
        "A0": A0,
        "D_K": D_K,
        "r": r,
        "K": K,
        "R": R,
        "E_formal": (R - h) // D,
    }


def canonical_odd_lift(p: int, h: int, D: int) -> int:
    """Construct one CRT lift in the exact capacity residue class."""
    M = (p * p + p + 1) // 3
    u = h // 3
    v = M // u
    A0 = u * (p * p - 1) // 4
    D_K = D // gcd(D, A0)
    residue = (3 * v * pow(p * p, -1, D_K)) % D_K if D_K > 1 else 0
    omega = crt_pair(residue, D_K, 1, 2 * v)
    if omega == 0:
        raise AssertionError("CRT primitive lift unexpectedly vanished")
    return omega


def divisor_gates(p: int, r: int, h: int, D: int, m: int) -> tuple[int, int]:
    M = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, M)
    v = M // u
    omega = (2 * r + 1) // u
    delta = h - p - 1
    n = m - 1
    root_gate = delta**3 + n * delta**2 + n * n * delta + v * n**3
    capacity_gate = (delta * delta - n * n) * (
        omega * delta * delta - 3 * v * n * n
    )
    return root_gate, capacity_gate


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def prime_divisors(value: int) -> tuple[int, ...]:
    divisors: list[int] = []
    trial = 2
    while trial * trial <= value:
        if value % trial == 0:
            divisors.append(trial)
            while value % trial == 0:
                value //= trial
        trial = 3 if trial == 2 else trial + 2
    if value > 1:
        divisors.append(value)
    return tuple(divisors)


def canonical_complete_excess_divisor(A: int, K: int, z: int) -> tuple[int, int]:
    """Return the canonical normalized divisor D and complete-excess block Q."""

    excess_base = z // gcd(z, K)
    Q = gcd(z, pow(excess_base, z.bit_length(), z))
    return z // Q * gcd(A, Q), Q


def check_canonical_receipt_lift_saturation() -> None:
    """Check the valuation-preserving lift on a noncore canonical-D control."""

    p, h, r = 67, 93, 25_311
    M = (p * p + p + 1) // 3
    u, v = h // 3, M // (h // 3)
    omega = (2 * r + 1) // u
    A0 = u * (p * p - 1) // 4
    K = A0 * (p * p * omega - 3 * v)
    A = K // (p - 1)
    R = (4 * K - 1) // p
    z = R - h
    D, Q = canonical_complete_excess_divisor(A, K, z)
    H = p * h + 1
    D_K = D // gcd(D, A0)
    L = (A * K * z * H) ** 2
    omega_lifted = omega + 2 * D_K * v * L
    K_lifted = A0 * (p * p * omega_lifted - 3 * v)
    A_lifted = K_lifted // (p - 1)
    R_lifted = (4 * K_lifted - 1) // p
    z_lifted = R_lifted - h
    D_lifted, Q_lifted = canonical_complete_excess_divisor(
        A_lifted, K_lifted, z_lifted
    )

    if not (
        M == 1_519
        and D == 1_558
        and Q == 19_540_216
        and H == 6_232
        and D_K == 779
        and omega_lifted % 2 == 1
        and gcd(omega_lifted, v) == 1
        and D_lifted == D
        and Q_lifted > 1
        and K_lifted % D == 0
        and z_lifted % D == 0
    ):
        raise AssertionError("canonical-D lift control changed")
    for prime in prime_divisors(H):
        before = tuple(valuation(value, prime) for value in (A, K, z))
        after = tuple(
            valuation(value, prime) for value in (A_lifted, K_lifted, z_lifted)
        )
        if before != after:
            raise AssertionError("canonical-D lift changed an H-adic valuation")


def check_core_curve_shadow_saturation() -> None:
    p = 115_815_206_209
    h = 1_169_617_882_071
    D = 1_207_185_892_628_946_440
    omega = 3_161_408_027_583
    row = root_lift_data(p, h, D, omega)
    m = (D + h - 1) // p
    if not (
        row["v"] == 11_467_986_421
        and row["D_K"] == 30_179_647_315_723_661
        and row["E_formal"] % p == 1
        and m == 10_423_390
    ):
        raise AssertionError("core high curve control changed")
    root_gate, capacity_gate = divisor_gates(p, row["r"], h, D, m)
    if root_gate % D or capacity_gate % D:
        raise AssertionError("saturated control no longer satisfies both gates")
    for t in (1, 7):
        omega_t = omega + 2 * row["D_K"] * row["v"] * t
        lifted = root_lift_data(p, h, D, omega_t)
        if lifted["R"] % p != 1:
            raise AssertionError("periodic root chart changed")


def check_crt_primitive_lift() -> None:
    p = 115_815_206_209
    h = 1_169_617_882_071
    D = 1_207_185_892_628_946_440
    omega = canonical_odd_lift(p, h, D)
    row = root_lift_data(p, h, D, omega)
    if omega % (2 * row["v"]) != 1:
        raise AssertionError("CRT lift did not preserve odd primitive class")


def check_high_vieta_noninvariance() -> None:
    d, c, x, y = 11, 1, 101, 1020
    if y * y + x * y - x * x != c * (d * x * y - 1):
        raise AssertionError("high Pell control changed")
    other_y = (c * d - 1) * x - y
    other_x = -(c * d - 1) * y - x
    if other_y % 3 == 0 or other_x >= 0:
        raise AssertionError("high Vieta boundary changed")


def verify() -> None:
    check_core_curve_shadow_saturation()
    check_crt_primitive_lift()
    check_canonical_receipt_lift_saturation()
    check_high_vieta_noninvariance()
    print("verified high stutter root-lift saturation boundary")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
