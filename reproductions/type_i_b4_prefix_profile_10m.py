#!/usr/bin/env python3
"""Reproduce the complete B<=4 maximum-tail even-source prefix profile through 10M."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "reproductions" / "type_i_b4_prefix_boundary_21169.py"
DEFAULT_LIMIT = 10_000_009
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b4-prefix-profile-10m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


prefix = load_module("b4_prefix_profile_10m_prefix", PREFIX)


def run_profile(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Run the exact B<=4 natural-gap audit and retain its compact summary."""
    result = prefix.run_audit(limit, 4)
    return {
        "arithmetic": result["arithmetic"],
        "scope_note": (
            "Complete finite prefix profile for the stated Type I family. It does not turn the fixed B<=4 "
            "family into a global selector and does not test other reverse coordinates or Type II."
        ),
        "prime_limit": result["prime_limit"],
        "b_cap": result["b_cap"],
        "core_prime_count": result["core_prime_count"],
        "captured_count": result["captured_count"],
        "misses": result["misses"],
        "first_miss": result["first_miss"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
