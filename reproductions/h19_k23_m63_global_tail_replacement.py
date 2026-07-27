#!/usr/bin/env python3
"""Replace the nonuniform m=63 tails by the next globally available H19-k23 tails."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-canonical-tail-support-defect-1048576.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-m63-global-tail-replacement-1048576.json"
CANONICAL = ROOT / "reproductions" / "h19_k23_canonical_tail_support_defect_audit.py"
INVARIANTS = ROOT / "reproductions" / "h19_k23_uniform_tail_base_invariants.py"
NONUNIFORM_GAP = 63
MAX_REPLACEMENT_GAP = 95


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_module("h19_k23_canonical_defect_for_m63", CANONICAL)
invariants = load_module("h19_k23_invariants_for_m63", INVARIANTS)


def global_tail_factor_and_gaps() -> tuple[int, list[int]]:
    """Return G and every globally available tail strictly between 63 and 95."""
    branches = invariants.load_branches()
    forms = [branch["prime_form"] for branch in branches]
    coefficients = {int(form["coefficient"]) for form in forms}
    if len(coefficients) != 1:
        raise AssertionError("residual branches do not have one common coefficient")
    coefficient = coefficients.pop()
    global_factor = math.gcd(
        coefficient, *(int(form["constant"]) - 1 for form in forms)
    )
    gaps = [
        divisor - 1
        for divisor in sympy.divisors(global_factor)
        if divisor % 4 == 0 and NONUNIFORM_GAP < divisor - 1 <= MAX_REPLACEMENT_GAP
    ]
    return global_factor, gaps


def run_audit(payload: dict[str, object], max_support: int = 2) -> dict[str, object]:
    """Find the first canonical support-bounded global replacement for each m=63 row."""
    global_factor, gaps = global_tail_factor_and_gaps()
    bases = canonical.canonical_bases()
    if any(bases[gap][1] != "maximal-global-affine" for gap in gaps):
        raise AssertionError("global-tail enumeration disagrees with affine base invariants")
    replacements = []
    globalized_by_gap: dict[int, Counter[int]] = {}
    for record in payload["records"]:
        original_gap = int(record["tail_gap"])
        if original_gap != NONUNIFORM_GAP:
            if record["base_origin"] != "maximal-global-affine":
                raise AssertionError("unexpected nonuniform tail outside m=63")
            globalized_by_gap.setdefault(original_gap, Counter())[int(record["support_defect"])] += 1
            continue
        prime = int(record["prime"])
        attempts = []
        chosen = None
        for gap in gaps:
            if (prime - 1) % (gap + 1):
                raise AssertionError("global tail factor did not divide p-1")
            witness = canonical.support_defect(prime, gap, bases[gap][0], max_support)
            attempts.append(
                {
                    "tail_gap": gap,
                    "support_defect": None if witness is None else witness["defect"],
                }
            )
            if witness is not None:
                chosen = (gap, witness)
                break
        if chosen is None:
            raise AssertionError("m=63 row has no bounded global-tail replacement")
        gap, witness = chosen
        replacements.append(
            {
                "prime": prime,
                "original_m63_defect": int(record["support_defect"]),
                "replacement_tail_gap": gap,
                "replacement_base_primes": sorted(bases[gap][0]),
                "replacement_support_defect": int(witness["defect"]),
                "replacement_divisor": int(witness["divisor"]),
                "attempts": attempts,
            }
        )
        globalized_by_gap.setdefault(gap, Counter())[int(witness["defect"])] += 1
    if len(replacements) != 6:
        raise AssertionError("expected six m=63 records in the checked artifact")
    if sum(sum(counts.values()) for counts in globalized_by_gap.values()) != len(payload["records"]):
        raise AssertionError("globalized tail profile did not cover every input record")
    return {
        "arithmetic": (
            "G=gcd(A,C_i-1) exactly enumerates globally available p-1 tails; each "
            "candidate receives an exhaustive canonical support-defect search through "
            "the stated bound and exact square-root-completion verification"
        ),
        "scope_note": (
            "A finite replacement of six nonuniform m=63 rows in the supplied H19-k23 "
            "artifact. It does not prove that the global tail menu always has defect at most two."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "global_p_minus_one_factor": global_factor,
        "global_tail_gaps_after_63_through_95": gaps,
        "max_support_checked": max_support,
        "replacement_count": len(replacements),
        "replacement_tail_gap_histogram": {
            str(gap): sum(1 for row in replacements if row["replacement_tail_gap"] == gap)
            for gap in gaps
            if any(row["replacement_tail_gap"] == gap for row in replacements)
        },
        "replacement_support_defect_histogram": {
            str(defect): sum(
                1 for row in replacements if row["replacement_support_defect"] == defect
            )
            for defect in range(max_support + 1)
            if any(row["replacement_support_defect"] == defect for row in replacements)
        },
        "globalized_record_count": len(payload["records"]),
        "globalized_support_defect_histogram_by_tail_gap": {
            str(gap): {str(defect): count for defect, count in sorted(counts.items())}
            for gap, counts in sorted(globalized_by_gap.items())
        },
        "replacements": replacements,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-support", type=int, default=2)
    args = parser.parse_args()
    if args.max_support < 0:
        raise ValueError("max-support must be nonnegative")
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.max_support)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
