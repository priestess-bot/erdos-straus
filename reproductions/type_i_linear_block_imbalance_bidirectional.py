#!/usr/bin/env python3
"""Audit both orientations of the dyadic block-imbalance transfer."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from sympy import factorint, n_order


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-trichotomy-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-bidirectional-results.json"
EXPECTED_INPUT_SHA256 = "36750eec865b011089342d95b3b72ba9afa319a99e5179fedd6dd51c0e5d5ce1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def odd_blocks(U: int, V: int, lambda_two: int) -> tuple[int, int]:
    U_factors = factorint(U)
    V_factors = factorint(V)
    U_odd = U // (2 ** int(U_factors.get(2, 0)))
    V_odd = V // (2 ** int(V_factors.get(2, 0)))
    common = math.gcd(U_odd, V_odd)
    if lambda_two > 0:
        A, B = V_odd // common, U_odd // common
    else:
        A, B = U_odd // common, V_odd // common
    if A <= 0 or B <= 0 or math.gcd(A, B) != 1 or A % 2 == 0 or B % 2 == 0:
        raise AssertionError("invalid odd block normalization")
    return A, B


def oriented_terminal(
    prime: int,
    modulus: int,
    K: int,
    U: int,
    V: int,
    lambda_two: int,
    orientation: str,
) -> list[dict[str, int | str]]:
    A, B = odd_blocks(U, V, lambda_two)
    order_two = int(n_order(2, modulus))
    j0 = abs(lambda_two)
    if orientation == "reverse":
        A, B = B, A
        j0 = (-j0) % order_two
        if j0 == 0:
            j0 = order_two
    elif orientation != "forward":
        raise ValueError(f"unknown orientation: {orientation}")
    max_J = int(factorint(K).get(2, 0)) + 1
    terminals: list[dict[str, int | str]] = []
    for J in range(1, max_J + 1):
        if (J - j0) % order_two:
            continue
        if (A - (2**J) * B) % modulus:
            raise AssertionError("block ratio failed the selected dyadic congruence")
        if not A < (2**J) * B:
            continue
        E_fraction = Fraction((2 * K) * A, B * (2 ** (J - 1)))
        if E_fraction.denominator != 1:
            raise AssertionError("dyadic terminal is not integral")
        E = E_fraction.numerator
        source, remainder = divmod(4 * K - E, modulus)
        if E % 2 or (4 * K * K) % E or E % modulus != 1:
            raise AssertionError("invalid dyadic terminal divisor")
        if remainder or source <= 0 or source >= prime or source % 2:
            raise AssertionError("invalid dyadic terminal source")
        terminals.append(
            {
                "orientation": orientation,
                "A": A,
                "B": B,
                "J": J,
                "E": E,
                "source": source,
                "order_two": order_two,
            }
        )
    return terminals


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen trichotomy input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records: list[dict[str, object]] = []
    classification = Counter()
    orientation_counts = Counter()
    prime_terminal_counts: Counter[int] = Counter()
    for record in payload["records"]:
        if record["classification"] not in {"dyadic_terminal", "dyadic_unresolved"}:
            continue
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = int(record["K"])
        U = int(record["U"])
        V = int(record["V"])
        lambda_two = int(record["lambda_two"])
        candidates: list[dict[str, int | str]] = []
        for orientation in ("forward", "reverse"):
            candidates.extend(
                oriented_terminal(
                    prime, modulus, K, U, V, lambda_two, orientation
                )
            )
        candidates.sort(
            key=lambda item: (
                item["orientation"] != "forward",
                int(item["J"]),
                int(item["E"]),
            )
        )
        kind = "bidirectional_terminal" if candidates else "bidirectional_unresolved"
        classification[kind] += 1
        if record["classification"] == "dyadic_unresolved" and candidates:
            classification["rescued_from_forward"] += 1
        for candidate in candidates:
            orientation_counts[str(candidate["orientation"])] += 1
            prime_terminal_counts[prime] += 1
        records.append(
            {
                "prime": prime,
                "R": modulus,
                "K": K,
                "a": int(record["a"]),
                "s": int(record["s"]),
                "U": U,
                "V": V,
                "lambda_two": lambda_two,
                "forward_classification": record["classification"],
                "classification": kind,
                "terminal_candidates": candidates,
                "canonical_terminal": candidates[0] if candidates else None,
            }
        )
    return {
        "arithmetic": (
            "Audit both orientations of A=2^J B modulo R. The reverse orientation uses "
            "J congruent to -j0 modulo the order of 2 and the same finite dyadic budget."
        ),
        "scope_note": (
            "Finite complete-spectrum extension. It preserves the original forward orientation "
            "and adds only the mathematically equivalent reverse transfer; no global selector "
            "or arithmetic descent theorem is claimed."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "source_dyadic_state_count": len(records),
        "classification_counts": {
            key: int(value) for key, value in sorted(classification.items())
        },
        "terminal_state_count": int(classification["bidirectional_terminal"]),
        "unresolved_state_count": int(classification["bidirectional_unresolved"]),
        "terminal_candidate_count": int(sum(orientation_counts.values())),
        "orientation_candidate_counts": {
            key: int(value) for key, value in sorted(orientation_counts.items())
        },
        "terminal_prime_count": len(prime_terminal_counts),
        "prime_terminal_counts": {
            str(prime): int(count)
            for prime, count in sorted(prime_terminal_counts.items())
        },
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
                key: result[key]
                for key in (
                    "source_dyadic_state_count",
                    "classification_counts",
                    "terminal_state_count",
                    "unresolved_state_count",
                    "terminal_candidate_count",
                    "orientation_candidate_counts",
                    "terminal_prime_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
