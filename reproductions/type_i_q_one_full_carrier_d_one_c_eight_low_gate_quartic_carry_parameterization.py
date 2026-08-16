#!/usr/bin/env python3
"""Verify the c=8 low-gate quartic carry parameterization.

The check proves the fixed polynomial identity for c=1,...,7 and replays one
non-low high-q control. It does not scan parameters, primes, or V factors.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source


def source_polynomial(prime: int) -> int:
    """Return P(p)=4V in the c=8 high-R source normal form."""
    return (
        121 * prime**4
        - 396 * prime**3
        + 346 * prime**2
        + 4 * prime
        - 79
    )


def carry_quartic(capacity: int, carry: int) -> int:
    """Return the D-independent quartic G_c(lambda)."""
    return (
        carry**4
        - 4 * capacity * carry**3
        - 27_334 * capacity**2 * carry**2
        + 2_471_436 * capacity**3 * carry
        - 59_657_719 * capacity**4
    )


def transported_polynomial(capacity: int, carry: int) -> int:
    """Return P(p)*lambda^4 after replacing p*lambda by 79*c."""
    value = 79 * capacity
    return (
        121 * value**4
        - 396 * value**3 * carry
        + 346 * value**2 * carry**2
        + 4 * value * carry**3
        - 79 * carry**4
    )


def verify_symbolic_coefficients() -> None:
    """Replay the exact transport identity on all seven low capacities."""
    for capacity in range(1, 8):
        carry = 16 * (capacity + 10) - capacity
        if not (
            carry % 16 == (-capacity) % 16
            and transported_polynomial(capacity, carry)
            == -79 * carry_quartic(capacity, carry)
        ):
            raise AssertionError("low-gate quartic transport identity changed")


def non_low_high_q_control() -> dict[str, int]:
    """Replay the D_s=11 raw control through the quartic reparameterization."""
    data = source.source_data(116)
    q = 578_581
    edge = source.v_side_raw_edge(data, q)
    a, _, layer = edge["destination"]
    support = data.K // 8
    defect = gcd(data.V, support)
    capacity = (8 * pow(a // defect, -1, data.prime)) % data.prime
    carry_numerator = 32 * defect * q + 79 * capacity
    carry, remainder = divmod(carry_numerator, data.prime)
    if not (
        data.prime == 5_569
        and data.V == source_polynomial(data.prime) // 4
        and q > 2 * (data.prime - 1)
        and layer == 1
        and defect == 11
        and capacity == 4_202
        and remainder == 0
        and carry == 36_630
        and carry % 16 == (-capacity) % 16
        and gcd(q, carry) == 1
        and data.V % q == 0
        and carry_quartic(capacity, carry) % q == 0
        and source_polynomial(data.prime) % q == 0
    ):
        raise AssertionError("non-low c=8 quartic carry control changed")
    return {"defect": defect, "capacity": capacity, "carry": carry}


def verify() -> None:
    verify_symbolic_coefficients()
    if non_low_high_q_control() != {
        "defect": 11,
        "capacity": 4_202,
        "carry": 36_630,
    }:
        raise AssertionError("stored quartic parameterization control changed")
    print(
        "verified c=8 low-gate quartic carry parameterization: "
        "seven low capacities transport to G_c(lambda), with a non-low high-q control"
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
