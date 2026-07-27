#!/usr/bin/env python3
"""Close the 1B H19 residuals by bounded Type I reverse two-tail lifts."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
PROFILE = ROOT / "reproductions" / "type_i_tail_reverse_small_b_profile.py"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_GAP_CAP = 127
DEFAULT_B_CAP = 1
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-terminal-b1-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_b = load_module("h19_reverse_two_tail_small_b", PROFILE)
landscape = load_module("h19_reverse_two_tail_landscape", LANDSCAPE)


def terminal_factor(source: int) -> tuple[dict[int, int], int]:
    """Return a complete factorization and its least non-core prime factor."""
    factors = landscape.factor_by_trial_division(source)
    for prime in factors:
        if prime % 24 != 1:
            return factors, prime
    raise AssertionError("reverse source has only core prime factors")


def run_closure(h19: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP, b_cap: int = DEFAULT_B_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")
    residuals = [int(profile["prime"]) for profile in h19["profiles"]]
    if len(residuals) != int(h19["source_free_count"]):
        raise AssertionError("H19 residual count did not reconstruct")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    b_counts: dict[str, int] = {}
    terminal_residue_counts: dict[str, int] = {}
    normal_forms_checked = 0
    for prime in residuals:
        edge, checked = small_b.first_small_b_edge(prime, gap_cap, b_cap)
        normal_forms_checked += checked
        if edge is None:
            misses.append(prime)
            continue
        source = int(edge["reverse_two_tail_lift"]["source_denominator"])
        factors, terminal_prime = terminal_factor(source)
        multiplier = source // terminal_prime
        if terminal_prime * multiplier != source:
            raise AssertionError("terminal factor did not reconstruct source")
        b = int(edge["normal_form"][1])
        b_counts[str(b)] = b_counts.get(str(b), 0) + 1
        residue = str(terminal_prime % 24)
        terminal_residue_counts[residue] = terminal_residue_counts.get(residue, 0) + 1
        records.append(
            {
                "prime": prime,
                "gap": edge["gap"],
                "divisor": edge["divisor"],
                "normal_form": edge["normal_form"],
                "target_solution": edge["target_solution"],
                "reverse_two_tail_lift": edge["reverse_two_tail_lift"],
                "source_solution": edge["source_solution"],
                "source_factorization": {str(q): exponent for q, exponent in factors.items()},
                "terminal_prime": terminal_prime,
                "terminal_prime_mod_24": terminal_prime % 24,
                "scaling_multiplier": multiplier,
            }
        )
    return {
        "arithmetic": (
            "for every stored H19 source-free residual, enumerate each Type I normal "
            "certificate with m=3 (mod 4) through gap_cap and B<=b_cap; apply the "
            "complete maximum-tail reverse-two-tail selector, verify both identities, "
            "and factor the strict source to select a prime outside 1 modulo 24"
        ),
        "scope_note": (
            "Finite cross-family audit on the stored 1B H19 residuals. It does not "
            "prove a uniform source-side selector or extend the canonical H19 range."
        ),
        "input_h19_artifact": "type-ii-source-free-transition-h19-1b-results.json",
        "prime_limit": h19["prime_limit"],
        "base_shift_bound": h19["base_shift_bound"],
        "h19_residual_count": len(residuals),
        "gap_cap": gap_cap,
        "b_cap": b_cap,
        "captured_count": len(records),
        "misses": misses,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "total_small_b_normal_forms_checked_until_first_edge_or_cap": normal_forms_checked,
        "first_hit_b_counts": dict(sorted(b_counts.items(), key=lambda item: int(item[0]))),
        "unresolved_core_source_count": 0 if not misses else None,
        "terminal_prime_residue_counts_mod_24": dict(
            sorted(terminal_residue_counts.items(), key=lambda item: int(item[0]))
        ),
        "maximum_selected_terminal_prime": max(
            (int(record["terminal_prime"]) for record in records), default=None
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_closure(
        json.loads(args.h19.read_text(encoding="utf-8")), args.gap_cap, args.b_cap
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
