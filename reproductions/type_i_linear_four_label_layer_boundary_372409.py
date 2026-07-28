#!/usr/bin/env python3
"""Certify a complete linear-spectrum target hit that needs all four label layers."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
LAYER_SCRIPT = ROOT / "reproductions" / "type_i_linear_label_layer_support_profile.py"
TAIL_MISS_INPUT = (
    ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-four-label-layer-boundary-372409-results.json"
)
PRIME = 372_409
EXPECTED_TAIL_MISS_INPUT_SHA256 = (
    "426ef578d796c7307505e87d16794d28569a91d8297693ec742bcf21873d4f77"
)
EXPECTED_HIT_RS = [7, 59, 83, 131, 471]
EXPECTED_SUPPORT_COUNTS = {"1": 8, "2": 1, "4": 2}


def load_module(name: str, path: Path):
    """Load the layer-audit helpers without running their command-line entry point."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


layers = load_module("four_label_layer_helpers", LAYER_SCRIPT)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_tail_miss_membership(path: Path = TAIL_MISS_INPUT) -> None:
    """Guard that the pressure prime is a stored ordinary Type II tail miss."""
    if file_sha256(path) != EXPECTED_TAIL_MISS_INPUT_SHA256:
        raise AssertionError("ordinary-tail-miss input hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    primes = [int(record["prime"]) for record in payload["records"]]
    if (
        int(payload["ordinary_tail_miss_count"]) != 1_717
        or len(primes) != 1_717
        or primes != sorted(primes)
        or PRIME not in primes
    ):
        raise AssertionError("the selected core prime is no longer a frozen tail miss")


def matching_square_divisors(K: int, R: int) -> list[int]:
    """Directly enumerate every K-squared target divisor at one source modulus."""
    return [
        int(divisor)
        for divisor in sympy.divisors(K * K)
        if int(divisor) % R == (-K) % R
    ]


def run_audit(tail_miss_input: Path = TAIL_MISS_INPUT) -> dict[str, object]:
    """Audit every linear source modulus of p=372409 without search cutoffs."""
    checked_tail_miss_membership(tail_miss_input)
    bound, states_by_R = layers.sources.enumerate_linear_source_states(PRIME)
    labels, collision_lcms = layers.coordinate_label_lcms(states_by_R)
    records = []
    support_counts: Counter[str] = Counter()
    hit_Rs = []
    for R, states in states_by_R.items():
        K = (PRIME * R + 1) // 4
        matches = matching_square_divisors(K, R)
        if not matches:
            continue
        hit_Rs.append(R)
        orientations = [
            layers.audit_orientation(PRIME, R, a, s, collision_lcms)
            for a, s in states
        ]
        for orientation in orientations:
            support_counts[str(orientation["minimum_target_layer_support"])] += 1
        records.append(
            {
                "R": R,
                "K": K,
                "K_factorization": layers.factorization_payload(
                    layers.exact_factorization(K)
                ),
                "matching_square_divisors": matches,
                "orientations": orientations,
            }
        )
    support_counts = dict(sorted(support_counts.items()))
    if hit_Rs != EXPECTED_HIT_RS:
        raise AssertionError("complete target-hit modulus list changed")
    if support_counts != EXPECTED_SUPPORT_COUNTS:
        raise AssertionError("four-layer support boundary changed")
    four_layer_orientations = [
        orientation
        for record in records
        for orientation in record["orientations"]
        if int(orientation["minimum_target_layer_support"]) == 4
    ]
    expected_four_layer_states = {(471, 1, 789), (471, 789, 1)}
    if {
        (int(item["R"]), int(item["a"]), int(item["s"]))
        for item in four_layer_orientations
    } != expected_four_layer_states:
        raise AssertionError("four-layer states changed")
    if any(
        item["minimum_target_layer_masks"] != [list(layers.LAYER_NAMES)]
        for item in four_layer_orientations
    ):
        raise AssertionError("a four-layer state acquired a proper hitting subset")
    return {
        "arithmetic": (
            "enumerate every linear source p=a+s+asR through its exact "
            "min(a,s) bound; directly enumerate every d|K^2 with d=-K mod R; "
            "then test every nonempty coordinate-label layer subproduct"
        ),
        "scope_note": (
            "This is a complete one-prime counterexample to reducing every "
            "fixed successful orientation to at most three full label layers. "
            "The same prime still has other target hits of smaller support."
        ),
        "ordinary_tail_miss_input": tail_miss_input.name,
        "ordinary_tail_miss_input_sha256": file_sha256(tail_miss_input),
        "prime": PRIME,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(states_by_R),
        "complete_directed_linear_source_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "coordinate_label_count": len(labels),
        "target_hit_Rs": hit_Rs,
        "directed_target_hit_source_count": sum(
            len(record["orientations"]) for record in records
        ),
        "minimum_target_layer_support_counts": support_counts,
        "four_layer_orientations": four_layer_orientations,
        "target_hit_records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-miss-input", type=Path, default=TAIL_MISS_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.tail_miss_input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "prime": result["prime"],
                "complete_linear_R_count": result["complete_linear_R_count"],
                "target_hit_Rs": result["target_hit_Rs"],
                "minimum_target_layer_support_counts": result[
                    "minimum_target_layer_support_counts"
                ],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
