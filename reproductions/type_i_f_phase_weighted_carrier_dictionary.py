#!/usr/bin/env python3
"""Build a phase-order versus q-adic-carrier dictionary for frozen F states.

This is deliberately a diagnostic bridge.  A character denominator is recorded
next to, but never identified with, the valuation of an actual source block.
The latter is checked against the exact same-label modulus-difference capacity
available in the frozen records.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-two-direction-phase-demand-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-f-phase-weighted-carrier-dictionary-results.json"
)
EXPECTED_INPUT_SHA256 = "27e15c714b238cc580b313b70c691c96b1759ab6b022bd12808429ec082265ea"
EXPECTED_STATE_COUNT = 45


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_from_pair(pair: list[int] | tuple[int, int]) -> Fraction:
    value = Fraction(int(pair[0]), int(pair[1]))
    return value


def pair_from_fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def role_order(phase: Fraction) -> int:
    """Return the order of exp(2*pi*i*phase) for a reduced phase."""
    if phase == 0:
        return 1
    return phase.denominator


def order_debt(exponent: int, order: int) -> Fraction:
    """The bounded diagnostic debt used by the existing Fourier receipts."""
    return min(Fraction(1), Fraction(exponent * exponent, order * order))


def load_records(path: Path) -> list[dict[str, Any]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen phase-demand input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen phase-demand profile is incomplete")
    return [dict(record) for record in records]


def direction_payload(
    record: dict[str, Any], carrier: dict[str, Any]
) -> dict[str, Any]:
    factors = {int(q): int(exponent) for q, exponent in record["factorization"]}
    q = int(carrier["prime"])
    if q not in factors:
        raise AssertionError(f"carrier prime {q} is absent from K")
    phase = fraction_from_pair(carrier["phase"])
    if phase == 0:
        raise AssertionError("selected carrier has a trivial phase")
    exponent = factors[q]
    order = role_order(phase)
    height = int(carrier["height"])
    if height <= 0:
        raise AssertionError("selected carrier has no positive q-adic height")
    margin = order - 2 * exponent
    return {
        "prime": int(record["prime"]),
        "R": int(record["R"]),
        "q": q,
        "label": str(carrier["label"]),
        "phase": pair_from_fraction(phase),
        "phase_order": order,
        "K_exponent": exponent,
        "carrier_height": height,
        "order_debt_fraction": pair_from_fraction(order_debt(exponent, order)),
        # This margin is an exact single-active diagnostic only.  It is not a
        # theorem for multi-active characters because other coordinates may
        # cancel the target phase.
        "single_active_margin": margin,
        "phase_order_exceeds_twice_height": order > 2 * height,
        "phase_projection_empty": int(record["phase_projection_pair_count"]) == 0,
    }


def capacity_groups(directions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    for direction in directions:
        grouped[(direction["prime"], direction["q"], direction["label"])].append(
            direction
        )

    output: list[dict[str, Any]] = []
    for (prime, q, label), group in sorted(grouped.items()):
        pair_checks = []
        for left, right in combinations(group, 2):
            if left["R"] == right["R"]:
                # The frozen profile has at most one selected direction per
                # (p,R,q,label); duplicate rows would need a separate fiber
                # multiplicity contract rather than a modulus-difference test.
                continue
            delta = abs(left["R"] - right["R"])
            required_power = q ** min(
                left["carrier_height"], right["carrier_height"]
            )
            pair_checks.append(
                {
                    "R_left": left["R"],
                    "R_right": right["R"],
                    "required_power": required_power,
                    "modulus_difference": delta,
                    "divides": delta % required_power == 0,
                }
            )
        if not all(check["divides"] for check in pair_checks):
            raise AssertionError("same-label carrier failed modulus-difference divisibility")

        R_values = [entry["R"] for entry in group]
        R_min, R_max = min(R_values), max(R_values)
        # For odd q, every R is 3 mod 4 and q-power divisibility also holds
        # after dividing the difference by 4.  The q=2 path uses R directly.
        scale = 4 if q % 2 and all(value % 4 == 3 for value in R_values) else 1
        width = Fraction(R_max - R_min, scale)
        max_height = max(entry["carrier_height"] for entry in group)
        bound = width / (q - 1) + max_height
        height_sum = sum(entry["carrier_height"] for entry in group)
        output.append(
            {
                "prime": prime,
                "q": q,
                "label": label,
                "state_count": len(group),
                "R_min": R_min,
                "R_max": R_max,
                "coordinate_scale": scale,
                "height_sum": height_sum,
                "capacity_bound": pair_from_fraction(bound),
                "capacity_bound_decimal": float(bound),
                "capacity_satisfied": Fraction(height_sum) <= bound,
                "pair_checks": pair_checks,
            }
        )
    return output


def build_payload(path: Path) -> dict[str, Any]:
    records = load_records(path)
    directions: list[dict[str, Any]] = []
    state_rows = []
    for record in records:
        row_directions = [
            direction_payload(record, carrier)
            for carrier in record["selected_carriers"]
        ]
        directions.extend(row_directions)
        state_rows.append(
            {
                "prime": int(record["prime"]),
                "R": int(record["R"]),
                "phase_projection_empty": int(record["phase_projection_pair_count"])
                == 0,
                "directions": row_directions,
                "joint_order_debt_fraction": pair_from_fraction(
                    sum(
                        (
                            fraction_from_pair(direction["order_debt_fraction"])
                            for direction in row_directions
                        ),
                        Fraction(0),
                    )
                ),
            }
        )

    groups = capacity_groups(directions)
    phase_orders = Counter(direction["phase_order"] for direction in directions)
    nonempty = [row for row in state_rows if not row["phase_projection_empty"]]
    nonempty_orders = Counter(
        direction["phase_order"]
        for row in nonempty
        for direction in row["directions"]
    )
    margins = Counter(
        "positive" if direction["single_active_margin"] > 0 else
        "zero" if direction["single_active_margin"] == 0 else "negative"
        for direction in directions
    )
    debt_total = sum(
        (fraction_from_pair(direction["order_debt_fraction"]) for direction in directions),
        Fraction(0),
    )
    mismatch_count = sum(
        direction["phase_order_exceeds_twice_height"] for direction in directions
    )
    return {
        "arithmetic": (
            "For frozen two-direction F receipts, record the exact character order and K-exponent "
            "beside the selected source-block q-adic height, then verify same-label modulus-difference "
            "capacity. Character order is not treated as a q-adic height."
        ),
        "scope_note": (
            "Diagnostic bridge only. The single-active margin is not a multi-active theorem; "
            "phase order alone does not produce an external carrier, a common congruence chain, "
            "or a recursive edge. The capacity check applies only to the selected same-label "
            "linear blocks in this frozen profile."
        ),
        "input": path.name,
        "input_sha256": sha256(path),
        "state_count": len(records),
        "direction_count": len(directions),
        "phase_projection_empty_count": sum(
            row["phase_projection_empty"] for row in state_rows
        ),
        "phase_order_counts": {str(key): int(value) for key, value in sorted(phase_orders.items())},
        "nonempty_projection_phase_order_counts": {
            str(key): int(value) for key, value in sorted(nonempty_orders.items())
        },
        "single_active_margin_sign_counts": dict(sorted(margins.items())),
        "phase_order_exceeds_twice_height_count": mismatch_count,
        "order_debt_total": pair_from_fraction(debt_total),
        "order_debt_total_decimal": float(debt_total),
        "capacity_group_count": len(groups),
        "capacity_violation_count": sum(not group["capacity_satisfied"] for group in groups),
        "capacity_groups": groups,
        "records": state_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    payload = build_payload(args.input)
    if args.verify:
        if payload["capacity_violation_count"] != 0:
            raise AssertionError("capacity violation in frozen same-label records")
        if payload["phase_projection_empty_count"] == 0:
            raise AssertionError("expected a state-internal empty phase projection")
        if payload["phase_order_exceeds_twice_height_count"] == 0:
            raise AssertionError("expected explicit phase-order/carrier-height separation")
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "state_count",
                    "direction_count",
                    "phase_projection_empty_count",
                    "phase_order_counts",
                    "nonempty_projection_phase_order_counts",
                    "single_active_margin_sign_counts",
                    "phase_order_exceeds_twice_height_count",
                    "order_debt_total",
                    "capacity_group_count",
                    "capacity_violation_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
