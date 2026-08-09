#!/usr/bin/env python3
"""Verify the target-odd affine offset repair gate."""

from __future__ import annotations

import argparse
import math


def solve_labels(p: int, q: int, e: int, c: int, h: int, lower: int, upper: int):
    modulus = q**e
    beta = (-p * pow(4, -1, modulus)) % modulus
    g = math.gcd(h, modulus)
    delta = (beta - c) % modulus
    if delta % g:
        return {"branch": "TARGET_ODD_AFFINE_REPAIR_GCD_OBSTRUCTED", "labels": []}
    h1, n1 = h // g, modulus // g
    t0 = 0 if n1 == 1 else (delta // g * pow(h1, -1, n1)) % n1
    t_min = math.ceil((lower - c) / h)
    t_max = math.floor((upper - c) / h)
    labels = [c + h * t for t in range(t_min, t_max + 1) if (t - t0) % n1 == 0]
    if not labels:
        return {"branch": "TARGET_ODD_AFFINE_REPAIR_INTERVAL_EMPTY", "labels": []}
    return {"branch": "TARGET_ODD_AFFINE_REPAIRED", "labels": labels}


def verify() -> None:
    p, q, e = 73, 3, 2
    modulus = q**e
    gamma = 0
    beta = (-p * pow(4, -1, modulus)) % modulus
    assert beta == 2
    assert gamma == 0

    # Identity ownership remains impossible.
    assert gamma != beta

    repaired = solve_labels(p, q, e, c=5, h=3, lower=6, upper=20)
    assert repaired == {"branch": "TARGET_ODD_AFFINE_REPAIRED", "labels": [11, 20]}
    assert all((p + 4 * label) % modulus == 0 for label in repaired["labels"])

    interval_empty = solve_labels(p, q, e, c=5, h=3, lower=6, upper=10)
    assert interval_empty == {
        "branch": "TARGET_ODD_AFFINE_REPAIR_INTERVAL_EMPTY",
        "labels": [],
    }

    gcd_obstructed = solve_labels(p, q, e, c=4, h=3, lower=0, upper=20)
    assert gcd_obstructed == {
        "branch": "TARGET_ODD_AFFINE_REPAIR_GCD_OBSTRUCTED",
        "labels": [],
    }

    # No affine offset can create a q=2 prefix for an odd p.
    assert all((p + 4 * s) % 2 == 1 for s in range(-3, 4))

    print("verified target-odd affine offset repair gate")
    print(
        {
            "p": p,
            "q": q,
            "e": e,
            "gamma": gamma,
            "beta": beta,
            "repaired_labels": repaired["labels"],
            "interval_branch": interval_empty["branch"],
            "gcd_branch": gcd_obstructed["branch"],
            "q2_branch": "QPREFIX_CAPACITY_ZERO_BY_PARITY",
        }
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
