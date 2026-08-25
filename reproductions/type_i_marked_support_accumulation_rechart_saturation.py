#!/usr/bin/env python3
"""Verify focused marked-support rechart and overflow boundaries."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-marked-support-accumulation-rechart-saturation-results.json"
)

ACCUMULATION_CHAIN = (
    {"Q": 2, "q": 2, "e": 1, "alpha": 1, "beta": 1},
    {"Q": 3, "q": 3, "e": 1, "alpha": 1, "beta": 4},
    {"Q": 11, "q": 11, "e": 1, "alpha": 2, "beta": 1},
    {"Q": 23, "q": 23, "e": 1, "alpha": 2, "beta": 1},
)

FORMER_STRONG_MISSES = (
    {"prime": 241, "R": 7, "Q": 5, "q": 5, "e": 1, "alpha": 1, "beta": 2},
    {"prime": 193, "R": 15, "Q": 7, "q": 7, "e": 1, "alpha": 2, "beta": 1},
    {"prime": 337, "R": 23, "Q": 7, "q": 7, "e": 1, "alpha": 3, "beta": 2},
    {
        "prime": 107_722_177,
        "R": 207,
        "Q": 103,
        "q": 103,
        "e": 1,
        "alpha": 2,
        "beta": 1,
    },
    {
        "prime": 214_729,
        "R": 391,
        "Q": 193,
        "q": 193,
        "e": 1,
        "alpha": 2,
        "beta": 5,
    },
    {
        "prime": 21_169,
        "R": 23,
        "Q": 7,
        "q": 7,
        "e": 1,
        "alpha": 3,
        "beta": 2,
    },
)

OVERFLOW_CASES = (
    {
        "prime": 73,
        "R": 63,
        "Q": 31,
        "q": 31,
        "e": 1,
        "alpha": 2,
        "beta": 1,
        "expected_R_M": 107,
        "expected_gap": 51,
    },
    {
        "prime": 241,
        "R": 215,
        "Q": 71,
        "q": 71,
        "e": 1,
        "alpha": 3,
        "beta": 2,
        "expected_R_M": 251,
        "expected_gap": 43,
    },
    {
        "prime": 13_177,
        "R": 12_299,
        "Q": 4_096,
        "q": 2,
        "e": 12,
        "alpha": 3,
        "beta": 11,
        "expected_R_M": 14_647,
        "expected_gap": 3_207,
    },
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def factorization(n: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors.append((n, 1))
    return factors


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    chart_R = (-pow(prime, -1, modulus)) % modulus
    chart_K = (prime * chart_R + 1) // 4
    assert 1 <= chart_R < modulus
    assert chart_R % 4 == 3
    assert chart_K % support == 0
    return chart_R, chart_K


def centered_classification(
    R: int, factors: list[tuple[int, int]]
) -> dict[str, object]:
    primes = [prime for prime, _ in factors]
    exponent_ranges = [
        range(-exponent, exponent + 1) for _, exponent in factors
    ]
    target = (-1) % R
    witnesses: list[tuple[int, ...]] = []
    residues: set[int] = set()
    for vector in product(*exponent_ranges):
        residue = 1
        for prime, exponent in zip(primes, vector, strict=True):
            residue = residue * pow(prime, exponent, R) % R
        residues.add(residue)
        if residue == target:
            witnesses.append(vector)
    if witnesses:
        witness = min(witnesses, key=lambda row: (sum(map(abs, row)), row))
        return {
            "type": "hit",
            "centered_spectrum_size": len(residues),
            "canonical_witness": list(witness),
        }

    subgroup = {1 % R}
    frontier = [1 % R]
    generators = sorted(
        {prime % R for prime in primes}
        | {pow(prime, -1, R) for prime in primes}
    )
    while frontier:
        residue = frontier.pop()
        for generator in generators:
            successor = residue * generator % R
            if successor not in subgroup:
                subgroup.add(successor)
                frontier.append(successor)
    return {
        "type": "F" if target in subgroup else "G",
        "centered_spectrum_size": len(residues),
        "support_subgroup_size": len(subgroup),
    }


def verify_marked_state(
    prime: int, R: int, K: int, absorbed_support: int
) -> dict[str, object]:
    assert is_prime(prime)
    assert prime % 24 == 1
    assert 3 <= R <= prime - 2
    assert R % 4 == 3
    assert 4 * K == prime * R + 1
    assert K % absorbed_support == 0
    factors = factorization(K)
    rebuilt = 1
    for factor, exponent in factors:
        rebuilt *= factor**exponent
    assert rebuilt == K
    bound = (prime - 1) ** 2 // 4
    assert absorbed_support <= K <= bound
    return {
        "focused_state_key": (
            f"linear_absorbed_support_v1:{prime}:{R}:{absorbed_support}"
        ),
        "prime": prime,
        "R": R,
        "K": K,
        "absorbed_support": absorbed_support,
        "factorization": [[factor, exponent] for factor, exponent in factors],
        "equation_target": [4, prime],
        "marked_solution_set": f"Sol(4,{prime})",
        "normal_form": "linear_chart_with_absorbed_support_v1",
        "potential_bound": bound,
        "potential": bound // absorbed_support,
        "centered_classification": centered_classification(R, factors),
    }


def verify_clean_slab(
    state: dict[str, object], slab: dict[str, int]
) -> None:
    prime = int(state["prime"])
    R = int(state["R"])
    K = int(state["K"])
    Q = slab["Q"]
    q = slab["q"]
    e = slab["e"]
    alpha = slab["alpha"]
    beta = slab["beta"]
    X = Q * alpha
    assert Q == q**e and is_prime(q)
    assert X + beta == R
    assert gcd(X, beta) == 1
    assert K % (alpha * beta) == 0
    assert K % q != 0
    assert Q < R < prime
    assert q != prime


def verify_focused_marked_external_accumulation_edge_v1(
    state: dict[str, object], slab: dict[str, int]
) -> dict[str, object]:
    verify_clean_slab(state, slab)
    prime = int(state["prime"])
    absorbed_support = int(state["absorbed_support"])
    Q = slab["Q"]
    _q = slab["q"]
    assert gcd(absorbed_support, Q) == 1
    combined_support = absorbed_support * Q
    chart_R, chart_K = canonical_chart(prime, combined_support)
    assert chart_R != int(state["R"])

    if chart_R < prime:
        target = verify_marked_state(
            prime, chart_R, chart_K, combined_support
        )
        assert int(target["potential"]) < int(state["potential"])
        return {
            "classification": "verified_marked_support_edge",
            "slab": slab,
            "combined_support": combined_support,
            "source_state_key": state["focused_state_key"],
            "target_state": target,
            "solution_lift": "identity_on_Sol(4,p)",
        }

    assert chart_R > prime
    C, remainder = divmod(chart_K, combined_support)
    assert remainder == 0
    n = 4 * combined_support - chart_R
    d = prime - C
    assert combined_support > prime / 4
    assert 1 <= C <= prime - 1
    assert n > 0 and d > 0
    assert prime * n == 4 * combined_support * d + 1
    assert gcd(combined_support, prime * n) == 1
    return {
        "classification": "marked_support_overflow",
        "slab": slab,
        "combined_support": combined_support,
        "R_M": chart_R,
        "K_M": chart_K,
        "C": C,
        "n": n,
        "d": d,
        "determinant": prime * n,
    }


def one_denominator_spectrum(
    prime: int, Q: int, q: int, e: int
) -> dict[str, object]:
    h = 4 * Q - prime
    rows = []
    for p_exponent in range(3):
        for q_exponent in range(2 * e + 1):
            divisor = prime**p_exponent * q**q_exponent
            hit = (divisor + prime * Q) % h == 0
            rows.append(
                {
                    "p_exponent": p_exponent,
                    "q_exponent": q_exponent,
                    "hit": hit,
                }
            )
    return {
        "gap": h,
        "candidate_count": len(rows),
        "hit_count": sum(bool(row["hit"]) for row in rows),
        "rows": rows,
    }


def analyze_chain() -> dict[str, object]:
    prime = 73
    initial = verify_marked_state(prime, 3, 55, 1)
    states = [initial]
    edges = []
    state = initial
    for slab in ACCUMULATION_CHAIN:
        edge = verify_focused_marked_external_accumulation_edge_v1(state, slab)
        edges.append(edge)
        if edge["classification"] == "marked_support_overflow":
            break
        state = dict(edge["target_state"])
        states.append(state)
    assert [int(state["R"]) for state in states] == [3, 7, 23, 47]
    assert [int(state["absorbed_support"]) for state in states] == [1, 2, 6, 66]
    assert [int(state["potential"]) for state in states] == [1296, 648, 216, 19]
    assert edges[-1]["classification"] == "marked_support_overflow"
    assert (
        edges[-1]["combined_support"],
        edges[-1]["R_M"],
        edges[-1]["C"],
        edges[-1]["n"],
        edges[-1]["d"],
    ) == (1518, 3743, 45, 2329, 28)
    return {"states": states, "edges": edges}


def analyze_former_strong_misses() -> list[dict[str, object]]:
    records = []
    for case in FORMER_STRONG_MISSES:
        prime = case["prime"]
        R = case["R"]
        K = (prime * R + 1) // 4
        state = verify_marked_state(prime, R, K, 1)
        slab = {
            key: case[key]
            for key in ("Q", "q", "e", "alpha", "beta")
        }
        edge = verify_focused_marked_external_accumulation_edge_v1(state, slab)
        assert edge["classification"] == "verified_marked_support_edge"
        records.append(
            {
                **case,
                "R_M": edge["target_state"]["R"],
                "source_potential": state["potential"],
                "target_potential": edge["target_state"]["potential"],
            }
        )
    assert [int(record["R_M"]) for record in records] == [
        19,
        19,
        27,
        375,
        731,
        27,
    ]
    return records


def analyze_overflows() -> list[dict[str, object]]:
    records = []
    for case in OVERFLOW_CASES:
        prime = case["prime"]
        R = case["R"]
        K = (prime * R + 1) // 4
        state = verify_marked_state(prime, R, K, 1)
        slab = {
            key: case[key]
            for key in ("Q", "q", "e", "alpha", "beta")
        }
        edge = verify_focused_marked_external_accumulation_edge_v1(state, slab)
        assert edge["classification"] == "marked_support_overflow"
        assert edge["R_M"] == case["expected_R_M"]
        spectrum = one_denominator_spectrum(
            prime, case["Q"], case["q"], case["e"]
        )
        assert spectrum["gap"] == case["expected_gap"]
        assert spectrum["hit_count"] == 0
        records.append(
            {
                **case,
                "K": K,
                "overflow": edge,
                "one_denominator_spectrum": spectrum,
            }
        )
    return records


def analyze_self_dual_sample() -> dict[str, object]:
    Q = 37
    prime = 2 * Q - 1
    R = Q + 2
    K = (2 * Q * Q + 3 * Q - 1) // 4
    state = verify_marked_state(prime, R, K, 1)
    overflow = verify_focused_marked_external_accumulation_edge_v1(
        state,
        {"Q": Q, "q": Q, "e": 1, "alpha": 1, "beta": 2},
    )
    assert overflow["classification"] == "marked_support_overflow"
    assert overflow["R_M"] == prime + 2
    assert overflow["K_M"] == Q * Q
    assert overflow["n"] == prime
    spectrum = one_denominator_spectrum(prime, Q, Q, 1)
    assert spectrum["hit_count"] == 0

    alternative = verify_focused_marked_external_accumulation_edge_v1(
        state,
        {"Q": 19, "q": 19, "e": 1, "alpha": 2, "beta": 1},
    )
    assert alternative["classification"] == "verified_marked_support_edge"
    assert alternative["target_state"]["R"] == 51
    return {
        "Q": Q,
        "prime": prime,
        "R": R,
        "K": K,
        "same_Q_overflow": overflow,
        "same_Q_spectrum": spectrum,
        "alternative_carrier_R": alternative["target_state"]["R"],
    }


def run() -> dict[str, object]:
    chain = analyze_chain()
    former = analyze_former_strong_misses()
    overflows = analyze_overflows()
    self_dual = analyze_self_dual_sample()
    return {
        "schema_version": "marked-support-accumulation-rechart-saturation/v1",
        "scope_note": (
            "Focused exact verification of the arithmetic state/edge verifier, "
            "one accumulated chain, six reclassified strong misses, and three "
            "overflow spectra. It does not scan historical data or close overflow."
        ),
        "summary": {
            "accepted_chain_edge_count": 3,
            "chain_overflow_count": 1,
            "former_strong_miss_reclassified_count": len(former),
            "overflow_boundary_count": len(overflows),
            "overflow_spectrum_candidate_counts": [
                record["one_denominator_spectrum"]["candidate_count"]
                for record in overflows
            ],
            "overflow_spectrum_hit_count": sum(
                int(record["one_denominator_spectrum"]["hit_count"])
                for record in overflows
            ),
        },
        "accumulation_chain": chain,
        "former_strong_misses": former,
        "overflow_boundaries": overflows,
        "self_dual_sample": self_dual,
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
