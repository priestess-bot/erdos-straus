#!/usr/bin/env python3
"""Verify the gap-3/gap-7 survivor sieve for minimal automatic-q sources.

The script combines the parameter phase gate with exact Bradford predicates
at gaps 3 and 7.  Its prefix is deliberately finite: a miss remains only a
candidate for the full terminal-first menu, never a registered macro edge.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from short_certificate import (
    certificate_at_gap,
    divisors_of_square,
    gap_seven_congruence_certificate,
    gap_three_criterion,
    smallest_prime_factors,
    verify_certificate,
)
import type_i_high_anchor_q2_bku_parameterization as q2
import type_i_high_anchor_q3_bku_parameterization as q3
import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-automatic-q-gap3-gap7-survivor-sieve-results.json"

PHASE_SOURCE_CONTROLS = (
    {"label": "p3793_fixed_gap7", "q": 2, "p": 3_793, "terminal": "fixed_gap7"},
    {"label": "p60913_fixed_gap7", "q": 3, "p": 60_913, "terminal": "fixed_gap7"},
    {"label": "p34897_gap3", "q": 2, "p": 34_897, "terminal": "gap3"},
    {"label": "p68713_gap3_before_nonfixed_gap7", "q": 2, "p": 68_713, "terminal": "gap3"},
)

CORE_BOUNDARIES = (
    {"label": "p193_nonfixed_gap7", "p": 193, "prefix_miss": False},
    {"label": "p1201_true_prefix_miss", "p": 1_201, "prefix_miss": True},
)


def phase_is_minimal(q: int, k: int) -> bool:
    if q == 2:
        return k % 2 == 0
    if q == 3:
        return k % 3 == 2
    raise AssertionError("automatic-q sieve only permits q=2 or q=3")


def source_control(q: int, prime: int) -> dict[str, int | str]:
    if q == 2:
        for control in q2.CONTROLS:
            if int(control["p"]) == prime:
                q2.verify_positive_control(control)
                return control
    if q == 3:
        for control in q3.CONTROLS:
            if int(control["p"]) == prime:
                q3.verify_control(control)
                return control
    raise AssertionError("missing frozen minimal-phase automatic source control")


def gap_profile(prime: int) -> dict[str, object]:
    if not (shared.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("gap profile requires a core prime")
    x3 = (prime + 3) // 4
    x7 = (prime + 7) // 4
    spf = smallest_prime_factors(x7 + 1)
    gap3 = certificate_at_gap(prime, 3, spf)
    gap7 = certificate_at_gap(prime, 7, spf)
    fixed_gap7 = gap_seven_congruence_certificate(prime)
    x3_factors = shared.factorization(x3)
    x3_all_one_mod_three = all(factor % 3 == 1 for factor, _ in x3_factors)
    gap3_exact = gap_three_criterion(prime, spf)
    divisors = divisors_of_square(x7, spf)
    type_i_target = (-prime * x7) % 7
    type_ii_target = (-x7) % 7
    type_i_hits = [divisor for divisor in divisors if divisor % 7 == type_i_target]
    type_ii_hits = [
        divisor for divisor in divisors if divisor <= x7 and divisor % 7 == type_ii_target
    ]
    if gap3 is not None and not verify_certificate(gap3):
        raise AssertionError("gap-3 certificate stopped verifying")
    if gap7 is not None and not verify_certificate(gap7):
        raise AssertionError("gap-7 certificate stopped verifying")
    if fixed_gap7 is not None and not verify_certificate(fixed_gap7):
        raise AssertionError("fixed gap-7 certificate stopped verifying")
    checks = {
        "x3_is_one_mod_three": x3 % 3 == 1,
        "gap3_factor_criterion": (gap3 is None) == x3_all_one_mod_three == (not gap3_exact),
        "gap7_target_simplification": (
            type_i_target == (-2 * prime * prime) % 7
            and type_ii_target == (-2 * prime) % 7
        ),
        "gap7_divisor_criterion": (gap7 is None) == (not type_i_hits and not type_ii_hits),
        "fixed_gap7_residue_classes": (
            (fixed_gap7 is None) == (prime % 7 in (1, 2, 4))
        ),
        "crt_fixed_gap7_survivor_classes": (
            (prime % 7 in (1, 2, 4)) == (prime % 168 in (1, 25, 121))
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"gap sieve criterion changed for p={prime}: {checks}")
    return {
        "p": prime,
        "p_mod_168": prime % 168,
        "x3": x3,
        "x3_factors": [[factor, exponent] for factor, exponent in x3_factors],
        "x3_all_one_mod_three": x3_all_one_mod_three,
        "gap3": None if gap3 is None else {"type": gap3.certificate_type, "divisor": gap3.divisor},
        "gap7": None if gap7 is None else {"type": gap7.certificate_type, "divisor": gap7.divisor},
        "fixed_gap7": (
            None
            if fixed_gap7 is None
            else {"type": fixed_gap7.certificate_type, "divisor": fixed_gap7.divisor}
        ),
        "gap7_targets": {"type_i": type_i_target, "type_ii": type_ii_target},
        "gap7_hits": {"type_i": type_i_hits, "type_ii": type_ii_hits},
        "prefix_miss": gap3 is None and gap7 is None,
        "factor_form_miss": x3_all_one_mod_three and not type_i_hits and not type_ii_hits,
        "checks": checks,
    }


def replay_phase_source(item: dict[str, int | str]) -> dict[str, object]:
    q = int(item["q"])
    control = source_control(q, int(item["p"]))
    k = int(control["k"])
    profile = gap_profile(int(control["p"]))
    expected_terminal = str(item["terminal"])
    checks = {
        "minimal_parameter_phase": phase_is_minimal(q, k),
        "prefix_terminal": not bool(profile["prefix_miss"]),
        "expected_terminal_kind": (
            (expected_terminal == "fixed_gap7" and profile["fixed_gap7"] is not None)
            or (expected_terminal == "gap3" and profile["gap3"] is not None)
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"{item['label']}: phase-source sieve control failed: {checks}")
    return {
        "label": str(item["label"]),
        "q": q,
        "k": k,
        "profile": profile,
        "checks": checks,
    }


def replay_core_boundary(item: dict[str, int | str | bool]) -> dict[str, object]:
    profile = gap_profile(int(item["p"]))
    checks = {
        "fixed_gap7_residue_survivor": int(profile["p_mod_168"]) in (1, 25, 121),
        "gap3_miss": profile["gap3"] is None,
        "prefix_miss_matches_control": bool(profile["prefix_miss"]) == bool(item["prefix_miss"]),
    }
    if not all(checks.values()):
        raise AssertionError(f"{item['label']}: core boundary changed: {checks}")
    return {"label": str(item["label"]), "profile": profile, "checks": checks}


def build_result() -> dict[str, object]:
    source_rows = [replay_phase_source(item) for item in PHASE_SOURCE_CONTROLS]
    boundary_rows = [replay_core_boundary(item) for item in CORE_BOUNDARIES]
    if any(bool(row["profile"]["prefix_miss"]) for row in source_rows):
        raise AssertionError("frozen minimal-phase source controls unexpectedly survived the prefix")
    if [bool(row["profile"]["prefix_miss"]) for row in boundary_rows] != [False, True]:
        raise AssertionError("core prefix-survivor boundaries changed")
    return {
        "schema_version": 1,
        "certificate_type": "automatic_q_gap3_gap7_prefix_survivor_sieve_v1",
        "scope": (
            "Exact [gap 3, gap 7] direct-terminal predicates applied after the q=2/q=3 "
            "minimal-phase parameter gate. A prefix miss is only a candidate for the full "
            "terminal-first menu and cannot register a macro edge."
        ),
        "phase_source_controls": source_rows,
        "core_boundaries": boundary_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified automatic-q gap-3/gap-7 survivor sieve: 4 phase sources + 2 core boundaries")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
