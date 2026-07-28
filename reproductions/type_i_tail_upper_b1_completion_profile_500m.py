#!/usr/bin/env python3
"""Close the 500M ordinary-tail residual with upper-half B=1 Type I bridges.

This is a composition audit.  The complete m<=215 B=1 scan supplies 1,713
even-source bridges, of which 1,709 are already upper-half.  Four lower-half
records are re-selected through the same source-state generation window; three
then have B=1 realizations and the remaining target is released directly at
m=231.  The four direct B=1 misses are supplied by the independent m<=999
extension.  Every selected final bridge is rebuilt exactly.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
DIRECT_EXTENSION = ROOT / "reproductions" / "type-i-direct-b1-gap-extension-500m-results.json"
P_MIN_ONE_EXTENSION = (
    ROOT / "reproductions" / "type-i-pminusone-miss-upper-b1-gap-extension-500m-results.json"
)
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
RESELECTION = ROOT / "reproductions" / "type_i_pminusone_miss_upper_b3_reselection_profile.py"
P_MIN_ONE_EXTENSION_SCRIPT = ROOT / "reproductions" / "type_i_pminusone_miss_upper_b1_gap_extension.py"
SOURCE_STATE_GAP_CAP = 215
P_MIN_ONE_EXTENSION_GAP_CAP = 231
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-upper-b1-completion-profile-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("tail_upper_b1_completion_landscape", LANDSCAPE)
bridge = load_module("tail_upper_b1_completion_bridge", BRIDGE)
reselection = load_module("tail_upper_b1_completion_reselection", RESELECTION)
pminus_extension = load_module(
    "tail_upper_b1_completion_pminus_extension", P_MIN_ONE_EXTENSION_SCRIPT
)


def verify_certificate(
    prime: int,
    gap: int,
    normal_form: list[int],
    source: int,
    bridge_factor: int,
    expected_source_term: int | None = None,
    require_upper_half: bool = True,
) -> dict[str, int | list[int]]:
    """Rebuild a selected upper-half B=1 bridge and both unit-fraction identities."""
    A, B, C = (int(value) for value in normal_form)
    if B != 1 or gap < 3 or gap % 4 != 3:
        raise AssertionError("selected record is not a natural B=1 normal form")
    R = (4 * C + 1) // gap
    H = A * R - 1
    K = C * H
    source_term, remainder = divmod(source * K, bridge_factor)
    if remainder:
        raise AssertionError("bridge factor did not divide the normalized source term")
    if expected_source_term is not None and source_term != expected_source_term:
        raise AssertionError("stored source term did not reconstruct")
    target = (A * C, A * C * H, prime * K)
    source_solution = (source_term, target[0], target[1])
    if (
        R < 3
        or R % 2 == 0
        or H <= 0
        or gap * R != 4 * C + 1
        or 4 * K != prime * R + 1
        or source % 2
        or bridge_factor % 2
        or bridge_factor % R != 1
        or bridge_factor > 4 * K - 2 * R
        or (4 * K * K) % bridge_factor
        or (4 * C + 1) % R
    ):
        raise AssertionError("selected B=1 bridge failed its exact conditions")
    if require_upper_half and 2 * source < prime + 1:
        raise AssertionError("selected B=1 bridge is not an upper-half source")
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("selected target identity did not verify")
    if Fraction(4, source) != sum(
        (Fraction(1, term) for term in source_solution), Fraction()
    ):
        raise AssertionError("selected source identity did not verify")
    return {
        "gap": gap,
        "normal_form": [A, B, C],
        "R": R,
        "K": K,
        "E": bridge_factor,
        "source_denominator": source,
        "source_distance": prime - source,
        "source_term": source_term,
    }


def stored_witness(prime: int, witness: dict[str, object]) -> dict[str, int | list[int]]:
    """Validate one witness from the complete m<=215 B=1 audit."""
    lift = witness["reverse_two_tail_lift"]
    if not isinstance(lift, dict):
        raise AssertionError("stored B=1 witness has no reverse lift")
    divisor = int(lift["bridge_divisor"])
    if divisor % (prime * prime):
        raise AssertionError("stored B=1 witness has no integral bridge factor")
    return verify_certificate(
        prime,
        int(witness["gap"]),
        [int(value) for value in witness["normal_form"]],
        int(lift["source_denominator"]),
        divisor // (prime * prime),
        int(lift["source_term"]),
        False,
    )


def direct_upper_extension_candidate(
    prime: int, gap_cap: int
) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust an already known direct residual for its least-gap upper B=1 edge."""
    candidates: list[dict[str, object]] = []
    forms_checked = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B != 1:
                continue
            forms_checked += 1
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            lifts_checked += len(lifts)
            for lift in lifts:
                source = int(lift["source_denominator"])
                if source % 2 or 2 * source < prime + 1:
                    continue
                divisor = int(lift["bridge_divisor"])
                if divisor % (prime * prime):
                    raise AssertionError("direct extension lift did not reconstruct a bridge factor")
                bridge_factor = divisor // (prime * prime)
                certificate = verify_certificate(
                    prime, gap, [A, B, C], source, bridge_factor, int(lift["source_term"])
                )
                candidates.append({"certificate": certificate})
    if not candidates:
        return None, forms_checked, lifts_checked
    return (
        min(
            candidates,
            key=lambda row: (
                int(row["certificate"]["gap"]),
                int(row["certificate"]["source_distance"]),
                int(row["certificate"]["E"]),
            ),
        ),
        forms_checked,
        lifts_checked,
    )


def reselection_candidate(
    prime: int, gap_cap: int
) -> tuple[dict[str, object] | None, int, int]:
    """Choose the least-gap B=1 realization among upper states generated in the box."""
    states, forms_checked, lifts_checked = reselection.upper_source_states(prime, gap_cap)
    candidates: list[dict[str, object]] = []
    for state in states:
        source = int(state["source_denominator"])
        bridge_factor = int(state["E"])
        witness = reselection.B_one_realization(prime, source, bridge_factor)
        if witness is None:
            continue
        certificate = verify_certificate(
            prime,
            int(witness["m"]),
            [int(witness["A"]), int(witness["B"]), int(witness["C"])],
            source,
            bridge_factor,
        )
        candidates.append(
            {
                "generated_source_state": state,
                "B_one_realization": witness,
                "certificate": certificate,
            }
        )
    if not candidates:
        return None, forms_checked, lifts_checked
    return (
        min(
            candidates,
            key=lambda row: (
                int(row["B_one_realization"]["m"]),
                int(row["certificate"]["source_distance"]),
                int(row["certificate"]["E"]),
                int(row["generated_source_state"]["origin_gap"]),
            ),
        ),
        forms_checked,
        lifts_checked,
    )


def pminus_extension_candidate(prime: int) -> tuple[dict[str, object], int, int]:
    """Directly extend the sole source-state residual through m=231."""
    candidates, forms_checked, lifts_checked = pminus_extension.upper_b_one_candidates(
        prime, SOURCE_STATE_GAP_CAP, P_MIN_ONE_EXTENSION_GAP_CAP
    )
    if not candidates:
        raise AssertionError("p-minus-one source-state residual was not released at m<=231")
    first_gap = min(int(row["gap"]) for row in candidates)
    first = [row for row in candidates if int(row["gap"]) == first_gap]
    selected = min(
        first,
        key=lambda row: (int(row["source_distance"]), int(row["E"])),
    )
    certificate = verify_certificate(
        prime,
        int(selected["gap"]),
        [int(value) for value in selected["normal_form"]],
        int(selected["source_denominator"]),
        int(selected["E"]),
    )
    return (
        {
            "first_upper_B_eq_1_gap": first_gap,
            "first_gap_candidate_count": len(first),
            "selected": selected,
            "certificate": certificate,
        },
        forms_checked,
        lifts_checked,
    )


def run_profile(
    base: dict[str, object],
    direct_extension: dict[str, object],
    pminus_extension_profile: dict[str, object],
) -> dict[str, object]:
    """Compose the exact finite B=1 artifacts into an upper-half closure."""
    records = base["records"]
    base_misses = [int(prime) for prime in base["misses"]]
    if not isinstance(records, list) or len(records) != 1713:
        raise AssertionError("base B=1 profile must contain its exact 1,713 captured records")
    if base_misses != [39_407_449, 63_332_329, 172_657_489, 193_288_489]:
        raise AssertionError("base B=1 profile has an unexpected direct residual")
    if int(base["gap_cap"]) != SOURCE_STATE_GAP_CAP:
        raise AssertionError("base source-state generation cap changed")
    if int(direct_extension["direct_b_one_count"]) != len(records):
        raise AssertionError("direct B=1 extension is not based on the same captured set")

    direct_upper: list[int] = []
    lower_records: list[tuple[int, dict[str, object]]] = []
    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("base B=1 profile contains a malformed record")
        prime = int(record["prime"])
        witness = record["minimum_b1_source_witness"]
        if not isinstance(witness, dict):
            raise AssertionError("base B=1 record has no witness")
        certificate = stored_witness(prime, witness)
        if 2 * int(certificate["source_denominator"]) >= prime + 1:
            direct_upper.append(prime)
        else:
            lower_records.append((prime, record))
    if len(direct_upper) != 1709 or len(lower_records) != 4:
        raise AssertionError("base B=1 source-half split changed")

    reselected: list[dict[str, object]] = []
    source_state_misses: list[int] = []
    source_forms_checked = 0
    source_lifts_checked = 0
    for prime, _ in lower_records:
        candidate, forms_checked, lifts_checked = reselection_candidate(
            prime, SOURCE_STATE_GAP_CAP
        )
        source_forms_checked += forms_checked
        source_lifts_checked += lifts_checked
        if candidate is None:
            source_state_misses.append(prime)
        else:
            reselected.append({"prime": prime, **candidate})
    if [row["prime"] for row in reselected] != [629_689, 58_757_449, 83_445_289]:
        raise AssertionError("lower B=1 re-selection did not release the expected three targets")
    if source_state_misses != [218_482_009]:
        raise AssertionError("unexpected lower B=1 source-state residual")

    pminus_record, pminus_forms_checked, pminus_lifts_checked = pminus_extension_candidate(
        source_state_misses[0]
    )

    direct_extension_records = direct_extension["extensions"]
    if not isinstance(direct_extension_records, list) or len(direct_extension_records) != 4:
        raise AssertionError("direct extension must release the exact four B=1 misses")
    extended: list[dict[str, object]] = []
    direct_extension_forms_checked = 0
    direct_extension_lifts_checked = 0
    direct_extension_gap_cap = int(direct_extension["gap_cap"])
    for row in direct_extension_records:
        if not isinstance(row, dict) or not isinstance(row["witness"], dict):
            raise AssertionError("direct extension contains a malformed witness")
        prime = int(row["prime"])
        if prime not in base_misses:
            raise AssertionError("direct extension released a non-residual target")
        candidate, forms_checked, lifts_checked = direct_upper_extension_candidate(
            prime, direct_extension_gap_cap
        )
        direct_extension_forms_checked += forms_checked
        direct_extension_lifts_checked += lifts_checked
        if candidate is None:
            raise AssertionError("direct B=1 extension has no upper-half B=1 witness")
        extended.append({"prime": prime, **candidate})
    if [row["prime"] for row in extended] != base_misses:
        raise AssertionError("direct extension did not preserve the exact residual order")

    selected_gaps = [
        int(row["certificate"]["gap"]) for row in reselected
    ] + [int(pminus_record["certificate"]["gap"])] + [
        int(row["certificate"]["gap"]) for row in extended
    ]
    if max(selected_gaps) != 5_963:
        raise AssertionError("combined upper B=1 gap maximum changed")
    if len(direct_upper) + len(reselected) + 1 + len(extended) != 1_717:
        raise AssertionError("combined upper B=1 branches did not close the full residual")
    if int(pminus_extension_profile["upper_B_eq_1_source_state_closure_count"]) != 185:
        raise AssertionError("p-minus-one extension input did not preserve its source-state closure")
    return {
        "arithmetic": (
            "partition the complete 500M B=1 even-source audit into direct upper and lower records; "
            "for the four lower records generate every upper source state through m<=215 and reconstruct "
            "least-gap B=1 normal forms; release the one remaining source-state target directly through "
            "m=231; join the four direct B=1 misses to their complete m<=999 extension; and rebuild every "
            "selected target/source Egyptian-fraction identity"
        ),
        "scope_note": (
            "A complete finite composition audit for the stored 1,717 ordinary Type II tail misses. "
            "It proves the stated B=1 upper-source closure only for this input and selected finite "
            "subsearches; it gives neither a global gap bound nor a universal selector."
        ),
        "base_B_one_artifact": BASE.name,
        "direct_B_one_extension_artifact": DIRECT_EXTENSION.name,
        "p_minus_one_extension_artifact": P_MIN_ONE_EXTENSION.name,
        "ordinary_tail_miss_count": 1_717,
        "base_source_state_generation_gap_cap": SOURCE_STATE_GAP_CAP,
        "direct_upper_B_eq_1_count": len(direct_upper),
        "lower_B_eq_1_record_count": len(lower_records),
        "lower_source_state_reselected_B_eq_1_count": len(reselected),
        "lower_source_state_direct_gap_extension_count": 1,
        "direct_B_eq_1_gap_extension_count": len(extended),
        "upper_B_eq_1_closure_count": 1_717,
        "maximum_selected_B_eq_1_normal_gap": max(selected_gaps),
        "lower_source_state_normal_forms_exhaustively_checked": source_forms_checked,
        "lower_source_state_strict_reverse_lifts_exhaustively_checked": source_lifts_checked,
        "p_minus_one_extension_normal_forms_exhaustively_checked": pminus_forms_checked,
        "p_minus_one_extension_strict_reverse_lifts_exhaustively_checked": pminus_lifts_checked,
        "direct_B_eq_1_extension_normal_forms_exhaustively_checked": direct_extension_forms_checked,
        "direct_B_eq_1_extension_strict_reverse_lifts_exhaustively_checked": direct_extension_lifts_checked,
        "direct_upper_primes": direct_upper,
        "lower_source_state_reselected_records": reselected,
        "lower_source_state_direct_gap_extension_record": {
            "prime": source_state_misses[0],
            **pminus_record,
        },
        "direct_B_eq_1_gap_extension_records": extended,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=BASE)
    parser.add_argument("--direct-extension", type=Path, default=DIRECT_EXTENSION)
    parser.add_argument("--pminus-extension", type=Path, default=P_MIN_ONE_EXTENSION)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.base.read_text(encoding="utf-8")),
        json.loads(args.direct_extension.read_text(encoding="utf-8")),
        json.loads(args.pminus_extension.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key
                not in {
                    "direct_upper_primes",
                    "lower_source_state_reselected_records",
                    "lower_source_state_direct_gap_extension_record",
                    "direct_B_eq_1_gap_extension_records",
                }
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
