#!/usr/bin/env python3
"""Verify the gcd-shadow endpoint descent for terminal-free Type II reach.

The verifier is deliberately local.  It checks the universal arithmetic
projection, two terminal outcomes, two genuine edges, and the q=1 base
dichotomy.  It does not run a prime-range scan.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions.short_certificate import (
    certificate_at_gap,
    smallest_prime_factors,
    type_ii_residue_certificate,
    verify_certificate,
)
from reproductions.type_ii_relation_scc_proper_endpoint_descent import (
    endpoint_state,
    signed_box_profile,
    terminal_first_relation_reach,
)
from reproductions.type_ii_odd_kernel_overflow_natural_tail_relation_graph import (
    factorization,
)


def node_gcd_shadows(cofactor: int, node: tuple[int, int]) -> tuple[int, ...]:
    """Return the proper q-owned shadows of a bottom relation node."""
    if cofactor <= 1:
        raise AssertionError("gcd-shadow descent requires q > 1")
    first, second = node
    if first + second != 4 * cofactor - 1 or gcd(first, second) != 1:
        raise AssertionError("node is not a primitive endpoint bottom relation")
    shadows = tuple(
        sorted(
            {
                shadow
                for coordinate in node
                if (shadow := gcd(coordinate, cofactor)) < cofactor
            }
        )
    )
    if not shadows:
        raise AssertionError("both coordinates cannot be divisible by q")
    if any(cofactor % shadow for shadow in shadows):
        raise AssertionError("gcd shadow is not a divisor of q")
    return shadows


def q_one_base_profile(prime: int) -> dict[str, object]:
    """Classify the q=1 endpoint and verify that F-empty is impossible."""
    profile = signed_box_profile(prime, 1)
    if int(profile["gap"]) != 3 or int(profile["x"]) % 3 != 1:
        raise AssertionError("q=1 endpoint arithmetic changed")
    negative_generators = sorted(
        carrier
        for carrier in profile["factors"]
        if int(carrier) % 3 == 2
    )
    target_in_source = bool(profile["target_in_source_subgroup"])
    if target_in_source != bool(negative_generators):
        raise AssertionError("U(3) source-image dichotomy failed")
    if profile["classification"] == "F":
        raise AssertionError("q=1 cannot have an F-empty signed box")
    if target_in_source and profile["classification"] != "hit":
        raise AssertionError("a nontrivial U(3) generator did not hit the box")
    if not target_in_source and profile["classification"] != "G":
        raise AssertionError("trivial U(3) source image did not classify as G")
    return {
        **profile,
        "negative_generators_mod_3": negative_generators,
        "F_empty_impossible": True,
    }


def gcd_shadow_dispatch(
    prime: int, cofactor: int, initial_pair: tuple[int, int]
) -> dict[str, object]:
    """Dispatch a terminal-free reach through its q-owned gcd shadows."""
    source = endpoint_state(prime, cofactor)
    if cofactor == 1:
        return {
            "selector_status": "q_one_base",
            "base_profile": q_one_base_profile(prime),
        }

    source_profile = signed_box_profile(prime, cofactor)
    if source_profile["classification"] != "F":
        raise AssertionError("gcd-shadow source is not an F-empty endpoint")
    source_support = set(source_profile["factors"])
    if any(
        carrier not in source_support
        for carrier in factorization(initial_pair[0] * initial_pair[1])
    ):
        raise AssertionError("initial relation is not a real x-supported target preimage")

    reach = terminal_first_relation_reach(prime, cofactor, initial_pair)
    if reach["status"] != "terminal_free":
        return {"selector_status": "preempted", "relation_reach": reach}

    provenance: dict[int, list[dict[str, object]]] = {}
    for raw_node in reach["bottom_nodes"]:
        node = tuple(raw_node)
        for shadow in node_gcd_shadows(cofactor, node):
            provenance.setdefault(shadow, []).append(
                {"bottom_node": node, "gcd_shadow": shadow}
            )

    spf = smallest_prime_factors(prime // 2 + 2)
    candidates: list[dict[str, object]] = []
    for shadow in sorted(provenance):
        target = signed_box_profile(prime, shadow)
        short_certificate = certificate_at_gap(prime, int(target["gap"]), spf)
        type_ii_certificate = type_ii_residue_certificate(
            prime, int(target["gap"]), spf
        )
        for certificate in (short_certificate, type_ii_certificate):
            if certificate is not None and not verify_certificate(certificate):
                raise AssertionError("gcd-shadow terminal failed verification")
        if target["classification"] == "hit" and type_ii_certificate is None:
            raise AssertionError("gcd-shadow box hit did not reconstruct Type II")

        witness = min(
            provenance[shadow],
            key=lambda item: tuple(item["bottom_node"]),
        )
        node = tuple(witness["bottom_node"])
        gcd_matches = any(gcd(coordinate, cofactor) == shadow for coordinate in node)
        candidates.append(
            {
                "source_bottom_node": node,
                "all_shadow_provenance": provenance[shadow],
                "target": target,
                "short_certificate": (
                    None if short_certificate is None else asdict(short_certificate)
                ),
                "type_ii_certificate": (
                    None if type_ii_certificate is None else asdict(type_ii_certificate)
                ),
                "E1_premises": (
                    node in reach["bottom_nodes"]
                    and sum(node) == 4 * cofactor - 1
                    and gcd_matches
                    and cofactor % shadow == 0
                    and shadow < cofactor
                    and source_profile["classification"] == "F"
                ),
                "E2_construction": (
                    int(target["cofactor"]) == shadow
                    and int(target["gap"]) == 4 * shadow - 1
                    and int(target["x"]) == int(source["U"]) + shadow
                ),
                "E3_normal_form": (
                    int(source["U"]) % shadow == 0
                    and 4 * int(target["x"])
                    == prime + int(target["gap"])
                    and int(target["cofactor"])
                    <= int(target["endpoint_bound"])
                ),
                "E4_solution_lift": "identity_on_Sol(p)",
                "E5_rank": [cofactor, shadow],
                "E5_strict": shadow < cofactor,
            }
        )

    terminal_candidates = [
        candidate
        for candidate in candidates
        if candidate["short_certificate"] is not None
        or candidate["type_ii_certificate"] is not None
    ]
    selected = min(
        terminal_candidates or candidates,
        key=lambda candidate: int(candidate["target"]["cofactor"]),
    )
    for field in ("E1_premises", "E2_construction", "E3_normal_form", "E5_strict"):
        if not selected[field]:
            raise AssertionError(f"gcd-shadow receipt failed {field}")
    selected["selector_status"] = (
        "terminal_leaf" if terminal_candidates else "verified_edge"
    )
    selected["recursive_edge_eligible"] = not terminal_candidates
    selected["relation_reach"] = reach
    selected["source_profile"] = source_profile
    selected["all_shadow_cofactors"] = sorted(provenance)
    return selected


def verify() -> dict[str, object]:
    # Coordinate 1 is not a universal Reach conclusion.  This actual F-empty
    # source has a terminal-free five-node reach whose minimum coordinate is 2.
    no_one = gcd_shadow_dispatch(7_057, 36, (18, 125))
    if (
        no_one["selector_status"],
        min(node[0] for node in no_one["relation_reach"]["bottom_nodes"]),
        no_one["target"]["cofactor"],
        no_one["target"]["classification"],
    ) != ("terminal_leaf", 2, 1, "hit"):
        raise AssertionError("p=7057 no-coordinate-one boundary changed")

    q_coordinate = gcd_shadow_dispatch(47_713, 142, (142, 425))
    if (
        q_coordinate["selector_status"],
        q_coordinate["target"]["cofactor"],
        q_coordinate["short_certificate"]["gap"],
    ) != ("terminal_leaf", 2, 7):
        raise AssertionError("p=47713 q-coordinate shadow terminal changed")

    edge_1201 = gcd_shadow_dispatch(1_201, 3, (9, 101))
    if (
        edge_1201["selector_status"],
        edge_1201["target"]["cofactor"],
        edge_1201["target"]["classification"],
        edge_1201["E5_rank"],
    ) != ("verified_edge", 1, "G", [3, 1]):
        raise AssertionError("p=1201 gcd-shadow edge changed")

    edge_31249 = gcd_shadow_dispatch(31_249, 42, (14, 153))
    if (
        edge_31249["selector_status"],
        edge_31249["target"]["cofactor"],
        edge_31249["target"]["classification"],
        edge_31249["E5_rank"],
    ) != ("verified_edge", 1, "G", [42, 1]):
        raise AssertionError("p=31249 gcd-shadow edge changed")

    base_g = q_one_base_profile(73)
    base_hit = q_one_base_profile(97)
    if base_g["classification"] != "G" or base_g["negative_generators_mod_3"]:
        raise AssertionError("p=73 q=1 G base changed")
    if base_hit["classification"] != "hit" or base_hit["negative_generators_mod_3"] != [5]:
        raise AssertionError("p=97 q=1 hit base changed")

    return {
        "status": "verified",
        "no_coordinate_one_boundary": no_one,
        "q_coordinate_terminal": q_coordinate,
        "verified_edges": [edge_1201, edge_31249],
        "q_one_bases": [base_g, base_hit],
        "scope": "gcd-shadow projection and q=1 base only; no range scan",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = verify()
    if args.verify:
        print(result)


if __name__ == "__main__":
    main()
