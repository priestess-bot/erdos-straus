#!/usr/bin/env python3
"""Verify the frozen-graph premises of the ordinary-G producer pruning claim."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "data" / "t6-proof-frontier-v2.json"


def verify() -> dict[str, object]:
    frontier = json.loads(FRONTIER.read_text(encoding="utf-8"))
    initializer = frontier["initializer"]
    if set(initializer["targets"]) != {
        "type_ii_relation_g_endpoint",
        "direct_terminal_leaf",
    }:
        raise AssertionError("initializer target surface changed")

    relation_targets = {"type_ii_relation_f_endpoint", "type_ii_relation_g_endpoint"}
    target_producers = []
    for edge in frontier["registered_edges"]:
        if relation_targets.intersection(edge["target_family_ids"]):
            target_producers.append(edge)
            if set(edge["source_family_ids"]) != {"type_ii_relation_f_endpoint"}:
                raise AssertionError("a non-F source can now seed a relation endpoint")

    if {edge["id"] for edge in target_producers} != {
        "type_ii_proper_endpoint_descent",
        "type_ii_gcd_shadow_endpoint_descent",
    }:
        raise AssertionError("relation producer set changed")

    g_exits = {
        edge["id"]: edge
        for edge in frontier["registered_edges"]
        if edge["source_family_ids"] == ["type_ii_relation_g_endpoint"]
    }
    if set(g_exits) != {
        "q_one_g_full_carrier_phase_root",
        "positive_q_g_full_carrier_phase_root",
        "q_one_g_c3_source_lineage_relay",
    }:
        raise AssertionError("ordinary G exit surface changed")
    if any(edge["target_family_ids"] != ["type_i_full_carrier_post_g"] for edge in g_exits.values()):
        raise AssertionError("ordinary G exit target family changed")

    return {
        "status": "FROZEN_GRAPH_PREMISES_REPLAYED",
        "initializer_nonterminal_G_q": 1,
        "relation_target_producers": sorted(edge["id"] for edge in target_producers),
        "relation_target_producer_source": "type_ii_relation_f_endpoint",
        "positive_q_G_seed": False,
        "requested_selected_G_exit": "q_one_g_full_carrier_phase_root",
        "requested_nonrecursive_alternates": [
            "positive_q_g_full_carrier_phase_root",
            "q_one_g_c3_source_lineage_relay",
        ],
        "scope": "frozen_selected_graph_not_abstract_arithmetic_family",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(verify()["status"])


if __name__ == "__main__":
    main()
