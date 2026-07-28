#!/usr/bin/env python3
"""Audit compensated-square B=1 bridges on the m<=999 self-square residual."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-b1-self-square-reselection-profile-600m-m999-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b1-compensated-square-profile-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("b1_compensated_square_landscape", LANDSCAPE)


def compensated_witness(
    prime: int, A: int, C: int, gap: int, R: int, T: int
) -> dict[str, int | bool] | None:
    """Build E=4*C^2*T from a complementary square divisor T of H."""
    H = A * R - 1
    K = C * H
    if (
        prime % 24 != 1
        or gap < 3
        or gap % 4 != 3
        or R < 3
        or R % 4 != 3
        or gap * R != 4 * C + 1
        or prime != 4 * A * C - gap
        or 4 * K != prime * R + 1
        or T <= 0
        or H * H % T
        or T % R != 4 % R
    ):
        return None
    q, remainder = divmod(H - C * T, R)
    if remainder or q <= 0 or q * H % T:
        return None
    E = 4 * C * C * T
    source = 4 * C * q
    source_term = q * H // T
    if (
        E % 2
        or E % R != 1
        or (4 * K * K) % E
        or E > 4 * K - 2 * R
        or source % 2
        or not (2 <= source < prime)
        or Fraction(4, prime)
        != Fraction(1, A * C) + Fraction(1, A * C * H) + Fraction(1, prime * K)
        or Fraction(4, source)
        != Fraction(1, source_term) + Fraction(1, A * C) + Fraction(1, A * C * H)
    ):
        raise AssertionError("compensated-square bridge did not reconstruct")
    return {
        "A": A,
        "B": 1,
        "C": C,
        "H": H,
        "m": gap,
        "R": R,
        "K": K,
        "T": T,
        "E": E,
        "q": q,
        "source_denominator": source,
        "source_term": source_term,
        "upper_half": 2 * source >= prime + 1,
    }


def candidates(prime: int, gap_cap: int) -> tuple[list[dict[str, int | bool]], int, int]:
    """Enumerate B=1 normal forms and all eligible square divisors of their H."""
    found: list[dict[str, int | bool]] = []
    forms_checked = 0
    H_square_divisors_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B != 1:
                continue
            forms_checked += 1
            R, remainder = divmod(4 * C + 1, gap)
            if remainder:
                raise AssertionError("B=1 normal form lost its R")
            H = A * R - 1
            factors = landscape.factor_by_trial_division(H)
            for T in landscape.divisors_of_square(factors):
                H_square_divisors_checked += 1
                witness = compensated_witness(prime, A, C, gap, R, int(T))
                if witness is not None:
                    found.append(witness)
    return found, forms_checked, H_square_divisors_checked


def choose_candidate(values: list[dict[str, int | bool]]) -> dict[str, int | bool]:
    """Use a deterministic finite-box order without promoting it to a selector theorem."""
    if not values:
        raise ValueError("cannot choose an empty candidate set")
    return min(
        values,
        key=lambda witness: (
            int(witness["m"]),
            int(witness["source_denominator"]),
            int(witness["T"]),
            int(witness["A"]),
            int(witness["C"]),
        ),
    )


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Close as much as possible of the frozen m<=999 self-square residual."""
    profile = json.loads(input_path.read_text(encoding="utf-8"))
    gap_cap = int(profile["gap_cap"])
    residual = [int(prime) for prime in profile["misses"]]
    if gap_cap != 999 or len(residual) != 57 or len(set(residual)) != len(residual):
        raise AssertionError("input is not the exact m<=999 self-square residual")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms_checked = 0
    H_square_divisors_checked = 0
    candidate_count = 0
    for prime in residual:
        values, local_forms, local_divisors = candidates(prime, gap_cap)
        forms_checked += local_forms
        H_square_divisors_checked += local_divisors
        candidate_count += len(values)
        if not values:
            misses.append(prime)
            continue
        records.append(
            {
                "prime": prime,
                "compensated_square_candidate_count": len(values),
                "selected_witness": choose_candidate(values),
            }
        )
    if len(records) + len(misses) != len(residual):
        raise AssertionError("compensated-square audit did not partition its residual")
    return {
        "arithmetic": (
            "for each m<=999 B=1 normal form on the frozen self-square residual, factor H and enumerate "
            "T|H^2; retain T=4 (mod R), q=(H-CT)/R>0 and T|qH, then set E=4C^2T"
        ),
        "scope_note": (
            "This is a complete finite compensated-square audit only on the stated residual and target box. "
            "It does not select a B=1 normal form outside that box or prove a universal terminal selector."
        ),
        "input": input_path.name,
        "gap_cap": gap_cap,
        "input_residual_count": len(residual),
        "compensated_square_covered_count": len(records),
        "compensated_square_miss_count": len(misses),
        "B_one_normal_forms_exhaustively_checked": forms_checked,
        "H_square_divisors_exhaustively_checked": H_square_divisors_checked,
        "compensated_square_candidate_count": candidate_count,
        "upper_half_covered_count": sum(bool(row["selected_witness"]["upper_half"]) for row in records),
        "maximum_selected_gap": max((int(row["selected_witness"]["m"]) for row in records), default=None),
        "misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key not in {"misses", "records"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
