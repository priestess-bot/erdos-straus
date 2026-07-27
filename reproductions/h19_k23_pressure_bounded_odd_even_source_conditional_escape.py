#!/usr/bin/env python3
"""Build a joint Dickson escape from all odd c<=99 standard even-source fans."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-bounded-odd-even-source-conditional-escape-2097152.json"
BOUNDARY = ROOT / "reproductions" / "h19_k23_pressure_even_source_polynomial_boundary.py"
TARGET_SEED = 748_375_048_866_405_601
MAX_DISTANCE = 99


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_module("h19_k23_bounded_odd_even_source_boundary", BOUNDARY)


def subtract(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def scale(factor: int, value):
    return tuple(factor * entry for entry in value)


def divide_linear(value, divisor: int):
    if any(entry % divisor for entry in value):
        return None
    return tuple(entry // divisor for entry in value)


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check primitive local admissibility of a finite affine prime tuple."""
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


def candidate_totals(s, k):
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


def audit_state(distance: int, label: str, p, shift, s, k, r):
    """Validate one source identity and exhaust its square-tail factor patterns."""
    m1 = boundary.multiply(s, k)
    if boundary.multiply(shift, s) != subtract(p, (distance, 0, 0)):
        raise AssertionError(f"source denominator factorization is inconsistent on c={distance}, {label}")
    if scale(4 * distance, k) != subtract(p, shift):
        raise AssertionError(f"k relation is inconsistent on c={distance}, {label}")
    if scale(distance, boundary.multiply(shift, r)) != subtract(subtract(p, shift), (distance, 0, 0)):
        raise AssertionError(f"r relation is inconsistent on c={distance}, {label}")
    if scale(4 * distance, boundary.multiply(shift, m1)) != boundary.multiply(subtract(p, shift), subtract(p, (distance, 0, 0))):
        raise AssertionError(f"strict-lift product identity is inconsistent on c={distance}, {label}")
    candidate_count = 0
    linear_remainder_max = 0
    constant_r_pointwise = True
    for _, total in candidate_totals(s, k):
        candidate_count += 1
        if boundary.divisible_by(total, r):
            raise AssertionError(f"uniform polynomial tail survived on c={distance}, {label}")
        if boundary.degree(r) == 0:
            if any(coefficient % r[0] for coefficient in total[1:]) or total[0] % r[0] == 0:
                constant_r_pointwise = False
        else:
            remainder = (
                total[2] * r[0] * r[0]
                - total[1] * r[0] * r[1]
                + total[0] * r[1] * r[1]
            )
            if remainder == 0:
                raise AssertionError(f"linear-r state has a uniform tail on c={distance}, {label}")
            linear_remainder_max = max(linear_remainder_max, abs(remainder))
    if boundary.degree(r) == 0 and not constant_r_pointwise:
        raise AssertionError(f"constant-r state is not pointwise closed on c={distance}, {label}")
    forms = []
    for factor, factor_label in ((s, "s"), (k, "k")):
        if boundary.degree(factor) > 0:
            _, primitive = boundary.divide_content(factor)
            forms.append(((primitive[1], primitive[0]), f"c={distance},{label},{factor_label}"))
    return {
        "label": label,
        "r_degree": boundary.degree(r),
        "m1_degree": boundary.degree(m1),
        "eventual_polynomial_candidate_count": candidate_count,
        "constant_r_pointwise_closed": constant_r_pointwise,
        "maximum_nonzero_linear_remainder": linear_remainder_max,
    }, forms


def distance_states(distance: int, p, base: int, ell):
    """List all shifts d=a or d=a*ell under p-c=base*ell with ell prime."""
    for divisor in sympy.divisors(base):
        divisor = int(divisor)
        shift = (divisor, 0, 0)
        s = scale(base // divisor, ell)
        k = divide_linear(subtract(p, shift), 4 * distance)
        r = divide_linear(subtract(s, (1, 0, 0)), distance)
        if k is not None and r is not None:
            yield f"d={divisor}", shift, s, k, r
        shift = scale(divisor, ell)
        s = (base // divisor, 0, 0)
        k = divide_linear(subtract(p, shift), 4 * distance)
        r = divide_linear(subtract(s, (1, 0, 0)), distance)
        if k is not None and r is not None:
            yield f"d={divisor}*ell", shift, s, k, r


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Build one conditional prime tuple escaping every odd c<=99 source fan."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    p = (prime, coefficient, 0)
    form_labels: dict[tuple[int, int], list[str]] = {(coefficient, prime): ["p"]}
    distance_rows = []
    raw_form_count = 1
    for distance in range(1, MAX_DISTANCE + 1, 2):
        base = math.gcd(prime - distance, coefficient)
        ell = ((prime - distance) // base, coefficient // base, 0)
        if boundary.multiply((base, 0, 0), ell) != subtract(p, (distance, 0, 0)):
            raise AssertionError(f"p-c factorization failed at c={distance}")
        if math.gcd(ell[0], ell[1]) != 1:
            raise AssertionError(f"nonprimitive quotient at c={distance}")
        ell_form = (ell[1], ell[0])
        form_labels.setdefault(ell_form, []).append(f"c={distance}:ell")
        raw_form_count += 1
        state_rows = []
        for label, shift, s, k, r in distance_states(distance, p, base, ell):
            state, forms = audit_state(distance, label, p, shift, s, k, r)
            state_rows.append(state)
            for form, form_label in forms:
                form_labels.setdefault(form, []).append(form_label)
                raw_form_count += 1
        distance_rows.append(
            {
                "distance": distance,
                "p_minus_c_base_factor": base,
                "compatible_ray_count": len(state_rows),
                "eventual_polynomial_candidate_count": sum(int(item["eventual_polynomial_candidate_count"]) for item in state_rows),
                "state_rows": state_rows,
            }
        )
    forms = list(form_labels)
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("bounded odd-distance joint prime tuple is locally obstructed")
    return {
        "arithmetic": (
            "for every odd c<=99, p-c=B_c*ell_c is reduced to one primitive linear "
            "factor; assuming all ell_c and residual tail factors prime, every divisor is "
            "of the form a or a*ell_c and the complete compatible source fan is enumerated"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of the displayed tuple escape all standard even-source fans at "
            "odd distances c<=99. This does not exclude unbounded distances or other descent families."
        ),
        "seed_prime": prime,
        "maximum_odd_distance": MAX_DISTANCE,
        "distance_count": len(distance_rows),
        "nonempty_distance_count": sum(bool(row["compatible_ray_count"]) for row in distance_rows),
        "total_compatible_ray_count": sum(int(row["compatible_ray_count"]) for row in distance_rows),
        "total_eventual_polynomial_candidate_count": sum(int(row["eventual_polynomial_candidate_count"]) for row in distance_rows),
        "raw_affine_prime_form_count": raw_form_count,
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "distance_rows": distance_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "labels": labels}
            for form, labels in form_labels.items()
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
    print(json.dumps({key: value for key, value in result.items() if key not in {"distance_rows", "form_labels"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
