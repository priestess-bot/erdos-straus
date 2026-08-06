#!/usr/bin/env python3
"""Verify ordered raw-lineage normalized-phase rigidity controls.

The p=1009 control replays one declared universal-source word with no gcd
reductions.  The p=193 control replays one target-derived formal p-parent only
to expose a nontrivial gcd phase at an F/q=3 quotient.  Neither control creates
a root, source-to-F map, terminal certificate, or recursive edge.
"""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def is_prime(value: int) -> bool:
    """Use trial division because every focused control is constant size."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorization(value: int) -> dict[int, int]:
    """Factor a focused control integer without an external dependency."""
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def ordered_raw_step(
    *,
    modulus: int,
    carrier: int,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    expected_destination: tuple[int, int, int],
    name: str,
) -> dict[str, object]:
    """Replay one selected-first raw step and retain its actual gcd reduction."""
    if selected_coordinate_index not in (0, 1):
        raise AssertionError(f"{name}: invalid selected-coordinate index")
    left, right, layer = source
    if min(left, right, layer) <= 0 or left + right != modulus * layer:
        raise AssertionError(f"{name}: source is not a positive formal node")
    if gcd(left, right) != 1:
        raise AssertionError(f"{name}: source is not primitive")
    selected, other = (
        (left, right) if selected_coordinate_index == 0 else (right, left)
    )
    if not is_prime(q) or selected % q:
        raise AssertionError(f"{name}: selected coordinate lacks the declared prime")
    shift = (-layer) % q
    if not (1 <= shift < q):
        raise AssertionError(f"{name}: shift is not strict")
    if valuation(selected, q) <= valuation(carrier, q):
        raise AssertionError(f"{name}: raw capacity is not strict")
    if gcd(q, modulus * layer * other) != 1:
        raise AssertionError(f"{name}: raw unit condition failed")

    selected_after_division = selected // q
    if (other + modulus * shift) % q or (layer + shift) % q:
        raise AssertionError(f"{name}: raw division is not integral")
    other_after_shift = (other + modulus * shift) // q
    layer_after_shift = (layer + shift) // q
    reduction = gcd(selected_after_division, other_after_shift)
    if reduction <= 0 or layer_after_shift % reduction:
        raise AssertionError(f"{name}: gcd reduction did not preserve the layer")
    destination = (
        selected_after_division // reduction,
        other_after_shift // reduction,
        layer_after_shift // reduction,
    )
    if destination != expected_destination:
        raise AssertionError(f"{name}: ordered destination changed")
    if (
        min(destination) <= 0
        or gcd(destination[0], destination[1]) != 1
        or destination[0] + destination[1] != modulus * destination[2]
    ):
        raise AssertionError(f"{name}: destination is not a primitive formal node")
    return {
        "name": name,
        "source": source,
        "selected_coordinate_index": selected_coordinate_index,
        "q": q,
        "shift": shift,
        "pre_gcd_destination": (
            selected_after_division,
            other_after_shift,
            layer_after_shift,
        ),
        "gcd_reduction": reduction,
        "destination": destination,
    }


def normalized_phase(value: int, modulus: int) -> int:
    """Return the unique unit phase satisfying phase * value = -1 mod modulus."""
    if gcd(value, modulus) != 1:
        raise AssertionError("lineage coordinate is not a unit")
    return (-pow(value, -1, modulus)) % modulus


def trace_lineage(
    *,
    modulus: int,
    carrier: int,
    source: tuple[int, int, int],
    source_coordinate_index: int,
    specs: tuple[tuple[int, int, tuple[int, int, int], str], ...],
) -> dict[str, object]:
    """Replay a word and follow one coordinate through ordered destinations."""
    if source_coordinate_index not in (0, 1):
        raise AssertionError("invalid source lineage coordinate")
    current = source
    lineage_index = source_coordinate_index
    coordinates = [current[lineage_index]]
    products = [1]
    phases = [normalized_phase(coordinates[0], modulus)]
    rows: list[dict[str, object]] = []

    for step_index, (selected_index, q, destination, name) in enumerate(specs, start=1):
        row = ordered_raw_step(
            modulus=modulus,
            carrier=carrier,
            source=current,
            selected_coordinate_index=selected_index,
            q=q,
            expected_destination=destination,
            name=name,
        )
        reduction = int(row["gcd_reduction"])
        next_index = 0 if lineage_index == selected_index else 1
        next_coordinate = destination[next_index]
        previous_coordinate = coordinates[-1]
        if q * reduction * next_coordinate % modulus != previous_coordinate % modulus:
            raise AssertionError(f"{name}: q*g lineage transport changed")
        product = products[-1] * q * reduction % modulus
        if product * next_coordinate % modulus != coordinates[0] % modulus:
            raise AssertionError(f"{name}: accumulated lineage transport changed")
        phase = normalized_phase(next_coordinate, modulus)
        if phase != product * phases[0] % modulus:
            raise AssertionError(f"{name}: normalized phase transport changed")
        if phase * pow(phases[-1], -1, modulus) % modulus != q * reduction % modulus:
            raise AssertionError(f"{name}: one-step normalized phase ratio changed")
        rows.append(row)
        coordinates.append(next_coordinate)
        products.append(product)
        phases.append(phase)
        current = destination
        lineage_index = next_index

    return {
        "rows": rows,
        "coordinates": coordinates,
        "products": products,
        "phases": phases,
        "final_coordinate_index": lineage_index,
    }


def verify_physical_tail(
    *,
    prime: int,
    modulus: int,
    carrier: int,
    cofactor: int,
    tail: int,
    orientation: int,
    coordinate: int,
    expected_phase: int,
) -> dict[str, int]:
    """Check Phi=-orientation*n*t^-1 for one declared physical row reading."""
    if orientation not in (-1, 1):
        raise AssertionError("physical-tail orientation must be a sign")
    if carrier * cofactor != (prime * modulus + 1) // 4:
        raise AssertionError("physical row does not recover the Type I carrier")
    if coordinate % modulus != orientation * cofactor * tail % modulus:
        raise AssertionError("lineage coordinate does not match the marked physical tail")
    row_n = 4 * carrier - modulus
    if row_n <= 0:
        raise AssertionError("physical row is not an overflow row")
    if prime * row_n != 4 * carrier * (prime - cofactor) + 1:
        raise AssertionError("physical determinant changed")
    actual_phase = normalized_phase(coordinate, modulus)
    tail_phase = (-orientation * row_n * pow(tail, -1, modulus)) % modulus
    if actual_phase != tail_phase or actual_phase != expected_phase:
        raise AssertionError("physical-tail phase law changed")
    return {
        "C": cofactor,
        "M": carrier,
        "t": tail,
        "n_row": row_n,
        "orientation": orientation,
        "phase": actual_phase,
    }


def verify_p1009_control() -> dict[str, object]:
    """Replay the declared p=1009 bypass and its three physical tail points."""
    prime, modulus, carrier = 1009, 4359, 1_099_558
    M, C = 1093, 1006
    source = (1009, 4_392_863, 1008)
    if (
        not is_prime(prime)
        or prime % 24 != 1
        or factorization(carrier) != {2: 1, 503: 1, 1093: 1}
        or carrier != M * C
        or prime * modulus + 1 != 4 * carrier
    ):
        raise AssertionError("p=1009 chart changed")
    specs = (
        (1, 349, (12_587, 490, 3), "p1009_bypass_349"),
        (0, 41, (307, 4052, 1), "p1009_bypass_41"),
        (1, 1013, (4, 4355, 1), "p1009_bypass_1013"),
        (1, 13, (335, 4024, 1), "p1009_bypass_13"),
        (1, 2, (2012, 2347, 1), "p1009_bypass_2a"),
        (0, 2, (1006, 3353, 1), "p1009_bypass_2b"),
    )
    trace = trace_lineage(
        modulus=modulus,
        carrier=carrier,
        source=source,
        source_coordinate_index=0,
        specs=specs,
    )
    if trace["coordinates"] != [1009, 490, 4052, 4, 4024, 2012, 1006]:
        raise AssertionError("p=1009 ordered lineage changed")
    if trace["products"] != [1, 349, 1232, 1342, 10, 20, 40]:
        raise AssertionError("p=1009 enriched products changed")
    if trace["phases"] != [2942, 2393, 2215, 3269, 3266, 2173, 4346]:
        raise AssertionError("p=1009 normalized phases changed")
    if any(int(row["gcd_reduction"]) != 1 for row in trace["rows"]):
        raise AssertionError("p=1009 control unexpectedly gained a gcd reduction")

    tail_rows = [
        verify_physical_tail(
            prime=prime,
            modulus=modulus,
            carrier=M,
            cofactor=C,
            tail=tail,
            orientation=1,
            coordinate=coordinate,
            expected_phase=phase,
        )
        for tail, coordinate, phase in ((4, 4024, 3266), (2, 2012, 2173), (1, 1006, 4346))
    ]
    return {
        "chart": {"p": prime, "R": modulus, "K": carrier},
        "scope": "declared universal-source raw word only; no F/source-map claim",
        "lineage": trace,
        "physical_tail_rows": tail_rows,
    }


def units(modulus: int) -> set[int]:
    """Return the finite unit group for the one small F control."""
    return {value for value in range(1, modulus) if gcd(value, modulus) == 1}


def generated_subgroup(generators: set[int], modulus: int) -> set[int]:
    """Close a small multiplicative subgroup under the supplied generators."""
    subgroup = {1}
    changed = True
    while changed:
        changed = False
        expanded = {
            left * right % modulus
            for left in subgroup
            for right in subgroup | generators
        }
        if not expanded <= subgroup:
            subgroup |= expanded
            changed = True
    return subgroup


def centered_residues(factors: dict[int, int], modulus: int) -> set[int]:
    """Build the centered fixed layer used by the focused F control."""
    residues = {1}
    for prime, bound in factors.items():
        residues = {
            residue * pow(prime, exponent, modulus) % modulus
            for residue in residues
            for exponent in range(-bound, bound + 1)
        }
    return residues


def p193_f_quotient() -> tuple[dict[int, int], dict[str, object]]:
    """Construct the C6 F quotient and the q=3 direct target datum."""
    modulus = 63
    group = units(modulus)
    if generated_subgroup({2, 5, 19}, modulus) != group:
        raise AssertionError("p=193 support no longer generates U(63)")
    stabilizer = {pow(2, exponent, modulus) for exponent in range(6)}
    if stabilizer != {1, 2, 4, 8, 16, 32}:
        raise AssertionError("p=193 fixed stabilizer changed")
    coordinate: dict[int, int] = {}
    for exponent in range(6):
        coset = {pow(5, exponent, modulus) * element % modulus for element in stabilizer}
        if len(coset) != len(stabilizer) or any(element in coordinate for element in coset):
            raise AssertionError("p=193 quotient cosets are not disjoint")
        coordinate.update({element: exponent for element in coset})
    if set(coordinate) != group or coordinate[5] != 1 or coordinate[62] != 3:
        raise AssertionError("p=193 C6 quotient coordinates changed")

    fixed_layer = centered_residues({2: 5, 19: 1}, modulus)
    actual_stabilizer = {
        candidate
        for candidate in group
        if {candidate * value % modulus for value in fixed_layer} == fixed_layer
    }
    if actual_stabilizer != stabilizer:
        raise AssertionError("p=193 centered fixed-layer stabilizer changed")
    fixed_coordinates = {coordinate[value] for value in fixed_layer}
    if fixed_coordinates != {0, 1, 5}:
        raise AssertionError("p=193 F fixed layer changed")
    representation_counts = [0] * 6
    for fixed_coordinate in fixed_coordinates:
        for exponent in (-1, 0, 1):
            representation_counts[(fixed_coordinate + exponent) % 6] += 1
    if representation_counts != [3, 2, 1, 0, 1, 2]:
        raise AssertionError("p=193 F quotient representation vector changed")
    if representation_counts[coordinate[62]] != 0:
        raise AssertionError("p=193 F target is no longer absent")
    if coordinate[62] % 3 != 0:
        raise AssertionError("p=193 q=3 direct target phase changed")
    return coordinate, {
        "quotient_order": 6,
        "generator": 5,
        "target_coordinate": coordinate[62],
        "fixed_coordinates": sorted(fixed_coordinates),
        "representation_counts": representation_counts,
        "q_primary_target_exponent_mod_3": coordinate[62] % 3,
    }


def verify_p193_control() -> dict[str, object]:
    """Expose the p=193 F/q=3 false pass caused by omitting g=25."""
    prime, modulus, K = 193, 63, 3040
    if (
        not is_prime(prime)
        or prime % 24 != 1
        or prime * modulus + 1 != 4 * K
        or factorization(K) != {2: 5, 5: 1, 19: 1}
    ):
        raise AssertionError("p=193 Type I F chart changed")
    quotient_coordinate, f_data = p193_f_quotient()

    # This parent is deliberately target-derived.  It is a local g-transport
    # control, not a root provenance receipt.
    source = (24_125, 279_787, 4824)
    specs = ((0, 193, (5, 58, 1), "p193_target_derived_p_parent"),)
    trace = trace_lineage(
        modulus=modulus,
        carrier=K,
        source=source,
        source_coordinate_index=0,
        specs=specs,
    )
    row = trace["rows"][0]
    if row["shift"] != 1 or row["pre_gcd_destination"] != (125, 1450, 25):
        raise AssertionError("p=193 pre-gcd raw transcript changed")
    if int(row["gcd_reduction"]) != 25:
        raise AssertionError("p=193 gcd reduction changed")
    if trace["coordinates"] != [24_125, 5]:
        raise AssertionError("p=193 selected-coordinate lineage changed")
    if trace["products"] != [1, 37] or trace["phases"] != [16, 25]:
        raise AssertionError("p=193 enriched phase transport changed")

    physical = verify_physical_tail(
        prime=prime,
        modulus=modulus,
        carrier=608,
        cofactor=5,
        tail=1,
        orientation=1,
        coordinate=5,
        expected_phase=25,
    )
    factor_only_phase = prime * int(trace["phases"][0]) % modulus
    if factor_only_phase != 1:
        raise AssertionError("p=193 factor-only phase changed")

    def psi_three_exponent(value: int) -> int:
        return quotient_coordinate[value % modulus] % 3

    actual_phase = int(trace["phases"][1])
    if (
        psi_three_exponent(25) != 2
        or psi_three_exponent(actual_phase) != 2
        or psi_three_exponent(factor_only_phase) != 0
        or psi_three_exponent(prime) != 0
    ):
        raise AssertionError("p=193 q=3 gcd-omission character control changed")
    return {
        "chart": {"p": prime, "R": modulus, "K": K},
        "scope": (
            "target-derived formal p-parent only; the quotient is a conditional "
            "source-to-F candidate, not an established semantic source map; "
            "R < p, so this is not a carry/E2 overflow transcript"
        ),
        "F_q3": f_data,
        "lineage": trace,
        "physical_tail_row": physical,
        "factor_only_phase": factor_only_phase,
        "q3_character_exponents": {
            "gcd_reduction_25": psi_three_exponent(25),
            "actual_enriched_phase": psi_three_exponent(actual_phase),
            "factor_only_phase": psi_three_exponent(factor_only_phase),
            "direct_F_target": 0,
        },
    }


def run_controls() -> dict[str, object]:
    """Run only the two named, constant-size mathematical controls."""
    return {
        "certificate_type": "ordered_raw_lineage_normalized_phase_rigidity_v1",
        "scope": (
            "Exact raw-lineage transport, physical-tail normalization, and a "
            "conditional F/q-primary compatibility preflight only."
        ),
        "p1009": verify_p1009_control(),
        "p193": verify_p193_control(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    run_controls()
    if args.verify:
        print("verified ordered raw-lineage normalized-phase rigidity controls")


if __name__ == "__main__":
    main()
