#!/usr/bin/env python3
"""Audit shortest lower-modulus F relations and direct Type-II endpoint bridges."""

from __future__ import annotations

from collections import Counter, deque
import hashlib
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-shortest-relation-results.json"
EXPECTED_INPUT_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def shortest_relation(
    factors: list[tuple[int, int]], modulus: int
) -> tuple[int, ...]:
    """Find an exact shortest l1 exponent vector mapping to -1 mod modulus."""
    generators = [int(q) for q, _nu in factors]
    inverses = [pow(q, -1, modulus) for q in generators]
    start = 1 % modulus
    target = modulus - 1
    queue: deque[int] = deque([start])
    vectors: dict[int, tuple[int, ...]] = {start: (0,) * len(generators)}
    while queue:
        residue = queue.popleft()
        vector = vectors[residue]
        if residue == target:
            return vector
        for index, (generator, inverse) in enumerate(zip(generators, inverses)):
            for step, multiplier in ((1, generator), (-1, inverse)):
                next_residue = residue * multiplier % modulus
                if next_residue in vectors:
                    continue
                next_vector = list(vector)
                next_vector[index] += step
                vectors[next_residue] = tuple(next_vector)
                queue.append(next_residue)
    raise AssertionError("the lower-modulus target was not reached")


def admissible_type_ii_gaps(prime: int, endpoint_sum: int) -> list[int]:
    return [
        int(gap)
        for gap in sympy.divisors(endpoint_sum)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]


def type_ii_endpoint_hits(prime: int, left: int, right: int) -> list[dict[str, int]]:
    """Check the exact Type-II normal form for the endpoint pair."""
    product = left * right
    if product > prime // 2:
        return []
    hits = []
    for gap in admissible_type_ii_gaps(prime, left + right):
        numerator = prime + gap
        if numerator % 4:
            continue
        x = numerator // 4
        if x % product:
            continue
        hits.append({"gap": gap, "x": x, "C": x // product})
    return hits


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the lower-modulus split input changed")
    if sha256(SOURCE_INPUT) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): dict(row)
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }
    profiles: list[dict[str, object]] = []
    for row in payload["records"]:
        key = (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"]))
        source_row = source_rows[key]
        for candidate in row["candidates"]:
            if candidate["lower_modulus_classification"] != "F_box_miss":
                continue
            prime = int(row["prime"])
            original_R = int(row["R"])
            gap = int(candidate["gap"])
            modulus = int(candidate["balanced_t"])
            factors = [(int(q), int(nu)) for q, nu in source_row["factorization"]]
            vector = shortest_relation(factors, modulus)
            residue = 1 % modulus
            for (q, _nu), exponent in zip(factors, vector):
                power = (
                    pow(q, exponent, modulus)
                    if exponent >= 0
                    else pow(pow(q, -1, modulus), -exponent, modulus)
                )
                residue = residue * power % modulus
            if residue != modulus - 1:
                raise AssertionError("shortest relation did not reach -1")
            positive = math.prod(
                q**max(exponent, 0) for (q, _nu), exponent in zip(factors, vector)
            )
            negative = math.prod(
                q**max(-exponent, 0) for (q, _nu), exponent in zip(factors, vector)
            )
            if math.gcd(positive, negative) != 1:
                raise AssertionError("shortest relation endpoints are not coprime")
            if (positive + negative) % modulus:
                raise AssertionError("shortest relation endpoints lost the target sum")
            overflow = sum(
                max(abs(exponent) - nu, 0)
                for (_q, nu), exponent in zip(factors, vector)
            )
            endpoint_product = positive * negative
            size_excluded = endpoint_product > prime // 2
            endpoint_hits = [] if size_excluded else type_ii_endpoint_hits(
                prime, positive, negative
            )
            three_t_gap = 3 * modulus
            three_t_hit = False
            if 3 <= three_t_gap <= prime - 2 and three_t_gap % 4 == 3:
                numerator = prime + three_t_gap
                if numerator % 4 == 0:
                    three_t_x = numerator // 4
                    three_t_hit = three_t_x % endpoint_product == 0
            profiles.append(
                {
                    "prime": prime,
                    "orientation": row["orientation"],
                    "original_R": original_R,
                    "gap": gap,
                    "lower_modulus": modulus,
                    "factorization": [[int(q), int(nu)] for q, nu in factors],
                    "shortest_relation": list(vector),
                    "shortest_l1": sum(abs(exponent) for exponent in vector),
                    "positive_endpoint": positive,
                    "negative_endpoint": negative,
                    "endpoint_product": endpoint_product,
                    "overflow_layers": overflow,
                    "size_excluded": size_excluded,
                    "endpoint_type_ii_hits": endpoint_hits,
                    "three_t_gap": three_t_gap,
                    "three_t_endpoint_hit": three_t_hit,
                }
            )
    if len(profiles) != 42:
        raise AssertionError(f"unexpected F-box miss count: {len(profiles)}")
    small_product = [profile for profile in profiles if not profile["size_excluded"]]
    return {
        "arithmetic": (
            "For every lower-modulus F-box miss, BFS in the Cayley graph generated by "
            "q_i^{+/-1} gives an exact shortest l1 target relation. Writing it as U/V, "
            "the endpoint-pair Type-II normal form is checked for every admissible divisor "
            "of U+V; the product-size bound excludes the remaining cases."
        ),
        "scope_note": (
            "Finite audit of the 42 frozen lower-modulus F-box misses. A shortest relation "
            "is a choice-invariant word-length witness, but failure of this endpoint-pair "
            "Type-II bridge does not exclude factor-splitting, non-shortest relations, or "
            "other Type-II forms."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "factorization_input": SOURCE_INPUT.name,
        "factorization_input_sha256": sha256(SOURCE_INPUT),
        "state_count": len(profiles),
        "shortest_l1_min": min(int(profile["shortest_l1"]) for profile in profiles),
        "shortest_l1_max": max(int(profile["shortest_l1"]) for profile in profiles),
        "overflow_layers_min": min(int(profile["overflow_layers"]) for profile in profiles),
        "overflow_layers_max": max(int(profile["overflow_layers"]) for profile in profiles),
        "overflow_layers_histogram": {
            str(value): count
            for value, count in sorted(
                Counter(int(profile["overflow_layers"]) for profile in profiles).items()
            )
        },
        "size_excluded_count": sum(bool(profile["size_excluded"]) for profile in profiles),
        "small_product_count": len(small_product),
        "endpoint_type_ii_hit_count": sum(
            bool(profile["endpoint_type_ii_hits"]) for profile in profiles
        ),
        "three_t_endpoint_hit_count": sum(
            bool(profile["three_t_endpoint_hit"]) for profile in profiles
        ),
        "exception_small_product_profiles": [
            {
                "prime": profile["prime"],
                "original_R": profile["original_R"],
                "gap": profile["gap"],
                "lower_modulus": profile["lower_modulus"],
                "positive_endpoint": profile["positive_endpoint"],
                "negative_endpoint": profile["negative_endpoint"],
                "endpoint_sum": (
                    int(profile["positive_endpoint"]) + int(profile["negative_endpoint"])
                ),
                "endpoint_type_ii_hits": profile["endpoint_type_ii_hits"],
            }
            for profile in small_product
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
                    "shortest_l1_min",
                    "shortest_l1_max",
                    "overflow_layers_min",
                    "overflow_layers_max",
                    "size_excluded_count",
                    "small_product_count",
                    "endpoint_type_ii_hit_count",
                    "three_t_endpoint_hit_count",
                    "exception_small_product_profiles",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
