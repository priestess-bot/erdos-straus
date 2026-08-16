#!/usr/bin/env python3
"""Verify the conditional q=1 G -> c=3 source-lineage phase relay.

The raw c=3 word is never treated as a chain of recursive selector edges.
Instead, this verifier accepts a replayable transcript beginning at the
predeclared universal p-source, preserves the descendant of its first
coordinate, and builds a fresh root only as the target of the named q=1 G
phase reindexing.  The following d=3 RESET is then checked separately.
"""

from __future__ import annotations

import argparse
import hashlib
import json

import type_i_c3_affine_prime_even_tail_root_entry as c3
import type_i_high_r_chart_two_anchor as shared
import type_ii_q_one_full_carrier_phase_root_entry as q_one


ADAPTER = "q_one_c3_source_lineage_phase_root_entry_v1"
RAW_ENTRY_ADAPTER = "c3_source_lineage_even_tail_root_receipt_v1"
SOURCE_SCOPE = "fresh_source_tree_only"
ENDPOINT_PHASE = "type_ii_q_one_g_endpoint"
ROOT_PHASE = "type_i_c3_source_lineage_tree"
SMALLER_PHASE = "smaller_denominator"
PHASE_RANK = {
    ENDPOINT_PHASE: 2,
    ROOT_PHASE: 1,
    SMALLER_PHASE: 0,
}


def digest(payload: object) -> str:
    """Return the canonical content digest used by this receipt family."""
    encoded = json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def as_node(value: object, *, name: str) -> tuple[int, int, int]:
    """Parse an ordered primitive-node payload without accepting loose shapes."""
    if not isinstance(value, (list, tuple)) or len(value) != 3 or not all(isinstance(item, int) for item in value):
        raise AssertionError(f"{name}: expected an integer triple")
    return tuple(value)


def c3_parameters(prime: int) -> dict[str, int]:
    """Recompute the target-independent c=3 chart prescribed by p."""
    if not (shared.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("c=3 phase relay requires a core prime p = 1 mod 24")
    h = (prime - 1) // 24
    R = 104 * h - 9
    M = 26 * h + 1
    x = prime - 3
    K = M * x
    checks = {
        "h_minimum": h >= 3,
        "c3_branch": h % 3 != 2,
        "thirteen_capacity_branch": h % 13 != 12,
        "high_chart": R > prime and R % 4 == 3,
        "canonical_chart": shared.canonical_chart(prime, M) == (R, K),
        "determinant": prime * R + 1 == 4 * K,
        "tail_identity": R == 4 * M - 13,
        "d3_dual": prime * 13 == 4 * M * 3 + 1,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"c=3 chart preconditions failed: {failed}")
    return {"p": prime, "h": h, "R": R, "M": M, "x": x, "K": K}


def raw_action(
    *,
    name: str,
    source: tuple[int, int, int],
    selected_coordinate_index: int,
    q: int,
    destination: tuple[int, int, int],
) -> dict[str, object]:
    """Build one serializable raw action for a supplied transcript."""
    return {
        "kind": "raw",
        "name": name,
        "source": list(source),
        "selected_coordinate_index": selected_coordinate_index,
        "q": q,
        "destination": list(destination),
    }


def canonical_anchor_swap(R: int) -> dict[str, object]:
    """Record the sole metadata swap admitted by the p-first c=3 grammar."""
    return {
        "kind": "coordinate_swap",
        "name": "canonical_p_anchor_orientation",
        "source": [1, R - 1, 1],
        "destination": [R - 1, 1, 1],
    }


def affine_prime_actions(h: int, a: int, b: int) -> list[dict[str, object]]:
    """Construct the declared p-first two-intermediate c=3 raw word."""
    if h < 3 or a <= 0 or b <= 0:
        raise AssertionError("affine c=3 action parameters must be positive")
    p = 24 * h + 1
    R = 104 * h - 9
    x = p - 3
    alpha = (R - 1) // b
    beta = (R - b) // a
    gamma = (R - a) // 8
    if (R - 1) % b or (R - b) % a or (R - a) % 8:
        raise AssertionError("two-intermediate action divisibilities failed")
    source = (p, R * (p - 1) - p, p - 1)
    return [
        raw_action(
            name="universal_p_edge",
            source=source,
            selected_coordinate_index=0,
            q=p,
            destination=(1, R - 1, 1),
        ),
        canonical_anchor_swap(R),
        raw_action(
            name="anchor_to_b",
            source=(R - 1, 1, 1),
            selected_coordinate_index=0,
            q=alpha,
            destination=(b, R - b, 1),
        ),
        raw_action(
            name="b_to_a",
            source=(b, R - b, 1),
            selected_coordinate_index=1,
            q=beta,
            destination=(a, R - a, 1),
        ),
        raw_action(
            name="a_to_4gamma",
            source=(a, R - a, 1),
            selected_coordinate_index=1,
            q=2,
            destination=(4 * gamma, R - 4 * gamma, 1),
        ),
        raw_action(
            name="4gamma_to_4",
            source=(4 * gamma, R - 4 * gamma, 1),
            selected_coordinate_index=0,
            q=gamma,
            destination=(4, R - 4, 1),
        ),
        raw_action(
            name="4_to_t4",
            source=(4, R - 4, 1),
            selected_coordinate_index=1,
            q=13,
            destination=(R - 4 * x, 4 * x, 1),
        ),
        raw_action(
            name="t4_to_t2",
            source=(R - 4 * x, 4 * x, 1),
            selected_coordinate_index=1,
            q=2,
            destination=(2 * x, R - 2 * x, 1),
        ),
        raw_action(
            name="t2_to_t1",
            source=(2 * x, R - 2 * x, 1),
            selected_coordinate_index=0,
            q=2,
            destination=(x, R - x, 1),
        ),
    ]


def p1009_bypass_actions() -> list[dict[str, object]]:
    """Return the fixed non-p-first control as ordinary source actions."""
    return [
        raw_action(
            name="source_bypass_349",
            source=(1009, 4392863, 1008),
            selected_coordinate_index=1,
            q=349,
            destination=(12587, 490, 3),
        ),
        raw_action(
            name="source_bypass_41",
            source=(12587, 490, 3),
            selected_coordinate_index=0,
            q=41,
            destination=(307, 4052, 1),
        ),
        raw_action(
            name="source_bypass_1013",
            source=(307, 4052, 1),
            selected_coordinate_index=1,
            q=1013,
            destination=(4, 4355, 1),
        ),
        raw_action(
            name="source_bypass_13",
            source=(4, 4355, 1),
            selected_coordinate_index=1,
            q=13,
            destination=(335, 4024, 1),
        ),
        raw_action(
            name="source_bypass_2a",
            source=(335, 4024, 1),
            selected_coordinate_index=1,
            q=2,
            destination=(2012, 2347, 1),
        ),
        raw_action(
            name="source_bypass_2b",
            source=(2012, 2347, 1),
            selected_coordinate_index=0,
            q=2,
            destination=(1006, 3353, 1),
        ),
    ]


def replay_source_lineage(prime: int, actions: list[dict[str, object]]) -> dict[str, object]:
    """Replay a declared-source word and prove its c=3 tail source mark.

    A coordinate swap is metadata only.  It is accepted exactly once, only
    immediately after the canonical p-edge from the declared source.  Raw
    source-bypass words are also accepted, but every action must still replay
    from that same predeclared source.
    """
    params = c3_parameters(prime)
    R, M, x, K = (params[name] for name in ("R", "M", "x", "K"))
    universal = shared.high_R_universal_source(prime, R)
    source = as_node(universal["source"], name="universal source")
    if not actions:
        raise AssertionError("source-lineage transcript is empty")

    current = source
    p_line_index = 0
    p_line = prime
    transport = 1
    rows: list[dict[str, object]] = []
    lineage: list[dict[str, object]] = []
    swap_count = 0
    previous_was_canonical_p_edge = False

    for action_index, action in enumerate(actions, start=1):
        if not isinstance(action, dict):
            raise AssertionError("source-lineage action must be a mapping")
        kind = action.get("kind")
        if kind == "coordinate_swap":
            swap_source = as_node(action.get("source"), name="swap source")
            swap_destination = as_node(action.get("destination"), name="swap destination")
            if not (
                swap_count == 0
                and previous_was_canonical_p_edge
                and current == (1, R - 1, 1)
                and swap_source == current
                and swap_destination == (R - 1, 1, 1)
                and p_line_index == 0
                and p_line == 1
            ):
                raise AssertionError("coordinate swap is outside the canonical p-anchor exception")
            current = swap_destination
            p_line_index = 1
            swap_count += 1
            previous_was_canonical_p_edge = False
            continue
        if kind != "raw":
            raise AssertionError("source-lineage action must be raw or the one admitted swap")

        action_source = as_node(action.get("source"), name="raw source")
        action_destination = as_node(action.get("destination"), name="raw destination")
        side = action.get("selected_coordinate_index")
        q = action.get("q")
        name = action.get("name")
        if not isinstance(side, int) or not isinstance(q, int) or not isinstance(name, str):
            raise AssertionError("raw action has malformed fields")
        if action_source != current:
            raise AssertionError(f"{name}: transcript did not continue from the prior node")
        row = c3.ordered_raw_step(
            modulus=R,
            K=K,
            source=current,
            selected_coordinate_index=side,
            q=q,
            expected_destination=action_destination,
            name=name,
        )
        if not row["strict_capacity"] or not row["unit_condition"]:
            raise AssertionError(f"{name}: raw action is not admissible")
        reduction = int(row["gcd_reduction"])
        next_p_line_index = 0 if p_line_index == side else 1
        next_p_line = action_destination[next_p_line_index]
        if q * reduction * next_p_line % R != p_line % R:
            raise AssertionError(f"{name}: source-coordinate transport changed")
        transport = transport * q * reduction % R
        if transport * next_p_line % R != prime % R:
            raise AssertionError(f"{name}: accumulated source transport changed")
        rows.append(row)
        lineage.append(
            {
                "raw_step": len(rows),
                "action_index": action_index,
                "q": q,
                "gcd_reduction": reduction,
                "source_coordinate_index": p_line_index,
                "destination_coordinate_index": next_p_line_index,
                "p_line": next_p_line,
                "transport_product_mod_R": transport,
            }
        )
        previous_was_canonical_p_edge = bool(
            len(rows) == 1
            and current == source
            and side == 0
            and q == prime
            and action_destination == (1, R - 1, 1)
        )
        current = action_destination
        p_line = next_p_line
        p_line_index = next_p_line_index

    if len(rows) < 3:
        raise AssertionError("source-lineage transcript lacks the c=3 even tail")
    if current[2] != 1 or {current[0], current[1]} != {x, R - x}:
        raise AssertionError("source-lineage transcript did not reach the c=3 complement seed")
    tail_rows = rows[-3:]
    tail_lineage = lineage[-3:]
    expected_labels = [13, 2, 2]
    expected_t = [4, 2, 1]
    if [int(row["q"]) for row in tail_rows] != expected_labels:
        raise AssertionError("source-lineage tail labels are not 13,2,2")

    orientation: int | None = None
    tail: list[dict[str, object]] = []
    sigma = (-pow(prime, -1, R)) % R
    for row, line, t in zip(tail_rows, tail_lineage, expected_t):
        destination = as_node(row["destination"], name="tail destination")
        if destination[2] != 1 or {destination[0], destination[1]} != {t * x, R - t * x}:
            raise AssertionError("source-lineage tail left the required physical row")
        p_coordinate = int(line["p_line"])
        step_orientation = 1 if p_coordinate == t * x else -1 if p_coordinate == R - t * x else 0
        if step_orientation == 0:
            raise AssertionError("source lineage is not on either c=3 tail orientation")
        if orientation is None:
            orientation = step_orientation
        elif orientation != step_orientation:
            raise AssertionError("source-lineage tail orientation changed")
        theta = sigma * int(line["transport_product_mod_R"]) % R
        expected_theta = (-step_orientation * (4 * M // t)) % R
        if not (
            theta == expected_theta
            and theta * p_coordinate % R == R - 1
            and int(line["transport_product_mod_R"]) * p_coordinate % R == prime % R
        ):
            raise AssertionError("source-lineage normalized tail mark changed")
        tail.append(
            {
                "t": t,
                "destination": list(destination),
                "p_line": p_coordinate,
                "orientation": step_orientation,
                "theta": theta,
                "expected_theta": expected_theta,
            }
        )
    if orientation is None:
        raise AssertionError("source-lineage tail orientation was not defined")

    raw_transcript = {
        "source": list(source),
        "actions": actions,
        "replayed_raw_rows": rows,
        "swap_count": swap_count,
        "final_node": list(current),
    }
    lineage_payload = {
        "source_mark_sigma": sigma,
        "rows": lineage,
        "tail": tail,
        "tail_orientation": orientation,
    }
    return {
        "parameters": params,
        "universal_source": universal,
        "raw_transcript": raw_transcript,
        "lineage": lineage_payload,
        "raw_entry_digest": "raw-receipt:" + digest(raw_transcript),
        "lineage_digest": "lineage:" + digest(lineage_payload),
        "E1": True,
    }


def state_id_is_valid(state: dict[str, object]) -> bool:
    """Validate the extended state identity used by the source-lineage root."""
    core = {key: value for key, value in state.items() if key != "state_id"}
    return state.get("state_id") == "state:" + digest(core)


def source_lineage_root_entry(
    *,
    prime: int,
    actions: list[dict[str, object]],
    fiber_declaration: dict[str, object],
) -> dict[str, object]:
    """Create the E1--E3 c=3 root receipt used only by the named relay."""
    replay = replay_source_lineage(prime, actions)
    params = replay["parameters"]
    if not isinstance(params, dict):
        raise AssertionError("c=3 parameter receipt changed shape")
    R, K = int(params["R"]), int(params["K"])
    fiber = c3.materialize_typed_fiber(R=R, K=K, declaration=fiber_declaration)
    typed_fiber = c3.typed_fiber_payload(fiber)
    typed_fiber_digest = "fiber:" + digest(fiber)
    root = {
        "adapter": RAW_ENTRY_ADAPTER,
        "state_origin": RAW_ENTRY_ADAPTER,
        "source_tree_scope": SOURCE_SCOPE,
        "normal_form": "c3_source_lineage_even_tail_overflow_seed_v1",
        "phase": ROOT_PHASE,
        "phase_rank": PHASE_RANK[ROOT_PHASE],
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "chart": {"R": R, "K": K},
        "absorbed_support": 1,
        "state_class": "overflow",
        "fiber_class": str(fiber["classification"]),
        "typed_fiber_digest": typed_fiber_digest,
        "raw_entry_digest": replay["raw_entry_digest"],
        "lineage_digest": replay["lineage_digest"],
        "tail_orientation": replay["lineage"]["tail_orientation"],
    }
    root["state_id"] = "state:" + digest(root)
    local_e1_e3 = {
        "E1": bool(
            replay["E1"]
            and replay["universal_source"].get("source") == replay["raw_transcript"]["source"]
            and root["source_tree_scope"] == SOURCE_SCOPE
        ),
        "E2": bool(
            prime * R + 1 == 4 * K
            and int(params["x"]) == prime - 3
            and int(params["R"]) == 4 * int(params["M"]) - 13
            and prime * 13 == 4 * int(params["M"]) * 3 + 1
        ),
        "E3": bool(
            state_id_is_valid(root)
            and root["fiber_class"] == typed_fiber["classification"]
            and root["typed_fiber_digest"] == typed_fiber_digest
            and all(item["theta"] == item["expected_theta"] for item in replay["lineage"]["tail"])
        ),
    }
    if not all(local_e1_e3.values()):
        failed = [name for name, passed in local_e1_e3.items() if not passed]
        raise AssertionError(f"source-lineage root receipt failed: {failed}")
    return {
        "adapter": RAW_ENTRY_ADAPTER,
        "parameters": params,
        "root": root,
        "typed_fiber": typed_fiber,
        "fiber_certificate": fiber,
        "source_lineage": replay,
        "local_e1_e3": local_e1_e3,
        "admission": {
            "direct_root_initialization": "analysis_evidence_only",
            "authorized_edge_target": ADAPTER,
            "terminal_first": "required_before_optional_phase_handoff",
            "charged_history": "forbidden",
            "reverse_p_parent": "insufficient_for_source_provenance",
        },
    }


def phase_relay(
    *,
    prime: int,
    root_entry: dict[str, object],
    r11_fiber_declaration: dict[str, object],
) -> dict[str, object]:
    """Bind a valid c=3 root receipt to q=1 G and the d=3 R=11 RESET."""
    endpoint = q_one.q_one_g_endpoint(prime)
    params = root_entry.get("parameters")
    root = root_entry.get("root")
    source_lineage = root_entry.get("source_lineage")
    if not isinstance(params, dict) or not isinstance(root, dict) or not isinstance(source_lineage, dict):
        raise AssertionError("phase relay requires a source-lineage root receipt")
    h, R, K = (int(params[name]) for name in ("h", "R", "K"))
    if not (
        root_entry.get("local_e1_e3") == {"E1": True, "E2": True, "E3": True}
        and root.get("equation_target") == [4, prime]
        and root.get("marked_solution_set") == "Sol(p)"
        and root.get("phase") == ROOT_PHASE
        and root.get("source_tree_scope") == SOURCE_SCOPE
        and root.get("raw_entry_digest") == source_lineage.get("raw_entry_digest")
        and root.get("lineage_digest") == source_lineage.get("lineage_digest")
        and source_lineage.get("E1") is True
        and state_id_is_valid(root)
    ):
        raise AssertionError("phase relay received an invalid or foreign c=3 root")

    R11 = 11
    K11 = 3 * (22 * h + 1)
    if not (prime * R11 + 1 == 4 * K11 and K11 == (prime * R11 + 1) // 4):
        raise AssertionError("d=3 R=11 RESET formula changed")
    r11_fiber = c3.materialize_typed_fiber(R=R11, K=K11, declaration=r11_fiber_declaration)
    r11_typed_fiber = c3.typed_fiber_payload(r11_fiber)
    r11_typed_fiber_digest = "fiber:" + digest(r11_fiber)
    r11 = {
        "adapter": ADAPTER,
        "state_origin": ADAPTER,
        "source_tree_scope": SOURCE_SCOPE,
        "normal_form": "c3_d3_r11_reset_v1",
        "phase": ROOT_PHASE,
        "phase_rank": PHASE_RANK[ROOT_PHASE],
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "chart": {"R": R11, "K": K11},
        "absorbed_support": 3,
        "state_class": "reset_target",
        "fiber_class": str(r11_fiber["classification"]),
        "typed_fiber_digest": r11_typed_fiber_digest,
        "parent_root_state_id": root["state_id"],
        "parent_raw_entry_digest": root["raw_entry_digest"],
    }
    r11["state_id"] = "state:" + digest(r11)

    phase_policy = {
        "rank_order": PHASE_RANK,
        "allowed_nonterminal_transitions": [
            [ENDPOINT_PHASE, ROOT_PHASE],
            [ROOT_PHASE, ROOT_PHASE],
            [ROOT_PHASE, SMALLER_PHASE],
        ],
        "forbidden_nonterminal_transition": [ROOT_PHASE, ENDPOINT_PHASE],
        "type_ii_after_root": "terminal_leaf_only",
    }
    B_p = (prime - 1) ** 2 // 4
    endpoint_potential = [PHASE_RANK[ENDPOINT_PHASE], 1, 0]
    root_potential = [PHASE_RANK[ROOT_PHASE], B_p, K]
    r11_potential = [PHASE_RANK[ROOT_PHASE], B_p // 3, K11 // 3]

    phase_root_e1_e5 = {
        "E1": bool(
            endpoint.get("phase") == ENDPOINT_PHASE
            and endpoint.get("endpoint", {}).get("q") == 1
            and root_entry["local_e1_e3"]["E1"]
            and root.get("raw_entry_digest") == source_lineage.get("raw_entry_digest")
            and root.get("lineage_digest") == source_lineage.get("lineage_digest")
        ),
        "E2": bool(root.get("chart") == {"R": R, "K": K} and root.get("state_origin") == RAW_ENTRY_ADAPTER),
        "E3": bool(state_id_is_valid(root) and root_entry["local_e1_e3"]["E3"]),
        "E4": bool(
            endpoint.get("equation_target") == root.get("equation_target")
            and endpoint.get("marked_solution_set") == root.get("marked_solution_set") == "Sol(p)"
        ),
        "E5": bool(
            endpoint_potential > root_potential
            and phase_policy["forbidden_nonterminal_transition"] == [ROOT_PHASE, ENDPOINT_PHASE]
        ),
    }
    reset_e1_e5 = {
        "E1": bool(root_entry["local_e1_e3"]["E1"] and root.get("absorbed_support") == 1),
        "E2": bool(R11 == 11 and K11 == 3 * (22 * h + 1) and prime * 13 == 4 * (26 * h + 1) * 3 + 1),
        "E3": bool(
            state_id_is_valid(r11)
            and r11_typed_fiber["classification"] == r11["fiber_class"]
            and r11["typed_fiber_digest"] == r11_typed_fiber_digest
            and r11.get("source_tree_scope") == SOURCE_SCOPE
        ),
        "E4": bool(
            root.get("equation_target") == r11.get("equation_target")
            and root.get("marked_solution_set") == r11.get("marked_solution_set") == "Sol(p)"
        ),
        "E5": bool(root_potential > r11_potential),
    }
    if not all(phase_root_e1_e5.values()) or not all(reset_e1_e5.values()):
        raise AssertionError("q=1 G c=3 phase relay did not close E1--E5")
    return {
        "adapter": ADAPTER,
        "endpoint": endpoint,
        "root": root,
        "r11_reset_target": r11,
        "r11_typed_fiber": r11_typed_fiber,
        "r11_fiber_certificate": r11_fiber,
        "phase_policy": phase_policy,
        "phase_root_e1_e5": phase_root_e1_e5,
        "r11_reset_e1_e5": reset_e1_e5,
        "solution_lifts": {
            "endpoint_to_root": "identity: Sol(p) -> Sol(p)",
            "root_to_r11": "identity: Sol(p) -> Sol(p)",
        },
        "potentials": {
            "endpoint": endpoint_potential,
            "root": root_potential,
            "r11_reset_target": r11_potential,
        },
        "scope": {
            "terminal_first": "required before this optional nonterminal handoff",
            "conditional_on": ["q=1 G endpoint", "valid c=3 declared-source lineage receipt"],
            "not_proved": [
                "a source-lineage raw transcript for every core prime",
                "a total selector after the R=11 RESET",
                "a global G/Type I exit",
            ],
        },
    }


def verify() -> dict[str, object]:
    """Replay three q=1 G phase controls and one source-bypass-only control."""
    declarations = [
        {"h": 3, "a": 7, "b": 2, "fiber": {"classification": "F", "witness": [-2, 1, 0, 2]}},
        {"h": 43, "a": 7, "b": 46, "fiber": {"classification": "F", "witness": [0, -1, 1, 12, 0]}},
        {"h": 138, "a": 79, "b": 202, "fiber": {"classification": "F", "witness": [0, -3, 0, -2, 0]}},
    ]
    controls: dict[int, dict[str, object]] = {}
    for declaration in declarations:
        h, a, b = (int(declaration[name]) for name in ("h", "a", "b"))
        prime = 24 * h + 1
        root = source_lineage_root_entry(
            prime=prime,
            actions=affine_prime_actions(h, a, b),
            fiber_declaration=dict(declaration["fiber"]),
        )
        relay = phase_relay(
            prime=prime,
            root_entry=root,
            r11_fiber_declaration={"classification": "G", "conductor": 11},
        )
        if not (
            root["source_lineage"]["lineage"]["tail_orientation"] == -1
            and all(relay["phase_root_e1_e5"].values())
            and all(relay["r11_reset_e1_e5"].values())
            and relay["potentials"]["endpoint"] > relay["potentials"]["root"] > relay["potentials"]["r11_reset_target"]
        ):
            raise AssertionError(f"q=1 G c=3 control changed for p={prime}")
        controls[prime] = {"root": root, "relay": relay}

    bypass = replay_source_lineage(1009, p1009_bypass_actions())
    if not (
        bypass["lineage"]["tail_orientation"] == 1
        and [item["theta"] for item in bypass["lineage"]["tail"]] == [3266, 2173, 4346]
    ):
        raise AssertionError("p=1009 source-bypass control changed")
    try:
        q_one.q_one_g_endpoint(1009)
    except AssertionError:
        bypass_q_one_status = "not_a_q1_g_endpoint"
    else:
        raise AssertionError("p=1009 unexpectedly entered the q=1 G phase relay")
    return {
        "status": "verified",
        "controls": controls,
        "source_bypass_control": {
            "prime": 1009,
            "tail_orientation": bypass["lineage"]["tail_orientation"],
            "tail_theta": [item["theta"] for item in bypass["lineage"]["tail"]],
            "q_one_status": bypass_q_one_status,
        },
        "scope": "Conditional q=1 G phase relay and d=3 RESET only; no universal raw-transcript theorem or global exit.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = verify()
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
