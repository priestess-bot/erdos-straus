#!/usr/bin/env python3
"""Rewrite every H19-k23 1048576-layer ordinary descent through the global tail menu."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-1048576.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
CANONICAL = ROOT / "reproductions" / "h19_k23_canonical_tail_support_defect_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_module("h19_k23_global_tail_closure_branches", BRANCHES)
canonical = load_module("h19_k23_global_tail_closure_canonical", CANONICAL)


def global_tail_bases() -> tuple[int, dict[int, set[int]]]:
    """Return G and the maximal affine base for every globally available tail."""
    branches = boundary.remaining_branches()
    forms = [branch["prime_form"] for branch in branches]
    coefficients = {int(form["coefficient"]) for form in forms}
    if len(coefficients) != 1:
        raise AssertionError("residual branches do not have one common coefficient")
    coefficient = coefficients.pop()
    global_factor = math.gcd(
        coefficient, *(int(form["constant"]) - 1 for form in forms)
    )
    bases: dict[int, set[int]] = {}
    for denominator in sympy.divisors(global_factor):
        if denominator % 4:
            continue
        gap = denominator - 1
        q = denominator // 4
        slope = coefficient // denominator
        intercepts = [(int(form["constant"]) + gap) // denominator for form in forms]
        uniform_u_factor = math.gcd(slope, *intercepts)
        bases[gap] = {int(prime) for prime in sympy.factorint(q * uniform_u_factor)}
    return global_factor, bases


def first_global_support_two_tail(
    prime: int, start_gap: int, bases: dict[int, set[int]], max_support: int
) -> tuple[int, dict[str, int]] | None:
    """Find the first global tail at or above start_gap with canonical defect at most k."""
    for gap in sorted(gap for gap in bases if gap >= start_gap):
        witness = canonical.support_defect(prime, gap, bases[gap], max_support)
        if witness is not None:
            return gap, witness
    return None


def run_audit(payload: dict[str, object], max_support: int = 2) -> dict[str, object]:
    """Keep direct global rows and rewrite every other ordinary-tail row globally."""
    global_factor, bases = global_tail_bases()
    direct_global_count = 0
    direct_global_gaps: Counter[int] = Counter()
    replacement_origin_gaps: Counter[int] = Counter()
    replacement_tail_gaps: Counter[int] = Counter()
    replacement_defects: Counter[int] = Counter()
    replacements = []
    misses = []
    for record in payload["records"]:
        prime = int(record["prime"])
        shared_gap = int(record["shared_selector_gap"])
        route = str(record["route"])
        if route == "shared-gap" and shared_gap in bases:
            direct_global_count += 1
            direct_global_gaps[shared_gap] += 1
            continue
        if route == "shared-gap":
            start_gap = shared_gap
            origin = "direct-nonglobal-shared-gap"
        elif route == "alternative-p-minus-one-gap":
            stored = record["tail_witness"]
            if stored is None:
                raise AssertionError("alternative route is missing its ordinary tail witness")
            start_gap = int(stored["gap"])
            origin = "alternative-tail"
        else:
            raise AssertionError("unknown ordinary-tail route")
        selected = first_global_support_two_tail(prime, start_gap, bases, max_support)
        if selected is None:
            misses.append({"prime": prime, "shared_selector_gap": shared_gap, "start_gap": start_gap})
            continue
        gap, witness = selected
        replacement_origin_gaps[shared_gap] += 1
        replacement_tail_gaps[gap] += 1
        replacement_defects[int(witness["defect"])] += 1
        replacements.append(
            {
                "prime": prime,
                "origin": origin,
                "shared_selector_gap": shared_gap,
                "start_tail_gap": start_gap,
                "global_tail_gap": gap,
                "base_primes": sorted(bases[gap]),
                "support_defect": int(witness["defect"]),
                "divisor": int(witness["divisor"]),
            }
        )
    if direct_global_count + len(replacements) + len(misses) != len(payload["records"]):
        raise AssertionError("global-tail classification did not partition the input")
    return {
        "arithmetic": (
            "the existing exact ordinary-tail closure is retained for shared gaps whose "
            "denominator divides G; every remaining row receives an exhaustive canonical "
            "support search over the complete sorted global-tail menu, with exact "
            "square-root-completion verification"
        ),
        "scope_note": (
            "A complete finite rewrite of the supplied 1048576-layer H19-k23 closure. "
            "It does not prove that the global menu covers all parameters or all core primes."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "input_record_count": len(payload["records"]),
        "global_p_minus_one_factor": global_factor,
        "global_tail_count": len(bases),
        "direct_global_tail_count": direct_global_count,
        "direct_global_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(direct_global_gaps.items())
        },
        "rewritten_global_tail_count": len(replacements),
        "rewrite_origin_shared_gap_histogram": {
            str(gap): count for gap, count in sorted(replacement_origin_gaps.items())
        },
        "rewrite_global_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(replacement_tail_gaps.items())
        },
        "rewrite_support_defect_histogram": {
            str(defect): count for defect, count in sorted(replacement_defects.items())
        },
        "global_tail_misses": misses,
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
    print(json.dumps({key: value for key, value in result.items() if key != "replacements"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
