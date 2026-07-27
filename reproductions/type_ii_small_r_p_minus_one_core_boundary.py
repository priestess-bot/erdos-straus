#!/usr/bin/env python3
"""Find core primes missed by both r<=103 and p-minus-one strict lifts."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
SMALL_R_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"
DEFAULT_LIMIT = 100_000
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-core-boundary-100k-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_r = load_script("small_r_p_minus_one_core_boundary", SMALL_R_SCRIPT)
p_minus_one = load_script("p_minus_one_core_boundary", P_MINUS_ONE_SCRIPT)


def has_small_r_strict_lift(prime: int, spf: list[int]) -> bool:
    """Require a full source/target witness, not merely a tail-residue prehit."""
    for r in range(7, 104, 8):
        rays = small_r.compatible_rays(prime, r)
        if not rays or not small_r.tail_hit_count(prime, r):
            continue
        for ray in rays:
            witness = p_minus_one.descent.short_certificate.even_source_distance_descent_witness(
                prime, int(ray["distance"]), spf
            )
            if witness is not None:
                return True
    return False


def run_audit(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Audit all core primes and retain the exact joint-mechanism boundary."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    spf = p_minus_one.descent.short_certificate.smallest_prime_factors(limit)
    core_primes = [int(prime) for prime in sympy.primerange(2, limit + 1) if prime % 24 == 1]
    r_misses = [
        prime for prime in core_primes if not has_small_r_strict_lift(prime, spf)
    ]
    records = []
    candidate_count = 0
    tail_divisor_test_count = 0
    hit_candidate_count = 0
    for prime in r_misses:
        result = p_minus_one.audit_primes([prime])
        record = result["records"][0]
        records.append(record)
        candidate_count += int(result["unique_scaled_source_candidate_count"])
        tail_divisor_test_count += int(result["tail_divisor_test_count"])
        hit_candidate_count += int(result["hit_candidate_count"])
    unclosed = [
        int(record["prime"]) for record in records if record["first_witness"] is None
    ]
    return {
        "arithmetic": (
            "all p=1 mod 24 primes; full certified r<=103 even-source lifts; "
            "then complete b=2,4 p-minus-one candidate and square-tail "
            "enumeration with exact rational and Type I verification"
        ),
        "scope_note": (
            "A finite mechanism boundary. An unclosed prime is not a "
            "counterexample to Erdős-Straus and may have other certificates."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes),
        "small_r_strict_lift_count": len(core_primes) - len(r_misses),
        "small_r_residual_count": len(r_misses),
        "p_minus_one_scaled_source_candidate_count": candidate_count,
        "p_minus_one_tail_divisor_test_count": tail_divisor_test_count,
        "p_minus_one_hit_candidate_count": hit_candidate_count,
        "joint_strict_lift_count": len(core_primes) - len(unclosed),
        "joint_unclosed_primes": unclosed,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
