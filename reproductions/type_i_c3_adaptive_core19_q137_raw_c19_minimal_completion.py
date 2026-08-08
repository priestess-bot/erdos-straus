#!/usr/bin/env python3
"""Verify the minimal two-raw-atom q=19 target completion on the q=137 ray.

This fixture proves an arithmetic owner/normalization control only.  It does
not create an F/G Fourier demand, a Hall request, a capacity price, or a
selector edge.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt

import type_i_c3_adaptive_core19_q137_first_entry_family as q137
import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks


RAW_ENDPOINT_Q = 19
RAW_EDGE_Q = 5
TARGET_H = RAW_ENDPOINT_Q * RAW_EDGE_Q
SOURCE_A = 2
SOURCE_C = 1
SOURCE_D = SOURCE_A * SOURCE_C
SOURCE_M = 4 * SOURCE_D
SOURCE_K = (TARGET_H + 1) // SOURCE_M

NORMAL_GCD = 2
NORMAL_A = SOURCE_A // NORMAL_GCD
NORMAL_C = NORMAL_GCD**2 * SOURCE_C
NORMAL_D = NORMAL_A * NORMAL_C
NORMAL_M = 4 * NORMAL_D
NORMAL_K = SOURCE_K // NORMAL_GCD

REDUCED_STEP = q137.P_STEP // RAW_ENDPOINT_Q
SUBRAY_W0 = 27
SUBRAY_W_STEP = 25
PRIME_BASE = q137.P0 + q137.P_STEP * SUBRAY_W0
PRIME_STEP = q137.P_STEP * SUBRAY_W_STEP
COFACTOR_BASE = (PRIME_BASE + 16) // TARGET_H
COFACTOR_STEP = PRIME_STEP // TARGET_H
RAW_Q_BASE = q137.Q0 + q137.Q_STEP * SUBRAY_W0
RAW_Q_STEP = q137.Q_STEP * SUBRAY_W_STEP
RAW_Q_TAIL_CONTROL = 944_714_543


def valuation(value: int, prime: int) -> int:
    """Return the positive prime-adic valuation used by this focused control."""
    if value <= 0 or prime <= 1:
        raise AssertionError("valuation requires a positive value and prime")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def is_prime_by_trial(value: int) -> bool:
    """Certify the small-to-medium fixed labels without a probabilistic oracle."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def one_base_pocklington(
    value: int,
    base: int,
    factors: tuple[tuple[int, int], ...],
) -> None:
    """Check a complete one-base Pocklington certificate from known primes."""
    proved_factor = 1
    for prime, exponent in factors:
        if exponent <= 0 or not is_prime_by_trial(prime):
            raise AssertionError("Pocklington factor was not certified")
        proved_factor *= prime**exponent
    if not (
        value - 1 == proved_factor
        and proved_factor > isqrt(value)
        and pow(base, value - 1, value) == 1
        and all(
            gcd(pow(base, (value - 1) // prime, value) - 1, value) == 1
            for prime, _exponent in factors
        )
    ):
        raise AssertionError("Pocklington certificate changed")


def certify_prime_control() -> None:
    """Certify the first prime on the exact-height two-atom subray."""
    inner = 66_869_669
    if not all(is_prime_by_trial(value) for value in (3, 13, 3_701, 4_517)):
        raise AssertionError("small Pocklington input changed")
    one_base_pocklington(inner, 2, ((2, 2), (3_701, 1), (4_517, 1)))
    if not (
        inner - 1 == 2**2 * 3_701 * 4_517
        and PRIME_BASE - 1 == 2**3 * 3 * 13 * inner
    ):
        raise AssertionError("Pocklington factorization changed")
    one_base_pocklington(
        PRIME_BASE,
        17,
        ((2, 3), (3, 1), (13, 1), (inner, 1)),
    )


def completion_residue(r: int) -> int | None:
    """Return the unique target-completion class when the linear gate is open."""
    if r <= 0:
        raise AssertionError("completion complement must be positive")
    common = gcd(r, REDUCED_STEP)
    if 11 % common:
        return None
    return (-11 * pow(REDUCED_STEP // common, -1, r // common)) % (r // common)


def verify_minimal_completion_classification() -> dict[str, object]:
    """Classify every q=19-containing target factor in the fixed N=p+16 fiber."""
    r_min = RAW_EDGE_Q
    r_old = 13
    if not (
        q137.P_STEP
        == 2**3 * 3**2 * 7 * 19**2 * 31 * 137
        and REDUCED_STEP == 40_669_272
        and REDUCED_STEP == 2**3 * 3**2 * 7 * 19 * 31 * 137
        and gcd(11, REDUCED_STEP) == 1
        and SOURCE_M == 8
        and TARGET_H == 95 == 8 * SOURCE_K - 1
        and r_min % SOURCE_M == 5
        and all(candidate % SOURCE_M != 5 for candidate in range(1, r_min))
        and gcd(r_min, REDUCED_STEP) == 1
        and completion_residue(r_min) == 2
        and r_old % SOURCE_M == 5
        and completion_residue(r_old) == 4
        and completion_residue(21) is None
    ):
        raise AssertionError("minimal q=19 completion classification changed")
    return {
        "candidate_integer": "N(w)=p(w)+16=19*(11+40669272*w)",
        "target_gate": "h=19*r is -1 mod 8 iff r is 5 mod 8",
        "solvability_gate": (
            "19*r divides N(w) iff gcd(r, 40669272) divides 11; "
            "equivalently gcd(r, 40669272)=1"
        ),
        "completion_residue": "w=-11*(40669272)^(-1) mod r",
        "minimal_completion": {"r": r_min, "h": TARGET_H, "w_mod_r": 2},
        "previous_h247_check": {"r": r_old, "h": 247, "w_mod_r": 4},
        "closed_example": {"r": 21, "gcd_with_reduced_step": 21},
    }


def verify_raw_two_atom_control() -> dict[str, object]:
    """Replay the actual raw 5-edge and 19 endpoint at the prime control."""
    certify_prime_control()
    w = SUBRAY_W0
    prime = PRIME_BASE
    R = q137.R0 + q137.R_STEP * w
    chart_h = q137.H0 + q137.H_STEP * w
    chart_M = 26 * chart_h + 1
    chart_K = chart_M * (prime - 3)
    b = (R - 1) // q137.FIRST_LABEL
    Q = (R - b) // RAW_ENDPOINT_Q
    if not (
        w == 27
        and prime == 20_863_336_729
        and Q == RAW_Q_BASE == RAW_EDGE_Q * RAW_Q_TAIL_CONTROL
        and RAW_Q_BASE % (RAW_EDGE_Q**2) != 0
        and is_prime_by_trial(RAW_Q_TAIL_CONTROL)
        and gcd(Q, chart_K * R) == 1
        and R - 1 == q137.FIRST_LABEL * b
        and R - b == RAW_ENDPOINT_Q * Q
        and chart_K % q137.FIRST_LABEL != 0
        and R % q137.FIRST_LABEL == 1
    ):
        raise AssertionError("q=137 two-atom raw control arithmetic changed")

    source = (prime, R * (prime - 1) - prime, prime - 1)
    p_edge = raw.ordered_raw_step(
        modulus=R,
        K=chart_K,
        source=source,
        selected_coordinate_index=0,
        q=prime,
        expected_destination=(1, R - 1, 1),
        name="q137_minimal_completion_universal_p_edge",
    )
    first = raw.ordered_raw_step(
        modulus=R,
        K=chart_K,
        source=(1, R - 1, 1),
        selected_coordinate_index=1,
        q=q137.FIRST_LABEL,
        expected_destination=(b, R - b, 1),
        name="q137_minimal_completion_first_label",
    )
    endpoint, block = factor_blocks.replay_block(
        modulus=R,
        K=chart_K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=[RAW_EDGE_Q, RAW_Q_TAIL_CONTROL],
        endpoint=(RAW_ENDPOINT_Q, R - RAW_ENDPOINT_Q, 1),
        name="q137_minimal_completion_two_atom_block",
    )
    rows = [p_edge, first, *block]
    raw_five = block[0]
    if not (
        endpoint == (RAW_ENDPOINT_Q, R - RAW_ENDPOINT_Q, 1)
        and raw_five["q"] == RAW_EDGE_Q
        and raw_five["selected_q_height"] == 1
        and raw_five["K_q_height"] == 0
        and all(
            row["strict_capacity"]
            and row["unit_condition"]
            and row["gcd_reduction"] == 1
            for row in rows
        )
    ):
        raise AssertionError("q=137 two-atom raw word lost primitivity")
    return {
        "w": w,
        "prime": prime,
        "R": R,
        "Q": Q,
        "raw_word_after_anchor": [q137.FIRST_LABEL, RAW_EDGE_Q, RAW_Q_TAIL_CONTROL],
        "raw_five_occurrence_id": "q137_c19:w=27:137;5;944714543:edge-5",
        "raw_nineteen_occurrence_id": "q137_c19:w=27:137;5;944714543:endpoint-19",
    }


def verify_two_atom_owner_and_normalization() -> dict[str, object]:
    """Verify exact candidate heights and the non-admissible normalization neighbor."""
    raw_control = verify_raw_two_atom_control()
    source_rows: list[dict[str, int]] = []
    for parameter in (0, 1, 17):
        w = SUBRAY_W0 + SUBRAY_W_STEP * parameter
        prime = PRIME_BASE + PRIME_STEP * parameter
        N = prime + 4 * SOURCE_A * SOURCE_D
        cofactor = N // TARGET_H
        B = (SOURCE_K * prime + SOURCE_A) // TARGET_H
        gap = (SOURCE_A + B) // SOURCE_K
        x = SOURCE_A * B * SOURCE_C
        d = SOURCE_A**2 * SOURCE_C
        y = prime * SOURCE_A * SOURCE_C * SOURCE_K
        z = prime * B * SOURCE_C * SOURCE_K
        normal_B = B // NORMAL_GCD
        if not (
            w == SUBRAY_W0 + SUBRAY_W_STEP * parameter
            and prime == q137.P0 + q137.P_STEP * w
            and N == TARGET_H * cofactor
            and cofactor
            == COFACTOR_BASE + COFACTOR_STEP * parameter
            and cofactor % RAW_EDGE_Q == 1
            and cofactor % RAW_ENDPOINT_Q == 6
            and valuation(N, RAW_EDGE_Q) == valuation(N, RAW_ENDPOINT_Q) == 1
            and TARGET_H * B == SOURCE_K * prime + SOURCE_A
            and B == 12 * cofactor - 2
            and B % NORMAL_GCD == 0
            and gap == cofactor
            and 3 <= gap <= prime - 2
            and x == NORMAL_A * normal_B * NORMAL_C
            and d == NORMAL_A**2 * NORMAL_C == 4
            and (x + d) % gap == 0
            and x * x % d == 0
            and 4 * x * y * z == prime * (x * y + x * z + y * z)
            and gcd(SOURCE_A, B) == NORMAL_GCD
            and TARGET_H == 4 * NORMAL_A * NORMAL_C * NORMAL_K - 1
            and TARGET_H * normal_B == NORMAL_K * prime + NORMAL_A
        ):
            raise AssertionError("minimal two-atom terminal or normalization changed")
        source_rows.append(
            {
                "u": parameter,
                "w": w,
                "prime": prime,
                "N": N,
                "cofactor": cofactor,
                "B": B,
                "x": x,
                "d": d,
                "y": y,
                "z": z,
            }
        )

    q19_block = {pow(RAW_ENDPOINT_Q, exponent, SOURCE_M) for exponent in range(2)}
    q5_block = {pow(RAW_EDGE_Q, exponent, SOURCE_M) for exponent in range(2)}
    product_block = {
        left * right % SOURCE_M for left in q19_block for right in q5_block
    }
    raw_q_base = RAW_Q_BASE // RAW_EDGE_Q
    if not (
        SOURCE_D == 2
        and SOURCE_M == 8
        and NORMAL_D == 4
        and NORMAL_M == 16 == NORMAL_GCD * SOURCE_M
        and SOURCE_A * SOURCE_D == NORMAL_A * NORMAL_D == 4
        and TARGET_H + 1 == SOURCE_M * SOURCE_K == NORMAL_M * NORMAL_K
        and NORMAL_C == 4
        and NORMAL_C % (2**2) == 0
        and raw_q_base % RAW_EDGE_Q == 3
        and RAW_Q_STEP // RAW_EDGE_Q % RAW_EDGE_Q == 0
        and (q137.R0 + q137.R_STEP * SUBRAY_W0) % RAW_EDGE_Q == 4
        and q137.R_STEP * SUBRAY_W_STEP % RAW_EDGE_Q == 0
        and q19_block == {1, 3}
        and q5_block == {1, 5}
        and product_block == {1, 3, 5, 7}
    ):
        raise AssertionError("two-atom fiber ownership data changed")
    return {
        "parameter_subray": {
            "w": "27+25*u",
            "p": [PRIME_BASE, PRIME_STEP],
            "N": [PRIME_BASE + 16, PRIME_STEP],
            "N_over_95": [COFACTOR_BASE, COFACTOR_STEP],
            "Dirichlet_progression_gcd": gcd(PRIME_BASE, PRIME_STEP),
        },
        "raw_status": (
            "Every prime parameter inherits the q=137 raw receipt; Q is exactly "
            "divisible by 5, so 137;5;Fac(Q/5) is available."
        ),
        "two_atom_owner_map": {
            "domain_atoms": [
                {
                    "raw_occurrence_id": raw_control["raw_five_occurrence_id"],
                    "q": RAW_EDGE_Q,
                    "layer": 1,
                    "kind": "actual_raw_edge",
                },
                {
                    "raw_occurrence_id": raw_control["raw_nineteen_occurrence_id"],
                    "q": RAW_ENDPOINT_Q,
                    "layer": 1,
                    "kind": "actual_raw_endpoint",
                },
            ],
            "codomain_tokens": [
                {"fiber": [SOURCE_D, SOURCE_A], "q": RAW_EDGE_Q, "layer": 1},
                {
                    "fiber": [SOURCE_D, SOURCE_A],
                    "q": RAW_ENDPOINT_Q,
                    "layer": 1,
                },
            ],
            "injection": "distinct raw q labels map to distinct exact candidate q layers",
        },
        "target_product": {
            "h": TARGET_H,
            "source_factors": [RAW_ENDPOINT_Q, RAW_EDGE_Q],
            "residue_blocks_mod_8": {
                "q19": sorted(q19_block),
                "q5": sorted(q5_block),
                "product": sorted(product_block),
            },
        },
        "normalization_neighbor": {
            "unnormalized": {
                "A": SOURCE_A,
                "C": SOURCE_C,
                "K": SOURCE_K,
                "D": SOURCE_D,
                "M": SOURCE_M,
            },
            "normalized": {
                "A": NORMAL_A,
                "C": NORMAL_C,
                "K": NORMAL_K,
                "D": NORMAL_D,
                "M": NORMAL_M,
            },
            "invariants": ["p+4*A*D", "h", "m", "x", "d", "Type-II identity"],
            "source_switch_boundary": (
                "The normalized quotient C=4 is not squarefree, so this is a "
                "normal-form neighbor rather than an admissible source-switch fiber."
            ),
        },
        "controls": source_rows,
    }


def build_result() -> dict[str, object]:
    """Build the minimal completion classification and its actual raw control."""
    return {
        "certificate_type": "q137_raw_c19_minimal_two_atom_completion_v1",
        "classification": verify_minimal_completion_classification(),
        "owner_and_normalization": verify_two_atom_owner_and_normalization(),
        "not_established": [
            "an F/G fixed-layer state or canonical Fourier role",
            "a typed Fourier/source demand",
            "a Hall request, demand-to-slot injection, or q-adic capacity price",
            "an admissible normalized source-switch fiber, descent edge, or selector edge",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=137 raw C=19 minimal two-atom target completion and normalization neighbor")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
