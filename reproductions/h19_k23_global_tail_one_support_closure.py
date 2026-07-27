#!/usr/bin/env python3
"""Eliminate every support-two row in the H19-k23 global-tail closure by later tails."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-1048576.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
CANONICAL = ROOT / "reproductions" / "h19_k23_canonical_tail_support_defect_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_global_tail_one_support_menu", GLOBAL_CLOSURE)
canonical = load_module("h19_k23_global_tail_one_support_canonical", CANONICAL)


def first_later_one_support_tail(
    prime: int, current_gap: int, bases: dict[int, set[int]]
) -> tuple[int, dict[str, int]] | None:
    """Find the first strictly later global tail with canonical support at most one."""
    for gap in sorted(gap for gap in bases if gap > current_gap):
        witness = canonical.support_defect(prime, gap, bases[gap], 1)
        if witness is not None:
            return gap, witness
    return None


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Keep support-zero/one rows and reroute every support-two row globally."""
    global_factor, bases = global_closure.global_tail_bases()
    retained = []
    reroutes = []
    final_tail_histogram: Counter[int] = Counter()
    final_support_histogram: Counter[int] = Counter()
    for record in payload["replacements"]:
        prime = int(record["prime"])
        old_gap = int(record["global_tail_gap"])
        old_support = int(record["support_defect"])
        if old_support <= 1:
            final_tail_histogram[old_gap] += 1
            final_support_histogram[old_support] += 1
            retained.append(record)
            continue
        if old_support != 2:
            raise AssertionError("input global closure exceeded the audited support bound")
        selected = first_later_one_support_tail(prime, old_gap, bases)
        if selected is None:
            raise AssertionError("support-two row has no later one-support global tail")
        gap, witness = selected
        final_tail_histogram[gap] += 1
        final_support_histogram[int(witness["defect"])] += 1
        reroutes.append(
            {
                "prime": prime,
                "shared_selector_gap": int(record["shared_selector_gap"]),
                "old_global_tail_gap": old_gap,
                "old_support_defect": old_support,
                "new_global_tail_gap": gap,
                "new_base_primes": sorted(bases[gap]),
                "new_support_defect": int(witness["defect"]),
                "new_divisor": int(witness["divisor"]),
            }
        )
    if len(retained) + len(reroutes) != len(payload["replacements"]):
        raise AssertionError("one-support closure did not partition the rewrites")
    if any(int(row["new_support_defect"]) > 1 for row in reroutes):
        raise AssertionError("reroute exceeded support one")
    return {
        "arithmetic": (
            "each support-two global witness is followed through the sorted complete "
            "global-tail menu; later tails exhaust canonical support zero and one product "
            "sets, with exact square-root-completion verification"
        ),
        "scope_note": (
            "A finite support-improving reroute of the supplied 1048576-layer global "
            "closure. It does not prove a global one-support selector."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "input_record_count": payload["input_record_count"],
        "direct_global_tail_count": payload["direct_global_tail_count"],
        "global_p_minus_one_factor": global_factor,
        "input_rewrite_count": len(payload["replacements"]),
        "retained_support_zero_or_one_count": len(retained),
        "rerouted_support_two_count": len(reroutes),
        "final_rewrite_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(final_tail_histogram.items())
        },
        "final_rewrite_support_histogram": {
            str(support): count for support, count in sorted(final_support_histogram.items())
        },
        "reroutes": reroutes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "reroutes"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
