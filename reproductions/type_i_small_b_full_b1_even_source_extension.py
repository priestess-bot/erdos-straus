#!/usr/bin/env python3
"""Extend B=1 maximum-tail even-source reverse lifts on the 20M small-box residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-small-b-tail-deflation-20m-profile.json"
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
SMALL_B = ROOT / "reproductions" / "type_i_small_b_tail_deflation_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-small-b-full-b1-even-source-extension-20m-results.json"
GAP_CAP = 999
EXTENSION_GAP_CAP = 9999
EXACT_BOUNDARY_PRIME = 21_169


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("small_b_full_b1_direct", DIRECT)
small_b = load_module("small_b_full_b1_profile", SMALL_B)


def scan_b_one_normal_forms(
    prime: int, spf: list[int], gap_cap: int, stop_at_first_even: bool
) -> dict[str, object]:
    """Enumerate B=1 normal forms and their exact maximum-tail reverse lifts."""
    if prime % 4 != 1 or gap_cap < 3:
        raise ValueError("prime or gap cap is outside the Type I natural range")
    cap = min(gap_cap, prime - 2)
    normal_forms: list[dict[str, object]] = []
    strict_lifts: list[dict[str, object]] = []
    even_lifts: list[dict[str, object]] = []
    for gap in range(3, cap + 1, 4):
        x = (prime + gap) // 4
        for C in small_b.short_certificate.positive_divisors_from_spf(x, spf):
            if (4 * C + 1) % gap:
                continue
            A = x // C
            form = {"gap": gap, "normal_form": [A, 1, C]}
            normal_forms.append(form)
            _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(
                prime, gap, A, 1, C
            )
            for lift in lifts:
                record = {**form, "lift": lift}
                strict_lifts.append(record)
                if int(lift["source_denominator"]) % 2:
                    continue
                even_lifts.append(record)
                if stop_at_first_even:
                    return {
                        "gap_cap": cap,
                        "normal_form_count": len(normal_forms),
                        "strict_reverse_lift_count": len(strict_lifts),
                        "first_even_lift": record,
                    }
    return {
        "gap_cap": cap,
        "normal_form_count": len(normal_forms),
        "strict_reverse_lift_count": len(strict_lifts),
        "first_even_lift": None if not even_lifts else even_lifts[0],
        "all_normal_forms": normal_forms,
        "all_strict_reverse_lifts": strict_lifts,
        "all_even_lifts": even_lifts,
    }


def first_even_lift(prime: int, spf: list[int], gap_cap: int) -> dict[str, object] | None:
    """Return the first strict even B=1 lift in ascending gap order."""
    return scan_b_one_normal_forms(prime, spf, gap_cap, True)["first_even_lift"]


def run_audit(
    input_path: Path = INPUT,
    gap_cap: int = GAP_CAP,
    extension_gap_cap: int = EXTENSION_GAP_CAP,
) -> dict[str, object]:
    """Profile the two finite B=1 extensions and the exact B=1 boundary point."""
    if gap_cap < 239 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 239 and congruent to 3 modulo 4")
    if extension_gap_cap < gap_cap or extension_gap_cap % 4 != 3:
        raise ValueError("extension gap cap must be at least gap_cap and congruent to 3 modulo 4")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = [int(prime) for prime in source["misses"]]
    if source["prime_limit"] != 20_000_000 or len(residuals) != 2356:
        raise AssertionError("input does not match the stored 20M small-B tail-deflation profile")

    spf = small_b.short_certificate.smallest_prime_factors(
        (max(residuals) + gap_cap) // 4 + 1
    )
    first_stage = []
    first_misses = []
    for prime in residuals:
        witness = first_even_lift(prime, spf, gap_cap)
        record = {"prime": prime, "first_even_lift": witness}
        first_stage.append(record)
        if witness is None:
            first_misses.append(prime)

    extension_spf = small_b.short_certificate.smallest_prime_factors(
        (max(first_misses) + extension_gap_cap) // 4 + 1
    )
    extension_records = []
    extension_misses = []
    for prime in first_misses:
        witness = first_even_lift(prime, extension_spf, extension_gap_cap)
        extension_records.append({"prime": prime, "first_even_lift": witness})
        if witness is None:
            extension_misses.append(prime)

    exact_spf = small_b.short_certificate.smallest_prime_factors(
        (2 * EXACT_BOUNDARY_PRIME - 2) // 4 + 1
    )
    exact = scan_b_one_normal_forms(
        EXACT_BOUNDARY_PRIME, exact_spf, EXACT_BOUNDARY_PRIME - 2, False
    )
    if exact["first_even_lift"] is not None:
        raise AssertionError("the stated full-range B=1 boundary was unexpectedly released")
    if EXACT_BOUNDARY_PRIME not in extension_misses:
        raise AssertionError("exact boundary prime was not a persistent extension miss")

    initial_gaps = [
        int(record["first_even_lift"]["gap"])
        for record in first_stage
        if record["first_even_lift"] is not None
    ]
    extension_gaps = [
        int(record["first_even_lift"]["gap"])
        for record in extension_records
        if record["first_even_lift"] is not None
    ]
    return {
        "arithmetic": (
            "start from every m<=239, B<=4 canonical-tail-deflation miss in the stored 20M profile; "
            "for each target enumerate every divisor C of x=(p+m)/4 satisfying m|(4C+1), hence every "
            "B=1 Type I normal form, and enumerate every exact maximum-tail reverse lift, retaining strict "
            "even source denominators"
        ),
        "scope_note": (
            "The first two layers are finite window profiles. Only the final p=21169 audit exhausts every "
            "natural Type I gap for that one target, and it excludes only B=1 maximum-tail even-source lifts."
        ),
        "input_profile": input_path.name,
        "input_prime_limit": source["prime_limit"],
        "input_residual_count": len(residuals),
        "gap_cap": gap_cap,
        "captured_count": len(residuals) - len(first_misses),
        "misses": first_misses,
        "maximum_first_gap": max(initial_gaps, default=None),
        "extension_gap_cap": extension_gap_cap,
        "extension_captured_count": len(first_misses) - len(extension_misses),
        "extension_records": extension_records,
        "extension_misses": extension_misses,
        "maximum_extension_first_gap": max(extension_gaps, default=None),
        "exact_boundary_prime": EXACT_BOUNDARY_PRIME,
        "exact_boundary": exact,
        "records": first_stage,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--gap-cap", type=int, default=GAP_CAP)
    parser.add_argument("--extension-gap-cap", type=int, default=EXTENSION_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input, args.gap_cap, args.extension_gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key not in {"records", "extension_records"}},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
