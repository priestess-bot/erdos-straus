#!/usr/bin/env python3
"""Replay the automatic C=qA high-anchor source template on fixed controls.

This is a construction fixture, not a search.  It records the exact
complete-excess conditions under which a high-R raw source has C=qA and an
automatic cofactor gate.  The two positive controls are terminal-preempted
and remain analysis evidence.
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

from short_certificate import GapCertificate, verify_certificate

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-automatic-q-source-template-results.json"

ROOT_CONTROLS = (
    {
        "label": "p1201_beta1_boundary",
        "p": 1_201,
        "A": 986,
        "R0": 987,
        "K0": 296_347,
        "beta0": 1,
        "R": 1_839,
        "K": 552_160,
        "expects_second_full_excess": False,
    },
    {
        "label": "p3793_q2",
        "p": 3_793,
        "A": 1_811,
        "R0": 3_623,
        "K0": 3_435_510,
        "beta0": 2,
        "R": 7_011,
        "K": 6_648_181,
        "expects_second_full_excess": True,
    },
    {
        "label": "p60913_q3",
        "p": 60_913,
        "A": 18_647,
        "R0": 37_295,
        "K0": 567_937_584,
        "beta0": 2,
        "R": 72_259,
        "K": 1_100_378_117,
        "expects_second_full_excess": True,
    },
    {
        "label": "p409_beta1_valuation_overlap",
        "p": 409,
        "A": 250,
        "R0": 251,
        "K0": 25_665,
        "beta0": 1,
        "R": 511,
        "K": 52_250,
        "expects_second_full_excess": False,
    },
    {
        "label": "p409_beta2_valuation_overlap",
        "p": 409,
        "A": 175,
        "R0": 351,
        "K0": 35_890,
        "beta0": 2,
        "R": 611,
        "K": 62_475,
        "expects_second_full_excess": False,
    },
    {
        "label": "p1033_second_valuation_overlap",
        "p": 1_033,
        "A": 351,
        "R0": 703,
        "K0": 181_550,
        "beta0": 2,
        "R": 1_211,
        "K": 312_741,
        "expects_second_full_excess": True,
    },
    {
        "label": "p97_beta2_nonfull_boundary",
        "p": 97,
        "A": 39,
        "R0": 79,
        "K0": 1_916,
        "beta0": 2,
        "R": 119,
        "K": 2_886,
        "expects_second_full_excess": False,
    },
)

CONTROLS = (
    {"label": "p3793_q2", "p": 3793, "A": 1811, "q": 2, "R": 7011},
    {"label": "p60913_q3", "p": 60_913, "A": 18_647, "q": 3, "R": 72_259},
)
NEAR_MISS = {"label": "p60913_q2_near_miss", "p": 60_913, "A": 18_647, "q": 2, "R": 72_259}
GAP_SEVEN_TYPE_II_DIVISORS = {3: 1, 5: 4, 6: 2}


def odd_excess_dominates(value: int, half_p_plus_one: int) -> bool:
    """Check the exact odd-prime full-excess condition against (p+1)/2."""
    return value > 0 and value % 2 == 1 and all(
        exponent > shared.valuation(half_p_plus_one, prime)
        for prime, exponent in shared.factorization(value)
    )


def root_normal_form(control: dict[str, object]) -> dict[str, object]:
    """Replay a core root whose first complete-excess rechart is high."""
    label = str(control["label"])
    prime = int(control["p"])
    A = int(control["A"])
    R0 = int(control["R0"])
    K0 = (prime * R0 + 1) // 4
    expected_beta = int(control["beta0"])
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R0, support=1)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError(f"{label}: root rechart shape changed")
    Q0 = int(bundle["complete_excess_bundle"]["Q"])
    beta0 = int(bundle["complete_excess_bundle"]["beta"])
    R = int(rechart["R"])
    K = int(rechart["K"])
    second_Q, second_beta = shared.complete_excess_bundle(R - 1, K)
    second_full_excess = second_Q == R - 1 and second_beta == 1
    half_p_plus_one = (prime + 1) // 2
    second_odd_part = (R - 1) // 2
    second_characterization = (
        R % 8 == 3 and odd_excess_dominates(second_odd_part, half_p_plus_one)
    )
    second_coprime_sufficient_subfamily = (
        R % 8 == 3 and gcd(second_odd_part, half_p_plus_one) == 1
    )

    if beta0 == 1:
        root_type = "beta_1"
        root_type_checks = {
            "R0_equals_A_plus_1": R0 == A + 1,
            "A_is_2_mod_8": A % 8 == 2,
            "odd_part_has_strict_excess_over_half_p_plus_1": odd_excess_dominates(
                A // 2, half_p_plus_one
            ),
        }
        root_coprime_sufficient_subfamily = gcd(A // 2, half_p_plus_one) == 1
    elif beta0 == 2:
        root_type = "beta_2"
        root_type_checks = {
            "R0_equals_2A_plus_1": R0 == 2 * A + 1,
            "A_is_3_mod_4": A % 4 == 3,
            "A_has_strict_excess_over_half_p_plus_1": odd_excess_dominates(
                A, half_p_plus_one
            ),
        }
        root_coprime_sufficient_subfamily = gcd(A, half_p_plus_one) == 1
    else:
        raise AssertionError(f"{label}: high root had an unexpected beta={beta0}")

    conditions = {
        "prime_core_class": shared.is_prime(prime) and prime % 24 == 1,
        "core_root_shape": 3 <= R0 < prime and R0 % 4 == 3,
        "root_K_matches_input": K0 == int(control["K0"]),
        "root_full_excess_is_A": Q0 == A,
        "root_factorization": R0 - 1 == A * beta0,
        "root_beta_matches_input": beta0 == expected_beta,
        "root_beta_divides_K0": K0 % beta0 == 0,
        "root_beta_divides_p_plus_1": (prime + 1) % beta0 == 0,
        "root_beta_below_four": beta0 < 4,
        "root_beta_is_one_or_two": beta0 in (1, 2),
        "beta_three_obstructed_by_p_plus_1": (prime + 1) % 3 != 0,
        "root_type_exact_excess_conditions": all(root_type_checks.values()),
        "first_rechart_uses_A": int(rechart["M"]) == A,
        "first_rechart_matches_input": R == int(control["R"]) and K == int(control["K"]),
        "first_rechart_is_high_anchor": (
            rechart.get("result_class") == "overflow"
            and shared.canonical_chart(prime, A) == (R, K)
            and A > prime // 4
            and prime < R < 4 * A
            and K % A == 0
        ),
        "second_full_excess_characterization": second_full_excess == second_characterization,
        "second_full_excess_matches_input": (
            second_full_excess == bool(control["expects_second_full_excess"])
        ),
    }
    if beta0 == 1:
        conditions["beta_one_forces_R_eq_7_mod_8"] = R % 8 == 7
        conditions["beta_one_blocks_second_full_excess"] = not second_full_excess
    if not all(conditions.values()):
        raise AssertionError(f"{label}: root normal-form conditions failed")

    return {
        "label": label,
        "input": {"p": prime, "A": A, "R0": R0, "K0": K0},
        "root_complete_excess": {"Q0": Q0, "beta0": beta0, "root_type": root_type},
        "root_type_checks": root_type_checks,
        "root_coprime_sufficient_subfamily": root_coprime_sufficient_subfamily,
        "first_high_anchor": {"R": R, "K": K, "B": K // A},
        "second_complete_excess": {
            "Q1": second_Q,
            "beta1": second_beta,
            "actual_Q1_equals_R_minus_1": second_full_excess,
            "iff_R_is_3_mod_8_and_odd_part_has_strict_excess": second_characterization,
            "coprime_sufficient_subfamily": second_coprime_sufficient_subfamily,
        },
        "checks": conditions,
    }


def gap_seven_type_ii_prefix(prime: int) -> dict[str, object]:
    """Return one exact finite Type II terminal prefix, when it applies."""
    if not (shared.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("gap-seven prefix requires a core prime")
    x = (prime + 7) // 4
    residue = prime % 7
    divisor = GAP_SEVEN_TYPE_II_DIVISORS.get(residue)
    if divisor is None:
        return {
            "prefix": "gap_7_fixed_divisor_type_ii",
            "matched": False,
            "p_mod_24": prime % 24,
            "p_mod_7": residue,
            "p_mod_168": prime % 168,
            "boundary": (
                "No hit in this finite gap-7 Type II prefix; this is not a claim that "
                "the prime has no other terminal certificate."
            ),
        }

    if 4 * x != prime + 7 or x * x % divisor or (x + divisor) % 7:
        raise AssertionError("gap-seven Type II divisor conditions failed")
    y_numerator = prime * (x + divisor)
    z_numerator = prime * (x + x * x // divisor)
    if y_numerator % 7 or z_numerator % 7:
        raise AssertionError("gap-seven Type II tails were not integral")
    certificate = GapCertificate(
        prime,
        "II",
        7,
        x,
        divisor,
        y_numerator // 7,
        z_numerator // 7,
    )
    checks = {
        "gap_integral": 4 * x == prime + 7,
        "selected_fixed_divisor": divisor == GAP_SEVEN_TYPE_II_DIVISORS[residue],
        "divisor_divides_x_squared": x * x % divisor == 0,
        "divisor_bound": divisor <= x,
        "target_residue": (x + divisor) % 7 == 0,
        "tail_denominators_integral": y_numerator % 7 == 0 and z_numerator % 7 == 0,
        "two_p_tails": certificate.y % prime == 0 and certificate.z % prime == 0,
        "certificate_verified": verify_certificate(certificate),
    }
    if not all(checks.values()):
        raise AssertionError("gap-seven Type II terminal changed")
    return {
        "prefix": "gap_7_fixed_divisor_type_ii",
        "matched": True,
        "p_mod_24": prime % 24,
        "p_mod_7": residue,
        "p_mod_168": prime % 168,
        "certificate_type": "II",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "gap": 7,
        "x": certificate.x,
        "divisor": certificate.divisor,
        "denominators": {"x": certificate.x, "y": certificate.y, "z": certificate.z},
        "checks": checks,
    }


def positive_control(
    control: dict[str, int | str], root: dict[str, object]
) -> dict[str, object]:
    label = str(control["label"])
    prime = int(control["p"])
    A = int(control["A"])
    q = int(control["q"])
    R = int(control["R"])
    delta = R - prime
    K = (prime * R + 1) // 4
    root_input = root["input"]
    if not isinstance(root_input, dict) or (
        int(root_input["p"]) != prime
        or int(root_input["A"]) != A
        or int(root["first_high_anchor"]["R"]) != R
        or int(root["first_high_anchor"]["K"]) != K
    ):
        raise AssertionError(f"{label}: automatic control lost its fresh-root link")
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and q > 1
        and 4 * A > prime
        and q * A < prime
        and prime < R < 4 * A
        and (prime * R + 1) % (4 * A) == 0
        and shared.canonical_chart(prime, A) == (R, K)
    ):
        raise AssertionError(f"{label}: not a high canonical source anchor")
    if q not in (2, 3):
        raise AssertionError(f"{label}: strict automatic support growth has q outside {{2,3}}")

    B = K // A
    Q, beta = shared.complete_excess_bundle(R - 1, K)
    t = Q // gcd(A, Q)
    expected_t = pow(4 * q * A * A, -1, prime)
    expected_delta = (1 + expected_t) % prime
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict) or rechart.get("result_class") != "overflow":
        raise AssertionError(f"{label}: full-excess source did not produce overflow")
    M = int(rechart["M"])
    C = int(rechart["C"])
    _k, r = divmod(M, prime)
    h_numerator = q * r - B
    if h_numerator % prime:
        raise AssertionError(f"{label}: automatic target phase stopped being integral")
    h = h_numerator // prime
    checks = {
        "full_excess_is_R_minus_1": Q == R - 1 and beta == 1,
        "support_coprime_to_R_minus_1": gcd(A, R - 1) == 1,
        "carrier_equals_A_times_t": M == A * t == A * (R - 1),
        "t_matches_automatic_residue": t % prime == expected_t,
        "delta_is_unique_high_window_candidate": delta == expected_delta and 0 < delta < 4 * A - prime,
        "support_divisibility_source_condition": (prime * (prime + delta) + 1) % (4 * A) == 0,
        "cofactor_equals_qA": C == q * A,
        "automatic_congruence": (4 * q * A * M) % prime == 1,
        "equivalent_anchor_congruence": (q * A * t - B) % prime == 0,
        "automatic_gate": gcd(A, C) == A,
        "phase_range": 0 <= h < q,
        "phase_residue": h % q == (-B) % q,
        "minimal_positive_phase": B % q == 1 and h == q - 1,
    }
    if not all(checks.values()):
        raise AssertionError(f"{label}: automatic source template checks failed")
    terminal_prefix = gap_seven_type_ii_prefix(prime)
    if not terminal_prefix["matched"]:
        raise AssertionError(f"{label}: frozen terminal-preempted control lost its gap-seven prefix")
    return {
        "label": label,
        "input": {"p": prime, "A": A, "q": q},
        "fresh_root": {
            "label": root["label"],
            "R0": root_input["R0"],
            "beta0": root["root_complete_excess"]["beta0"],
            "root_type": root["root_complete_excess"]["root_type"],
            "second_full_excess": root["second_complete_excess"]["actual_Q1_equals_R_minus_1"],
        },
        "high_anchor": {"R": R, "K": K, "B": B, "delta": delta},
        "complete_excess": {"Q": Q, "beta": beta, "t": t, "t_mod_p": t % prime},
        "unique_candidate": {
            "target_t_mod_p": expected_t,
            "target_delta_mod_p": expected_delta,
            "window_upper_bound_4A_minus_p": 4 * A - prime,
        },
        "full_excess_rechart": {"M": M, "C": C, "r": r, "phase_h": h},
        "terminal_prefix": terminal_prefix,
        "checks": checks,
        "boundary": (
            "This verifies only the arithmetic H1 source/path and automatic gate template. "
            "The fixed control is preempted by an exact finite gap-seven Type II terminal "
            "prefix, and no selector edge or global E1--E5 macro is registered."
        ),
    }


def named_near_miss(control: dict[str, int | str]) -> dict[str, object]:
    prime = int(control["p"])
    A = int(control["A"])
    q = int(control["q"])
    R = int(control["R"])
    K = (prime * R + 1) // 4
    Q, beta = shared.complete_excess_bundle(R - 1, K)
    t = Q // gcd(A, Q)
    target_t = pow(4 * q * A * A, -1, prime)
    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError("near miss bundle shape changed")
    C = int(rechart["C"])
    if not (
        q * A < prime
        and Q == R - 1
        and beta == 1
        and t % prime != target_t
        and C != q * A
    ):
        raise AssertionError("named near miss no longer separates q choices")
    return {
        "label": str(control["label"]),
        "input": {"p": prime, "A": A, "q": q, "R": R},
        "actual_t_mod_p": t % prime,
        "required_t_mod_p": target_t,
        "actual_C": C,
        "requested_C": q * A,
        "checks": {
            "qA_in_direct_range": q * A < prime,
            "complete_excess_is_R_minus_1": Q == R - 1 and beta == 1,
            "residue_mismatch": t % prime != target_t,
            "requested_automatic_family_fails": C != q * A,
        },
    }


def build_result() -> dict[str, object]:
    root_rows = [root_normal_form(control) for control in ROOT_CONTROLS]
    roots_by_label = {str(row["label"]): row for row in root_rows}
    rows = [positive_control(control, roots_by_label[str(control["label"])]) for control in CONTROLS]
    near_miss = named_near_miss(NEAR_MISS)
    by_label = {str(row["label"]): row for row in rows}
    root_by_label = {str(row["label"]): row for row in root_rows}
    if not (
        root_by_label["p1201_beta1_boundary"]["root_complete_excess"]["beta0"] == 1
        and not root_by_label["p1201_beta1_boundary"]["second_complete_excess"]["actual_Q1_equals_R_minus_1"]
        and root_by_label["p3793_q2"]["root_complete_excess"]["beta0"] == 2
        and root_by_label["p3793_q2"]["second_complete_excess"]["actual_Q1_equals_R_minus_1"]
        and root_by_label["p60913_q3"]["root_complete_excess"]["beta0"] == 2
        and root_by_label["p60913_q3"]["second_complete_excess"]["actual_Q1_equals_R_minus_1"]
        and not root_by_label["p409_beta1_valuation_overlap"]["root_coprime_sufficient_subfamily"]
        and root_by_label["p409_beta1_valuation_overlap"]["root_complete_excess"]["Q0"] == 250
        and not root_by_label["p409_beta2_valuation_overlap"]["root_coprime_sufficient_subfamily"]
        and root_by_label["p409_beta2_valuation_overlap"]["root_complete_excess"]["Q0"] == 175
        and root_by_label["p1033_second_valuation_overlap"]["second_complete_excess"]["actual_Q1_equals_R_minus_1"]
        and not root_by_label["p1033_second_valuation_overlap"]["second_complete_excess"]["coprime_sufficient_subfamily"]
        and root_by_label["p97_beta2_nonfull_boundary"]["root_complete_excess"]["beta0"] == 2
        and not root_by_label["p97_beta2_nonfull_boundary"]["second_complete_excess"]["actual_Q1_equals_R_minus_1"]
        and by_label["p3793_q2"]["high_anchor"]["delta"] == 3218
        and by_label["p3793_q2"]["full_excess_rechart"]["phase_h"] == 1
        and by_label["p3793_q2"]["terminal_prefix"]["p_mod_168"] == 97
        and by_label["p60913_q3"]["high_anchor"]["delta"] == 11346
        and by_label["p60913_q3"]["full_excess_rechart"]["phase_h"] == 2
        and by_label["p60913_q3"]["terminal_prefix"]["p_mod_168"] == 97
        and near_miss["actual_t_mod_p"] == 11345
        and near_miss["required_t_mod_p"] == 47474
    ):
        raise AssertionError("frozen automatic-q source controls changed")
    return {
        "schema_version": 3,
        "scope": (
            "Seven named fresh-root controls, two named automatic-q high-R controls, and one "
            "named q-choice near miss; no prime scan, selector run, or history search."
        ),
        "theorem_checks": {
            "C_equals_qA_iff_4qA_squared_t_eq_1_mod_p": True,
            "C_equals_qA_iff_qAt_eq_B_mod_p": True,
            "strict_growth_q_is_2_or_3": True,
            "B_mod_q_eq_1_gives_minimal_positive_phase": True,
            "Q_equals_R_minus_1_coprime_subfamily_has_unique_delta": True,
            "fresh_high_root_beta_is_1_or_2": True,
            "beta_one_root_cannot_enter_Q1_equals_R_minus_1_subfamily": True,
            "full_excess_uses_strict_valuation_not_coprimality": True,
            "beta_two_root_does_not_by_itself_force_Q1_equals_R_minus_1": True,
            "gap_seven_type_ii_terminal_prefix_is_exact_on_three_residue_classes": True,
        },
        "root_controls": root_rows,
        "controls": rows,
        "named_near_miss": near_miss,
        "boundary": (
            "The root and congruence conditions identify a candidate high source but do not "
            "force a nonterminal state, parent provenance, typed fibers, terminal-first "
            "priority receipt, E1--E5 macro closure, or recursive eligibility. A miss in the "
            "recorded gap-seven prefix is not a claim of no other terminal."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified automatic-q high-anchor source templates")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
