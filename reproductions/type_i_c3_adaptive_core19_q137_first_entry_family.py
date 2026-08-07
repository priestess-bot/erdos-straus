#!/usr/bin/env python3
"""Verify the q=137 C=19 raw family and its fixed-pair terminal boundary."""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks
import type_i_high_r_chart_two_anchor as shared


P0 = 193
P_STEP = 772_716_168
R0 = 823
R_STEP = 3_348_436_728
H0 = 8
H_STEP = 32_196_507
Q0 = 43
Q_STEP = 174_947_136
FIRST_LABEL = 137
TERMINAL_GAP = 1_319
TERMINAL_SUBRAY_STEP = P_STEP * TERMINAL_GAP


def prime_word(value: int) -> list[int]:
    """Expand one positive integer into its ordered prime word."""
    word: list[int] = []
    for prime, exponent in shared.factorization(value):
        word.extend([prime] * exponent)
    return word


def positive_divisors(factors: tuple[tuple[int, int], ...]) -> list[int]:
    """Return divisors from a declared complete factorization."""
    values = [1]
    for prime, exponent in factors:
        values = [
            value * prime**power
            for value in values
            for power in range(exponent + 1)
        ]
    return sorted(values)


def type_ii_factor_pair(prime: int, gap: int, divisor: int) -> dict[str, int]:
    """Verify a direct factor-pair terminal without any terminal scan."""
    if gap <= 0 or gap % 4 != 3 or (prime + gap) % 4:
        raise AssertionError("q=137 terminal gap has the wrong parity")
    x = (prime + gap) // 4
    if not (
        divisor <= x
        and x * x % divisor == 0
        and (x + divisor) % gap == 0
    ):
        raise AssertionError("q=137 control terminal arithmetic changed")
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("q=137 control terminal identity changed")
    return {"gap": gap, "divisor": divisor, "x": x, "y": y, "z": z}


def verify_capacity_subray() -> dict[str, object]:
    """Prove the four exact residue gates and freeze them at v=12369*w."""
    M0, M_STEP_V = 209, 67_678
    X0, X_STEP_V = 190, 62_472
    R_BASE, R_STEP_V = 823, 270_712
    Q_STEP_V = 14_144
    determinants = (
        Q0 * M_STEP_V - Q_STEP_V * M0,
        Q0 * X_STEP_V - Q_STEP_V * X0,
        Q0 * R_STEP_V - Q_STEP_V * R_BASE,
    )
    forbidden = ((3, 1), (7, 5), (19, 16), (31, 14))
    if not (
        determinants == (-45_942, -1_064, 104)
        and abs(determinants[0]) == 2 * 3 * 13 * 19 * 31
        and abs(determinants[1]) == 2**3 * 7 * 19
        and determinants[2] == 2**3 * 13
        and 12_369 == 3 * 7 * 19 * 31
        and gcd(P0, P_STEP) == 1
        and P0 + P_STEP == 772_716_361
        and R0 + R_STEP == 3_348_437_551
        and Q0 + Q_STEP == 174_947_179
        and P_STEP == 62_472 * 12_369
        and R_STEP == R_STEP_V * 12_369
        and Q_STEP == Q_STEP_V * 12_369
        and (209, 190, 823) == (26 * 8 + 1, 193 - 3, 104 * 8 - 9)
        and (M_STEP_V, X_STEP_V, R_STEP_V) == (137 * 494, 137 * 456, 137 * 1976)
        and 137 % 2 and 137 % 3 and 137 % 7 and 137 % 13 and 137 % 19 and 137 % 31
        and all(
            value % FIRST_LABEL != 0
            for value in (209, 190, 823)
        )
        and all(value % 19 == 0 for value in (209, 190, M_STEP_V, X_STEP_V))
        and (63 * P0 + 1) % 76 == 0
        and P_STEP % 76 == 0
        and Q0 % 2 and Q0 % 13
        and Q_STEP_V % 13 == 0
        and all(
            (Q0 + Q_STEP_V * root) % modulus == 0
            and Q_STEP_V % modulus != 0
            and Q0 % modulus != 0
            for modulus, root in forbidden
        )
    ):
        raise AssertionError("q=137 capacity subray arithmetic changed")
    return {
        "base_v_filters": {f"mod_{modulus}": root for modulus, root in forbidden},
        "stable_subray": {"v": "12369*w", "p": [P0, P_STEP]},
        "determinants": list(determinants),
        "raw_admission": "every prime p(w) has gcd(Q, K*R)=1",
        "fixed_c_reset": {"C": 19, "rho": 63, "target_R": 63},
    }


def verify_fixed_pair_screen() -> dict[str, object]:
    """Exhaust only the finite fixed-template criterion for this affine ray."""
    factorization = ((2, 3), (3, 2), (7, 1), (19, 2), (31, 1), (137, 1))
    divisors = positive_divisors(factorization)
    gaps = [value for value in divisors if value % 4 == 3]
    candidates: list[tuple[int, int]] = []
    candidate_count = 0
    for gap in gaps:
        E = gcd((P0 + gap) // 4, P_STEP // 4)
        d_values = positive_divisors(tuple(shared.factorization(E * E)))
        candidate_count += len(d_values)
        for divisor in d_values:
            if divisor <= (P0 + gap) // 4 and (P0 + 4 * divisor) % gap == 0:
                candidates.append((gap, divisor))
    if not (len(gaps) == 36 and candidate_count == 144 and not candidates):
        raise AssertionError("q=137 fixed-pair screen changed")
    return {
        "fixed_gap_count": len(gaps),
        "fixed_divisor_candidate_count": candidate_count,
        "uniform_pair_hits": candidates,
        "scope": "fixed affine (m,d) templates only",
    }


def verify_terminal_preempted_subray() -> dict[str, object]:
    """Close the moving m=1319 terminal subray before raw RESET dispatch."""
    base = P0 + P_STEP
    quotient = 585_835
    K0 = 146_459
    x0 = 193_179_420
    K_step = 193_179_042
    x_step = 254_803_156_398
    if not (
        TERMINAL_GAP == 1_319
        and P_STEP % TERMINAL_GAP == -197 % TERMINAL_GAP
        and gcd(197, TERMINAL_GAP) == 1
        and TERMINAL_SUBRAY_STEP == 1_019_212_625_592
        and base == 772_716_361
        and shared.is_prime(base)
        and gcd(base, TERMINAL_SUBRAY_STEP) == 1
        and base % 24 == 1
        and TERMINAL_SUBRAY_STEP % 24 == 0
        and base + 4 == TERMINAL_GAP * quotient
        and 4 * K0 - 1 == quotient
        and x0 == TERMINAL_GAP * K0 - 1
        and 4 * x0 == base + TERMINAL_GAP
        and TERMINAL_GAP * K_step == x_step
    ):
        raise AssertionError("q=137 terminal subray arithmetic changed")
    initial = type_ii_factor_pair(base, TERMINAL_GAP, 1)
    if initial != {
        "gap": TERMINAL_GAP,
        "divisor": 1,
        "x": x0,
        "y": 113_171_265_515_699,
        "z": 21_862_359_432_988_733_714_580,
    }:
        raise AssertionError("q=137 terminal control changed")
    for t in (0, 1, 17):
        prime = base + TERMINAL_SUBRAY_STEP * t
        K = K0 + K_step * t
        x = x0 + x_step * t
        if not (
            prime + 4 == TERMINAL_GAP * (quotient + P_STEP * t)
            and 4 * K - 1 == (prime + 4) // TERMINAL_GAP
            and x == TERMINAL_GAP * K - 1
            and 4 * x == prime + TERMINAL_GAP
            and type_ii_factor_pair(prime, TERMINAL_GAP, 1)["x"] == x
        ):
            raise AssertionError("q=137 terminal family identity changed")
    return {
        "gap": TERMINAL_GAP,
        "divisor": 1,
        "parameter_subray": {
            "w": "1 + 1319*t",
            "p": [base, TERMINAL_SUBRAY_STEP],
            "t": "nonnegative; retain prime parameters",
        },
        "certificate": initial,
        "prime_progression_gcd": gcd(base, TERMINAL_SUBRAY_STEP),
        "raw_status": "q=137 admission remains actual; terminal-first preempts RESET",
    }


def verify_prime_control() -> dict[str, object]:
    """Replay the focused prime w=1 raw word."""
    w = 1
    prime = P0 + P_STEP * w
    R = R0 + R_STEP * w
    h = H0 + H_STEP * w
    M = 26 * h + 1
    K = M * (prime - 3)
    b = (R - 1) // FIRST_LABEL
    Q_value = (R - b) // 19
    if not (
        shared.is_prime(prime)
        and K == 2 * 19**2 * 3803 * 5347 * 44_058_389
        and R - 1 == FIRST_LABEL * b
        and R - b == 19 * Q_value
        and Q_value == 11 * 181 * 87_869
        and gcd(Q_value, K * R) == 1
        and K % FIRST_LABEL != 0
        and R % FIRST_LABEL == 1
    ):
        raise AssertionError("q=137 prime raw control changed")
    source = (prime, R * (prime - 1) - prime, prime - 1)
    p_edge = raw.ordered_raw_step(
        modulus=R,
        K=K,
        source=source,
        selected_coordinate_index=0,
        q=prime,
        expected_destination=(1, R - 1, 1),
        name="q137_universal_p_edge",
    )
    first = raw.ordered_raw_step(
        modulus=R,
        K=K,
        source=(1, R - 1, 1),
        selected_coordinate_index=1,
        q=FIRST_LABEL,
        expected_destination=(b, R - b, 1),
        name="q137_first_label",
    )
    _, block = factor_blocks.replay_block(
        modulus=R,
        K=K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=prime_word(Q_value),
        endpoint=(19, R - 19, 1),
        name="q137_c19_block",
    )
    rows = [p_edge, first, *block]
    if any(
        not row["strict_capacity"]
        or not row["unit_condition"]
        or row["gcd_reduction"] != 1
        for row in rows
    ):
        raise AssertionError("q=137 prime word lost a primitive raw edge")
    terminal = type_ii_factor_pair(prime, TERMINAL_GAP, 1)
    if terminal["x"] != 193_179_420:
        raise AssertionError("q=137 prime control lost its direct terminal")
    return {
        "w": w,
        "p": prime,
        "R": R,
        "Q": Q_value,
        "raw_word": [[1, 137], [1, 11], [0, 181], [0, 87869]],
        "destination": [19, R - 19, 1],
        "terminal": terminal,
        "terminal_status": "direct Type II m=1319,d=1; terminal-first",
    }


def build_result() -> dict[str, object]:
    """Build actual raw controls and their deliberately narrow terminal boundary."""
    return {
        "certificate_type": "c3_core19_q137_first_entry_family_v2",
        "capacity_subray": verify_capacity_subray(),
        "fixed_pair_screen": verify_fixed_pair_screen(),
        "terminal_preempted_subray": verify_terminal_preempted_subray(),
        "prime_raw_control": verify_prime_control(),
        "base_terminal_control": type_ii_factor_pair(193, 7, 20),
        "selector_status": "actual_raw_family_with_terminal_preempted_subray",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=137 C=19 actual raw family and fixed-pair boundary")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
