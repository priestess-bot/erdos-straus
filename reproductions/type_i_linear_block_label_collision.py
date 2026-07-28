#!/usr/bin/env python3
"""Audit coordinate-label collisions among the two blocks of linear sources."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-block-label-collision-results.json"
PRESSURE_PRIMES = (
    214_729,
    878_089,
    2_210_569,
    13_782_409,
    64_214_329,
    105_295_129,
    536_944_489,
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("linear_block_collision_sources", SOURCE_SCRIPT)


def integer_list_sha256(values: list[int]) -> str:
    return hashlib.sha256(",".join(str(value) for value in values).encode()).hexdigest()


def block_rows(prime: int) -> tuple[int, list[dict[str, int | str]]]:
    """Return p-s and p-a blocks for every directed linear source."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    rows: list[dict[str, int | str]] = []
    for R, states in states_by_R.items():
        K = (prime * R + 1) // 4
        for a, s in states:
            E = s * R + 1
            F = a * R + 1
            if (
                prime != a + s + a * s * R
                or prime - s != a * E
                or prime - a != s * F
                or E * F != 4 * K
            ):
                raise AssertionError("linear block factorization did not reconstruct")
            rows.extend(
                (
                    {"R": R, "a": a, "s": s, "kind": "E", "label": s, "value": E},
                    {"R": R, "a": a, "s": s, "kind": "F", "label": a, "value": F},
                )
            )
    return bound, sorted(
        rows,
        key=lambda row: (
            int(row["label"]),
            int(row["R"]),
            int(row["a"]),
            int(row["s"]),
            str(row["kind"]),
        ),
    )


def audit_prime(prime: int) -> dict[str, object]:
    """Strip coordinate-difference layers and check cross-label private cores."""
    bound, rows = block_rows(prime)
    labels = sorted({int(row["label"]) for row in rows})
    label_lcms = {
        label: math.lcm(*(abs(label - other) for other in labels if other != label))
        if len(labels) > 1
        else 1
        for label in labels
    }
    blocks: list[dict[str, int | str]] = []
    for row in rows:
        label = int(row["label"])
        value = int(row["value"])
        collision_lcm = label_lcms[label]
        collision_layer = math.gcd(value, collision_lcm)
        blocks.append(
            {
                **row,
                "label_collision_lcm": collision_lcm,
                "collision_layer": collision_layer,
                "private_layer": value // collision_layer,
            }
        )

    cross_label_pair_count = 0
    raw_cross_label_shared_pair_count = 0
    for index, left in enumerate(blocks):
        for right in blocks[index + 1 :]:
            if left["label"] == right["label"]:
                continue
            cross_label_pair_count += 1
            raw_gcd = math.gcd(int(left["value"]), int(right["value"]))
            if raw_gcd > 1:
                raw_cross_label_shared_pair_count += 1
            label_difference = abs(int(left["label"]) - int(right["label"]))
            if label_difference % raw_gcd:
                raise AssertionError("a block gcd escaped its coordinate difference")
            if math.gcd(int(left["private_layer"]), int(right["private_layer"])) != 1:
                raise AssertionError("cross-label private layers are not coprime")

    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "directed_linear_source_state_count": len(rows) // 2,
        "block_count": len(rows),
        "distinct_label_count": len(labels),
        "cross_label_pair_count": cross_label_pair_count,
        "raw_cross_label_shared_pair_count": raw_cross_label_shared_pair_count,
        "block_value_sha256": integer_list_sha256([int(row["value"]) for row in blocks]),
        "blocks": blocks,
    }


def run_audit(primes: tuple[int, ...] = PRESSURE_PRIMES) -> dict[str, object]:
    """Audit the exact collision decomposition on seven complete source spectra."""
    if tuple(sorted(set(primes))) != primes:
        raise ValueError("primes must be a strictly ascending tuple")
    profiles = [audit_prime(prime) for prime in primes]
    return {
        "arithmetic": (
            "for every directed linear source p=a+s+asR, form E=sR+1 dividing p-s "
            "and F=aR+1 dividing p-a; strip each block by the gcd with the lcm of "
            "coordinate differences from its label to all other labels"
        ),
        "scope_note": (
            "This exact finite collision decomposition does not make a target residue hit or compare "
            "the varying target unit groups across source moduli."
        ),
        "primes": list(primes),
        "profile_count": len(profiles),
        "directed_linear_source_state_count": sum(
            int(profile["directed_linear_source_state_count"]) for profile in profiles
        ),
        "block_count": sum(int(profile["block_count"]) for profile in profiles),
        "cross_label_pair_count": sum(
            int(profile["cross_label_pair_count"]) for profile in profiles
        ),
        "raw_cross_label_shared_pair_count": sum(
            int(profile["raw_cross_label_shared_pair_count"]) for profile in profiles
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
