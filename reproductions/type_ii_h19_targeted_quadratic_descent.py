#!/usr/bin/env python3
"""Audit strict external-source descents only on a stored H19 residual set."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-300m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-300m-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_targeted_quadratic_short_certificate", SHORT_CERTIFICATE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


class TrialSmallestFactors:
    """SPF-compatible facade for values below a finite residual bound."""

    def __init__(self, limit: int):
        self.limit = limit
        self.primes = short_certificate.primes_up_to(math.isqrt(limit))

    def __len__(self) -> int:
        return self.limit + 1

    @lru_cache(maxsize=None)
    def __getitem__(self, value: int) -> int:
        if not 1 <= value <= self.limit:
            raise IndexError(value)
        for prime in self.primes:
            if prime * prime > value:
                break
            if value % prime == 0:
                return prime
        return value


def serialize_witness(witness) -> dict[str, object] | None:
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


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Run the nested strict-lift families on every listed H19 residual."""
    primes = [int(row["prime"]) for row in payload["profiles"]]
    if not primes:
        raise ValueError("input profile has no residual primes")
    spf = TrialSmallestFactors(max(primes))
    records: list[dict[str, object]] = []
    for prime in primes:
        adaptive = short_certificate.external_source_descent_witness(prime, spf)
        mixed = short_certificate.mixed_factor_external_source_descent_witness(prime, spf)
        quadratic = short_certificate.quadratic_factor_external_source_descent_witness(prime, spf)
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
                "quadratic_factor_external_source_descent": serialize_witness(quadratic),
            }
        )
    misses = {
        label: [
            record["prime"]
            for record in records
            if record[label] is None
        ]
        for label in (
            "adaptive_external_source_descent",
            "mixed_factor_external_source_descent",
            "quadratic_factor_external_source_descent",
        )
    }
    quadratic_k = Counter(
        record["quadratic_factor_external_source_descent"]["k"]
        for record in records
        if record["quadratic_factor_external_source_descent"] is not None
    )
    return {
        "arithmetic": (
            "exact trial-prime factorization of each residual's k and n_k, "
            "with exact rational verification of source identity, target "
            "identity, strict source order, and Type I certificate"
        ),
        "scope_note": (
            "A targeted finite audit over a stored H19 residual profile. It "
            "does not prove that an external-source selector succeeds in general."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": payload["base_shift_bound"],
        "h19_residual_count": len(records),
        "adaptive_descent_count": len(records) - len(misses["adaptive_external_source_descent"]),
        "mixed_factor_descent_count": len(records) - len(misses["mixed_factor_external_source_descent"]),
        "quadratic_factor_descent_count": len(records) - len(misses["quadratic_factor_external_source_descent"]),
        "adaptive_descent_misses": misses["adaptive_external_source_descent"],
        "mixed_factor_descent_misses": misses["mixed_factor_external_source_descent"],
        "quadratic_factor_descent_misses": misses["quadratic_factor_external_source_descent"],
        "quadratic_factor_k_histogram": {
            str(k): count for k, count in sorted(quadratic_k.items())
        },
        "maximum_quadratic_k": max(quadratic_k, default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
