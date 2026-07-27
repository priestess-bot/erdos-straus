#!/usr/bin/env python3
"""Profile the least residue offset in shifted quadratic external descents."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGETED_DESCENT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-100m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-100m-results.json"
DEFAULT_OFFSET_BOUND = 7_161


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("tail_shifted_offset_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("tail_shifted_offset_targeted_descent", TARGETED_DESCENT)


def first_offset_witness(prime: int, spf, offset_bound: int) -> tuple[object | None, int | None, int]:
    """Enumerate every compatible k for each offset s in increasing order.

    Since p == 1 (mod 4), a compatible positive offset has s == 1 (mod 4).
    For fixed s, p = 4*k*d + s, hence all possible k are exactly divisors of
    (p-s)/4; this avoids treating a k cutoff as a structural parameter.
    """
    candidate_pairs = 0
    for shift in range(1, min(offset_bound, prime - 1) + 1, 4):
        base = (prime - shift) // 4
        for k in short_certificate.positive_divisors_from_spf(base, spf):
            if (4 * k - 1) % shift:
                continue
            candidate_pairs += 1
            witness = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, shift, spf
            )
            if witness is not None:
                return witness, shift, candidate_pairs
    return None, None, candidate_pairs


def serialize_witness(witness, shift: int, candidate_pairs: int) -> dict[str, int]:
    if not 2 <= witness.source_denominator < witness.prime:
        raise AssertionError("shifted source must be strictly smaller")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in witness.source_solution), Fraction()
    ):
        raise AssertionError("source solution did not verify")
    if Fraction(4, witness.prime) != sum(
        (Fraction(1, value) for value in witness.target_solution), Fraction()
    ):
        raise AssertionError("target lift did not verify")
    distance = witness.prime - witness.source_denominator
    if witness.q % shift:
        raise AssertionError("reported shift does not divide q")
    t = witness.q // shift
    if (
        witness.prime - distance != shift * (distance * t + 1)
        or witness.k != (shift * t + 1) // 4
        or shift * t % 4 != 3
    ):
        raise AssertionError("source-distance parametrization did not reconstruct")
    return {
        "source_denominator": witness.source_denominator,
        "source_distance": distance,
        "k": witness.k,
        "q": witness.q,
        "shift": shift,
        "t": t,
        "factor": witness.factor,
        "gap": witness.certificate.gap,
        "candidate_pairs_examined": candidate_pairs,
    }


def run_audit(payload: dict[str, object], offset_bound: int = DEFAULT_OFFSET_BOUND) -> dict[str, object]:
    """Run the full fixed-offset divisor parametrization on each pressure point."""
    if offset_bound <= 0:
        raise ValueError("offset_bound must be positive")
    primes = [int(prime) for prime in payload["quadratic_factor_misses"]]
    if not primes:
        raise ValueError("input profile has no zero-offset quadratic misses")
    spf = targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for prime in primes:
        witness, shift, candidates = first_offset_witness(prime, spf, offset_bound)
        records.append(
            {
                "prime": prime,
                "offset_descent": (
                    None if witness is None else serialize_witness(witness, shift, candidates)
                ),
                "candidate_pairs_examined": candidates,
            }
        )
    missing = [record["prime"] for record in records if record["offset_descent"] is None]
    tail_count = int(payload["core_prime_count"]) - int(payload["tail_deflation_miss_count"])
    return {
        "arithmetic": (
            "exact enumeration of every compatible divisor k of (p-s)/4 for each stated "
            "residue offset, complete square-product tail enumeration, and rational checks"
        ),
        "scope_note": (
            "A finite offset-selector profile, not a proof of a uniform offset bound or "
            "a universal descent theorem."
        ),
        "prime_limit": payload["prime_limit"],
        "core_prime_count": payload["core_prime_count"],
        "two_tail_descent_count": tail_count,
        "zero_offset_quadratic_descent_count_on_tail_misses": int(payload["quadratic_factor_descent_count"]),
        "zero_offset_quadratic_miss_count": len(records),
        "offset_bound": offset_bound,
        "offset_descent_count": len(records) - len(missing),
        "offset_missing_primes": missing,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--offset-bound", type=int, default=DEFAULT_OFFSET_BOUND)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.offset_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
