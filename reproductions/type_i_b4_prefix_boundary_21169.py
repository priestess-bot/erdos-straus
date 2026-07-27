#!/usr/bin/env python3
"""Find the first core-prime failure of the B<=4 maximum-tail even-source box."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
DEFAULT_LIMIT = 21_169
DEFAULT_B_CAP = 4
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b4-prefix-boundary-21169-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("b4_prefix_boundary_direct", DIRECT)


def first_bounded_even_lift(prime: int, b_cap: int) -> dict[str, object] | None:
    """Return the first natural-gap strict even reverse edge with B at most ``b_cap``."""
    for gap in range(3, prime - 1, 4):
        for entry in direct.support_min.landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B > b_cap:
                continue
            _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(
                prime, gap, A, B, C
            )
            for lift in lifts:
                if int(lift["source_denominator"]) % 2:
                    continue
                return {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "source_denominator": int(lift["source_denominator"]),
                    "source_term": int(lift["source_term"]),
                    "bridge_factor": int(lift["bridge_divisor"]) // (prime * prime),
                }
    return None


def run_audit(limit: int = DEFAULT_LIMIT, b_cap: int = DEFAULT_B_CAP) -> dict[str, object]:
    """Audit every core prime through ``limit`` against the complete B-bounded box."""
    if limit < 73 or limit % 24 != 1:
        raise ValueError("limit must be at least 73 and congruent to 1 modulo 24")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")
    primes = [
        prime
        for prime in direct.support_min.landscape.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    records = []
    misses = []
    for prime in primes:
        witness = first_bounded_even_lift(prime, b_cap)
        record = {"prime": prime, "witness": witness}
        records.append(record)
        if witness is None:
            misses.append(prime)
    return {
        "arithmetic": (
            "for every core prime p through the stated limit, enumerate every natural Type I gap and every "
            "Type I normal form with B<=b_cap, then enumerate every p-divisible maximum-tail bridge E|4K^2 "
            "and retain exact strict even sources"
        ),
        "scope_note": (
            "A complete finite prefix audit. A miss excludes only this B-bounded maximum-tail, two-term-preserving "
            "Type I reverse family, not other B values, coordinates, or Type II descent."
        ),
        "prime_limit": limit,
        "b_cap": b_cap,
        "core_prime_count": len(primes),
        "captured_count": len(primes) - len(misses),
        "misses": misses,
        "first_miss": None if not misses else misses[0],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
