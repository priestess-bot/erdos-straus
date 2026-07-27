#!/usr/bin/env python3
"""Verify the algebra behind fixed-tail two-source lift rigidity.

For distinct stationary scales k,l, try to use c*n_l as one tail in

    4/n_k = 1/(k*n_k) + 1/(c*n_l) + 1/v.

The remaining denominator is v=c*(k*n_k)*n_l/D with
D=c*(4k-1)*n_l-k*n_k.  A uniform lift would require D to divide the
product for every parameter.  The affine forms k*n_k and n_l are never
proportional for k!=l, so polynomial remainder rigidity rules this out for
every fixed positive c.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "two-source-fixed-tail-rigidity.json"


def source_form(prime_step: int, prime_residue: int, scale: int) -> tuple[int, int]:
    """Return n_k=A*t+B for p=prime_step*t+prime_residue."""
    q = 4 * scale - 1
    denominator = 4 * scale
    if prime_step % denominator or (q * prime_residue + 1) % denominator:
        raise ValueError("scale is not stationary on this prime progression")
    return q * prime_step // denominator, (q * prime_residue + 1) // denominator


def determinant(
    left: tuple[int, int], right: tuple[int, int]
) -> int:
    return left[0] * right[1] - left[1] * right[0]


def symbolic_profile(
    prime_step: int, prime_residue: int, left_scale: int, right_scale: int, multiplier: int
) -> dict[str, int | bool]:
    """Check all nonproportionality terms in the fixed-tail obstruction."""
    if left_scale == right_scale or multiplier < 1:
        raise ValueError("require distinct positive scales and positive multiplier")
    left_source = source_form(prime_step, prime_residue, left_scale)
    right_source = source_form(prime_step, prime_residue, right_scale)
    left_product = (left_scale * left_source[0], left_scale * left_source[1])
    q = 4 * left_scale - 1
    tail_difference = (
        multiplier * q * right_source[0] - left_product[0],
        multiplier * q * right_source[1] - left_product[1],
    )
    return {
        "left_scale": left_scale,
        "right_scale": right_scale,
        "multiplier": multiplier,
        "source_determinant": determinant(left_product, right_source),
        "tail_difference_slope": tail_difference[0],
        "tail_difference_with_left_determinant": determinant(tail_difference, left_product),
        "tail_difference_with_right_determinant": determinant(tail_difference, right_source),
        "sources_nonproportional": determinant(left_product, right_source) != 0,
        "tail_difference_nonconstant": tail_difference[0] != 0,
    }


def run_audit() -> dict[str, object]:
    # The common post-affine H19-k23 progression step and one residual constant.
    prime_step = 1_552_726_375_200
    prime_residue = 932_109_739_201
    scales = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 23)
    profiles = [
        symbolic_profile(prime_step, prime_residue, left, right, multiplier)
        for left in scales
        for right in scales
        if left != right
        for multiplier in (1, 2, 7, 19)
    ]
    if not all(
        profile["sources_nonproportional"]
        and profile["tail_difference_nonconstant"]
        and profile["tail_difference_with_left_determinant"] != 0
        and profile["tail_difference_with_right_determinant"] != 0
        for profile in profiles
    ):
        raise AssertionError("unexpected proportional two-source form")
    return {
        "arithmetic": (
            "exact affine source forms and determinant checks for the fixed-tail "
            "two-source remainder denominator"
        ),
        "scope_note": (
            "The proof is general for distinct stationary scales. The finite "
            "profiles only check the formulas on representative H19-k23 data; "
            "the result does not exclude parameter-dependent tails or nonlinear coupling."
        ),
        "representative_profile_count": len(profiles),
        "profiles": profiles,
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
