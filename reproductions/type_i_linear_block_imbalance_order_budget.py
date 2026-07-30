#!/usr/bin/env python3
"""Audit the multiplicative-order versus dyadic-budget gap."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

from sympy import factorint, n_order


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-bidirectional-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-order-budget-results.json"
EXPECTED_INPUT_SHA256 = "83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the bidirectional input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = [
        record
        for record in payload["records"]
        if record["classification"] == "bidirectional_unresolved"
    ]
    order_counts: Counter[int] = Counter()
    budget_counts: Counter[int] = Counter()
    gap_counts: Counter[int] = Counter()
    square_class_counts: Counter[str] = Counter()
    enriched: list[dict[str, object]] = []
    for record in records:
        modulus = int(record["R"])
        K = int(record["K"])
        lambda_two = abs(int(record["lambda_two"]))
        order_two = int(n_order(2, modulus))
        max_J = int(factorint(K).get(2, 0)) + 1
        forward_residues = [
            J for J in range(1, max_J + 1) if (J - lambda_two) % order_two == 0
        ]
        reverse_residue = (-lambda_two) % order_two or order_two
        reverse_residues = [
            J for J in range(1, max_J + 1) if (J - reverse_residue) % order_two == 0
        ]
        if not order_two > max_J:
            raise AssertionError("unresolved state lacks an order-budget gap")
        if forward_residues and reverse_residues:
            residue_window = "both"
        elif forward_residues:
            residue_window = "forward_only"
        elif reverse_residues:
            residue_window = "reverse_only"
        else:
            residue_window = "none"
        U, V = int(record["U"]), int(record["V"])
        if U < V and V % 2 == 1:
            square_class = "mixed_parity_square_obstruction"
        else:
            X = min(U, V)
            E = X * X
            source = (U * V - E) // modulus
            square_class = "even_terminal" if source % 2 == 0 else "odd_marked_descent"
        order_counts[order_two] += 1
        budget_counts[max_J] += 1
        gap_counts[order_two - max_J] += 1
        square_class_counts[square_class] += 1
        enriched.append(
            {
                "prime": int(record["prime"]),
                "R": modulus,
                "K": K,
                "lambda_two_abs": lambda_two,
                "order_two": order_two,
                "max_J": max_J,
                "order_budget_gap": order_two - max_J,
                "residue_window": residue_window,
                "square_classification": square_class,
            }
        )
    return {
        "arithmetic": (
            "For every bidirectionally unresolved dyadic state, verify the common "
            "order-budget gap ord_R(2)>v_2(2K), then classify whether the forward "
            "or reverse congruence class still enters the finite budget interval."
        ),
        "scope_note": (
            "Finite diagnostic boundary. The order-budget gap is a certificate for "
            "failure of this dyadic family only; it is not a target nonexistence proof."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "record_count": len(records),
        "order_budget_gap_count": len(records),
        "minimum_order": min(order_counts),
        "maximum_order": max(order_counts),
        "minimum_budget": min(budget_counts),
        "maximum_budget": max(budget_counts),
        "order_counts": {
            str(key): int(value) for key, value in sorted(order_counts.items())
        },
        "budget_counts": {
            str(key): int(value) for key, value in sorted(budget_counts.items())
        },
        "square_classification_counts": {
            key: int(value) for key, value in sorted(square_class_counts.items())
        },
        "residue_window_counts": {
            key: int(value)
            for key, value in sorted(
                Counter(record["residue_window"] for record in enriched).items()
            )
        },
        "gap_counts": {
            str(key): int(value) for key, value in sorted(gap_counts.items())
        },
        "records": enriched,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "record_count": result["record_count"],
                "order_budget_gap_count": result["order_budget_gap_count"],
                "minimum_order": result["minimum_order"],
                "maximum_order": result["maximum_order"],
                "minimum_budget": result["minimum_budget"],
                "maximum_budget": result["maximum_budget"],
                "square_classification_counts": result[
                    "square_classification_counts"
                ],
                "residue_window_counts": result["residue_window_counts"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
