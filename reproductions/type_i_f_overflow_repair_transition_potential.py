#!/usr/bin/env python3
"""Audit well-founded potentials on the frozen overflow-repair transition graph.

The audit keeps legal Type-I states and lower-modulus quotient representations
as different node types.  This distinction is essential: primary repair stays
inside the legal state space but increases the modulus, whereas balanced
quotient reduction decreases the modulus but lands at 1 modulo 4.
"""

from __future__ import annotations

from collections import Counter, deque
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPAIR_INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
TYPE_II_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-shared-gap-type-ii-results.json"
)
OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-repair-transition-potential-results.json"
)

EXPECTED_REPAIR_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"
EXPECTED_TYPE_II_SHA256 = "1a5b85c88bcdf8f9aa975f04629ddec9eeca3d2ebf58dabe107bbbeef7a3d65e"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def box_image(factors: list[tuple[int, int]], modulus: int) -> set[int]:
    """Return the exact image of the exponent box modulo ``modulus``."""
    residues = {1 % modulus}
    for prime, exponent_bound in factors:
        if math.gcd(prime, modulus) != 1:
            raise AssertionError("a K-support prime is not a unit modulo the state")
        inverse = pow(prime, -1, modulus)
        powers = {
            (
                pow(prime, exponent, modulus)
                if exponent >= 0
                else pow(inverse, -exponent, modulus)
            )
            for exponent in range(-exponent_bound, exponent_bound + 1)
        }
        residues = {
            residue * power % modulus
            for residue in residues
            for power in powers
        }
    return residues


def exact_unit_overflow_cost(
    factors: list[tuple[int, int]], modulus: int
) -> dict[str, int]:
    """Compute Omega_1 as distance from the box image in a finite Cayley graph.

    Multiplication by q_i or q_i^{-1} costs one.  The distance from the box
    image to -1 is exactly min_z sum_i (|z_i|-nu_i)_+.
    """
    starts = box_image(factors, modulus)
    target = modulus - 1
    if target in starts:
        return {
            "omega": 0,
            "box_image_size": len(starts),
            "visited_residue_count": len(starts),
        }

    generators: list[int] = []
    for prime, _exponent in factors:
        generators.extend((prime % modulus, pow(prime, -1, modulus)))
    distances = {residue: 0 for residue in starts}
    queue: deque[int] = deque(starts)
    while queue:
        residue = queue.popleft()
        next_distance = distances[residue] + 1
        for generator in generators:
            next_residue = residue * generator % modulus
            if next_residue in distances:
                continue
            distances[next_residue] = next_distance
            if next_residue == target:
                return {
                    "omega": next_distance,
                    "box_image_size": len(starts),
                    "visited_residue_count": len(distances),
                }
            queue.append(next_residue)
    raise AssertionError("the inherited F target was not in the generated subgroup")


def prime_factor_count_with_multiplicity(value: int) -> int:
    if value <= 0:
        raise ValueError("factor count requires a positive integer")
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            value //= divisor
            count += 1
        divisor += 2
    if value > 1:
        count += 1
    return count


def source_node_id(prime: int, modulus: int, orientation: str) -> str:
    return f"source:{prime}:{modulus}:{orientation}"


def primary_node_id(prime: int, modulus: int, orientation: str, gap: int) -> str:
    return f"primary:{prime}:{modulus}:{orientation}:{gap}"


def quotient_node_id(prime: int, modulus: int, orientation: str) -> str:
    return f"quotient:{prime}:{modulus}:{orientation}"


def second_node_id(prime: int, modulus: int, parent: str, gap: int) -> str:
    return f"second:{prime}:{modulus}:{parent}:{gap}"


def graph_profile(nodes: dict[str, str], edges: list[dict[str, object]]) -> dict[str, object]:
    adjacency: dict[str, list[str]] = {node: [] for node in nodes}
    indegree = {node: 0 for node in nodes}
    for edge in edges:
        source = str(edge["source"])
        target = str(edge["target"])
        adjacency[source].append(target)
        indegree[target] += 1

    queue: deque[str] = deque(node for node, degree in indegree.items() if degree == 0)
    topological_order: list[str] = []
    longest = {node: 0 for node in nodes}
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for target in adjacency[node]:
            longest[target] = max(longest[target], longest[node] + 1)
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    acyclic = len(topological_order) == len(nodes)
    return {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "node_kind_histogram": dict(sorted(Counter(nodes.values()).items())),
        "edge_kind_histogram": dict(
            sorted(Counter(str(edge["kind"]) for edge in edges).items())
        ),
        "sink_node_count": sum(not adjacency[node] for node in nodes),
        "acyclic": acyclic,
        "directed_cycle_count": 0 if acyclic else None,
        "maximum_known_path_length": max(longest.values(), default=0),
    }


def run() -> dict[str, object]:
    repair_hash = sha256(REPAIR_INPUT)
    source_hash = sha256(SOURCE_INPUT)
    type_ii_hash = sha256(TYPE_II_INPUT)
    if repair_hash != EXPECTED_REPAIR_SHA256:
        raise AssertionError("the frozen repair input changed")
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen support input changed")
    if type_ii_hash != EXPECTED_TYPE_II_SHA256:
        raise AssertionError("the frozen shared-gap Type II input changed")

    repair_payload = json.loads(REPAIR_INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    type_ii_payload = json.loads(TYPE_II_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): row
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }
    type_ii_rows = {
        (
            int(row["prime"]),
            int(row["original_R"]),
            str(row["orientation"]),
            int(row["lower_modulus"]),
        ): row
        for row in type_ii_payload["records"]
    }

    omega_cache: dict[tuple[tuple[tuple[int, int], ...], int], dict[str, int]] = {}

    def cached_omega(factors: list[tuple[int, int]], modulus: int) -> dict[str, int]:
        key = (tuple(factors), modulus)
        if key not in omega_cache:
            omega_cache[key] = exact_unit_overflow_cost(factors, modulus)
        return omega_cache[key]

    nodes: dict[str, str] = {}
    edges: list[dict[str, object]] = []
    primary_profiles: list[dict[str, object]] = []
    quotient_profiles: list[dict[str, object]] = []
    second_profiles: list[dict[str, object]] = []
    source_state_keys: set[tuple[int, int]] = {
        (int(key[0]), int(key[1])) for key in source_rows
    }

    for row in repair_payload["records"]:
        if not row["candidates"]:
            continue
        prime = int(row["prime"])
        original_modulus = int(row["original_R"])
        orientation = str(row["orientation"])
        source_id = source_node_id(prime, original_modulus, orientation)
        nodes[source_id] = "source_F_state"
        source_key = (
            prime,
            original_modulus,
            tuple(int(value) for value in row["witness_exponents"]),
        )
        if source_key not in source_rows:
            raise AssertionError("a repair state is missing its factorization source")
        factors = [
            (int(q), int(exponent))
            for q, exponent in source_rows[source_key]["factorization"]
        ]
        original_omega = cached_omega(factors, original_modulus)
        if original_omega["omega"] <= 0:
            raise AssertionError("an overflow source unexpectedly hit the original box")

        for candidate_index, candidate in enumerate(row["candidates"]):
            gap = int(candidate["gap"])
            repaired_modulus = int(candidate["repaired_R"])
            repaired_K = int(candidate["repaired_K"])
            original_K = (prime * original_modulus + 1) // 4
            primary_id = primary_node_id(prime, repaired_modulus, orientation, gap)
            nodes[primary_id] = "legal_primary_repair_state"
            edges.append(
                {
                    "source": source_id,
                    "target": primary_id,
                    "kind": "primary_legal_repair",
                }
            )
            if not (repaired_modulus > original_modulus and repaired_K > original_K):
                raise AssertionError("primary repair did not strictly increase state height")
            primary_profiles.append(
                {
                    "prime": prime,
                    "orientation": orientation,
                    "original_modulus": original_modulus,
                    "gap": gap,
                    "repaired_modulus": repaired_modulus,
                    "original_K": original_K,
                    "repaired_K": repaired_K,
                    "modulus_strictly_increases": True,
                    "K_strictly_increases": True,
                    "modulus_bit_length_growth": (
                        repaired_modulus.bit_length() - original_modulus.bit_length()
                    ),
                    "direct_square_terminal": bool(
                        candidate["target_divisor_divides_first_square"]
                    ),
                    "inherits_F_factorization_or_witness": False,
                    "reenters_frozen_source_domain": (
                        (prime, repaired_modulus) in source_state_keys
                    ),
                }
            )

            if candidate["strict_balanced_reduction"]:
                lower_modulus = int(candidate["balanced_t"])
                quotient_id = quotient_node_id(prime, lower_modulus, orientation)
                nodes[quotient_id] = "lower_modulus_quotient_representation"
                edges.append(
                    {
                        "source": source_id,
                        "target": quotient_id,
                        "kind": "balanced_quotient_projection",
                    }
                )
                lower_omega = cached_omega(factors, lower_modulus)
                if lower_omega["omega"] > original_omega["omega"]:
                    raise AssertionError("quotient reduction increased the target-fiber cost")
                if not (
                    (lower_omega["omega"], lower_modulus)
                    < (original_omega["omega"], original_modulus)
                ):
                    raise AssertionError("the quotient lexicographic potential did not descend")
                left_residual = int(candidate["balanced_u_support_residual"])
                right_residual = int(candidate["balanced_v_support_residual"])
                escape_count = int(left_residual > 1) + int(right_residual > 1)
                if escape_count == 0:
                    raise AssertionError("the frozen quotient unexpectedly preserved both supports")
                source_factor_height = prime_factor_count_with_multiplicity(original_modulus)
                lower_factor_height = prime_factor_count_with_multiplicity(lower_modulus)
                if lower_factor_height >= source_factor_height:
                    raise AssertionError("proper factor quotient did not lower factor height")

                terminal_record = type_ii_rows.get(
                    (prime, original_modulus, orientation, lower_modulus)
                )
                terminal_count = (
                    0
                    if terminal_record is None
                    else int(terminal_record["type_ii_certificate_count"])
                )
                for certificate_index in range(terminal_count):
                    terminal_id = (
                        f"terminal:typeII:{prime}:{lower_modulus}:"
                        f"{orientation}:{certificate_index}"
                    )
                    nodes[terminal_id] = "type_II_certificate_terminal"
                    edges.append(
                        {
                            "source": quotient_id,
                            "target": terminal_id,
                            "kind": "shared_gap_type_II_terminal",
                        }
                    )
                quotient_profiles.append(
                    {
                        "prime": prime,
                        "orientation": orientation,
                        "original_modulus": original_modulus,
                        "gap": gap,
                        "lower_modulus": lower_modulus,
                        "classification": candidate["lower_modulus_classification"],
                        "original_omega_1": original_omega["omega"],
                        "lower_omega_1": lower_omega["omega"],
                        "omega_direction": (
                            "strict_decrease"
                            if lower_omega["omega"] < original_omega["omega"]
                            else "equal"
                        ),
                        "omega_R_lexicographic_strict_decrease": True,
                        "source_modulus_factor_height": source_factor_height,
                        "lower_modulus_factor_height": lower_factor_height,
                        "modulus_factor_height_drop": (
                            source_factor_height - lower_factor_height
                        ),
                        "K_support_prime_count": len(factors),
                        "K_support_prime_count_changes": False,
                        "support_escape_endpoint_count": escape_count,
                        "support_escape_product_bit_length": (
                            left_residual * right_residual
                        ).bit_length(),
                        "is_legal_type_I_modulus": lower_modulus % 4 == 3,
                        "shared_gap_type_II_terminal_count": terminal_count,
                        "has_proved_solution_lift": terminal_count > 0,
                        "reenters_frozen_source_domain": (
                            (prime, lower_modulus) in source_state_keys
                        ),
                    }
                )

            for second_gap in candidate["second_repair_gaps"]:
                second_gap = int(second_gap)
                repair_divisor = int(candidate["repair_divisor"])
                second_modulus = (4 * repair_divisor + 1) // second_gap
                second_id = second_node_id(
                    prime, second_modulus, f"{orientation}:{candidate_index}", second_gap
                )
                nodes[second_id] = "legal_second_repair_state"
                edges.append(
                    {
                        "source": primary_id,
                        "target": second_id,
                        "kind": "second_legal_repair",
                    }
                )
                second_profiles.append(
                    {
                        "prime": prime,
                        "orientation": orientation,
                        "original_modulus": original_modulus,
                        "primary_gap": gap,
                        "repair_divisor": repair_divisor,
                        "second_gap": second_gap,
                        "second_modulus": second_modulus,
                        "strictly_below_original_modulus": (
                            second_modulus < original_modulus
                        ),
                        "direct_square_terminal": second_gap
                        in candidate["second_repair_square_hits"],
                        "inherits_F_factorization_or_witness": False,
                        "reenters_frozen_source_domain": (
                            (prime, second_modulus) in source_state_keys
                        ),
                    }
                )

    # Re-entry is tested after the complete source domain has been collected.
    for profile in primary_profiles:
        profile["reenters_frozen_source_domain"] = (
            (int(profile["prime"]), int(profile["repaired_modulus"]))
            in source_state_keys
        )
    for profile in quotient_profiles:
        profile["reenters_frozen_source_domain"] = (
            (int(profile["prime"]), int(profile["lower_modulus"]))
            in source_state_keys
        )
    for profile in second_profiles:
        profile["reenters_frozen_source_domain"] = (
            (int(profile["prime"]), int(profile["second_modulus"]))
            in source_state_keys
        )

    if len(primary_profiles) != 149 or len(quotient_profiles) != 48:
        raise AssertionError("the frozen transition counts changed")
    if len(second_profiles) != 2:
        raise AssertionError("the frozen second-repair count changed")
    if any(profile["direct_square_terminal"] for profile in primary_profiles):
        raise AssertionError("a frozen primary repair unexpectedly became terminal")
    if any(profile["reenters_frozen_source_domain"] for profile in primary_profiles):
        raise AssertionError("a primary repair unexpectedly re-entered the frozen domain")
    if any(profile["reenters_frozen_source_domain"] for profile in quotient_profiles):
        raise AssertionError("a quotient unexpectedly re-entered the frozen domain")
    if any(profile["reenters_frozen_source_domain"] for profile in second_profiles):
        raise AssertionError("a second repair unexpectedly re-entered the frozen domain")

    omega_histogram = dict(
        sorted(Counter(int(row["lower_omega_1"]) for row in quotient_profiles).items())
    )
    f_miss_profiles = [
        row for row in quotient_profiles if row["classification"] == "F_box_miss"
    ]
    f_miss_omega_histogram = dict(
        sorted(Counter(int(row["lower_omega_1"]) for row in f_miss_profiles).items())
    )
    graph = graph_profile(nodes, edges)
    if not graph["acyclic"]:
        raise AssertionError("the frozen known-edge graph contains a directed cycle")

    return {
        "arithmetic": (
            "For t|R, the target fiber modulo R embeds in the target fiber modulo t, "
            "so Omega_1(t)<=Omega_1(R). If t<R, (Omega_1(t),t) is strictly smaller "
            "lexicographically. This ranks quotient representations, not legal Type-I "
            "states: every balanced t is 1 mod 4. Conversely, every primary legal repair "
            "has R'>R and K'>K."
        ),
        "scope_note": (
            "Complete graph audit for the frozen repair artifacts and their currently proved "
            "shared-gap Type-II terminals. Acyclicity is vacuous for global descent because "
            "none of the 151 derived legal states re-enters the frozen witness domain, and "
            "the 48 quotient nodes have no general solution lift."
        ),
        "repair_input": REPAIR_INPUT.name,
        "repair_input_sha256": repair_hash,
        "source_input": SOURCE_INPUT.name,
        "source_input_sha256": source_hash,
        "type_ii_input": TYPE_II_INPUT.name,
        "type_ii_input_sha256": type_ii_hash,
        "graph": graph,
        "primary_legal_repair_count": len(primary_profiles),
        "primary_modulus_increase_count": sum(
            bool(row["modulus_strictly_increases"]) for row in primary_profiles
        ),
        "primary_K_increase_count": sum(
            bool(row["K_strictly_increases"]) for row in primary_profiles
        ),
        "primary_direct_terminal_count": sum(
            bool(row["direct_square_terminal"]) for row in primary_profiles
        ),
        "primary_minimum_modulus_bit_length_growth": min(
            int(row["modulus_bit_length_growth"]) for row in primary_profiles
        ),
        "primary_maximum_modulus_bit_length_growth": max(
            int(row["modulus_bit_length_growth"]) for row in primary_profiles
        ),
        "strict_quotient_count": len(quotient_profiles),
        "quotient_omega_strict_decrease_count": sum(
            row["omega_direction"] == "strict_decrease" for row in quotient_profiles
        ),
        "quotient_omega_equal_count": sum(
            row["omega_direction"] == "equal" for row in quotient_profiles
        ),
        "quotient_omega_increase_count": 0,
        "quotient_omega_R_lexicographic_strict_decrease_count": sum(
            bool(row["omega_R_lexicographic_strict_decrease"])
            for row in quotient_profiles
        ),
        "quotient_legal_type_I_modulus_count": sum(
            bool(row["is_legal_type_I_modulus"]) for row in quotient_profiles
        ),
        "quotient_support_escape_endpoint_histogram": dict(
            sorted(
                Counter(
                    int(row["support_escape_endpoint_count"])
                    for row in quotient_profiles
                ).items()
            )
        ),
        "quotient_support_escape_product_bit_length_minimum": min(
            int(row["support_escape_product_bit_length"])
            for row in quotient_profiles
        ),
        "quotient_support_escape_product_bit_length_maximum": max(
            int(row["support_escape_product_bit_length"])
            for row in quotient_profiles
        ),
        "quotient_modulus_factor_height_strict_decrease_count": sum(
            int(row["modulus_factor_height_drop"]) > 0 for row in quotient_profiles
        ),
        "quotient_lower_omega_1_histogram": {
            str(key): value for key, value in omega_histogram.items()
        },
        "F_box_miss_exact_omega_1_histogram": {
            str(key): value for key, value in f_miss_omega_histogram.items()
        },
        "F_box_miss_exact_omega_1_minimum": min(
            int(row["lower_omega_1"]) for row in f_miss_profiles
        ),
        "F_box_miss_exact_omega_1_maximum": max(
            int(row["lower_omega_1"]) for row in f_miss_profiles
        ),
        "shared_gap_type_II_terminal_edge_count": sum(
            int(row["shared_gap_type_II_terminal_count"])
            for row in quotient_profiles
        ),
        "shared_gap_type_II_terminal_state_count": sum(
            int(row["shared_gap_type_II_terminal_count"]) > 0
            for row in quotient_profiles
        ),
        "unclosed_quotient_state_count": sum(
            int(row["shared_gap_type_II_terminal_count"]) == 0
            for row in quotient_profiles
        ),
        "second_legal_repair_count": len(second_profiles),
        "second_repair_strict_below_original_count": sum(
            bool(row["strictly_below_original_modulus"]) for row in second_profiles
        ),
        "second_repair_direct_terminal_count": sum(
            bool(row["direct_square_terminal"]) for row in second_profiles
        ),
        "derived_legal_state_count": len(primary_profiles) + len(second_profiles),
        "derived_legal_reentry_count": sum(
            bool(row["reenters_frozen_source_domain"])
            for row in primary_profiles + second_profiles
        ),
        "quotient_reentry_count": sum(
            bool(row["reenters_frozen_source_domain"])
            for row in quotient_profiles
        ),
        "potential_order_audit": {
            "ascending_R_then_other_on_primary_legal_edges": "fails_149_of_149",
            "ascending_Omega_then_R_on_quotient_edges": "strict_48_of_48",
            "ascending_R_then_other_on_quotient_edges": "strict_48_of_48",
            "ascending_support_escape_then_R_on_quotient_edges": "fails_48_of_48",
            "combined_legal_and_quotient_ranking": "not_defined_on_a_closed_state_space",
        },
        "missing_lift_conditions": [
            "A quotient modulus t is 1 mod 4 and is not a legal Type-I gap state.",
            "No marked source denominator n<p or map from a nonempty marked Sol(n) set is supplied.",
            "A primary or second legal repair does not inherit an F/G factorization witness for its new K.",
            "Support residuals are not proved to divide a Type-II endpoint or a common q-adic carrier.",
            "Omega_1 is not proved to pay q-adic capacity; it is equal on 26 quotient edges.",
            "Three lower-box hits and all 42 lower-box misses lack a proved shared-gap Type-II terminal.",
        ],
        "primary_profiles": primary_profiles,
        "quotient_profiles": quotient_profiles,
        "second_profiles": second_profiles,
        "edges": edges,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "graph",
                    "primary_legal_repair_count",
                    "primary_modulus_increase_count",
                    "primary_direct_terminal_count",
                    "strict_quotient_count",
                    "quotient_omega_strict_decrease_count",
                    "quotient_omega_equal_count",
                    "quotient_omega_R_lexicographic_strict_decrease_count",
                    "quotient_legal_type_I_modulus_count",
                    "F_box_miss_exact_omega_1_histogram",
                    "shared_gap_type_II_terminal_state_count",
                    "unclosed_quotient_state_count",
                    "second_legal_repair_count",
                    "derived_legal_reentry_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
