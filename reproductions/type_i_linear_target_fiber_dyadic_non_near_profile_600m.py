#!/usr/bin/env python3
"""Search dyadic divisor-ratio terminals on non-near target fibers."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-target-fiber-neighbor-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-target-fiber-dyadic-non-near-profile-600m-results.json"
EXPECTED_INPUT_SHA256 = "9de9af84928e2837a717f1d6174a6a178997f30553edf770bebbbd976d3e6d31"
EXPECTED_NON_NEAR_COUNT = 226
EXPECTED_MIN_J_COUNTS = {1: 226}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coprime_divisor_pairs(L: int) -> list[tuple[int, int, int, int]]:
    factors = sorted((int(q), int(e)) for q, e in sympy.factorint(L).items())
    choices = []
    for q, exponent in factors:
        choices.append(
            [(0, 0)]
            + [(power, 0) for power in range(1, exponent + 1)]
            + [(0, power) for power in range(1, exponent + 1)]
        )
    pairs = []
    for selected in itertools.product(*choices):
        a = math.prod(q**left for (q, _), (left, _) in zip(factors, selected))
        b = math.prod(q**right for (q, _), (_, right) in zip(factors, selected))
        alpha = 0
        beta = 0
        for (q, _), (left, right) in zip(factors, selected):
            if q == 2:
                alpha, beta = left, right
        pairs.append((a, b, alpha, beta))
    return pairs


def legal_terminals(R: int, K: int) -> list[dict[str, int]]:
    L = 2 * K
    lambda_2 = int(sympy.factorint(L).get(2, 0))
    p = (4 * K - 1) // R
    candidates = []
    for a, b, alpha, beta in coprime_divisor_pairs(L):
        max_j = lambda_2 + alpha - beta
        for j in range(1, max_j + 1):
            if (a - pow(2, j, R) * b) % R:
                continue
            if not a < (1 << j) * b:
                continue
            numerator = L * a
            denominator = (1 << (j - 1)) * b
            if numerator % denominator:
                raise AssertionError("dyadic candidate is not integral")
            E = numerator // denominator
            if (
                math.gcd(a, b) != 1
                or E % 2
                or (L * L) % E
                or E % R != 1 % R
                or E >= 2 * L
            ):
                raise AssertionError("dyadic candidate failed terminal divisibility")
            difference = 2 * L - E
            if difference <= 0 or difference % R:
                raise AssertionError("dyadic candidate failed terminal congruence")
            n = difference // R
            if not (0 < n < p and n % 2 == 0):
                raise AssertionError("dyadic candidate failed terminal range")
            candidates.append({"j": j, "a": a, "b": b, "E": E, "n": n})
    return sorted(candidates, key=lambda item: (item["j"], item["n"], item["a"], item["b"]))


def load_non_near_states(path: Path = INPUT) -> list[dict[str, object]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen target-fiber profile changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = [dict(record) for record in payload["records"] if not record["near_pair"]]
    if len(records) != EXPECTED_NON_NEAR_COUNT:
        raise AssertionError("the frozen non-near state count changed")
    return records


def run_audit(path: Path = INPUT) -> dict[str, object]:
    source_records = load_non_near_states(path)
    records = []
    for source in source_records:
        R = int(source["R"])
        K = int(source["K"])
        terminals = legal_terminals(R, K)
        if not terminals:
            raise AssertionError(f"no dyadic terminal for non-near state {(R, K)}")
        records.append(
            {
                "prime": int(source["prime"]),
                "R": R,
                "K": K,
                "minimum_pair_excess": int(source["minimum_pair_excess"]),
                "terminal": terminals[0],
                "candidate_count": len(terminals),
            }
        )
    min_j_counts = Counter(int(record["terminal"]["j"]) for record in records)
    actual = {str(key): int(value) for key, value in sorted(min_j_counts.items())}
    expected = {str(key): value for key, value in EXPECTED_MIN_J_COUNTS.items()}
    if actual != expected:
        raise AssertionError(f"minimum dyadic j profile changed: {actual}")
    terminal_ns = [int(record["terminal"]["n"]) for record in records]
    return {
        "arithmetic": (
            "for all 226 non-near target-fiber hit states, enumerate coprime divisor pairs "
            "a,b|2K and all legal j with a=2^j b (mod R), then verify the exact even terminal"
        ),
        "scope_note": (
            "This is a finite boundary audit. Every non-near state in the frozen hit spectrum "
            "has a j=1 divisor-ratio terminal, but this does not prove a universal terminal selector."
        ),
        "input": path.name,
        "input_sha256": sha256(path),
        "non_near_state_count": len(records),
        "minimum_j_distribution": actual,
        "terminal_n_min": min(terminal_ns),
        "terminal_n_max": max(terminal_ns),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
