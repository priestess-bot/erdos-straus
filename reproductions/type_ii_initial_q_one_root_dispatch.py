#!/usr/bin/env python3
"""Verify the p-only q=1 initial root terminal-or-edge dispatch.

The accompanying claim proves the universal factorization dichotomy. This
program replays stable serialization, direct Type-II terminal reconstruction,
and the inherited q=1 G handoff receipt on fixed controls. It performs no
prime-range scan and does not claim post-G Type-I totality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))

# Sibling verifiers are imported after the standalone-script path bootstrap.
import type_ii_q_one_full_carrier_phase_root_entry as q_one  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


INITIALIZER = "initial_q_one_root_dispatch_v1"
ROOT_TERMINAL = "root_terminal_leaf"
G_ENDPOINT = "type_ii_q_one_g_endpoint"


def digest(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def endpoint_bound(value: int) -> int:
    """Rebuild Q(value) for the q=1 endpoint-domain receipt."""
    if value < 1:
        raise AssertionError("endpoint bound requires a positive cofactor")
    k_zero = (value + 5) // 4
    denominator = 4 * k_zero - value - 1
    if denominator not in {1, 2, 3, 4}:
        raise AssertionError("endpoint-bound normal form changed")
    return k_zero * (k_zero + 1) // denominator


def root_data(prime: int) -> dict[str, object]:
    """Construct the p-only q=1 endpoint data before selecting an outcome."""
    if not (rail.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("initial dispatch requires a core prime")

    t = (prime - 1) // 24
    U = (prime - 1) // 4
    x_value = U + 1
    factors = rail.factorization(x_value)
    if not (
        t >= 3
        and U == 6 * t
        and x_value == 6 * t + 1
        and 4 * x_value == prime + 3
        and x_value % 3 == 1
        and 1 <= endpoint_bound(U)
        and all(prime_factor % 3 in {1, 2} for prime_factor in factors)
    ):
        raise AssertionError("canonical q=1 root arithmetic changed")

    return {
        "prime": prime,
        "t": t,
        "U": U,
        "x": x_value,
        "factorization": [[factor, exponent] for factor, exponent in sorted(factors.items())],
        "negative_mod_three_factors": sorted(
            factor for factor in factors if factor % 3 == 2
        ),
        "endpoint_downset_receipt": {
            "cofactor": 1,
            "cofactor_divides_U": True,
            "endpoint_bound": endpoint_bound(U),
            "within_endpoint_bound": True,
        },
    }


def initial_state(data: dict[str, object], classification: str) -> dict[str, object]:
    """Serialize the frozen root state without inventing an incoming edge."""
    prime = int(data["prime"])
    x_value = int(data["x"])
    negative_factors = list(data["negative_mod_three_factors"])
    if classification == "hit":
        target_fiber: dict[str, object] = {
            "status": "hit",
            "least_negative_factor": negative_factors[0],
        }
        terminal_prefix = {
            "scope": "complete_gap_three_direct_type_I_II_predicate",
            "outcome": "hit",
        }
        terminal_first_digest = {
            "scope": "q_one_gap_three_direct_type_I_II",
            "outcome": "hit",
            "complete_within_scope": True,
            "does_not_assert": "all_root_direct_certificate_families",
        }
    elif classification == "G":
        target_fiber = {
            "status": "empty",
            "canonical_separator": {
                "modulus": 3,
                "source_image": [1],
                "target_residue": 2,
                "character": "nontrivial_character_of_U(3)",
            },
        }
        terminal_prefix = {
            "scope": "complete_gap_three_direct_type_I_II_predicate",
            "outcome": "miss",
            "reason": "no prime factor of x is 2 modulo 3",
        }
        terminal_first_digest = {
            "scope": "q_one_gap_three_direct_type_I_II",
            "outcome": "miss",
            "complete_within_scope": True,
            "does_not_assert": "all_root_direct_certificate_families",
        }
    else:
        raise AssertionError("unknown q=1 initial-root classification")

    state: dict[str, object] = {
        "state_origin": INITIALIZER,
        "root_context": prime,
        "state_scope": "type_ii_endpoint_only",
        "phase": G_ENDPOINT if classification == "G" else "terminal_first",
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "endpoint": {
            "q": 1,
            "gap": 3,
            "first_denominator": x_value,
            "U": int(data["U"]),
        },
        "endpoint_downset_receipt": data["endpoint_downset_receipt"],
        "source_factorization": data["factorization"],
        "terminal_prefix": terminal_prefix,
        "terminal_first_digest": terminal_first_digest,
        "target_fiber": target_fiber,
        "initialization_provenance": {
            "kind": "frozen_p_only_root",
            "root_prime": prime,
            "construction": "q=1, m=3, x=(p+3)/4",
            "incoming_recursive_edge": False,
        },
    }
    state["state_id"] = "state:" + digest(state)
    return state


def type_ii_root_terminal(data: dict[str, object]) -> dict[str, object]:
    """Reconstruct the canonical gap-3 Type-II root certificate."""
    prime = int(data["prime"])
    x_value = int(data["x"])
    divisor = int(list(data["negative_mod_three_factors"])[0])
    quotient = x_value // divisor
    y_value = prime * (x_value + divisor) // 3
    z_value = prime * (x_value + x_value * x_value // divisor) // 3

    if not (
        x_value % divisor == 0
        and divisor <= x_value
        and divisor % 3 == 2
        and (x_value + divisor) % 3 == 0
        and (x_value + x_value * x_value // divisor) % 3 == 0
        and quotient % 3 == 2
        and 3 % 4 == 3
        and 3 <= prime - 2
        and Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value)
        == Fraction(4, prime)
    ):
        raise AssertionError("canonical gap-3 Type-II terminal did not replay")

    return {
        "certificate_type": "type_II_hit",
        "terminal_context": ROOT_TERMINAL,
        "root_context": prime,
        "short_bound": {"function": "p-2", "value": prime - 2},
        "gap": 3,
        "first_denominator": x_value,
        "divisor": divisor,
        "normal_form": {"A": 1, "B": quotient, "C": divisor},
        "denominators": [x_value, y_value, z_value],
        "root_equation_verified": True,
        "recursive_edge_eligible": False,
    }


def initial_dispatch(prime: int) -> dict[str, object]:
    """Return a root terminal or q=1 G edge after its local terminal pass."""
    data = root_data(prime)
    if data["negative_mod_three_factors"]:
        state = initial_state(data, "hit")
        return {
            "adapter": INITIALIZER,
            "selector_status": ROOT_TERMINAL,
            "initial_state": state,
            "terminal": type_ii_root_terminal(data),
            "recursive_edge_eligible": False,
        }

    state = initial_state(data, "G")
    handoff = q_one.phase_root_entry(prime)
    endpoint = handoff["endpoint"]
    endpoint_data = endpoint["endpoint"]
    e1 = bool(
        state["phase"] == G_ENDPOINT
        and endpoint_data == state["endpoint"]
        and endpoint["source_factorization"] == state["source_factorization"]
        and state["terminal_prefix"]["outcome"] == "miss"
        and state["terminal_first_digest"]["outcome"] == "miss"
        and state["terminal_first_digest"]["complete_within_scope"]
        and state["terminal_first_digest"]["does_not_assert"]
        == "all_root_direct_certificate_families"
        and state["target_fiber"]["status"] == "empty"
        and handoff["phase_reindexing_e1_e5"]["E1"]
    )
    edge = {
        "source_state_id": state["state_id"],
        "target_state_id": handoff["root"]["state_id"],
        "target_family": "type_i_full_carrier_post_g",
        "E1": e1,
        "E2": handoff["phase_reindexing_e1_e5"]["E2"],
        "E3": handoff["phase_reindexing_e1_e5"]["E3"],
        "E4": handoff["phase_reindexing_e1_e5"]["E4"],
        "E5": handoff["phase_reindexing_e1_e5"]["E5"],
        "E5_ticket": "PHASE_DROP",
        "solution_lift": "identity: Sol(p) -> Sol(p)",
        "terminal_first_digest": state["terminal_first_digest"],
        "target": handoff["root"],
    }
    if not all(edge[item] for item in ("E1", "E2", "E3", "E4", "E5")):
        raise AssertionError("initial q=1 G handoff lost an E1--E5 component")
    return {
        "adapter": INITIALIZER,
        "selector_status": "verified_edge",
        "initial_state": state,
        "edge": edge,
        "first_type_i_step": handoff["first_type_i_step"],
        "recursive_edge_eligible": True,
    }


def verify() -> None:
    controls = {
        73: ("verified_edge", None),
        97: (ROOT_TERMINAL, 5),
        193: ("verified_edge", None),
        241: ("verified_edge", None),
        337: (ROOT_TERMINAL, 5),
        1201: ("verified_edge", None),
    }
    for prime, (expected_status, expected_divisor) in controls.items():
        result = initial_dispatch(prime)
        if result["selector_status"] != expected_status:
            raise AssertionError(f"initial dispatch changed for p={prime}")
        if expected_divisor is not None:
            terminal = result["terminal"]
            if not (
                terminal["divisor"] == expected_divisor
                and terminal["root_equation_verified"]
                and not result["recursive_edge_eligible"]
            ):
                raise AssertionError(f"root terminal changed for p={prime}")
        else:
            edge = result["edge"]
            if not (
                all(edge[item] for item in ("E1", "E2", "E3", "E4", "E5"))
                and edge["E5_ticket"] == "PHASE_DROP"
                and result["recursive_edge_eligible"]
            ):
                raise AssertionError(f"initial G edge changed for p={prime}")

    for noncore in (25, 49, 71):
        try:
            initial_dispatch(noncore)
        except AssertionError:
            continue
        raise AssertionError("noncore input was accepted by the root serializer")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified canonical q=1 initial root terminal-or-edge dispatch")


if __name__ == "__main__":
    main()
