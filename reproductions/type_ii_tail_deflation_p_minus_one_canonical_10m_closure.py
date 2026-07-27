#!/usr/bin/env python3
"""Close the 10m strict-descent boundary by a tiny canonical Type II fan."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-tail-deflation-p-minus-one-10m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-canonical-10m-results.json"
)
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_script("tail_deflation_p_minus_one_canonical", CANONICAL_SCRIPT)


def run_audit(
    input_path: Path = DEFAULT_INPUT, canonical_shift_cap: int = 2
) -> dict[str, object]:
    """Certify all supplied strict-descent misses by canonical Type II rays."""
    if canonical_shift_cap < 1:
        raise ValueError("canonical_shift_cap must be positive")
    input_payload = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = [int(prime) for prime in input_payload["uncovered_primes"]]
    pairs = [
        canonical.canonical_pair(shift)
        for shift in range(1, canonical_shift_cap + 1)
    ]
    max_shift = max(a * a * c for a, c in pairs)
    spf = canonical.ray.short_certificate.smallest_prime_factors(
        max(residuals) + 4 * max_shift
    )
    records = []
    for prime in residuals:
        witness = next(
            (
                {"first_shift": shift, **candidate}
                for shift, pair in enumerate(pairs, start=1)
                if (
                    candidate := canonical.witness_for_pair(prime, pair, spf)
                )
                is not None
            ),
            None,
        )
        records.append({"prime": prime, "witness": witness})
    misses = [record["prime"] for record in records if record["witness"] is None]
    strict_lifts = int(input_payload["combined_strict_lift_count"])
    core_count = int(input_payload["core_prime_count"])
    return {
        "arithmetic": (
            "exact canonical Type II ray divisor enumeration and reconstructed "
            "Type II certificate checks on every residual strict-descent prime"
        ),
        "scope_note": (
            "A finite short-certificate-or-descent closure. Canonical-ray "
            "certificates are direct certificates, not asserted strict descents."
        ),
        "input_artifact": input_path.name,
        "prime_limit": input_payload["prime_limit"],
        "canonical_shift_cap": canonical_shift_cap,
        "core_prime_count": core_count,
        "strict_descent_count": strict_lifts,
        "canonical_short_certificate_count": len(records) - len(misses),
        "unclosed_count": len(misses),
        "unclosed_primes": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--canonical-shift-cap", type=int, default=2)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input, args.canonical_shift_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
