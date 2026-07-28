#!/usr/bin/env python3
"""Resolve seven compensated-square residuals by their full linear target spectra."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-general-b-compensated-square-full-linear-profile-600m-results.json"
COMPENSATED_SCRIPT = ROOT / "reproductions" / "type_i_general_b_compensated_square_full_linear_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-general-b-spectrum-resolution-profile-600m-results.json"

EXPECTED_INPUT_SHA256 = "57d323b8bd92db35c0e584c3bbab727cc993b595389e8207fbb9f684e492d0e6"
EXPECTED_RESIDUAL = [
    214_729,
    878_089,
    2_210_569,
    13_782_409,
    64_214_329,
    105_295_129,
    536_944_489,
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


compensated = load_module("linear_spectrum_compensated", COMPENSATED_SCRIPT)
sources = compensated.sources


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_fraction_identity(numerator: int, denominators: list[int]) -> bool:
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def direct_linear_terminal_witness(
    prime: int, a: int, s: int, form: dict[str, int]
) -> dict[str, object]:
    """Replay the direct beta=1 terminal bridge at a target-spectrum hit."""
    A = int(form["A"])
    B = int(form["B"])
    C = int(form["C"])
    H = int(form["H"])
    gap = int(form["m"])
    R = int(form["R"])
    K = int(form["K"])
    E = s * R + 1
    source = prime - s
    target_divisor = B * B * C
    target_solution = [A * B * C, A * C * H, prime * K]
    source_solution = [a * K, A * B * C, A * C * H]
    conditions = {
        "linear_source": prime == a + s + a * s * R,
        "source_factorization": source == a * E,
        "even_source": source >= 2 and source % 2 == 0,
        "K_relation": 4 * K == prime * R + 1,
        "linear_K_factorization": 4 * K == (a * R + 1) * E,
        "terminal_congruence": E % R == 1 % R,
        "terminal_divides_source": source % E == 0,
        "terminal_divides_four_K_squared": (4 * K * K) % E == 0,
        "terminal_reconstruction": source == (4 * K - E) // R
        and (4 * K - E) % R == 0,
        "terminal_upper_bound": E <= 4 * K - 2 * R,
        "target_square_divisor": (K * K) % target_divisor == 0,
        "target_residue": (4 * target_divisor + 1) % R == 0,
        "natural_type_I_form": prime == 4 * A * B * C - gap
        and 4 * B * C * H == prime * R + 1,
        "target_identity": exact_fraction_identity(prime, target_solution),
        "source_identity": exact_fraction_identity(source, source_solution),
    }
    if not all(conditions.values()):
        failed = [name for name, value in conditions.items() if not value]
        raise AssertionError(f"invalid direct terminal bridge: {failed}")
    return {
        "a": a,
        "s": s,
        "R": R,
        "K": K,
        "E": E,
        "source_denominator": source,
        "matched_square_divisor": target_divisor,
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "gap": gap,
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def witness_key(witness: dict[str, object]) -> tuple[int, ...]:
    return tuple(
        int(witness[field])
        for field in ("gap", "B", "C", "R", "s", "a", "matched_square_divisor")
    )


def load_residual(input_path: Path = INPUT) -> list[int]:
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full compensated-square input artifact changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    residual = [int(value) for value in payload["misses"]]
    if (
        residual != EXPECTED_RESIDUAL
        or int(payload["full_linear_R_compensated_square_miss_count"]) != len(residual)
    ):
        raise AssertionError("the seven-point compensated-square residual changed")
    return residual


def audit_prime(prime: int) -> tuple[dict[str, object], Counter[str]]:
    """Exhaust every induced R and retain all target-spectrum hits before selecting."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    local: Counter[str] = Counter()
    candidates: list[dict[str, object]] = []
    hit_Rs: list[dict[str, object]] = []
    for R, states in states_by_R.items():
        local["linear_R_count"] += 1
        local["directed_linear_source_state_count"] += len(states)
        forms, square_divisor_count, target_hit_count = compensated.target_forms_for_R(
            prime, R
        )
        local["K_square_divisors_checked"] += square_divisor_count
        local["target_divisor_hits"] += target_hit_count
        local["target_normal_form_count"] += len(forms)
        if not forms:
            continue
        hit_Rs.append(
            {
                "R": R,
                "source_state_count": len(states),
                "target_divisor_hit_count": target_hit_count,
                "target_normal_form_count": len(forms),
            }
        )
        for form in forms:
            for a, s in states:
                candidates.append(direct_linear_terminal_witness(prime, a, s, form))
    if not candidates:
        raise AssertionError("a compensated-square residual has no linear target-spectrum hit")
    selected = min(candidates, key=witness_key)
    return (
        {
            "prime": prime,
            "linear_source_coordinate_bound": bound,
            "linear_R_count": local["linear_R_count"],
            "directed_linear_source_state_count": local[
                "directed_linear_source_state_count"
            ],
            "K_square_divisors_checked": local["K_square_divisors_checked"],
            "target_divisor_hits": local["target_divisor_hits"],
            "target_normal_form_count": local["target_normal_form_count"],
            "target_hit_Rs": hit_Rs,
            "direct_terminal_candidate_count": len(candidates),
            "selected_witness": selected,
        },
        local,
    )


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    residual = load_residual(input_path)
    records: list[dict[str, object]] = []
    totals: Counter[str] = Counter()
    for prime in residual:
        record, local = audit_prime(prime)
        records.append(record)
        totals.update(local)
    if len(records) != len(residual):
        raise AssertionError("the spectrum audit did not partition its frozen input")
    return {
        "arithmetic": (
            "for every directed linear source p=a+s+asR through the exact min(a,s) bound, "
            "deduplicate induced R; at each R enumerate every d|K^2 with 4d=-1 (mod R), "
            "normalize each target form, and replay its direct beta=1 terminal bridge with every "
            "source state at that R"
        ),
        "scope_note": (
            "This is a complete finite target-spectrum audit for the seven residuals of the stated "
            "compensated-square mechanism. It proves that all seven have ordinary linear-source general-B "
            "terminal bridges, but it does not prove the universal cross-source selector conjecture."
        ),
        "input": input_path.name,
        "input_residual_count": len(residual),
        "spectrum_resolved_count": len(records),
        "spectrum_unresolved_count": 0,
        "linear_source_coordinate_bound_max": max(
            int(record["linear_source_coordinate_bound"]) for record in records
        ),
        "linear_R_exhaustively_checked": totals["linear_R_count"],
        "directed_linear_source_state_count": totals["directed_linear_source_state_count"],
        "K_square_divisors_exhaustively_checked": totals["K_square_divisors_checked"],
        "target_divisor_hits": totals["target_divisor_hits"],
        "target_normal_forms_exhaustively_checked": totals["target_normal_form_count"],
        "direct_terminal_candidate_count": sum(
            int(record["direct_terminal_candidate_count"]) for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
