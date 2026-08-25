#!/usr/bin/env python3
"""Replay canonicality and E1-negative controls for high-support charts."""

from __future__ import annotations

import argparse


def chart(prime: int, support: int, cofactor: int) -> dict[str, int]:
    carrier = support * cofactor
    if (4 * carrier - 1) % prime:
        raise ValueError("chart is not integral")
    residual = (4 * carrier - 1) // prime
    return {
        "p": prime,
        "A": support,
        "C": cofactor,
        "K": carrier,
        "R": residual,
        "Bp": (prime - 1) ** 2 // 4,
    }


def canonicality(record: dict[str, int]) -> dict[str, int]:
    prime, support, cofactor = record["p"], record["A"], record["C"]
    canonical = pow(4 * support, -1, prime)
    excess, remainder = divmod(cofactor - canonical, prime)
    if remainder or excess < 0:
        raise AssertionError("cofactor does not replay from canonical residue")
    return {
        **record,
        "c": canonical,
        "t": excess,
        "R_canonical": record["R"] - 4 * support * excess,
        "K_canonical": support * canonical,
    }


def synthetic_determinant(record: dict[str, int]) -> dict[str, int]:
    return {
        "M": record["K"],
        "d": record["p"] - 1,
        "n": 4 * record["K"] - record["R"],
    }


def verify() -> None:
    noncanonical = canonicality(chart(73, 1369, 74))
    if not (
        noncanonical["Bp"] == 1296
        and noncanonical["R"] == 5551
        and noncanonical["c"] == 1
        and noncanonical["t"] == 1
        and noncanonical["R_canonical"] == 75
        and noncanonical["K_canonical"] == 1369
        and noncanonical["R_canonical"] > noncanonical["p"]
        and noncanonical["R"] > 4 * noncanonical["A"]
    ):
        raise AssertionError("noncanonical high-support control changed")
    determinant = synthetic_determinant(noncanonical)
    if not (
        noncanonical["p"] * determinant["n"]
        == 4 * determinant["M"] * determinant["d"] + 1
    ):
        raise AssertionError("post-hoc determinant identity changed")

    canonical = canonicality(chart(73, 1518, 45))
    if not (
        canonical["c"] == 45
        and canonical["t"] == 0
        and canonical["R"] < 4 * canonical["A"]
    ):
        raise AssertionError("canonical high-support control changed")
    print("verified canonical/noncanonical high-support split and E1-negative determinant control")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
