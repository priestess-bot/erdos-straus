#!/usr/bin/env python3
"""Re-select upper-half B=1 source states on the dense 500M--600M residual.

The input gives one B=1 Type I terminal bridge for each ordinary Type II tail
miss, but that initially selected source can lie below p/2.  For precisely
those records, exhaust the same m<=215 Type I box and retain all even,
upper-half strict maximum-tail reverse lifts before applying the exact B=1
source-state divisor-residue test.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
RESELECTION = ROOT / "reproductions" / "type_i_pminusone_miss_upper_b3_reselection_profile.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-upper-b1-reselection-profile-600m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


reselection = load_module("dense_upper_b1_reselection", RESELECTION)


def stored_bridge_factor(record: dict[str, object]) -> tuple[int, int, int]:
    """Recover p, n and E from one stored B=1 reverse-tail bridge."""
    prime = int(record["prime"])
    normal_form = record["normal_form"]
    lift = record["reverse_two_tail_lift"]
    if not isinstance(normal_form, list) or int(normal_form[1]) != 1:
        raise AssertionError("input record is not a B=1 normal form")
    if not isinstance(lift, dict):
        raise AssertionError("input record has no reverse lift")
    divisor = int(lift["bridge_divisor"])
    if divisor % (prime * prime):
        raise AssertionError("stored divisor did not reconstruct a bridge factor")
    return prime, int(lift["source_denominator"]), divisor // (prime * prime)


def choose_upper_b_one(
    prime: int, states: list[dict[str, object]]
) -> dict[str, object] | None:
    """Choose a deterministic B=1 realization among all enumerated upper states."""
    candidates: list[dict[str, object]] = []
    for state in states:
        witness = reselection.B_one_realization(
            prime, int(state["source_denominator"]), int(state["E"])
        )
        if witness is not None:
            candidates.append({**state, "B_one_realization": witness})
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda candidate: (
            int(candidate["B_one_realization"]["m"]),
            int(candidate["source_distance"]),
            int(candidate["E"]),
            int(candidate["origin_gap"]),
        ),
    )


def run_profile(profile: dict[str, object]) -> dict[str, object]:
    """Release lower-half stored B=1 witnesses through upper source re-selection."""
    records = profile["records"]
    gap_cap = int(profile["gap_cap"])
    if not isinstance(records, list) or len(records) != 247:
        raise AssertionError("input must contain the exact 247-point dense residual")
    if int(profile["b_cap"]) != 1 or int(profile["captured_count"]) != len(records):
        raise AssertionError("input must be a complete B=1 dense profile")

    direct: list[int] = []
    direct_gaps: list[int] = []
    lower: list[int] = []
    reselected: list[dict[str, object]] = []
    misses: list[dict[str, object]] = []
    forms_checked = 0
    lifts_checked = 0
    seen: set[int] = set()

    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("input contains a non-object record")
        prime, source, bridge_factor = stored_bridge_factor(record)
        if prime in seen:
            raise AssertionError("input contains a duplicate prime")
        seen.add(prime)
        if 2 * source >= prime + 1:
            witness = reselection.B_one_realization(prime, source, bridge_factor)
            if witness is None:
                raise AssertionError("stored upper-half B=1 witness did not reconstruct")
            direct.append(prime)
            direct_gaps.append(int(record["gap"]))
            continue

        lower.append(prime)
        states, local_forms, local_lifts = reselection.upper_source_states(prime, gap_cap)
        forms_checked += local_forms
        lifts_checked += local_lifts
        selected = choose_upper_b_one(prime, states)
        if selected is not None:
            reselected.append(
                {
                    "prime": prime,
                    "upper_source_state_count": len(states),
                    "selected_upper_B_one_state": selected,
                }
            )
            continue
        fallback = reselection.least_upper_realization(prime, states)
        misses.append(
            {
                "prime": prime,
                "upper_source_state_count": len(states),
                "least_upper_realization": fallback,
            }
        )

    if len(direct) + len(lower) != len(records):
        raise AssertionError("stored source-half classification did not partition the input")
    if len(reselected) + len(misses) != len(lower):
        raise AssertionError("upper source re-selection did not partition the lower records")
    reselected_B_one_realization_gaps = [
        int(row["selected_upper_B_one_state"]["B_one_realization"]["m"])
        for row in reselected
    ]
    return {
        "arithmetic": (
            "verify every stored B=1 terminal bridge; for each stored lower-half source, exhaust every "
            "Type I normal form and strict maximum-tail lift through the same gap cap, retain every even "
            "upper-half source state, and test it with the exact B=1 source-state divisor-residue criterion"
        ),
        "scope_note": (
            "A complete finite source-state re-selection profile for the 247 ordinary-tail misses generated "
            "from the shared 500M--600M, m<=215 Type I box. The selected B=1 realization is minimized first "
            "by its normal-form gap, yielding the stated finite m<=131 closure; it supplies neither a global "
            "B=1 bound nor a universal source-selection rule."
        ),
        "input_artifact": INPUT.name,
        "prime_interval": profile["prime_interval"],
        "gap_cap": gap_cap,
        "ordinary_tail_miss_count": len(records),
        "stored_upper_B_eq_1_count": len(direct),
        "stored_lower_B_eq_1_count": len(lower),
        "reselected_upper_B_eq_1_count": len(reselected),
        "upper_B_eq_1_miss_count": len(misses),
        "upper_B_eq_1_closure_count": len(direct) + len(reselected),
        "maximum_direct_upper_B_eq_1_gap": max(direct_gaps, default=None),
        "reselected_upper_B_eq_1_realization_gap_exceeding_source_box_count": sum(
            gap > gap_cap for gap in reselected_B_one_realization_gaps
        ),
        "maximum_reselected_upper_B_eq_1_realization_gap": max(
            reselected_B_one_realization_gaps, default=None
        ),
        "maximum_selected_upper_B_eq_1_normal_gap": max(
            [*direct_gaps, *reselected_B_one_realization_gaps], default=None
        ),
        "reselection_normal_forms_exhaustively_checked": forms_checked,
        "reselection_strict_reverse_lifts_exhaustively_checked": lifts_checked,
        "direct_upper_B_eq_1_primes": direct,
        "stored_lower_B_eq_1_primes": lower,
        "reselected_upper_B_eq_1_records": reselected,
        "upper_B_eq_1_misses": misses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"direct_upper_B_eq_1_primes", "stored_lower_B_eq_1_primes", "reselected_upper_B_eq_1_records", "upper_B_eq_1_misses"}
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
