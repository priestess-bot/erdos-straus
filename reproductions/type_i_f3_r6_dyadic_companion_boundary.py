#!/usr/bin/env python3
"""Check the symbolic scope controls for the R6 dyadic companion lemma."""

from __future__ import annotations

import argparse


def verify_controls() -> None:
    # These are algebraic shape controls, not actual R6 receipts.
    p, lam, j, L, H = 337, 4, 1, 21, 5
    a2 = 2**lam
    if not (
        (p - 1) == a2 * (j * L)
        and H <= j * L
        and H % 2 == 1
        and (a2 - 1) * j > 4
    ):
        raise AssertionError("R6 dyadic size control changed")
    print("verified R6 dyadic companion proof-shape controls (nonactual arithmetic scope)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify_controls()


if __name__ == "__main__":
    main()
