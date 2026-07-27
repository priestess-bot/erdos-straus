#!/usr/bin/env python3
"""Reconstruct the final one-million short-source edges through the B=1 residue selector."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERAL = ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-1m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-shifted-source-b1-selector-1m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("shifted_source_b1_selector", SELECTOR)


def run_audit(general_path: Path = GENERAL) -> dict[str, object]:
    """Check that every final short-source edge is exactly a shifted B=1 divisor-residue witness."""
    general = json.loads(general_path.read_text(encoding="utf-8"))
    records = []
    for record in general["records"]:
        prime = int(record["prime"])
        edge = record["minimum_source_distance"]
        A, B, C = (int(value) for value in edge["normal_form"])
        shift = int(edge["source_distance"])
        R = int(edge["R"])
        if B != 1:
            raise AssertionError("final short-source witness was not B=1")
        witness = selector.shifted_source_b1_witness(prime, shift, R, C)
        if witness is None:
            raise AssertionError("shifted B=1 selector did not recover final residual")
        expected = {
            "gap": int(edge["gap"]),
            "normal_form": [A, B, C],
            "source_denominator": int(edge["source_denominator"]),
            "source_term": int(edge["source_term"]),
            "E": int(edge["E"]),
        }
        actual = {key: witness[key] for key in expected}
        if actual != expected:
            raise AssertionError("shifted B=1 selector reconstructed a different edge")
        records.append(witness)
    return {
        "arithmetic": (
            "for each final general-source residual, set s=p-n and R=(E-1)/s; check the source-square "
            "condition, C|K=(pR+1)/4, and 4C=-1 (mod R), then reconstruct the B=1 target and source "
            "unit-fraction identities and the generic maximum-tail lift"
        ),
        "scope_note": (
            "A finite reconstruction of the three stored short-source edges. It does not claim that fixed "
            "shifts or a fixed R work for all core primes."
        ),
        "prime_limit": general["prime_limit"],
        "record_count": len(records),
        "shift_histogram": {
            str(shift): sum(record["shift"] == shift for record in records)
            for shift in sorted({record["shift"] for record in records})
        },
        "R_histogram": {
            str(R): sum(record["R"] == R for record in records)
            for R in sorted({record["R"] for record in records})
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--general", type=Path, default=GENERAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.general)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
