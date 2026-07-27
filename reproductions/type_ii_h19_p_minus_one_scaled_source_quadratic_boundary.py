#!/usr/bin/env python3
"""Test p-minus-one scaled sources on the four H19 quadratic-descent misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUADRATIC_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-p-minus-one-scaled-source-quadratic-boundary-1b-results.json"


def load_script():
    spec = importlib.util.spec_from_file_location(
        "p_minus_one_scaled_source_quadratic_boundary", P_MINUS_ONE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {P_MINUS_ONE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p_minus_one = load_script()


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Test exactly the stored four misses, without weakening their definition."""
    misses = [int(prime) for prime in payload["quadratic_factor_descent_misses"]]
    result = p_minus_one.audit_primes(misses, include_standard=True)
    return {
        "arithmetic": (
            "complete b=1,2,4 scaled-source candidate enumeration at n=p-1, "
            "forced-multiple square-tail enumeration, and exact rational plus "
            "Type I certificate verification"
        ),
        "scope_note": (
            "A finite full p-minus-one boundary test on the four stored H19 "
            "quadratic-descent misses. It does not exclude other sources or descents."
        ),
        "prime_limit": payload["prime_limit"],
        "quadratic_descent_miss_count": len(misses),
        **result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=QUADRATIC_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
