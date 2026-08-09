#!/usr/bin/env python3
"""Verify the odd-owner cross-fiber incidence-lattice source map."""

from __future__ import annotations

import argparse
from math import prod

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint


def q_valuation(value: int, q: int) -> int:
    exponent = 0
    while value % q == 0:
        value //= q
        exponent += 1
    return exponent


def canonical_type_ii_vertex(s: int) -> tuple[int, int, int]:
    factors = factorint(s)
    A = prod(prime ** (exponent // 2) for prime, exponent in factors)
    C = prod(prime ** (exponent % 2) for prime, exponent in factors)
    D = A * C
    assert s == A * D == A * A * C
    assert D % A == 0
    assert all(exponent == 1 for _, exponent in factorint(C))
    return D, A, C


def owner_window(p: int, q: int, j: int) -> dict[str, object]:
    modulus = q**j
    beta = (-p * pow(4, -1, modulus)) % modulus
    assert 0 < beta < modulus
    bound = (p - 1) // 4
    rows: list[dict[str, int]] = []
    max_index = -1
    if beta <= bound:
        max_index = (bound - beta) // modulus
        for index in range(max_index + 1):
            s = beta + index * modulus
            D, A, C = canonical_type_ii_vertex(s)
            assert 4 * s < p
            assert (p + 4 * s) % modulus == 0
            assert D * A == s and D % q != 0
            rows.append(
                {
                    "index": index,
                    "s": s,
                    "digit": index % q,
                    "height": q_valuation(p + 4 * s, q),
                    "cofactor": (p + 4 * s) // modulus,
                    "D": D,
                    "A": A,
                    "C": C,
                }
            )
    digits = {row["digit"] for row in rows}
    inverse_four = pow(4, -1, q)
    for left, right in zip(rows, rows[1:]):
        assert right["cofactor"] - left["cofactor"] == 4
        assert (right["digit"] - left["digit"]) % q == (
            inverse_four * (right["cofactor"] - left["cofactor"])
        ) % q
    rank = int(len(digits) >= 2)
    return {
        "p": p,
        "q": q,
        "j": j,
        "beta": beta,
        "bound": bound,
        "max_index": max_index,
        "rows": rows,
        "rank": rank,
        "full_digit_coverage": len(digits) == q,
    }


def theta_on_difference(left: dict[str, int], right: dict[str, int], q: int) -> int:
    return (left["digit"] - right["digit"]) % q


def affine_pair(
    phase_left: int,
    phase_right: int,
    digit_left: int,
    digit_right: int,
    q: int,
) -> tuple[int, int]:
    denominator = (phase_left - phase_right) % q
    assert denominator
    a = (digit_left - digit_right) * pow(denominator, -1, q) % q
    c = (digit_left - a * phase_left) % q
    assert a
    assert (a * phase_right + c) % q == digit_right
    return a, c


def full_affine_lift(
    phases: list[int], data: dict[str, object], a: int, c: int
) -> dict[int, int]:
    q = int(data["q"])
    rows = data["rows"]
    assert isinstance(rows, list)
    by_digit: dict[int, int] = {}
    for row in rows:
        by_digit.setdefault(int(row["digit"]), int(row["s"]))
    assignment = {phase: by_digit[(a * phase + c) % q] for phase in phases}
    for phase, s in assignment.items():
        row = next(row for row in rows if int(row["s"]) == s)
        assert int(row["digit"]) == (a * phase + c) % q
    return assignment


def verify() -> None:
    p97_q11 = owner_window(97, 11, 1)
    rows_11 = p97_q11["rows"]
    assert isinstance(rows_11, list)
    assert p97_q11["beta"] == 6 and p97_q11["bound"] == 24
    assert [row["s"] for row in rows_11] == [6, 17]
    assert [row["digit"] for row in rows_11] == [0, 1]
    assert [(row["D"], row["A"]) for row in rows_11] == [(6, 1), (17, 1)]
    assert [row["height"] for row in rows_11] == [2, 1]
    assert [row["cofactor"] for row in rows_11] == [11, 15]
    assert (rows_11[1]["cofactor"] - rows_11[0]["cofactor"]) % 11 == 4
    assert p97_q11["rank"] == 1 and not p97_q11["full_digit_coverage"]
    assert theta_on_difference(rows_11[1], rows_11[0], 11) == 1
    assert affine_pair(2, 9, 0, 1, 11) == (8, 6)

    p97_q3 = owner_window(97, 3, 1)
    rows_3 = p97_q3["rows"]
    assert isinstance(rows_3, list)
    assert p97_q3["beta"] == 2
    assert [row["s"] for row in rows_3] == [2, 5, 8, 11, 14, 17, 20, 23]
    assert p97_q3["rank"] == 1 and p97_q3["full_digit_coverage"]
    assert [(row["D"], row["A"]) for row in rows_3[:3]] == [(2, 1), (5, 1), (4, 2)]
    assert [row["height"] for row in rows_3[:3]] == [1, 2, 1]
    assert [row["cofactor"] for row in rows_3[:3]] == [35, 39, 43]
    assert all(
        rows_3[index + 1]["cofactor"] - rows_3[index]["cofactor"] == 4
        for index in range(len(rows_3) - 1)
    )
    assert full_affine_lift([0, 1, 2], p97_q3, 1, 0) == {0: 2, 1: 5, 2: 8}

    p73_q17 = owner_window(73, 17, 1)
    rows_17 = p73_q17["rows"]
    assert isinstance(rows_17, list)
    assert p73_q17["beta"] == 3 and p73_q17["bound"] == 18
    assert [row["s"] for row in rows_17] == [3]
    assert [row["height"] for row in rows_17] == [1]
    assert [row["cofactor"] for row in rows_17] == [5]
    assert p73_q17["rank"] == 0 and not p73_q17["full_digit_coverage"]

    print("verified odd-owner fiber-incidence lattice source map")
    print("p97_q11", "owners=(6,17)", "incidence_quotient=C11", "affine=(8,6)")
    print("p97_q3", "full_digits", "owners=(2,5,8)", "depths=(1,2,1)")
    print("p73_q17", "singleton_owner=3", "transverse_rank=0")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
