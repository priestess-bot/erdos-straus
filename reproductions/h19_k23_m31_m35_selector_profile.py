#!/usr/bin/env python3
"""Profile m=35 selectors after the H19-k23 m=31 one-prime boundary."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-m31-m35-selector-profile-262144.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
FIXED_FACTOR = 3**4 * 13**2


def load_branches():
    spec = importlib.util.spec_from_file_location("h19_k23_m35_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def fixed_divisors() -> list[int]:
    return sorted(3**three_power * 13**thirteen_power for three_power in range(5) for thirteen_power in range(3))


def selector_witness(prime: int, divisor: int) -> dict[str, int]:
    normalized = family.verify_normal_form(prime, 35, divisor)
    if normalized["q"] != 9:
        raise AssertionError("m=35 did not recover q=9")
    return normalized


def new_prime_powers(u: int) -> dict[int, list[int]]:
    if u % 13:
        raise ValueError("u must contain the uniform factor 13")
    result: dict[int, list[int]] = {}
    for prime, multiplicity in sympy.factorint(u // 13).items():
        prime = int(prime)
        if prime in {3, 13}:
            continue
        power = 1
        values = []
        for _ in range(2 * int(multiplicity)):
            power *= prime
            values.append(power)
        result[prime] = values
    return result


def selector_divisor(u: int, support_size: int) -> int | None:
    """Return a fixed-base divisor supported on exactly one or two new primes."""
    if support_size not in {0, 1, 2}:
        raise ValueError("support_size must be zero, one, or two")
    target = (-9 * u) % 35
    primes = new_prime_powers(u)
    candidates: list[int] = []
    if support_size == 0:
        products = [1]
    elif support_size == 1:
        products = [power for powers in primes.values() for power in powers]
    else:
        products = [
            left_power * right_power
            for index, (_, left_powers) in enumerate(sorted(primes.items()))
            for _, right_powers in sorted(primes.items())[index + 1 :]
            for left_power in left_powers
            for right_power in right_powers
        ]
    for product in products:
        for fixed in fixed_divisors():
            divisor = fixed * product
            if divisor <= 9 * u and divisor % 35 == target:
                candidates.append(divisor)
    return min(candidates) if candidates else None


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Classify the m=35 exit after every recorded m=31 selector miss."""
    branches = load_branches()
    coefficient = int(branches[0]["prime_form"]["coefficient"])
    constants = {int(branch["prime_form"]["constant"]) for branch in branches}
    for branch in branches:
        form = branch["prime_form"]
        if int(form["coefficient"]) != coefficient:
            raise AssertionError("residual branches do not share a coefficient")
        if coefficient % 36 or (int(form["constant"]) - 1) % 36:
            raise AssertionError("m=35 is not universally available on the branch")
        if (coefficient // 36) % 13 or ((int(form["constant"]) + 35) // 36) % 13:
            raise AssertionError("the fixed m=35 factor is not uniform on the branch")

    counts: Counter[str] = Counter()
    later_tail_gaps: Counter[int] = Counter()
    for record in payload["records"]:
        if (
            int(record["shared_selector_gap"]) != 27
            or record["route"] != "alternative-p-minus-one-gap"
            or int(record["tail_witness"]["gap"]) == 31
        ):
            continue
        prime = int(record["prime"])
        if prime % coefficient not in constants:
            raise AssertionError("m=31 miss is outside the residual branch set")
        u = (prime + 35) // 36
        if u % 13:
            raise AssertionError("m=31 miss lost the fixed m=35 factor")
        fixed = selector_divisor(u, 0)
        one_new = selector_divisor(u, 1)
        two_new = selector_divisor(u, 2)
        tail_gap = int(record["tail_witness"]["gap"])
        if tail_gap == 35:
            if fixed is not None:
                selector_witness(prime, fixed)
                counts["fixed_m35_hit"] += 1
            elif one_new is not None:
                selector_witness(prime, one_new)
                counts["one_new_prime_m35_hit"] += 1
            elif two_new is not None:
                selector_witness(prime, two_new)
                counts["two_new_prime_m35_hit"] += 1
            else:
                raise AssertionError("m=35 tail has no bounded selector support")
        else:
            if fixed is not None or one_new is not None or two_new is not None:
                raise AssertionError("bounded m=35 selector contradicted the stored first tail gap")
            counts["m35_miss"] += 1
            later_tail_gaps[tail_gap] += 1
    total = sum(counts.values())
    return {
        "arithmetic": (
            "exact branch congruences for 36|p-1 and 13|(p+35)/36, complete "
            "fixed-base one- and two-new-prime-power divisor enumeration, and exact "
            "q=9 square-root-completion verification for every constructed m=35 witness"
        ),
        "scope_note": (
            "A finite selector profile after the stored m=31 misses. It does not "
            "assert a bounded-support selector beyond this artifact."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "m31_miss_record_count": total,
        "all_branches_have_36_dividing_p_minus_one": True,
        "all_branches_have_13_dividing_m35_u": True,
        "fixed_m35_factor": FIXED_FACTOR,
        "fixed_m35_selector_hit_count": counts["fixed_m35_hit"],
        "one_new_prime_m35_selector_hit_count": counts["one_new_prime_m35_hit"],
        "two_new_prime_m35_selector_hit_count": counts["two_new_prime_m35_hit"],
        "m35_selector_miss_count": counts["m35_miss"],
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
