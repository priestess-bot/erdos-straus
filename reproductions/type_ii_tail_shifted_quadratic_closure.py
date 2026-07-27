#!/usr/bin/env python3
"""Close stored tail/quadratic misses by bounded shifted-quadratic descents."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-closure-100m-results.json"
DEFAULT_K_BOUND = 340_574


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("tail_shifted_quadratic_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("tail_shifted_quadratic_targeted_descent", TARGETED_DESCENT)


def shifted_witness(prime: int, spf, k_bound: int) -> tuple[object | None, int | None, int]:
    """Return the first verified shifted witness in the stated finite box."""
    candidates = 0
    for k in range(1, k_bound + 1):
        q = 4 * k - 1
        shift = prime % (4 * k)
        if shift == 0 or q % shift:
            continue
        candidates += 1
        witness = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
            prime, k, shift, spf
        )
        if witness is not None:
            return witness, shift, candidates
    return None, None, candidates


def serialize_witness(witness, shift: int, candidates: int) -> dict[str, object]:
    if not 2 <= witness.source_denominator < witness.prime:
        raise AssertionError("shifted external source is not strict")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in witness.source_solution), Fraction()
    ):
        raise AssertionError("shifted external source solution did not verify")
    if Fraction(4, witness.prime) != sum(
        (Fraction(1, value) for value in witness.target_solution), Fraction()
    ):
        raise AssertionError("shifted external target lift did not verify")
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "shift": shift,
        "factor": witness.factor,
        "gap": witness.certificate.gap,
        "candidate_pairs_examined": candidates,
    }


def run_audit(payload: dict[str, object], k_bound: int = DEFAULT_K_BOUND) -> dict[str, object]:
    """Audit a bounded shifted-quadratic branch after the complete zero-shift one."""
    if k_bound <= 0:
        raise ValueError("k_bound must be positive")
    primes = [int(prime) for prime in payload["quadratic_factor_misses"]]
    if not primes:
        raise ValueError("input profile has no quadratic-factor misses")
    spf = targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for prime in primes:
        witness, shift, candidates = shifted_witness(prime, spf, k_bound)
        records.append(
            {
                "prime": prime,
                "shifted_quadratic_descent": (
                    None if witness is None else serialize_witness(witness, shift, candidates)
                ),
                "candidate_pairs_examined": candidates,
            }
        )
    missing = [record["prime"] for record in records if record["shifted_quadratic_descent"] is None]
    tail_count = int(payload["core_prime_count"]) - int(payload["tail_deflation_miss_count"])
    return {
        "arithmetic": (
            "exact finite enumeration of compatible (k, shift) pairs, complete square-product "
            "divisor enumeration, and exact rational verification of every strict lift"
        ),
        "scope_note": (
            "A finite three-branch strict-descent closure in the stated k box. It does not "
            "prove that this box, or the branch order, works for every core prime."
        ),
        "prime_limit": payload["prime_limit"],
        "core_prime_count": payload["core_prime_count"],
        "two_tail_descent_count": tail_count,
        "quadratic_factor_descent_count_on_tail_misses": int(payload["quadratic_factor_descent_count"]),
        "zero_shift_quadratic_miss_count": len(records),
        "shifted_quadratic_k_bound": k_bound,
        "shifted_quadratic_descent_count": len(records) - len(missing),
        "shifted_quadratic_missing_primes": missing,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--k-bound", type=int, default=DEFAULT_K_BOUND)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.k_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
