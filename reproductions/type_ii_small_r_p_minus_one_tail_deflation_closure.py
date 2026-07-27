#!/usr/bin/env python3
"""Close the five small-r/p-minus-one/even-source residuals by Type II deflation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVEN_SOURCE_INPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-even-source-boundary-100k-results.json"
CORE_INPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-core-boundary-100k-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-tail-deflation-closure-100k-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "small_r_p_minus_one_tail_deflation_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SHORT_CERTIFICATE.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def serialize_witness(witness) -> dict[str, object]:
    return {
        "source_denominator": witness.source_denominator,
        "gap": witness.gap,
        "source_solution": list(witness.source_solution),
        "target_solution": list(witness.target_solution),
        "certificate": {
            "type": witness.certificate.certificate_type,
            "gap": witness.certificate.gap,
            "x": witness.certificate.x,
            "divisor": witness.certificate.divisor,
            "y": witness.certificate.y,
            "z": witness.certificate.z,
        },
    }


def run_audit(
    even_source_payload: dict[str, object], core_payload: dict[str, object]
) -> dict[str, object]:
    """Deflate every full-even-source miss and compose the finite closure."""
    primes = [int(prime) for prime in even_source_payload["fully_even_source_unclosed_primes"]]
    spf = short_certificate.smallest_prime_factors(max(primes))
    records = []
    for prime in primes:
        witness = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if witness is None:
            records.append({"prime": prime, "witness": None})
            continue
        records.append({"prime": prime, "witness": serialize_witness(witness)})
    unclosed = [record["prime"] for record in records if record["witness"] is None]
    prior_joint = int(core_payload["joint_strict_lift_count"])
    core_count = int(core_payload["core_prime_count"])
    prior_residual = int(even_source_payload["joint_small_r_p_minus_one_residual_count"])
    if core_count != prior_joint + prior_residual:
        raise AssertionError("the source boundary did not partition the core range")
    return {
        "arithmetic": (
            "exact Type II residue certificates at divisor gaps of p-1, "
            "with both p-divisible tails deflated and source/target identities "
            "verified by the constructor"
        ),
        "scope_note": (
            "A finite four-branch closure on the stored p<=100000 core "
            "range. It does not prove a universal tail-deflation selector."
        ),
        "prime_limit": core_payload["prime_limit"],
        "core_prime_count": core_count,
        "prior_small_r_or_p_minus_one_count": prior_joint,
        "prior_small_r_or_p_minus_one_residual_count": prior_residual,
        "even_source_strict_lift_count": int(
            even_source_payload["even_source_strict_lift_count"]
        ),
        "tail_deflation_residual_count": len(primes),
        "tail_deflation_strict_lift_count": len(primes) - len(unclosed),
        "unclosed_primes": unclosed,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--even-source", type=Path, default=EVEN_SOURCE_INPUT)
    parser.add_argument("--core", type=Path, default=CORE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    even_source_payload = json.loads(args.even_source.read_text(encoding="utf-8"))
    core_payload = json.loads(args.core.read_text(encoding="utf-8"))
    result = run_audit(even_source_payload, core_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
