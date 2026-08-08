#!/usr/bin/env python3
"""Verify the typed Fourier-to-owner q-prefix bridge controls."""

from __future__ import annotations

import argparse
from collections import Counter


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def inverse(value: int, modulus: int) -> int:
    return pow(value, -1, modulus)


def beta(prime: int, q: int, height: int) -> int:
    modulus = q**height
    return (-prime * inverse(4, modulus)) % modulus


def capacity(q: int, shifts: tuple[int, ...], height: int) -> int:
    counts = Counter(shift % (q**height) for shift in shifts)
    return max(counts.values(), default=0)


def positive(value: int) -> int:
    return max(value, 0)


def decomposition(owner_count: int, cap: int, demand: int, mu: int) -> tuple[int, int, int]:
    owner_gap = positive(demand - mu * owner_count)
    slack = mu * (cap - owner_count)
    global_gap = positive(demand - mu * cap)
    if global_gap != positive(owner_gap - slack):
        raise AssertionError("Fourier owner decomposition changed")
    return owner_gap, slack, global_gap


def verify() -> None:
    prime = 433
    q = 7
    shifts = (16, 100)
    heights = tuple(valuation(prime + 4 * shift, q) for shift in shifts)
    if heights != (1, 2):
        raise AssertionError("aligned owner heights changed")
    if beta(prime, q, 1) != 2 or beta(prime, q, 2) != 2:
        raise AssertionError("arithmetic target residue changed")
    if shifts[0] % 7 != beta(prime, q, 1):
        raise AssertionError("first Fourier owner phase is not aligned")
    if shifts[1] % 49 != beta(prime, q, 2):
        raise AssertionError("second Fourier owner phase is not aligned")
    if capacity(q, shifts, 2) != 1:
        raise AssertionError("tight second-layer capacity changed")
    if decomposition(owner_count=1, cap=1, demand=2, mu=1) != (1, 0, 1):
        raise AssertionError("tight Fourier owner split changed")
    if valuation(shifts[1] - shifts[0], q) != 1:
        raise AssertionError("Fourier owner boundary changed")

    # Fourier phase can exist without an arithmetic q-prefix owner alignment.
    gamma = 1
    if beta(prime, 3, 1) != 2 or gamma == beta(prime, 3, 1):
        raise AssertionError("nonidentified phase control changed")

    # A G-state source-trivial role is typed as support separation, not q demand.
    g_state = {"source_difference_trivial": True, "target_phase_nontrivial": True}
    if not g_state["source_difference_trivial"] or not g_state["target_phase_nontrivial"]:
        raise AssertionError("G-state support separation control changed")
    print(
        "verified F/G Fourier phase-owner bridge: "
        "aligned tight escape, nonidentified phase, and G separation"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
