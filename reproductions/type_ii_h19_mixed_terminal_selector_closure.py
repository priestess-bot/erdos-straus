#!/usr/bin/env python3
"""Close H19 residuals by a Type II tail certificate or an even Type I bridge."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE_SCRIPT = ROOT / "reproductions" / "type_i_even_external_source_normal_bridge.py"
DEFAULT_TAIL = ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
DEFAULT_EXTERNAL = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-mixed-terminal-selector-closure-1b-results.json"


def load_bridge_module():
    spec = importlib.util.spec_from_file_location(
        "h19_mixed_terminal_bridge", BRIDGE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_i_even_external_source_normal_bridge.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bridge_audit = load_bridge_module()


def terminal_record(prime: int, witness: dict[str, object]) -> dict[str, object]:
    """Normalize and retain the finite data needed for one terminal bridge."""
    bridge = bridge_audit.bridge_from_quadratic_external_witness(prime, witness)
    if not all(bridge["conditions"].values()):
        raise AssertionError("fallback external witness is not an even terminal bridge")
    return {
        key: bridge[key]
        for key in (
            "prime",
            "source_denominator",
            "k",
            "R",
            "K",
            "external_factor",
            "gap",
            "normal_form",
            "E",
            "source_first_denominator",
            "conditions",
        )
    }


def run_audit(
    tail_payload: dict[str, object], external_payload: dict[str, object]
) -> dict[str, object]:
    """Replace exactly the ordinary-tail misses with Type I terminal bridges."""
    tail_records = tail_payload["tail_records"]
    tail_misses = [int(prime) for prime in tail_payload["tail_deflation_missing_primes"]]
    if len(tail_records) + len(tail_misses) != int(tail_payload["h19_residual_count"]):
        raise AssertionError("tail profile does not partition the H19 residuals")
    tail_primes = {int(record["prime"]) for record in tail_records}
    external_records = {
        int(record["prime"]): record for record in external_payload["records"]
    }

    terminal_fallbacks = []
    for prime in tail_misses:
        record = external_records.get(prime)
        if record is None:
            raise AssertionError("ordinary-tail miss is absent from external profile")
        witness = record["quadratic_factor_external_source_descent"]
        if witness is None:
            raise AssertionError("ordinary-tail miss has no quadratic external witness")
        if not isinstance(witness, dict):
            raise TypeError("quadratic external witness must be an object")
        terminal_fallbacks.append(terminal_record(prime, witness))

    terminal_primes = {int(record["prime"]) for record in terminal_fallbacks}
    if tail_primes & terminal_primes:
        raise AssertionError("ordinary-tail and terminal branches overlap")
    if len(tail_primes | terminal_primes) != int(tail_payload["h19_residual_count"]):
        raise AssertionError("mixed terminal branches do not close the H19 residuals")

    return {
        "arithmetic": (
            "stored exact Type II two-tail certificates for the ordinary branch, "
            "plus fresh Type I normal-form reconstruction for each tail miss"
        ),
        "scope_note": (
            "A finite H19 instance of the mixed terminal selector dichotomy. "
            "It does not prove a global choice of either branch."
        ),
        "prime_limit": tail_payload["prime_limit"],
        "base_shift_bound": tail_payload["base_shift_bound"],
        "h19_residual_count": int(tail_payload["h19_residual_count"]),
        "ordinary_type_ii_tail_certificate_count": len(tail_primes),
        "type_i_even_terminal_bridge_count": len(terminal_fallbacks),
        "unclosed_primes": [],
        "type_i_even_terminal_bridge_records": terminal_fallbacks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-profile", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--external-profile", type=Path, default=DEFAULT_EXTERNAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.tail_profile.read_text(encoding="utf-8")),
        json.loads(args.external_profile.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
