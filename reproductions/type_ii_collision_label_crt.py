#!/usr/bin/env python3
"""Compile collision-source labels into a CRT state for one-new Type II factors."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-two-collision-release-372271201-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-collision-label-crt-372271201-results.json"
)


def combine_coprime_congruences(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    """Return the least CRT residue and product modulus for coprime moduli."""
    residue, modulus = 0, 1
    for next_residue, next_modulus in congruences:
        if next_modulus < 2 or math.gcd(modulus, next_modulus) != 1:
            raise ValueError("CRT moduli must be pairwise coprime and at least two")
        multiplier = ((next_residue - residue) * pow(modulus, -1, next_modulus)) % next_modulus
        residue += modulus * multiplier
        modulus *= next_modulus
        residue %= modulus
    return residue, modulus


def label_state(
    prime: int, witness: dict[str, object], base_shift_bound: int
) -> dict[str, object]:
    """Verify all collision source classes and compile their CRT intersection."""
    shift = int(witness["shift"])
    labels = witness["collision_source_labels"]
    congruences: list[tuple[int, int]] = []
    collision_product = 1
    for label in labels:
        factor = int(label["prime"])
        sources = [int(source) for source in label["source_shifts"]]
        residue = int(label["target_shift_residue"])
        expected_sources = [
            source
            for source in range(1, base_shift_bound + 1)
            if (prime + 4 * source) % factor == 0
        ]
        if sources != expected_sources or not sources:
            raise AssertionError("stored collision sources are not complete")
        if any(source % factor != residue for source in sources) or shift % factor != residue:
            raise AssertionError("collision source class does not force the target shift")
        congruences.append((residue, factor))
        collision_product *= factor
    if len({modulus for _, modulus in congruences}) != len(congruences):
        raise AssertionError("collision labels must use distinct primes")
    crt_residue, crt_modulus = (
        combine_coprime_congruences(congruences) if congruences else (0, 1)
    )
    if shift % crt_modulus != crt_residue:
        raise AssertionError("target shift misses the label CRT class")
    factors = witness["h_factorization"]
    new = [
        int(factor["prime"])
        for factor in factors
        if int(factor["prime"]) not in {int(label["prime"]) for label in labels}
    ]
    if len(new) != 1:
        raise AssertionError("audit expects exactly one non-collision prime")
    new_prime = new[0]
    modulus = 4 * int(witness["a"]) * int(witness["c"])
    if math.gcd(collision_product, modulus) != 1:
        raise AssertionError("collision product must be invertible modulo the ray modulus")
    forced_residue = (-pow(collision_product, -1, modulus)) % modulus
    if new_prime % modulus != forced_residue:
        raise AssertionError("new factor misses its forced inverse residue")
    return {
        "shift": shift,
        "collision_product": collision_product,
        "collision_label_crt_residue": crt_residue,
        "collision_label_crt_modulus": crt_modulus,
        "new_prime": new_prime,
        "ray_modulus": modulus,
        "new_prime_residue": new_prime % modulus,
        "forced_new_prime_residue": forced_residue,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile the first two-collision, one-collision, and pure release states."""
    by_cap = {int(row["shift_cap"]): row for row in payload["records"]}
    selected = [
        by_cap[200]["best_witness"],
        by_cap[401]["first_zero_or_one_collision"],
        by_cap[484]["first_pure_new"],
    ]
    if any(witness is None for witness in selected):
        raise AssertionError("release audit is missing a selected witness")
    states = [
        label_state(int(payload["prime"]), witness, int(payload["base_shift_bound"]))
        for witness in selected
    ]
    return {
        "arithmetic": (
            "exact collision-source divisibility, CRT intersection, and "
            "Type II inverse-residue checks"
        ),
        "scope_note": (
            "A state compilation for one delayed-release example. The observed "
            "CRT moduli do not assert a monotone release invariant."
        ),
        "prime": payload["prime"],
        "base_shift_bound": payload["base_shift_bound"],
        "states": states,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
