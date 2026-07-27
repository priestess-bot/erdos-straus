#!/usr/bin/env python3
"""Audit bounded-interface two-sided factor completions of shifted tails."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OPPOSITE_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_opposite_pair_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-two-sided-completion-300m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


opposite_profile = load_module("tail_shifted_two_sided_completion_opposite_profile", OPPOSITE_PROFILE)


def unit_or_prime_power_divisors(value: int, spf) -> list[int]:
    values = [1]
    for prime, exponent in opposite_profile.square_audit.factor_exponents((value,), spf).items():
        values.extend(prime**power for power in range(1, exponent + 1))
    return values


def two_sided_completion_witness(prime: int, shift: int, spf):
    """Search k=alpha*r*beta, N=gamma*z*delta with beta,delta prime-power interfaces."""
    base = (prime - shift) // 4
    candidate_k_count = 0
    block_choices_examined = 0
    for k in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(base, spf):
        q = 4 * k - 1
        if q % shift:
            continue
        candidate_k_count += 1
        source = (q * prime + shift) // (q + 1)
        if (q + 1) * source != q * prime + shift or source % shift:
            raise AssertionError("compatible source failed normalization")
        t = q // shift
        N = source // shift
        L = k * N
        for beta in unit_or_prime_power_divisors(k, spf):
            for delta in unit_or_prime_power_divisors(N, spf):
                b = beta * delta
                for r in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(k // beta, spf):
                    alpha = k // (beta * r)
                    for z in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(N // delta, spf):
                        block_choices_examined += 1
                        if (4 * r * z * b * b + 1) % t:
                            continue
                        gamma = N // (delta * z)
                        a = alpha * gamma
                        if L % a or L % b or L % (a * b) or (a + b) % t:
                            raise AssertionError("two-sided completion did not produce opposite divisors")
                        tail_factor = L * a // b
                        normalized_factor = min(tail_factor, L * L // tail_factor)
                        certified = next(
                            (
                                row
                                for row in opposite_profile.square_audit.tail_factors(prime, shift, k, spf)
                                if int(row["factor"]) == normalized_factor
                            ),
                            None,
                        )
                        if certified is None:
                            raise AssertionError("two-sided completion did not reconstruct a verified tail")
                        return {
                            "shift": shift,
                            "k": k,
                            "source_denominator": source,
                            "source_distance": prime - source,
                            "t": t,
                            "N": N,
                            "L": L,
                            "alpha": alpha,
                            "r": r,
                            "beta": beta,
                            "gamma": gamma,
                            "z": z,
                            "delta": delta,
                            "a": a,
                            "b": b,
                            "two_sided_square_root_quotient": (4 * r * z * b * b + 1) // t,
                            "tail_factor": normalized_factor,
                            "gap": certified["gap"],
                            "candidate_k_count": candidate_k_count,
                            "block_choices_examined": block_choices_examined,
                        }, candidate_k_count, block_choices_examined
    return None, candidate_k_count, block_choices_examined


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    records_in = [
        record
        for record in payload["records"]
        if not record["symmetric_box_subgroup_saturation_witness_count"]
        and not record["inverse_pairing_parity_witness_count"]
    ]
    if not records_in:
        raise ValueError("input has no minimal structural misses")
    primes = [int(record["prime"]) for record in records_in]
    spf = opposite_profile.square_audit.targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for record in records_in:
        prime = int(record["prime"])
        shift = int(record["minimal_offset"])
        witness, candidate_k_count, block_choices = two_sided_completion_witness(prime, shift, spf)
        records.append(
            {
                "prime": prime,
                "minimal_offset": shift,
                "two_sided_completion": witness,
                "candidate_k_count": candidate_k_count,
                "block_choices_examined": block_choices,
            }
        )
    misses = [record["prime"] for record in records if record["two_sided_completion"] is None]
    return {
        "arithmetic": (
            "complete compatible-k enumeration at each stored minimal offset; complete factor "
            "partitions k=alpha*r*beta and N=gamma*z*delta with beta and delta each a unit or "
            "one prime power; exact 4*r*z*(beta*delta)^2 == -1 (mod t) checks and verified tails"
        ),
        "scope_note": (
            "This is a bounded-interface factor-completion profile on the minimal structural-miss "
            "set. Failure does not rule out a larger interface or a later shifted ray."
        ),
        "prime_limit": payload["prime_limit"],
        "minimal_structural_miss_count": len(records),
        "two_sided_completion_hit_count": len(records) - len(misses),
        "two_sided_completion_miss_primes": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
