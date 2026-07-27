#!/usr/bin/env python3
"""Build a Dickson escape from the complete distance-one even-source fan."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-full-even-source-conditional-escape-2097152.json"
BOUNDARY = ROOT / "reproductions" / "h19_k23_pressure_even_source_polynomial_boundary.py"
TARGET_SEED = 748_375_048_866_405_601


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_module("h19_k23_full_even_source_boundary", BOUNDARY)


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check local admissibility for the finite prime tuple."""
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


def state_candidates(s, k, r):
    """Yield all eventual polynomial divisors of M1^2 with their total polynomial."""
    m1 = boundary.multiply(s, k)
    source_factors = [factor for factor in (s, k) if boundary.degree(factor) > 0]
    constant_content = math.prod(
        abs(factor[0]) for factor in (s, k) if boundary.degree(factor) == 0
    )
    contents_and_primitives = [boundary.divide_content(factor) for factor in source_factors]
    content = constant_content * math.prod(item[0] for item in contents_and_primitives)
    primitives = [item[1] for item in contents_and_primitives]
    for constant_factor in sympy.divisors(content * content):
        for powers in itertools.product(range(3), repeat=len(primitives)):
            if sum(powers) > boundary.degree(m1):
                continue
            candidate = (int(constant_factor), 0, 0)
            for primitive, exponent in zip(primitives, powers):
                candidate = boundary.multiply(candidate, boundary.power(primitive, exponent))
            if not boundary.eventually_at_most(candidate, m1):
                continue
            yield candidate, tuple(m1[index] + candidate[index] for index in range(3))


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile every c=1 ray into one prime-factor conditional escape tuple."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    base = math.gcd(prime - 1, coefficient)
    h = ((prime - 1) // base, coefficient // base, 0)
    form_labels: dict[tuple[int, int], list[str]] = {
        (coefficient, prime): ["p"],
        (h[1], h[0]): ["h"],
    }
    state_rows = []
    for divisor in sympy.divisors(base):
        divisor = int(divisor)
        if divisor % 4 != 1:
            continue
        for uses_h in (False, True):
            s, k, r = boundary.state_polynomials(base, h, divisor, uses_h)
            for name, factor in (("s", s), ("k", k)):
                if boundary.degree(factor) == 0:
                    continue
                _, primitive = boundary.divide_content(factor)
                form_labels.setdefault((primitive[1], primitive[0]), []).append(
                    f"d={divisor},uses_h={uses_h},{name}"
                )
            candidate_count = 0
            linear_remainder_max = 0
            for _, total in state_candidates(s, k, r):
                candidate_count += 1
                if boundary.divisible_by(total, r):
                    raise AssertionError("uniform polynomial tail survived")
                if boundary.degree(r) == 0:
                    # In this state all variable primitive-factor slopes are r-multiples,
                    # so polynomial nondivisibility is also pointwise nondivisibility.
                    if any(coefficient % r[0] for coefficient in total[1:]):
                        raise AssertionError("constant-r state has a moving residue")
                    if total[0] % r[0] == 0:
                        raise AssertionError("constant-r state has a pointwise witness")
                else:
                    remainder = (
                        total[2] * r[0] * r[0]
                        - total[1] * r[0] * r[1]
                        + total[0] * r[1] * r[1]
                    )
                    if remainder == 0:
                        raise AssertionError("linear-r state has a uniform witness")
                    linear_remainder_max = max(linear_remainder_max, abs(remainder))
            state_rows.append(
                {
                    "shift_base_divisor": divisor,
                    "shift_uses_h": uses_h,
                    "r_degree": boundary.degree(r),
                    "eventual_polynomial_candidate_count": candidate_count,
                    "maximum_nonzero_linear_remainder": linear_remainder_max,
                }
            )
    forms = list(form_labels)
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("complete even-source prime tuple is locally obstructed")
    return {
        "arithmetic": (
            "p-1=B*h and every distance-one shift d or d*h are factorized into fixed "
            "contents and a finite set of primitive linear factors; complete square-tail "
            "patterns are checked exactly, with constant-r states pointwise fixed and "
            "linear-r states leaving only finitely many exceptional parameters"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of the displayed tuple escape the complete distance-one "
            "even-source fan. This does not exclude larger odd distances or other descent "
            "families."
        ),
        "seed_prime": prime,
        "p_minus_one_base_factor": base,
        "distance_one_ray_count": len(state_rows),
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "labels": labels}
            for form, labels in form_labels.items()
        ],
        "state_rows": state_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: value for key, value in result.items() if key not in {"form_labels", "state_rows"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
