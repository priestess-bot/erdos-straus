#!/usr/bin/env python3
"""Build a Dickson escape from the complete distance-five even-source fan."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-c5-even-source-conditional-escape-2097152.json"
BOUNDARY = ROOT / "reproductions" / "h19_k23_pressure_even_source_polynomial_boundary.py"
TARGET_SEED = 748_375_048_866_405_601
DISTANCE = 5


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_module("h19_k23_c5_even_source_boundary", BOUNDARY)


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


def subtract(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def scale(factor: int, value):
    return tuple(factor * entry for entry in value)


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


def audit_state(label: str, p, shift: int, s, k, r) -> tuple[dict[str, object], tuple[int, int]]:
    """Audit one compatible c=5 source shift and return its new prime form."""
    m1 = boundary.multiply(s, k)
    if scale(shift, s) != subtract(p, (DISTANCE, 0, 0)):
        raise AssertionError(f"source denominator factorization is inconsistent on {label}")
    if scale(4 * DISTANCE, k) != subtract(p, (shift, 0, 0)):
        raise AssertionError(f"c=5 k relation is inconsistent on {label}")
    if scale(DISTANCE * shift, r) != subtract(subtract(p, (shift, 0, 0)), (DISTANCE, 0, 0)):
        raise AssertionError(f"c=5 r relation is inconsistent on {label}")
    if scale(4 * DISTANCE * shift, m1) != boundary.multiply(subtract(p, (shift, 0, 0)), subtract(p, (DISTANCE, 0, 0))):
        raise AssertionError(f"strict-lift product identity is inconsistent on {label}")
    content, q = boundary.divide_content(k)
    candidate_count = 0
    linear_remainder_max = 0
    for _, total in candidate_totals(s, k):
        candidate_count += 1
        if boundary.divisible_by(total, r):
            raise AssertionError(f"uniform polynomial tail survived on {label}")
        remainder = (
            total[2] * r[0] * r[0]
            - total[1] * r[0] * r[1]
            + total[0] * r[1] * r[1]
        )
        if remainder == 0:
            raise AssertionError(f"linear-r state has a uniform tail on {label}")
        linear_remainder_max = max(linear_remainder_max, abs(remainder))
    return (
        {
            "label": label,
            "shift": shift,
            "r_degree": boundary.degree(r),
            "m1_degree": boundary.degree(m1),
            "k_fixed_content": content,
            "eventual_polynomial_candidate_count": candidate_count,
            "maximum_nonzero_linear_remainder": linear_remainder_max,
        },
        (q[1], q[0]),
    )


def compatible_shift_labels(base: int, ell) -> list[str]:
    """Enumerate d=a and d=a*ell under the conditional ell-prime factorization."""
    result = []
    for divisor in sympy.divisors(base):
        divisor = int(divisor)
        if (
            (TARGET_SEED - divisor) % (4 * DISTANCE) == 0
            and (base * ell[1]) % (4 * DISTANCE) == 0
            and (base // divisor * ell[0] - 1) % DISTANCE == 0
            and (base // divisor * ell[1]) % DISTANCE == 0
        ):
            result.append(f"d={divisor}")
        if (
            (base // divisor - 1) % DISTANCE == 0
            and (TARGET_SEED - divisor * ell[0]) % (4 * DISTANCE) == 0
            and ((base - divisor) * ell[1]) % (4 * DISTANCE) == 0
        ):
            result.append(f"d={divisor}*ell")
    return result


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile the complete c=5 even-source fan into a Dickson escape tuple."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    base = math.gcd(prime - DISTANCE, coefficient)
    p = (prime, coefficient, 0)
    ell = ((prime - DISTANCE) // base, coefficient // base, 0)
    if base != 10004 or boundary.degree(ell) != 1 or math.gcd(ell[0], ell[1]) != 1:
        raise AssertionError("unexpected distance-five factorization")
    labels = compatible_shift_labels(base, ell)
    expected_labels = ["d=1", "d=41", "d=61", "d=2501"]
    if labels != expected_labels:
        raise AssertionError(f"unexpected complete shift fan {labels}")

    state_rows = []
    new_forms = []
    for shift in (1, 41, 61, 2501):
        s = ((prime - DISTANCE) // shift, coefficient // shift, 0)
        k = ((prime - shift) // (4 * DISTANCE), coefficient // (4 * DISTANCE), 0)
        r = ((s[0] - 1) // DISTANCE, s[1] // DISTANCE, 0)
        state, q_form = audit_state(f"d={shift}", p, shift, s, k, r)
        state_rows.append(state)
        new_forms.append(q_form)
    forms = [(p[1], p[0]), (ell[1], ell[0]), *new_forms]
    if len(set(forms)) != len(forms):
        raise AssertionError("c=5 prime forms unexpectedly collide")
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("c=5 prime tuple is locally obstructed")
    return {
        "arithmetic": (
            "p-5=10004*ell and the exact c=5 source congruences leave exactly four "
            "shifts d=1,41,61,2501 when ell is prime; every resulting M1^2 factor "
            "pattern is enumerated from its fixed content and two primitive linear factors"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of p,ell and the four displayed k cofactors escape the complete "
            "distance-five even-source fan. This does not exclude other odd distances or "
            "other descent families."
        ),
        "seed_prime": prime,
        "p_minus_five_base_factor": base,
        "distance": DISTANCE,
        "compatible_shift_labels": labels,
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "label": label}
            for form, label in zip(forms, ("p", "ell", "q_d1", "q_d41", "q_d61", "q_d2501"))
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
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in {"form_labels", "state_rows"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
