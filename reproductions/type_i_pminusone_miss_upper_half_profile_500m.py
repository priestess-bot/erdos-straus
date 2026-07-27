#!/usr/bin/env python3
"""Normalize upper-half Type I states on the 500M p-minus-one residual.

Join the complete p-minus-one bridge boundary with the independently minimized
even-source profile.  Every joined record is rebuilt from its stored Type I
normal form, bridge factor, divisor pair, and the target/source Egyptian
fraction identities.  The result is a finite pressure profile, not a selector
outside the stated normal-form box.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P_MINUS_ONE = ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json"
MINIMUM_SOURCE = (
    ROOT / "reproductions" / "type-i-tail-reverse-even-source-min-source-distance-500m-results.json"
)
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bridge = load_module("pminusone_miss_upper_half_bridge", BRIDGE)


def histogram(values: list[int]) -> dict[str, int]:
    return {str(value): count for value, count in sorted(Counter(values).items())}


def rebuild_record(prime: int, raw_witness: dict[str, object]) -> dict[str, object]:
    """Rebuild one shortest non-p-minus-one upper-half bridge exactly."""
    distance = int(raw_witness["source_distance"])
    gap = int(raw_witness["gap"])
    A, B, C = (int(value) for value in raw_witness["normal_form"])
    E = int(raw_witness["E"])
    raw_lift = raw_witness["reverse_two_tail_lift"]
    if not isinstance(raw_lift, dict):
        raise AssertionError("minimum source witness is missing its reverse lift")
    source = int(raw_lift["source_denominator"])
    source_term = int(raw_lift["source_term"])
    bridge_divisor = int(raw_lift["bridge_divisor"])

    R = (4 * B * B * C + 1) // gap
    H = A * R - B
    K = B * C * H
    L = 2 * K
    certificate = bridge.short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
    if certificate is None:
        raise AssertionError("stored Type I normal form did not reconstruct")
    if (
        gap * R != 4 * B * B * C + 1
        or 4 * K != prime * R + 1
        or R % 4 != 3
        or source != prime - distance
        or bridge_divisor != prime * prime * E
        or (4 * K * K) % E
        or E % R != 1
        or E % 2
        or E > 4 * K - 2 * R
        or (4 * K - E) % R
        or source != (4 * K - E) // R
        or source % 2
    ):
        raise AssertionError("stored minimum source bridge did not reconstruct")

    divisor_gcd = math.gcd(E, L)
    a, b = E // divisor_gcd, L // divisor_gcd
    if (
        math.gcd(a, b) != 1
        or L % a
        or L % b
        or E != L * a // b
        or (a - 2 * b) % R
        or a >= b
        or source < (prime + 1) // 2
    ):
        raise AssertionError("minimum source is not an upper-half small-side bridge")

    target_solution = (certificate.x, certificate.y, certificate.z)
    source_solution = (source_term, certificate.x, certificate.y)
    if Fraction(4, prime) != sum(
        (Fraction(1, denominator) for denominator in target_solution), Fraction()
    ):
        raise AssertionError("target Egyptian-fraction identity failed")
    if Fraction(4, source) != sum(
        (Fraction(1, denominator) for denominator in source_solution), Fraction()
    ):
        raise AssertionError("source Egyptian-fraction identity failed")

    return {
        "prime": prime,
        "source_distance": distance,
        "gap": gap,
        "normal_form": [A, B, C],
        "R": R,
        "K": K,
        "E": E,
        "a": a,
        "b": b,
        "source_denominator": source,
    }


def run_profile(pminusone: dict[str, object], minimum_source: dict[str, object]) -> dict[str, object]:
    """Join every p-minus-one miss to its minimized upper-half source state."""
    misses = [int(prime) for prime in pminusone["p_minus_one_misses"]]
    source_records = minimum_source["records"]
    if not isinstance(source_records, list):
        raise AssertionError("minimum source records must be a list")
    source_by_prime: dict[int, dict[str, object]] = {}
    for raw_record in source_records:
        if not isinstance(raw_record, dict):
            raise AssertionError("minimum source record must be an object")
        prime = int(raw_record["prime"])
        witness = raw_record["minimum_source_witness"]
        if not isinstance(witness, dict):
            raise AssertionError("minimum source record must contain a witness")
        if prime in source_by_prime:
            raise AssertionError("minimum source profile repeated a prime")
        source_by_prime[prime] = witness

    records = []
    for prime in misses:
        witness = source_by_prime.get(prime)
        if witness is None:
            raise AssertionError("p-minus-one residual has no minimum-source witness")
        record = rebuild_record(prime, witness)
        if record["source_distance"] <= 1:
            raise AssertionError("p-minus-one residual unexpectedly retained p-minus-one source")
        records.append(record)
    if len(records) != len(misses) or {record["prime"] for record in records} != set(misses):
        raise AssertionError("p-minus-one residual join did not preserve the exact prime set")

    distances = [int(record["source_distance"]) for record in records]
    factors = [int(record["E"]) for record in records]
    b_values = [int(record["normal_form"][1]) for record in records]
    gaps = [int(record["gap"]) for record in records]
    max_distance_record = max(records, key=lambda record: int(record["source_distance"]))
    max_factor_record = max(records, key=lambda record: int(record["E"]))
    return {
        "arithmetic": (
            "join the complete 500M p-minus-one Type I bridge misses to the independently minimized "
            "even-source witnesses; rebuild each normal form, E|4K^2 bridge, reduced small-side divisor "
            "pair, upper-half source, and both Egyptian-fraction identities exactly"
        ),
        "scope_note": (
            "A complete finite profile only for the 185 p-minus-one misses within the shared p<=500M, "
            "m<=215 Type I normal-form box. It neither selects a bridge outside this box nor proves the "
            "global upper-half mixed terminal selector."
        ),
        "pminusone_input_artifact": P_MINUS_ONE.name,
        "minimum_source_input_artifact": MINIMUM_SOURCE.name,
        "prime_limit": int(pminusone["prime_limit"]),
        "gap_cap": int(pminusone["gap_cap"]),
        "p_minus_one_miss_count": len(misses),
        "joined_minimum_source_count": len(records),
        "upper_half_small_side_count": len(records),
        "upper_half_failures": [],
        "minimum_source_distance": min(distances),
        "maximum_source_distance": max(distances),
        "source_distance_histogram": histogram(distances),
        "gap_histogram": histogram(gaps),
        "normal_form_B_histogram": histogram(b_values),
        "distinct_bridge_factor_count": len(set(factors)),
        "minimum_bridge_factor": min(factors),
        "maximum_bridge_factor": max(factors),
        "maximum_source_distance_record": max_distance_record,
        "maximum_bridge_factor_record": max_factor_record,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pminusone", type=Path, default=P_MINUS_ONE)
    parser.add_argument("--minimum-source", type=Path, default=MINIMUM_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.pminusone.read_text(encoding="utf-8")),
        json.loads(args.minimum_source.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
