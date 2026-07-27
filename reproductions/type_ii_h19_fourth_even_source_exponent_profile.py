#!/usr/bin/env python3
"""Measure the square-tail exponent power needed by finite-product tail states."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUBGROUP_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-subgroup-profile-640775689-results.json"
)
DEFAULT_TAIL_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-tail-profile-640775689-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-exponent-profile-640775689-results.json"
)
DEFAULT_POWER_CAP = 12


def factorization_from_ray(ray: dict[str, object]) -> dict[int, int]:
    """Factor M1 from its stored k and s factors without factoring M1 itself."""
    factors: dict[int, int] = {}
    for value in (int(ray["k"]), int(ray["s"])):
        for prime, exponent in sympy.factorint(value).items():
            factors[int(prime)] = factors.get(int(prime), 0) + int(exponent)
    return factors


def divisor_residues(modulus: int, factors: dict[int, int], power: int) -> set[int]:
    """Return residues of all divisors of M1 to the given power."""
    residues = {1}
    for prime, exponent in factors.items():
        prime_powers = [pow(prime, index, modulus) for index in range(power * exponent + 1)]
        residues = {
            left * right % modulus for left in residues for right in prime_powers
        }
    return residues


def run_profile(
    subgroup_payload: dict[str, object],
    tail_payload: dict[str, object],
    power_cap: int = DEFAULT_POWER_CAP,
) -> dict[str, object]:
    """Find each finite-product state's first target hit through a finite power cap."""
    if power_cap < 2:
        raise ValueError("power cap must be at least two")
    tail_by_key = {
        (int(row["distance"]), int(row["r"])): row for row in tail_payload["rays"]
    }
    records: list[dict[str, object]] = []
    for state in subgroup_payload["records"]:
        if state["classification"] != "finite-product-set":
            continue
        key = (int(state["distance"]), int(state["r"]))
        ray = tail_by_key[key]
        factors = factorization_from_ray(ray)
        target = int(state["target_residue"])
        first_power = None
        for power in range(2, power_cap + 1):
            residues = divisor_residues(key[1], factors, power)
            if target in residues:
                first_power = power
                break
        if int(state["tail_residue_factor_count"]) or first_power == 2:
            raise AssertionError("finite-product state unexpectedly hits at square power")
        records.append(
            {
                "distance": key[0],
                "r": key[1],
                "m1_factorization": {
                    str(prime): exponent for prime, exponent in sorted(factors.items())
                },
                "first_cover_power_through_cap": first_power,
            }
        )
    histogram = Counter(
        str(record["first_cover_power_through_cap"])
        if record["first_cover_power_through_cap"] is not None
        else f">{power_cap}"
        for record in records
    )
    return {
        "arithmetic": (
            "exact M1 factorization from k and s and exhaustive bounded exponent "
            "enumeration of all divisor residues modulo each r"
        ),
        "scope_note": (
            "A finite exponent-deficit profile. It does not assert that the "
            "required prime-factor repetitions can be forced."
        ),
        "prime": subgroup_payload["prime"],
        "power_cap": power_cap,
        "finite_product_state_count": len(records),
        "first_cover_power_histogram": dict(sorted(histogram.items())),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subgroup-input", type=Path, default=DEFAULT_SUBGROUP_INPUT)
    parser.add_argument("--tail-input", type=Path, default=DEFAULT_TAIL_INPUT)
    parser.add_argument("--power-cap", type=int, default=DEFAULT_POWER_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    subgroup_payload = json.loads(args.subgroup_input.read_text(encoding="utf-8"))
    tail_payload = json.loads(args.tail_input.read_text(encoding="utf-8"))
    result = run_profile(subgroup_payload, tail_payload, args.power_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
