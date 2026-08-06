#!/usr/bin/env python3
"""Targeted arithmetic boundary for high-anchor positive cofactor phases.

This is intentionally a two-instance replay.  It verifies the p=1201
minimal h=1 and h=2 arithmetic r-charts, then exhausts the five Bradford
gaps below 23.  It does not construct source/path or F/G provenance and
does not claim a recursive selector edge.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-high-anchor-positive-phase-terminal-boundary-results.json"
)


@dataclass(frozen=True)
class MinimalPhaseInput:
    phase: int
    support: int
    target_defect: int
    source_multiplier: int


def factorization(value: int) -> list[tuple[int, int]]:
    if value <= 0:
        raise ValueError("factorization requires a positive value")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return factors


def positive_divisors_from_factorization(
    factors: list[tuple[int, int]],
) -> list[int]:
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def square_divisors(value: int) -> list[int]:
    return positive_divisors_from_factorization(
        [(prime, 2 * exponent) for prime, exponent in factorization(value)]
    )


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    residue = (-pow(prime, -1, modulus)) % modulus
    chart = (residue, (prime * residue + 1) // 4)
    if not (
        1 <= chart[0] < modulus
        and prime * chart[0] + 1 == 4 * chart[1]
        and chart[1] % support == 0
    ):
        raise AssertionError("canonical chart failed")
    return chart


def verify_minimal_phase(
    prime: int, item: MinimalPhaseInput
) -> dict[str, object]:
    h = item.phase
    q = h + 1
    A = item.support
    delta = item.target_defect
    C = q * A
    r = prime - delta
    B = prime - q * delta
    K = A * B
    residual_numerator = 4 * q * A * delta + 1
    if residual_numerator % prime:
        raise AssertionError("minimal residual is not integral")
    n = residual_numerator // prime
    R = 4 * A - n

    # The least positive k makes M=kp+r a multiple of A.  This makes the
    # source an arithmetic overflow chart with cofactor C, not a provenance receipt.
    k = (-r * pow(prime, -1, A)) % A
    if k == 0:
        k = A
    M = k * prime + r
    d_source = prime - C
    n_source_numerator = 4 * M * d_source + 1
    if n_source_numerator % prime:
        raise AssertionError("source overflow determinant is not integral")
    n_source = n_source_numerator // prime
    R_source = 4 * M - n_source
    K_source = M * C

    s_numerator = 4 * r * d_source + 1
    if s_numerator % prime:
        raise AssertionError("r-chart cofactor equation is not integral")
    s = s_numerator // prime
    R_target = 4 * r - s
    K_target = r * C
    A_target = C
    n_target = 4 * A_target - R_target
    anchor_defect = prime - B
    target_defect = prime - r

    checks = {
        "prime_is_1_mod_24": prime % 24 == 1,
        "source_carrier_decomposition": M == k * prime + r and 1 <= r < prime,
        "source_support_divisibility": M % A == 0,
        "source_overflow_equation": prime * n_source == 4 * M * d_source + 1,
        "source_chart": prime * R_source + 1 == 4 * K_source,
        "source_canonical_chart": canonical_chart(prime, M) == (R_source, K_source),
        "cofactor_range": 1 <= C < prime and d_source == prime - C,
        "high_anchor": prime < R < 4 * A,
        "anchor_chart": prime * R + 1 == 4 * K and K == A * B,
        "anchor_canonical_chart": canonical_chart(prime, A) == (R, K),
        "minimal_parameters": C % A == 0 and q in (2, 3),
        "phase_relation": q * r == B + prime * h,
        "cofactor_gate": A_target == C and K_target % A_target == 0,
        "r_chart": prime * R_target + 1 == 4 * K_target,
        "target_canonical_chart": canonical_chart(prime, A_target)
        == (R_target, K_target),
        "phase_value": K_target - K == prime * A * h,
        "fixed_n_shadow": anchor_defect == q * target_defect
        and n_target == n
        and A_target == q * A,
        "residual_mod_4": n % 4 == 1 and n_target % 4 == 1,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"minimal phase checks failed: {failed}")

    return {
        "phase": h,
        "q": q,
        "anchor": {"A": A, "B": B, "R": R, "K": K, "n": n},
        "arithmetic_source_only": {
            "M": M,
            "k": k,
            "r": r,
            "C": C,
            "d_source": d_source,
            "n_source": n_source,
            "R_source": R_source,
            "K_source": K_source,
        },
        "target": {
            "A": A_target,
            "R": R_target,
            "K": K_target,
            "n": n_target,
            "target_defect": target_defect,
            "s": s,
        },
        "checks": checks,
    }


def audit_bradford_gap(prime: int, gap: int) -> dict[str, object]:
    if gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise ValueError("gap is outside the Bradford domain")
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise AssertionError("gap does not give an integral first denominator")
    divisors = square_divisors(x)
    type_i_target = (-prime * x) % gap
    type_ii_target = (-x) % gap
    type_i_hits = [divisor for divisor in divisors if divisor % gap == type_i_target]
    type_ii_hits = [
        divisor
        for divisor in divisors
        if divisor <= x and divisor % gap == type_ii_target
    ]
    return {
        "gap": gap,
        "x": x,
        "x_factorization": [list(pair) for pair in factorization(x)],
        "divisor_residues": sorted({divisor % gap for divisor in divisors}),
        "type_i_target_residue": type_i_target,
        "type_ii_target_residue": type_ii_target,
        "type_i_hits": type_i_hits,
        "type_ii_hits": type_ii_hits,
    }


def type_i_certificate(prime: int, gap: int, divisor: int) -> dict[str, int]:
    x = (prime + gap) // 4
    if x * x % divisor or (prime * x + divisor) % gap:
        raise AssertionError("not a Type I divisor")
    y = (prime * x + divisor) // gap
    z_numerator = prime * (x + prime * x * x // divisor)
    if z_numerator % gap:
        raise AssertionError("Type I third denominator is not integral")
    z = z_numerator // gap
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("Type I certificate identity failed")
    return {"gap": gap, "x": x, "divisor": divisor, "y": y, "z": z}


def build_result() -> dict[str, object]:
    prime = 1201
    inputs = (
        MinimalPhaseInput(phase=1, support=319, target_defect=8, source_multiplier=135),
        MinimalPhaseInput(phase=2, support=346, target_defect=35, source_multiplier=82),
    )
    phase_rows = [verify_minimal_phase(prime, item) for item in inputs]
    for item, row in zip(inputs, phase_rows, strict=True):
        source = row["arithmetic_source_only"]
        if not isinstance(source, dict) or source["k"] != item.source_multiplier:
            raise AssertionError("frozen source multiplier changed")

    small_gaps = [audit_bradford_gap(prime, gap) for gap in range(3, 23, 4)]
    if any(row["type_i_hits"] or row["type_ii_hits"] for row in small_gaps):
        raise AssertionError("a Bradford gap below 23 unexpectedly hit")

    first_certificate = type_i_certificate(prime, 23, 34)
    if first_certificate != {
        "gap": 23,
        "x": 306,
        "divisor": 34,
        "y": 15980,
        "z": 172727820,
    }:
        raise AssertionError("frozen first Type I certificate changed")

    return {
        "schema_version": 1,
        "certificate_type": "high_anchor_positive_phase_terminal_boundary_v1",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "prime": prime,
        "scope": {
            "positive_phases": [1, 2],
            "arithmetic_only": True,
            "not_verified": [
                "source_path_provenance",
                "charged_parent_receipt",
                "F_G_fiber_lift",
                "global_E1_E5_edge",
            ],
        },
        "minimal_phase_charts": phase_rows,
        "Bradford_gaps_below_23": small_gaps,
        "first_type_i_certificate": first_certificate,
        "conclusion": {
            "all_Bradford_gaps_3_through_19_miss": True,
            "first_Bradford_hit_gap": 23,
            "positive_phase_does_not_force_gap_below_23_terminal": True,
            "not_an_Erdos_Straus_counterexample": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if not args.verify:
        args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "prime": result["prime"],
                "phases": result["scope"]["positive_phases"],
                "small_gap_count": len(result["Bradford_gaps_below_23"]),
                "first_Bradford_hit_gap": result["conclusion"]["first_Bradford_hit_gap"],
                "selector_status": result["selector_status"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
