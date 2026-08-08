#!/usr/bin/env python3
"""Verify the fixed-fiber affine source-rank cap and annihilator control."""

from __future__ import annotations

import argparse


P = 73
D = 1
A = 27
CARRIERS = (675, 2646, 10530)
N_VALUES = (37, 145, 577)


def source_vector(m: int) -> tuple[int, int]:
    return (1, (m + 1) % 3)


def sub_vectors(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return tuple((a - b) % 3 for a, b in zip(left, right))  # type: ignore[return-value]


def lam(vector: tuple[int, int]) -> int:
    return (vector[0] - vector[1]) % 3


def verify() -> None:
    if P % 24 != 1 or not (0 < D < P) or A % P == 0:
        raise AssertionError("fixed-fiber parameters changed")
    if len(CARRIERS) != len(N_VALUES):
        raise AssertionError("control row count changed")

    modulus = A * P
    if len({m % modulus for m in CARRIERS}) != 1:
        raise AssertionError("fixed-fiber CRT class changed")
    for m, n in zip(CARRIERS, N_VALUES):
        if m % A or P * n != 4 * D * m + 1:
            raise AssertionError("overflow source row changed")
        if 4 * m - n <= P:
            raise AssertionError("overflow range changed")

    vectors = tuple(source_vector(m) for m in CARRIERS)
    if vectors != ((1, 1),) * len(CARRIERS):
        raise AssertionError("affine source-map did not collapse")
    if any(lam(vector) != 0 for vector in vectors):
        raise AssertionError("annihilator does not kill source span")

    target = (1, 0)
    if lam(target) != 1:
        raise AssertionError("target separation changed")
    if sub_vectors(target, vectors[0]) != (0, 2):
        raise AssertionError("target/source control relation changed")
    # K = {(x,x): x in F_3}; it has 3 elements in H = F_3^2.
    kernel = {(x, x) for x in range(3)}
    if kernel != {(0, 0), (1, 1), (2, 2)}:
        raise AssertionError("annihilator kernel changed")
    if len(kernel) != 3 or 9 // len(kernel) != 3:
        raise AssertionError("strict quotient size changed")

    print(
        "verified fixed-fiber affine rank cap: "
        "dim(source span)=1 < dim(demand)=2, quotient=C3"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
