#!/usr/bin/env python3
"""Exhaust p-minus-one Type I bridges on the complete 500M tail residual.

For every ordinary Type II p-1-tail miss in the stored 500M closure, enumerate
every Type I normal form through m<=215.  Source n=p-1 forces the unique bridge
factor E=R+1, so the p-minus-one square criterion checks that state directly
without materializing the much larger list of unrelated reverse lifts.  Thus a
miss is an exact boundary for this finite normal-form box, not evidence against
p-minus-one bridges at larger m.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("pminusone_profile_landscape", LANDSCAPE)
bridge = load_module("pminusone_profile_bridge", BRIDGE)


def first_pminusone_edge(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust normal forms and retain the first unique p-minus-one bridge state."""
    best: dict[str, object] | None = None
    forms = 0
    states_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            R = (4 * B * B * C + 1) // gap
            H = A * R - B
            K = B * C * H
            L = 2 * K
            certificate = bridge.short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
            if certificate is None:
                raise AssertionError("stored Type I normal form did not reconstruct")
            states_checked += 1
            E = R + 1
            r = E // 4
            t = (prime - 1) // 4
            if (t * t) % r:
                continue
            source = prime - 1
            source_term_numerator = source * K
            if source_term_numerator % E:
                raise AssertionError("p-minus-one square condition did not reconstruct the source term")
            source_term = source_term_numerator // E
            divisor_gcd = math.gcd(E, L)
            a, b = E // divisor_gcd, L // divisor_gcd
            if (
                R % 4 != 3
                or E != R + 1
                or (4 * K * K) % E
                or math.gcd(a, b) != 1
                or L % a
                or L % b
                or a >= b
                or (a - 2 * b) % R
                or E != L * a // b
                or E % 2
                or E > 2 * L - 2 * R
            ):
                raise AssertionError("p-minus-one bridge failed the exact normal conditions")
            target_solution = (certificate.x, certificate.y, certificate.z)
            source_solution = (source_term, certificate.x, certificate.y)
            if Fraction(4, prime) != sum(
                (Fraction(1, denominator) for denominator in target_solution), Fraction()
            ):
                raise AssertionError("p-minus-one target identity failed")
            if Fraction(4, source) != sum(
                (Fraction(1, denominator) for denominator in source_solution), Fraction()
            ):
                raise AssertionError("p-minus-one source identity failed")
            candidate = {
                "gap": gap,
                "normal_form": [A, B, C],
                "R": R,
                "K": K,
                "E": E,
                "a": a,
                "b": b,
                "source_denominator": source,
            }
            key = (gap, B, E, A, C, a, b)
            if best is None or key < (
                int(best["gap"]),
                int(best["normal_form"][1]),
                int(best["E"]),
                int(best["normal_form"][0]),
                int(best["normal_form"][2]),
                int(best["a"]),
                int(best["b"]),
            ):
                best = candidate
    return best, forms, states_checked


def run_profile(closure: dict[str, object]) -> dict[str, object]:
    """Profile the p-minus-one subselector on every stored ordinary-tail miss."""
    gap_cap = int(closure["gap_cap"])
    source_records = closure["records"]
    if not isinstance(source_records, list):
        raise AssertionError("closure records must be a list")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    states = 0
    for raw_record in source_records:
        if not isinstance(raw_record, dict):
            raise AssertionError("closure record must be an object")
        prime = int(raw_record["prime"])
        witness, local_forms, local_states = first_pminusone_edge(prime, gap_cap)
        forms += local_forms
        states += local_states
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "p_minus_one_witness": witness})
    if len(records) + len(misses) != len(source_records):
        raise AssertionError("p-minus-one profile did not partition the tail residual")
    gap_histogram = Counter(int(record["p_minus_one_witness"]["gap"]) for record in records)
    b_histogram = Counter(int(record["p_minus_one_witness"]["normal_form"][1]) for record in records)
    return {
        "arithmetic": (
            "for every stored 500M ordinary Type II p-1-tail miss, enumerate all Type I normal forms "
            "through m<=gap_cap; for each normal form test its unique p-minus-one factor E=R+1 via "
            "r|((p-1)/4)^2, then recheck the small-side divisor pair and both Egyptian-fraction identities"
        ),
        "scope_note": (
            "A complete p-minus-one audit only in the stated m<=gap_cap Type I normal-form box. A miss "
            "does not rule out p-minus-one bridges at larger gaps, other upper-half sources, or the global "
            "mixed terminal selector."
        ),
        "input_artifact": INPUT.name,
        "prime_limit": int(closure["prime_limit"]),
        "gap_cap": gap_cap,
        "ordinary_tail_residual_count": len(source_records),
        "p_minus_one_captured_count": len(records),
        "p_minus_one_misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "p_minus_one_states_exhaustively_checked": states,
        "selected_gap_histogram": {str(key): value for key, value in sorted(gap_histogram.items())},
        "selected_B_histogram": {str(key): value for key, value in sorted(b_histogram.items())},
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
