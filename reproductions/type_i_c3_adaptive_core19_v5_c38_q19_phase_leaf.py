#!/usr/bin/env python3
"""Verify the third v=5 primitive raw leaf and its q=19 phase boundary."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt, lcm

import type_i_c3_adaptive_core19_v5_d6303_fiber_catalog as catalog
import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_adaptive_core19_v5_q19_phase_compatible_fiber as candidate
import type_i_ordered_raw_lineage_normalized_phase_rigidity as lineage
import type_i_raw_transcript_persistent_carry_core as carry


C2 = 38
T2 = 137_067_755_324
Z2 = 5_208_574_702_312
M2 = v5.K // C2
D2 = v5.P - C2
N2 = 4 * M2 - v5.R
MU2 = 5_050_926_882_929
H_BASE = 194_563
H3 = H_BASE * 19**3
C38_SUFFIX = (
    (1, 5_623, (926_605_010, 5_209_373_366_221, 1), "c38_5623"),
    (1, 6_961, (748_365_661, 5_209_551_605_570, 1), "c38_6961"),
    (1, 3_041, (1_713_104_770, 5_208_586_866_461, 1), "c38_3041"),
    (1, 3_019, (1_725_268_919, 5_208_574_702_312, 1), "c38_3019"),
)
C38_SPECS = (v5.COMMON[0],) + C38_SUFFIX


def valuation(value: int, prime: int) -> int:
    """Return the exact valuation of one positive focused control value."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def is_small_prime(value: int) -> bool:
    """Certify the four small raw labels by deterministic trial division."""
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


def one_base_pocklington(value: int, prime_divisors: tuple[int, ...]) -> None:
    """Check a focused one-base Pocklington certificate."""
    if pow(2, value - 1, value) != 1:
        raise AssertionError("Pocklington Fermat condition changed")
    for prime in prime_divisors:
        if gcd(pow(2, (value - 1) // prime, value) - 1, value) != 1:
            raise AssertionError("Pocklington gcd condition changed")


def verify_prime_label_p() -> None:
    """Avoid repeated sqrt(P) trial division while certifying the p raw label."""
    q = 477_133_697
    inner_proved_factor = 286_739
    if not (
        v5.P - 1 == 2**3 * 3**2 * 5 * 7 * q
        and q - 1 == 2**7 * 13 * 17 * 101 * 167
        and all(is_small_prime(value) for value in (2, 3, 5, 7, 13, 17, 101, 167))
        and inner_proved_factor == 17 * 101 * 167
        and (q - 1) % inner_proved_factor == 0
        and inner_proved_factor > isqrt(q)
        and q > isqrt(v5.P)
    ):
        raise AssertionError("focused Pocklington factor data changed")
    one_base_pocklington(q, (17, 101, 167))
    one_base_pocklington(v5.P, (q,))


def is_prime_label(value: int) -> bool:
    """Use the Pocklington label proof for p and trial division for small labels."""
    return value == v5.P or is_small_prime(value)


def replay_raw_step(
    *,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    expected_destination: tuple[int, int, int],
    name: str,
) -> dict[str, object]:
    """Replay one raw step without recomputing the known p trial factorization."""
    left, right, layer = source
    if (
        selected_coordinate_index not in (0, 1)
        or min(left, right, layer) <= 0
        or left + right != v5.R * layer
        or gcd(left, right) != 1
    ):
        raise AssertionError(f"{name}: invalid primitive source")
    selected, other = (
        (left, right) if selected_coordinate_index == 0 else (right, left)
    )
    shift = (-layer) % q
    selected_height = valuation(selected, q)
    carrier_height = valuation(v5.K, q)
    unit_condition = gcd(q, v5.R * layer * other) == 1
    if not (
        is_prime_label(q)
        and selected % q == 0
        and selected_height > carrier_height
        and 1 <= shift < q
        and unit_condition
    ):
        raise AssertionError(f"{name}: raw primality, capacity, or unit condition changed")
    selected_after_division = selected // q
    other_after_shift = (other + v5.R * shift) // q
    layer_after_shift = (layer + shift) // q
    reduction = gcd(selected_after_division, other_after_shift)
    destination = (
        selected_after_division // reduction,
        other_after_shift // reduction,
        layer_after_shift // reduction,
    )
    if not (
        (other + v5.R * shift) % q == 0
        and (layer + shift) % q == 0
        and reduction > 0
        and layer_after_shift % reduction == 0
        and destination == expected_destination
        and min(destination) > 0
        and gcd(destination[0], destination[1]) == 1
        and destination[0] + destination[1] == v5.R * destination[2]
    ):
        raise AssertionError(f"{name}: raw arithmetic or destination changed")
    return {
        "name": name,
        "source": source,
        "selected_coordinate_index": selected_coordinate_index,
        "selected_coordinate": selected,
        "q": q,
        "shift": shift,
        "selected_q_height": selected_height,
        "K_q_height": carrier_height,
        "strict_capacity": selected_height > carrier_height,
        "unit_condition": unit_condition,
        "gcd_reduction": reduction,
        "destination": destination,
    }


def replay_c38_word() -> list[dict[str, object]]:
    """Replay the declared receipt after one focused proof of the p label."""
    verify_prime_label_p()
    current = v5.SOURCE
    rows: list[dict[str, object]] = []
    for selected_index, q, destination, name in C38_SPECS:
        row = replay_raw_step(
            source=current,
            selected_coordinate_index=selected_index,
            q=q,
            expected_destination=destination,
            name=name,
        )
        rows.append(row)
        current = destination
    return rows


def replay_c38_lineage() -> dict[str, object]:
    """Transport the universal source's second coordinate through the receipt."""
    rows = replay_c38_word()
    lineage_index = 1
    coordinates = [v5.SOURCE[lineage_index]]
    products = [1]
    phases = [-pow(coordinates[0], -1, v5.R) % v5.R]
    for row in rows:
        selected_index = int(row["selected_coordinate_index"])
        destination = tuple(int(value) for value in row["destination"])
        next_index = 0 if lineage_index == selected_index else 1
        next_coordinate = destination[next_index]
        token = int(row["q"]) * int(row["gcd_reduction"])
        if token * next_coordinate % v5.R != coordinates[-1] % v5.R:
            raise AssertionError("C=38 tracked-coordinate transport changed")
        products.append(products[-1] * token % v5.R)
        phases.append(-pow(next_coordinate, -1, v5.R) % v5.R)
        if phases[-1] != products[-1] * phases[0] % v5.R:
            raise AssertionError("C=38 normalized phase transport changed")
        coordinates.append(next_coordinate)
        lineage_index = next_index
    return {
        "rows": rows,
        "coordinates": coordinates,
        "products": products,
        "phases": phases,
        "final_coordinate_index": lineage_index,
    }


def all_primitive(rows: list[dict[str, object]]) -> bool:
    """Retain only the declared strict, unit, gcd-one raw receipt."""
    return all(
        bool(row["strict_capacity"])
        and bool(row["unit_condition"])
        and row["gcd_reduction"] == 1
        for row in rows
    )


def verify_c38_raw_receipt() -> dict[str, object]:
    """Replay the new all-right raw word from the universal p-edge."""
    rows = replay_c38_word()
    selected_values = [int(row["selected_coordinate"]) for row in rows]
    destinations = [list(row["destination"]) for row in rows]
    if not (
        all_primitive(rows)
        and [int(row["q"]) for row in rows] == [v5.P, 5_623, 6_961, 3_041, 3_019]
        and [int(row["selected_coordinate_index"]) for row in rows] == [0, 1, 1, 1, 1]
        and [int(row["shift"]) for row in rows] == [1, 5_622, 6_960, 3_040, 3_018]
        and [int(row["selected_q_height"]) for row in rows] == [1, 1, 1, 1, 1]
        and [int(row["K_q_height"]) for row in rows] == [0, 0, 0, 0, 0]
        and selected_values == [
            v5.P,
            v5.R - 1,
            5_209_373_366_221,
            5_209_551_605_570,
            5_208_586_866_461,
        ]
        and v5.R - 1 == 2 * 5 * 5_623 * 92_660_501
        and selected_values[2] == 41 * 101 * 127 * 1_423 * 6_961
        and selected_values[3] == 2 * 5 * 13 * 3_041 * 13_177_729
        and selected_values[4] == 11 * 17 * 43 * 3_019 * 214_559
        and destinations[-1] == [1_725_268_919, Z2, 1]
        and C38_SUFFIX[0][1] != v5.COMMON[1][1]
    ):
        raise AssertionError("v=5 C=38 primitive raw receipt changed")
    return {
        "shared_prefix": "universal p edge only",
        "raw_word_after_anchor": [5_623, 6_961, 3_041, 3_019],
        "row_count": len(rows),
        "endpoint": destinations[-1],
        "primitive": True,
    }


def verify_c38_marked_tail() -> dict[str, object]:
    """Decode the tracked second coordinate as one physical signed C=38 tail."""
    trace = replay_c38_lineage()
    tail = lineage.verify_physical_tail(
        prime=v5.P,
        modulus=v5.R,
        carrier=M2,
        cofactor=C2,
        tail=T2,
        orientation=1,
        coordinate=Z2,
        expected_phase=MU2,
    )
    expected_coordinates = [
        v5.SOURCE[1],
        v5.R - 1,
        926_605_010,
        5_209_551_605_570,
        1_713_104_770,
        Z2,
    ]
    if not (
        v5.K % C2 == 0
        and Z2 == C2 * T2 == 2**3 * 19 * 233 * 147_068_407
        and M2 == 41_215_423_770_666_847_308_611
        and D2 == 1_202_376_916_403
        and N2 == 164_861_695_077_457_089_263_213
        and gcd(T2, M2) == gcd(Z2, v5.R) == 1
        and 0 < Z2 < v5.R
        and v5.P * N2 == 4 * M2 * D2 + 1
        and trace["coordinates"] == expected_coordinates
        and trace["final_coordinate_index"] == 1
        and trace["phases"][-1] == MU2
        and MU2 == -pow(Z2, -1, v5.R) % v5.R
        and MU2 == -N2 * pow(T2, -1, v5.R) % v5.R
        and tail["phase"] == MU2
    ):
        raise AssertionError("v=5 C=38 physical marked tail changed")
    return {"lineage": trace, "physical_tail": tail}


def verify_phase_compatibility() -> dict[str, object]:
    """Match the third raw mark to the nested candidate cofactor H_base*19^3."""
    candidate_record = candidate.verify_candidate_fiber()
    N = int(candidate_record["N"])
    mu2_over_mu1 = MU2 * pow(candidate.MU1, -1, v5.R) % v5.R
    mu2_over_mu0 = MU2 * pow(candidate.MU0, -1, v5.R) % v5.R
    if not (
        H3 == 1_334_507_617
        and N == 901 * H3
        and N % H3 == 0
        and candidate.chi(H3) == pow(MU2, 10, 191) == 52
        and 52 == pow(candidate.ZETA, 11, 191)
        and pow(mu2_over_mu1, 10, 191) == pow(candidate.ZETA, 3, 191)
        and candidate.chi(19**2) == pow(candidate.ZETA, 3, 191)
        and pow(mu2_over_mu0, 10, 191) == pow(candidate.ZETA, 14, 191)
        and candidate.chi(19**3) == pow(candidate.ZETA, 14, 191)
    ):
        raise AssertionError("v=5 C=38 q=19 phase correspondence changed")
    return {
        "mu2": MU2,
        "eta_exponent_mu2": 11,
        "candidate_cofactor": H3,
        "candidate_factorization": "H_base*19^3",
        "relative_eta_exponents": {"mu2_over_mu1": 3, "mu2_over_mu0": 14},
        "scope": "character correspondence only; no occurrence-to-candidate functor",
    }


def verify_three_row_carry_control() -> dict[str, object]:
    """Compute a three-row carry control without identifying successor states."""
    rows = [
        {"p": v5.P, "A": 19, "M": v5.M0, "C": v5.C0, "d": 3, "n": 13},
        {"p": v5.P, "A": 19, "M": v5.M1, "C": v5.C1, "d": v5.P - v5.C1, "n": v5.N1},
        {"p": v5.P, "A": 19, "M": M2, "C": C2, "d": D2, "n": N2},
    ]
    remainders = [int(row["M"]) % v5.P for row in rows]
    target_carriers = [lcm(19, int(row["C"])) for row in rows[1:]]
    for row in rows:
        carry.verify_overflow_row(row)
        if not carry.e2_passes(A=19, C=int(row["C"]), M=int(row["M"]), p=v5.P):
            raise AssertionError("v=5 C=38 carry row lost E2")
    if not (
        remainders == [100_198_076_370, 996_707_180_734, 498_353_590_367]
        and carry.persistent_carry_core(rows=rows, e2_indices={0, 1, 2}) == 19
        and 19 * remainders[1] == 38 * remainders[2] == 18_937_436_433_946
        and 4 * 19 * remainders[1] == 4 * 38 * remainders[2] == 63 * v5.P + 1
        and target_carriers == [19, 38]
    ):
        raise AssertionError("v=5 C=38 carry/reset arithmetic changed")
    return {
        "rows": [{**row, "r": int(row["M"]) % v5.P} for row in rows],
        "carry_core": 19,
        "shared_r_chart_arithmetic": {
            "R_r": 63,
            "K_r": 18_937_436_433_946,
            "target_carriers_for_C19_C38": target_carriers,
        },
        "scope": (
            "A three-row physical cofactor-overflow and E2 arithmetic control only; "
            "the C=19 and C=38 rows share an r-chart but have distinct target "
            "carriers. A state identity, entry digest, or slot count cannot be "
            "inferred from the common r-chart arithmetic alone."
        ),
    }


def verify_d6303_candidate_label_boundary() -> dict[str, object]:
    """Keep the selected H3 correspondence below the missing raw functor."""
    labels = catalog.admissible_a_values()
    heights = {
        a: catalog.valuation(v5.P + 4 * catalog.D * a, 19)
        for a in labels
    }
    phase_11_candidates = [
        (a, value)
        for a in labels
        for value in catalog.divisors(catalog.FIBERS[a])
        if catalog.phase_exponent(value) == 11
    ]
    height_3_phase_11_candidates = [
        (a, value)
        for a, value in phase_11_candidates
        if catalog.valuation(value, 19) == 3
    ]
    if not (
        labels == tuple(catalog.FIBERS)
        and heights == {1: 0, 3: 1, 11: 0, 33: 0, 191: 0, 573: 3, 2101: 0, 6303: 0}
        and candidate.SOURCE_A1 == 573
        and candidate.D * candidate.SOURCE_A1 == 3_611_619
        and (v5.P + 4 * catalog.D * 3) % 19 == 0
        and (v5.P + 4 * catalog.D * 573) % H3 == 0
        and catalog.phase_exponent(19) == 11
        and catalog.phase_exponent(H3) == 11
        and phase_11_candidates == [
            (3, 19),
            (11, 70_715_591),
            (11, 495_009_137),
            (11, 3_465_063_959),
            (573, 19),
            (573, 1_014_049),
            (573, 3_307_571),
            (573, H3),
        ]
        and height_3_phase_11_candidates == [(573, H3)]
    ):
        raise AssertionError("v=5 D=6303 q-active label boundary changed")
    return {
        "q_active_candidate_labels": {a: height for a, height in heights.items() if height},
        "phase_11_candidates": phase_11_candidates,
        "height_3_phase_11_candidates": height_3_phase_11_candidates,
        "conditional_H3_correspondence": (
            "Within the fixed catalog, (A,H)=(573,H_base*19^3) is the unique tagged "
            "candidate if a future functor preserves both phase zeta^11 and positive "
            "cofactor height v19(H)=3. No functor is currently supplied, so this "
            "conditional uniqueness does not assign the raw occurrence."
        ),
        "shared_budget": "H_base, H_base*19, and H_base*19^3 are nested in one N_A.",
    }


def build_result() -> dict[str, object]:
    """Build a terminal-preempted third raw occurrence, not a selector edge."""
    return {
        "certificate_type": "v5_c38_q19_phase_leaf_v1",
        "status": "analysis_evidence_only",
        "terminal_preempted_by": v5.verify_terminal_first(),
        "raw_receipt": verify_c38_raw_receipt(),
        "marked_tail": verify_c38_marked_tail(),
        "phase_compatibility": verify_phase_compatibility(),
        "three_row_carry_control": verify_three_row_carry_control(),
        "d6303_candidate_label_boundary": verify_d6303_candidate_label_boundary(),
        "missing_for_adapter_capacity_or_selector": [
            "complete transition/source universe",
            "occurrence-to-(a,b,H,slot) functor",
            "prefix request and layer allocation",
            "independent physical slots and demand_to_slot",
            "target-odd carrier, E4/E5, and terminal-first clearance",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 C=38 q=19 phase leaf")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
