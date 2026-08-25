#!/usr/bin/env python3
"""Audit the generous q-adic modulus capacity for the full Fourier spectrum."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOURIER_RESULT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
FULL_SPECTRUM = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-full-spectrum-qadic-modulus-capacity-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_SPECTRUM_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def load_input() -> tuple[list[dict[str, object]], dict[int, list[dict[str, int]]]]:
    if sha256(FOURIER_RESULT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the full Fourier result changed")
    if sha256(FULL_SPECTRUM) != EXPECTED_SPECTRUM_SHA256:
        raise AssertionError("the full spectrum result changed")
    fourier = json.loads(FOURIER_RESULT.read_text(encoding="utf-8"))
    spectrum = json.loads(FULL_SPECTRUM.read_text(encoding="utf-8"))
    records = [
        dict(record)
        for record in fourier["records"]
        if record["status"] == "bounded_fourier_certificate"
    ]
    all_states: dict[int, list[dict[str, int]]] = {}
    for profile in spectrum["profiles"]:
        prime = int(profile["prime"])
        all_states[prime] = [
            {"R": int(record["R"]), "K": int(record["K"])}
            for record in profile["records"]
        ]
    return records, all_states


def run() -> dict[str, object]:
    records, all_states = load_input()
    demand: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for record in records:
        factorization = {
            int(prime): int(exponent) for prime, exponent in record["factorization"]
        }
        for q in record["active_primes"]:
            q = int(q)
            exponent = factorization[q]
            # The high carrier has at least half of the total K exponent. This
            # deliberately gives the capacity audit more room than an exact
            # color/height assignment.
            required_height = (exponent + (2 if q == 2 else 0) + 1) // 2
            demand[(int(record["prime"]), q)].append(
                {
                    "R": int(record["R"]),
                    "required_height": required_height,
                    "total_exponent": exponent,
                }
            )

    groups = []
    for (prime, q), entries in sorted(demand.items()):
        states = all_states[prime]
        capacity = sum(valuation(state["K"], q) for state in states)
        required = sum(entry["required_height"] for entry in entries)
        R_values = [state["R"] for state in states]
        interval_width = (max(R_values) - min(R_values)) / 4
        max_exponent = max(entry["total_exponent"] for entry in entries)
        coarse_capacity = interval_width / (q - 1) + max_exponent
        groups.append(
            {
                "prime": prime,
                "q": q,
                "occurrence_count": len(entries),
                "required_height": required,
                "finite_R_capacity": capacity,
                "finite_R_ratio": required / capacity if capacity else None,
                "coarse_modulus_capacity": coarse_capacity,
                "coarse_modulus_ratio": required / coarse_capacity
                if coarse_capacity
                else None,
                "max_total_exponent": max_exponent,
            }
        )

    finite_ratios = [
        group["finite_R_ratio"]
        for group in groups
        if group["finite_R_ratio"] is not None
    ]
    coarse_ratios = [group["coarse_modulus_ratio"] for group in groups]
    finite_overloads = [
        group for group in groups if group["finite_R_ratio"] is not None and group["finite_R_ratio"] > 1
    ]
    coarse_overloads = [group for group in groups if group["coarse_modulus_ratio"] > 1]
    return {
        "arithmetic": "Group every full-spectrum bounded Fourier certificate by (p,q), demand ceil((v_q(K)+2*1_{q=2})/2), and compare with the generous sum of v_q(K) over every complete linear R state and with the coarse modulus-difference capacity.",
        "scope_note": "Finite negative boundary only. The capacity is intentionally generous: it ignores colors, phase quality, and joint directions. No overload is not evidence of a selector theorem.",
        "fourier_input": FOURIER_RESULT.name,
        "fourier_input_sha256": sha256(FOURIER_RESULT),
        "spectrum_input": FULL_SPECTRUM.name,
        "spectrum_input_sha256": sha256(FULL_SPECTRUM),
        "certificate_state_count": len(records),
        "group_count": len(groups),
        "active_occurrence_count": sum(group["occurrence_count"] for group in groups),
        "finite_R_overload_count": len(finite_overloads),
        "coarse_modulus_overload_count": len(coarse_overloads),
        "maximum_finite_R_ratio": max(finite_ratios) if finite_ratios else None,
        "maximum_coarse_modulus_ratio": max(coarse_ratios) if coarse_ratios else None,
        "finite_R_saturation_count": sum(ratio == 1 for ratio in finite_ratios),
        "top_finite_R_groups": sorted(
            groups,
            key=lambda group: (
                group["finite_R_ratio"] is not None,
                group["finite_R_ratio"] or -1,
            ),
            reverse=True,
        )[:50],
        "top_coarse_modulus_groups": sorted(
            groups,
            key=lambda group: group["coarse_modulus_ratio"],
            reverse=True,
        )[:50],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run()
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "certificate_state_count",
                    "group_count",
                    "active_occurrence_count",
                    "finite_R_overload_count",
                    "coarse_modulus_overload_count",
                    "maximum_finite_R_ratio",
                    "maximum_coarse_modulus_ratio",
                    "finite_R_saturation_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
