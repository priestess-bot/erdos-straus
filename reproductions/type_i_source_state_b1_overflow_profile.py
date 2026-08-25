#!/usr/bin/env python3
"""Measure the least square-divisor exponent overflow resolving B=1 misses."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
TAIL = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-source-state-b1-overflow-profile-results.json"


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for factor, exponent in factors.items():
        result = [value * factor**power for value in result for power in range(exponent + 1)]
    return sorted(result)


def overflow(factor: int, base_factors: dict[int, int]) -> int:
    factors = {int(prime): int(exponent) for prime, exponent in sympy.factorint(factor).items()}
    return sum(max(0, exponent - base_factors.get(prime, 0)) for prime, exponent in factors.items())


def square_divisor_witness(prime: int, source: int, bridge: int, K: int, factor: int) -> dict[str, int] | None:
    offset = prime - source
    if offset <= 0 or (bridge - 1) % offset:
        return None
    R = (bridge - 1) // offset
    if factor % R != -pow(4, -1, R) % R:
        return None
    B = factor // math.gcd(factor, K)
    D = factor // B
    if D % B:
        return None
    C = D // B
    H = K // D
    if K % D or (H + B) % R or (4 * B * B * C + 1) % R:
        return None
    A = (H + B) // R
    m = (4 * B * B * C + 1) // R
    if math.gcd(A, B) != 1 or bridge * (source * K // bridge) != source * K:
        return None
    a = source * K // bridge
    if Fraction(4, source) != Fraction(1, a) + Fraction(1, A * B * C) + Fraction(1, A * C * H):
        return None
    if Fraction(4, prime) != Fraction(1, A * B * C) + Fraction(1, A * C * H) + Fraction(1, prime * K):
        return None
    return {"F": factor, "B": B, "C": C, "H": H, "A": A, "m": m}


def profile(records: list[dict[str, object]], label: str) -> dict[str, object]:
    rows = []
    for entry in records:
        prime = int(entry["prime"])
        edge = entry["selected_edge"]
        source = int(edge["reverse_two_tail_lift"]["source_denominator"])
        bridge, K = int(edge["E"]), int(edge["K"])
        _offset, R = prime - source, (bridge - 1) // (prime - source)
        target = -pow(4, -1, R) % R
        base_factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(K).items()}
        if any(divisor % R == target for divisor in divisors(base_factors)):
            continue
        square_factors = {factor: 2 * exponent for factor, exponent in base_factors.items()}
        candidates = []
        for factor in divisors(square_factors):
            witness = square_divisor_witness(prime, source, bridge, K, factor)
            if witness is not None:
                candidates.append((overflow(factor, base_factors), witness))
        if not candidates:
            raise AssertionError("B=1 miss had no valid square-divisor realization")
        extra, witness = min(candidates, key=lambda item: (item[0], item[1]["B"], item[1]["F"]))
        rows.append({"prime": prime, "R": R, "extra_exponent_count": extra, "witness": witness})
    histogram = Counter(str(row["extra_exponent_count"]) for row in rows)
    return {
        "label": label,
        "B_eq_1_miss_count": len(rows),
        "least_extra_exponent_histogram": dict(sorted(histogram.items(), key=lambda item: int(item[0]))),
        "maximum_extra_exponent_count": max((row["extra_exponent_count"] for row in rows), default=None),
        "records": rows,
    }


def run_audit(h19: dict[str, object], tail: dict[str, object]) -> dict[str, object]:
    if len(h19["records"]) != 664 or len(tail["records"]) != 1717:
        raise AssertionError("inputs do not match the stored H19 and 500M bridge profiles")
    h19_profile = profile(h19["records"], "H19-1B")
    tail_profile = profile(tail["records"], "tail-500M")
    if (h19_profile["B_eq_1_miss_count"], tail_profile["B_eq_1_miss_count"]) != (17, 72):
        raise AssertionError("B=1 miss counts diverged from the realization audits")
    return {
        "arithmetic": (
            "for every B=1 source-state miss, enumerate F|K^2 with 4F=-1 (mod R), canonically recover "
            "B=F/gcd(F,K), C,H,A,m, and retain the valid witness of least exponent excess over K"
        ),
        "scope_note": (
            "A finite square-divisor overflow profile. A small exponent excess need not produce a small "
            "integer B, and the result does not supply a recursive construction of the repeated factors."
        ),
        "profiles": [h19_profile, tail_profile],
        "total_B_eq_1_miss_count": h19_profile["B_eq_1_miss_count"] + tail_profile["B_eq_1_miss_count"],
        "total_least_extra_exponent_histogram": {
            "1": sum(profile["least_extra_exponent_histogram"].get("1", 0) for profile in (h19_profile, tail_profile)),
            "2": sum(profile["least_extra_exponent_histogram"].get("2", 0) for profile in (h19_profile, tail_profile)),
        },
        "maximum_extra_exponent_count": max(
            h19_profile["maximum_extra_exponent_count"], tail_profile["maximum_extra_exponent_count"]
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.h19.read_text(encoding="utf-8")),
        json.loads(args.tail.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "profiles"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
