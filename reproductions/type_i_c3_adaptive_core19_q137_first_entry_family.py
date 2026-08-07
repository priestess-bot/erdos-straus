#!/usr/bin/env python3
"""Verify the q=137 C=19 raw family and its fixed-pair terminal boundary."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt

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
D1_WEB_CONTROLS = ((11, 3), (55, 36), (1_319, 1))
TARGET_D = 6_303
TARGET_A = 1
TARGET_C = TARGET_D
TARGET_MODULUS = 4 * TARGET_D
TARGET_FACTOR = TARGET_MODULUS - 1
TARGET_W0 = 21_771
TARGET_PARAMETER_STEP = TARGET_FACTOR
TARGET_P_BASE = 16_822_803_693_721
TARGET_P_STEP = 19_480_947_311_448
TARGET_CONTROL_T = 2
TARGET_CONTROL_W = 72_193
TARGET_CONTROL_P = 55_784_698_316_617


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


def d1_terminal_web_entry(gap: int) -> dict[str, object]:
    """Construct one exact d=1 moving-terminal ray inside the q=137 family."""
    if gap <= 0 or gap % 4 != 3 or gcd(gap, P_STEP) != 1:
        raise AssertionError("d=1 terminal-web gap is not admissible")
    inverse = pow(P_STEP, -1, gap)
    w0 = (-(P0 + 4) * inverse) % gap
    prime0 = P0 + P_STEP * w0
    prime_step = P_STEP * gap
    L0 = (prime0 + 4) // gap
    K0 = (L0 + 1) // 4
    x0 = gap * K0 - 1
    if not (
        P_STEP == 2**3 * 3**2 * 7 * 19**2 * 31 * 137
        and gcd(P0, P_STEP) == gcd(P_STEP, P0 + 4) == 1
        and gap != 3
        and 0 <= w0 < gap
        and (prime0 + 4) % gap == 0
        and L0 % 4 == 3
        and prime0 + 4 == gap * (4 * K0 - 1)
        and 4 * x0 == prime0 + gap
        and prime0 > gap + 2
        and 0 < x0 < prime0
        and gcd(prime0, prime_step) == 1
        and prime0 % 24 == 1
        and prime_step % 24 == 0
    ):
        raise AssertionError("d=1 terminal-web base arithmetic changed")

    certificates = []
    for t in (0, 1, 17):
        prime = prime0 + prime_step * t
        K = K0 + (P_STEP // 4) * t
        x = x0 + (gap * P_STEP // 4) * t
        certificate = type_ii_factor_pair(prime, gap, 1)
        if not (
            (prime + 4) // gap == 4 * K - 1
            and x == gap * K - 1
            and 4 * x == prime + gap
            and prime > gap + 2
            and 0 < x < prime
            and certificate == {
                "gap": gap,
                "divisor": 1,
                "x": x,
                "y": prime * K,
                "z": prime * K * x,
            }
        ):
            raise AssertionError("d=1 terminal-web affine identity changed")
        certificates.append(certificate)
    return {
        "gap": gap,
        "w_residue": w0,
        "parameter_ray": {"w": f"{w0}+{gap}*t", "p": [prime0, prime_step]},
        "Dirichlet_progression_gcd": gcd(prime0, prime_step),
        "certificate_controls": certificates,
        "scope": "for prime terms only; terminal-first preempts the actual q=137 raw receipt",
    }


def verify_d1_terminal_web() -> dict[str, object]:
    """Prove the exact d=1 gap classification, not a full terminal cover."""
    controls = [d1_terminal_web_entry(gap) for gap, _ in D1_WEB_CONTROLS]
    by_gap = {int(control["gap"]): control for control in controls}
    if not (
        [(int(control["gap"]), int(control["w_residue"])) for control in controls]
        == list(D1_WEB_CONTROLS)
        and by_gap[1_319]["parameter_ray"]["p"]
        == [772_716_361, TERMINAL_SUBRAY_STEP]
        and P0 + 4 == 197
        and 197 % 4 == 1
    ):
        raise AssertionError("d=1 terminal-web controls changed")
    return {
        "classification": (
            "For m congruent to 3 modulo 4, d=1 holds at p(w)=193+D*w "
            "iff gcd(m,D)=1 and w equals -(197)*D^-1 modulo m."
        ),
        "controls": controls,
        "base_w_zero_status": "outside the d=1 web; it has the separate (m,d)=(7,20) terminal",
        "scope": "d=1 factor-pair terminals only; this is an infinite web, not full coverage",
    }


def one_base_pocklington(
    value: int,
    base: int,
    factors: tuple[tuple[int, int], ...],
    verified_primes: set[int],
) -> None:
    """Replay a short Pocklington step from previously certified primes."""
    proved_factor = 1
    for prime, exponent in factors:
        if prime not in verified_primes or exponent <= 0:
            raise AssertionError("Pocklington chain has an uncertified factor")
        proved_factor *= prime**exponent
    if not (
        value > 2
        and (value - 1) % proved_factor == 0
        and proved_factor > isqrt(value)
        and pow(base, value - 1, value) == 1
        and all(
            gcd(pow(base, (value - 1) // prime, value) - 1, value) == 1
            for prime, _exponent in factors
        )
    ):
        raise AssertionError("target-tuned Pocklington step changed")


def verify_target_tuned_prime_control() -> None:
    """Certify one actual prime term without trial-dividing the large label."""
    small_primes = {2, 3, 5, 7, 29, 43, 53, 1_163}
    if not all(shared.is_prime(prime) for prime in small_primes):
        raise AssertionError("target-tuned Pocklington base factor is not prime")
    verified_primes = set(small_primes)
    chain = (
        (21_003_781, 10, ((2, 2), (3, 1), (5, 1), (7, 1), (43, 1), (1_163, 1))),
        (252_045_373, 2, ((21_003_781, 1),)),
        (43_855_894_903, 2, ((252_045_373, 1),)),
        (TARGET_CONTROL_P, 2, ((43_855_894_903, 1),)),
    )
    for value, base, factors in chain:
        one_base_pocklington(value, base, factors, verified_primes)
        verified_primes.add(value)
    if not (
        21_003_781 - 1 == 2**2 * 3 * 5 * 7 * 43 * 1_163
        and 252_045_373 - 1 == 2**2 * 3 * 21_003_781
        and 43_855_894_903 - 1 == 2 * 3 * 29 * 252_045_373
        and TARGET_CONTROL_P - 1 == 2**3 * 3 * 53 * 43_855_894_903
    ):
        raise AssertionError("target-tuned Pocklington factorizations changed")


def verify_target_tuned_subray(
    capacity_subray: dict[str, object] | None = None,
) -> dict[str, object]:
    """Construct an actual q=137 raw subray with a D=6303 Type II target."""
    verify_target_tuned_prime_control()
    if capacity_subray is None:
        capacity_subray = verify_capacity_subray()
    if capacity_subray.get("stable_subray") != {
        "v": "12369*w",
        "p": [P0, P_STEP],
    }:
        raise AssertionError("target-tuned subray lost its q=137 raw-family gate")
    if not (
        TARGET_D == 3 * 11 * 191
        and TARGET_A == 1
        and TARGET_C == TARGET_D // TARGET_A == 6_303
        and TARGET_MODULUS == 25_212
        and TARGET_FACTOR == 25_211 == 4 * TARGET_A * TARGET_C - 1
        and gcd(TARGET_FACTOR, TARGET_MODULUS) == 1
        and gcd(P_STEP, TARGET_FACTOR) == 1
        and TARGET_W0
        == (-(P0 + TARGET_A * TARGET_MODULUS) * pow(P_STEP, -1, TARGET_FACTOR))
        % TARGET_FACTOR
        and TARGET_P_BASE == P0 + P_STEP * TARGET_W0
        and TARGET_P_STEP == P_STEP * TARGET_PARAMETER_STEP
        and TARGET_CONTROL_W == TARGET_W0 + TARGET_PARAMETER_STEP * TARGET_CONTROL_T
        and TARGET_CONTROL_P == TARGET_P_BASE + TARGET_P_STEP * TARGET_CONTROL_T
        and gcd(TARGET_P_BASE, TARGET_P_STEP) == 1
        and TARGET_P_BASE % 24 == 1
        and TARGET_P_STEP % 24 == 0
        and TARGET_A * TARGET_MODULUS < TARGET_P_BASE
        and (TARGET_P_BASE + TARGET_A * TARGET_MODULUS) % TARGET_FACTOR == 0
    ):
        raise AssertionError("target-tuned raw progression changed")

    certificates = []
    for t in (0, TARGET_CONTROL_T, 17):
        w = TARGET_W0 + TARGET_PARAMETER_STEP * t
        prime = TARGET_P_BASE + TARGET_P_STEP * t
        B = (prime + TARGET_A) // TARGET_FACTOR
        gap = TARGET_A + B
        x = TARGET_A * B * TARGET_C
        certificate = type_ii_factor_pair(prime, gap, TARGET_A**2 * TARGET_C)
        if not (
            w >= 0
            and prime == P0 + P_STEP * w
            and prime + TARGET_A * TARGET_MODULUS == TARGET_FACTOR * gap
            and TARGET_FACTOR * B == prime + TARGET_A
            and gap % 4 == 3
            and 3 <= gap <= prime - 2
            and TARGET_A <= B
            and gcd(TARGET_A, B) == 1
            and x == TARGET_A * B * TARGET_C
            and 0 < x < prime
            and certificate
            == {
                "gap": gap,
                "divisor": TARGET_A**2 * TARGET_C,
                "x": x,
                "y": prime * TARGET_A * TARGET_C,
                "z": prime * B * TARGET_C,
            }
        ):
            raise AssertionError("target-tuned Type II normal form changed")
        certificates.append({"t": t, "w": w, "B": B, **certificate})
    return {
        "D_star": TARGET_D,
        "A": TARGET_A,
        "C": TARGET_C,
        "K": 1,
        "target_factor": TARGET_FACTOR,
        "parameter_subray": {
            "w": f"{TARGET_W0}+{TARGET_PARAMETER_STEP}*t",
            "p": [TARGET_P_BASE, TARGET_P_STEP],
            "prime_terms": "Dirichlet progression; t=2 is Pocklington-certified",
        },
        "prime_progression_gcd": gcd(TARGET_P_BASE, TARGET_P_STEP),
        "actual_raw_status": "q=137 raw receipt follows for every prime parameter",
        "certificates": certificates,
        "scope": (
            "An explicitly target-tuned terminal subray, not a raw-to-fiber adapter "
            "or a terminal-free selector branch."
        ),
    }


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
    """Build actual raw controls and their terminal-first boundaries."""
    capacity_subray = verify_capacity_subray()
    return {
        "certificate_type": "c3_core19_q137_first_entry_family_v3",
        "capacity_subray": capacity_subray,
        "fixed_pair_screen": verify_fixed_pair_screen(),
        "terminal_preempted_subray": verify_terminal_preempted_subray(),
        "d1_terminal_web": verify_d1_terminal_web(),
        "target_tuned_terminal_subray": verify_target_tuned_subray(capacity_subray),
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
        print("verified q=137 C=19 raw family, d=1 terminal web, and target-tuned Type II subray")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
