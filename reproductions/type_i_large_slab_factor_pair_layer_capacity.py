#!/usr/bin/env python3
"""Verify the large-slab factor-pair normal form and layer gcd capacity."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-large-slab-factor-pair-layer-capacity-results.json"
)

SLAB_CASES = (
    {"prime": 5_596_369, "R": 35, "q": 2, "e": 5, "alpha": 1, "beta": 3},
    {
        "prime": 212_973_049,
        "R": 215,
        "q": 71,
        "e": 1,
        "alpha": 3,
        "beta": 2,
    },
    {
        "prime": 122_014_489,
        "R": 471,
        "q": 467,
        "e": 1,
        "alpha": 1,
        "beta": 4,
    },
    {
        "prime": 37_793_809,
        "R": 12_423,
        "q": 6_211,
        "e": 1,
        "alpha": 2,
        "beta": 1,
    },
)

EXPECTED_ADMISSIBLE_BETAS = {
    (5_596_369, 2, 5, 1): [3],
    (212_973_049, 71, 1, 3): [2],
    (122_014_489, 467, 1, 1): [4, 244],
    (37_793_809, 6_211, 1, 2): [1],
}

SOURCE_WORD_CASES = (
    {
        "prime": 10_170_169,
        "R": 127,
        "q": 101,
        "e": 1,
        "U": 1,
        "V": 5_079,
        "theta": 210,
        "X_U": 101,
        "X_V": 26,
        "source_path": [
            {"node": [4, 20_189, 159], "q": 2, "g": 2},
            {"node": [1, 5_079, 40], "q": 3, "g": 1},
            {"node": [85, 1_693, 14], "q": 5, "g": 1},
            {"node": [17, 364, 3], "q": 7, "g": 1},
            {"node": [52, 75, 1], "q": 2, "g": 1},
            {"node": [26, 101, 1]},
        ],
        "anchor_gap": 63,
        "anchor_type_i_divisor": 62,
        "expected_R_Q": 35,
    },
    {
        "prime": 5_596_369,
        "R": 35,
        "q": 2,
        "e": 5,
        "U": 237,
        "V": 8,
        "theta": 1_496,
        "X_U": 32,
        "X_V": 3,
    },
    {
        "prime": 212_973_049,
        "R": 215,
        "q": 71,
        "e": 1,
        "U": 1_259,
        "V": 1_966,
        "theta": 983,
        "X_U": 213,
        "X_V": 2,
    },
    {
        "prime": 122_014_489,
        "R": 471,
        "q": 467,
        "e": 1,
        "U": 3_221,
        "V": 76,
        "theta": 19,
        "X_U": 467,
        "X_V": 4,
    },
    {
        "prime": 37_793_809,
        "R": 12_423,
        "q": 6_211,
        "e": 1,
        "U": 48_143,
        "V": 1_549,
        "theta": 1_549,
        "X_U": 12_422,
        "X_V": 1,
    },
)


def factorization(value: int) -> dict[int, int]:
    """Small deterministic trial factorization for the focused examples."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    remainder = value
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remainder //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in sorted(factors.items()):
        values = [value * prime**power for value in values for power in range(exponent + 1)]
    return sorted(values)


def multiplicative_order(base: int, modulus: int) -> int:
    if math.gcd(base, modulus) != 1:
        raise ValueError("multiplicative order requires coprime inputs")
    residue = 1
    for order in range(1, modulus + 1):
        residue = residue * base % modulus
        if residue == 1:
            return order
    raise AssertionError("multiplicative order not found")


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def formal_transition(node: list[int], R: int, q: int) -> tuple[list[int], int]:
    A, B, layer = node
    if A % q:
        A, B = B, A
    assert A % q == 0 and B % q != 0
    shift = (-layer) % q
    assert 1 <= shift < q
    A0 = A // q
    B0 = (B + R * shift) // q
    layer0 = (layer + shift) // q
    common = math.gcd(A0, B0)
    assert layer0 % common == 0
    return [*sorted((A0 // common, B0 // common)), layer0 // common], common


def admissible_records(prime: int, q: int, e: int, alpha: int) -> list[dict[str, int]]:
    Q = q**e
    N = alpha * prime * Q + 1
    records: list[dict[str, int]] = []
    for beta in divisors_from_factors(factorization(N)):
        H = N // beta
        if (H + prime) % (4 * alpha):
            continue
        c = (H + prime) // (4 * alpha)
        if c % q == 0 or beta >= (4 - alpha) * Q:
            continue
        R = alpha * Q + beta
        K = alpha * beta * c
        if not 3 <= R <= prime - 2:
            continue
        assert math.gcd(Q * alpha, beta) == 1
        assert K % q != 0
        assert 4 * K == prime * R + 1
        assert 4 * Q > R
        records.append({"beta": beta, "H": H, "c": c, "R": R, "K": K})
    return records


def analyze_slab(case: dict[str, int]) -> dict[str, object]:
    prime = case["prime"]
    R = case["R"]
    q = case["q"]
    e = case["e"]
    alpha = case["alpha"]
    beta = case["beta"]
    Q = q**e
    K = (prime * R + 1) // 4
    assert prime % 24 == 1
    assert R == alpha * Q + beta
    assert alpha in (1, 2, 3) and alpha % q != 0
    assert math.gcd(Q * alpha, beta) == 1
    assert K % (alpha * beta) == 0 and K % q != 0
    assert 4 * Q > R
    c = K // (alpha * beta)
    H = 4 * alpha * c - prime
    N = alpha * prime * Q + 1
    assert beta * H == N
    assert beta < (4 - alpha) * Q
    assert (4 - alpha) * H > alpha * prime

    admissible = admissible_records(prime, q, e, alpha)
    key = (prime, q, e, alpha)
    admissible_betas = [record["beta"] for record in admissible]
    assert admissible_betas == EXPECTED_ADMISSIBLE_BETAS[key]
    selected = next(record for record in admissible if record["beta"] == beta)
    assert selected["R"] == R and selected["K"] == K
    return {
        **case,
        "Q": Q,
        "K": K,
        "N": N,
        "N_factorization": {str(p): a for p, a in factorization(N).items()},
        "H": H,
        "c": c,
        "admissible_records_in_linear_range": admissible,
    }


def layer_value(prime: int, q: int, alpha: int, exponent: int) -> int:
    return alpha * prime * q**exponent + 1


def verify_layer_capacity() -> dict[str, object]:
    prime = 337
    q = 7
    alphas = (1, 2, 3)
    exponents = tuple(range(1, 6))
    nodes = [(alpha, exponent) for exponent in exponents for alpha in alphas]
    pair_checks = []
    for index, (alpha, exponent) in enumerate(nodes):
        left = layer_value(prime, q, alpha, exponent)
        for alpha2, exponent2 in nodes[index + 1 :]:
            right = layer_value(prime, q, alpha2, exponent2)
            if exponent2 < exponent:
                alpha, exponent, alpha2, exponent2 = alpha2, exponent2, alpha, exponent
                left, right = right, left
            delta = abs(alpha2 * q ** (exponent2 - exponent) - alpha)
            actual = math.gcd(left, right)
            predicted = math.gcd(left, delta)
            assert actual == predicted
            pair_checks.append(
                {
                    "left": [alpha, exponent],
                    "right": [alpha2, exponent2],
                    "gcd": actual,
                    "difference": delta,
                }
            )

    same_exponent = []
    for exponent in exponents:
        for alpha, alpha2, expected in ((1, 2, 1), (2, 3, 1), (1, 3, 2)):
            actual = math.gcd(
                layer_value(prime, q, alpha, exponent),
                layer_value(prime, q, alpha2, exponent),
            )
            assert actual == expected
            same_exponent.append(
                {"exponent": exponent, "alphas": [alpha, alpha2], "gcd": actual}
            )

    repeated_carriers = []
    for alpha in alphas:
        occurrences: dict[int, list[int]] = {}
        for exponent in exponents:
            value = layer_value(prime, q, alpha, exponent)
            for carrier in factorization(value):
                occurrences.setdefault(carrier, []).append(exponent)
        for carrier, carrier_exponents in sorted(occurrences.items()):
            if len(carrier_exponents) < 2:
                continue
            order = multiplicative_order(q, carrier)
            anchor = carrier_exponents[0]
            assert all((exponent - anchor) % order == 0 for exponent in carrier_exponents)
            bound = (exponents[-1] - exponents[0]) // order + 1
            assert len(carrier_exponents) <= bound
            repeated_carriers.append(
                {
                    "alpha": alpha,
                    "carrier": carrier,
                    "exponents": carrier_exponents,
                    "order": order,
                    "interval_capacity": bound,
                }
            )

    expected_repeated = [
        {"alpha": 1, "carrier": 2, "exponents": [1, 2, 3, 4, 5], "order": 1},
        {"alpha": 1, "carrier": 5, "exponents": [1, 5], "order": 4},
        {"alpha": 2, "carrier": 3, "exponents": [1, 2, 3, 4, 5], "order": 1},
        {"alpha": 3, "carrier": 2, "exponents": [1, 2, 3, 4, 5], "order": 1},
    ]
    assert [
        {key: record[key] for key in ("alpha", "carrier", "exponents", "order")}
        for record in repeated_carriers
    ] == expected_repeated

    multi_layer_checks = []
    for alpha, selected in ((1, (1, 3, 5)), (2, (1, 2, 5)), (3, (2, 4, 5))):
        anchor = min(selected)
        step_gcd = math.gcd(*(exponent - anchor for exponent in selected if exponent > anchor))
        values = [layer_value(prime, q, alpha, exponent) for exponent in selected]
        actual = math.gcd(*values)
        predicted = math.gcd(values[0], q**step_gcd - 1)
        assert actual == predicted
        multi_layer_checks.append(
            {
                "alpha": alpha,
                "exponents": list(selected),
                "step_gcd": step_gcd,
                "common_gcd": actual,
            }
        )

    return {
        "prime": prime,
        "q": q,
        "alphas": list(alphas),
        "exponents": list(exponents),
        "pair_check_count": len(pair_checks),
        "same_exponent_checks": same_exponent,
        "repeated_carriers": repeated_carriers,
        "multi_layer_checks": multi_layer_checks,
        "nontrivial_pair_examples": [record for record in pair_checks if record["gcd"] > 2][
            :8
        ],
    }


def analyze_source_word_carrier(case: dict[str, int]) -> dict[str, object]:
    prime = case["prime"]
    R = case["R"]
    q = case["q"]
    e = case["e"]
    U = case["U"]
    V = case["V"]
    theta = case["theta"]
    X_U = case["X_U"]
    X_V = case["X_V"]
    K = (prime * R + 1) // 4
    x_R = (prime + R) // 4
    assert prime % 24 == 1
    assert U + V > 0 and (U + V) % R == 0
    assert X_U + X_V == R
    assert K % U == 0 and K % q != 0
    u = (theta * X_U - U) // R
    v = (theta * X_V - V) // R
    assert theta * X_U == U + R * u and u >= 0
    assert theta * X_V == V + R * v and v >= 0
    assert u + v == theta - (U + V) // R

    boundary: dict[str, object] | None = None
    if "source_path" in case:
        source_path = case["source_path"]
        for current, following in zip(source_path, source_path[1:]):
            destination, common = formal_transition(current["node"], R, current["q"])
            assert destination == following["node"] and common == current["g"]
        assert source_path[1]["node"] == sorted((U, V)) + [(U + V) // R]
        assert source_path[-1]["node"] == sorted((X_U, X_V)) + [1]

        gap = case["anchor_gap"]
        divisor = case["anchor_type_i_divisor"]
        first_denominator = (prime + gap) // 4
        assert first_denominator**2 % divisor == 0
        assert (prime * first_denominator + divisor) % gap == 0
        second_denominator = (prime * first_denominator + divisor) // gap
        numerator = prime * first_denominator * second_denominator
        assert numerator % divisor == 0
        third_denominator = numerator // divisor
        assert (
            Fraction(1, first_denominator)
            + Fraction(1, second_denominator)
            + Fraction(1, third_denominator)
            == Fraction(4, prime)
        )
        R_Q = (-pow(prime, -1, 4 * q**e)) % (4 * q**e)
        assert R_Q == case["expected_R_Q"] and R_Q < R
        boundary = {
            "anchor_type_i": {
                "gap": gap,
                "divisor": divisor,
                "solution": [first_denominator, second_denominator, third_denominator],
            },
            "R_Q": R_Q,
            "decreases_R": True,
        }
    e_U = valuation(X_U, q)
    e_V = valuation(X_V, q)
    assert sorted((e_U, e_V)) == [0, e]

    d_U = math.gcd(U, theta * X_V)
    d_V = math.gcd(V, theta * X_U)
    L_U = U * theta * X_V // d_U**2
    L_V = V * theta * X_U // d_V**2
    common_capacity = math.lcm(K, x_R)
    C_U = L_U // math.gcd(L_U, common_capacity)
    C_V = L_V // math.gcd(L_V, common_capacity)

    a = valuation(theta, q)
    b = valuation(V, q)
    s = valuation(x_R, q)
    predicted_U = max(0, a + e_V - s)
    predicted_V = max(0, abs(b - a - e_U) - s)
    actual_U = valuation(C_U, q)
    actual_V = valuation(C_V, q)
    assert valuation(L_U, q) == a + e_V
    assert valuation(L_V, q) == abs(b - a - e_U)
    assert (actual_U, actual_V) == (predicted_U, predicted_V)

    return {
        **case,
        "K": K,
        "x_R": x_R,
        "path_valuations": {"a": a, "b": b, "s": s, "e_U": e_U, "e_V": e_V},
        "path_quotients": {"u": u, "v": v},
        "cross_products": {"L_U": L_U, "L_V": L_V},
        "common_overload_factors": {"C_U": C_U, "C_V": C_V},
        "q_overload_exponents": {"U": actual_U, "V": actual_V},
        "q_in_union": bool(actual_U or actual_V),
        "boundary": boundary,
    }


def run() -> dict[str, object]:
    slab_records = [analyze_slab(case) for case in SLAB_CASES]
    layer_capacity = verify_layer_capacity()
    source_word_records = [analyze_source_word_carrier(case) for case in SOURCE_WORD_CASES]
    summary = {
        "slab_case_count": len(slab_records),
        "covered_alpha": sorted({record["alpha"] for record in slab_records}),
        "admissible_factor_pair_count": sum(
            len(record["admissible_records_in_linear_range"]) for record in slab_records
        ),
        "layer_gcd_pair_check_count": layer_capacity["pair_check_count"],
        "same_exponent_check_count": len(layer_capacity["same_exponent_checks"]),
        "repeated_carrier_count": len(layer_capacity["repeated_carriers"]),
        "source_word_carrier_case_count": len(source_word_records),
        "source_word_slab_q_union_hit_count": sum(
            record["q_in_union"] for record in source_word_records
        ),
    }
    expected_summary = {
        "slab_case_count": 4,
        "covered_alpha": [1, 2, 3],
        "admissible_factor_pair_count": 5,
        "layer_gcd_pair_check_count": 105,
        "same_exponent_check_count": 15,
        "repeated_carrier_count": 4,
        "source_word_carrier_case_count": 5,
        "source_word_slab_q_union_hit_count": 4,
    }
    if summary != expected_summary:
        raise AssertionError(f"focused factor-pair capacity boundary changed: {summary}")
    return {
        "schema_version": "type-i-large-slab-factor-pair-layer-capacity/v1",
        "scope_note": (
            "Focused exact checks of four arithmetic large slabs and a 15-layer "
            "gcd grid. This does not rerun the historical 1412-slab census, prove "
            "source Reach membership, or upgrade a slab to a Type I/II or E4 exit."
        ),
        "summary": summary,
        "slab_records": slab_records,
        "layer_capacity": layer_capacity,
        "source_word_carrier_records": source_word_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
