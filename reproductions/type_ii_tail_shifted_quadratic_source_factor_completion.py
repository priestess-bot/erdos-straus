#!/usr/bin/env python3
"""Audit the u^2*v + 4 source-factor completion for shifted quadratic tails."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OPPOSITE_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_opposite_pair_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-source-factor-completion-200m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


opposite_profile = load_module("tail_shifted_source_factor_completion_opposite_profile", OPPOSITE_PROFILE)


def source_factor_completion_witness(prime: int, shift: int, spf):
    """Search all compatible k and N=u*v*w for u^2*v == -4 (mod t).

    With q=s*t, N=d*t+1 and L=k*N, one has k == 1/4 and N == 1 (mod t).
    Thus u^2*v == -4 makes a=u*k and b=w=N/(u*v) opposite ordinary divisors.
    """
    base = (prime - shift) // 4
    candidate_k_count = 0
    factor_partitions_examined = 0
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
        for u in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(N, spf):
            for v in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(N // u, spf):
                factor_partitions_examined += 1
                if (u * u * v + 4) % t:
                    continue
                w = N // (u * v)
                a = u * k
                b = w
                if L % a or L % b or (a + b) % t:
                    raise AssertionError("source-factor completion did not make opposite divisors")
                tail_factor = L * a // b
                complement = L * L // tail_factor
                normalized_factor = min(tail_factor, complement)
                rows = opposite_profile.square_audit.tail_factors(prime, shift, k, spf)
                certified = next(
                    (row for row in rows if int(row["factor"]) == normalized_factor), None
                )
                if certified is None:
                    raise AssertionError("source-factor completion did not reconstruct a verified tail")
                return {
                    "shift": shift,
                    "k": k,
                    "source_denominator": source,
                    "source_distance": prime - source,
                    "t": t,
                    "N": N,
                    "L": L,
                    "u": u,
                    "v": v,
                    "w": w,
                    "a": a,
                    "b": b,
                    "u_squared_v_plus_four_over_t": (u * u * v + 4) // t,
                    "tail_factor": normalized_factor,
                    "gap": certified["gap"],
                    "candidate_k_count": candidate_k_count,
                    "factor_partitions_examined": factor_partitions_examined,
                }, candidate_k_count, factor_partitions_examined
    return None, candidate_k_count, factor_partitions_examined


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
        witness = source_factor_completion_witness(prime, shift, spf)
        if witness is None:
            value, candidate_k_count, partition_count = None, 0, 0
        else:
            value, candidate_k_count, partition_count = witness
        records.append(
            {
                "prime": prime,
                "minimal_offset": shift,
                "source_factor_completion": value,
                "candidate_k_count": candidate_k_count,
                "factor_partitions_examined": partition_count,
            }
        )
    misses = [record["prime"] for record in records if record["source_factor_completion"] is None]
    return {
        "arithmetic": (
            "complete compatible-k enumeration at each stored minimal offset, complete ordered "
            "factor partition N=u*v*w enumeration, the exact u^2*v == -4 (mod t) check, and "
            "independent verified-tail reconstruction"
        ),
        "scope_note": (
            "This is an exact selector profile only for the minimal structural-miss set. "
            "Failure does not rule out a different factor completion or a later shifted ray."
        ),
        "prime_limit": payload["prime_limit"],
        "minimal_structural_miss_count": len(records),
        "source_factor_completion_hit_count": len(records) - len(misses),
        "source_factor_completion_miss_primes": misses,
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
