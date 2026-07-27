#!/usr/bin/env python3
"""Profile general low-B even-source edges on the dyadic p-1 residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DYADIC = ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-100k-results.json"
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
SUPPORT = ROOT / "reproductions" / "type_i_tail_reverse_even_source_support_minimization.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-dyadic-residual-general-edge-profile-100k-results.json"
B_CAP = 4


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("dyadic_residual_general_direct", DIRECT)
support = load_module("dyadic_residual_general_support", SUPPORT)


def bridge_complexity(prime: int, gap: int, A: int, B: int, C: int, lift: dict[str, int]) -> dict[str, object]:
    """Factor E using the already-factored normal-form product, not by trial division of E."""
    R = (4 * B * B * C + 1) // gap
    H = A * R - B
    K = B * C * H
    E = int(lift["bridge_divisor"]) // (prime * prime)
    if int(lift["bridge_divisor"]) != prime * prime * E:
        raise AssertionError("bridge divisor did not normalize to p^2 E")
    factors = support.factor_E_from_K(E, direct.support_min.bridge.factor_product(B, C, H))
    odd_factors = {str(q): exponent for q, exponent in factors.items() if q != 2}
    return {
        "gap": gap,
        "normal_form": [A, B, C],
        "R": R,
        "K": K,
        "source_denominator": int(lift["source_denominator"]),
        "source_distance": prime - int(lift["source_denominator"]),
        "source_term": int(lift["source_term"]),
        "E": E,
        "E_factorization": {str(q): exponent for q, exponent in factors.items()},
        "odd_E_factorization": odd_factors,
        "odd_E_prime_support": len(odd_factors),
        "odd_E_exponent_count": sum(odd_factors.values()),
    }


def all_low_b_even_edges(prime: int, b_cap: int = B_CAP) -> tuple[list[dict[str, object]], int, int]:
    """Exhaust every natural-gap B-bounded normal form and strict even maximum-tail lift."""
    candidates: list[dict[str, object]] = []
    form_count = 0
    strict_lift_count = 0
    for gap in range(3, prime - 1, 4):
        for entry in direct.support_min.landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B > b_cap:
                continue
            form_count += 1
            _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            strict_lift_count += len(lifts)
            for lift in lifts:
                if int(lift["source_denominator"]) % 2:
                    continue
                candidates.append(bridge_complexity(prime, gap, A, B, C, lift))
    return candidates, form_count, strict_lift_count


def source_distance_key(candidate: dict[str, object]) -> tuple[int, int, int, int, int, int]:
    return (
        int(candidate["source_distance"]),
        int(candidate["odd_E_prime_support"]),
        int(candidate["odd_E_exponent_count"]),
        int(candidate["E"]),
        int(candidate["normal_form"][1]),
        int(candidate["gap"]),
    )


def odd_bridge_key(candidate: dict[str, object]) -> tuple[int, int, int, int, int, int]:
    return (
        int(candidate["odd_E_prime_support"]),
        int(candidate["odd_E_exponent_count"]),
        int(candidate["E"]),
        int(candidate["source_distance"]),
        int(candidate["normal_form"][1]),
        int(candidate["gap"]),
    )


def verify_witness(prime: int, witness: dict[str, object]) -> None:
    """Validate one stored edge from its arithmetic fields alone."""
    gap = int(witness["gap"])
    A, B, C = (int(value) for value in witness["normal_form"])
    R = int(witness["R"])
    K = int(witness["K"])
    source = int(witness["source_denominator"])
    source_term = int(witness["source_term"])
    E = int(witness["E"])
    H = A * R - B
    target = (A * B * C, A * C * H, prime * K)

    if (
        gap % 4 != 3
        or gap * R != 4 * B * B * C + 1
        or H <= 0
        or K != B * C * H
        or 4 * K != prime * R + 1
    ):
        raise AssertionError("stored normal form does not reconstruct")
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("stored target identity does not verify")
    if (
        source != prime - int(witness["source_distance"])
        or source % 2
        or not 2 <= source < prime
        or source * R != 4 * K - E
        or source * K != source_term * E
        or (4 * K * K) % E
    ):
        raise AssertionError("stored bridge data does not reconstruct")
    if Fraction(4, source) != sum(
        (Fraction(1, term) for term in (source_term, target[0], target[1])), Fraction()
    ):
        raise AssertionError("stored source identity does not verify")


def verify_result(payload: dict[str, object]) -> None:
    """Independently check each selected certificate retained in the profile."""
    records = payload["records"]
    if len(records) != int(payload["input_residual_count"]):
        raise AssertionError("stored record count changed")
    for record in records:
        prime = int(record["prime"])
        verify_witness(prime, record["minimum_source_distance"])
        verify_witness(prime, record["minimum_odd_bridge"])


def run_profile(dyadic_path: Path = DYADIC, b_cap: int = B_CAP) -> dict[str, object]:
    """Classify the exact low-B alternatives for every dyadic p-1 residual."""
    source = json.loads(dyadic_path.read_text(encoding="utf-8"))
    residuals = [int(prime) for prime in source["misses"]]
    if source["prime_limit"] != 100_009 or len(residuals) != 94:
        raise AssertionError("input does not match the stored 100K dyadic residual profile")
    records = []
    all_candidate_count = 0
    all_form_count = 0
    all_strict_lift_count = 0
    for prime in residuals:
        candidates, form_count, strict_lift_count = all_low_b_even_edges(prime, b_cap)
        if not candidates:
            raise AssertionError(f"dyadic residual {prime} escaped the stated low-B box")
        all_candidate_count += len(candidates)
        all_form_count += form_count
        all_strict_lift_count += strict_lift_count
        records.append(
            {
                "prime": prime,
                "b_bounded_normal_form_count": form_count,
                "b_bounded_strict_reverse_lift_count": strict_lift_count,
                "strict_even_candidate_count": len(candidates),
                "minimum_source_distance": min(candidates, key=source_distance_key),
                "minimum_odd_bridge": min(candidates, key=odd_bridge_key),
            }
        )
    min_distance = [record["minimum_source_distance"] for record in records]
    min_odd = [record["minimum_odd_bridge"] for record in records]
    payload = {
        "arithmetic": (
            "for each stored dyadic p-1 residual, enumerate every natural Type I gap, every normal form "
            "with B<=4, and every exact maximum-tail reverse bridge; retain strict even sources and factor "
            "E only through its certified divisibility in 4K^2"
        ),
        "scope_note": (
            "A complete finite complement profile for the 94 stated residuals. It identifies alternative "
            "low-B Type I edges, but does not establish a universal bound on source distance or bridge complexity."
        ),
        "input_dyadic_profile": dyadic_path.name,
        "input_residual_count": len(residuals),
        "b_cap": b_cap,
        "b_bounded_normal_form_count": all_form_count,
        "b_bounded_strict_reverse_lift_count": all_strict_lift_count,
        "strict_even_candidate_count": all_candidate_count,
        "minimum_source_distance_histogram": dict(
            sorted(Counter(str(record["source_distance"]) for record in min_distance).items(), key=lambda item: int(item[0]))
        ),
        "minimum_source_distance_maximum": max(record["source_distance"] for record in min_distance),
        "minimum_odd_bridge_support_histogram": dict(
            sorted(Counter(str(record["odd_E_prime_support"]) for record in min_odd).items(), key=lambda item: int(item[0]))
        ),
        "minimum_odd_bridge_exponent_histogram": dict(
            sorted(Counter(str(record["odd_E_exponent_count"]) for record in min_odd).items(), key=lambda item: int(item[0]))
        ),
        "minimum_odd_bridge_dyadic_count": sum(record["odd_E_prime_support"] == 0 for record in min_odd),
        "p_minus_one_low_b_count": sum(record["source_distance"] == 1 for record in min_distance),
        "records": records,
    }
    verify_result(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dyadic", type=Path, default=DYADIC)
    parser.add_argument("--b-cap", type=int, default=B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.dyadic, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
