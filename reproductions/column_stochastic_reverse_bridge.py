#!/usr/bin/env python3
"""Exact reverse audit for low-denominator column-stochastic transports.

For a nonnegative 3 by 3 integer matrix M with every column summing to D,
the rational map t'=(n/(pD))Mt carries every reciprocal vector of total 4/n
to one of total 4/p.  This program reverses every reduced, invertible,
genuinely mixing matrix in a finite denominator box against a fixed target
family.  It therefore decides every strict integer source in that box without
enumerating source Egyptian-fraction solutions.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
from itertools import product
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "column-stochastic-reverse-bridge-2451289-ac14-d6-results.json"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


targeted_bridge = load_module(
    "column_stochastic_targeted_bridge", "targeted_descent_bridge.py"
)

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def compositions(total: int):
    """Yield all ordered nonnegative triples having the prescribed sum."""
    for first in range(total + 1):
        for second in range(total - first + 1):
            yield first, second, total - first - second


def determinant(matrix: Matrix) -> int:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def adjugate(matrix: Matrix) -> Matrix:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return (
        (e * i - f * h, c * h - b * i, b * f - c * e),
        (f * g - d * i, a * i - c * g, c * d - a * f),
        (d * h - e * g, b * g - a * h, a * e - b * d),
    )


def is_genuine_matrix(matrix: Matrix, denominator: int) -> bool:
    """Require reduced, invertible, nonnegative, genuinely mixing transport."""
    if denominator < 2:
        return False
    entries = tuple(entry for row in matrix for entry in row)
    if any(entry < 0 for entry in entries) or math.gcd(*entries) != 1:
        return False
    if any(sum(matrix[row][column] for row in range(3)) != denominator for column in range(3)):
        return False
    if any(sum(entry > 0 for entry in row) < 2 for row in matrix):
        return False
    if any(sum(matrix[row][column] > 0 for row in range(3)) < 2 for column in range(3)):
        return False
    return determinant(matrix) != 0


def matrices_at_denominator(denominator: int) -> tuple[Matrix, ...]:
    """Enumerate all reduced genuinely mixing column-stochastic matrices."""
    values: list[Matrix] = []
    columns = tuple(compositions(denominator))
    for first, second, third in product(columns, repeat=3):
        matrix = tuple(
            tuple(column[row] for column in (first, second, third)) for row in range(3)
        )
        if is_genuine_matrix(matrix, denominator):
            values.append(matrix)
    return tuple(values)


def matrices_through(max_denominator: int) -> tuple[tuple[int, Matrix], ...]:
    if max_denominator < 2:
        raise ValueError("max_matrix_denominator must be at least two")
    return tuple(
        (denominator, matrix)
        for denominator in range(2, max_denominator + 1)
        for matrix in matrices_at_denominator(denominator)
    )


def inverse_profile(
    prime: int, target: tuple[int, int, int], matrix: Matrix, denominator: int
) -> tuple[Fraction, Fraction, Fraction]:
    """Return H where every inverse reciprocal source vector is H/n."""
    if not is_genuine_matrix(matrix, denominator):
        raise ValueError("matrix is not a reduced genuine column-stochastic transport")
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
    if any(value <= 0 for value in profile):
        return None
    return max(2, math.lcm(*(value.numerator for value in profile)))


def reverse_lift(
    prime: int, target: tuple[int, int, int], matrix: Matrix, denominator: int
) -> dict[str, object] | None:
    """Return the least strict integer source for a fixed column-stochastic map."""
    profile = inverse_profile(prime, target, matrix, denominator)
    source_denominator = least_source_denominator(profile)
    if source_denominator is None or source_denominator >= prime:
        return None
    source = tuple(
        source_denominator * value.denominator // value.numerator for value in profile
    )
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(4, source_denominator):
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
    """Audit every bounded-AC target against the complete stated matrix box."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    raw = targeted_bridge.ac_first_term_audit(prime, ac_bound)
    matrices = matrices_through(max_matrix_denominator)
    histogram = Counter(denominator for denominator, _ in matrices)
    records = []
    for record in raw["records"]:
        solution = targeted_bridge.type_ii_solution(
            prime, record["a"], record["c"], record["k"]
        )
        target = (solution["x"], solution["y"], solution["z"])
        lifts = [
            lift
            for denominator, matrix in matrices
            if (lift := reverse_lift(prime, target, matrix, denominator)) is not None
        ]
        records.append(
            {
                "a": record["a"],
                "c": record["c"],
                "k": record["k"],
                "h": record["h"],
                "gap": solution["gap"],
                "target_solution": list(target),
                "reverse_column_stochastic_lifts": lifts,
            }
        )
    return {
        "arithmetic": "exact fractions.Fraction adjugate inverse and integer reconstruction",
        "scope_note": (
            "The family is exhaustive only for reduced, invertible, nonnegative, "
            "genuinely mixing 3 by 3 column-stochastic matrices within the stated "
            "denominator bound. It does not cover singular, nonlinear, or "
            "higher-denominator transports."
        ),
        "prime": prime,
        "ac_bound": ac_bound,
        "max_matrix_denominator": max_matrix_denominator,
        "target_solutions": len(records),
        "matrix_count_by_denominator": dict(sorted(histogram.items())),
        "matrix_count": len(matrices),
        "candidate_profiles": len(matrices) * len(records),
        "records": records,
        "reverse_column_stochastic_lifts": sum(
            len(record["reverse_column_stochastic_lifts"]) for record in records
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=2_451_289)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--max-matrix-denominator", type=int, default=6)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = ac_reverse_audit(args.prime, args.ac_bound, args.max_matrix_denominator)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
