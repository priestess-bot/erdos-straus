#!/usr/bin/env python3
"""Audit nonmultiple scaled-source descents from p-1 on the H19 r boundary."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
CANDIDATE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_bounded_r_scaled_source_candidate_profile.py"
DESCENT_SCRIPT = ROOT / "reproductions" / "type_ii_h19_bounded_r_scaled_source_descent.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-p-minus-one-scaled-source-descent-1b-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


candidates = load_script("p_minus_one_scaled_source_candidates", CANDIDATE_SCRIPT)
descent = load_script("p_minus_one_scaled_source_descent", DESCENT_SCRIPT)


def standard_candidates(prime: int) -> list[tuple[int, int, int]]:
    """Return the b=1 p-minus-one candidates, i.e. the old c=1 source form."""
    source = prime - 1
    return [
        ((prime - shift) // 4, 1, int(shift))
        for shift in candidates.sympy.divisors(source)
        if shift % 4 == 1
    ]


def audit_primes(
    primes: list[int], include_standard: bool = False
) -> dict[str, object]:
    """Fully test b=2,4, and optionally b=1, candidates sourced at n=p-1."""
    records = []
    total_candidates = 0
    total_tail_divisor_tests = 0
    total_hits = 0

    for prime in primes:
        source = prime - 1
        source_candidates = {
            (candidate["a"], candidate["b"], candidate["shift"])
            for candidate in candidates.scaled_candidates(prime, source)
        }
        if include_standard:
            source_candidates.update(standard_candidates(prime))
        source_candidates = sorted(source_candidates)
        total_candidates += len(source_candidates)
        hits = 0
        first_witness = None
        for a, b, shift in source_candidates:
            witness, tested = descent.scaled_tail_witness(prime, source, a, b, shift)
            total_tail_divisor_tests += tested
            if witness is None:
                continue
            hits += 1
            first_witness = first_witness or {
                "a": a,
                "b": b,
                "shift": shift,
                "source_first_denominator": a * source // b,
                **witness,
            }
        total_hits += hits
        records.append(
            {
                "prime": prime,
                "source_denominator": source,
                "candidate_count": len(source_candidates),
                "hit_candidate_count": hits,
                "first_witness": first_witness,
            }
        )

    uncovered_primes = [
        record["prime"] for record in records if record["first_witness"] is None
    ]
    return {
        "residual_prime_count": len(records),
        "unique_scaled_source_candidate_count": total_candidates,
        "tail_divisor_test_count": total_tail_divisor_tests,
        "hit_candidate_count": total_hits,
        "covered_prime_count": len(records) - len(uncovered_primes),
        "uncovered_primes": uncovered_primes,
        "records": records,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Audit all stored r-capped boundary primes."""
    result = audit_primes([int(row["prime"]) for row in payload["records"]])
    return {
        "arithmetic": (
            "complete b=2,4 scaled-source candidate enumeration at n=p-1, "
            "forced-multiple square-tail enumeration, and exact rational plus "
            "Type I certificate verification"
        ),
        "scope_note": (
            "A finite audit on the stored H19 r-capped residual. It does not "
            "establish a universal p-minus-one scaled-source selector."
        ),
        "prime_limit": payload["prime_limit"],
        "input_r_cap": payload["r_cap"],
        **result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=OBSTRUCTION_INPUT)
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
