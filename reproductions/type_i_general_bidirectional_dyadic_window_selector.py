#!/usr/bin/env python3
"""Verify the maximal-window bidirectional dyadic selector."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import cache
import hashlib
import json
import math
from pathlib import Path

from sympy import n_order


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-block-imbalance-bidirectional-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-general-bidirectional-dyadic-window-selector-results.json"
)
EXPECTED_INPUT_SHA256 = (
    "83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f"
)
EXPECTED_STATE_COUNT = 15_356
EXPECTED_WINDOW_COUNTS = {
    "none": 7_433,
    "forward_only": 6_460,
    "both": 1_231,
    "reverse_only": 232,
}
EXPECTED_CANONICAL_ORIENTATIONS = {"forward": 2_776, "reverse": 907}
EXPECTED_BOTH_HEIGHT_COUNT = 133
EXPECTED_ORDER_BUDGET_MATRIX = {
    "order_lt_budget": {
        "bidirectional_terminal": 616,
        "bidirectional_unresolved": 0,
    },
    "order_eq_budget": {
        "bidirectional_terminal": 469,
        "bidirectional_unresolved": 0,
    },
    "order_gt_budget": {
        "bidirectional_terminal": 2_598,
        "bidirectional_unresolved": 11_673,
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation_two(value: int) -> int:
    if value <= 0:
        raise ValueError("2-adic valuation requires a positive integer")
    return (value & -value).bit_length() - 1


@cache
def order_two(modulus: int) -> int:
    return int(n_order(2, modulus))


def odd_blocks(U: int, V: int, lambda_two: int) -> tuple[int, int]:
    U_odd = U >> valuation_two(U)
    V_odd = V >> valuation_two(V)
    common = math.gcd(U_odd, V_odd)
    if lambda_two > 0:
        A, B = V_odd // common, U_odd // common
    elif lambda_two < 0:
        A, B = U_odd // common, V_odd // common
    else:
        raise AssertionError("the dyadic selector received a zero block imbalance")
    if A <= 0 or B <= 0 or A % 2 == 0 or B % 2 == 0 or math.gcd(A, B) != 1:
        raise AssertionError("invalid odd block normalization")
    return A, B


def positive_representative(exponent: int, order: int) -> int:
    return exponent % order or order


def maximal_window_exponent(
    representative: int, order: int, budget: int
) -> int | None:
    if representative > budget:
        return None
    return representative + ((budget - representative) // order) * order


def selected_terminal(
    record: dict[str, object],
    orientation: str,
    A: int,
    B: int,
    exponent: int,
    order: int,
) -> dict[str, int | str]:
    prime = int(record["prime"])
    modulus = int(record["R"])
    K = int(record["K"])
    E_fraction = Fraction(2 * K * A, B * (2 ** (exponent - 1)))
    if E_fraction.denominator != 1:
        raise AssertionError("maximal-window terminal is not integral")
    E = E_fraction.numerator
    source, remainder = divmod(4 * K - E, modulus)
    if (
        remainder
        or E % 2
        or (4 * K * K) % E
        or E % modulus != 1
        or source <= 0
        or source >= prime
        or source % 2
    ):
        raise AssertionError("maximal-window terminal arithmetic failed")
    return {
        "orientation": orientation,
        "A": A,
        "B": B,
        "J": exponent,
        "E": E,
        "source": source,
        "order_two": order,
    }


def run() -> dict[str, object]:
    input_hash = sha256(INPUT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen bidirectional input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = payload["records"]
    if not isinstance(records, list) or len(records) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen dyadic state count changed")

    directed_keys: set[tuple[int, ...]] = set()
    primes: set[int] = set()
    moduli: set[int] = set()
    window_counts: Counter[str] = Counter()
    cross_table: Counter[tuple[str, str]] = Counter()
    height_pattern_counts: Counter[str] = Counter()
    selector_classification_counts: Counter[str] = Counter()
    canonical_orientation_counts: Counter[str] = Counter()
    order_budget_counts: Counter[tuple[str, str]] = Counter()
    both_window_violation_count = 0
    classification_mismatch_count = 0
    frozen_candidate_mismatch_count = 0
    frozen_orientation_mismatch_count = 0

    for raw_record in records:
        if not isinstance(raw_record, dict):
            raise AssertionError("a frozen dyadic record is not an object")
        record = raw_record
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = int(record["K"])
        a = int(record["a"])
        s = int(record["s"])
        U = int(record["U"])
        V = int(record["V"])
        lambda_two = int(record["lambda_two"])
        stored_classification = str(record["classification"])
        state_key = (prime, modulus, a, s, U, V)
        if state_key in directed_keys:
            raise AssertionError("duplicate directed dyadic state")
        directed_keys.add(state_key)
        primes.add(prime)
        moduli.add(modulus)

        if (
            modulus % 2 == 0
            or 4 * K != prime * modulus + 1
            or U != s * modulus + 1
            or V != a * modulus + 1
            or U * V != 4 * K
            or lambda_two != valuation_two(U) - valuation_two(V)
            or lambda_two == 0
        ):
            raise AssertionError("directed dyadic state arithmetic changed")

        A, B = odd_blocks(U, V, lambda_two)
        order = order_two(modulus)
        budget = valuation_two(K) + 1
        forward_representative = positive_representative(abs(lambda_two), order)
        reverse_representative = positive_representative(-abs(lambda_two), order)
        forward_J = maximal_window_exponent(
            forward_representative, order, budget
        )
        reverse_J = maximal_window_exponent(reverse_representative, order, budget)

        if forward_J is not None and (A - (2**forward_J) * B) % modulus:
            raise AssertionError("forward maximal window lost its congruence")
        if reverse_J is not None and (B - (2**reverse_J) * A) % modulus:
            raise AssertionError("reverse maximal window lost its congruence")

        if forward_J is not None and reverse_J is not None:
            window = "both"
        elif forward_J is not None:
            window = "forward_only"
        elif reverse_J is not None:
            window = "reverse_only"
        else:
            window = "none"

        forward_height = (
            forward_J is not None and A < (2**forward_J) * B
        )
        reverse_height = reverse_J is not None and B < (2**reverse_J) * A
        if forward_height and reverse_height:
            height_pattern = "both"
        elif forward_height:
            height_pattern = "forward_only"
        elif reverse_height:
            height_pattern = "reverse_only"
        else:
            height_pattern = "neither"

        selector_orientation: str | None
        selector_terminal: dict[str, int | str] | None
        if forward_height:
            selector_orientation = "forward"
            selector_terminal = selected_terminal(
                record, "forward", A, B, int(forward_J), order
            )
        elif reverse_height:
            selector_orientation = "reverse"
            selector_terminal = selected_terminal(
                record, "reverse", B, A, int(reverse_J), order
            )
        else:
            selector_orientation = None
            selector_terminal = None

        selector_classification = (
            "bidirectional_terminal"
            if selector_terminal is not None
            else "bidirectional_unresolved"
        )
        frozen_candidates = record["terminal_candidates"]
        frozen_canonical = record["canonical_terminal"]
        if not isinstance(frozen_candidates, list):
            raise AssertionError("frozen terminal candidates are not a list")
        if selector_terminal is not None and selector_terminal not in frozen_candidates:
            frozen_candidate_mismatch_count += 1
        if frozen_canonical is not None and not isinstance(frozen_canonical, dict):
            raise AssertionError("the frozen canonical terminal is not an object")
        frozen_orientation = (
            None
            if frozen_canonical is None
            else str(frozen_canonical["orientation"])
        )
        if selector_orientation != frozen_orientation:
            frozen_orientation_mismatch_count += 1
        if selector_classification != stored_classification:
            classification_mismatch_count += 1
        if window == "both" and selector_terminal is None:
            both_window_violation_count += 1

        window_counts[window] += 1
        cross_table[(window, stored_classification)] += 1
        height_pattern_counts[height_pattern] += 1
        selector_classification_counts[selector_classification] += 1
        if selector_orientation is not None:
            canonical_orientation_counts[selector_orientation] += 1
        order_band = (
            "order_lt_budget"
            if order < budget
            else "order_eq_budget"
            if order == budget
            else "order_gt_budget"
        )
        order_budget_counts[(order_band, stored_classification)] += 1

    normalized_window_counts = {
        key: int(window_counts[key]) for key in EXPECTED_WINDOW_COUNTS
    }
    normalized_cross_table = {
        window: {
            classification: int(cross_table[(window, classification)])
            for classification in (
                "bidirectional_terminal",
                "bidirectional_unresolved",
            )
        }
        for window in EXPECTED_WINDOW_COUNTS
    }
    normalized_order_matrix = {
        band: {
            classification: int(order_budget_counts[(band, classification)])
            for classification in (
                "bidirectional_terminal",
                "bidirectional_unresolved",
            )
        }
        for band in EXPECTED_ORDER_BUDGET_MATRIX
    }
    normalized_orientations = {
        key: int(canonical_orientation_counts[key])
        for key in EXPECTED_CANONICAL_ORIENTATIONS
    }
    if normalized_window_counts != EXPECTED_WINDOW_COUNTS:
        raise AssertionError("the maximal-window classification changed")
    if normalized_orientations != EXPECTED_CANONICAL_ORIENTATIONS:
        raise AssertionError("the canonical orientation counts changed")
    if height_pattern_counts["both"] != EXPECTED_BOTH_HEIGHT_COUNT:
        raise AssertionError("the two-height overlap count changed")
    if normalized_order_matrix != EXPECTED_ORDER_BUDGET_MATRIX:
        raise AssertionError("the order-budget matrix changed")
    if (
        both_window_violation_count
        or classification_mismatch_count
        or frozen_candidate_mismatch_count
        or frozen_orientation_mismatch_count
    ):
        raise AssertionError("the maximal-window selector failed a frozen invariant")

    return {
        "schema_version": "type-i-general-bidirectional-dyadic-window-selector/v1",
        "arithmetic": (
            "For each nonzero dyadic block imbalance, select the largest forward "
            "and reverse exponents in 1<=J<=v_2(2K), then prefer a valid forward "
            "height and otherwise use a valid reverse height."
        ),
        "scope_note": (
            "This is a hash-frozen audit of 15,356 directed dyadic states from 200 "
            "selected pressure primes. It verifies a local maximal-window selector, "
            "not a global Type I/II selector or lifting theorem."
        ),
        "input": INPUT.name,
        "input_sha256": input_hash,
        "state_count": len(records),
        "unique_directed_state_count": len(directed_keys),
        "prime_count": len(primes),
        "unique_modulus_count": len(moduli),
        "window_counts": normalized_window_counts,
        "window_classification_cross_table": normalized_cross_table,
        "height_pattern_counts": {
            key: int(height_pattern_counts[key])
            for key in ("neither", "forward_only", "both", "reverse_only")
        },
        "both_window_implication": {
            "checked": int(window_counts["both"]),
            "terminal": int(
                cross_table[("both", "bidirectional_terminal")]
            ),
            "violations": both_window_violation_count,
        },
        "selector_classification_counts": {
            key: int(selector_classification_counts[key])
            for key in (
                "bidirectional_terminal",
                "bidirectional_unresolved",
            )
        },
        "selector_classification_mismatch_count": classification_mismatch_count,
        "selected_terminal_arithmetic_check": {
            "checked": sum(canonical_orientation_counts.values()),
            "failures": 0,
        },
        "selected_terminal_frozen_candidate_mismatch_count": (
            frozen_candidate_mismatch_count
        ),
        "canonical_orientation_counts": normalized_orientations,
        "canonical_orientation_mismatch_count": frozen_orientation_mismatch_count,
        "both_height_count": int(height_pattern_counts["both"]),
        "order_budget_matrix": normalized_order_matrix,
    }


def summary(payload: dict[str, object]) -> dict[str, object]:
    return {
        key: payload[key]
        for key in (
            "state_count",
            "unique_directed_state_count",
            "window_counts",
            "window_classification_cross_table",
            "both_window_implication",
            "selector_classification_counts",
            "selected_terminal_arithmetic_check",
            "canonical_orientation_counts",
            "both_height_count",
            "order_budget_matrix",
        )
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
        print(json.dumps(summary(payload), ensure_ascii=False, indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary(payload), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
