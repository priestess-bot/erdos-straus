#!/usr/bin/env python3
"""Audit p-minus-one strict descents on 10m Type II tail-deflation misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-10m-full-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-tail-deflation-p-minus-one-10m-results.json"
)
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p_minus_one = load_script("tail_deflation_p_minus_one_10m", P_MINUS_ONE_SCRIPT)


def run_audit(input_path: Path = DEFAULT_INPUT) -> dict[str, object]:
    """Completely test b=1,2,4 p-minus-one strict sources on stored misses."""
    input_payload = json.loads(input_path.read_text(encoding="utf-8"))
    tail_misses = [int(record["prime"]) for record in input_payload["misses"]]
    result = p_minus_one.audit_primes(tail_misses, include_standard=True)
    tail_hit_count = int(input_payload["tail_deflation_hit_count"])
    core_prime_count = int(input_payload["core_prime_count"])
    return {
        "arithmetic": (
            "complete b=1,2,4 p-minus-one scaled-source enumeration, forced "
            "multiple square-tail enumeration, and exact rational plus Type I "
            "certificate verification on every stored Type II tail-deflation miss"
        ),
        "scope_note": (
            "A finite boundary profile. The p-minus-one branch is a strict "
            "source descent here, but the remaining points show that the two "
            "branches are not a universal selector in this range."
        ),
        "input_artifact": input_path.name,
        "prime_limit": input_payload["prime_limit"],
        "core_prime_count": core_prime_count,
        "tail_deflation_strict_lift_count": tail_hit_count,
        "tail_deflation_residual_count": len(tail_misses),
        "p_minus_one_strict_lift_count": result["covered_prime_count"],
        "combined_strict_lift_count": tail_hit_count + result["covered_prime_count"],
        "combined_unclosed_count": len(result["uncovered_primes"]),
        **result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
