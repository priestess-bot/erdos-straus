#!/usr/bin/env python3
"""Join first-r overflow tails to the same-certificate tail-deflation criterion."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
TAIL_PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_even_source_overflow_profile.py"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_QUADRATIC = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-overflow-tail-deflation-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tail_profile = load_module("h19_overflow_tail_deflation_tail_profile", TAIL_PROFILE)
short_certificate = load_module("h19_overflow_tail_deflation_short_certificate", SHORT_CERTIFICATE)


def tail_deflation_row(prime: int, r: int, tail: dict[str, object]) -> dict[str, object]:
    """Specialize normal tail deflation to one even-source tail."""
    gap, overflow = int(tail["gap"]), int(tail["overflow"])
    normal_a, normal_b, normal_c = (int(value) for value in tail["normal_form"])
    if normal_b != overflow:
        raise AssertionError("tail overflow disagrees with its Type I normal form")
    numerator = 4 * normal_b * normal_b * normal_c + 1
    if numerator % gap or numerator // gap != r:
        raise AssertionError("even-source tail did not specialize the normal quotient to r")
    criterion_holds = (4 * normal_b * normal_c * (normal_a + normal_b)) % (r + 1) == 0
    r_divisor_condition = (prime - 1) % (r + 1) == 0
    if criterion_holds != r_divisor_condition:
        raise AssertionError("same-tail deflation did not reduce to r+1 dividing p-1")
    witness = short_certificate.type_i_normal_tail_deflation_witness(
        prime, gap, normal_a, normal_b
    )
    if (witness is not None) != criterion_holds:
        raise AssertionError("specialized tail-deflation congruence disagrees with witness construction")
    return {
        "tail_factor": int(tail["tail_factor"]),
        "gap": gap,
        "overflow": overflow,
        "normal_form": [normal_a, normal_b, normal_c],
        "tail_deflation_condition_holds": criterion_holds,
        "r_plus_one_divides_p_minus_one": r_divisor_condition,
        "source_denominator": witness.source_denominator if witness is not None else None,
    }


def run_audit(overflow_payload: dict[str, object], quadratic_payload: dict[str, object]) -> dict[str, object]:
    """Measure when a high first-r tail itself provides a strict source descent."""
    quadratic = {
        int(row["prime"]): row["quadratic_factor_external_source_descent"]
        for row in quadratic_payload["records"]
    }
    records = []
    for row in overflow_payload["records"]:
        if int(row["minimum_overflow"]) == 1:
            continue
        prime, r = int(row["prime"]), int(row["r"])
        m1 = (r * prime + 1) // 4
        tails = [tail_deflation_row(prime, r, tail) for tail in tail_profile.tail_rows(prime, r, m1)]
        direct = [tail for tail in tails if tail["tail_deflation_condition_holds"]]
        if len({bool(tail["tail_deflation_condition_holds"]) for tail in tails}) != 1:
            raise AssertionError("same-r tails disagreed on the r-only deflation condition")
        if prime not in quadratic or quadratic[prime] is None:
            raise AssertionError("stored high-overflow state lacks quadratic external descent")
        records.append(
            {
                "prime": prime,
                "r": r,
                "minimum_overflow": int(row["minimum_overflow"]),
                "all_tail_overflows": [int(tail["overflow"]) for tail in tails],
                "same_tail_deflation_witnesses": direct,
                "r_plus_one_divides_p_minus_one": bool(direct),
                "quadratic_external_source": {
                    key: int(quadratic[prime][key])
                    for key in ("source_denominator", "k", "q", "factor")
                },
            }
        )
    direct_records = [record for record in records if record["same_tail_deflation_witnesses"]]
    misses = [record for record in records if not record["same_tail_deflation_witnesses"]]
    composite_only = [
        record
        for record in records
        if not any(sympy.isprime(overflow) for overflow in record["all_tail_overflows"])
    ]
    composite_direct = [record for record in composite_only if record["same_tail_deflation_witnesses"]]
    composite_misses = [record for record in composite_only if not record["same_tail_deflation_witnesses"]]
    miss_k_histogram = Counter(int(record["quadratic_external_source"]["k"]) for record in misses)
    composite_miss_k_histogram = Counter(
        int(record["quadratic_external_source"]["k"]) for record in composite_misses
    )
    if any(int(record["quadratic_external_source"]["q"]) == int(record["r"]) for record in misses):
        raise AssertionError("an r-divisibility failure cannot use the same external modulus")
    return {
        "arithmetic": (
            "exact first-r tail enumeration, the specialized normal-tail divisibility "
            "test r+1 | 4*B*C*(A+B), and exact external-source witness joins"
        ),
        "scope_note": (
            "A finite same-tail deflation profile. It does not prove that either this "
            "tail condition or a quadratic external source exists generally."
        ),
        "prime_limit": overflow_payload["prime_limit"],
        "high_overflow_state_count": len(records),
        "same_tail_deflation_state_count": len(direct_records),
        "r_plus_one_divides_p_minus_one_count": sum(
            bool(record["r_plus_one_divides_p_minus_one"]) for record in records
        ),
        "same_tail_deflation_is_exactly_r_divisor_condition": True,
        "same_tail_deflation_miss_count": len(misses),
        "all_same_tail_deflation_misses_have_quadratic_external_source": all(
            record["quadratic_external_source"] for record in misses
        ),
        "all_same_tail_deflation_misses_use_different_external_q": True,
        "same_tail_deflation_miss_quadratic_k_histogram": {
            str(key): value for key, value in sorted(miss_k_histogram.items())
        },
        "maximum_same_tail_deflation_miss_quadratic_k": max(miss_k_histogram, default=None),
        "composite_only_overflow_state_count": len(composite_only),
        "composite_only_same_tail_deflation_count": len(composite_direct),
        "composite_only_same_tail_deflation_miss_count": len(composite_misses),
        "composite_only_miss_quadratic_k_histogram": {
            str(key): value for key, value in sorted(composite_miss_k_histogram.items())
        },
        "maximum_composite_only_miss_quadratic_k": max(composite_miss_k_histogram, default=None),
        "composite_only_misses": misses_for_json(composite_misses),
        "records": records,
    }


def misses_for_json(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Keep the unresolved same-tail branch compact and inspectable."""
    return [
        {
            "prime": record["prime"],
            "r": record["r"],
            "tail_overflows": record["all_tail_overflows"],
            "quadratic_external_source": record["quadratic_external_source"],
        }
        for record in records
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--quadratic", type=Path, default=DEFAULT_QUADRATIC)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.input.read_text(encoding="utf-8")),
        json.loads(args.quadratic.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
