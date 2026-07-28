#!/usr/bin/env python3
"""Re-select B=1 self-square bridges on the frozen 600M ordinary-tail pressure set."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EARLY = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
DENSE = ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
SELF_SQUARE = ROOT / "reproductions" / "type_i_b1_self_square_terminal_bridge_profile_600m.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b1-self-square-reselection-profile-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("self_square_reselection_landscape", LANDSCAPE)
self_square = load_module("self_square_reselection_bridge", SELF_SQUARE)


def pressure_primes(early: dict[str, object], dense: dict[str, object]) -> list[int]:
    """Recover the exact 1,964 ordinary-tail misses used by the 600M pressure profile."""
    early_misses = early["misses"]
    dense_records = dense["type_i_even_terminal_bridge_records"]
    if not isinstance(early_misses, list) or not isinstance(dense_records, list):
        raise TypeError("pressure inputs do not contain prime lists")
    primes = [int(row["prime"]) for row in early_misses] + [int(row["prime"]) for row in dense_records]
    if len(early_misses) != 1717 or len(dense_records) != 247 or len(primes) != len(set(primes)):
        raise AssertionError("pressure-set partition did not reconstruct 1,964 distinct primes")
    return sorted(primes)


def self_square_candidates(prime: int, gap_cap: int) -> tuple[list[dict[str, int | bool]], int]:
    """Enumerate every upper-half B=1 self-square bridge in the stated target box."""
    candidates: list[dict[str, int | bool]] = []
    forms_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B != 1:
                continue
            forms_checked += 1
            if A % 2 == 0 or A < 2 * gap:
                continue
            R, remainder = divmod(4 * C + 1, gap)
            if remainder:
                raise AssertionError("stored B=1 normal form lost its R")
            H = A * R - 1
            K = C * H
            witness = self_square.self_square_witness(prime, A, C, H, R, K)
            if witness is None or not bool(witness["upper_half"]):
                raise AssertionError("A-parity/size criterion did not produce an upper self-square bridge")
            candidates.append(witness)
    return candidates, forms_checked


def choose_candidate(candidates: list[dict[str, int | bool]]) -> dict[str, int | bool]:
    """Use a stable target-first order without claiming it is a universal selector."""
    if not candidates:
        raise ValueError("cannot choose from an empty self-square candidate set")
    return min(
        candidates,
        key=lambda witness: (
            int(witness["m"]),
            int(witness["source_denominator"]),
            int(witness["E"]),
            int(witness["A"]),
            int(witness["C"]),
        ),
    )


def run_audit(
    early_path: Path = EARLY,
    dense_path: Path = DENSE,
    gap_cap: int = DEFAULT_GAP_CAP,
) -> dict[str, object]:
    """Exhaust the finite B=1 target box and retain one self-square witness per hit."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    primes = pressure_primes(
        json.loads(early_path.read_text(encoding="utf-8")),
        json.loads(dense_path.read_text(encoding="utf-8")),
    )
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms_checked = 0
    candidate_count = 0
    for prime in primes:
        candidates, local_forms = self_square_candidates(prime, gap_cap)
        forms_checked += local_forms
        candidate_count += len(candidates)
        if not candidates:
            misses.append(prime)
            continue
        records.append(
            {
                "prime": prime,
                "self_square_candidate_count": len(candidates),
                "selected_witness": choose_candidate(candidates),
            }
        )
    if len(records) + len(misses) != len(primes):
        raise AssertionError("self-square re-selection did not partition the pressure set")
    return {
        "arithmetic": (
            "on each frozen ordinary Type II tail miss, enumerate every Type I normal form with "
            "m<=gap_cap and B=1; retain exactly A odd and A>=2m, then set E=16C^2 and replay "
            "the resulting upper-half source identity"
        ),
        "scope_note": (
            "This is an exhaustive finite target-box re-selection profile. It does not bound the required "
            "gap for arbitrary core primes or assert a universal B=1 normal-form selector."
        ),
        "early_input": early_path.name,
        "dense_input": dense_path.name,
        "gap_cap": gap_cap,
        "ordinary_tail_pressure_count": len(primes),
        "self_square_reselection_covered_count": len(records),
        "self_square_reselection_miss_count": len(misses),
        "B_one_normal_forms_exhaustively_checked": forms_checked,
        "upper_self_square_candidate_count": candidate_count,
        "maximum_selected_gap": max((int(row["selected_witness"]["m"]) for row in records), default=None),
        "misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--early", type=Path, default=EARLY)
    parser.add_argument("--dense", type=Path, default=DENSE)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.early, args.dense, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key not in {"misses", "records"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
