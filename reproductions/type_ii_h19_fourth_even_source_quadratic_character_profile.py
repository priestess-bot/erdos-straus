#!/usr/bin/env python3
"""Find explicit quadratic characters for fourth-pressure-point tail obstructions."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-subgroup-profile-640775689-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-quadratic-character-640775689-results.json"
)


def quadratic_character(support: tuple[int, ...], value: int) -> int:
    """Evaluate the product of Legendre characters on a unit."""
    if any(math.gcd(prime, value) != 1 for prime in support):
        raise ValueError("quadratic character input must be a unit")
    return math.prod(int(sympy.legendre_symbol(value % prime, prime)) for prime in support)


def separating_quadratic_support(
    modulus: int, generators: list[int], target: int
) -> tuple[int, ...] | None:
    """Return a smallest CRT quadratic character killing generators but not target."""
    primes = tuple(sorted(sympy.factorint(modulus)))
    for size in range(1, len(primes) + 1):
        for support in itertools.combinations(primes, size):
            if (
                all(quadratic_character(support, generator) == 1 for generator in generators)
                and quadratic_character(support, target) == -1
            ):
                return support
    return None


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Compile explicit low-order separators for all subgroup-character failures."""
    records: list[dict[str, object]] = []
    for row in payload["records"]:
        if row["classification"] != "subgroup-character":
            continue
        support = separating_quadratic_support(
            int(row["r"]),
            [int(value) for value in row["generator_primes"]],
            int(row["target_residue"]),
        )
        if support is None:
            raise AssertionError("subgroup obstruction lacks a quadratic separator")
        if quadratic_character(support, -1) != -1:
            raise AssertionError("separator must distinguish the negative tail target")
        records.append(
            {
                "distance": int(row["distance"]),
                "r": int(row["r"]),
                "generated_subgroup_index": int(row["generated_subgroup_index"]),
                "quadratic_character_support": list(support),
            }
        )
    return {
        "arithmetic": (
            "exact factorization of each r and exhaustive enumeration of its "
            "CRT quadratic characters, checked on every M1 prime generator"
        ),
        "scope_note": (
            "A finite low-order character profile for one pressure point. It "
            "does not show that quadratic characters suffice in general."
        ),
        "prime": payload["prime"],
        "subgroup_character_ray_count": len(records),
        "quadratically_separated_count": len(records),
        "higher_order_remainder_count": 0,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
