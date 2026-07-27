#!/usr/bin/env python3
"""Build a Dickson escape from the complete distance-three even-source fan."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-c3-even-source-conditional-escape-2097152.json"
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


boundary = load_module("h19_k23_c3_even_source_boundary", BOUNDARY)


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check the finite prime tuple's primitive local admissibility."""
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


def candidate_totals(s, k, r):
    """Yield every eventual square-tail divisor pattern of M=s*k."""
    m1 = boundary.multiply(s, k)
    variable_factors = [factor for factor in (s, k) if boundary.degree(factor) > 0]
    constant_content = math.prod(abs(factor[0]) for factor in (s, k) if boundary.degree(factor) == 0)
    contents_and_primitives = [boundary.divide_content(factor) for factor in variable_factors]
    content = constant_content * math.prod(item[0] for item in contents_and_primitives)
    primitives = [item[1] for item in contents_and_primitives]
    for constant_factor in sympy.divisors(content * content):
        for powers in itertools.product(range(3), repeat=len(primitives)):
            if sum(powers) > boundary.degree(m1):
                continue
            candidate = (int(constant_factor), 0, 0)
            for primitive, exponent in zip(primitives, powers):
                candidate = boundary.multiply(candidate, boundary.power(primitive, exponent))
            if boundary.eventually_at_most(candidate, m1):
                yield candidate, tuple(m1[index] + candidate[index] for index in range(3))


def subtract(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def scale(factor: int, value):
    return tuple(factor * entry for entry in value)


def audit_state(label: str, p, shift: tuple[int, int, int], s, k, r) -> dict[str, object]:
    """Audit one compatible c=3 source shift exactly at the polynomial level."""
    m1 = boundary.multiply(s, k)
    if boundary.multiply(shift, s) != subtract(p, (3, 0, 0)):
        raise AssertionError(f"source denominator factorization is inconsistent on {label}")
    if scale(12, k) != subtract(p, shift):
        raise AssertionError(f"c=3 k relation is inconsistent on {label}")
    if scale(3, boundary.multiply(shift, r)) != subtract(subtract(p, shift), (3, 0, 0)):
        raise AssertionError(f"c=3 r relation is inconsistent on {label}")
    if scale(12, boundary.multiply(shift, m1)) != boundary.multiply(subtract(p, shift), subtract(p, (3, 0, 0))):
        raise AssertionError(f"strict-lift product identity is inconsistent on {label}")
    candidate_count = 0
    linear_remainder_max = 0
    constant_r_moving_coefficients_divisible = True
    for _, total in candidate_totals(s, k, r):
        candidate_count += 1
        if boundary.divisible_by(total, r):
            raise AssertionError(f"uniform polynomial tail survived on {label}")
        if boundary.degree(r) == 0:
            if any(coefficient % r[0] for coefficient in total[1:]):
                constant_r_moving_coefficients_divisible = False
            if total[0] % r[0] == 0:
                raise AssertionError(f"constant-r state has a pointwise tail on {label}")
        else:
            remainder = (
                total[2] * r[0] * r[0]
                - total[1] * r[0] * r[1]
                + total[0] * r[1] * r[1]
            )
            if remainder == 0:
                raise AssertionError(f"linear-r state has a uniform tail on {label}")
            linear_remainder_max = max(linear_remainder_max, abs(remainder))
    if boundary.degree(r) == 0 and not constant_r_moving_coefficients_divisible:
        raise AssertionError(f"constant-r state is not pointwise fixed on {label}")
    return {
        "label": label,
        "shift_degree": boundary.degree(shift),
        "r_degree": boundary.degree(r),
        "m1_degree": boundary.degree(m1),
        "eventual_polynomial_candidate_count": candidate_count,
        "constant_r_moving_coefficients_divisible": constant_r_moving_coefficients_divisible,
        "maximum_nonzero_linear_remainder": linear_remainder_max,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile the complete c=3 even-source fan into a Dickson escape tuple."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    base = math.gcd(prime - 1, coefficient)
    h = ((prime - 1) // base, coefficient // base, 0)
    if base != 165600 or h[0] % 4 != 1 or h[1] % 4:
        raise AssertionError("unexpected pressure-ray normalization")

    # p-3=22*ell.  Under ell prime, d|p-3 and 12|(p-d) leave d=1, ell only.
    ell = ((82800 * h[0] - 1) // 11, 82800 * h[1] // 11, 0)
    q = ((144900 * h[0] + 1) // 121, 144900 * h[1] // 121, 0)
    p = (prime, coefficient, 0)
    if any(value % 1 for value in (*ell, *q)):
        raise AssertionError("nonintegral c=3 prime form")
    if boundary.multiply((22, 0, 0), ell) != (p[0] - 3, p[1], 0):
        raise AssertionError("p-3 factorization is inconsistent")
    if boundary.multiply((11, 0, 0), q) != (
        (p[0] - ell[0]) // 12,
        (p[1] - ell[1]) // 12,
        0,
    ):
        raise AssertionError("shift-ell k factorization is inconsistent")
    if ell[0] % 12 != 1 or ell[1] % 12:
        raise AssertionError("ell does not give the claimed compatible-shift list")

    states = [
        audit_state(
            "d=1",
            p,
            (1, 0, 0),
            boundary.multiply((22, 0, 0), ell),
            boundary.multiply((13800, 0, 0), h),
            (55200 * h[0] - 1, 55200 * h[1], 0),
        ),
        audit_state(
            "d=ell",
            p,
            ell,
            (22, 0, 0),
            boundary.multiply((11, 0, 0), q),
            (7, 0, 0),
        ),
    ]
    forms = [(p[1], p[0]), (h[1], h[0]), (ell[1], ell[0]), (q[1], q[0])]
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("c=3 prime tuple is locally obstructed")
    return {
        "arithmetic": (
            "p-3=22*ell and 12 divides p-d leave exactly d=1 and d=ell when ell "
            "is prime. Their tail products are 303600*h*ell and 242*q respectively; "
            "every eventual square divisor pattern is enumerated from these factorizations"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of p,h,ell,q escape the complete distance-three even-source fan. "
            "This does not exclude other odd distances or other descent families."
        ),
        "seed_prime": prime,
        "p_minus_one_base_factor": base,
        "distance": 3,
        "compatible_shift_labels": [state["label"] for state in states],
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "label": label}
            for form, label in zip(forms, ("p", "h", "ell", "q"))
        ],
        "state_rows": states,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in {"form_labels", "state_rows"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
