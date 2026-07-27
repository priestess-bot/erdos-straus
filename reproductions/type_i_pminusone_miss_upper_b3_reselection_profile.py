#!/usr/bin/env python3
"""Re-select upper-half source states on the 500M p-minus-one residual.

For each of the 185 p-minus-one bridge misses, first test whether its stored
shortest upper-half source has a B=1 normal realization.  A B=1 miss is then
allowed to re-select every even upper-half source state produced by every Type
I normal form and strict maximum-tail lift in the same m<=215 box.  This
separates failure of a *state* from failure of the target prime.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
REALIZATION = ROOT / "reproductions" / "type_i_normal_source_state_realization.py"
OVERFLOW = ROOT / "reproductions" / "type_i_source_state_b1_overflow_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-b3-reselection-profile-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("pminusone_upper_b3_landscape", LANDSCAPE)
bridge = load_module("pminusone_upper_b3_bridge", BRIDGE)
realization = load_module("pminusone_upper_b3_realization", REALIZATION)
overflow = load_module("pminusone_upper_b3_overflow", OVERFLOW)


def B_one_realization(prime: int, source: int, bridge_factor: int) -> dict[str, int] | None:
    """Return the exact B=1 normal realization of a source state, if one exists."""
    distance = prime - source
    if source <= 0 or distance <= 0 or bridge_factor % 2 or (bridge_factor - 1) % distance:
        raise AssertionError("invalid source-state parameters")
    R = (bridge_factor - 1) // distance
    if R < 3 or R % 2 == 0 or (prime * R + 1) % 4:
        raise AssertionError("invalid source-state R")
    K = (prime * R + 1) // 4
    if (source * source // math.gcd(bridge_factor, 4)) % bridge_factor:
        raise AssertionError("source state failed the normalized square condition")
    if bridge_factor > 4 * K - 2 * R or 2 * source < prime + 1:
        raise AssertionError("source state was not an upper-half terminal bridge")

    factors = {int(q): int(exponent) for q, exponent in overflow.sympy.factorint(K).items()}
    target = -pow(4, -1, R) % R
    for C in overflow.divisors(factors):
        if C % R != target:
            continue
        H = K // C
        if (H + 1) % R or (4 * C + 1) % R:
            raise AssertionError("B=1 complementary residue did not follow")
        A = (H + 1) // R
        gap = (4 * C + 1) // R
        source_term = source * K // bridge_factor
        if (
            A <= 0
            or gap <= 0
            or bridge_factor * source_term != source * K
            or prime != 4 * A * C - gap
            or 4 * K != prime * R + 1
        ):
            raise AssertionError("B=1 source-state realization did not reconstruct")
        if Fraction(4, prime) != Fraction(1, A * C) + Fraction(1, A * C * H) + Fraction(1, prime * K):
            raise AssertionError("B=1 target identity failed")
        if Fraction(4, source) != Fraction(1, source_term) + Fraction(1, A * C) + Fraction(1, A * C * H):
            raise AssertionError("B=1 source identity failed")
        return {"A": A, "B": 1, "C": C, "H": H, "m": gap, "R": R, "K": K}
    return None


def upper_source_states(prime: int, gap_cap: int) -> tuple[list[dict[str, object]], int, int]:
    """Enumerate every distinct even upper-half source state in the stated Type I box."""
    states: dict[tuple[int, int], dict[str, object]] = {}
    forms = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                source = int(lift["source_denominator"])
                if source % 2 or 2 * source < prime + 1:
                    continue
                divisor = int(lift["bridge_divisor"])
                if divisor % (prime * prime):
                    raise AssertionError("reverse lift did not reconstruct a bridge factor")
                bridge_factor = divisor // (prime * prime)
                distance = prime - source
                key = (distance, bridge_factor)
                candidate = {
                    "source_distance": distance,
                    "source_denominator": source,
                    "E": bridge_factor,
                    "origin_gap": gap,
                    "origin_normal_form": [A, B, C],
                }
                previous = states.get(key)
                if previous is None or (
                    gap,
                    B,
                    A,
                    C,
                ) < (
                    int(previous["origin_gap"]),
                    int(previous["origin_normal_form"][1]),
                    int(previous["origin_normal_form"][0]),
                    int(previous["origin_normal_form"][2]),
                ):
                    states[key] = candidate
    return list(states.values()), forms, lifts_checked


def least_upper_realization(prime: int, states: list[dict[str, object]]) -> dict[str, object] | None:
    """Find the least B across the enumerated upper source states."""
    candidates: list[dict[str, object]] = []
    for state in states:
        source = int(state["source_denominator"])
        bridge_factor = int(state["E"])
        forms = realization.source_state_forms(prime, source, bridge_factor)
        if not forms:
            raise AssertionError("upper source state has no normal realization")
        form = forms[0]
        candidates.append({**state, "realization": form})
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda candidate: (
            int(candidate["realization"]["B"]),
            int(candidate["source_distance"]),
            int(candidate["E"]),
            int(candidate["origin_gap"]),
        ),
    )


def run_profile(profile: dict[str, object]) -> dict[str, object]:
    """Release shortest-source B=1 misses by upper-half source-state re-selection."""
    records = profile["records"]
    gap_cap = int(profile["gap_cap"])
    if not isinstance(records, list) or len(records) != 185:
        raise AssertionError("input must be the exact 185-point p-minus-one residual profile")

    direct_B_one: list[dict[str, object]] = []
    reselected_B_one: list[dict[str, object]] = []
    B_one_misses: list[dict[str, object]] = []
    forms_checked = 0
    lifts_checked = 0
    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("source profile contains a non-object record")
        prime = int(record["prime"])
        source = int(record["source_denominator"])
        bridge_factor = int(record["E"])
        direct = B_one_realization(prime, source, bridge_factor)
        if direct is not None:
            direct_B_one.append({"prime": prime, "stored_state": record, "B_one_realization": direct})
            continue

        states, local_forms, local_lifts = upper_source_states(prime, gap_cap)
        forms_checked += local_forms
        lifts_checked += local_lifts
        B_one_candidates = []
        for state in states:
            witness = B_one_realization(prime, int(state["source_denominator"]), int(state["E"]))
            if witness is not None:
                B_one_candidates.append({**state, "B_one_realization": witness})
        if B_one_candidates:
            selected = min(
                B_one_candidates,
                key=lambda candidate: (
                    int(candidate["source_distance"]),
                    int(candidate["E"]),
                    int(candidate["origin_gap"]),
                    int(candidate["B_one_realization"]["m"]),
                ),
            )
            reselected_B_one.append(
                {"prime": prime, "stored_state": record, "selected_upper_B_one_state": selected}
            )
            continue

        fallback = least_upper_realization(prime, states)
        if fallback is None:
            raise AssertionError("B=1 miss had no upper-half replacement source")
        B_one_misses.append(
            {"prime": prime, "stored_state": record, "upper_source_state_count": len(states), "least_upper_realization": fallback}
        )

    if len(direct_B_one) + len(reselected_B_one) + len(B_one_misses) != len(records):
        raise AssertionError("upper source re-selection did not partition the residual")
    if any(int(row["least_upper_realization"]["realization"]["B"]) > 3 for row in B_one_misses):
        raise AssertionError("a B>3 upper source re-selection miss was found")
    return {
        "arithmetic": (
            "test the stored shortest upper-half source state with the exact B=1 divisor-residue criterion; "
            "for each B=1 miss, exhaust every Type I normal form and strict maximum-tail lift through the "
            "same gap cap, retain every even upper-half source, then either reconstruct a B=1 source-state "
            "normal form or enumerate its compatible normal forms to minimize B"
        ),
        "scope_note": (
            "A complete finite source-reselection profile for the 185 p-minus-one misses in the shared "
            "p<=500M, m<=215 Type I box. It neither bounds B nor selects source states for arbitrary core primes."
        ),
        "input_artifact": INPUT.name,
        "p_minus_one_residual_count": len(records),
        "stored_upper_B_eq_1_count": len(direct_B_one),
        "reselected_upper_B_eq_1_count": len(reselected_B_one),
        "upper_B_eq_1_miss_count": len(B_one_misses),
        "upper_B_le_3_closure_count": len(records),
        "reselection_normal_forms_exhaustively_checked": forms_checked,
        "reselection_strict_reverse_lifts_exhaustively_checked": lifts_checked,
        "direct_B_eq_1_records": direct_B_one,
        "reselected_B_eq_1_records": reselected_B_one,
        "upper_B_eq_1_misses": B_one_misses,
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
            {key: value for key, value in result.items() if not key.endswith("_records") and key != "upper_B_eq_1_misses"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
