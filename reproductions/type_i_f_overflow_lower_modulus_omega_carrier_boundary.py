#!/usr/bin/env python3
"""Audit the exact lower-modulus Omega_1 interface to q-adic carriers.

For every frozen lower-modulus F-box miss whose Omega_1 value is known exactly,
enumerate the whole minimum shell.  The audit verifies the two-orientation
rational-denominator identity and asks whether *any* minimum overflow pattern
can be injected coordinatewise into deliberately optimistic local block,
label-difference, and modulus-difference heights.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OMEGA_INPUT = (
    ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-weighted-cost-results.json"
)
REPAIR_INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_SCRIPT = (
    ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
OUTPUT = (
    ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-omega-carrier-boundary-results.json"
)

EXPECTED_OMEGA_SHA256 = "e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82"
EXPECTED_REPAIR_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "96ee0c6711a4995fe387686a4915b41f1fcefa70cd4fe808c05a4092bf05e07d"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_module("omega_carrier_linear_source", SOURCE_SCRIPT)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("q-adic height of zero is not a finite capacity")
    value = abs(value)
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def exact_overflow_vectors(nu: tuple[int, ...], cost: int):
    """Yield every vector with sum_i (|z_i|-nu_i)_+ equal to cost."""
    vector = [0] * len(nu)

    def visit(index: int, remaining: int):
        if index == len(nu):
            if remaining == 0:
                yield tuple(vector)
            return

        bound = nu[index]
        for exponent in range(-bound, bound + 1):
            vector[index] = exponent
            yield from visit(index + 1, remaining)
        for excess in range(1, remaining + 1):
            for exponent in (bound + excess, -bound - excess):
                vector[index] = exponent
                yield from visit(index + 1, remaining - excess)
        vector[index] = 0

    yield from visit(0, cost)


def relation_residue(
    factors: tuple[int, ...], modulus: int, vector: tuple[int, ...]
) -> int:
    residue = 1 % modulus
    for q, exponent in zip(factors, vector):
        base = q if exponent >= 0 else pow(q, -1, modulus)
        residue = residue * pow(base, abs(exponent), modulus) % modulus
    return residue


def overflow_pattern(
    vector: tuple[int, ...], nu: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(max(abs(exponent) - bound, 0) for exponent, bound in zip(vector, nu))


def formal_pair(
    factors: tuple[int, ...], vector: tuple[int, ...]
) -> tuple[int, int]:
    numerator = math.prod(
        pow(q, max(exponent, 0)) for q, exponent in zip(factors, vector)
    )
    denominator = math.prod(
        pow(q, max(-exponent, 0)) for q, exponent in zip(factors, vector)
    )
    return numerator, denominator


def best_difference_height(values: set[int], current: set[int], q: int) -> int:
    return max(
        (
            valuation(value - other, q)
            for value in current
            for other in values
            if value != other
        ),
        default=0,
    )


def run() -> dict[str, object]:
    for path, expected, label in (
        (OMEGA_INPUT, EXPECTED_OMEGA_SHA256, "Omega profile"),
        (REPAIR_INPUT, EXPECTED_REPAIR_SHA256, "endpoint repair"),
        (SOURCE_SCRIPT, EXPECTED_SOURCE_SHA256, "linear source enumerator"),
    ):
        if sha256(path) != expected:
            raise AssertionError(f"the frozen {label} input changed")

    omega_payload = json.loads(OMEGA_INPUT.read_text(encoding="utf-8"))
    repair_payload = json.loads(REPAIR_INPUT.read_text(encoding="utf-8"))
    repair_rows = {
        (
            int(row["prime"]),
            int(row["R"]),
            str(row["orientation"]),
        ): row
        for row in repair_payload["records"]
    }
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    records: list[dict[str, object]] = []

    for profile in omega_payload["profiles"]:
        if profile["omega_secondary"] is None:
            continue
        prime = int(profile["prime"])
        original_R = int(profile["original_R"])
        orientation = str(profile["orientation"])
        gap = int(profile["gap"])
        lower_modulus = int(profile["lower_modulus"])
        omega = int(profile["omega_secondary"])
        factorization = tuple(
            (int(q), int(exponent)) for q, exponent in profile["factorization"]
        )
        factors = tuple(q for q, _exponent in factorization)
        nu = tuple(exponent for _q, exponent in factorization)
        if any(q == 2 for q in factors):
            raise AssertionError("this frozen lower-modulus boundary is odd-supported")
        K = math.prod(pow(q, exponent) for q, exponent in factorization)
        if original_R != gap * lower_modulus or 4 * K != prime * original_R + 1:
            raise AssertionError("the scaled lower-modulus state is inconsistent")
        scaled_numerator = (4 * K - 1) // lower_modulus
        if scaled_numerator != prime * gap:
            raise AssertionError("the lower modulus did not scale p by the endpoint gap")

        if prime not in source_cache:
            _bound, source_cache[prime] = source.enumerate_linear_source_states(prime)
        states_by_R = source_cache[prime]
        current_states = states_by_R.get(original_R)
        if not current_states:
            raise AssertionError("the current linear source state disappeared")
        all_moduli = set(states_by_R)
        all_labels = {
            label
            for states in states_by_R.values()
            for a, s in states
            for label in (a, s)
        }
        current_labels = {label for a, s in current_states for label in (a, s)}

        repair_row = repair_rows[(prime, original_R, orientation)]
        candidate = next(
            item
            for item in repair_row["candidates"]
            if int(item["gap"]) == gap
            and int(item["balanced_t"]) == lower_modulus
            and item["lower_modulus_classification"] == "F_box_miss"
        )
        formal_A = int(repair_row["formal_A"])
        formal_B = int(repair_row["formal_B"])
        if (formal_A + 1) % gap or (formal_B - 1) % gap:
            raise AssertionError("the balanced endpoints are not integral")
        endpoint_u = (formal_A + 1) // gap
        endpoint_v = (formal_B - 1) // gap
        endpoint_gcd = math.gcd(endpoint_u, endpoint_v)
        reduced_u = endpoint_u // endpoint_gcd
        reduced_v = endpoint_v // endpoint_gcd
        if math.gcd(reduced_u, reduced_v) != 1:
            raise AssertionError("the reduced balanced endpoints are not coprime")
        if int(candidate["balanced_pair_gcd"]) != endpoint_gcd:
            raise AssertionError("the stored endpoint gcd changed")

        heights: list[dict[str, int]] = []
        for q, exponent in factorization:
            block_height = max(
                max(valuation(a * original_R + 1, q), valuation(s * original_R + 1, q))
                for a, s in current_states
            )
            block_total_heights = {
                valuation(a * original_R + 1, q)
                + valuation(s * original_R + 1, q)
                for a, s in current_states
            }
            if block_total_heights != {exponent}:
                raise AssertionError("odd block heights do not sum to v_q(K)")
            label_height = best_difference_height(all_labels, current_labels, q)
            modulus_height = best_difference_height(all_moduli, {original_R}, q)
            endpoint_height = max(valuation(reduced_u, q), valuation(reduced_v, q))
            if any(valuation(value, q) for value in (original_R, gap, lower_modulus)):
                raise AssertionError("a K-prime unexpectedly divides R, m, or t")
            heights.append(
                {
                    "q": q,
                    "nu": exponent,
                    "block_max": block_height,
                    "label_difference_max": label_height,
                    "modulus_difference_max": modulus_height,
                    "three_channel_sum": block_height + label_height + modulus_height,
                    "reduced_endpoint_max": endpoint_height,
                    "three_channel_plus_endpoint_sum": (
                        block_height + label_height + modulus_height + endpoint_height
                    ),
                }
            )

        target_vector_count = 0
        patterns: set[tuple[int, ...]] = set()
        canonical_vector = tuple(int(value) for value in profile["omega_secondary_vector"])
        canonical_seen = False
        for vector in exact_overflow_vectors(nu, omega):
            if relation_residue(factors, lower_modulus, vector) != lower_modulus - 1:
                continue
            target_vector_count += 1
            canonical_seen |= vector == canonical_vector
            pattern = overflow_pattern(vector, nu)
            if sum(pattern) != omega:
                raise AssertionError("minimum-shell overflow cost changed")
            patterns.add(pattern)

            numerator, denominator = formal_pair(factors, vector)
            if math.gcd(numerator, denominator) != 1:
                raise AssertionError("the formal relation pair is not coprime")
            if (numerator + denominator) % lower_modulus:
                raise AssertionError("the target relation is not a sum multiple")
            negative_defect = denominator // math.gcd(denominator, K)
            positive_defect = numerator // math.gcd(numerator, K)
            defect_product = math.prod(pow(q, excess) for q, excess in zip(factors, pattern))
            if negative_defect * positive_defect != defect_product:
                raise AssertionError("the two-orientation denominator identity failed")

        if not target_vector_count or not canonical_seen:
            raise AssertionError("the exact Omega shell or its canonical vector disappeared")

        channel_caps = tuple(item["three_channel_sum"] for item in heights)
        extended_caps = tuple(
            item["three_channel_plus_endpoint_sum"] for item in heights
        )
        block_caps = tuple(item["block_max"] for item in heights)
        block_feasible = [
            pattern for pattern in patterns if all(e <= cap for e, cap in zip(pattern, block_caps))
        ]
        channel_feasible = [
            pattern for pattern in patterns if all(e <= cap for e, cap in zip(pattern, channel_caps))
        ]
        extended_feasible = [
            pattern for pattern in patterns if all(e <= cap for e, cap in zip(pattern, extended_caps))
        ]

        def minimum_deficit(caps: tuple[int, ...]) -> int:
            return min(
                sum(max(excess - cap, 0) for excess, cap in zip(pattern, caps))
                for pattern in patterns
            )

        canonical_pattern = overflow_pattern(canonical_vector, nu)
        records.append(
            {
                "prime": prime,
                "orientation": orientation,
                "original_R": original_R,
                "gap": gap,
                "lower_modulus": lower_modulus,
                "scaled_numerator": scaled_numerator,
                "omega": omega,
                "canonical_vector": list(canonical_vector),
                "canonical_overflow_pattern": list(canonical_pattern),
                "minimum_target_vector_count": target_vector_count,
                "minimum_overflow_pattern_count": len(patterns),
                "minimum_overflow_patterns": [list(pattern) for pattern in sorted(patterns)],
                "current_directed_source_state_count": len(current_states),
                "complete_source_modulus_count": len(all_moduli),
                "complete_source_label_count": len(all_labels),
                "reduced_endpoints": [reduced_u, reduced_v],
                "coordinate_heights": heights,
                "block_feasible_minimum_pattern_count": len(block_feasible),
                "three_channel_feasible_minimum_pattern_count": len(channel_feasible),
                "three_channel_plus_endpoint_feasible_minimum_pattern_count": len(extended_feasible),
                "minimum_block_deficit": minimum_deficit(block_caps),
                "minimum_three_channel_deficit": minimum_deficit(channel_caps),
                "minimum_three_channel_plus_endpoint_deficit": minimum_deficit(extended_caps),
            }
        )

    if len(records) != 36:
        raise AssertionError(f"unexpected exact Omega state count: {len(records)}")

    coordinate_occurrences = [
        (record, index, excess)
        for record in records
        for pattern in record["minimum_overflow_patterns"]
        for index, excess in enumerate(pattern)
        if int(excess) > 0
    ]
    return {
        "arithmetic": (
            "For all 36 lower-modulus F-box misses with exact Omega_1<=9, enumerate the "
            "complete minimum shell; verify that the product of the two oriented rational "
            "first-denominator defects is prod(q_i^overflow_i); and compare every minimum "
            "overflow pattern with optimistic complete-source block, label-difference, "
            "modulus-difference, and reduced-endpoint q-adic heights."
        ),
        "scope_note": (
            "A state with no feasible minimum pattern is a finite counterexample to a "
            "coordinatewise injective local charge into the listed height levels. It does not "
            "rule out a nonlocal cross-state matching, reuse controlled by a separate theorem, "
            "a non-minimum target vector, factor splitting, or an arithmetic descent. The six "
            "states with Omega_1>=10 are outside this exact-shell audit."
        ),
        "omega_input": OMEGA_INPUT.name,
        "omega_input_sha256": sha256(OMEGA_INPUT),
        "repair_input": REPAIR_INPUT.name,
        "repair_input_sha256": sha256(REPAIR_INPUT),
        "source_script": SOURCE_SCRIPT.name,
        "source_script_sha256": sha256(SOURCE_SCRIPT),
        "exact_state_count": len(records),
        "unresolved_state_count": int(omega_payload["secondary_unresolved_count"]),
        "all_factors_odd": True,
        "all_scaled_numerators_equal_p_times_gap": True,
        "all_q_heights_of_R_gap_t_zero": True,
        "all_odd_block_total_heights_equal_nu": True,
        "all_minimum_vectors_satisfy_two_orientation_denominator_identity": True,
        "minimum_target_vector_count": sum(
            int(record["minimum_target_vector_count"]) for record in records
        ),
        "minimum_overflow_pattern_count": sum(
            int(record["minimum_overflow_pattern_count"]) for record in records
        ),
        "block_infeasible_state_count": sum(
            int(record["block_feasible_minimum_pattern_count"] == 0) for record in records
        ),
        "three_channel_infeasible_state_count": sum(
            int(record["three_channel_feasible_minimum_pattern_count"] == 0)
            for record in records
        ),
        "three_channel_plus_endpoint_infeasible_state_count": sum(
            int(record["three_channel_plus_endpoint_feasible_minimum_pattern_count"] == 0)
            for record in records
        ),
        "minimum_block_deficit_histogram": dict(
            sorted(Counter(int(record["minimum_block_deficit"]) for record in records).items())
        ),
        "minimum_three_channel_deficit_histogram": dict(
            sorted(
                Counter(int(record["minimum_three_channel_deficit"]) for record in records).items()
            )
        ),
        "minimum_three_channel_plus_endpoint_deficit_histogram": dict(
            sorted(
                Counter(
                    int(record["minimum_three_channel_plus_endpoint_deficit"])
                    for record in records
                ).items()
            )
        ),
        "minimum_pattern_coordinate_occurrence_count": len(coordinate_occurrences),
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "exact_state_count",
                    "unresolved_state_count",
                    "minimum_target_vector_count",
                    "minimum_overflow_pattern_count",
                    "block_infeasible_state_count",
                    "three_channel_infeasible_state_count",
                    "three_channel_plus_endpoint_infeasible_state_count",
                    "minimum_block_deficit_histogram",
                    "minimum_three_channel_deficit_histogram",
                    "minimum_three_channel_plus_endpoint_deficit_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
