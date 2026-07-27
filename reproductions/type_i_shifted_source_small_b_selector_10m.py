#!/usr/bin/env python3
"""Reconstruct the final ten-million short-source edges from fixed source states."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERAL = ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-10m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-shifted-source-small-b-selector-10m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("shifted_source_small_b_selector", SELECTOR)


def run_audit(general_path: Path = GENERAL) -> dict[str, object]:
    """Rebuild all final general-source witnesses through fixed (s,R,B,C) data."""
    general = json.loads(general_path.read_text(encoding="utf-8"))
    records = []
    for record in general["records"]:
        prime = int(record["prime"])
        edge = record["minimum_source_distance"]
        A, B, C = (int(value) for value in edge["normal_form"])
        shift = int(edge["source_distance"])
        R = int(edge["R"])
        witness = selector.shifted_source_witness(prime, shift, R, B, C)
        if witness is None:
            raise AssertionError("fixed shifted source state did not reconstruct final residual")
        expected = {
            "gap": int(edge["gap"]),
            "normal_form": [A, B, C],
            "source_denominator": int(edge["source_denominator"]),
            "source_term": int(edge["source_term"]),
            "E": int(edge["E"]),
        }
        actual = {key: witness[key] for key in expected}
        if actual != expected:
            raise AssertionError("fixed shifted source state reconstructed a different edge")
        records.append(witness)
    return {
        "arithmetic": (
            "for every final ten-million general-source residual, take s=p-n, R=(E-1)/s, and its normal "
            "B,C; check E|n^2/gcd(E,4), BC|K=(pR+1)/4, R|(4B^2C+1), and gcd((K/(BC)+B)/R,B)=1; "
            "then reconstruct both unit-fraction identities and the generic maximum-tail bridge"
        ),
        "scope_note": (
            "A finite reconstruction of seven stored short-source edges. It does not show that a fixed finite "
            "set of shifted source states captures all core primes."
        ),
        "prime_limit": general["prime_limit"],
        "record_count": len(records),
        "maximum_selected_shift": max(records, key=lambda record: (record["shift"], record["prime"])),
        "maximum_selected_B": max(records, key=lambda record: (record["normal_form"][1], record["prime"])),
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
