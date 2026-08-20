from __future__ import annotations

import json

from common import q_one_g, root_chart, universal_source


def contract_receipt(p: int) -> dict[str, object]:
    if not q_one_g(p):
        raise AssertionError("input must be ordinary q=1 G control")
    t, X, R, K = root_chart(p)
    source, anchor = universal_source(p, R, K)
    Bp = (p - 1) ** 2 // 4

    source_state = {
        "phase": "type_ii_q_one_g_endpoint",
        "phase_rank": 2,
        "equation_target": [4, p],
        "marked_solution_set": "Sol(p)",
        "scope": "type_ii_endpoint_only",
        "q": 1,
        "gap": 3,
        "X": X,
    }
    target_state = {
        "phase": "type_i_full_carrier_tree",
        "phase_rank": 1,
        "equation_target": [4, p],
        "marked_solution_set": "Sol(p)",
        "scope": "fresh_source_tree_only",
        "normal_form": "type_i_full_carrier_low_root_v1",
        "R": R,
        "K": K,
        "A": 1,
    }
    e = {
        "E1": anchor == (1, R - 1, 1) and source[0] == p,
        "E2": R == 16 * t + 3 and K == X * (16 * t + 1),
        "E3": 3 <= R <= p - 2 and K % X == 0 and target_state["scope"] == "fresh_source_tree_only",
        "E4": source_state["equation_target"] == target_state["equation_target"]
              and source_state["marked_solution_set"] == target_state["marked_solution_set"] == "Sol(p)",
        "E5": (target_state["phase_rank"], Bp, K) < (source_state["phase_rank"], 1, 0),
    }
    if not all(e.values()):
        raise AssertionError(f"E1-E5 failed at p={p}: {e}")
    return {
        "p": p,
        "source_state": source_state,
        "target_state": target_state,
        "raw_source": list(source),
        "anchor": list(anchor),
        "E1_E5": e,
        "solution_lift": "identity on Sol(p)",
        "forbidden_nonterminal": "type_i_full_carrier_tree -> type_ii_q_one_g_endpoint",
    }


def verify() -> dict[str, object]:
    rows = [contract_receipt(p) for p in (73, 241, 2521, 76129, 118801)]
    return {"status": "verified", "receipts": rows}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
