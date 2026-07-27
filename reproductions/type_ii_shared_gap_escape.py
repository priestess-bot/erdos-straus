#!/usr/bin/env python3
"""Audit one core prime for a shared Type II certificate through a gap cap."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-shared-gap-escape-p33011449-500k-results.json"
)


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_shared_gap_escape_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_audit(prime: int, gap_cap: int) -> dict[str, object]:
    """Run the complete shared-divisor scan for one core prime."""
    if prime < 73 or prime % 24 != 1:
        raise ValueError("prime must be a core residue at least 73")
    if gap_cap < 3:
        raise ValueError("gap_cap must be at least 3")
    last_gap = min(gap_cap, prime - 2)
    spf = short_certificate.smallest_prime_factors(prime + last_gap)
    if spf[prime] != prime:
        raise ValueError("prime must be prime")
    witness = short_certificate.type_ii_shared_divisor_tail_deflation_scan(
        prime, gap_cap, spf
    )
    result: dict[str, object] = {
        "arithmetic": (
            "exact SPF factorization; for every legal gap through the cap, "
            "complete Type II divisor certification and complete p+m divisor scan"
        ),
        "scope_note": (
            "A null witness excludes this shared Type II selector only through "
            "the stated gap cap, not at larger gaps or by other solution forms."
        ),
        "prime": prime,
        "gap_cap": gap_cap,
        "last_scanned_gap": last_gap - (last_gap - 3) % 4,
        "legal_gap_count": (last_gap - 3) // 4 + 1,
        "witness": None,
    }
    if witness is None:
        return result
    result["witness"] = {
        "gap": witness.gap,
        "first_scale": witness.first_scale,
        "shared_divisor": witness.first_scale * witness.gap + 1,
        "certificate_divisor": witness.certificate.divisor,
        "source_denominator": witness.source_denominator,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=33_011_449)
    parser.add_argument("--gap-cap", type=int, default=500_000)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.prime, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
