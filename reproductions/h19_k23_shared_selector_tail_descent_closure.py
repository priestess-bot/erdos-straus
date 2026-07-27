#!/usr/bin/env python3
"""Close an H19-k23 shared-selector artifact by two-tail descent.

For a shared Type II record, its own least gap gives an ordinary two-tail
descent exactly when gap+1 divides p-1.  Only the incompatible rows need an
exhaustive p-1 indexed alternative-gap scan.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-audit-16384.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-16384.json"
ALTERNATIVE_TAIL = ROOT / "reproductions" / "type_ii_collision_alternative_tail_descent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


alternative_tail = load_module("h19_k23_full_tail_alternative", ALTERNATIVE_TAIL)


def direct_tail_witness(prime: int, shared_witness: dict[str, object]) -> dict[str, object] | None:
    """Verify the shared record itself as an ordinary two-tail descent when legal."""
    gap = int(shared_witness["gap"])
    if (prime - 1) % (gap + 1):
        return None
    x = int(shared_witness["x"])
    divisor = int(shared_witness["type_ii_divisor"])
    if 4 * x != prime + gap or not 1 <= divisor <= x:
        raise AssertionError("stored shared witness has invalid Type II data")
    if x * x % divisor or divisor % gap != (-x) % gap:
        raise AssertionError("stored shared witness fails the Type II divisor criterion")
    y_numerator = prime * (x + divisor)
    z_numerator = prime * (x + x * x // divisor)
    if y_numerator % gap or z_numerator % gap:
        raise AssertionError("stored shared witness has nonintegral Type II tails")
    y, z = y_numerator // gap, z_numerator // gap
    source_denominator = (prime + gap) // (gap + 1)
    source_solution = (x, y // prime, z // prime)
    if y % prime or z % prime or not 2 <= source_denominator < prime:
        raise AssertionError("shared witness did not yield a strict two-tail source")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in (x, y, z)), Fraction()):
        raise AssertionError("stored shared witness failed its target identity")
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("stored shared witness failed its source identity")
    return {
        "gap": gap,
        "divisor": divisor,
        "source_denominator": source_denominator,
    }


def compact_alternative_witness(witness: dict[str, object]) -> dict[str, int]:
    certificate = witness["certificate"]
    return {
        "gap": int(witness["gap"]),
        "divisor": int(certificate["divisor"]),
        "source_denominator": int(witness["source_denominator"]),
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Verify a direct-or-alternative ordinary two-tail exit for every record."""
    records = []
    route_counts: Counter[str] = Counter()
    alternative_gap_count = 0
    for record in payload["records"]:
        prime = int(record["prime"])
        shared_witness = record["first_witness"]
        direct = direct_tail_witness(prime, shared_witness)
        if direct is not None:
            route = "shared-gap"
            witness = direct
            candidate_count = 0
        else:
            alternative, candidate_count = alternative_tail.first_alternative_tail_descent(prime)
            route = "alternative-p-minus-one-gap"
            witness = (
                compact_alternative_witness(alternative)
                if alternative is not None
                else None
            )
            alternative_gap_count += candidate_count
        route_counts[route] += 1
        records.append(
            {
                "prime": prime,
                "shared_selector_gap": int(shared_witness["gap"]),
                "route": route,
                "candidate_tail_gap_count": candidate_count,
                "tail_witness": witness,
            }
        )
    misses = [record["prime"] for record in records if record["tail_witness"] is None]
    return {
        "arithmetic": (
            "exact reconstruction of every compatible stored Type II certificate "
            "and source identity; for each incompatible row, complete p-1 factorization, "
            "4-divisible divisor-gap enumeration, Type II divisor checks, and exact "
            "Fraction verification"
        ),
        "scope_note": (
            "A complete finite closure of the supplied H19-k23 artifact. "
            "It does not imply ordinary two-tail descent for every core prime."
        ),
        "input_parameter_limit_exclusive": payload["parameter_limit_exclusive"],
        "input_prime_count": payload["prime_count"],
        "record_count": len(records),
        "ordinary_tail_descent_count": len(records) - len(misses),
        "ordinary_tail_descent_misses": misses,
        "route_counts": dict(sorted(route_counts.items())),
        "alternative_candidate_gap_count": alternative_gap_count,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in result if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
