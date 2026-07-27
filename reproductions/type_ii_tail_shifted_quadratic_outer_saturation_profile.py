#!/usr/bin/env python3
"""Seek later shifted rays whose symmetric divisor box fills its subgroup."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OPPOSITE_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_opposite_pair_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-outer-saturation-profile-200m-results.json"
DEFAULT_OFFSET_BOUND = 202_521


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


opposite_profile = load_module("tail_shifted_outer_saturation_opposite_profile", OPPOSITE_PROFILE)


def first_later_saturation(prime: int, minimal_offset: int, spf, offset_bound: int):
    """Find the first later offset with an exact subgroup-saturating tail box."""
    candidate_pairs = 0
    for shift in range(minimal_offset + 4, min(offset_bound, prime - 1) + 1, 4):
        base = (prime - shift) // 4
        for k in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(base, spf):
            q = 4 * k - 1
            if q % shift:
                continue
            candidate_pairs += 1
            source = (q * prime + shift) // (q + 1)
            if (q + 1) * source != q * prime + shift or source % shift:
                raise AssertionError("compatible shifted source failed normalization")
            t = q // shift
            L = k * (source // shift)
            L_exponents = opposite_profile.square_audit.factor_exponents(
                (k, source // shift), spf
            )
            density = opposite_profile.ordinary_divisor_residue_profile(L_exponents, t, spf)
            if not density["symmetric_box_fills_generated_subgroup"]:
                continue
            witness = opposite_profile.square_audit.short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, shift, spf
            )
            if witness is None:
                raise AssertionError("subgroup-saturating ray did not yield a verified tail")
            return {
                "shift": shift,
                "k": k,
                "source_denominator": witness.source_denominator,
                "source_distance": prime - witness.source_denominator,
                "t": t,
                "L": L,
                "factor": witness.factor,
                "gap": witness.certificate.gap,
                "candidate_pairs_examined": candidate_pairs,
                **density,
            }, candidate_pairs
    return None, candidate_pairs


def first_later_structural_witness(prime: int, minimal_offset: int, spf, offset_bound: int):
    """Find a later ray certified by saturation or inverse-pairing parity."""
    candidate_pairs = 0
    for shift in range(minimal_offset + 4, min(offset_bound, prime - 1) + 1, 4):
        base = (prime - shift) // 4
        for k in opposite_profile.square_audit.short_certificate.positive_divisors_from_spf(base, spf):
            q = 4 * k - 1
            if q % shift:
                continue
            candidate_pairs += 1
            source = (q * prime + shift) // (q + 1)
            if (q + 1) * source != q * prime + shift or source % shift:
                raise AssertionError("compatible shifted source failed normalization")
            t = q // shift
            L = k * (source // shift)
            L_exponents = opposite_profile.square_audit.factor_exponents(
                (k, source // shift), spf
            )
            density = opposite_profile.ordinary_divisor_residue_profile(L_exponents, t, spf)
            if density["symmetric_box_fills_generated_subgroup"]:
                mechanism = "symmetric-box-subgroup-saturation"
            elif density["inverse_pairing_parity_forces_target"]:
                mechanism = "inverse-pairing-parity"
            else:
                continue
            witness = opposite_profile.square_audit.short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, shift, spf
            )
            if witness is None:
                raise AssertionError("structurally certified ray did not yield a verified tail")
            return {
                "mechanism": mechanism,
                "shift": shift,
                "k": k,
                "source_denominator": witness.source_denominator,
                "source_distance": prime - witness.source_denominator,
                "t": t,
                "L": L,
                "factor": witness.factor,
                "gap": witness.certificate.gap,
                "candidate_pairs_examined": candidate_pairs,
                **density,
            }, candidate_pairs
    return None, candidate_pairs


def run_audit(payload: dict[str, object], offset_bound: int = DEFAULT_OFFSET_BOUND) -> dict[str, object]:
    if offset_bound <= 0:
        raise ValueError("offset bound must be positive")
    records_in = [
        record
        for record in payload["records"]
        if not record["symmetric_box_subgroup_saturation_witness_count"]
    ]
    if not records_in:
        raise ValueError("input has no symmetric-saturation misses")
    primes = [int(record["prime"]) for record in records_in]
    spf = opposite_profile.square_audit.targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for record in records_in:
        prime = int(record["prime"])
        minimal_offset = int(record["minimal_offset"])
        witness, candidates = first_later_saturation(prime, minimal_offset, spf, offset_bound)
        records.append(
            {
                "prime": prime,
                "minimal_offset_without_saturation": minimal_offset,
                "later_saturation": witness,
                "candidate_pairs_examined_after_minimal_offset": candidates,
            }
        )
    misses = [record["prime"] for record in records if record["later_saturation"] is None]
    return {
        "arithmetic": (
            "for every stored minimal-offset symmetric-box saturation miss, exact enumeration "
            "of every compatible k at each later shift through the stated bound; each proposed "
            "subgroup saturation is followed by construction and verification of the tail descent"
        ),
        "scope_note": (
            "This tests only offsets strictly larger than the already-audited minimal offset, "
            "within a finite bound. A miss is not a failure of shifted quadratic descent."
        ),
        "prime_limit": payload["prime_limit"],
        "input_symmetric_saturation_miss_count": len(records),
        "offset_bound": offset_bound,
        "later_saturation_count": len(records) - len(misses),
        "later_saturation_miss_primes": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--offset-bound", type=int, default=DEFAULT_OFFSET_BOUND)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.offset_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
