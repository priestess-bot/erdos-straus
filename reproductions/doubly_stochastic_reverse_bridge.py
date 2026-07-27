#!/usr/bin/env python3
"""Exact reverse audit for low-denominator doubly-stochastic transports.

For an integer 3 by 3 matrix M whose rows and columns sum to D, write W=M/D.
The transport t'=(n/p) Wt preserves the reciprocal sum.  For a fixed target,
the inverse has the form t=H/n, so the lcm of the H-coordinate numerators
decides every possible strict integer source without enumerating source
solutions.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT
    / "reproductions"
    / "doubly-stochastic-reverse-bridge-2451289-ac14-d10-results.json"
)


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


targeted_bridge = load_module(
    "doubly_stochastic_targeted_bridge", "targeted_descent_bridge.py"
)

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def compositions(total: int):
    """Yield all ordered nonnegative triples with the given sum."""
    for first in range(total + 1):
        for second in range(total - first + 1):
            yield first, second, total - first - second


def determinant(matrix: Matrix) -> int:
    """Return the determinant of a 3 by 3 integer matrix."""
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def adjugate(matrix: Matrix) -> Matrix:
    """Return the adjugate in the same row-major layout."""
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return (
        (e * i - f * h, c * h - b * i, b * f - c * e),
        (f * g - d * i, a * i - c * g, c * d - a * f),
        (d * h - e * g, b * g - a * h, a * e - b * d),
    )


def is_genuine_matrix(matrix: Matrix, denominator: int) -> bool:
    """Check the reduced, invertible, genuinely mixing matrix conditions."""
    if denominator < 2:
        return False
    entries = tuple(entry for row in matrix for entry in row)
    if any(entry < 0 for entry in entries) or math.gcd(*entries) != 1:
        return False
    if any(sum(row) != denominator for row in matrix):
        return False
    if any(sum(matrix[row][column] for row in range(3)) != denominator for column in range(3)):
        return False
    if any(sum(entry > 0 for entry in row) < 2 for row in matrix):
        return False
    if any(
        sum(matrix[row][column] > 0 for row in range(3)) < 2
        for column in range(3)
    ):
        return False
    return determinant(matrix) != 0


def matrices_at_denominator(denominator: int) -> tuple[Matrix, ...]:
    """Enumerate all reduced genuinely mixing doubly-stochastic matrices."""
    values: list[Matrix] = []
    for first_row in compositions(denominator):
        for second_row in compositions(denominator):
            third_row = tuple(
                denominator - first_row[column] - second_row[column]
                for column in range(3)
            )
            if min(third_row) < 0:
                continue
            matrix = (first_row, second_row, third_row)
            if is_genuine_matrix(matrix, denominator):
                values.append(matrix)
    return tuple(values)


def matrices_through(max_denominator: int) -> tuple[tuple[int, Matrix], ...]:
    """Return reduced matrices with their unique common denominator."""
    if max_denominator < 2:
        raise ValueError("max_denominator must be at least two")
    return tuple(
        (denominator, matrix)
        for denominator in range(2, max_denominator + 1)
        for matrix in matrices_at_denominator(denominator)
    )


def inverse_profile(
    prime: int, target: tuple[int, int, int], matrix: Matrix, denominator: int
) -> tuple[Fraction, Fraction, Fraction]:
    """Return H for which every inverse source reciprocal vector equals H / n."""
    if prime < 2 or any(value < 1 for value in target):
        raise ValueError("prime and target denominators must be positive")
    if not is_genuine_matrix(matrix, denominator):
        raise ValueError("matrix is not a reduced genuine transport")
    det = determinant(matrix)
    inverse_adjugate = adjugate(matrix)
    target_reciprocals = tuple(Fraction(1, value) for value in target)
    return tuple(
        Fraction(prime * denominator, det)
        * sum(
            Fraction(inverse_adjugate[row][column]) * target_reciprocals[column]
            for column in range(3)
        )
        for row in range(3)
    )


def least_source_denominator(profile: tuple[Fraction, Fraction, Fraction]) -> int | None:
    """Return the least n >= 2 that makes each source denominator integral."""
    if any(value <= 0 for value in profile):
        return None
    value = 1
    for coordinate in profile:
        value = math.lcm(value, coordinate.numerator)
    return max(2, value)


def reverse_lift(
    prime: int, target: tuple[int, int, int], matrix: Matrix, denominator: int
) -> dict[str, object] | None:
    """Return the least strict integer inverse source for a fixed transport."""
    profile = inverse_profile(prime, target, matrix, denominator)
    source_denominator = least_source_denominator(profile)
    if source_denominator is None or source_denominator >= prime:
        return None
    source = tuple(
        source_denominator * coordinate.denominator // coordinate.numerator
        for coordinate in profile
    )
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(
        4, source_denominator
    ):
        raise AssertionError("inverse profile did not reconstruct the source equation")

    recovered = []
    for row in matrix:
        reciprocal = Fraction(source_denominator, prime * denominator) * sum(
            Fraction(weight, value) for weight, value in zip(row, source)
        )
        if reciprocal.numerator != 1:
            raise AssertionError("inverse profile did not recover unit target terms")
        recovered.append(reciprocal.denominator)
    if tuple(recovered) != target:
        raise AssertionError("inverse profile recovered the wrong target")
    return {
        "matrix_denominator": denominator,
        "matrix": [list(row) for row in matrix],
        "source_denominator": source_denominator,
        "source_solution": list(source),
        "target_solution": list(target),
    }


def ac_reverse_audit(
    prime: int, ac_bound: int, max_matrix_denominator: int
) -> dict[str, object]:
    """Audit every bounded-AC target against every low-denominator matrix."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    raw = targeted_bridge.ac_first_term_audit(prime, ac_bound)
    matrices = matrices_through(max_matrix_denominator)
    matrix_histogram = Counter(denominator for denominator, _ in matrices)
    records = []
    for record in raw["records"]:
        solution = targeted_bridge.type_ii_solution(
            prime, record["a"], record["c"], record["k"]
        )
        target = (solution["x"], solution["y"], solution["z"])
        lifts = [
            lift
            for denominator, matrix in matrices
            if (
                lift := reverse_lift(prime, target, matrix, denominator)
            )
            is not None
        ]
        records.append(
            {
                "a": record["a"],
                "c": record["c"],
                "k": record["k"],
                "h": record["h"],
                "gap": solution["gap"],
                "target_solution": list(target),
                "reverse_doubly_stochastic_lifts": lifts,
            }
        )
    return {
        "arithmetic": (
            "exact fractions.Fraction adjugate inverse and integer source "
            "reconstruction"
        ),
        "scope_note": (
            "The matrix family is exhaustive only for reduced, invertible, "
            "genuinely mixing 3 by 3 doubly-stochastic matrices with the stated "
            "denominator bound. Empty output excludes every strict inverse source "
            "for that family, not nonlinear or higher-denominator transports."
        ),
        "prime": prime,
        "ac_bound": ac_bound,
        "max_matrix_denominator": max_matrix_denominator,
        "target_solutions": len(records),
        "matrix_count_by_denominator": dict(sorted(matrix_histogram.items())),
        "matrix_count": len(matrices),
        "candidate_profiles": len(matrices) * len(records),
        "records": records,
        "reverse_doubly_stochastic_lifts": sum(
            len(record["reverse_doubly_stochastic_lifts"]) for record in records
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=2_451_289)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--max-matrix-denominator", type=int, default=10)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = ac_reverse_audit(
        args.prime, args.ac_bound, args.max_matrix_denominator
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
