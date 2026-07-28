#!/usr/bin/env python3
"""Test general-B compensated squares on the 21-point B=1 residual."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-b1-compensated-square-profile-600m-results.json"
LINEAR = ROOT / "reproductions" / "type-i-linear-source-general-b-completion-profile-600m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-general-b-compensated-square-residual-profile-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("general_b_compensated_square_landscape", LANDSCAPE)


def compensated_witness(
    prime: int, A: int, B: int, C: int, gap: int, R: int, T: int
) -> dict[str, int | bool] | None:
    """Construct E=4*B^2*C^2*T from a general-B normal form."""
    H = A * R - B
    K = B * C * H
    if (
        prime % 24 != 1
        or gap < 3
        or gap % 4 != 3
        or R < 3
        or R % 4 != 3
        or gap * R != 4 * B * B * C + 1
        or prime != 4 * A * B * C - gap
        or 4 * K != prime * R + 1
        or T <= 0
        or H * H % T
        or T % R != (4 * B * B) % R
    ):
        return None
    q, remainder = divmod(H - B * C * T, R)
    if remainder or q <= 0 or q * H % T:
        return None
    E = 4 * B * B * C * C * T
    source = 4 * B * C * q
    source_term = q * H // T
    if (
        E % 2
        or E % R != 1
        or (4 * K * K) % E
        or E > 4 * K - 2 * R
        or source % 2
        or not (2 <= source < prime)
        or Fraction(4, prime)
        != Fraction(1, A * B * C) + Fraction(1, A * C * H) + Fraction(1, prime * K)
        or Fraction(4, source)
        != Fraction(1, source_term) + Fraction(1, A * B * C) + Fraction(1, A * C * H)
    ):
        raise AssertionError("general-B compensated-square bridge did not reconstruct")
    return {
        "A": A,
        "B": B,
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


def candidate_witnesses(prime: int, selected: dict[str, object]) -> tuple[list[dict[str, int | bool]], int]:
    """Enumerate the full H-square divisor menu for one stored linear normal form."""
    A = int(selected["A"])
    B = int(selected["B"])
    C = int(selected["C"])
    gap = int(selected["gap"])
    R = int(selected["R"])
    H = int(selected["H"])
    if H != A * R - B or int(selected["K"]) != B * C * H:
        raise AssertionError("stored linear normal form did not reconstruct")
    values: list[dict[str, int | bool]] = []
    divisors_checked = 0
    factors = landscape.factor_by_trial_division(H)
    for T in landscape.divisors_of_square(factors):
        divisors_checked += 1
        witness = compensated_witness(prime, A, B, C, gap, R, int(T))
        if witness is not None:
            values.append(witness)
    return values, divisors_checked


def choose_candidate(values: list[dict[str, int | bool]]) -> dict[str, int | bool]:
    """Choose deterministically within the already selected linear normal form."""
    if not values:
        raise ValueError("cannot choose an empty candidate set")
    return min(
        values,
        key=lambda witness: (
            int(witness["source_denominator"]),
            int(witness["T"]),
        ),
    )


def run_audit(input_path: Path = INPUT, linear_path: Path = LINEAR) -> dict[str, object]:
    """Apply compensated-square tests to the 21 residuals' selected linear normal forms."""
    residual_payload = json.loads(input_path.read_text(encoding="utf-8"))
    residual = [int(prime) for prime in residual_payload["misses"]]
    if len(residual) != 21 or len(set(residual)) != len(residual):
        raise AssertionError("input is not the exact 21-point compensated-square residual")
    linear_payload = json.loads(linear_path.read_text(encoding="utf-8"))
    linear_records = linear_payload["captured_records"]
    selected = {int(record["prime"]): record["selected_witness"] for record in linear_records}
    if len(selected) != 1964:
        raise AssertionError("linear input did not reconstruct the complete 1,964-point profile")

    records: list[dict[str, object]] = []
    misses: list[int] = []
    divisors_checked = 0
    candidate_count = 0
    for prime in residual:
        witness = selected.get(prime)
        if not isinstance(witness, dict):
            raise AssertionError("residual has no selected linear witness")
        values, local_divisors = candidate_witnesses(prime, witness)
        divisors_checked += local_divisors
        candidate_count += len(values)
        if not values:
            misses.append(prime)
            continue
        records.append(
            {
                "prime": prime,
                "selected_linear_B": int(witness["B"]),
                "compensated_square_candidate_count": len(values),
                "selected_witness": choose_candidate(values),
            }
        )
    if len(records) + len(misses) != len(residual):
        raise AssertionError("general-B compensated-square audit did not partition its residual")
    return {
        "arithmetic": (
            "on each residual's already selected complete linear general-B normal form, factor H and enumerate "
            "T|H^2; retain T=4B^2 (mod R), q=(H-BCT)/R>0 and T|qH, then set E=4B^2C^2T"
        ),
        "scope_note": (
            "This finite audit tests only one pre-selected linear normal form for each residual. A miss does "
            "not exclude another linear source, another normal form, or any other terminal mechanism."
        ),
        "residual_input": input_path.name,
        "linear_input": linear_path.name,
        "input_residual_count": len(residual),
        "general_B_compensated_square_covered_count": len(records),
        "general_B_compensated_square_miss_count": len(misses),
        "H_square_divisors_exhaustively_checked_within_selected_forms": divisors_checked,
        "general_B_compensated_square_candidate_count": candidate_count,
        "upper_half_covered_count": sum(bool(row["selected_witness"]["upper_half"]) for row in records),
        "selected_B_histogram": {
            str(B): sum(int(row["selected_linear_B"]) == B for row in records)
            for B in sorted({int(row["selected_linear_B"]) for row in records})
        },
        "misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--linear", type=Path, default=LINEAR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input, args.linear)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key not in {"misses", "records"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
