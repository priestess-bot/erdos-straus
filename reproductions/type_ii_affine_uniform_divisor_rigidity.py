#!/usr/bin/env python3
"""Verify the rigidity normal form for uniform affine Type II divisors.

For x(n)=S*n+T, every positive nonconstant affine d(n)=A*n+B
which divides x(n)^2 for every n and is eventually at most x(n) has

    x=E*N, d=a*N, E=gcd(S,T), a|E^2, 1<=a<=E.

The factor a need not divide E. Thus square-only affine divisor families are
larger than the usual d|x fixed-factor trap, but their data remain finite
once E is fixed.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-affine-uniform-divisor-rigidity.json"


def classify(S: int, T: int, A: int, B: int) -> dict[str, int | bool]:
    """Classify a proposed nonconstant affine divisor d=A*n+B."""
    if min(S, T, A, B) <= 0:
        raise ValueError("all affine coefficients must be positive")
    E = math.gcd(S, T)
    determinant = A * T - S * B
    result: dict[str, int | bool] = {
        "S": S,
        "T": T,
        "A": A,
        "B": B,
        "E": E,
        "determinant": determinant,
        "is_proportional": determinant == 0,
    }
    if determinant:
        return result
    N_coefficient = S // E
    N_constant = T // E
    if A % N_coefficient or B % N_constant:
        raise AssertionError("proportional integral affine forms were misclassified")
    a = A // N_coefficient
    if B != a * N_constant:
        raise AssertionError("inconsistent proportionality parameter")
    result.update(
        {
            "a": a,
            "a_divides_E_squared": E * E % a == 0,
            "a_at_most_E": a <= E,
            "a_divides_E": E % a == 0,
        }
    )
    return result


def verify_samples(S: int, T: int, A: int, B: int, count: int = 8) -> None:
    """Check d|x^2 and d<=x on a finite diagnostic sample."""
    for n in range(count):
        x = S * n + T
        divisor = A * n + B
        if divisor > x or x * x % divisor:
            raise AssertionError("sample does not satisfy the divisor conditions")


def type_ii_example() -> dict[str, object]:
    """Give a square-only uniform divisor with an explicit Type II identity."""
    # x=12(n+1), d=9(n+1); a=9 divides 12^2 but not 12.
    S, T, A, B, gap = 12, 12, 9, 9, 7
    classification = classify(S, T, A, B)
    if (
        not classification["a_divides_E_squared"]
        or classification["a_divides_E"]
        or not classification["a_at_most_E"]
    ):
        raise AssertionError("expected a genuinely square-only divisor")
    verify_samples(S, T, A, B)
    samples = []
    for n in range(4):
        x = S * n + T
        divisor = A * n + B
        prime_candidate = 4 * x - gap
        y = prime_candidate * (x + divisor) // gap
        z = prime_candidate * (x + x * x // divisor) // gap
        exact = Fraction(4, prime_candidate) == (
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        )
        if not exact:
            raise AssertionError("Type II reconstruction failed")
        samples.append(
            {
                "n": n,
                "p": prime_candidate,
                "x": x,
                "d": divisor,
                "y": y,
                "z": z,
                "exact_identity": exact,
            }
        )
    return {
        "classification": classification,
        "gap": gap,
        "gap_divides_E_plus_a": (
            int(classification["E"]) + int(classification["a"])
        )
        % gap
        == 0,
        "samples": samples,
    }


def run_audit() -> dict[str, object]:
    square_only = type_ii_example()
    nonproportional = classify(12, 12, 9, 10)
    if nonproportional["is_proportional"]:
        raise AssertionError("nonproportional control was misclassified")
    return {
        "arithmetic": (
            "exact determinant calculation, integer divisor checks, and "
            "fractions.Fraction verification of an explicit square-only "
            "Type II affine family"
        ),
        "square_only_example": square_only,
        "nonproportional_control": nonproportional,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
