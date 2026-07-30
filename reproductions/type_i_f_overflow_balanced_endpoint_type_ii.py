#!/usr/bin/env python3
"""Audit the exact Type-II boundary for balanced lower-modulus endpoint pairs."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-balanced-endpoint-type-ii-results.json"
EXPECTED_INPUT_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def admissible_gaps(prime: int, endpoint_sum: int) -> list[int]:
    return [
        int(gap)
        for gap in sympy.divisors(endpoint_sum)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]


def endpoint_type_ii_hits(prime: int, left: int, right: int) -> list[dict[str, int]]:
    product = left * right
    if product > prime // 2:
        return []
    hits: list[dict[str, int]] = []
    for gap in admissible_gaps(prime, left + right):
        numerator = prime + gap
        if numerator % 4:
            raise AssertionError("a legal gap must make x integral")
        x = numerator // 4
        if x % product:
            continue
        hits.append(
            {
                "gap": gap,
                "x": x,
                "A": min(left, right),
                "B": max(left, right),
                "C": x // product,
            }
        )
    return hits


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the balanced endpoint input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    profiles: list[dict[str, object]] = []
    for row in payload["records"]:
        for candidate in row["candidates"]:
            if candidate["lower_modulus_classification"] != "F_box_miss":
                continue
            prime = int(row["prime"])
            gap = int(candidate["gap"])
            modulus = int(candidate["balanced_t"])
            if gap <= 0 or modulus <= 1:
                raise AssertionError("invalid strict endpoint candidate")
            if (int(row["formal_A"]) + 1) % gap:
                raise AssertionError("formal A did not produce an integral balanced endpoint")
            if (int(row["formal_B"]) - 1) % gap:
                raise AssertionError("formal B did not produce an integral balanced endpoint")
            u = (int(row["formal_A"]) + 1) // gap
            v = (int(row["formal_B"]) - 1) // gap
            pair_gcd = math.gcd(u, v)
            if pair_gcd != int(candidate["balanced_pair_gcd"]):
                raise AssertionError("stored endpoint gcd disagrees with reconstruction")
            left = u // pair_gcd
            right = v // pair_gcd
            if math.gcd(left, right) != 1:
                raise AssertionError("reduced endpoint pair is not coprime")
            if (left + right) % modulus:
                raise AssertionError("reduced endpoints lost the lower-modulus relation")
            if (left * pow(right, -1, modulus) + 1) % modulus:
                raise AssertionError("reduced endpoints lost the target residue")
            product = left * right
            size_excluded = product > prime // 2
            hits = [] if size_excluded else endpoint_type_ii_hits(prime, left, right)
            three_t = 3 * modulus
            three_t_hit = False
            if 3 <= three_t <= prime - 2 and three_t % 4 == 3:
                x_three_t = (prime + three_t) // 4
                three_t_hit = x_three_t % product == 0
            profiles.append(
                {
                    "prime": prime,
                    "orientation": row["orientation"],
                    "original_R": int(row["original_R"]),
                    "gap": gap,
                    "lower_modulus": modulus,
                    "formal_A": int(row["formal_A"]),
                    "formal_B": int(row["formal_B"]),
                    "unreduced_u": u,
                    "unreduced_v": v,
                    "endpoint_pair_gcd": pair_gcd,
                    "reduced_u": left,
                    "reduced_v": right,
                    "endpoint_sum": left + right,
                    "endpoint_product": product,
                    "size_excluded": size_excluded,
                    "admissible_gap_count": 0 if size_excluded else len(
                        admissible_gaps(prime, left + right)
                    ),
                    "endpoint_type_ii_hits": hits,
                    "three_t_gap": three_t,
                    "three_t_endpoint_hit": three_t_hit,
                }
            )
    if len(profiles) != 42:
        raise AssertionError(f"unexpected F-box miss count: {len(profiles)}")
    small = [profile for profile in profiles if not profile["size_excluded"]]
    return {
        "arithmetic": (
            "For every frozen lower-modulus F-box miss, reconstruct the reduced coprime "
            "balanced endpoint pair U,V. A Type-II certificate using exactly this pair is "
            "equivalent to h | U+V, h=3 mod 4, h <= p-2, and U*V | (p+h)/4."
        ),
        "scope_note": (
            "Finite endpoint-pair audit only. The size bound and divisor scan do not exclude "
            "factor splitting, a different endpoint pair, a non-endpoint relation, or other "
            "Type-II normal forms."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "state_count": len(profiles),
        "size_excluded_count": sum(bool(profile["size_excluded"]) for profile in profiles),
        "small_product_count": len(small),
        "endpoint_type_ii_hit_count": sum(
            bool(profile["endpoint_type_ii_hits"]) for profile in profiles
        ),
        "three_t_endpoint_hit_count": sum(
            bool(profile["three_t_endpoint_hit"]) for profile in profiles
        ),
        "small_product_profiles": [
            {
                "prime": profile["prime"],
                "orientation": profile["orientation"],
                "lower_modulus": profile["lower_modulus"],
                "reduced_u": profile["reduced_u"],
                "reduced_v": profile["reduced_v"],
                "endpoint_product": profile["endpoint_product"],
                "admissible_gap_count": profile["admissible_gap_count"],
                "endpoint_type_ii_hits": profile["endpoint_type_ii_hits"],
            }
            for profile in small
        ],
        "profiles": profiles,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "state_count",
                    "size_excluded_count",
                    "small_product_count",
                    "endpoint_type_ii_hit_count",
                    "three_t_endpoint_hit_count",
                    "small_product_profiles",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
