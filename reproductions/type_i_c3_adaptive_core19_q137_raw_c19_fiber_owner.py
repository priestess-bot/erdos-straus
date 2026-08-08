#!/usr/bin/env python3
"""Verify an actual q=137 raw C=19 atom in one Type-II target fiber.

The fixture closes only the arithmetic raw-to-owner half for one raw atom.  It
does not manufacture a Fourier demand, a Hall request, a capacity price, or a
selector edge.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt

import type_i_c3_adaptive_core19_q137_first_entry_family as q137
import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks


RAW_Q = 19
SOURCE_Q = 13
TARGET_H = RAW_Q * SOURCE_Q
FIBER_D = 2
FIBER_A = 2
FIBER_C = 1
FIBER_M = 4 * FIBER_D
NORMAL_K = (TARGET_H + 1) // FIBER_M
SUBRAY_W0 = 4
SUBRAY_W_STEP = SOURCE_Q
CONTROL_T = 2
CONTROL_W = 30
CONTROL_P = 23_181_485_233
CONTROL_Q = 5_248_414_123


def valuation(value: int, prime: int) -> int:
    """Return the focused positive p-adic valuation."""
    if value <= 0:
        raise AssertionError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def is_prime_by_trial(value: int) -> bool:
    """Certify the small fixed labels used by this one control."""
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


def certify_control_prime() -> None:
    """Use a complete Pocklington certificate for the focused prime control."""
    factors = ((2, 4), (3, 1), (71, 1), (409, 1), (16_631, 1))
    proved_factor = 1
    for prime, exponent in factors:
        if not is_prime_by_trial(prime):
            raise AssertionError("Pocklington factor lost primality")
        proved_factor *= prime**exponent
    if not (
        CONTROL_P - 1 == proved_factor
        and proved_factor > isqrt(CONTROL_P)
        and pow(5, CONTROL_P - 1, CONTROL_P) == 1
        and all(
            gcd(pow(5, (CONTROL_P - 1) // prime, CONTROL_P) - 1, CONTROL_P) == 1
            for prime, _exponent in factors
        )
    ):
        raise AssertionError("Pocklington control for the raw/fiber point changed")


def verify_subray() -> dict[str, int]:
    """Construct the raw-compatible target-factor progression."""
    prime_base = q137.P0 + q137.P_STEP * SUBRAY_W0
    prime_step = q137.P_STEP * SUBRAY_W_STEP
    cofactor_base = prime_base + FIBER_A * FIBER_M
    cofactor_step = prime_step
    if not (
        q137.P_STEP
        == 2**3 * 3**2 * 7 * 19**2 * 31 * 137
        and TARGET_H == 247
        and TARGET_H % FIBER_M == FIBER_M - 1
        and NORMAL_K == 31
        and prime_base == 3_090_864_865
        and prime_step == 10_045_310_184
        and cofactor_base == 3_090_864_881 == TARGET_H * 12_513_623
        and cofactor_step == TARGET_H * 40_669_272
        and gcd(prime_base, prime_step) == 1
        and prime_base % 24 == 1
        and prime_step % 24 == 0
        and q137.P0 % RAW_Q == 3
        and q137.P_STEP % RAW_Q == 0
        and valuation(cofactor_base, RAW_Q) == 1
        and valuation(cofactor_step, RAW_Q) >= 2
    ):
        raise AssertionError("q=137 C=19 target-factor subray changed")
    return {
        "prime_base": prime_base,
        "prime_step": prime_step,
        "cofactor_base": cofactor_base,
        "cofactor_step": cofactor_step,
    }


def verify_actual_raw_control() -> dict[str, object]:
    """Replay one actual primitive word at the source-owner control point."""
    certify_control_prime()
    subray = verify_subray()
    w = SUBRAY_W0 + SUBRAY_W_STEP * CONTROL_T
    prime = q137.P0 + q137.P_STEP * w
    R = q137.R0 + q137.R_STEP * w
    chart_h = q137.H0 + q137.H_STEP * w
    chart_M = 26 * chart_h + 1
    chart_K = chart_M * (prime - 3)
    b = (R - 1) // q137.FIRST_LABEL
    Q = (R - b) // RAW_Q
    if not (
        w == CONTROL_W
        and prime == CONTROL_P == subray["prime_base"] + subray["prime_step"] * CONTROL_T
        and Q == CONTROL_Q
        and is_prime_by_trial(Q)
        and R - 1 == q137.FIRST_LABEL * b
        and R - b == RAW_Q * Q
        and gcd(Q, chart_K * R) == 1
        and chart_K % q137.FIRST_LABEL != 0
        and R % q137.FIRST_LABEL == 1
    ):
        raise AssertionError("q=137 raw control arithmetic changed")

    source = (prime, R * (prime - 1) - prime, prime - 1)
    p_edge = raw.ordered_raw_step(
        modulus=R,
        K=chart_K,
        source=source,
        selected_coordinate_index=0,
        q=prime,
        expected_destination=(1, R - 1, 1),
        name="q137_c19_owner_universal_p_edge",
    )
    first = raw.ordered_raw_step(
        modulus=R,
        K=chart_K,
        source=(1, R - 1, 1),
        selected_coordinate_index=1,
        q=q137.FIRST_LABEL,
        expected_destination=(b, R - b, 1),
        name="q137_c19_owner_first_label",
    )
    endpoint, block = factor_blocks.replay_block(
        modulus=R,
        K=chart_K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=[Q],
        endpoint=(RAW_Q, R - RAW_Q, 1),
        name="q137_c19_owner_raw_block",
    )
    rows = [p_edge, first, *block]
    if not (
        endpoint == (RAW_Q, R - RAW_Q, 1)
        and all(
            row["strict_capacity"]
            and row["unit_condition"]
            and row["gcd_reduction"] == 1
            for row in rows
        )
    ):
        raise AssertionError("q=137 C=19 raw word lost primitivity")
    return {
        "w": w,
        "prime": prime,
        "R": R,
        "raw_endpoint": RAW_Q,
        "raw_word_after_anchor": [q137.FIRST_LABEL, Q],
        "raw_occurrence_id": "q137_c19:w=30:137;5248414123",
    }


def verify_fiber_owner() -> dict[str, object]:
    """Bind the raw q=19 atom to the same fiber as a direct target product."""
    raw_control = verify_actual_raw_control()
    prime = int(raw_control["prime"])
    N = prime + FIBER_A * FIBER_M
    B = (NORMAL_K * prime + FIBER_A) // TARGET_H
    gap = (FIBER_A + B) // NORMAL_K
    x = FIBER_A * B * FIBER_C
    d = FIBER_A**2 * FIBER_C
    y = prime * FIBER_A * FIBER_C * NORMAL_K
    z = prime * B * FIBER_C * NORMAL_K
    q19_block = {pow(RAW_Q, exponent, FIBER_M) for exponent in range(2)}
    q13_block = {pow(SOURCE_Q, exponent, FIBER_M) for exponent in range(2)}
    product_block = {
        left * right % FIBER_M for left in q19_block for right in q13_block
    }
    factorization = ((13, 1), (19, 1), (23, 1), (83, 1), (211, 1), (233, 1))
    factor_product = 1
    for factor, exponent in factorization:
        if not is_prime_by_trial(factor):
            raise AssertionError("focused N factor lost primality")
        factor_product *= factor**exponent
    if not (
        FIBER_D == FIBER_A * FIBER_C == 2
        and FIBER_M == 8
        and FIBER_D % FIBER_A == 0
        and FIBER_D // FIBER_A == FIBER_C == 1
        and FIBER_A * FIBER_M < prime
        and N == 23_181_485_249 == factor_product
        and N == prime + 4 * FIBER_A**2 * FIBER_C
        and N % RAW_Q == N % SOURCE_Q == N % TARGET_H == 0
        and gcd(RAW_Q * SOURCE_Q, FIBER_M) == 1
        and valuation(N, RAW_Q) == 1
        and TARGET_H == 4 * FIBER_A * FIBER_C * NORMAL_K - 1
        and TARGET_H % FIBER_M == FIBER_M - 1
        and (NORMAL_K * prime + FIBER_A) % TARGET_H == 0
        and B == 2_909_417_175
        and B > FIBER_A
        and gcd(FIBER_A, B) == 1
        and (FIBER_A + B) % NORMAL_K == 0
        and gap == N // TARGET_H == 93_852_167
        and x == 5_818_834_350
        and d == 4
        and x * x % d == 0
        and (x + d) % gap == 0
        and 4 * x * y * z == prime * (x * y + x * z + y * z)
        and q19_block == {1, 3}
        and q13_block == {1, 5}
        and product_block == {1, 3, 5, 7}
    ):
        raise AssertionError("raw C=19 owner fiber or terminal changed")
    return {
        "fiber": {
            "D": FIBER_D,
            "a": FIBER_A,
            "c": FIBER_C,
            "M": FIBER_M,
            "N": N,
        },
        "raw_owner_map": {
            "domain_atom": {
                "raw_occurrence_id": raw_control["raw_occurrence_id"],
                "q": RAW_Q,
                "layer": 1,
            },
            "codomain_token": {
                "fiber": [FIBER_D, FIBER_A],
                "q": RAW_Q,
                "layer": 1,
                "source_factor": RAW_Q,
            },
            "injection": "singleton actual raw atom to singleton candidate q-layer",
            "arithmetic_basis": "19 divides both the raw endpoint and N=p+16 exactly once",
        },
        "same_fiber_target_product": {
            "source_factors": [RAW_Q, SOURCE_Q],
            "target_factor": TARGET_H,
            "target_residue_mod_M": TARGET_H % FIBER_M,
            "residue_blocks": {
                "q19": sorted(q19_block),
                "q13": sorted(q13_block),
                "product": sorted(product_block),
            },
        },
        "type_ii_terminal": {
            "A": FIBER_A,
            "B": B,
            "C": FIBER_C,
            "K": NORMAL_K,
            "h": TARGET_H,
            "gap": gap,
            "x": x,
            "d": d,
            "denominators": [x, y, z],
        },
    }


def verify_standalone_q19_obstruction() -> dict[str, object]:
    """Show that the raw q=19 cannot itself be the complete normal-form factor."""
    triples = ((1, 1, 5), (1, 5, 1), (5, 1, 1))
    residues = {
        (A, C, K): (K * q137.P0 + A) % RAW_Q for A, C, K in triples
    }
    if not (
        q137.P0 % RAW_Q == 3
        and q137.P_STEP % RAW_Q == 0
        and all(4 * A * C * K - 1 == RAW_Q for A, C, K in triples)
        and residues == {(1, 1, 5): 16, (1, 5, 1): 4, (5, 1, 1): 8}
        and all(residue != 0 for residue in residues.values())
    ):
        raise AssertionError("standalone q=19 normal-form obstruction changed")
    return {
        "raw_family_residue": "p(w)=3 mod 19",
        "ACK_equals_5_triples": [list(triple) for triple in triples],
        "Kp_plus_A_residues_mod_19": {
            ",".join(str(value) for value in triple): residue
            for triple, residue in residues.items()
        },
        "conclusion": "19 cannot be the whole Type-II normal-form target factor on this raw family",
    }


def build_result() -> dict[str, object]:
    """Build one actual raw-to-owner and same-fiber terminal control."""
    return {
        "certificate_type": "q137_raw_c19_same_fiber_owner_v1",
        "status": "terminal_preempted_actual_raw_owner_control",
        "subray": verify_subray(),
        "actual_raw_control": verify_actual_raw_control(),
        "raw_owner_and_terminal": verify_fiber_owner(),
        "standalone_q19_obstruction": verify_standalone_q19_obstruction(),
        "not_established": [
            "a Fourier or source-rank demand for the q=19 atom",
            "a Hall request-to-token or demand-to-slot injection",
            "a q=19 Kneser or stabilizer price",
            "a selector edge or a universal raw-to-owner functor",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=137 raw C=19 same-fiber owner and Type-II terminal")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
