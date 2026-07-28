#!/usr/bin/env python3
"""Audit the full label/modulus collision rigidity of linear-source blocks."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-labeled-block-gcd-rigidity-results.json"
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


sources = load_module("labeled_block_rigidity_sources", SOURCE_SCRIPT)


def integer_list_sha256(values: list[int]) -> str:
    return hashlib.sha256(",".join(str(value) for value in values).encode("ascii")).hexdigest()


def coordinate_blocks(prime: int) -> tuple[int, int, list[dict[str, int]]]:
    """Return distinct blocks B(t,R)=tR+1 from the complete source spectrum."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    identities: set[tuple[int, int]] = set()
    raw_block_occurrence_count = 0
    for R, states in states_by_R.items():
        for a, s in states:
            if prime != a + s + a * s * R:
                raise AssertionError("linear source state did not reconstruct")
            identities.update(((a, R), (s, R)))
            raw_block_occurrence_count += 2

    blocks = [
        {"label": label, "R": R, "value": label * R + 1}
        for label, R in sorted(identities)
    ]
    if any(block["value"] <= 1 for block in blocks):
        raise AssertionError("linear block is not positive")
    return bound, raw_block_occurrence_count, blocks


def collision_lcm(block: dict[str, int], blocks: list[dict[str, int]]) -> tuple[int, int, int]:
    """Collect every numerical difference capable of supporting a common factor."""
    label = block["label"]
    modulus = block["R"]
    label_differences = sorted(
        {
            abs(label - other["label"])
            for other in blocks
            if other["label"] != label
        }
    )
    modulus_differences = sorted(
        {
            abs(modulus - other["R"])
            for other in blocks
            if other["label"] == label and other["R"] != modulus
        }
    )
    differences = [*label_differences, *modulus_differences]
    return (
        math.lcm(*differences) if differences else 1,
        math.lcm(*label_differences) if label_differences else 1,
        math.lcm(*modulus_differences) if modulus_differences else 1,
    )


def audit_prime(prime: int) -> dict[str, object]:
    """Check every pair of distinct coordinate blocks for the exact gcd rules."""
    bound, raw_block_occurrence_count, raw_blocks = coordinate_blocks(prime)
    blocks: list[dict[str, int]] = []
    for raw_block in raw_blocks:
        full_lcm, label_lcm, modulus_lcm = collision_lcm(raw_block, raw_blocks)
        value = raw_block["value"]
        collision_layer = math.gcd(value, full_lcm)
        blocks.append(
            {
                **raw_block,
                "collision_lcm": full_lcm,
                "label_difference_lcm": label_lcm,
                "modulus_difference_lcm": modulus_lcm,
                "collision_layer": collision_layer,
                "private_layer": value // collision_layer,
            }
        )

    pair_counts = {"different_label": 0, "same_label_different_R": 0}
    raw_shared_pair_counts = {"different_label": 0, "same_label_different_R": 0}
    for index, left in enumerate(blocks):
        for right in blocks[index + 1 :]:
            raw_gcd = math.gcd(left["value"], right["value"])
            if left["label"] != right["label"]:
                kind = "different_label"
                difference = abs(left["label"] - right["label"])
                if difference % raw_gcd:
                    raise AssertionError("a cross-label block gcd escaped its label difference")
            else:
                kind = "same_label_different_R"
                difference = abs(left["R"] - right["R"])
                if raw_gcd != math.gcd(left["value"], difference):
                    raise AssertionError("same-label block gcd did not equal its modulus-difference gcd")
            pair_counts[kind] += 1
            if raw_gcd > 1:
                raw_shared_pair_counts[kind] += 1
            if math.gcd(left["private_layer"], right["private_layer"]) != 1:
                raise AssertionError("distinct blocks retained a common private factor")

    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "raw_block_occurrence_count": raw_block_occurrence_count,
        "distinct_coordinate_block_count": len(blocks),
        "duplicate_block_occurrence_count": raw_block_occurrence_count - len(blocks),
        "pair_counts": pair_counts,
        "raw_shared_pair_counts": raw_shared_pair_counts,
        "block_value_sha256": integer_list_sha256([block["value"] for block in blocks]),
        "blocks": blocks,
    }


def run_audit(primes: tuple[int, ...] = PRESSURE_PRIMES) -> dict[str, object]:
    """Audit all complete pressure spectra with the joint collision lcm."""
    if tuple(sorted(set(primes))) != primes:
        raise ValueError("primes must be a strictly ascending tuple")
    profiles = [audit_prime(prime) for prime in primes]
    return {
        "arithmetic": (
            "for distinct coordinate blocks B(t,R)=tR+1 in one complete linear source "
            "spectrum, a common divisor is controlled by |t-u| when labels differ and "
            "by |R-U| when labels agree; strip each block by the gcd with the lcm of "
            "all such eligible differences"
        ),
        "scope_note": (
            "This exact finite collision decomposition does not produce a target residue hit, "
            "and it does not compare target unit groups attached to different moduli."
        ),
        "primes": list(primes),
        "profile_count": len(profiles),
        "raw_block_occurrence_count": sum(
            int(profile["raw_block_occurrence_count"]) for profile in profiles
        ),
        "distinct_coordinate_block_count": sum(
            int(profile["distinct_coordinate_block_count"]) for profile in profiles
        ),
        "duplicate_block_occurrence_count": sum(
            int(profile["duplicate_block_occurrence_count"]) for profile in profiles
        ),
        "pair_counts": {
            kind: sum(int(profile["pair_counts"][kind]) for profile in profiles)
            for kind in ("different_label", "same_label_different_R")
        },
        "raw_shared_pair_counts": {
            kind: sum(int(profile["raw_shared_pair_counts"][kind]) for profile in profiles)
            for kind in ("different_label", "same_label_different_R")
        },
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
