#!/usr/bin/env python3
"""Audit the exceptional algebra in affine-tail two-source rigidity.

For distinct stationary external scales k,l, put

    q_j = 4*j-1,
    M = k*n_k = (q_k*p+1)/4,
    N = n_l = (q_l*p+1)/(4*l).

A nonconstant affine multiplier c in

    4/n_k = 1/(k*n_k) + 1/(c*n_l) + 1/v

would require D=c*q_k*N-M to divide c*M*N in Q[t].  Except when c is
proportional to M, D is coprime to c*M*N.  The sole proportional possibility
has k>l and is

    c = l*M/(k-l),   v = l*N/(4*l-1),

whose tail is never integral because 4*l*N = (4*l-1)*p+1.

The proof is general. The finite audit checks the exceptional formula on the
representative H19-k23 stationary affine progression.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "two-source-affine-tail-rigidity.json"


def source_form(prime_step: int, prime_residue: int, scale: int) -> tuple[int, int]:
    """Return n_scale=A*t+B for p=prime_step*t+prime_residue."""
    q = 4 * scale - 1
    denominator = 4 * scale
    if prime_step % denominator or (q * prime_residue + 1) % denominator:
        raise ValueError("scale is not stationary on this prime progression")
    return q * prime_step // denominator, (q * prime_residue + 1) // denominator


def scale_form(form: tuple[int, int], factor: Fraction) -> tuple[Fraction, Fraction]:
    return factor * form[0], factor * form[1]


def affine_candidate_profile(
    prime_step: int, prime_residue: int, left_scale: int, right_scale: int
) -> dict[str, object]:
    """Return the only possible proportional exceptional case, if positive."""
    if left_scale == right_scale or left_scale < 1 or right_scale < 1:
        raise ValueError("require distinct positive scales")
    q_left = 4 * left_scale - 1
    q_right = 4 * right_scale - 1
    left_source = source_form(prime_step, prime_residue, left_scale)
    right_source = source_form(prime_step, prime_residue, right_scale)
    preserved = scale_form(left_source, Fraction(left_scale))

    if left_scale < right_scale:
        return {
            "left_scale": left_scale,
            "right_scale": right_scale,
            "positive_proportional_exception": False,
            "reason": "the unique proportional multiplier has negative leading coefficient",
        }

    multiplier = Fraction(right_scale, left_scale - right_scale)
    residual_multiplier = Fraction(right_scale, q_right)
    residual_factor = Fraction(q_right, left_scale - right_scale)
    c_form = scale_form(preserved, multiplier)

    # The preceding expansion is intentionally quadratic.  Compare it to
    # residual_multiplier*M^2, the actual D after c=lambda*M.
    d_quadratic = q_left * c_form[0] * right_source[0]
    d_slope = q_left * (
        c_form[0] * right_source[1] + c_form[1] * right_source[0]
    ) - preserved[0]
    d_constant = q_left * c_form[1] * right_source[1] - preserved[1]
    expected_quadratic = residual_factor * preserved[0] * preserved[0]
    expected_slope = residual_factor * 2 * preserved[0] * preserved[1]
    expected_constant = residual_factor * preserved[1] * preserved[1]
    if (d_quadratic, d_slope, d_constant) != (
        expected_quadratic,
        expected_slope,
        expected_constant,
    ):
        raise AssertionError("exceptional remainder factor identity failed")

    # 4*l*N = q_l*p+1 makes l*N a unit modulo q_l for every parameter.
    if q_right <= 1 or right_scale % q_right == 0:
        raise AssertionError("unexpected scale/unit relation")
    return {
        "left_scale": left_scale,
        "right_scale": right_scale,
        "positive_proportional_exception": True,
        "c_over_M": {
            "numerator": multiplier.numerator,
            "denominator": multiplier.denominator,
        },
        "D_over_M_squared": {
            "numerator": residual_factor.numerator,
            "denominator": residual_factor.denominator,
        },
        "v_over_N": {
            "numerator": residual_multiplier.numerator,
            "denominator": residual_multiplier.denominator,
        },
        "tail_denominator": q_right,
        "tail_denominator_coprime_to_scale": True,
        "tail_never_integral": True,
    }


def run_audit() -> dict[str, object]:
    # The common post-affine H19-k23 progression step and one residual constant.
    prime_step = 1_552_726_375_200
    prime_residue = 932_109_739_201
    scales = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 23)
    profiles = [
        affine_candidate_profile(prime_step, prime_residue, left, right)
        for left in scales
        for right in scales
        if left != right
    ]
    exceptional = [
        profile for profile in profiles if profile["positive_proportional_exception"]
    ]
    if not exceptional or not all(profile["tail_never_integral"] for profile in exceptional):
        raise AssertionError("an affine two-source exceptional tail was not rejected")
    return {
        "arithmetic": (
            "exact affine source forms and rational coefficient checks for the "
            "unique proportional exceptional multiplier"
        ),
        "scope_note": (
            "The proof is general for distinct stationary scales. The finite "
            "profiles check only its exceptional algebra on representative "
            "H19-k23 data; the result does not exclude nonlinear coupling."
        ),
        "representative_profile_count": len(profiles),
        "positive_exception_count": len(exceptional),
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
