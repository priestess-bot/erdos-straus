#!/usr/bin/env python3
"""Replay the arithmetic core of the marked-G complete-excess adapter.

This is a focused p=601 control for the raw source, full-block bundle,
canonical target, local G typing, identity lift, and parent-to-target T5
comparison.  It does not construct a universal E3 owner, serializer, or
recursive re-entry proof for the target.
"""

from __future__ import annotations

import argparse
import json
from math import lcm

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def sharp_rank(prime: int, K: int, support: int) -> tuple[int, int]:
    if support <= 0 or K % support:
        raise AssertionError("charged support must divide K")
    bound = (prime - 1) ** 2 // 4
    return bound // support, K // support


def full_excess(selected: int, K: int) -> tuple[int, int]:
    K_factors = bottom.factorization(K)
    Q = 1
    beta = 1
    for q, exponent in bottom.factorization(selected).items():
        if exponent > K_factors.get(q, 0):
            Q *= q**exponent
        else:
            beta *= q**exponent
    return Q, beta


def jacobi_g_receipt(R: int, K: int) -> dict[str, object]:
    factors = bottom.factorization(K)
    values = {str(q): bottom.jacobi_symbol(q, R) for q in factors}
    minus_one = bottom.jacobi_symbol(-1, R)
    if not all(value == 1 for value in values.values()) or minus_one != -1:
        raise AssertionError("chart is not certified G by its Jacobi separator")
    return {
        "classification": "G",
        "support_factorization": [[q, exponent] for q, exponent in factors.items()],
        "separator": {
            "kind": "Jacobi",
            "modulus": R,
            "support_values": values,
            "minus_one": minus_one,
        },
    }


def p601_control() -> dict[str, object]:
    prime, R, K, support = 601, 599, 90_000, 1
    bound = (prime - 1) ** 2 // 4
    if not (
        prime % 24 == 1
        and 4 * K == prime * R + 1
        and 3 <= R <= prime - 2
        and K % support == 0
        and K <= bound
    ):
        raise AssertionError("p=601 source chart changed")

    source_fiber = jacobi_g_receipt(R, K)
    source = (prime, R * (prime - 1) - prime, prime - 1)
    anchor, shift, common = bottom.formal_transition(
        source, prime, R, bottom.factorization(K)
    )
    if (anchor, shift, common) != ((1, 598, 1), 1, 1):
        raise AssertionError("universal p-source edge changed")

    Q, beta = full_excess(anchor[1], K)
    residual = anchor[0] * beta
    target_support = lcm(support, Q)
    if not (
        (Q, beta, residual, target_support) == (299, 2, 2, 299)
        and residual > 0
        and K % residual == 0
        and K % Q != 0
        and target_support // support >= 2
    ):
        raise AssertionError("complete-excess receipt changed")

    target_R, target_K = bottom.canonical_chart(prime, target_support)
    if (target_R, target_K) != (199, 29_900):
        raise AssertionError("canonical target changed")
    target_fiber = jacobi_g_receipt(target_R, target_K)

    source_rank = sharp_rank(prime, K, support)
    target_rank = sharp_rank(prime, target_K, target_support)
    if not target_rank < source_rank:
        raise AssertionError("real parent-to-target T5 rank did not descend")

    terminal = (152, 13_053, 62_758_824)
    x, y, z = terminal
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("p=601 root-terminal control changed")

    return {
        "source_state": {
            "p": prime,
            "R": R,
            "K": K,
            "A": support,
            "fiber": source_fiber,
            "rank": list(source_rank),
        },
        "E1": {
            "universal_source": list(source),
            "q": prime,
            "shift": shift,
            "gcd_reduction": common,
            "anchor": list(anchor),
            "Q": Q,
            "beta": beta,
            "residual": residual,
        },
        "E2_target_typing_control": {
            "target_state": {
                "p": prime,
                "R": target_R,
                "K": target_K,
                "A": target_support,
                "fiber": target_fiber,
                "rank": list(target_rank),
            },
            "classification_was_recomputed": True,
            "target_owner_and_reentry_proved": False,
        },
        "E4": "identity_on_Sol(4,p)",
        "E5": {
            "ticket": "LOCAL_DROP",
            "source_rank": list(source_rank),
            "target_rank": list(target_rank),
        },
        "root_terminal_preemption_control": list(terminal),
        "global_scope": {
            "local_M_adapter": "CONDITIONAL_ON_E3_AND_SURFACE_ADMISSION",
            "F1_reachable_state_exhaustion": "OPEN",
            "registered_on_frozen_v2_surface": False,
        },
    }


def run() -> dict[str, object]:
    return {
        "theorem": "type-I-marked-g-universal-anchor-complete-excess-exit",
        "control": p601_control(),
        "status": "conditional_control_verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.verify:
        print("verified marked-G anchor complete-excess arithmetic control")
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
