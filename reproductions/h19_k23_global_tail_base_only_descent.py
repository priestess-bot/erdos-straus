#!/usr/bin/env python3
"""Route one-support global witnesses to later base-only tails when possible."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-full-global-tail-closure-1048576.json"
DEFAULT_ONE_SUPPORT = ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-1048576.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-1048576.json"
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


global_closure = load_module("h19_k23_global_tail_base_only_menu", GLOBAL_CLOSURE)
canonical = load_module("h19_k23_global_tail_base_only_canonical", CANONICAL)


def first_later_base_only_tail(
    prime: int, current_gap: int, bases: dict[int, set[int]]
) -> tuple[int, dict[str, int]] | None:
    """Find the first strictly later global tail with zero canonical defect."""
    for gap in sorted(gap for gap in bases if gap > current_gap):
        witness = canonical.support_defect(prime, gap, bases[gap], 0)
        if witness is not None:
            return gap, witness
    return None


def any_base_only_tail(
    prime: int, bases: dict[int, set[int]]
) -> tuple[int, dict[str, int]] | None:
    """Check whether a prime has any zero-defect witness in the full global menu."""
    for gap in sorted(bases):
        witness = canonical.support_defect(prime, gap, bases[gap], 0)
        if witness is not None:
            return gap, witness
    return None


def final_rows(
    global_payload: dict[str, object], one_support_payload: dict[str, object]
) -> list[dict[str, object]]:
    """Replace the original support-two rows by their already-checked later witnesses."""
    reroutes = {
        int(row["prime"]): row for row in one_support_payload["reroutes"]
    }
    rows = []
    for row in global_payload["replacements"]:
        prime = int(row["prime"])
        reroute = reroutes.get(prime)
        if reroute is None:
            rows.append(
                {
                    "prime": prime,
                    "shared_selector_gap": int(row["shared_selector_gap"]),
                    "current_global_tail_gap": int(row["global_tail_gap"]),
                    "current_support_defect": int(row["support_defect"]),
                    "current_divisor": int(row["divisor"]),
                    "source": "retained-one-support-closure",
                }
            )
            continue
        rows.append(
            {
                "prime": prime,
                "shared_selector_gap": int(reroute["shared_selector_gap"]),
                "current_global_tail_gap": int(reroute["new_global_tail_gap"]),
                "current_support_defect": int(reroute["new_support_defect"]),
                "current_divisor": int(reroute["new_divisor"]),
                "source": "support-two-reroute",
            }
        )
    if len(rows) != int(one_support_payload["input_rewrite_count"]):
        raise AssertionError("one-support closure does not cover the global replacements")
    if any(int(row["current_support_defect"]) > 1 for row in rows):
        raise AssertionError("input did not eliminate every support-two row")
    return rows


def run_audit(
    global_payload: dict[str, object], one_support_payload: dict[str, object]
) -> dict[str, object]:
    """Eliminate one-support rows by later base-only tails, retaining the pressure set."""
    global_factor, bases = global_closure.global_tail_bases()
    rows = final_rows(global_payload, one_support_payload)
    base_only_initial = []
    base_only_reroutes = []
    pressure_records = []
    for row in rows:
        prime = int(row["prime"])
        current_gap = int(row["current_global_tail_gap"])
        defect = int(row["current_support_defect"])
        if defect == 0:
            base_only_initial.append(row)
            continue
        selected = first_later_base_only_tail(prime, current_gap, bases)
        if selected is not None:
            gap, witness = selected
            base_only_reroutes.append(
                {
                    **row,
                    "new_global_tail_gap": gap,
                    "new_base_primes": sorted(bases[gap]),
                    "new_support_defect": int(witness["defect"]),
                    "new_divisor": int(witness["divisor"]),
                }
            )
            continue
        if any_base_only_tail(prime, bases) is not None:
            raise AssertionError("a later-base-only miss has an earlier base-only tail")
        pressure_records.append(row)
    if len(base_only_initial) + len(base_only_reroutes) + len(pressure_records) != len(rows):
        raise AssertionError("base-only descent did not partition the one-support closure")
    if any(int(row["new_support_defect"]) != 0 for row in base_only_reroutes):
        raise AssertionError("base-only reroute has positive defect")
    return {
        "arithmetic": (
            "the checked one-support global closure is retained; each remaining support-one "
            "row exhausts every strictly later global tail at canonical support zero, and "
            "each residual exhausts the entire global menu at support zero"
        ),
        "scope_note": (
            "A finite pressure-set audit of the supplied 1048576-layer H19-k23 closure. "
            "It does not establish a general cross-tail base-only descent theorem."
        ),
        "input_parameter_limit_exclusive": global_payload["input_parameter_limit_exclusive"],
        "input_rewrite_count": len(rows),
        "global_p_minus_one_factor": global_factor,
        "initial_base_only_count": len(base_only_initial),
        "input_one_support_count": sum(
            int(row["current_support_defect"]) == 1 for row in rows
        ),
        "later_base_only_reroute_count": len(base_only_reroutes),
        "base_only_rewrite_count": len(base_only_initial) + len(base_only_reroutes),
        "global_base_only_pressure_count": len(pressure_records),
        "base_only_reroutes": base_only_reroutes,
        "global_base_only_pressure_records": pressure_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--one-support", type=Path, default=DEFAULT_ONE_SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    global_payload = json.loads(args.input.read_text(encoding="utf-8"))
    one_support_payload = json.loads(args.one_support.read_text(encoding="utf-8"))
    result = run_audit(global_payload, one_support_payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"base_only_reroutes", "global_base_only_pressure_records"}
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
