#!/usr/bin/env python3
"""Replay the source-bound F3 m=3,q=5 macro interface.

The universal theorems are in the accompanying claim.  Fixed charts below
exercise raw-path and target/rank identities only; no fixture is claimed to be
an actual persistent m=3,5|D_star state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "data" / "t6-wave1" / "f3-m3-q5-p2-proof-receipt-v1.json"


def digest(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def factor(value: int) -> dict[int, int]:
    result: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def prime_word(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for prime, exponent in sorted(factor(value).items()):
        result.extend([prime] * exponent)
    return tuple(result)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def chart(prime: int, parameter: int) -> dict[str, int]:
    g = (prime + 1) // 2
    root_modulus = (prime * prime + prime + 1) // 3
    root_u = gcd(2 * parameter + 1, root_modulus)
    root_height = 3 * root_u
    t_value = prime * prime * parameter - g
    support = g * t_value
    capacity = support * (prime - 1)
    residual = 2 * prime**3 * parameter - prime * prime - 2 * prime * parameter - prime + 1
    if not (4 * capacity == prime * residual + 1 and support > 0):
        raise AssertionError("root chart changed")
    return {
        "p": prime,
        "r": parameter,
        "A": support,
        "K": capacity,
        "R": residual,
        "h": root_height,
    }


def peel_word(
    *, residual: int, capacity: int, selected: int, labels: tuple[int, ...]
) -> tuple[int, list[dict[str, int]]]:
    steps: list[dict[str, int]] = []
    current = selected
    for label in labels:
        other = residual - current
        if not (
            current % label == 0
            and valuation(current, label) > valuation(capacity, label)
            and gcd(label, residual * other) == 1
        ):
            raise AssertionError("raw capacity word changed")
        target = current // label
        if gcd(target, residual - target) != 1:
            raise AssertionError("raw word lost primitive node")
        steps.append(
            {
                "label": label,
                "selected_before": current,
                "selected_after": target,
                "other_after": residual - target,
                "shift": label - 1,
            }
        )
        current = target
    return current, steps


def source_path_receipt(
    prime: int,
    parameter: int,
    *,
    state_id: str,
    scope: str,
) -> dict[str, object]:
    data = chart(prime, parameter)
    residual, capacity, height = data["R"], data["K"], data["h"]
    source = (prime, residual * (prime - 1) - prime, prime - 1)
    if not (
        min(source) > 0
        and source[0] + source[1] == residual * source[2]
        and gcd(source[0], source[1]) == 1
        and capacity % prime
    ):
        raise AssertionError("universal p source changed")
    anchor = (1, residual - 1)
    if not (
        gcd(residual - 1, capacity) == prime + 1
        and gcd(residual - prime - 1, capacity) == height
    ):
        raise AssertionError("root capacity gcd identities changed")
    first_labels = prime_word((residual - 1) // (prime + 1))
    first_end, first_steps = peel_word(
        residual=residual,
        capacity=capacity,
        selected=residual - 1,
        labels=first_labels,
    )
    if first_end != prime + 1:
        raise AssertionError("first capacity word missed p+1")
    second_labels = prime_word((residual - prime - 1) // height)
    second_end, second_steps = peel_word(
        residual=residual,
        capacity=capacity,
        selected=residual - prime - 1,
        labels=second_labels,
    )
    if second_end != height:
        raise AssertionError("second capacity word missed root height")
    payload: dict[str, object] = {
        "schema_id": "f3_m3_q5_path_bound_source_receipt_v1",
        "state_id": state_id,
        "scope": scope,
        "charged_support": data["A"],
        "universal_source": source,
        "anchor": anchor,
        "first_word": first_steps,
        "second_word": second_steps,
        "root_endpoint": (height, residual - height),
        "priority_boundary": "prefix_receipts_required_from_common_terminal_scheduler",
        "fixtures_are_actual_track_evidence": False,
    }
    payload["digest"] = digest(payload)
    return payload


def serialize_endpoint(
    *, prime: int, support: int, capacity: int, residual: int, left: int, right: int
) -> dict[str, object]:
    if not (
        support > (prime - 1) ** 2 // 4
        and capacity == support * (prime - 1)
        and prime * residual + 1 == 4 * capacity
        and left + right == residual
        and gcd(left, right) == 1
        and left % prime
        and right % prime
    ):
        raise AssertionError("endpoint source contract failed")
    q_left, beta_left = complete_excess(left, capacity)
    q_right, beta_right = complete_excess(right, capacity)
    if q_left == q_right == 1:
        return {"outcome": "TERMINAL", "kind": "BOTTOM_TYPE_I"}
    target_support = lcm(support, q_left, q_right)
    if target_support <= support:
        raise AssertionError("nonterminal complete-excess target must increase support")
    multiplier = target_support // support
    cofactor = pow(4 * target_support, -1, prime)
    target_capacity = target_support * cofactor
    target_residual = (4 * target_capacity - 1) // prime
    strict = multiplier % prime != 1
    if strict != (cofactor < prime - 1):
        raise AssertionError("strict multiplier/cofactor equivalence changed")
    boundary = (prime - 1) ** 2 // 4
    if not (target_support > support > boundary):
        raise AssertionError("track target lost its high-support invariant")
    if not strict:
        shape = "P2_OR_OTHER_P_STUTTER_CHECKPOINT"
        ticket = None
    else:
        if target_residual <= prime:
            raise AssertionError("high-support target cannot lie below p")
        shape = "TYPEI_CHARGED_OVERFLOW"
        ticket = "LOCAL_DROP"
    return {
        "outcome": "CANDIDATE",
        "q_left": q_left,
        "beta_left": beta_left,
        "q_right": q_right,
        "beta_right": beta_right,
        "target_support": target_support,
        "L_omega": multiplier,
        "target_cofactor": cofactor,
        "target_capacity": target_capacity,
        "target_residual": target_residual,
        "target_shape": shape,
        "T5_ticket": ticket,
        "E4": "IDENTITY_ON_SOL_P_AFTER_TARGET_VALIDATION",
        "persistent_admission": "COORDINATOR_INTERFACE_REQUIRED",
    }


def verify_controls() -> dict[str, object]:
    # These verify formulas only.  Neither is an actual m=3,5|D_star witness.
    first = source_path_receipt(
        73, 3, state_id="control:p73:r3", scope="charged_history_only"
    )
    if first["root_endpoint"] != (3, 2_328_260):
        raise AssertionError("source-path control changed")

    source = chart(73, 1)
    strict_high = serialize_endpoint(
        prime=73,
        support=source["A"],
        capacity=source["K"],
        residual=source["R"],
        left=761_905,
        right=10_582,
    )
    if not (
        strict_high["target_shape"] == "TYPEI_CHARGED_OVERFLOW"
        and strict_high["T5_ticket"] == "LOCAL_DROP"
        and strict_high["target_cofactor"] == 67
    ):
        raise AssertionError("strict high-support control changed")

    return {
        "source_path": first,
        "strict_high": strict_high,
        "fixtures_are_actual_track_evidence": False,
    }


def verify_manifest() -> dict[str, object]:
    payload = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if not (
        payload["status"] == "PARTIAL_MATHEMATICAL_CLOSURE_INTEGRATION_AND_P2_OPEN"
        and len(payload["open_mathematical_leaves"]) == 4
        and "R2=CLOSED" in payload["forbidden_conclusions"]
        and "L1=L_omega" in payload["forbidden_conclusions"]
    ):
        raise AssertionError("proof receipt boundary changed")
    return payload


def run() -> dict[str, object]:
    manifest = verify_manifest()
    controls = verify_controls()
    return {
        "schema_id": manifest["schema_id"],
        "status": manifest["status"],
        "established_ids": [row["id"] for row in manifest["established"]],
        "open_leaf_ids": [row["id"] for row in manifest["open_mathematical_leaves"]],
        "control_summary": {
            "path_digest": controls["source_path"]["digest"],
            "strict_target_shape": controls["strict_high"]["target_shape"],
            "strict_ticket": controls["strict_high"]["T5_ticket"],
            "target_support_exceeds_parent": (
                controls["strict_high"]["target_support"]
                > chart(73, 1)["A"]
                > (73 - 1) ** 2 // 4
            ),
            "fixtures_are_actual_track_evidence": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(run(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
