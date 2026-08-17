#!/usr/bin/env python3
"""Verify the c=8 q_star=103 low-gate odd carry rays.

This checks eight CRT threshold rows, the seven formal ray starts on each
row, and one stored non-low high-q control. It does not scan source parameters,
primes, V factors, or certificate menus.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_q_one_full_carrier_d_one_c_eight_low_gate_quartic_carry_parameterization as quartic
import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source


DEFECT_CONGRUENCES = ((11, 6), (41, 30), (149, 55))
CRT_THRESHOLD_ROWS = (
    (1, 86),
    (11, 292),
    (41, 1_219),
    (149, 13_167),
    (451, 13_888),
    (1_639, 59_208),
    (6_109, 89_902),
    (67_199, 5_123_718),
)


def crt(congruences: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    """Return the least nonnegative solution and modulus for coprime rows."""
    value, modulus = 0, 1
    for prime, residue in congruences:
        step = ((residue - value) * pow(modulus, -1, prime)) % prime
        value += modulus * step
        modulus *= prime
    return value, modulus


def defect_from_residues(s: int) -> int:
    """Evaluate the exact D_s table without materializing the large source."""
    result = 1
    for prime, residue in DEFECT_CONGRUENCES:
        if s % prime == residue:
            result *= prime
    return result


def source_ray_data(prime: int, defect: int, capacity: int) -> tuple[int, int]:
    """Return sigma and eta in the parity-refined affine ray."""
    modulus = 64 * defect
    sigma = ((79 * capacity + 32 * defect) * pow(prime, -1, modulus)) % modulus
    numerator = prime * sigma - 79 * capacity
    eta, remainder = divmod(numerator, 32 * defect)
    if remainder:
        raise AssertionError("odd carry residue no longer reconstructs eta")
    return sigma, eta


def normalized_quartic(value: int) -> int:
    """Return f(X), the c-homogeneous normalization of G_c."""
    return (
        value**4
        - 4 * value**3
        - 27_334 * value**2
        + 2_471_436 * value
        - 59_657_719
    )


def carry_envelope(bound: int) -> int:
    """Return the explicit H(L) used for c<=7 and lambda<=L."""
    return (
        bound**4
        + 28 * bound**3
        + 1_339_366 * bound**2
        + 847_702_548 * bound
        + 143_238_183_319
    )


def verify_bounded_carry_finiteness_constants() -> None:
    """Check the root obstruction mod 19 and the exact envelope coefficients."""
    if any(normalized_quartic(value) % 19 == 0 for value in range(19)):
        raise AssertionError("the normalized quartic unexpectedly has a root mod 19")
    if not (
        27_334 * 7**2 == 1_339_366
        and 2_471_436 * 7**3 == 847_702_548
        and 59_657_719 * 7**4 == 143_238_183_319
        and carry_envelope(1)
        == 1 + 28 + 1_339_366 + 847_702_548 + 143_238_183_319
        and 64 * source.SHARED_SUPPORT == 4_300_736
    ):
        raise AssertionError("bounded-carry envelope constants changed")


def verify_crt_threshold_table() -> None:
    """Replay only the eight source lower bounds needed for p>32D."""
    for defect, least_s in CRT_THRESHOLD_ROWS:
        congruences = ((103, 86),) + tuple(
            (prime, residue)
            for prime, residue in DEFECT_CONGRUENCES
            if defect % prime == 0
        )
        s, modulus = crt(congruences)
        prime = 48 * s + 1
        if not (
            s == least_s
            and modulus == 103 * defect
            and s >= 86
            and defect_from_residues(s) == defect
            and prime > 32 * defect
            and gcd(prime, 64 * defect) == 1
        ):
            raise AssertionError("q_star=103 defect CRT threshold changed")

        for capacity in range(1, 8):
            sigma, eta = source_ray_data(prime, defect, capacity)
            carry = 64 * defect + sigma
            raw_prime = 2 * prime + eta
            if not (
                0 < sigma < 64 * defect
                and eta > 0
                and eta % 2 == 1
                and prime * carry == 32 * defect * raw_prime + 79 * capacity
                and carry % 16 == (-capacity) % 16
                and raw_prime % 2 == 1
                and raw_prime > 2 * (prime - 1)
            ):
                raise AssertionError("low-gate odd carry ray start changed")


def verify_non_low_high_q_control() -> None:
    """Replay the existing q=578581 control through the affine ray equations."""
    data = source.source_data(116)
    q = 578_581
    edge = source.v_side_raw_edge(data, q)
    a, _, layer = edge["destination"]
    defect = gcd(data.V, data.K // 8)
    capacity = (8 * pow(a // defect, -1, data.prime)) % data.prime
    carry = (32 * defect * q + 79 * capacity) // data.prime
    sigma, eta = source_ray_data(data.prime, defect, capacity)
    t, remainder = divmod(carry - (64 * defect + sigma), 64 * defect)
    if not (
        data.prime == 5_569
        and defect == 11
        and layer == 1
        and capacity == 4_202
        and carry == 36_630
        and sigma == 22
        and eta == -595
        and remainder == 0
        and t == 51
        and q == 2 * data.prime * (t + 1) + eta
        and q > 2 * (data.prime - 1)
        and q % 2 == 1
        and quartic.carry_quartic(capacity, carry) % q == 0
    ):
        raise AssertionError("stored non-low high-q odd carry control changed")


def verify() -> None:
    verify_bounded_carry_finiteness_constants()
    verify_crt_threshold_table()
    verify_non_low_high_q_control()
    print(
        "verified c=8 q_star=103 low-gate odd carry rays: "
        "mod-19 root obstruction, eight CRT thresholds, 56 formal starts, "
        "and one high-q control"
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
