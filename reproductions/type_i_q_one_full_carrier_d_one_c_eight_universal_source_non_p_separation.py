#!/usr/bin/env python3
"""Verify c=8 source-side support separation and one non-p raw receipt.

The script checks polynomial identities, three tiny residue tables, and one
stored c=8 macro control. It does not scan parameters or factor a target.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd

import type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction as c8
import type_ii_q_one_full_carrier_qstar_103_rough_selection_criterion as rough


SHARED_SUPPORT = 11 * 41 * 149
N_REMAINDER = 133_295


@dataclass(frozen=True)
class SourceData:
    s: int
    prime: int
    R: int
    K: int
    L: int
    E: int
    V: int


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def is_prime(value: int) -> bool:
    """Use trial division only for the fixed control label."""
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


def source_data(s: int) -> SourceData:
    """Materialize the c=8 high-R target and its source-side coordinate."""
    if s < 1:
        raise ValueError("s must be positive")
    target = c8.c_eight_target(s)
    p, R, K = target.prime, target.R, target.K
    L = 176 * s + 5
    E = 3168 * s * s + 24 * s - 1
    V = R * (p - 1) - p
    if not (
        p == 48 * s + 1
        and K == 72 * s * L * E
        and p * R + 1 == 4 * K
        and V
        == 160579584 * s**4
        + 2433024 * s**3
        - 66816 * s * s
        - 96 * s
        - 1
    ):
        raise AssertionError("c=8 source-side normal form changed")
    return SourceData(s, p, R, K, L, E, V)


def support_identities(data: SourceData) -> None:
    """Check the two Bezout bounds and exact N remainder without factoring."""
    s, p, R, K, L, E, V = (
        data.s,
        data.prime,
        data.R,
        data.K,
        data.L,
        data.E,
        data.V,
    )
    N = 6 * s - 1
    D = gcd(V, K)
    if not (
        4 * R - 79 == p * (278784 * s * s - 1584 * s - 83)
        and V % 2 == 1
        and V % 3 == 2
        and V % s == (-1) % s
        and -44 * V + 3 * (528 * s - 7) * (25344 * s * s - 1) * L == 149
        and -(5280 * s + 139) * V
        + 24 * (11151360 * s**3 + 378048 * s * s + 464 * s - 13) * E
        == 451
        and SHARED_SUPPORT % D == 0
        and V
        == N * (26763264 * s**3 + 4866048 * s * s + 799872 * s + 133296)
        + N_REMAINDER
        and N_REMAINDER % gcd(V, N) == 0
        and V > 160512768 * s * s - 1 > SHARED_SUPPORT
        and D < V
    ):
        raise AssertionError("c=8 source support identities changed")


def shared_support_residue_table() -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Enumerate only the three fixed support primes in their own residue rings."""
    expected = ((11, (6,)), (41, (30,)), (149, (55,)))
    rows: list[tuple[int, tuple[int, ...]]] = []
    for prime, expected_residues in expected:
        hits: list[int] = []
        for s in range(prime):
            L = 176 * s + 5
            E = 3168 * s * s + 24 * s - 1
            K = 72 * s * L * E
            V = (
                160579584 * s**4
                + 2433024 * s**3
                - 66816 * s * s
                - 96 * s
                - 1
            )
            if V % prime == 0 and K % prime == 0:
                hits.append(s)
        row = (prime, tuple(hits))
        if row != (prime, expected_residues):
            raise AssertionError("c=8 shared-support residue table changed")
        rows.append(row)
    return tuple(rows)


def canonical_p_edge(data: SourceData) -> tuple[int, int, int]:
    """Replay the high-R source's canonical p edge to the anchor."""
    p, R, K, V = data.prime, data.R, data.K, data.V
    source = (p, V, p - 1)
    destination = (source[0] // p, (source[1] + R) // p, (source[2] + 1) // p)
    if not (
        gcd(p, R) == 1
        and gcd(p, V) == 1
        and gcd(p, p - 1) == 1
        and K % p != 0
        and destination == (1, R - 1, 1)
    ):
        raise AssertionError("c=8 high-R canonical p source changed")
    return destination


def v_side_raw_edge(data: SourceData, prime: int) -> dict[str, object]:
    """Replay one actual raw edge selected from the V coordinate."""
    p, R, K, V = data.prime, data.R, data.K, data.V
    layer = p - 1
    shift = (-layer) % prime
    if not (
        is_prime(prime)
        and V % prime == 0
        and 1 <= shift < prime
        and valuation(V, prime) > valuation(K, prime)
        and gcd(prime, p * R * layer) == 1
    ):
        raise AssertionError("V-side label is not an actual strict raw label")
    selected_after = V // prime
    other_after = (p + R * shift) // prime
    layer_after = (layer + shift) // prime
    reduction = gcd(selected_after, other_after)
    if layer_after % reduction:
        raise AssertionError("V-side gcd reduction lost the raw layer")
    destination = (
        selected_after // reduction,
        other_after // reduction,
        layer_after // reduction,
    )
    if not (
        min(destination) > 0
        and gcd(destination[0], destination[1]) == 1
        and destination[0] + destination[1] == R * destination[2]
    ):
        raise AssertionError("V-side raw destination is not primitive")
    return {
        "q": prime,
        "shift": shift,
        "gcd_reduction": reduction,
        "destination": destination,
    }


def q_star_separation(data: SourceData) -> None:
    """Check that the rough macro carrier 103 is support-only, never V-side."""
    s, K, L, V = data.s, data.K, data.L, data.V
    N = 6 * s - 1
    if not rough.q_star_is_103(s):
        raise AssertionError("control left the true q_star=103 rough domain")
    if not (
        s % 103 == 86
        and N % 103 == 0
        and L % 103 == 0
        and K % 103 == 0
        and V % 103 == 13
        and (5 * 503) % gcd(V, N) == 0
    ):
        raise AssertionError("q_star=103 source separation changed")


def control_receipt() -> None:
    """Replay one actual c=8 macro control and its one-step non-p bypass."""
    c8.actual_c_eight_control()
    data = source_data(3279)
    support_identities(data)
    q_star_separation(data)
    if canonical_p_edge(data) != (1, data.R - 1, 1):
        raise AssertionError("c=8 canonical source anchor changed")

    q = 5_963_047
    edge = v_side_raw_edge(data, q)
    expected_v = 11 * 241 * q * 1_174_302_652_267
    if not (
        data.prime == 157_393
        and data.V == expected_v
        and gcd(data.V, data.K) == 1
        and q > data.prime - 1
        and edge
        == {
            "q": q,
            "shift": 5_805_655,
            "gcd_reduction": 1,
            "destination": (3_113_076_331_159_817, 114_830_786_617_996_134, 1),
        }
    ):
        raise AssertionError("stored c=8 non-p source receipt changed")


def verify() -> None:
    for s in (86, 3279):
        support_identities(source_data(s))
    if shared_support_residue_table() != ((11, (6,)), (41, (30,)), (149, (55,))):
        raise AssertionError("shared-support table changed")
    control_receipt()
    print(
        "verified q=1 zero-k c=8 source separation: bounded shared support, "
        "q_star=103 absent from V, and one non-p m=1 raw receipt"
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
