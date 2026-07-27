#!/usr/bin/env python3
"""Profile strict descents using one adaptive nonbase prime power in global rewrites."""

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
DEFAULT_GLOBAL_INPUT = ROOT / "reproductions" / "h19-k23-full-global-tail-closure-2097152.json"
DEFAULT_REROUTE_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
NORMAL_FORM = ROOT / "reproductions" / "type_ii_square_root_completion_family.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


normal_form = load_module("h19_k23_global_one_prime_power_normal_form", NORMAL_FORM)


def first_power_one_witness(
    prime: int, gap: int, base_primes: set[int]
) -> int | None:
    """Return the least witness using exactly one power of one nonbase prime."""
    q = (gap + 1) // 4
    u = (prime + gap) // (gap + 1)
    x = q * u
    factors = {
        int(factor): 2 * int(exponent)
        for factor, exponent in sympy.factorint(x).items()
    }
    base_values = [1]
    for factor, exponent in sorted(factors.items()):
        if factor in base_primes:
            base_values = [
                value * factor**power
                for value in base_values
                for power in range(exponent + 1)
            ]
    target = (-x) % gap
    candidates = [
        base * factor
        for factor in sorted(factors)
        if factor not in base_primes
        for base in base_values
        if base * factor <= x and (base * factor) % gap == target
    ]
    return min(candidates) if candidates else None


def profile_witness(
    prime: int,
    gap: int,
    divisor: int,
    base_primes: set[int],
    route: str,
) -> dict[str, object]:
    """Factor one support witness and reconstruct its strict ordinary tail descent."""
    q = (gap + 1) // 4
    if (prime - 1) % (gap + 1):
        raise AssertionError("global tail is not an ordinary p-1 tail")
    tail_parameter = (prime - 1) // (gap + 1)
    descent = normal_form.two_tail_witness(q, divisor, tail_parameter)
    nonbase = [
        (int(factor), int(exponent))
        for factor, exponent in sympy.factorint(divisor).items()
        if int(factor) not in base_primes
    ]
    if len(nonbase) != 1:
        raise AssertionError("one-support witness has the wrong nonbase factorization")
    new_prime, new_exponent = nonbase[0]
    u = tail_parameter + 1
    if u % new_prime:
        raise AssertionError("new nonbase prime does not divide the adaptive tail factor")
    if int(descent["source_denominator"]) != u:
        raise AssertionError("ordinary source denominator is not the tail quotient")
    first_power_divisor = (
        divisor
        if new_exponent == 1
        else first_power_one_witness(prime, gap, base_primes)
    )
    return {
        "prime": prime,
        "route": route,
        "tail_gap": gap,
        "base_primes": sorted(base_primes),
        "divisor": divisor,
        "new_prime": new_prime,
        "new_prime_exponent": new_exponent,
        "first_power_one_witness": first_power_divisor,
        "source_denominator": u,
    }


def run_audit(
    global_payload: dict[str, object], reroute_payload: dict[str, object]
) -> dict[str, object]:
    """Profile every final one-support global rewrite, including later reroutes."""
    retained = [
        profile_witness(
            int(row["prime"]),
            int(row["global_tail_gap"]),
            int(row["divisor"]),
            {int(prime) for prime in row["base_primes"]},
            "retained-one-support",
        )
        for row in global_payload["replacements"]
        if int(row["support_defect"]) == 1
    ]
    rerouted = [
        profile_witness(
            int(row["prime"]),
            int(row["new_global_tail_gap"]),
            int(row["new_divisor"]),
            {int(prime) for prime in row["new_base_primes"]},
            "rerouted-from-two-support",
        )
        for row in reroute_payload["reroutes"]
        if int(row["new_support_defect"]) == 1
    ]
    records = sorted(retained + rerouted, key=lambda row: int(row["prime"]))
    if len({int(row["prime"]) for row in records}) != len(records):
        raise AssertionError("one-support profile contains duplicate prime rows")
    expected = int(reroute_payload["final_rewrite_support_histogram"]["1"])
    if len(records) != expected:
        raise AssertionError("one-support profile does not match the reroute summary")
    exponent_histogram = Counter(int(row["new_prime_exponent"]) for row in records)
    first_power_histogram = Counter(
        "available" if row["first_power_one_witness"] is not None else "absent"
        for row in records
    )
    gap_histogram = Counter(int(row["tail_gap"]) for row in records)
    route_histogram = Counter(str(row["route"]) for row in records)
    return {
        "arithmetic": (
            "complete factorization of every final one-support divisor, exact "
            "square-root-completion reconstruction of its Type II certificate and "
            "ordinary two-tail source, and verification that the unique nonbase prime "
            "divides u=(p+m)/(m+1)"
        ),
        "scope_note": (
            "A finite profile of the rewritten portion of the 2097152-layer H19-k23 "
            "artifact. It does not prove that one-prime-power witnesses cover all "
            "parameters or all core primes."
        ),
        "input_parameter_limit_exclusive": global_payload["input_parameter_limit_exclusive"],
        "input_global_rewrite_count": len(global_payload["replacements"]),
        "final_one_support_count": len(records),
        "route_histogram": dict(sorted(route_histogram.items())),
        "new_prime_exponent_histogram": {
            str(exponent): count
            for exponent, count in sorted(exponent_histogram.items())
        },
        "first_power_one_witness_histogram": dict(sorted(first_power_histogram.items())),
        "tail_gap_histogram": {
            str(gap): count for gap, count in sorted(gap_histogram.items())
        },
        "distinct_new_prime_count": len({int(row["new_prime"]) for row in records}),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-input", type=Path, default=DEFAULT_GLOBAL_INPUT)
    parser.add_argument("--reroute-input", type=Path, default=DEFAULT_REROUTE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    global_payload = json.loads(args.global_input.read_text(encoding="utf-8"))
    reroute_payload = json.loads(args.reroute_input.read_text(encoding="utf-8"))
    result = run_audit(global_payload, reroute_payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
