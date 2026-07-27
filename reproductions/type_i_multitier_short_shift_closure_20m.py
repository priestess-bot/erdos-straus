#!/usr/bin/env python3
"""Compose the twenty-million Type I p-1 and short-shift finite selector tiers."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DYADIC = ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-20m-results.json"
MENU = ROOT / "reproductions" / "type-i-pminusone-b12-menu-profile-20m-results.json"
LOW_E = ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-20m-results.json"
SHIFTED_MENU = ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-20m-results.json"
SHORT_SHIFT = ROOT / "reproductions" / "type-i-short-shift-low-e-b7-profile-20m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-multitier-short-shift-closure-20m-results.json"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def record_map(payload: dict[str, object]) -> dict[int, dict[str, object]]:
    return {int(record["prime"]): record for record in payload["records"]}


def run_profile(
    dyadic_path: Path = DYADIC,
    menu_path: Path = MENU,
    low_e_path: Path = LOW_E,
    shifted_menu_path: Path = SHIFTED_MENU,
    short_shift_path: Path = SHORT_SHIFT,
) -> dict[str, object]:
    """Apply five disjoint finite selector stages to every stored twenty-million core prime."""
    dyadic = load_json(dyadic_path)
    menu = load_json(menu_path)
    low_e = load_json(low_e_path)
    shifted_menu = load_json(shifted_menu_path)
    short_shift = load_json(short_shift_path)
    payloads = (dyadic, menu, low_e, shifted_menu, short_shift)
    limits = {int(payload["prime_limit"]) for payload in payloads}
    if limits != {20_000_017}:
        raise AssertionError("input profiles do not share the stated twenty-million prefix")

    dyadic_records = record_map(dyadic)
    menu_records = record_map(menu)
    low_e_records = record_map(low_e)
    shifted_menu_records = record_map(shifted_menu)
    short_shift_records = record_map(short_shift)
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
            witness = low_e_record["witness"]
            selections.append(
                {
                    "prime": prime,
                    "stage": "square-allowed-low-E-p-minus-one",
                    "E": int(witness["E"]),
                    "B": int(witness["B"]),
                    "source_distance": 1,
                }
            )
            continue
        shifted_record = shifted_menu_records.get(prime)
        if shifted_record is not None and shifted_record["witness"] is not None:
            witness = shifted_record["witness"]
            selections.append(
                {
                    "prime": prime,
                    "stage": "fixed-shifted-source-b1",
                    "E": int(witness["E"]),
                    "B": 1,
                    "source_distance": int(witness["shift"]),
                }
            )
            continue
        short_shift_record = short_shift_records.get(prime)
        if short_shift_record is None or short_shift_record["witness"] is None:
            raise AssertionError(f"short-shift stage did not capture {prime}")
        witness = short_shift_record["witness"]
        selections.append(
            {
                "prime": prime,
                "stage": "dynamic-short-shift",
                "E": int(witness["E"]),
                "B": int(witness["B"]),
                "source_distance": int(witness["shift"]),
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
            "apply in order the complete dyadic p-1 selector, the fixed non-dyadic B=1,2 p-1 menu, "
            "the square-allowed E<=10^6 full-factor-pair p-1 refinement, the fixed shifted B=1 menu, "
            "and the four-shift dynamic-E selector with B<=7"
        ),
        "scope_note": (
            "A composed finite closure of a stated prefix. Its observed bounds are not universal theorems and "
            "do not prove the Erdos-Straus conjecture."
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
    parser.add_argument("--shifted-menu", type=Path, default=SHIFTED_MENU)
    parser.add_argument("--short-shift", type=Path, default=SHORT_SHIFT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.dyadic, args.menu, args.low_e, args.shifted_menu, args.short_shift)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
