#!/usr/bin/env python3
"""Normalize external-source witnesses into Type I maximum-tail bridges."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-even-external-source-normal-bridge-h19-1b-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_i_even_external_bridge_short_certificate", SHORT_CERTIFICATE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def bridge_from_quadratic_external_witness(
    prime: int, witness: dict[str, object]
) -> dict[str, object]:
    """Recover the Type I normal bridge encoded by one quadratic witness."""
    p = int(prime)
    n = int(witness["source_denominator"])
    k = int(witness["k"])
    q = int(witness["q"])
    factor = int(witness["factor"])
    source_solution = tuple(int(value) for value in witness["source_solution"])
    target_solution = tuple(int(value) for value in witness["target_solution"])
    certificate = witness["certificate"]
    if not isinstance(certificate, dict):
        raise TypeError("external witness certificate must be an object")

    gap = int(certificate["gap"])
    x = int(certificate["x"])
    divisor = int(certificate["divisor"])
    y = int(certificate["y"])
    z = int(certificate["z"])
    preserved = k * n

    if p % 24 != 1 or q != 4 * k - 1:
        raise AssertionError("external source parameters are not canonical")
    if (q + 1) * n != q * p + 1 or 4 * preserved != q * p + 1:
        raise AssertionError("external source denominator identities failed")
    if (
        factor <= 0
        or factor > preserved
        or (preserved * preserved) % factor
        or factor % q != (-preserved) % q
        or q * gap != 4 * factor + 1
    ):
        raise AssertionError("quadratic external divisor conditions failed")
    if source_solution != (preserved, x, y) or target_solution != (p * preserved, x, y):
        raise AssertionError("stored external solutions do not match their certificate")
    if z != p * preserved:
        raise AssertionError("stored Type I tail is not the lifted external denominator")
    if (
        Fraction(4, n)
        != sum((Fraction(1, value) for value in source_solution), Fraction())
        or Fraction(4, p)
        != sum((Fraction(1, value) for value in target_solution), Fraction())
    ):
        raise AssertionError("external source identities did not verify")

    normal_form = short_certificate.type_i_normal_form(p, gap, divisor)
    if normal_form is None:
        raise AssertionError("external Type I certificate did not normalize")
    a, b, c = normal_form
    if a * b * c != x:
        raise AssertionError("normal form did not reconstruct the first denominator")

    numerator = 4 * b * b * c + 1
    if numerator % gap:
        raise AssertionError("normal bridge quotient is not integral")
    r = numerator // gap
    h = a * r - b
    normal_k = b * c * h
    if h <= 0 or (a * c * h, p * normal_k) != (y, z):
        raise AssertionError("normal form did not reconstruct the external tails")
    if (r, normal_k) != (q, preserved) or 4 * normal_k != p * r + 1:
        raise AssertionError("external coordinates did not equal normal bridge coordinates")

    e = 4 * normal_k - n * r
    conditions = {
        "divides_4K_squared": (4 * normal_k * normal_k) % e == 0,
        "residue_one_mod_R": e % r == 1 % r,
        "strict_source_lower_bound": e <= 4 * normal_k - 2 * r,
        "source_is_even": n % 2 == 0,
    }
    if e != n or normal_k % e:
        raise AssertionError("external witness did not produce E=n")
    if n * normal_k // e != preserved:
        raise AssertionError("normal bridge did not recover the external source term")
    if not all(
        conditions[name]
        for name in (
            "divides_4K_squared",
            "residue_one_mod_R",
            "strict_source_lower_bound",
        )
    ):
        raise AssertionError("external witness failed a required normal bridge condition")

    return {
        "prime": p,
        "source_denominator": n,
        "k": k,
        "R": r,
        "K": normal_k,
        "external_factor": factor,
        "gap": gap,
        "normal_form": list(normal_form),
        "E": e,
        "source_first_denominator": preserved,
        "conditions": conditions,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Audit every successful quadratic external witness in one stored profile."""
    records = payload["records"]
    if not isinstance(records, list):
        raise TypeError("input profile records must be a list")

    bridges: list[dict[str, object]] = []
    misses: list[int] = []
    for record in records:
        if not isinstance(record, dict):
            raise TypeError("input profile record must be an object")
        prime = int(record["prime"])
        witness = record["quadratic_factor_external_source_descent"]
        if witness is None:
            misses.append(prime)
            continue
        if not isinstance(witness, dict):
            raise TypeError("quadratic external witness must be an object")
        bridges.append(bridge_from_quadratic_external_witness(prime, witness))

    expected_misses = [int(value) for value in payload["quadratic_factor_descent_misses"]]
    if misses != expected_misses:
        raise AssertionError("quadratic external misses disagree with the source profile")
    if len(bridges) != int(payload["quadratic_factor_descent_count"]):
        raise AssertionError("quadratic external hit count disagrees with the source profile")

    terminal = [
        bridge for bridge in bridges if bridge["conditions"]["source_is_even"]
    ]
    odd_source = [
        bridge for bridge in bridges if not bridge["conditions"]["source_is_even"]
    ]
    if len(terminal) + len(odd_source) != len(bridges):
        raise AssertionError("external source parity split is not exhaustive")

    return {
        "arithmetic": (
            "exact normalization of every stored complete quadratic external "
            "source witness into a Type I maximum-tail bridge"
        ),
        "scope_note": (
            "This only transports already selected external witnesses. It does "
            "not prove a global selector for a successful external witness."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": payload["base_shift_bound"],
        "h19_residual_count": len(records),
        "quadratic_external_hit_count": len(bridges),
        "quadratic_external_miss_count": len(misses),
        "quadratic_external_misses": misses,
        "normal_bridge_count": len(bridges),
        "terminal_even_bridge_count": len(terminal),
        "odd_source_bridge_count": len(odd_source),
        "terminal_even_records": terminal,
        "odd_source_samples": odd_source[:10],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
