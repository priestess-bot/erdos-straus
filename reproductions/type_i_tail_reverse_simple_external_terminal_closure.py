#!/usr/bin/env python3
"""Certify the low-complexity reverse/external terminal closure of 500M tail misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-terminal-min-500m-results.json"
HYBRID = ROOT / "reproductions" / "type-i-tail-reverse-surplus-external-hybrid-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-simple-external-terminal-closure-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("simple_external_terminal_landscape", LANDSCAPE)


def terminal_record(prime: int, source: int, branch: str) -> dict[str, object]:
    factors = landscape.factor_by_trial_division(source)
    terminal_prime = next((q for q in factors if q % 24 != 1), None)
    if terminal_prime is None:
        raise AssertionError("selected strict source has only core prime factors")
    multiplier = source // terminal_prime
    if terminal_prime * multiplier != source:
        raise AssertionError("terminal scaling factor did not reconstruct source")
    return {
        "prime": prime,
        "branch": branch,
        "source_denominator": source,
        "source_factorization": {str(q): exponent for q, exponent in factors.items()},
        "terminal_prime": terminal_prime,
        "terminal_prime_mod_24": terminal_prime % 24,
        "scaling_multiplier": multiplier,
    }


def run_audit(profile: dict[str, object], hybrid: dict[str, object]) -> dict[str, object]:
    simple_records = list(profile["records"])
    external_records = list(hybrid["records"])
    simple_primes = {int(record["prime"]) for record in simple_records}
    residuals = {int(prime) for prime in profile["misses"]}
    external_primes = {int(record["prime"]) for record in external_records}
    if simple_primes & external_primes:
        raise AssertionError("simple reverse and external branches overlap")
    if external_primes != residuals:
        raise AssertionError("external hybrid did not close exactly the simple reverse residual set")
    if len(simple_primes) + len(external_primes) != int(profile["ordinary_tail_miss_count"]):
        raise AssertionError("branches did not partition the ordinary-tail misses")
    records: list[dict[str, object]] = []
    for record in simple_records:
        records.append(
            terminal_record(
                int(record["prime"]),
                int(record["selected_edge"]["reverse_two_tail_lift"]["source_denominator"]),
                "linear_or_one_prime_reverse",
            )
        )
    for record in external_records:
        records.append(
            terminal_record(
                int(record["prime"]),
                int(record["external_descent"]["source_denominator"]),
                str(record["branch"]),
            )
        )
    branch_counts: dict[str, int] = {}
    terminal_residue_counts: dict[str, int] = {}
    maximum_terminal_factor = 0
    for record in records:
        branch = str(record["branch"])
        branch_counts[branch] = branch_counts.get(branch, 0) + 1
        residue = str(record["terminal_prime_mod_24"])
        terminal_residue_counts[residue] = terminal_residue_counts.get(residue, 0) + 1
        maximum_terminal_factor = max(maximum_terminal_factor, int(record["terminal_prime"]))
    return {
        "arithmetic": (
            "partition the stored 500M ordinary-tail misses into the terminal-minimized "
            "at-most-one-prime reverse-surplus profile and its independently rebuilt quadratic-external residual "
            "closure; factor every selected strict source and choose its least prime factor "
            "outside 1 modulo 24"
        ),
        "scope_note": (
            "A finite terminal closure with target-side selectors. It is not a globally "
            "iterable source-side descent theorem."
        ),
        "prime_limit": profile["prime_limit"],
        "ordinary_tail_miss_count": profile["ordinary_tail_miss_count"],
        "branch_counts": dict(sorted(branch_counts.items())),
        "unclosed_primes": [],
        "unresolved_core_source_count": 0,
        "terminal_prime_residue_counts_mod_24": dict(
            sorted(terminal_residue_counts.items(), key=lambda item: int(item[0]))
        ),
        "maximum_selected_terminal_prime": maximum_terminal_factor,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--hybrid", type=Path, default=HYBRID)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.profile.read_text(encoding="utf-8")),
        json.loads(args.hybrid.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
