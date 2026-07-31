#!/usr/bin/env python3
"""Verify focused same-1-mod-4 non-source D-only no-go examples."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "two-denominator-lift-same-one-mod-four-no-go-results.json"
)

CASES = (
    {
        "name": "unified_w_one_minimal_core",
        "p": 73,
        "n": 65,
        "delta": 1,
        "expected": {"a": 65, "b": 2, "c": 1, "w": 1},
    },
    {
        "name": "square_excess_minimal_core",
        "p": 193,
        "n": 185,
        "delta": 25,
        "expected": {"a": 37, "b": 1, "c": 1, "w": 5},
    },
    {
        "name": "e0_target_inside_window_but_not_divisor",
        "p": 673,
        "n": 657,
        "delta": 81,
        "expected": {"a": 73, "b": 1, "c": 1, "w": 9},
    },
    {
        "name": "clean_overflow_w_one",
        "p": 1_129,
        "n": 1_125,
        "delta": 5,
        "expected": {"a": 225, "b": 14, "c": 5, "w": 1},
        "overflow": {"M": 1_021, "R_M": 2_959, "d": 311, "C": 818},
    },
    {
        "name": "clean_overflow_square_excess",
        "p": 1_129,
        "n": 1_125,
        "delta": 405,
        "expected": {"a": 25, "b": 1, "c": 5, "w": 9},
        "overflow": {"M": 1_021, "R_M": 2_959, "d": 311, "C": 818},
    },
)


def divisors(value: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        low.append(divisor)
        if divisor * divisor != value:
            high.append(value // divisor)
    return low + high[::-1]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def analyze(case: dict[str, object]) -> dict[str, object]:
    p = int(case["p"])
    n = int(case["n"])
    delta = int(case["delta"])
    expected = {key: int(value) for key, value in dict(case["expected"]).items()}
    r = p - n
    modulus = 4 * r
    product = p * n
    D = p * delta
    complement = product * product // D

    assert is_prime(p)
    assert p % 4 == 1 and n % 4 == 1
    assert 2 <= n < p and r % 4 == 0 and r >= 4
    assert n * n % delta == 0
    assert product * product % D == 0
    assert 0 < D < n * n
    assert (D - product) % modulus == 0
    assert (complement - product) % modulus == 0
    assert n * n % D != 0

    source_coordinate = (product - D) // modulus
    target_coordinate = (complement - product) // modulus
    assert source_coordinate > 0 and target_coordinate > 0
    assert source_coordinate % p == 0 and target_coordinate % p == 0
    t = source_coordinate // p
    lam = target_coordinate // p
    mu = 4 * lam - 1
    H = n * n // delta
    assert H == p + mu * r
    assert 4 * lam * lam % H == 0
    s = 4 * lam * lam // H
    assert t == lam - r * s and t > 0

    common = gcd(H, lam)
    a = H // common
    assert common % a == 0
    c = common // a
    b = lam // common
    w = a - 4 * r * b
    normal = {"a": a, "b": b, "c": c, "w": w}
    assert normal == expected
    assert H == a * a * c
    assert lam == a * b * c
    assert gcd(a, b) == 1
    assert w > 0 and w % 2 == 1
    assert n == a * c * w
    assert delta == c * w * w
    assert t == b * c * w
    assert a == w + 4 * r * b and a > 16 * b
    assert (delta != 0 and n % delta == 0) == (w == 1)

    targets = {
        "e0": (-p * lam) % mu,
        "e1": (-lam) % mu,
        "e2": (-pow(p, -1, mu) * lam) % mu,
    }
    assert targets["e1"] == mu - lam > lam
    assert targets["e2"] == mu - 4 * b * b * c > lam

    hits: list[dict[str, int | str]] = []
    for value in divisors(lam * lam):
        if value >= lam:
            continue
        for target_name, residue in targets.items():
            if value % mu == residue:
                hits.append({"target": target_name, "divisor": value})
    assert not hits

    e0_inside_window = targets["e0"] < lam
    if e0_inside_window:
        assert lam * lam % targets["e0"] != 0
        numerator = 4 * targets["e0"] + p
        assert numerator % mu == 0
        quotient = numerator // mu
        assert quotient > 0
    else:
        quotient = None

    overflow = None
    if "overflow" in case:
        raw = {key: int(value) for key, value in dict(case["overflow"]).items()}
        M = raw["M"]
        R_M = raw["R_M"]
        d = raw["d"]
        C = raw["C"]
        assert p * n == 4 * M * d + 1
        assert R_M == 4 * M - n and R_M > p
        assert C == p - d
        assert 4 * M * C == p * R_M + 1
        overflow = raw

    return {
        "name": str(case["name"]),
        "p": p,
        "n": n,
        "r": r,
        "D": D,
        "delta": delta,
        "delta_divides_n": n % delta == 0,
        "source_coordinate": source_coordinate,
        "target_coordinate": target_coordinate,
        "t": t,
        "lambda": lam,
        "mu": mu,
        "H": H,
        "s": s,
        "normal_form": normal,
        "target_residues": targets,
        "e0_inside_normalized_window": e0_inside_window,
        "e0_quotient": quotient,
        "normalized_target_hits": hits,
        "overflow": overflow,
    }


def run() -> dict[str, object]:
    records = [analyze(case) for case in CASES]

    # This is the sharp excluded boundary of the abstract Vieta lemma.
    X, Y, L, m, c = 1, 2, 1, 2, 1
    assert 2 * X * Y * L * m * c == (
        X * X * m * c + Y * Y * L * c + L * m
    )

    summary = {
        "parameter_count": len(records),
        "w_one_count": sum(record["normal_form"]["w"] == 1 for record in records),
        "square_excess_count": sum(
            record["normal_form"]["w"] >= 3 for record in records
        ),
        "e0_inside_window_count": sum(
            bool(record["e0_inside_normalized_window"]) for record in records
        ),
        "normalized_target_hit_count": sum(
            len(record["normalized_target_hits"]) for record in records
        ),
        "clean_overflow_parameter_count": sum(
            record["overflow"] is not None for record in records
        ),
    }
    assert summary == {
        "parameter_count": 5,
        "w_one_count": 2,
        "square_excess_count": 3,
        "e0_inside_window_count": 2,
        "normalized_target_hit_count": 0,
        "clean_overflow_parameter_count": 2,
    }

    return {
        "schema_version": "same-one-mod-four-d-only-no-go/v1",
        "scope_note": (
            "Focused exact verification of five non-source D-only parameters, "
            "their unified normal forms, and their normalized target misses. "
            "It is not a historical scan or a substitute for the Vieta proof."
        ),
        "summary": summary,
        "vieta_lemma_excluded_boundary": {
            "X": X,
            "Y": Y,
            "L": L,
            "m": m,
            "c": c,
        },
        "records": records,
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
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
