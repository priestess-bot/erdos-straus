#!/usr/bin/env python3
"""Profile the m=31 divisor-selector boundary inside H19-k23 m=27 residuals."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions import type_ii_square_root_completion_family as family  # noqa: E402


DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-m27-m31-selector-profile-262144.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
FIXED_M31_FACTOR = 2**6 * 7**2 * 19**2


def load_branches():
    spec = importlib.util.spec_from_file_location("h19_k23_m31_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def m31_selector_witness(prime: int, divisor: int) -> dict[str, int]:
    """Verify the exact divisor condition for the universally available m=31 tail."""
    normalized = family.verify_normal_form(prime, 31, divisor)
    if normalized["q"] != 8:
        raise AssertionError("m=31 did not recover q=8")
    return normalized


def fixed_m31_divisors() -> list[int]:
    """All divisors of 2^6*7^2*19^2, in deterministic increasing order."""
    return sorted(
        2**two_power * 7**seven_power * 19**nineteen_power
        for two_power in range(7)
        for seven_power in range(3)
        for nineteen_power in range(3)
    )


def fixed_m31_selector_divisor(u: int) -> int | None:
    """Return the least fixed-factor divisor in the required m=31 residue class."""
    target = (-8 * u) % 31
    return next((divisor for divisor in fixed_m31_divisors() if divisor % 31 == target), None)


def one_new_prime_m31_selector_divisor(u: int) -> tuple[int, int, int] | None:
    """Return a fixed-factor times one-new-prime-power m=31 divisor, if present."""
    if u % 133:
        raise ValueError("u must contain the uniform factor 133")
    target = (-8 * u) % 31
    candidates: list[tuple[int, int, int]] = []
    for prime, multiplicity in sympy.factorint(u // 133).items():
        prime = int(prime)
        if prime in {2, 7, 19}:
            continue
        power = 1
        for exponent in range(1, 2 * int(multiplicity) + 1):
            power *= prime
            for fixed_divisor in fixed_m31_divisors():
                divisor = fixed_divisor * power
                if divisor <= 8 * u and divisor % 31 == target:
                    candidates.append((divisor, prime, exponent))
    return min(candidates) if candidates else None


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Separate the m=31 selection problem from later alternative tail gaps."""
    branches = load_branches()
    coefficient = int(branches[0]["prime_form"]["coefficient"])
    branch_by_constant = {
        int(branch["prime_form"]["constant"]): int(branch["v_mod_29"])
        for branch in branches
    }
    if len(branch_by_constant) != len(branches):
        raise AssertionError("branch constants are not unique")
    for branch in branches:
        form = branch["prime_form"]
        if int(form["coefficient"]) != coefficient:
            raise AssertionError("residual branches do not share a coefficient")
        if coefficient % 32 or (int(form["constant"]) - 1) % 32:
            raise AssertionError("m=31 is not universally available on the branch")
        if (coefficient // 32) % 133 or ((int(form["constant"]) + 31) // 32) % 133:
            raise AssertionError("the fixed m=31 square factor is not uniform on the branch")

    per_branch: dict[int, Counter[str]] = {int(branch["v_mod_29"]): Counter() for branch in branches}
    later_tail_gaps: Counter[int] = Counter()
    selector_hits = 0
    selector_misses = 0
    fixed_selector_hits = 0
    one_new_prime_hits = 0
    for record in payload["records"]:
        if (
            int(record["shared_selector_gap"]) != 27
            or record["route"] != "alternative-p-minus-one-gap"
        ):
            continue
        prime = int(record["prime"])
        constant = prime % coefficient
        branch = branch_by_constant.get(constant)
        if branch is None:
            raise AssertionError("m=27 record is outside the residual branch set")
        witness = record["tail_witness"]
        if witness is None:
            raise AssertionError("closed record omitted its tail witness")
        tail_gap = int(witness["gap"])
        u = (prime - 1) // 32 + 1
        if u % 133:
            raise AssertionError("m=27 record missed the fixed u factor")
        fixed_divisor = fixed_m31_selector_divisor(u)
        one_new_prime_divisor = (
            None if fixed_divisor is not None else one_new_prime_m31_selector_divisor(u)
        )
        per_branch[branch]["m27_records"] += 1
        if tail_gap == 31:
            normalized = m31_selector_witness(prime, int(witness["divisor"]))
            if normalized["source_denominator"] != int(witness["source_denominator"]):
                raise AssertionError("m=31 source denominator changed under normalization")
            selector_hits += 1
            per_branch[branch]["m31_hits"] += 1
            if fixed_divisor is not None:
                fixed_normalized = m31_selector_witness(prime, fixed_divisor)
                if fixed_normalized["divisor"] > fixed_normalized["x"]:
                    raise AssertionError("fixed m=31 divisor exceeds x")
                fixed_selector_hits += 1
                per_branch[branch]["fixed_m31_hits"] += 1
            else:
                if one_new_prime_divisor is None:
                    raise AssertionError("m=31 hit has no fixed-plus-one-new-prime selector")
                one_new_prime_normalized = m31_selector_witness(
                    prime, one_new_prime_divisor[0]
                )
                if one_new_prime_normalized["divisor"] > one_new_prime_normalized["x"]:
                    raise AssertionError("one-new-prime m=31 divisor exceeds x")
                one_new_prime_hits += 1
                per_branch[branch]["one_new_prime_m31_hits"] += 1
        else:
            # The closure scan tries all p-1 indexed gaps in increasing order.
            # Since 32 | p-1 on every branch, this row records an exhausted m=31 miss.
            if tail_gap < 31:
                raise AssertionError("alternative tail ordering is inconsistent")
            selector_misses += 1
            per_branch[branch]["m31_misses"] += 1
            later_tail_gaps[tail_gap] += 1
            if fixed_divisor is not None:
                raise AssertionError("fixed m=31 selector contradicted the stored first tail gap")
            if one_new_prime_divisor is not None:
                raise AssertionError("one-new-prime selector contradicted the stored first tail gap")

    rows = [
        {
            "v_mod_29": residue,
            "m27_record_count": counts["m27_records"],
            "m31_selector_hit_count": counts["m31_hits"],
            "fixed_m31_selector_hit_count": counts["fixed_m31_hits"],
            "variable_m31_selector_hit_count": counts["m31_hits"] - counts["fixed_m31_hits"],
            "one_new_prime_m31_selector_hit_count": counts["one_new_prime_m31_hits"],
            "m31_selector_miss_count": counts["m31_misses"],
        }
        for residue, counts in sorted(per_branch.items())
    ]
    total = selector_hits + selector_misses
    if total != sum(row["m27_record_count"] for row in rows):
        raise AssertionError("branch profile does not partition the m=27 records")
    return {
        "arithmetic": (
            "exact affine checks that 32 divides p-1 on every residual branch; "
            "exact q=8 square-root-completion normalization for each fixed or "
            "fixed-plus-one-new-prime m=31 construction; "
            "and the stored increasing p-1 tail-gap scan for each recorded m=31 miss"
        ),
        "scope_note": (
            "A finite profile of the dominant alternative branch. A miss says the "
            "least scanned ordinary tail gap exceeded 31; it does not exclude another "
            "certificate model or prove a general divisor-selection obstruction."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "residual_branch_count": len(branches),
        "common_prime_coefficient": coefficient,
        "all_branches_have_32_dividing_p_minus_one": True,
        "all_branches_have_133_dividing_u": True,
        "fixed_m31_factor": FIXED_M31_FACTOR,
        "fixed_divisor_residue_set_mod_31": sorted(
            {divisor % 31 for divisor in fixed_m31_divisors()}
        ),
        "fixed_u_residue_set_mod_31": sorted(
            {
                (-4 * residue) % 31
                for residue in {divisor % 31 for divisor in fixed_m31_divisors()}
            }
        ),
        "m27_alternative_record_count": total,
        "m31_selector_hit_count": selector_hits,
        "fixed_m31_selector_hit_count": fixed_selector_hits,
        "variable_m31_selector_hit_count": selector_hits - fixed_selector_hits,
        "one_new_prime_m31_selector_hit_count": one_new_prime_hits,
        "one_new_prime_selector_miss_count": selector_misses,
        "m31_selector_miss_count": selector_misses,
        "later_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(later_tail_gaps.items())
        },
        "branch_profile": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
