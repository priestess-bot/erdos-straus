#!/usr/bin/env python3
"""Certify non-core prime terminal factors of the bounded-B reverse sources."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-tail-reverse-small-b5-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-small-b-source-terminal-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("small_b_source_terminal_landscape", LANDSCAPE)


def terminal_factor(source: int) -> tuple[dict[int, int], int]:
    """Return the factorization and its least prime outside 1 modulo 24."""
    factors = landscape.factor_by_trial_division(source)
    for prime in factors:
        if prime % 24 != 1:
            return factors, prime
    raise AssertionError("source has no non-core prime factor")


def run_profile(profile: dict[str, object]) -> dict[str, object]:
    records: list[dict[str, object]] = []
    residue_counts: dict[str, int] = {}
    maximum_terminal_factor = 0
    for record in profile["records"]:
        prime = int(record["prime"])
        source = int(record["reverse_two_tail_lift"]["source_denominator"])
        factors, terminal_prime = terminal_factor(source)
        multiplier = source // terminal_prime
        if terminal_prime * multiplier != source:
            raise AssertionError("terminal scaling factor did not reconstruct source")
        if terminal_prime % 24 == 1:
            raise AssertionError("terminal prime remained in the core class")
        residue = str(terminal_prime % 24)
        residue_counts[residue] = residue_counts.get(residue, 0) + 1
        maximum_terminal_factor = max(maximum_terminal_factor, terminal_prime)
        records.append(
            {
                "prime": prime,
                "source_denominator": source,
                "source_factorization": {str(q): exponent for q, exponent in factors.items()},
                "terminal_prime": terminal_prime,
                "terminal_prime_mod_24": terminal_prime % 24,
                "scaling_multiplier": multiplier,
            }
        )
    if len(records) != int(profile["captured_count"]):
        raise AssertionError("terminal profile did not cover every selected reverse source")
    return {
        "arithmetic": (
            "factor every source denominator selected by the fixed m<=127, B<=5 "
            "Type I reverse-two-tail profile; choose its least prime factor q not "
            "congruent to 1 modulo 24 and record source=q*multiplier"
        ),
        "scope_note": (
            "Finite terminal-factor audit of the already selected 500M bounded-B "
            "reverse edges. It neither extends the prime limit nor proves a uniform selector."
        ),
        "input_prime_limit": profile["input_prime_limit"],
        "reverse_edge_count": len(records),
        "unresolved_core_source_count": 0,
        "terminal_prime_residue_counts_mod_24": dict(
            sorted(residue_counts.items(), key=lambda item: int(item[0]))
        ),
        "maximum_selected_terminal_prime": maximum_terminal_factor,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.profile.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
