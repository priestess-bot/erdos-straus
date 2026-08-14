#!/usr/bin/env python3
"""Verify the q=1 G full-carrier phase-root reindexing receipt.

This is a focused algebraic and state-contract verifier.  It checks the
target-independent root formula, the target-side universal raw source, the
ordinary Sol(p) identity lift, the one-way phase prefix, and the first strict
Type I support step.  It does not search for certificates or claim that the
remaining Type I selector is total.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd

import type_ii_q_one_type_i_carrier_rail_dispatch as rail


ADAPTER = "q_one_full_carrier_phase_root_entry_v1"
SOURCE_SCOPE = "fresh_source_tree_only"
ROOT_PHASE = "type_i_full_carrier_tree"
ENDPOINT_PHASE = "type_ii_q_one_g_endpoint"
PHASE_RANK = {"type_ii_q_one_g_endpoint": 2, "type_i_full_carrier_tree": 1, "smaller_denominator": 0}


def digest(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def q_one_g_endpoint(prime: int) -> dict[str, object]:
    """Rebuild the ordinary q=1 G endpoint from p, not cached labels."""
    if not (rail.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("q=1 endpoint requires a core prime")
    t = (prime - 1) // 24
    U = (prime - 1) // 4
    X = U + 1
    factors = rail.factorization(X)
    source_residues = {factor: factor % 3 for factor in factors}
    if not (
        t >= 3
        and X == 6 * t + 1
        and prime + 3 == 4 * X
        and all(residue == 1 for residue in source_residues.values())
    ):
        raise AssertionError("control is not a q=1 G endpoint")
    return {
        "phase": ENDPOINT_PHASE,
        "phase_rank": PHASE_RANK[ENDPOINT_PHASE],
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "endpoint": {"q": 1, "gap": 3, "first_denominator": X, "U": U},
        "source_factorization": [[factor, exponent] for factor, exponent in factors.items()],
        "source_residues_mod_3": source_residues,
        "target_fiber": {
            "status": "empty",
            "separator": "all q=1 source generators are 1 modulo 3",
        },
        "state_scope": "type_ii_endpoint_only",
    }


def universal_root_source(prime: int, R: int, K: int) -> dict[str, object]:
    """Reconstruct the p-raw source and its unique p-edge to the anchor."""
    source = (prime, R * (prime - 1) - prime, prime - 1)
    anchor = (1, R - 1, 1)
    if not (
        min(source) > 0
        and source[0] + source[1] == R * source[2]
        and gcd(source[0], source[1]) == 1
        and K % prime != 0
        and source[0] % prime == 0
        and (source[1] + R) % prime == 0
        and (source[2] + 1) % prime == 0
        and (source[0] // prime, (source[1] + R) // prime, (source[2] + 1) // prime) == anchor
    ):
        raise AssertionError("universal p source did not replay")
    return {
        "source": list(source),
        "q": prime,
        "shift": 1,
        "gcd_reduction": 1,
        "destination": list(anchor),
    }


def phase_root_entry(prime: int) -> dict[str, object]:
    """Build the q=1 G -> full-carrier root phase-reindexing receipt."""
    endpoint = q_one_g_endpoint(prime)
    t = (prime - 1) // 24
    X = (prime + 3) // 4
    carrier = rail.carrier_chart(prime, X)
    R, K = carrier["R"], carrier["K"]
    source = universal_root_source(prime, R, K)
    dispatch = rail.full_carrier_dispatch(prime)
    if carrier != dispatch["root"]:
        raise AssertionError("root receipt and carrier dispatch disagree")

    B_p = (prime - 1) ** 2 // 4
    root_state = {
        "adapter": ADAPTER,
        "state_origin": ADAPTER,
        "source_tree_scope": SOURCE_SCOPE,
        "normal_form": "type_i_full_carrier_low_root_v1",
        "phase": ROOT_PHASE,
        "phase_rank": PHASE_RANK[ROOT_PHASE],
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "chart": {"R": R, "K": K},
        "absorbed_support": 1,
        "carrier": X,
        "raw_source_digest": digest(source),
    }
    root_state["state_id"] = "state:" + digest(root_state)

    target = dispatch["dispatch"]
    support = int(target["support"])
    target_K = int(target["K"])
    if not (
        support > 1
        and target_K % support == 0
        and B_p // support < B_p
        and target["R"] < prime
        and prime * int(target["R"]) + 1 == 4 * target_K
    ):
        raise AssertionError("first Type I strict step did not replay")

    phase_policy = {
        "rank_order": PHASE_RANK,
        "allowed_nonterminal_transitions": [
            [ENDPOINT_PHASE, ROOT_PHASE],
            [ROOT_PHASE, ROOT_PHASE],
            [ROOT_PHASE, "smaller_denominator"],
        ],
        "forbidden_nonterminal_transition": [ROOT_PHASE, ENDPOINT_PHASE],
        "type_ii_after_root": "terminal_leaf_only",
    }
    source_potential = [PHASE_RANK[ENDPOINT_PHASE], 1, 0]
    root_potential = [PHASE_RANK[ROOT_PHASE], B_p, K]
    first_target_potential = [PHASE_RANK[ROOT_PHASE], B_p // support, target_K // support]

    e1_e5 = {
        "E1": bool(
            endpoint["endpoint"] == {"q": 1, "gap": 3, "first_denominator": X, "U": X - 1}
            and source["destination"] == [1, R - 1, 1]
        ),
        "E2": bool(
            R == 16 * t + 3
            and K == X * (16 * t + 1)
            and root_state["state_origin"] == ADAPTER
        ),
        "E3": bool(
            3 <= R <= prime - 2
            and gcd(X, K) == X
            and root_state["source_tree_scope"] == SOURCE_SCOPE
            and root_state["absorbed_support"] == 1
        ),
        "E4": bool(
            endpoint["equation_target"] == root_state["equation_target"]
            and endpoint["marked_solution_set"] == root_state["marked_solution_set"] == "Sol(p)"
        ),
        "E5": bool(
            source_potential > root_potential
            and phase_policy["forbidden_nonterminal_transition"] == [ROOT_PHASE, ENDPOINT_PHASE]
        ),
    }
    if not all(e1_e5.values()):
        failed = [name for name, passed in e1_e5.items() if not passed]
        raise AssertionError(f"phase-root entry failed: {failed}")
    if not root_potential > first_target_potential:
        raise AssertionError("root's first Type I edge is not strict in the local component")

    return {
        "adapter": ADAPTER,
        "endpoint": endpoint,
        "root": root_state,
        "root_source": source,
        "phase_policy": phase_policy,
        "phase_reindexing_e1_e5": e1_e5,
        "solution_lift": "identity: Sol(p) -> Sol(p)",
        "potentials": {
            "endpoint": source_potential,
            "root": root_potential,
            "first_type_i_target": first_target_potential,
        },
        "first_type_i_step": target,
        "scope": {
            "terminal_first": "required before this optional nonterminal handoff",
            "phase_entry": "one-way by the declared policy",
            "not_proved": [
                "a total Type I selector after the first step",
                "a global exit for every Type I state",
                "a strict smaller-denominator descendant for this branch",
            ],
        },
    }


def verify() -> dict[str, object]:
    controls = {prime: phase_root_entry(prime) for prime in (73, 241, 2521, 118801, 76129)}
    expected = {
        73: {"R": 51, "K": 931, "kind": "marked_absorb", "support": 50},
        241: {"R": 163, "K": 9821, "kind": "fixed_n_edge", "support": 45},
        2521: {"R": 1683, "K": 1060711, "kind": "marked_absorb", "support": 1682},
        118801: {"R": 79203, "K": 2352348901, "kind": "fixed_n_edge", "support": 22275},
        76129: {"R": 50755, "K": 965981849, "kind": "fixed_n_edge", "support": 14274},
    }
    for prime, receipt in controls.items():
        root = receipt["root"]
        step = receipt["first_type_i_step"]
        check = expected[prime]
        if not (
            root["chart"] == {"R": check["R"], "K": check["K"]}
            and step["kind"] == check["kind"]
            and step["support"] == check["support"]
            and all(receipt["phase_reindexing_e1_e5"].values())
            and receipt["potentials"]["endpoint"] > receipt["potentials"]["root"]
            and receipt["potentials"]["root"] > receipt["potentials"]["first_type_i_target"]
        ):
            raise AssertionError(f"phase-root control changed for p={prime}")
    if controls[76129]["endpoint"]["source_factorization"] != [[7, 1], [2719, 1]]:
        raise AssertionError("nontrivial q=1 G factorization control changed")
    return {
        "status": "verified",
        "controls": controls,
        "scope": "Target-independent q=1 G phase-root admission and first strict Type I segment only.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
