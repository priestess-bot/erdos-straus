#!/usr/bin/env python3
"""Cross a fixed Type II canonical fan with strict external-source descents.

For every core prime missed by the first H canonical Type II rays, this audit
tries three nested strict-lift families:

* the original adaptive external-source family;
* its mixed-factor extension;
* the complete quadratic-factor two-tail family.

All three constructors explicitly verify a source solution, a target solution,
and the resulting Type I certificate.  This remains a finite audit: neither
the H-ray bound nor any descent selector is asserted to be uniform.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT / "reproductions" / "type-ii-h19-quadratic-descent-closure-10m-results.json"
)
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_module("h19_closure_canonical", CANONICAL_SCRIPT)
short_certificate = load_module("h19_closure_short_certificate", SHORT_CERTIFICATE_SCRIPT)


def serialize_witness(witness) -> dict[str, object] | None:
    """Return the data needed to independently inspect a verified strict lift."""
    if witness is None:
        return None
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
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


def run_audit(limit: int = 10_000_000, base_shift_bound: int = 19) -> dict[str, object]:
    """Return the exact finite H-ray/descent closure classification."""
    if limit < 73 or base_shift_bound < 1:
        raise ValueError("require limit >= 73 and a positive base shift bound")

    pairs = tuple(
        canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    max_shift = max(a * a * c for a, c in pairs)
    ray_spf = short_certificate.smallest_prime_factors(limit + 4 * max_shift)
    descent_spf = short_certificate.smallest_prime_factors(limit)
    core_primes = [
        prime
        for prime in short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]

    records: list[dict[str, object]] = []
    captured_count = 0
    for prime in core_primes:
        first_certificate = next(
            (
                witness
                for pair in pairs
                if (
                    witness := canonical.witness_for_pair(prime, pair, ray_spf)
                )
                is not None
            ),
            None,
        )
        if first_certificate is not None:
            captured_count += 1
            continue

        adaptive = short_certificate.external_source_descent_witness(
            prime, descent_spf
        )
        mixed = short_certificate.mixed_factor_external_source_descent_witness(
            prime, descent_spf
        )
        quadratic = short_certificate.quadratic_factor_external_source_descent_witness(
            prime, descent_spf
        )
        if any(
            witness is not None and witness.source_denominator >= prime
            for witness in (adaptive, mixed, quadratic)
        ):
            raise AssertionError("a strict descent source must be smaller than p")
        records.append(
            {
                "prime": prime,
                "adaptive_external_source_descent": serialize_witness(adaptive),
                "mixed_factor_external_source_descent": serialize_witness(mixed),
                "quadratic_factor_external_source_descent": serialize_witness(
                    quadratic
                ),
            }
        )

    adaptive_misses = [
        record["prime"]
        for record in records
        if record["adaptive_external_source_descent"] is None
    ]
    mixed_misses = [
        record["prime"]
        for record in records
        if record["mixed_factor_external_source_descent"] is None
    ]
    quadratic_misses = [
        record["prime"]
        for record in records
        if record["quadratic_factor_external_source_descent"] is None
    ]
    mixed_k_histogram = Counter(
        record["mixed_factor_external_source_descent"]["k"]
        for record in records
        if record["mixed_factor_external_source_descent"] is not None
    )
    quadratic_k_histogram = Counter(
        record["quadratic_factor_external_source_descent"]["k"]
        for record in records
        if record["quadratic_factor_external_source_descent"] is not None
    )
    if any(record["mixed_factor_external_source_descent"] is None for record in records):
        # The complete quadratic family may cover more points, but a mixed miss
        # must remain visible rather than silently treating the families as equal.
        pass

    return {
        "arithmetic": (
            "exact canonical-ray divisor enumeration and constructors that "
            "verify the source identity, target identity, strict source order, "
            "and Type I certificate using exact rational arithmetic"
        ),
        "scope_note": (
            "A finite hybrid audit. It does not prove a uniform H-ray bound or "
            "that any strict-lift selector succeeds for every core prime."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "canonical_shift_count": len(pairs),
        "core_prime_count": len(core_primes),
        "canonical_captured_count": captured_count,
        "canonical_residual_count": len(records),
        "adaptive_descent_count": len(records) - len(adaptive_misses),
        "mixed_factor_descent_count": len(records) - len(mixed_misses),
        "quadratic_factor_descent_count": len(records) - len(quadratic_misses),
        "adaptive_descent_misses": adaptive_misses,
        "mixed_factor_descent_misses": mixed_misses,
        "quadratic_factor_descent_misses": quadratic_misses,
        "mixed_factor_k_histogram": {
            str(k): count for k, count in sorted(mixed_k_histogram.items())
        },
        "quadratic_factor_k_histogram": {
            str(k): count for k, count in sorted(quadratic_k_histogram.items())
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--base-shift-bound", type=int, default=19)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.base_shift_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
