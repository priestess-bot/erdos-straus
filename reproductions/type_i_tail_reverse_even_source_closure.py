#!/usr/bin/env python3
"""Find an even strict reverse source for every 500M ordinary-tail miss."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("even_source_closure_landscape", LANDSCAPE)
bridge = load_module("even_source_closure_bridge", BRIDGE)


def first_even_source_edge(
    prime: int, gap_cap: int
) -> tuple[dict[str, object] | None, int, int]:
    """Return the first exact strict reverse edge with an even source denominator."""
    forms = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            certificate = bridge.short_certificate.type_i_normal_form_certificate(
                prime, gap, A, B
            )
            if certificate is None:
                raise AssertionError("stored normal form did not rebuild")
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                source_prime = int(lift["source_denominator"])
                if source_prime % 2:
                    continue
                target = (certificate.x, certificate.y, certificate.z)
                source = (int(lift["source_term"]), certificate.x, certificate.y)
                if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
                    raise AssertionError("target identity did not verify")
                if Fraction(4, source_prime) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("source identity did not verify")
                return (
                    {
                        "gap": gap,
                        "normal_form": [A, B, C],
                        "target_solution": list(target),
                        "reverse_two_tail_lift": lift,
                        "source_solution": list(source),
                        "terminal_prime": 2,
                        "scaling_multiplier": source_prime // 2,
                    },
                    forms,
                    lifts_checked,
                )
    return None, forms, lifts_checked


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, local_forms, local_lifts = first_even_source_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, **witness})
    gap_histogram: dict[str, int] = {}
    b_histogram: dict[str, int] = {}
    for record in records:
        gap = str(record["gap"])
        B = str(record["normal_form"][1])
        gap_histogram[gap] = gap_histogram.get(gap, 0) + 1
        b_histogram[B] = b_histogram.get(B, 0) + 1
    return {
        "arithmetic": (
            "for every stored ordinary Type II p-1-tail miss, enumerate Type I normal "
            "certificates with m=3 (mod 4) through gap_cap and every strict maximum-tail "
            "reverse lift; select the first with an even source denominator and verify both "
            "Egyptian-fraction identities exactly"
        ),
        "scope_note": (
            "A finite target-side even-source closure. An even source is terminal by scaling "
            "from the known n=2 solution, but this does not provide a global source-side selector."
        ),
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "even_source_captured_count": len(records),
        "even_source_misses": misses,
        "normal_forms_checked_until_first_even_source_or_exhaustion": forms,
        "strict_reverse_lifts_checked_until_first_even_source_or_exhaustion": lifts,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "first_even_source_gap_histogram": dict(
            sorted(gap_histogram.items(), key=lambda item: int(item[0]))
        ),
        "first_even_source_B_histogram": dict(
            sorted(b_histogram.items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.tail.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
