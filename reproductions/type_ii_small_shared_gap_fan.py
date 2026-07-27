#!/usr/bin/env python3
"""Verify the explicit shared Type II fan at gaps 3, 7, and 11."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-small-shared-gap-10m-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_small_shared_gap_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


@dataclass(frozen=True)
class SmallSharedGapWitness:
    prime: int
    gap: int
    x: int
    type_ii_divisor: int
    shared_divisor: int
    branch: str


def factor_two_mod_three(value: int, spf: list[int]) -> int | None:
    """Return one prime divisor congruent to 2 modulo 3, if it exists."""
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the value")
    while value > 1:
        prime = spf[value]
        if prime % 3 == 2:
            return prime
        while value % prime == 0:
            value //= prime
    return None


def build_witness(
    prime: int, gap: int, divisor: int, shared_divisor: int, branch: str
) -> SmallSharedGapWitness:
    """Construct and exactly check one explicit Type II shared-gap witness."""
    x = (prime + gap) // 4
    if (
        4 * x != prime + gap
        or divisor < 1
        or divisor > x
        or x * x % divisor
        or (x + divisor) % gap
        or (prime + gap) % shared_divisor
        or shared_divisor % gap != 1
    ):
        raise AssertionError("the explicit small-gap conditions did not hold")
    certificate = short_certificate.GapCertificate(
        prime,
        "II",
        gap,
        x,
        divisor,
        prime * (x + divisor) // gap,
        prime * (x + x * x // divisor) // gap,
    )
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("the explicit Type II certificate did not verify")
    return SmallSharedGapWitness(
        prime, gap, x, divisor, shared_divisor, branch
    )


def small_shared_gap_witness(
    prime: int, spf: list[int]
) -> SmallSharedGapWitness | None:
    """Return the first explicit shared Type II witness in the 3,7,11 fan."""
    if prime % 24 != 1 or prime < 73:
        return None

    x_three = (prime + 3) // 4
    factor = factor_two_mod_three(x_three, spf)
    if factor is not None:
        return build_witness(prime, 3, factor, 4, "m3_factor_2_mod_3")

    seven_divisor = {3: 1, 5: 4, 6: 2}.get(prime % 7)
    if seven_divisor is not None:
        return build_witness(
            prime, 7, seven_divisor, 8, "m7_explicit_residue"
        )

    eleven_divisor = {7: 1, 8: 9, 10: 3}.get(prime % 11)
    if eleven_divisor is not None:
        return build_witness(
            prime, 11, eleven_divisor, 12, "m11_explicit_residue"
        )
    return None


def explicit_residual_conditions(prime: int, spf: list[int]) -> bool:
    """Return whether the three explicit branches all miss prime."""
    if prime % 24 != 1 or prime < 73:
        return False
    return (
        factor_two_mod_three((prime + 3) // 4, spf) is None
        and prime % 7 in {1, 2, 4}
        and prime % 11 in {1, 2, 3, 4, 5, 6, 9}
    )


def run_audit(limit: int, sample_cap: int = 20) -> dict[str, object]:
    """Count the exact coverage of only the three proved explicit branches."""
    if limit < 73 or sample_cap < 0:
        raise ValueError("limit must be at least 73 and sample_cap nonnegative")
    spf = short_certificate.smallest_prime_factors(limit + 11)
    counts = {
        "m3_factor_2_mod_3": 0,
        "m7_explicit_residue": 0,
        "m11_explicit_residue": 0,
        "explicit_residual": 0,
    }
    samples = {key: [] for key in counts}
    core_prime_count = 0
    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        witness = small_shared_gap_witness(prime, spf)
        branch = witness.branch if witness is not None else "explicit_residual"
        counts[branch] += 1
        if len(samples[branch]) < sample_cap:
            samples[branch].append(prime)
        if witness is None:
            if not explicit_residual_conditions(prime, spf):
                raise AssertionError("residual classification was inconsistent")
        elif not short_certificate.verify_certificate(
            short_certificate.GapCertificate(
                witness.prime,
                "II",
                witness.gap,
                witness.x,
                witness.type_ii_divisor,
                witness.prime * (witness.x + witness.type_ii_divisor)
                // witness.gap,
                witness.prime
                * (witness.x + witness.x * witness.x // witness.type_ii_divisor)
                // witness.gap,
            )
        ):
            raise AssertionError("audit witness no longer verifies")

    covered = core_prime_count - counts["explicit_residual"]
    return {
        "arithmetic": (
            "exact SPF factorization only for the m=3 branch; exact integer "
            "verification for every explicit Type II and shared divisor"
        ),
        "scope_note": (
            "This audits a proved three-branch sufficient fan. Its residual "
            "may still be captured by non-explicit divisor choices at 7 or 11."
        ),
        "prime_limit": limit,
        "core_prime_count": core_prime_count,
        "counts": counts,
        "covered_count": covered,
        "covered_ratio": covered / core_prime_count,
        "samples": samples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--sample-cap", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.sample_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
