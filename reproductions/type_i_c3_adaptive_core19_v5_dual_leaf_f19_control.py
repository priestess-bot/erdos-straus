#!/usr/bin/env python3
"""Verify the first prime adaptive core-19 dual-leaf and q=19 control.

This is a single terminal-preempted control point.  It proves a same-source
raw tree, a two-row carry computation, and a normalized 19-primary Fourier
mode on the trivial centered fixed layer.  It does not register a root or a
recursive selector edge.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt

import type_i_c3_adaptive_divisor_factor_block_normal_form as adaptive
import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_high_r_chart_two_anchor as shared
import type_i_ordered_raw_lineage_normalized_phase_rigidity as lineage
import type_i_raw_transcript_persistent_carry_core as carry


V = 5
H = 50_099_038_185
P = 1_202_376_916_441
R = 5_210_299_971_231
M0 = 1_302_574_992_811
C0 = P - 3
K = 1_566_186_103_285_340_197_727_218
B = 1_042_059_994_246
A = 595_462_853_855
GAMMA = 576_854_639_672
C1 = 19
M1 = K // C1
N1 = 329_723_390_160_124_478_497_657

SOURCE = (P, R * (P - 1) - P, P - 1)
COMMON = (
    (0, P, (1, R - 1, 1), "universal_p"),
    (1, 5, (B, R - B, 1), "shared_five"),
)
C1_SUFFIX = (
    (0, 92_660_501, (11_246, 5_210_299_959_985, 1), "c1_92660501"),
    (1, 5, (1_042_059_991_997, 4_168_239_979_234, 1), "c1_five_a"),
    (1, 10_798_549_169, (386, 5_210_299_970_845, 1), "c1_10798549169"),
    (1, 5, (1_042_059_994_169, 4_168_239_977_062, 1), "c1_five_b"),
    (0, 54_845_262_851, (19, R - 19, 1), "c1_54845262851"),
)

K_FACTORS = (
    (2, 1),
    (19, 2),
    (193, 1),
    (5_351, 1),
    (66_383, 1),
    (31_641_497_801, 1),
)
ETA_PHASES = (9, 11, 9, 3, 13, 2)
TALL_FACTOR = 31_641_497_801
F_WITNESS_EXPONENT = 105_942_250_765


def pocklington_certificate(
    *,
    value: int,
    proved_factor: int,
    proved_prime_divisors: tuple[int, ...],
) -> None:
    """Replay a one-base Pocklington certificate for a focused prime."""
    if value <= 2 or (value - 1) % proved_factor or proved_factor <= isqrt(value):
        raise AssertionError("Pocklington size or divisibility condition failed")
    for prime in proved_prime_divisors:
        if not shared.is_prime(prime) or proved_factor % prime:
            raise AssertionError("Pocklington factor was not completely certified")
        if pow(2, value - 1, value) != 1:
            raise AssertionError("Pocklington Fermat condition failed")
        if gcd(pow(2, (value - 1) // prime, value) - 1, value) != 1:
            raise AssertionError("Pocklington gcd condition failed")


def replay_word(
    specs: tuple[tuple[int, int, tuple[int, int, int], str], ...],
) -> list[dict[str, object]]:
    """Replay one declared raw word from the universal source."""
    current = SOURCE
    rows: list[dict[str, object]] = []
    for side, prime, destination, name in specs:
        row = raw.ordered_raw_step(
            modulus=R,
            K=K,
            source=current,
            selected_coordinate_index=side,
            q=prime,
            expected_destination=destination,
            name=name,
        )
        if not (
            row["strict_capacity"]
            and row["unit_condition"]
            and row["gcd_reduction"] == 1
        ):
            raise AssertionError("declared raw word lost a primitive raw condition")
        rows.append(row)
        current = destination
    return rows


def c0_specs(rows: list[dict[str, object]]) -> tuple[tuple[int, int, tuple[int, int, int], str], ...]:
    """Convert the existing adaptive C0 replay into lineage input."""
    return tuple(
        (
            int(row["selected_coordinate_index"]),
            int(row["q"]),
            tuple(int(value) for value in row["destination"]),
            str(row["name"]),
        )
        for row in rows
    )


def verify_prime_point() -> dict[str, object]:
    """Verify the first prime parameter by a short Pocklington chain."""
    if (H, P, R) != (35 * 1_431_401_091, 840 * 1_431_401_091 + 1, 104 * H - 9):
        raise AssertionError("adaptive v=5 parameter arithmetic changed")
    if not (P % 24 == 1 and P == 181_740_263_041 + 204_127_330_680 * V):
        raise AssertionError("adaptive v=5 did not remain on the stated ray")

    pocklington_certificate(
        value=477_133_697,
        proved_factor=286_739,
        proved_prime_divisors=(17, 101, 167),
    )
    pocklington_certificate(
        value=P,
        proved_factor=477_133_697,
        proved_prime_divisors=(477_133_697,),
    )
    if not shared.is_prime(P):
        raise AssertionError("Pocklington prime point failed independent replay")
    if P - 1 != 2**3 * 3**2 * 5 * 7 * 477_133_697:
        raise AssertionError("outer Pocklington factorization changed")
    if 477_133_697 - 1 != 2**7 * 13 * 17 * 101 * 167:
        raise AssertionError("inner Pocklington factorization changed")
    return {
        "v": V,
        "h": H,
        "p": P,
        "R": R,
        "pocklington": "2-base focused chain",
    }


def verify_raw_tree() -> dict[str, object]:
    """Replay two leaves and preserve their coordinate-frame distinction."""
    parameters = adaptive.c3_parameters(h=H, a=A, b=B)
    if parameters != {
        "h": H,
        "p": P,
        "R": R,
        "M": M0,
        "x": C0,
        "K": K,
        "S": (R - 1) // 2,
        "a": A,
        "b": B,
        "alpha": 5,
        "beta": 7,
        "gamma": GAMMA,
    }:
        raise AssertionError("adaptive C0 parameters changed")
    c0_rows = adaptive.replay_positive_control(parameters)
    c1_rows = replay_word(COMMON + C1_SUFFIX)
    p_edge_fields = {
        key: value for key, value in c0_rows[0].items() if key != "name"
    }
    if p_edge_fields != {
        key: value for key, value in c1_rows[0].items() if key != "name"
    }:
        raise AssertionError("the universal p edge is no longer common")
    c0_first_five = c0_rows[1]
    c1_first_five = c1_rows[1]
    if not (
        c0_first_five["source"] == [R - 1, 1, 1]
        and c1_first_five["source"] == [1, R - 1, 1]
        and c0_first_five["selected_coordinate_index"] == 0
        and c1_first_five["selected_coordinate_index"] == 1
        and c0_first_five["q"] == c1_first_five["q"] == 5
        and c0_first_five["destination"] == c1_first_five["destination"]
    ):
        raise AssertionError("the frame-equivalent first five moves changed")
    if c0_rows[-1]["destination"] != [C0, R - C0, 1]:
        raise AssertionError("adaptive C0 word reached the wrong leaf")
    if c1_rows[-1]["destination"] != [C1, R - C1, 1]:
        raise AssertionError("adaptive C1 word reached the wrong leaf")

    c1_trace = lineage.trace_lineage(
        modulus=R,
        carrier=K,
        source=SOURCE,
        source_coordinate_index=0,
        specs=COMMON + C1_SUFFIX,
    )
    if c1_trace["coordinates"][-1] != C1 or c1_trace["phases"][-1] != (-N1) % R:
        raise AssertionError("adaptive C1 physical lineage phase changed")

    c0_tail = lineage.verify_physical_tail(
        prime=P,
        modulus=R,
        carrier=M0,
        cofactor=C0,
        tail=1,
        orientation=-1,
        coordinate=R - C0,
        expected_phase=13,
    )
    c1_tail = lineage.verify_physical_tail(
        prime=P,
        modulus=R,
        carrier=M1,
        cofactor=C1,
        tail=1,
        orientation=1,
        coordinate=C1,
        expected_phase=(-N1) % R,
    )
    return {
        "common_ordered_raw_prefix_length": 1,
        "frame_equivalent_orbit_prefix": {
            "coordinate_frame_swap": [[1, R - 1, 1], [R - 1, 1, 1]],
            "first_five_destinations_agree": True,
            "warning": (
                "The two q=5 moves are not one shared ordered raw edge; "
                "the C0 move uses an explicit coordinate-frame swap."
            ),
        },
        "C0_raw_step_count": len(c0_rows),
        "C1_raw_step_count": len(c1_rows),
        "C1_lineage": c1_trace,
        "physical_tails": {"C0": c0_tail, "C1": c1_tail},
    }


def verify_two_row_carry() -> dict[str, object]:
    """Check the same-chart determinant pair and its exact carry core."""
    rows = [
        {"p": P, "A": 19, "M": M0, "C": C0, "d": 3, "n": 13},
        {"p": P, "A": 19, "M": M1, "C": C1, "d": P - C1, "n": N1},
    ]
    for row in rows:
        carry.verify_overflow_row(row)
        if not carry.e2_passes(A=19, C=int(row["C"]), M=int(row["M"]), p=P):
            raise AssertionError("A=19 E2 condition failed")
    if carry.persistent_carry_core(rows=rows, e2_indices={0, 1}) != 19:
        raise AssertionError("adaptive dual-leaf carry core changed")
    return {
        "rows": [{**row, "r": int(row["M"]) % P} for row in rows],
        "carry_core_for_T_equals_I_equals_0_1": 19,
    }


def centered_box_residues() -> set[int]:
    """Enumerate the 1215-point centered Type-I exponent box only."""
    residues: set[int] = set()
    for vector in product(*(range(-exponent, exponent + 1) for _prime, exponent in K_FACTORS)):
        residue = 1
        for (prime, _exponent), coordinate in zip(K_FACTORS, vector):
            residue = residue * pow(prime, coordinate, R) % R
        residues.add(residue)
    return residues


def verify_q19_fixed_layer() -> dict[str, object]:
    """Build the normalized q=19 mode on J=C_R(1)={1}."""
    if shared.factorization(K) != list(K_FACTORS):
        raise AssertionError("adaptive K factorization changed")
    residues = centered_box_residues()
    if len(residues) != 1_215 or R - 1 in residues:
        raise AssertionError("the focused point is no longer an F-type box miss")
    if pow(TALL_FACTOR, F_WITNESS_EXPONENT, R) != R - 1:
        raise AssertionError("explicit unbounded F witness changed")

    conductor = 191
    zeta = 150
    if R % conductor or K % conductor != 48 or pow(48, 10, conductor) != zeta:
        raise AssertionError("q=19 support-visibility congruence changed")
    if pow(zeta, 19, conductor) != 1 or zeta == 1:
        raise AssertionError("normalized q=19 root lost exact order")
    phase_table = {pow(zeta, exponent, conductor): exponent for exponent in range(19)}
    if len(phase_table) != 19:
        raise AssertionError("q=19 phase table is not cyclic")
    for (prime, exponent), phase in zip(K_FACTORS, ETA_PHASES):
        if pow(prime, 10, conductor) != pow(zeta, phase, conductor):
            raise AssertionError("q=19 support phase changed")
        if phase == 0 or (2 * exponent + 1) * phase % 19 == 0:
            raise AssertionError("q=19 Dirichlet block unexpectedly vanished")
    if sum(exponent * phase for (_prime, exponent), phase in zip(K_FACTORS, ETA_PHASES)) % 19 != 1:
        raise AssertionError("q=19 phase of K changed")

    # The singleton centered layer has trivial stabilizer, so the character
    # necessarily descends unchanged to its fixed-layer quotient.
    return {
        "fiber": {
            "classification": "F",
            "fixed_layer_N": 1,
            "J": [1],
            "stabilizer_P": [1],
            "centered_box_size": 1_215,
            "distinct_centered_residues": len(residues),
            "target_in_centered_box": False,
            "explicit_unbounded_witness": [0, 0, 0, 0, 0, F_WITNESS_EXPONENT],
        },
        "q19_mode": {
            "conductor": conductor,
            "normalization": "eta(a)=a^10 mod 191; zeta=150",
            "eta_K": zeta,
            "phase_vector": list(ETA_PHASES),
            "character_order": 19,
            "stabilizer_survival": True,
            "target_phase": 0,
            "target_even": True,
        },
    }


def verify_terminal_first() -> dict[str, object]:
    """Record the direct Type II certificate that preempts this control point."""
    gap, divisor = 3, 11
    x = (P + gap) // 4
    if x != 300_594_229_111 or x % divisor or divisor > x or (x + divisor) % gap:
        raise AssertionError("adaptive v=5 terminal predicate changed")
    y = P * (x + divisor) // gap
    z = P * (x + x * x // divisor) // gap
    if (y, z) != (
        120_475_854_103_889_934_264_934,
        3_292_213_317_349_827_317_887_300_015_390_334,
    ):
        raise AssertionError("adaptive v=5 terminal denominators changed")
    if 4 * x * y * z != P * (y * z + x * z + x * y):
        raise AssertionError("adaptive v=5 Type II identity changed")
    return {"gap": gap, "divisor": divisor, "denominators": [x, y, z]}


def build_result() -> dict[str, object]:
    """Build the terminal-preempted dual-leaf/Fourier control receipt."""
    if P * R + 1 != 4 * K or K != M0 * C0 or K != M1 * C1:
        raise AssertionError("adaptive v=5 Type I chart changed")
    return {
        "certificate_type": "c3_adaptive_core19_v5_dual_leaf_f19_control_v1",
        "scope": (
            "A terminal-preempted same-source dual-leaf and q=19 fixed-layer control. "
            "It does not create an odd/mixed root-entry adapter, a phase bridge, or a selector edge."
        ),
        "prime_point": verify_prime_point(),
        "raw_tree": verify_raw_tree(),
        "two_row_carry": verify_two_row_carry(),
        "fixed_layer_q19": verify_q19_fixed_layer(),
        "terminal_first": verify_terminal_first(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified adaptive core-19 v=5 dual-leaf q=19 F control")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
