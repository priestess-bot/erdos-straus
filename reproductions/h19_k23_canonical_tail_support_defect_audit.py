#!/usr/bin/env python3
"""Audit canonical support defects on the H19-k23 m=27 alternative-tail chain."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-1048576.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-canonical-tail-support-defect-1048576.json"
INVARIANTS = ROOT / "reproductions" / "h19_k23_uniform_tail_base_invariants.py"
DEFECT = ROOT / "reproductions" / "type_ii_tail_support_defect.py"
M27 = 27


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base_invariants = load_module("h19_k23_tail_base_invariants", INVARIANTS)
support = load_module("h19_k23_tail_support_defect", DEFECT)


def canonical_bases() -> dict[int, tuple[set[int], str]]:
    """Use the maximal global affine base, or q alone when no global tail exists."""
    rows = {
        int(row["tail_gap"]): row
        for row in base_invariants.run_audit()["tail_invariants"]
    }
    bases: dict[int, tuple[set[int], str]] = {}
    for gap, row in rows.items():
        q = int(row["q"])
        if bool(row["globally_available"]):
            bases[gap] = (
                {int(prime) for prime in row["canonical_base_primes"]},
                "maximal-global-affine",
            )
        else:
            bases[gap] = (
                {int(prime) for prime in sympy.factorint(q)},
                "q-only-nonuniform-tail",
            )
    return bases


def support_defect(
    prime: int, gap: int, base_primes: set[int], max_support: int = 2
) -> dict[str, int] | None:
    """Return the exact minimum defect when it is at most ``max_support``."""
    q, remainder = divmod(gap + 1, 4)
    if remainder:
        raise ValueError("tail gap is not 3 modulo 4")
    if (prime - 1) % (gap + 1):
        raise ValueError("tail gap is not an ordinary p-1 tail")
    u = (prime + gap) // (gap + 1)
    if 4 * q * u != prime + gap:
        raise AssertionError("tail normalization is not integral")
    for defect in range(max_support + 1):
        witness = support.support_witness(q, u, base_primes, defect)
        if witness is not None:
            return {
                "defect": defect,
                "divisor": int(witness["divisor"]),
                "q": q,
                "u": u,
            }
    return None


def run_audit(payload: dict[str, object], max_support: int = 2) -> dict[str, object]:
    """Recompute the minimum canonical defect at every first m=27 alternative tail."""
    bases = canonical_bases()
    records = []
    misses = []
    by_gap: dict[int, Counter[int]] = {}
    selected = 0
    for record in payload["records"]:
        if (
            int(record["shared_selector_gap"]) != M27
            or record["route"] != "alternative-p-minus-one-gap"
        ):
            continue
        selected += 1
        prime = int(record["prime"])
        stored = record["tail_witness"]
        if stored is None:
            raise AssertionError("ordinary-tail closure record is missing its witness")
        gap = int(stored["gap"])
        if gap not in bases:
            raise AssertionError(f"tail gap {gap} has no canonical base declaration")
        base_primes, base_origin = bases[gap]
        witness = support_defect(prime, gap, base_primes, max_support)
        if witness is None:
            misses.append({"prime": prime, "tail_gap": gap})
            continue
        by_gap.setdefault(gap, Counter())[int(witness["defect"])] += 1
        records.append(
            {
                "prime": prime,
                "tail_gap": gap,
                "base_primes": sorted(base_primes),
                "base_origin": base_origin,
                "support_defect": int(witness["defect"]),
                "divisor": int(witness["divisor"]),
            }
        )
    if selected != len(records) + len(misses):
        raise AssertionError("m=27 alternative records were not partitioned")
    return {
        "arithmetic": (
            "maximal global affine bases where available, q-only base for the nonuniform "
            "m=63 tail, exhaustive base-times-new-prime-power product enumeration through "
            "the stated defect bound, and exact square-root-completion verification"
        ),
        "scope_note": (
            "A finite audit of first ordinary tails for m=27 alternative records. It does "
            "not prove a cross-gap support-defect law outside this H19-k23 artifact."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "max_support_checked": max_support,
        "m27_alternative_record_count": selected,
        "canonical_support_defect_count": len(records),
        "support_defect_misses": misses,
        "support_defect_histogram_by_tail_gap": {
            str(gap): {str(defect): count for defect, count in sorted(counts.items())}
            for gap, counts in sorted(by_gap.items())
        },
        "records": records,
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
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
