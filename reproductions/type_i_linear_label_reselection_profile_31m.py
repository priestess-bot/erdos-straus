#!/usr/bin/env python3
"""Audit three-layer label reselection on every frozen tail miss through 31M."""

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
    ROOT / "reproductions" / "type-i-linear-label-reselection-profile-31m-results.json"
)
PRIME_LIMIT = 31_000_000
EXPECTED_TAIL_MISS_INPUT_SHA256 = (
    "426ef578d796c7307505e87d16794d28569a91d8297693ec742bcf21873d4f77"
)
EXPECTED_PRIME_COUNT = 200
EXPECTED_PRIME_LIST_SHA256 = (
    "7d5ce7fdacdb45e44c8293f5fe1285cc1d5a691bf029b02e9d5a4d73cd5cd203"
)
EXPECTED_SELECTED_SUPPORT_COUNTS = {"1": 185, "2": 13, "3": 2}
EXPECTED_SELECTED_THREE_LAYER_PRIMES = [13_782_409, 26_034_649]
EXPECTED_ALL_ORIENTATION_SUPPORT_COUNTS = {"1": 1_734, "2": 839, "3": 177, "4": 29}


def load_module(name: str, path: Path):
    """Load the exact label-layer helpers without executing their CLI."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


layers = load_module("label_reselection_helpers", LAYER_SCRIPT)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_list_sha256(values: list[int]) -> str:
    """Hash an ordered integer sequence in the repository's canonical format."""
    return hashlib.sha256(
        "".join(f"{value}\n" for value in values).encode("ascii")
    ).hexdigest()


def load_tail_misses(path: Path = TAIL_MISS_INPUT) -> list[int]:
    """Freeze the complete ordinary-tail-miss prefix below the numeric limit."""
    if file_sha256(path) != EXPECTED_TAIL_MISS_INPUT_SHA256:
        raise AssertionError("ordinary-tail-miss input hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    all_primes = [int(record["prime"]) for record in payload["records"]]
    primes = [prime for prime in all_primes if prime <= PRIME_LIMIT]
    if (
        int(payload["ordinary_tail_miss_count"]) != 1_717
        or len(all_primes) != 1_717
        or all_primes != sorted(all_primes)
        or len(primes) != EXPECTED_PRIME_COUNT
        or integer_list_sha256(primes) != EXPECTED_PRIME_LIST_SHA256
        or any(prime % 24 != 1 or not sympy.isprime(prime) for prime in primes)
        or any(prime <= PRIME_LIMIT for prime in all_primes[len(primes) :])
    ):
        raise AssertionError("frozen tail-miss prefix changed")
    return primes


def audit_prime(prime: int) -> dict[str, object]:
    """Exhaust one complete linear source spectrum and select its shortest layer hit."""
    bound, states_by_R = layers.sources.enumerate_linear_source_states(prime)
    labels, collision_lcms = layers.coordinate_label_lcms(states_by_R)
    orientations = []
    target_hit_Rs = []
    for R, states in states_by_R.items():
        K = (prime * R + 1) // 4
        if R - 1 not in layers.centered_square_spectrum(
            layers.exact_factorization(K), R
        ):
            continue
        target_hit_Rs.append(R)
        orientations.extend(
            layers.audit_orientation(prime, R, a, s, collision_lcms)
            for a, s in states
        )
    if not orientations:
        raise AssertionError("a frozen tail miss has no linear general-B target hit")
    support_counts = Counter(
        str(item["minimum_target_layer_support"]) for item in orientations
    )
    support_counts = dict(sorted(support_counts.items()))
    selected = min(
        orientations,
        key=lambda item: (
            int(item["minimum_target_layer_support"]),
            int(item["R"]),
            int(item["a"]),
            int(item["s"]),
        ),
    )
    if int(selected["minimum_target_layer_support"]) > 3:
        raise AssertionError("the finite three-layer reselection profile failed")
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(states_by_R),
        "complete_directed_linear_source_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "coordinate_label_count": len(labels),
        "target_hit_R_count": len(target_hit_Rs),
        "directed_target_hit_source_count": len(orientations),
        "all_target_orientation_support_counts": support_counts,
        "selected_orientation": selected,
    }


def run_audit(tail_miss_input: Path = TAIL_MISS_INPUT) -> dict[str, object]:
    """Run the complete source-spectrum reselection audit through 31 million."""
    primes = load_tail_misses(tail_miss_input)
    profiles = [audit_prime(prime) for prime in primes]
    selected_counts = Counter(
        str(profile["selected_orientation"]["minimum_target_layer_support"])
        for profile in profiles
    )
    selected_counts = dict(sorted(selected_counts.items()))
    all_orientation_counts = Counter(
        {
            support: sum(
                int(profile["all_target_orientation_support_counts"].get(support, 0))
                for profile in profiles
            )
            for support in ("1", "2", "3", "4")
        }
    )
    all_orientation_counts = {
        support: count for support, count in sorted(all_orientation_counts.items()) if count
    }
    selected_three_layer_primes = [
        int(profile["prime"])
        for profile in profiles
        if int(profile["selected_orientation"]["minimum_target_layer_support"]) == 3
    ]
    if selected_counts != EXPECTED_SELECTED_SUPPORT_COUNTS:
        raise AssertionError("selected layer-support counts changed")
    if selected_three_layer_primes != EXPECTED_SELECTED_THREE_LAYER_PRIMES:
        raise AssertionError("selected three-layer prime list changed")
    if all_orientation_counts != EXPECTED_ALL_ORIENTATION_SUPPORT_COUNTS:
        raise AssertionError("all-orientation layer-support counts changed")
    return {
        "arithmetic": (
            "for every ordinary Type II p-1 tail miss through 31 million, "
            "completely enumerate its linear source states, construct the full "
            "coordinate-label collision layers, decide every induced K-square "
            "target spectrum, and choose the least-support target orientation"
        ),
        "scope_note": (
            "This is a finite 31-million reselection profile. It supports but "
            "does not prove a universal three-layer reselection theorem."
        ),
        "ordinary_tail_miss_input": tail_miss_input.name,
        "ordinary_tail_miss_input_sha256": file_sha256(tail_miss_input),
        "prime_limit": PRIME_LIMIT,
        "prime_count": len(primes),
        "prime_list_sha256": integer_list_sha256(primes),
        "selected_layer_support_counts": selected_counts,
        "selected_three_layer_primes": selected_three_layer_primes,
        "all_target_orientation_layer_support_counts": all_orientation_counts,
        "profiles": profiles,
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
                "prime_count": result["prime_count"],
                "selected_layer_support_counts": result[
                    "selected_layer_support_counts"
                ],
                "selected_three_layer_primes": result[
                    "selected_three_layer_primes"
                ],
                "all_target_orientation_layer_support_counts": result[
                    "all_target_orientation_layer_support_counts"
                ],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
