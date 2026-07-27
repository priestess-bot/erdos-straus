#!/usr/bin/env python3
"""Compose the one-million Type I p-1 and short-source finite selector tiers."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DYADIC = ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-1m-results.json"
MENU = ROOT / "reproductions" / "type-i-pminusone-b12-menu-profile-1m-results.json"
LOW_E = ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-1m-results.json"
GENERAL = ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-1m-results.json"
GENERAL_CODE = ROOT / "reproductions" / "type_i_dyadic_residual_general_edge_profile_100k.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-multitier-short-source-closure-1m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


general = load_module("multitier_general_verifier", GENERAL_CODE)


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def record_map(payload: dict[str, object]) -> dict[int, dict[str, object]]:
    return {int(record["prime"]): record for record in payload["records"]}


def run_profile(
    dyadic_path: Path = DYADIC,
    menu_path: Path = MENU,
    low_e_path: Path = LOW_E,
    general_path: Path = GENERAL,
) -> dict[str, object]:
    """Apply four disjoint finite selector stages to each stored core prime."""
    dyadic = load_json(dyadic_path)
    menu = load_json(menu_path)
    low_e = load_json(low_e_path)
    final_general = load_json(general_path)
    limits = {int(payload["prime_limit"]) for payload in (dyadic, menu, low_e, final_general)}
    if limits != {1_000_009}:
        raise AssertionError("input profiles do not share the stated one-million prefix")

    dyadic_records = record_map(dyadic)
    menu_records = record_map(menu)
    low_e_records = record_map(low_e)
    general_records = record_map(final_general)
    selections = []
    for prime in sorted(dyadic_records):
        dyadic_witness = dyadic_records[prime]["witness"]
        if dyadic_witness is not None:
            selections.append(
                {
                    "prime": prime,
                    "stage": "dyadic-p-minus-one",
                    "E": 1 << int(dyadic_witness["exponent"]),
                    "B": int(dyadic_witness["B"]),
                    "source_distance": 1,
                }
            )
            continue
        menu_witness = menu_records[prime]["witness"]
        if menu_witness is not None:
            selections.append(
                {
                    "prime": prime,
                    "stage": "fixed-menu-p-minus-one",
                    "E": int(menu_witness["E"]),
                    "B": int(menu_witness["B"]),
                    "source_distance": 1,
                }
            )
            continue
        low_e_record = low_e_records.get(prime)
        if low_e_record is not None and low_e_record["witness"] is not None:
            low_e_witness = low_e_record["witness"]
            selections.append(
                {
                    "prime": prime,
                    "stage": "square-allowed-low-E-p-minus-one",
                    "E": int(low_e_witness["E"]),
                    "B": int(low_e_witness["B"]),
                    "source_distance": 1,
                }
            )
            continue
        general_record = general_records.get(prime)
        if general_record is None:
            raise AssertionError(f"no selector tier captured {prime}")
        witness = general_record["minimum_source_distance"]
        general.verify_witness(prime, witness)
        selections.append(
            {
                "prime": prime,
                "stage": "short-general-source",
                "E": int(witness["E"]),
                "B": int(witness["normal_form"][1]),
                "source_distance": int(witness["source_distance"]),
            }
        )

    expected_count = int(dyadic["core_prime_count"])
    if len(selections) != expected_count or len({entry["prime"] for entry in selections}) != expected_count:
        raise AssertionError("selector tiers did not form a disjoint closure")
    stage_histogram = Counter(entry["stage"] for entry in selections)
    max_E = max(selections, key=lambda entry: (entry["E"], entry["prime"]))
    max_B = max(selections, key=lambda entry: (entry["B"], entry["prime"]))
    max_distance = max(selections, key=lambda entry: (entry["source_distance"], entry["prime"]))
    return {
        "arithmetic": (
            "apply in order the stored complete dyadic p-1 selector, the fixed non-dyadic B=1,2 p-1 menu, "
            "the square-allowed E<=10^6 full-factor-pair p-1 refinement, and exact low-B general-source "
            "certificates for the final three residuals"
        ),
        "scope_note": (
            "A composed finite closure of a stated prefix. The observed bounds are not uniform theorems beyond "
            "this prefix and do not prove the Erdos-Straus conjecture."
        ),
        "prime_limit": int(dyadic["prime_limit"]),
        "core_prime_count": expected_count,
        "captured_count": len(selections),
        "stage_histogram": dict(sorted(stage_histogram.items())),
        "maximum_selected_E": max_E,
        "maximum_selected_B": max_B,
        "maximum_source_distance": max_distance,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dyadic", type=Path, default=DYADIC)
    parser.add_argument("--menu", type=Path, default=MENU)
    parser.add_argument("--low-e", type=Path, default=LOW_E)
    parser.add_argument("--general", type=Path, default=GENERAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.dyadic, args.menu, args.low_e, args.general)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
