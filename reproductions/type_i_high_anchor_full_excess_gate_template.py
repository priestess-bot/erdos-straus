#!/usr/bin/env python3
"""Replay the quotient-window form of the high-R full-excess cofactor gate.

This is intentionally a three-control algebraic fixture.  It does not search
primes, inspect selector history, or infer E1--E5 provenance.  Its purpose is
to pin down two exact design templates for a *given* high canonical anchor:

* the general gate is a quotient divisibility / short-residue-window test;
* the subfamily C=qA has an automatic gate and is characterized by one
  congruence modulo p.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-full-excess-gate-template-results.json"

CONTROLS = (
    {"label": "p1201_return", "p": 1201, "R": 1839, "K": 552_160, "A": 986},
    {"label": "p3793_q2", "p": 3793, "R": 7011, "K": 6_648_181, "A": 1811},
    {"label": "p60913_q3", "p": 60_913, "R": 72_259, "K": 1_100_378_117, "A": 18_647},
)


def analyze(control: dict[str, int | str]) -> dict[str, object]:
    label = str(control["label"])
    prime = int(control["p"])
    R = int(control["R"])
    K = int(control["K"])
    A = int(control["A"])
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and shared.canonical_chart(prime, A) == (R, K)
        and prime < R < 4 * A
        and K % A == 0
        and gcd(prime, A) == 1
    ):
        raise AssertionError(f"{label}: not a canonical high anchor")

    bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError(f"{label}: malformed high bundle")
    M = int(rechart["M"])
    C = int(rechart["C"])
    Q = int(bundle["complete_excess_bundle"]["Q"])
    if not 0 < C < prime:
        raise AssertionError(f"{label}: direct cofactor left its C<p range")
    k, r = divmod(M, prime)
    g = gcd(A, C)
    a = A // g
    if M % A or M != lcm(A, Q):
        raise AssertionError(f"{label}: carrier no longer contains anchor support")
    if M % a:
        raise AssertionError(f"{label}: reduced gate divisor does not divide carrier")

    # Since M=kp+r, a|M, and gcd(a,p)=1, these are exactly equivalent.
    gate = r % a == 0
    quotient_gate = k % a == 0
    residue_window = (M // a) % prime
    window_gate = a * residue_window < prime
    if not (gate == quotient_gate == window_gate):
        raise AssertionError(f"{label}: quotient-window gate equivalence failed")

    B = K // A
    target_support = lcm(A, C)
    target_chart = (4 * r - (4 * r * (prime - C) + 1) // prime, r * C)
    if (4 * r * (prime - C) + 1) % prime:
        raise AssertionError(f"{label}: r-chart integrality failed")
    if gate and shared.canonical_chart(prime, target_support) != target_chart:
        raise AssertionError(f"{label}: gate no longer gives canonical target")

    automatic_q: dict[str, object] | None = None
    if C % A == 0:
        q = C // A
        congruence = (4 * q * A * M) % prime == 1
        reverse = q * A < prime and congruence
        if not (q >= 1 and q * A < prime and congruence and gate and a == 1):
            raise AssertionError(f"{label}: automatic C=qA template failed")
        automatic_q = {
            "q": q,
            "C_equals_qA": True,
            "qA_below_p": q * A < prime,
            "congruence_4qAM_eq_1_mod_p": congruence,
            "reverse_characterization_conditions": reverse,
            "automatic_gate": gate,
            "strict_support_growth": target_support == q * A and q > 1,
        }

    return_template: dict[str, object] | None = None
    if target_chart == (R, K):
        if not gate:
            raise AssertionError(f"{label}: return target unexpectedly lacks gate")
        u = r // a
        c = C // g
        if not (
            A == g * a
            and C == g * c
            and B == u * c
            and r == a * u
            and M % prime == a * u
            and 0 < a * u < prime
            and gcd(a, c) == 1
            and (4 * g * c * M) % prime == 1
        ):
            raise AssertionError(f"{label}: return divisor template failed")
        return_template = {
            "g": g,
            "a": a,
            "u": u,
            "c": c,
            "A_equals_g_a": A == g * a,
            "B_equals_u_c": B == u * c,
            "r_equals_a_u": r == a * u,
            "M_mod_p_equals_a_u": M % prime == a * u,
            "a_u_in_residue_range": 0 < a * u < prime,
            "C_equals_g_c": C == g * c,
            "C_in_direct_range": 0 < C < prime,
            "gcd_a_c_is_one": gcd(a, c) == 1,
            "congruence_4gcM_eq_1_mod_p": (4 * g * c * M) % prime == 1,
            "target_returns_to_anchor": True,
        }

    return {
        "label": label,
        "anchor": {"p": prime, "R": R, "K": K, "A": A, "B": B},
        "full_excess": {"Q": Q, "M": M, "C": C, "k": k, "r": r},
        "gate": {
            "gcd_A_C": g,
            "reduced_divisor_a": a,
            "r_mod_a": r % a,
            "floor_M_over_p_mod_a": k % a,
            "M_over_a_mod_p": residue_window,
            "window_inequality_a_t_lt_p": a * residue_window < prime,
            "passed": gate,
        },
        "target": {"support": target_support, "chart": list(target_chart)},
        "automatic_q_template": automatic_q,
        "return_divisor_template": return_template,
    }


def build_result() -> dict[str, object]:
    rows = [analyze(control) for control in CONTROLS]
    by_label = {str(row["label"]): row for row in rows}
    p1201 = by_label["p1201_return"]
    p3793 = by_label["p3793_q2"]
    p60913 = by_label["p60913_q3"]
    if not (
        p1201["gate"]["reduced_divisor_a"] == 29
        and p1201["gate"]["M_over_a_mod_p"] == 20
        and p1201["return_divisor_template"] == {
            "g": 34,
            "a": 29,
            "u": 20,
            "c": 28,
            "A_equals_g_a": True,
            "B_equals_u_c": True,
            "r_equals_a_u": True,
            "M_mod_p_equals_a_u": True,
            "a_u_in_residue_range": True,
            "C_equals_g_c": True,
            "C_in_direct_range": True,
            "gcd_a_c_is_one": True,
            "congruence_4gcM_eq_1_mod_p": True,
            "target_returns_to_anchor": True,
        }
        and p3793["automatic_q_template"]["q"] == 2
        and p60913["automatic_q_template"]["q"] == 3
    ):
        raise AssertionError("frozen gate-template controls changed")
    return {
        "schema_version": 1,
        "scope": "three fixed high-R controls; arithmetic only; no selector/history replay",
        "theorem_checks": {
            "gate_iff_quotient_divisibility": True,
            "gate_iff_short_residue_window": True,
            "C_equals_qA_congruence_characterization": True,
            "same_chart_return_divisor_factorization": True,
        },
        "rows": rows,
        "boundary": (
            "A passed arithmetic gate does not prove parent provenance, typed F/G fibers, "
            "terminal-first exhaustion, E1--E4, or a global recursive edge."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified high-anchor full-excess gate templates")
        return
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
