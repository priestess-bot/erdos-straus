#!/usr/bin/env python3
"""Build a joint Dickson escape from the complete c=1,3,5 even-source fans."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-c1-c3-c5-joint-even-source-conditional-escape-2097152.json"


def load_module(name: str, filename: str):
    path = ROOT / "reproductions" / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


c1 = load_module("h19_k23_joint_c1", "h19_k23_pressure_full_even_source_conditional_escape.py")
c3 = load_module("h19_k23_joint_c3", "h19_k23_pressure_c3_even_source_conditional_escape.py")
c5 = load_module("h19_k23_joint_c5", "h19_k23_pressure_c5_even_source_conditional_escape.py")


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check local admissibility of the deduplicated simultaneous prime tuple."""
    if any(coefficient <= 0 or constant <= 0 or math.gcd(coefficient, constant) != 1 for coefficient, constant in forms):
        return False, []
    rows = []
    for prime in sympy.primerange(2, len(forms) + 1):
        roots = set()
        for coefficient, constant in forms:
            if coefficient % prime:
                roots.add((-constant * pow(coefficient, -1, prime)) % prime)
            elif constant % prime == 0:
                return False, []
        rows.append({"prime": int(prime), "root_count": len(roots)})
        if len(roots) == prime:
            return False, rows
    return True, rows


def form_entries(distance: int, result: dict[str, object]):
    for row in result["form_labels"]:
        labels = row.get("labels")
        if labels is None:
            labels = [row["label"]]
        yield (int(row["coefficient"]), int(row["constant"])), [f"c={distance}:{label}" for label in labels]


def component_summary(distance: int, result: dict[str, object]) -> dict[str, int]:
    states = result["state_rows"]
    return {
        "distance": distance,
        "ray_count": len(states),
        "eventual_polynomial_candidate_count": sum(int(row["eventual_polynomial_candidate_count"]) for row in states),
        "raw_affine_prime_form_count": len(result["form_labels"]),
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Re-run all three complete-fan audits and test their joint prime tuple."""
    components = [(1, c1.run_audit(payload)), (3, c3.run_audit(payload)), (5, c5.run_audit(payload))]
    combined_labels: dict[tuple[int, int], list[str]] = {}
    raw_count = 0
    for distance, result in components:
        for form, labels in form_entries(distance, result):
            raw_count += 1
            combined_labels.setdefault(form, []).extend(labels)
    forms = list(combined_labels)
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("joint c=1,3,5 prime tuple is locally obstructed")
    return {
        "arithmetic": (
            "the complete c=1, c=3, and c=5 fan audits are re-run from the same pressure "
            "input; their required primitive linear factors are deduplicated before one "
            "simultaneous Dickson local-admissibility check"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of this joint tuple escape all complete c=1, c=3, and c=5 "
            "even-source fans at once. This does not exclude other distances or descent families."
        ),
        "seed_prime": c1.TARGET_SEED,
        "distances": [distance for distance, _ in components],
        "component_rows": [component_summary(distance, result) for distance, result in components],
        "raw_affine_prime_form_count": raw_count,
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "labels": labels}
            for form, labels in combined_labels.items()
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "form_labels"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
