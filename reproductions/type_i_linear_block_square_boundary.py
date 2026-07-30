#!/usr/bin/env python3
"""Audit the smaller-block square boundary on bidirectionally unresolved states."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-bidirectional-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-square-boundary-results.json"
EXPECTED_INPUT_SHA256 = "83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_record(record: dict[str, object]) -> dict[str, object]:
    prime = int(record["prime"])
    modulus = int(record["R"])
    K = int(record["K"])
    U = int(record["U"])
    V = int(record["V"])
    if record["classification"] != "bidirectional_unresolved":
        raise AssertionError("square-boundary audit received a resolved state")
    if U == V or U % 2:
        raise AssertionError("unexpected symmetric or odd U state")
    X, Y = sorted((U, V))
    E = X * X
    square_divisor = (4 * K * K) % E == 0
    if square_divisor:
        numerator = U * V - E
        source, remainder = divmod(numerator, modulus)
        if remainder or not (0 < source < prime):
            raise AssertionError("invalid smaller-block square source")
        if E % modulus != 1 or E <= 1 or E >= 4 * K:
            raise AssertionError("invalid smaller-block square terminal")
        if (n := source) * K % E:
            raise AssertionError("terminal divisor does not divide source product")
        kind = "even_terminal" if E % 2 == 0 else "odd_marked_descent"
        return {
            **record,
            "square_classification": kind,
            "X": X,
            "Y": Y,
            "E": E,
            "source": source,
            "square_divisor": True,
        }
    if not (U < V and V % 2 == 1):
        raise AssertionError("square-divisor obstruction was not the exact mixed-parity case")
    return {
        **record,
        "square_classification": "mixed_parity_square_obstruction",
        "X": X,
        "Y": Y,
        "E": E,
        "square_divisor": False,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the bidirectional input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = [
        audit_record(record)
        for record in payload["records"]
        if record["classification"] == "bidirectional_unresolved"
    ]
    counts = Counter(str(record["square_classification"]) for record in records)
    prime_counts = {
        kind: len(
            {
                int(record["prime"])
                for record in records
                if record["square_classification"] == kind
            }
        )
        for kind in sorted(counts)
    }
    return {
        "arithmetic": (
            "For U=sR+1 even and V=aR+1 with UV=4K, the smaller block square "
            "X^2 is a divisor of 4K^2 unless U<V and V is odd. When valid, it "
            "gives E=X^2, a smaller source, and parity-matched even terminal or "
            "odd marked descent."
        ),
        "scope_note": (
            "Finite audit of the bidirectionally unresolved dyadic states. The "
            "square obstruction is exact for this smaller-block-square mechanism; "
            "it does not rule out another terminal or Type I/II certificate."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "record_count": len(records),
        "classification_counts": {
            key: int(value) for key, value in sorted(counts.items())
        },
        "classification_prime_counts": prime_counts,
        "records": records,
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
                "classification_counts": result["classification_counts"],
                "classification_prime_counts": result["classification_prime_counts"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
