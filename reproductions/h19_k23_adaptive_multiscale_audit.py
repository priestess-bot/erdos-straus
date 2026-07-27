#!/usr/bin/env python3
"""Audit adaptive complete-square-tail descents on the 14 H19-k23 states.

For every prime value p=P*t+C in the first PARAMETER_LIMIT layers of every
post-affine residual progression, inspect the 37 stationary scales in their
fixed order.  At scale k, put M=k*n_k and q=4*k-1.  A strict source descent
exists exactly when some e|M^2 satisfies e=-M (mod q); the complementary
divisor lets us take e<=M.  This is a finite parameter audit, not a uniform
scale-selection theorem.
"""

from __future__ import annotations

from collections import Counter
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-adaptive-multiscale-audit.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
PARAMETER_LIMIT = 1_024


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "h19_k23_adaptive_multiscale_mixed_boundary", MIXED_BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load mixed-factor boundary")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_mixed_boundary()
branching = mixed_boundary.branching


def is_prime_64(value: int) -> bool:
    """Deterministic Miller--Rabin for every value below 2**64."""
    if not 2 <= value < 2**64:
        raise ValueError("audit primality input must be in the 64-bit range")
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value == prime:
            return True
        if value % prime == 0:
            return False
    exponent = value - 1
    power = 0
    while exponent % 2 == 0:
        exponent //= 2
        power += 1
    # These seven bases are deterministic below 341,550,071,728,321; the
    # standard 64-bit set below supplies the required wider range.
    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        reduced_base = base % value
        if reduced_base == 0:
            continue
        residue = pow(reduced_base, exponent, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor a 64-bit source product and independently check the result."""
    factors = tuple(sorted((int(prime), int(power)) for prime, power in sympy.factorint(value).items()))
    if math.prod(prime**power for prime, power in factors) != value:
        raise AssertionError("factorization product mismatch")
    if not all(is_prime_64(prime) for prime, _ in factors):
        raise AssertionError("factorization contains a composite factor")
    return factors


def divisor_residue_witness(
    factors: tuple[tuple[int, int], ...], modulus: int, target: int, bound: int
) -> tuple[int | None, int]:
    """Find e|M^2, e<=M in one target residue class, with exact enumeration."""
    residues: dict[int, int] = {1: 1}
    for prime, exponent in factors:
        residues = {
            residue * pow(prime, power, modulus) % modulus: divisor * prime**power
            for residue, divisor in residues.items()
            for power in range(2 * exponent + 1)
        }
    candidate = residues.get(target % modulus)
    if candidate is None:
        return None, len(residues)
    complement = bound * bound // candidate
    if complement < candidate:
        candidate = complement
    if candidate > bound or bound * bound % candidate:
        raise AssertionError("complement reduction failed")
    return candidate, len(residues)


def source_witness(prime: int, scale: int) -> dict[str, object] | None:
    """Return a verified complete-square-tail lift at one stationary scale."""
    q = 4 * scale - 1
    numerator = q * prime + 1
    if numerator % (4 * scale):
        raise AssertionError("scale is not stationary at this prime")
    source = numerator // (4 * scale)
    product_value = scale * source
    factors = factorization(product_value)
    divisor, residue_count = divisor_residue_witness(
        factors, q, -product_value, product_value
    )
    if divisor is None:
        return None
    first_tail = (product_value + divisor) // q
    second_tail = product_value * first_tail // divisor
    if (
        (product_value + divisor) % q
        or product_value * first_tail % divisor
        or Fraction(4, source)
        != Fraction(1, product_value) + Fraction(1, first_tail) + Fraction(1, second_tail)
        or Fraction(4, prime)
        != Fraction(1, product_value * prime)
        + Fraction(1, first_tail)
        + Fraction(1, second_tail)
    ):
        raise AssertionError("invalid complete-square-tail strict lift")
    return {
        "k": scale,
        "q": q,
        "source_denominator": source,
        "source_product": product_value,
        "factorization": [
            {"prime": factor_prime, "exponent": exponent}
            for factor_prime, exponent in factors
        ],
        "square_tail_divisor": divisor,
        "residue_count": residue_count,
        "first_tail": first_tail,
        "second_tail": second_tail,
    }


def run_audit(parameter_limit: int = PARAMETER_LIMIT) -> dict[str, object]:
    """Audit the first parameter_limit layers of all 14 residual branches."""
    if parameter_limit < 1:
        raise ValueError("parameter_limit must be positive")
    branches = mixed_boundary.remaining_branches()
    scales = tuple(branching.SCALES)
    records: list[dict[str, object]] = []
    scale_histogram: Counter[int] = Counter()
    prime_count_by_branch: Counter[int] = Counter()
    escaped: list[dict[str, int]] = []

    for branch in branches:
        form = branch["prime_form"]
        coefficient = int(form["coefficient"])
        constant = int(form["constant"])
        for parameter in range(parameter_limit):
            prime = coefficient * parameter + constant
            if not is_prime_64(prime):
                continue
            prime_count_by_branch[branch["v_mod_29"]] += 1
            witness = None
            tested_scales = 0
            for scale in scales:
                tested_scales += 1
                witness = source_witness(prime, scale)
                if witness is not None:
                    break
            if witness is None:
                escaped.append(
                    {
                        "v_mod_29": branch["v_mod_29"],
                        "parameter": parameter,
                        "prime": prime,
                    }
                )
                continue
            scale_histogram[int(witness["k"])] += 1
            records.append(
                {
                    "v_mod_29": branch["v_mod_29"],
                    "parameter": parameter,
                    "prime": prime,
                    "tested_scale_count": tested_scales,
                    "first_success": witness,
                }
            )

    if len(branches) != 14:
        raise AssertionError("expected fourteen post-affine residual branches")
    if len(records) + len(escaped) != sum(prime_count_by_branch.values()):
        raise AssertionError("prime classification is incomplete")
    return {
        "arithmetic": (
            "deterministic 64-bit primality, complete 64-bit source-product "
            "factorization, exact M_k^2 divisor-residue enumeration, and "
            "Fraction verification of every recorded strict lift"
        ),
        "scope_note": (
            "A finite adaptive-scale audit on concrete prime values. It does "
            "not prove that 37 scales, or any bounded scale set, succeeds on "
            "every value of a residual progression."
        ),
        "parameter_limit_exclusive": parameter_limit,
        "state_schema": {
            "post_affine_residual_branch_count": len(branches),
            "stationary_scale_count": len(scales),
        },
        "prime_count": sum(prime_count_by_branch.values()),
        "prime_count_by_branch": {
            str(branch): count for branch, count in sorted(prime_count_by_branch.items())
        },
        "first_success_scale_histogram": {
            str(scale): count for scale, count in sorted(scale_histogram.items())
        },
        "largest_first_success_scale": max(scale_histogram, default=None),
        "uncovered_records": escaped,
        "records": records,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary = {
        key: payload[key]
        for key in (
            "parameter_limit_exclusive",
            "prime_count",
            "first_success_scale_histogram",
            "largest_first_success_scale",
            "uncovered_records",
        )
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
