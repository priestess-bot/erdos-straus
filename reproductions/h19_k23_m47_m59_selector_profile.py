#!/usr/bin/env python3
"""Close the H19-k23 m=27 tail-support ladder at m=59 and its terminal gaps."""

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

from reproductions import type_ii_square_root_completion_family as family


DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-m47-m59-selector-profile-262144.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
BASE_EXPONENTS = {3: 2, 5: 2, 7: 0}
TERMINAL_BASE_PRIMES = {63: {2}, 71: {2, 3}, 79: {2, 5}, 91: {23}, 95: {2, 3}}


def load_branches():
    spec = importlib.util.spec_from_file_location("h19_k23_m59_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def smooth_base_divisors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in sorted(BASE_EXPONENTS.items()):
        prior = tuple(values)
        power = 1
        for _ in range(exponent + 2 * factors.get(prime, 0)):
            power *= prime
            values.extend(value * power for value in prior)
    return values


def selector_divisor(u: int, support_size: int) -> int | None:
    if support_size not in {0, 1, 2}:
        raise ValueError("support_size must be zero, one, or two")
    factors = {int(prime): int(power) for prime, power in sympy.factorint(u).items()}
    base = smooth_base_divisors(factors)
    new = {prime: power for prime, power in factors.items() if prime not in BASE_EXPONENTS}
    if support_size == 0:
        products = [1]
    elif support_size == 1:
        products = [prime**exponent for prime, power in new.items() for exponent in range(1, 2 * power + 1)]
    else:
        products = [
            left**left_exponent * right**right_exponent
            for index, (left, left_power) in enumerate(sorted(new.items()))
            for right, right_power in sorted(new.items())[index + 1 :]
            for left_exponent in range(1, 2 * left_power + 1)
            for right_exponent in range(1, 2 * right_power + 1)
        ]
    target = (-15 * u) % 59
    candidates = [
        base_divisor * product
        for base_divisor in base
        for product in products
        if base_divisor * product <= 15 * u and (base_divisor * product) % 59 == target
    ]
    return min(candidates) if candidates else None


def terminal_support(prime: int, gap: int, divisor: int) -> int:
    normalized = family.verify_normal_form(prime, gap, divisor)
    if gap not in TERMINAL_BASE_PRIMES:
        raise ValueError("unexpected terminal gap")
    factors = sympy.factorint(divisor)
    return sum(1 for factor in factors if int(factor) not in TERMINAL_BASE_PRIMES[gap])


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    branches = load_branches()
    coefficient = int(branches[0]["prime_form"]["coefficient"])
    constants = {int(branch["prime_form"]["constant"]) for branch in branches}
    for branch in branches:
        form = branch["prime_form"]
        if int(form["coefficient"]) != coefficient:
            raise AssertionError("residual branches do not share a coefficient")
        if coefficient % 60 or (int(form["constant"]) - 1) % 60:
            raise AssertionError("m=59 is not universally available on the branch")
        if (coefficient // 60) % 7 or ((int(form["constant"]) + 59) // 60) % 7:
            raise AssertionError("the fixed m=59 factor is not uniform on the branch")

    counts: Counter[str] = Counter()
    terminal_counts: Counter[int] = Counter()
    terminal_support_histograms: dict[int, Counter[int]] = {gap: Counter() for gap in TERMINAL_BASE_PRIMES}
    for record in payload["records"]:
        if (
            int(record["shared_selector_gap"]) != 27
            or record["route"] != "alternative-p-minus-one-gap"
            or int(record["tail_witness"]["gap"]) in {31, 35, 39, 47}
        ):
            continue
        prime = int(record["prime"])
        if prime % coefficient not in constants:
            raise AssertionError("m=47 miss is outside the residual branch set")
        witness = record["tail_witness"]
        tail_gap = int(witness["gap"])
        u = (prime + 59) // 60
        fixed = selector_divisor(u, 0)
        one_new = selector_divisor(u, 1)
        two_new = selector_divisor(u, 2)
        if tail_gap == 59:
            selected = fixed or one_new or two_new
            if selected is None:
                raise AssertionError("m=59 tail has no support-two selector")
            family.verify_normal_form(prime, 59, selected)
            counts[
                "smooth_base_m59_hit" if fixed is not None else "one_new_prime_m59_hit"
                if one_new is not None else "two_new_prime_m59_hit"
            ] += 1
        else:
            if fixed is not None or one_new is not None or two_new is not None:
                raise AssertionError("bounded m=59 selector contradicted the stored first tail gap")
            support = terminal_support(prime, tail_gap, int(witness["divisor"]))
            if support > 2:
                raise AssertionError("terminal witness exceeded support two")
            counts["m59_miss"] += 1
            terminal_counts[tail_gap] += 1
            terminal_support_histograms[tail_gap][support] += 1
    total = sum(counts.values())
    return {
        "arithmetic": (
            "exact branch congruences for 60|p-1 and 7|(p+59)/60, complete "
            "3,5,7-smooth-base support-two enumeration at m=59, and exact normal-form "
            "verification plus factor-support checks at terminal gaps 63, 71, 79, 91, and 95"
        ),
        "scope_note": "A finite closure of the final m=27 tail-support ladder states.",
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "m47_miss_record_count": total,
        "all_branches_have_60_dividing_p_minus_one": True,
        "all_branches_have_7_dividing_m59_u": True,
        "smooth_base_m59_selector_hit_count": counts["smooth_base_m59_hit"],
        "one_new_prime_m59_selector_hit_count": counts["one_new_prime_m59_hit"],
        "two_new_prime_m59_selector_hit_count": counts["two_new_prime_m59_hit"],
        "m59_selector_miss_count": counts["m59_miss"],
        "terminal_gap_histogram": {str(gap): count for gap, count in sorted(terminal_counts.items())},
        "terminal_support_histograms": {
            str(gap): {str(support): count for support, count in sorted(histogram.items())}
            for gap, histogram in sorted(terminal_support_histograms.items())
            if histogram
        },
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
