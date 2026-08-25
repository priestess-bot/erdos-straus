#!/usr/bin/env python3
"""Exclude capacity one on the actual H4 clean-q atomic source gate.

The proof reduces the negative D-residue condition to two exact finite menus.
Only the final surviving arithmetic row is sent through the actual H3-to-H4
maximal-carrier reconstruction.  No prime interval or denominator scan is
performed.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    STEP,
    base_prime,
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import (
    complete_excess,
)


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = (
    ROOT / "data" / "t6-wave1" / "f2-h4-atomic-capacity-one-exclusion-v1.json"
)


def _phase_linear_solution(d: int, base: int) -> tuple[int, int] | None:
    """Solve 2*d*q == base+1 (mod STEP)."""
    coefficient = 2 * d
    target = base + 1
    common = gcd(coefficient, STEP)
    if target % common:
        return None
    modulus = STEP // common
    residue = (target // common) * pow(coefficient // common, -1, modulus) % modulus
    return residue, modulus


def _odd_phase_pairs() -> list[tuple[int, int, int]]:
    rows: list[tuple[int, int, int]] = []
    for u in sorted(FINAL_RESIDUAL):
        a = selector_a(base_prime(u))
        for d in sympy.divisors(abs(1536 - a)):
            d = int(d)
            if d % 2:
                rows.append((u, a, d))
    if len(rows) != 109:
        raise AssertionError("the 31-phase odd carrier menu changed")
    return rows


def low_p_menu() -> dict[str, object]:
    """Exhaust p<=delta_d with the exact phase progression and negative residue."""
    q_values = 0
    phase_primes = 0
    d_candidates = 0
    hits: list[dict[str, int]] = []
    for u, a, d in _odd_phase_pairs():
        base = base_prime(u)
        solution = _phase_linear_solution(d, base)
        if solution is None:
            continue
        q_start, q_modulus = solution
        if q_start < 2:
            q_start += ((2 - q_start + q_modulus - 1) // q_modulus) * q_modulus
        s_d = 4 * d * d - 2 * d + 1
        delta = 2 * d * s_d
        for q in range(q_start, s_d + 1, q_modulus):
            q_values += 1
            p = 2 * d * q - 1
            if p < base or (p - base) % STEP or not sympy.isprime(p):
                continue
            phase_primes += 1
            divisor_bound = (2 * d - 1) * ((2 * d + 1) * q - 1)
            residue = (-delta) % p or p
            for lift in range(2 * d):
                D = residue + lift * p
                if D >= 2 * d * p:
                    break
                d_candidates += 1
                if divisor_bound % D == 0:
                    hits.append(
                        {
                            "u": u,
                            "a": a,
                            "d": d,
                            "q": q,
                            "p": p,
                            "D": D,
                            "ell": divisor_bound // D,
                        }
                    )
    if (
        q_values,
        phase_primes,
        d_candidates,
        hits,
    ) != (2204, 524, 1_054_140, []):
        raise AssertionError("the low-p negative D-residue menu changed")
    return {
        "phase_carrier_pairs": 109,
        "q_values": q_values,
        "phase_primes": phase_primes,
        "D_candidates": d_candidates,
        "divisibility_hits": hits,
    }


def high_p_menu() -> dict[str, object]:
    """Parameterize p>delta_d and return the exact phase survivors."""
    counts = {
        "k1_divisor_parameters": 0,
        "k1_prime_values": 0,
        "k1_phase_values": 0,
        "k_ge_2_ell_parameters": 0,
        "k_ge_2_integral_values": 0,
        "k_ge_2_prime_values": 0,
        "k_ge_2_phase_values": 0,
    }
    survivors: list[dict[str, int]] = []
    for u, a, d in _odd_phase_pairs():
        base = base_prime(u)
        s_d = 4 * d * d - 2 * d + 1
        delta = 2 * d * s_d

        # k=1: p=delta+C/m, with m|C and m=1 (mod 2d).
        constant = delta * (4 * d * d - 1) + (2 * d - 1)
        for m_raw in sympy.divisors(constant):
            m = int(m_raw)
            if m % (2 * d) != 1:
                continue
            ell = (m + 4 * d * d - 1) // (2 * d)
            if ell < 2 * d:
                continue
            counts["k1_divisor_parameters"] += 1
            p = delta + constant // m
            if not sympy.isprime(p):
                continue
            counts["k1_prime_values"] += 1
            if p < base or (p - base) % STEP or (p + 1) % (2 * d):
                continue
            counts["k1_phase_values"] += 1
            q = (p + 1) // (2 * d)
            D = p - delta
            divisor_bound = (2 * d - 1) * ((2 * d + 1) * q - 1)
            if D > 0 and D < 2 * d * p and divisor_bound == ell * D:
                survivors.append(
                    {"u": u, "a": a, "d": d, "q": q, "p": p, "D": D, "ell": ell, "k": 1, "delta": delta}
                )

        # k>=2: k*ell>=2d and ell*(k-1)<=2d-1 force one k for each ell<2d.
        for ell in range(1, 2 * d):
            counts["k_ge_2_ell_parameters"] += 1
            k = (2 * d + ell - 1) // ell
            denominator = 2 * d * k * ell - (4 * d * d - 1)
            numerator = 2 * d * ell * delta + (2 * d - 1)
            if denominator <= 0 or numerator % denominator:
                continue
            counts["k_ge_2_integral_values"] += 1
            p = numerator // denominator
            if p <= delta or not sympy.isprime(p):
                continue
            counts["k_ge_2_prime_values"] += 1
            if p < base or (p - base) % STEP or (p + 1) % (2 * d):
                continue
            counts["k_ge_2_phase_values"] += 1
            q = (p + 1) // (2 * d)
            D = k * p - delta
            divisor_bound = (2 * d - 1) * ((2 * d + 1) * q - 1)
            if D > 0 and D < 2 * d * p and divisor_bound == ell * D:
                survivors.append(
                    {"u": u, "a": a, "d": d, "q": q, "p": p, "D": D, "ell": ell, "k": k, "delta": delta}
                )

    expected_counts = {
        "k1_divisor_parameters": 255,
        "k1_prime_values": 98,
        "k1_phase_values": 0,
        "k_ge_2_ell_parameters": 32_853,
        "k_ge_2_integral_values": 422,
        "k_ge_2_prime_values": 108,
        "k_ge_2_phase_values": 1,
    }
    expected_survivors = [
        {
            "u": 117,
            "a": 2046,
            "d": 85,
            "q": 48_842_701,
            "p": 8_303_259_169,
            "D": 141_150_521_603,
            "ell": 10,
            "k": 17,
            "delta": 4_884_270,
        }
    ]
    if counts != expected_counts or survivors != expected_survivors:
        raise AssertionError("the high-p negative D-residue parameterization changed")
    return {**counts, "phase_survivors": survivors}


def actual_carrier_check(row: dict[str, int]) -> dict[str, int | bool]:
    """Rebuild the exact H3-to-H4 maximal carrier on the sole survivor."""
    p = row["p"]
    data = h3_data(p)
    block, beta = complete_excess(int(data["R_3"]) - 1, int(data["K_3"]))
    overlap = gcd(int(data["M_3"]), block)
    lambda_value = beta * overlap // 2
    M4 = lcm(int(data["M_3"]), block)
    actual_d = gcd((p + 1) // 2, M4)
    result: dict[str, int | bool] = {
        "p": p,
        "u": row["u"],
        "a": int(data["a"]),
        "required_d": row["d"],
        "actual_d": actual_d,
        "beta": beta,
        "overlap": overlap,
        "lambda": lambda_value,
        "carrier_matches": actual_d == row["d"],
    }
    if result != {
        "p": 8_303_259_169,
        "u": 117,
        "a": 2046,
        "required_d": 85,
        "actual_d": 1,
        "beta": 10,
        "overlap": 1,
        "lambda": 5,
        "carrier_matches": False,
    }:
        raise AssertionError("the sole H4 C1 survivor actual-carrier check changed")
    return result


def build_receipt() -> dict[str, object]:
    low = low_p_menu()
    high = high_p_menu()
    survivors = high["phase_survivors"]
    if not isinstance(survivors, list) or len(survivors) != 1:
        raise AssertionError("the high-p menu must have exactly one arithmetic survivor")
    carrier = actual_carrier_check(survivors[0])
    return {
        "artifact_id": "f2_h4_atomic_capacity_one_exclusion_v1",
        "theorem": "type-I-h4-atomic-capacity-one-source-gate-exclusion",
        "status": "H4_C1_ACTUAL_SOURCE_FAMILY_EMPTY",
        "negative_gate": {
            "capacity_condition": "c_q=1 iff E_x=-q mod p",
            "source_condition": "D=-delta_d mod p; D divides (2d-1)((2d+1)q-1); 0<D<2dp",
            "phase_condition": "p=base(u) mod 108528; d divides abs(1536-a(u)); d=gcd((p+1)/2,M4)",
        },
        "low_p": low,
        "high_p": high,
        "sole_survivor_actual_carrier": carrier,
        "conclusion": {
            "actual_h4_clean_q_capacity_one": "EMPTY",
            "c8_second_full_excess_capacity_one": "EMPTY_BY_EXISTING_75C_EQ_64_THEOREM",
            "global_high_support_C1": "NOT_CLOSED_WITHOUT_ALL_PRODUCER_TARGET_SETS",
        },
    }


def verify() -> None:
    stored = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    actual = build_receipt()
    if actual != stored:
        raise AssertionError("stored H4 capacity-one exclusion receipt is stale")
    print(
        "verified H4 clean-q capacity-one exclusion: low-p menu empty; "
        "one high-p arithmetic row; actual carrier 1 != required 85"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.json:
        print(json.dumps(build_receipt(), indent=2, sort_keys=True))
        return
    if not args.verify:
        parser.error("pass --verify or --json")
    verify()


if __name__ == "__main__":
    main()
