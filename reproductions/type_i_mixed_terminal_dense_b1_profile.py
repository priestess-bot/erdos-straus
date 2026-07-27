#!/usr/bin/env python3
"""Minimize the Type I normal-form B coordinate on the dense 500M--600M tail misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
PROFILE_SCRIPT = ROOT / "reproductions" / "type_i_tail_reverse_small_b_profile.py"
DEFAULT_GAP_CAP = 215
DEFAULT_B_CAP = 1
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_b = load_module("mixed_terminal_dense_b1_small_b", PROFILE_SCRIPT)


def tail_payload(dense_payload: dict[str, object]) -> dict[str, object]:
    """Expose exactly the dense ordinary-tail misses in the generic profile format."""
    records = dense_payload["type_i_even_terminal_bridge_records"]
    if not isinstance(records, list):
        raise TypeError("dense terminal records must be a list")
    primes = [int(record["prime"]) for record in records]
    if len(set(primes)) != len(primes):
        raise AssertionError("dense terminal records contain a duplicate prime")
    if int(dense_payload["ordinary_type_ii_tail_miss_count"]) != len(primes):
        raise AssertionError("dense terminal records do not equal the ordinary-tail misses")
    return {"prime_limit": int(dense_payload["prime_interval"][1]), "misses": [{"prime": prime} for prime in primes]}


def run_audit(
    dense_payload: dict[str, object],
    gap_cap: int = DEFAULT_GAP_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Rebuild the complete even-source B-bounded profile for the dense residuals."""
    profile = small_b.run_profile(tail_payload(dense_payload), gap_cap, b_cap, True)
    original_primes = {
        int(record["prime"])
        for record in dense_payload["type_i_even_terminal_bridge_records"]
    }
    selected_primes = {int(record["prime"]) for record in profile["records"]}
    if selected_primes & set(profile["misses"]):
        raise AssertionError("selected and missed B-bounded branches overlap")
    if selected_primes | set(profile["misses"]) != original_primes:
        raise AssertionError("B-bounded profile does not partition dense ordinary-tail misses")
    return {
        **profile,
        "arithmetic": (
            "extract every ordinary Type II tail miss from the dense 500M--600M audit, "
            "then exhaust every Type I normal certificate through the stated gap cap with "
            "B<=b_cap and every maximum-tail bridge; retain only even terminal sources"
        ),
        "scope_note": (
            "A dense finite B-bounded profile. Its closure does not extend B=1 to the "
            "earlier 500M range, where exact B=1 counterexamples are already known."
        ),
        "prime_interval": dense_payload["prime_interval"],
        "input_dense_terminal_artifact": INPUT.name,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.gap_cap, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
