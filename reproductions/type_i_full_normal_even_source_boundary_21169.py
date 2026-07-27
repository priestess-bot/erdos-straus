#!/usr/bin/env python3
"""Exhaust every Type I normal maximum-tail reverse lift at p=21169."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
DEFAULT_PRIME = 21_169
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-full-normal-even-source-boundary-21169-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("full_normal_boundary_direct", DIRECT)


def run_audit(prime: int = DEFAULT_PRIME) -> dict[str, object]:
    """Enumerate all natural gaps, normal forms, and maximum-tail reverse edges."""
    if prime % 24 != 1 or prime not in direct.support_min.landscape.short_certificate.primes_up_to(prime):
        raise ValueError("prime must be a core prime")
    forms: list[dict[str, object]] = []
    strict_lifts: list[dict[str, object]] = []
    even_lifts: list[dict[str, object]] = []
    for gap in range(3, prime - 1, 4):
        for entry in direct.support_min.landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(
                prime, gap, A, B, C
            )
            form = {"gap": gap, "normal_form": [A, B, C], "strict_reverse_lift_count": len(lifts)}
            forms.append(form)
            for lift in lifts:
                record = {"gap": gap, "normal_form": [A, B, C], "lift": lift}
                strict_lifts.append(record)
                if int(lift["source_denominator"]) % 2 == 0:
                    even_lifts.append(record)
    form_b_histogram: dict[str, int] = {}
    even_b_histogram: dict[str, int] = {}
    for record in forms:
        key = str(record["normal_form"][1])
        form_b_histogram[key] = form_b_histogram.get(key, 0) + 1
    for record in even_lifts:
        key = str(record["normal_form"][1])
        even_b_histogram[key] = even_b_histogram.get(key, 0) + 1
    minimum_b = min((record["normal_form"][1] for record in even_lifts), default=None)
    minimum_b_lifts = [record for record in even_lifts if record["normal_form"][1] == minimum_b]
    return {
        "arithmetic": (
            "for every natural Type I gap m=3 (mod 4), 3<=m<=p-2, enumerate every d|x^2 "
            "for x=(p+m)/4 satisfying the exact Type I congruence, normalize to every (A,B,C), then "
            "enumerate every bridge E|4K^2 for the p-divisible maximum tail and verify every strict source"
        ),
        "scope_note": (
            "This is a complete one-point audit. It rules out only maximum-tail, two-term-preserving, "
            "strict even-source Type I lifts with the stated B cap; it does not exclude other coordinates or Type II."
        ),
        "prime": prime,
        "gap_range": [3, prime - 2],
        "normal_form_count": len(forms),
        "strict_reverse_lift_count": len(strict_lifts),
        "strict_even_lift_count": len(even_lifts),
        "normal_form_b_histogram": dict(sorted(form_b_histogram.items(), key=lambda item: int(item[0]))),
        "strict_even_lift_b_histogram": dict(sorted(even_b_histogram.items(), key=lambda item: int(item[0]))),
        "minimum_even_lift_b": minimum_b,
        "minimum_even_b_lifts": minimum_b_lifts,
        "forms": forms,
        "strict_even_lifts": even_lifts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=DEFAULT_PRIME)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.prime)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key not in {"forms", "strict_even_lifts"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
