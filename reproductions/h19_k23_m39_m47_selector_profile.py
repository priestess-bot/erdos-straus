#!/usr/bin/env python3
"""Profile m=47 support after the H19-k23 m=39 selector boundary."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-m39-m47-selector-profile-262144.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
BASE_EXPONENTS = {2: 4, 3: 2}


def load_branches():
    spec = importlib.util.spec_from_file_location("h19_k23_m47_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def smooth_base_divisors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, base_exponent in sorted(BASE_EXPONENTS.items()):
        prior = tuple(values)
        power = 1
        for _ in range(base_exponent + 2 * factors.get(prime, 0)):
            power *= prime
            values.extend(value * power for value in prior)
    return values


def new_prime_powers(factors: dict[int, int]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for prime, multiplicity in factors.items():
        if prime in BASE_EXPONENTS:
            continue
        power = 1
        values = []
        for _ in range(2 * multiplicity):
            power *= prime
            values.append(power)
        result[prime] = values
    return result


def selector_divisor(u: int, support_size: int) -> int | None:
    if support_size not in {0, 1, 2}:
        raise ValueError("support_size must be zero, one, or two")
    factors = {int(prime): int(power) for prime, power in sympy.factorint(u).items()}
    base = smooth_base_divisors(factors)
    new_powers = new_prime_powers(factors)
    if support_size == 0:
        products = [1]
    elif support_size == 1:
        products = [power for values in new_powers.values() for power in values]
    else:
        ordered = sorted(new_powers.items())
        products = [
            left_power * right_power
            for index, (_, left_values) in enumerate(ordered)
            for _, right_values in ordered[index + 1 :]
            for left_power in left_values
            for right_power in right_values
        ]
    target = (-12 * u) % 47
    candidates = [
        base_divisor * product
        for base_divisor in base
        for product in products
        if base_divisor * product <= 12 * u and (base_divisor * product) % 47 == target
    ]
    return min(candidates) if candidates else None


def verify_witness(prime: int, divisor: int) -> None:
    normalized = family.verify_normal_form(prime, 47, divisor)
    if normalized["q"] != 12:
        raise AssertionError("m=47 did not recover q=12")


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Classify m=47 exits after stored m=31, m=35, and m=39 misses."""
    branches = load_branches()
    coefficient = int(branches[0]["prime_form"]["coefficient"])
    constants = {int(branch["prime_form"]["constant"]) for branch in branches}
    for branch in branches:
        form = branch["prime_form"]
        if int(form["coefficient"]) != coefficient:
            raise AssertionError("residual branches do not share a coefficient")
        if coefficient % 48 or (int(form["constant"]) - 1) % 48:
            raise AssertionError("m=47 is not universally available on the branch")

    counts: Counter[str] = Counter()
    later_tail_gaps: Counter[int] = Counter()
    for record in payload["records"]:
        if (
            int(record["shared_selector_gap"]) != 27
            or record["route"] != "alternative-p-minus-one-gap"
            or int(record["tail_witness"]["gap"]) in {31, 35, 39}
        ):
            continue
        prime = int(record["prime"])
        if prime % coefficient not in constants:
            raise AssertionError("m=39 miss is outside the residual branch set")
        u = (prime + 47) // 48
        fixed = selector_divisor(u, 0)
        one_new = selector_divisor(u, 1)
        two_new = selector_divisor(u, 2)
        tail_gap = int(record["tail_witness"]["gap"])
        if tail_gap == 47:
            if fixed is not None:
                verify_witness(prime, fixed)
                counts["smooth_base_m47_hit"] += 1
            elif one_new is not None:
                verify_witness(prime, one_new)
                counts["one_new_prime_m47_hit"] += 1
            elif two_new is not None:
                verify_witness(prime, two_new)
                counts["two_new_prime_m47_hit"] += 1
            else:
                raise AssertionError("m=47 tail has no support-two selector")
        else:
            if fixed is not None or one_new is not None or two_new is not None:
                raise AssertionError("bounded m=47 selector contradicted the stored first tail gap")
            counts["m47_miss"] += 1
            later_tail_gaps[tail_gap] += 1
    total = sum(counts.values())
    return {
        "arithmetic": (
            "exact branch congruences for 48|p-1, complete 2,3-smooth-base "
            "extension plus one- and two-new-prime-power divisor enumeration, and "
            "exact q=12 square-root-completion verification for every constructed witness"
        ),
        "scope_note": "A finite support profile after stored m=39 misses.",
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "m39_miss_record_count": total,
        "all_branches_have_48_dividing_p_minus_one": True,
        "smooth_base_m47_selector_hit_count": counts["smooth_base_m47_hit"],
        "one_new_prime_m47_selector_hit_count": counts["one_new_prime_m47_hit"],
        "two_new_prime_m47_selector_hit_count": counts["two_new_prime_m47_hit"],
        "m47_selector_miss_count": counts["m47_miss"],
        "later_tail_gap_histogram": {str(gap): count for gap, count in sorted(later_tail_gaps.items())},
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
