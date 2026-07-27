#!/usr/bin/env python3
"""Measure the gap cost of replacing a small Type I overflow by B=1.

The input is the finite 100M minimum-B profile. For each of its non-B=1
points, search the first external-source (B=1) target divisor through a
separate stated gap cap. This is a finite tradeoff audit, not a uniform gap
bound for external-source certificates.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
INPUT = ROOT / "reproductions" / "type-i-small-b-normal-form-100m-profile.json"
RESULTS = ROOT / "reproductions" / "type-i-overflow-gap-tradeoff-100m-m999-results.json"
DEFAULT_GAP_CAP = 999


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_i_overflow_gap_tradeoff_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def first_b_one_certificate(
    prime: int, spf: list[int], gap_cap: int
) -> dict[str, int] | None:
    """Find the least gap through the cap with a B=1 Type I certificate."""
    for gap in range(3, min(gap_cap, prime - 2) + 1, 4):
        x = (prime + gap) // 4
        target = (-pow(4, -1, gap)) % gap
        for target_divisor in short_certificate.positive_divisors_from_spf(x, spf):
            if target_divisor % gap != target:
                continue
            certificate = short_certificate.type_i_normal_form_certificate(
                prime, gap, x // target_divisor, 1
            )
            if certificate is None:
                raise AssertionError("B=1 target divisor did not reconstruct")
            return {
                "gap": gap,
                "target_divisor": target_divisor,
                "normal_a": x // target_divisor,
                "certificate_divisor": certificate.divisor,
            }
    return None


def run_profile(
    input_path: Path = INPUT, gap_cap: int = DEFAULT_GAP_CAP
) -> dict[str, object]:
    """Compare each finite-profile small-B witness with its first B=1 gap."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    records = source["non_b_one_witnesses"]
    if not records:
        raise ValueError("input profile has no non-B=1 witnesses")
    maximum_prime = max(record["prime"] for record in records)
    spf = short_certificate.smallest_prime_factors((maximum_prime + gap_cap) // 4 + 1)
    results: list[dict[str, int | None]] = []
    for record in records:
        b_one = first_b_one_certificate(record["prime"], spf, gap_cap)
        results.append(
            {
                "prime": record["prime"],
                "small_b": record["b"],
                "small_b_gap": record["gap"],
                "first_b_one_gap": None if b_one is None else b_one["gap"],
                "first_b_one_target_divisor": (
                    None if b_one is None else b_one["target_divisor"]
                ),
                "first_b_one_normal_a": None if b_one is None else b_one["normal_a"],
            }
        )
    misses = [record["prime"] for record in results if record["first_b_one_gap"] is None]
    return {
        "arithmetic": (
            "for every non-B=1 witness in the stated small-B profile, scan "
            "m=3 (mod 4) in increasing order; at each m enumerate every "
            "divisor e of x=(p+m)/4 and check e=-1/4 (mod m), then "
            "reconstruct the B=1 Type I certificate exactly"
        ),
        "scope_note": (
            "Finite comparison of the input exceptions. It does not establish "
            "a uniform B=1 gap bound or a general overflow-gap tradeoff."
        ),
        "input_profile": input_path.name,
        "input_prime_limit": source["prime_limit"],
        "gap_cap": gap_cap,
        "non_b_one_count": len(records),
        "b_one_recovered_count": len(records) - len(misses),
        "b_one_misses": misses,
        "maximum_first_b_one_gap": max(
            (record["first_b_one_gap"] for record in results if record["first_b_one_gap"] is not None),
            default=None,
        ),
        "records": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.input, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
