#!/usr/bin/env python3
"""Test whether the least nonbase factor can realize final global first-power tails."""

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
DEFAULT_PROFILE_INPUT = ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
DEFAULT_REROUTE_INPUT = ROOT / "reproductions" / "h19-k23-global-first-power-tail-reroute-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-min-nonbase-factor-boundary-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_min_factor_global", GLOBAL_CLOSURE)


def least_nonbase_prime_witness(
    prime: int, gap: int, base_primes: set[int]
) -> tuple[int, int | None]:
    """Test every base divisor against the least nonbase prime factor of x."""
    q = (gap + 1) // 4
    u = (prime + gap) // (gap + 1)
    x = q * u
    factors = {
        int(factor): 2 * int(exponent)
        for factor, exponent in sympy.factorint(x).items()
    }
    nonbase = sorted(factor for factor in factors if factor not in base_primes)
    if not nonbase:
        raise AssertionError("one-support row lacks a nonbase prime")
    least_prime = nonbase[0]
    base_values = [1]
    for factor, exponent in sorted(factors.items()):
        if factor in base_primes:
            base_values = [
                value * factor**power
                for value in base_values
                for power in range(exponent + 1)
            ]
    candidates = [
        value * least_prime
        for value in base_values
        if value * least_prime <= x
        and (value * least_prime) % gap == (-x) % gap
    ]
    return least_prime, min(candidates) if candidates else None


def run_audit(
    profile_payload: dict[str, object], reroute_payload: dict[str, object]
) -> dict[str, object]:
    """Profile the deterministic least-factor rule on every final first-power tail."""
    _, bases = global_closure.global_tail_bases()
    reroutes = {int(row["prime"]): row for row in reroute_payload["reroutes"]}
    by_tail: Counter[tuple[int, str]] = Counter()
    failures = []
    for row in profile_payload["records"]:
        prime = int(row["prime"])
        if prime in reroutes:
            chosen = reroutes[prime]
            gap = int(chosen["new_tail_gap"])
            base_primes = bases[gap]
        else:
            gap = int(row["tail_gap"])
            base_primes = {int(factor) for factor in row["base_primes"]}
        least_prime, witness = least_nonbase_prime_witness(
            prime, gap, base_primes
        )
        status = "works" if witness is not None else "fails"
        by_tail[(gap, status)] += 1
        if witness is None:
            failures.append(
                {
                    "prime": prime,
                    "tail_gap": gap,
                    "least_nonbase_prime": least_prime,
                }
            )
    total = int(profile_payload["final_one_support_count"])
    if sum(by_tail.values()) != total:
        raise AssertionError("least-factor audit did not cover the first-power profile")
    return {
        "arithmetic": (
            "for every final first-power tail, complete factorization of x and "
            "exhaustive enumeration of all canonical-base divisors multiplied by "
            "the least nonbase prime factor"
        ),
        "scope_note": (
            "A finite boundary for the least-nonbase-prime selection rule on the "
            "rewritten 2097152-layer H19-k23 profile. It does not exclude selection "
            "by a different nonbase factor or a different tail."
        ),
        "input_final_one_support_count": total,
        "least_nonbase_prime_works_count": by_tail_total(by_tail, "works"),
        "least_nonbase_prime_fails_count": by_tail_total(by_tail, "fails"),
        "tail_histogram": {
            str(gap): {
                status: by_tail[(gap, status)]
                for status in ("works", "fails")
                if by_tail[(gap, status)]
            }
            for gap in sorted({gap for gap, _ in by_tail})
        },
        "failures": failures,
    }


def by_tail_total(histogram: Counter[tuple[int, str]], status: str) -> int:
    return sum(count for (_, row_status), count in histogram.items() if row_status == status)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-input", type=Path, default=DEFAULT_PROFILE_INPUT)
    parser.add_argument("--reroute-input", type=Path, default=DEFAULT_REROUTE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    profile_payload = json.loads(args.profile_input.read_text(encoding="utf-8"))
    reroute_payload = json.loads(args.reroute_input.read_text(encoding="utf-8"))
    result = run_audit(profile_payload, reroute_payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "failures"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
