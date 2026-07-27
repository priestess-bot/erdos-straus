#!/usr/bin/env python3
"""Classify true finite pure-new exceptions by two dynamic selectors.

For fixed ``X`` and ``H``, this script recomputes the set from its definition:
core primes ``p <= X`` for which no shift ``20 <= s <= H`` has a prime factor
``r | p + 4s`` satisfying

    r == -1 (mod 4*a_s*c_s),  r not in union_{1 <= t <= 19} Supp(p + 4t),

where ``s = a_s^2*c_s`` and ``c_s`` is squarefree.  It then independently
tests every divisor scale of ``(p-1)/4`` for a support-defect-at-most-two
ordinary tail and for the repository's dynamic external-source exit.

This is a deterministic finite experiment, not a uniform selector theorem.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions import short_certificate  # noqa: E402
from reproductions import type_ii_canonical_ray as canonical  # noqa: E402
from reproductions import type_ii_tail_support_defect as support_defect  # noqa: E402


DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-dynamic-selector-100k-h50-results.json"
)
H19_BOUND = 19


def distinct_prime_factors_from_spf(value: int, spf: list[int]) -> set[int]:
    """Return the exact prime support of ``value`` using a covering SPF table."""
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    factors: set[int] = set()
    while value > 1:
        prime = spf[value]
        factors.add(prime)
        while value % prime == 0:
            value //= prime
    return factors


def h19_source_support(prime: int, spf: list[int]) -> set[int]:
    """Return ``union_{1 <= t <= 19} Supp(p+4t)`` exactly."""
    if prime < 2 or prime + 4 * H19_BOUND >= len(spf):
        raise ValueError("SPF table does not cover the H19 source window")
    result: set[int] = set()
    for shift in range(1, H19_BOUND + 1):
        result.update(distinct_prime_factors_from_spf(prime + 4 * shift, spf))
    return result


def pure_new_witness(
    prime: int, shift_bound: int, spf: list[int]
) -> dict[str, object] | None:
    """Return the lexicographically first witness excluded by ``E_new(X,H)``.

    The set definition itself applies to every core prime.  The direct Type II
    certificate is required and recorded only beyond the theorem's strict
    boundary ``p > 4H``; smaller primes are a separately reported finite edge.
    """
    if prime % 24 != 1 or shift_bound <= H19_BOUND:
        raise ValueError("require a core prime and a shift bound above 19")
    if prime + 4 * shift_bound >= len(spf):
        raise ValueError("SPF table does not cover the shifted interval")

    old_support = h19_source_support(prime, spf)
    for shift in range(H19_BOUND + 1, shift_bound + 1):
        a, c = canonical.canonical_pair(shift)
        modulus = 4 * a * c
        shifted = prime + 4 * shift
        for new_factor in sorted(distinct_prime_factors_from_spf(shifted, spf)):
            if new_factor % modulus != modulus - 1 or new_factor in old_support:
                continue
            k = (new_factor + 1) // modulus
            certificate = short_certificate.type_ii_raw_ray_certificate(
                prime, a, c, k
            )
            if prime > 4 * shift_bound and certificate is None:
                raise AssertionError("guarded pure-new factor did not yield Type II")
            return {
                "shift": shift,
                "canonical_a": a,
                "canonical_c": c,
                "canonical_modulus": modulus,
                "shifted_integer": shifted,
                "new_prime_factor": new_factor,
                "ray_k": k,
                "h19_source_prime_support": sorted(old_support),
                "type_ii_certificate": (
                    None if certificate is None else asdict(certificate)
                ),
            }
    return None


def exact_tail_certificate(
    prime: int, scale: int, u: int, divisor: int
) -> short_certificate.GapCertificate:
    """Reconstruct and verify one ordinary ``p-1`` Type II tail certificate."""
    gap = 4 * scale - 1
    x = scale * u
    if 4 * x != prime + gap or divisor > x or x * x % divisor:
        raise AssertionError("ordinary-tail normalization failed")
    if divisor % gap != (-x) % gap:
        raise AssertionError("ordinary-tail divisor misses its target residue")
    first_numerator = prime * (x + divisor)
    second_numerator = prime * (x + x * x // divisor)
    if first_numerator % gap or second_numerator % gap:
        raise AssertionError("ordinary-tail denominators are not integral")
    certificate = short_certificate.GapCertificate(
        prime=prime,
        certificate_type="II",
        gap=gap,
        x=x,
        divisor=divisor,
        y=first_numerator // gap,
        z=second_numerator // gap,
    )
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("ordinary-tail certificate did not replay")
    if certificate.y % prime or certificate.z % prime:
        raise AssertionError("ordinary-tail certificate did not deflate")
    source_solution = (x, certificate.y // prime, certificate.z // prime)
    if Fraction(4, u) != sum(
        (Fraction(1, denominator) for denominator in source_solution), Fraction()
    ):
        raise AssertionError("ordinary-tail source identity failed")
    return certificate


def dynamic_low_defect_tail(
    prime: int, spf: list[int], max_support: int
) -> dict[str, object] | None:
    """Find the first globally minimum-defect dynamic ordinary tail.

    Scales are all positive divisors of ``B=(p-1)/4``.  For scale ``q``, set
    ``u=B/q+1``, ``m=4q-1``, and ``x=q*u``.  A prime in ``Supp(d)`` is charged
    exactly when it is outside ``Supp(q)``.  Iterating the defect first proves
    minimality through ``max_support`` rather than merely finding a small
    divisor under that threshold.
    """
    if prime % 24 != 1 or prime >= len(spf) or max_support < 0:
        raise ValueError("require a covered core prime and nonnegative support")
    base = (prime - 1) // 4
    scales = short_certificate.positive_divisors_from_spf(base, spf)
    for defect in range(max_support + 1):
        for scale in scales:
            u = base // scale + 1
            base_primes = distinct_prime_factors_from_spf(scale, spf)
            witness = support_defect.support_witness(
                scale, u, base_primes, defect
            )
            if witness is None:
                continue
            divisor = int(witness["divisor"])
            divisor_support = distinct_prime_factors_from_spf(divisor, spf)
            new_support = divisor_support - base_primes
            if len(new_support) != defect or int(witness["support"]) != defect:
                raise AssertionError("reported support defect is not globally minimal")
            certificate = exact_tail_certificate(prime, scale, u, divisor)
            source_solution = [
                certificate.x,
                certificate.y // prime,
                certificate.z // prime,
            ]
            return {
                "support_defect": defect,
                "scale": scale,
                "p_minus_one_over_four": base,
                "u": u,
                "gap": certificate.gap,
                "x": certificate.x,
                "divisor": divisor,
                "scale_prime_support": sorted(base_primes),
                "divisor_prime_support": sorted(divisor_support),
                "new_prime_support": sorted(new_support),
                "source_denominator": u,
                "source_solution": source_solution,
                "target_solution": [
                    certificate.x,
                    certificate.y,
                    certificate.z,
                ],
                "type_ii_certificate": asdict(certificate),
            }
    return None


def dynamic_external_source_exit(
    prime: int, spf: list[int]
) -> dict[str, object] | None:
    """Return the first complete-square-tail exit over every ``k|B``.

    This is the full branch E: with ``r=4k-1``, ``n=(r*p+1)/(4k)`` and
    ``M=k*n``, it exhausts every ``e|M^2`` through the repository's exact SPF
    divisor API.  It is strictly broader than the standard ``factor|n`` exit.
    """
    if prime % 24 != 1 or prime >= len(spf):
        raise ValueError("require a covered core prime")
    base = (prime - 1) // 4
    for scale in short_certificate.positive_divisors_from_spf(base, spf):
        source_modulus = 4 * scale - 1
        numerator = source_modulus * prime + 1
        source, remainder = divmod(numerator, 4 * scale)
        if remainder or source != prime - base // scale or not 2 <= source < prime:
            raise AssertionError("dynamic external source normalization failed")
        source_product = scale * source
        target_residue = (-source_product) % source_modulus
        checked_divisors = 0
        for square_divisor in short_certificate.positive_divisors_square_product_from_spf(
            scale, source, spf
        ):
            if square_divisor > source_product:
                break
            checked_divisors += 1
            if square_divisor % source_modulus != target_residue:
                continue
            first_tail, remainder = divmod(
                source_product + square_divisor, source_modulus
            )
            if remainder or source_product * first_tail % square_divisor:
                raise AssertionError("complete-square-tail divisibility failed")
            second_tail = source_product * first_tail // square_divisor
            source_solution = (source_product, first_tail, second_tail)
            target_solution = (source_product * prime, first_tail, second_tail)
            for denominator, solution in (
                (source, source_solution),
                (prime, target_solution),
            ):
                if Fraction(4, denominator) != sum(
                    (Fraction(1, value) for value in solution), Fraction()
                ):
                    raise AssertionError("external-source identity failed")
            return {
                "scale": scale,
                "source_modulus": source_modulus,
                "source_denominator": source,
                "source_product": source_product,
                "square_tail_divisor": square_divisor,
                "checked_square_divisors_at_success_scale": checked_divisors,
                "first_tail": first_tail,
                "second_tail": second_tail,
                "source_solution": list(source_solution),
                "target_solution": list(target_solution),
            }
    return None


def availability_class(tail: object | None, external: object | None) -> str:
    """Return one of four mutually exclusive availability classes."""
    if tail is not None and external is not None:
        return "both"
    if tail is not None:
        return "tail-only"
    if external is not None:
        return "external-only"
    return "neither"


def selected_branch(tail: object | None, external: object | None) -> str:
    """Choose one mutually exclusive route, preferring the low-defect tail."""
    if tail is not None:
        return "dynamic-low-defect-tail"
    if external is not None:
        return "dynamic-external-source-exit"
    return "unresolved"


def compact_report(report: dict[str, object]) -> dict[str, object]:
    """Return a small, hash-anchored representation of a full experiment."""
    records = report["records"]
    if not isinstance(records, list):
        raise TypeError("full report records must be a list")
    canonical_records = json.dumps(
        records,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    class_primes = {
        name: [
            int(record["prime"])
            for record in records
            if record["availability_class"] == name
        ]
        for name in ("tail-only", "external-only", "neither")
    }
    tail_records = [
        record
        for record in records
        if record["dynamic_low_defect_tail"] is not None
    ]
    tail_scales = [
        int(record["dynamic_low_defect_tail"]["scale"])
        for record in tail_records
    ]
    if not tail_scales:
        raise AssertionError("a covered selector report must contain a tail record")
    maximum_tail_scale = max(tail_scales)
    retained_keys = (
        "arithmetic",
        "scope_note",
        "definition",
        "prime_limit",
        "shift_bound",
        "max_support_checked",
        "strict_newness_prime_guard",
        "core_prime_count",
        "small_boundary_core_prime_count",
        "pure_new_captured_count",
        "pure_new_exception_count",
        "pure_new_exception_primes",
        "availability_counts",
        "selected_branch_counts",
        "minimum_tail_support_defect_histogram",
        "selector_union_covered_count",
        "selector_union_unresolved_count",
        "selector_union_unresolved_primes",
    )
    return {
        "format": "compact-dynamic-selector-report-v1",
        **{key: report[key] for key in retained_keys},
        "availability_boundary_primes": class_primes,
        "selected_tail_scale_summary": {
            "minimum": min(tail_scales),
            "maximum": maximum_tail_scale,
            "maximum_primes": [
                int(record["prime"])
                for record in tail_records
                if int(record["dynamic_low_defect_tail"]["scale"])
                == maximum_tail_scale
            ],
            "meaning": (
                "Each stored tail first minimizes support defect, then chooses the "
                "least divisor scale q attaining that defect."
            ),
        },
        "external_only_records": [
            record
            for record in records
            if record["availability_class"] == "external-only"
        ],
        "full_record_count": len(records),
        "full_records_sha256": hashlib.sha256(canonical_records).hexdigest(),
        "hash_canonicalization": (
            "JSON records array with ensure_ascii=false, sort_keys=true, "
            "and separators=(',', ':') encoded as UTF-8"
        ),
    }


def run_experiment(
    limit: int = 100_000, shift_bound: int = 50, max_support: int = 2
) -> dict[str, object]:
    """Recompute ``E_new(X,H)`` and classify every member exactly."""
    if limit < 73 or shift_bound <= H19_BOUND or max_support < 0:
        raise ValueError("require limit >= 73, H >= 20, and nonnegative support")
    spf = short_certificate.smallest_prime_factors(limit + 4 * shift_bound)
    core_primes = [
        prime
        for prime in short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]

    exception_primes: list[int] = []
    capture_samples: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    availability_counts: Counter[str] = Counter()
    selection_counts: Counter[str] = Counter()
    for prime in core_primes:
        witness = pure_new_witness(prime, shift_bound, spf)
        if witness is not None:
            if len(capture_samples) < 12:
                capture_samples.append({"prime": prime, **witness})
            continue

        exception_primes.append(prime)
        tail = dynamic_low_defect_tail(prime, spf, max_support)
        external = dynamic_external_source_exit(prime, spf)
        availability = availability_class(tail, external)
        selected = selected_branch(tail, external)
        availability_counts[availability] += 1
        selection_counts[selected] += 1
        records.append(
            {
                "prime": prime,
                "above_strict_newness_guard": prime > 4 * shift_bound,
                "dynamic_low_defect_tail": tail,
                "dynamic_external_source_exit": external,
                "availability_class": availability,
                "selected_branch": selected,
            }
        )

    exception_count = len(exception_primes)
    if sum(availability_counts.values()) != exception_count:
        raise AssertionError("availability classes do not partition E_new")
    if sum(selection_counts.values()) != exception_count:
        raise AssertionError("selected branches do not partition E_new")
    unresolved = [
        int(record["prime"])
        for record in records
        if record["selected_branch"] == "unresolved"
    ]
    defect_histogram = Counter(
        int(record["dynamic_low_defect_tail"]["support_defect"])
        for record in records
        if record["dynamic_low_defect_tail"] is not None
    )
    union_covered = exception_count - len(unresolved)
    return {
        "arithmetic": (
            "integer SPF factorizations for every defining shift, exhaustive divisor "
            "scales of (p-1)/4, exact support enumeration, and Fraction-based replay "
            "of every stored source and target certificate"
        ),
        "scope_note": (
            "This is a finite experiment on the exact E_new(X,H) definition. A hit "
            "does not prove a uniform selector, and an unresolved point excludes only "
            "the two precisely stated dynamic branches."
        ),
        "definition": {
            "core_primes": "prime p <= X with p == 1 (mod 24)",
            "old_support": "union of Supp(p+4t) for 1 <= t <= 19",
            "exception": (
                "for every 20 <= s <= H, no prime r divides p+4s with "
                "r == -1 (mod 4*a_s*c_s) outside old_support, where s=a_s^2*c_s"
            ),
            "tail_defect": (
                "minimum over q|(p-1)/4 and d|x^2, d<=x, d==-x (mod 4q-1) "
                "of |Supp(d)\\Supp(q)|, with x=q*((p-1)/(4q)+1)"
            ),
            "external_exit": (
                "for k|(p-1)/4, M=k*((4k-1)p+1)/(4k) has e|M^2 with "
                "e<=M and e==-M modulo 4k-1, yielding a verified strict lift"
            ),
        },
        "prime_limit": limit,
        "shift_bound": shift_bound,
        "max_support_checked": max_support,
        "strict_newness_prime_guard": 4 * shift_bound,
        "core_prime_count": len(core_primes),
        "small_boundary_core_prime_count": sum(
            prime <= 4 * shift_bound for prime in core_primes
        ),
        "pure_new_captured_count": len(core_primes) - exception_count,
        "pure_new_exception_count": exception_count,
        "pure_new_exception_primes": exception_primes,
        "pure_new_capture_samples": capture_samples,
        "availability_counts": {
            name: availability_counts.get(name, 0)
            for name in ("both", "tail-only", "external-only", "neither")
        },
        "selected_branch_counts": {
            name: selection_counts.get(name, 0)
            for name in (
                "dynamic-low-defect-tail",
                "dynamic-external-source-exit",
                "unresolved",
            )
        },
        "minimum_tail_support_defect_histogram": {
            str(defect): defect_histogram.get(defect, 0)
            for defect in range(max_support + 1)
        },
        "selector_union_covered_count": union_covered,
        "selector_union_unresolved_count": len(unresolved),
        "selector_union_unresolved_primes": unresolved,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--shift-bound", type=int, default=50)
    parser.add_argument("--max-support", type=int, default=2)
    parser.add_argument(
        "--compact",
        action="store_true",
        help="store a compact summary plus a canonical hash of the full records",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    full_result = run_experiment(args.limit, args.shift_bound, args.max_support)
    result = compact_report(full_result) if args.compact else full_result
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    verbose_summary_keys = {
        "records",
        "pure_new_exception_primes",
        "pure_new_capture_samples",
        "availability_boundary_primes",
        "external_only_records",
    }
    summary = {
        key: value for key, value in result.items() if key not in verbose_summary_keys
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
