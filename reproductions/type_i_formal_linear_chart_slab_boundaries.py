#!/usr/bin/env python3
"""Verify focused p-edge and linear large-slab boundary examples."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-formal-linear-chart-slab-boundaries-results.json"
)

SLAB_CASES = (
    {
        "prime": 241,
        "R": 7,
        "source_a": 30,
        "source_s": 1,
        "Q": 5,
        "alpha": 1,
        "beta": 2,
    },
    {
        "prime": 193,
        "R": 15,
        "source_a": 12,
        "source_s": 1,
        "Q": 7,
        "alpha": 2,
        "beta": 1,
    },
    {
        "prime": 337,
        "R": 23,
        "source_a": 14,
        "source_s": 1,
        "Q": 7,
        "alpha": 3,
        "beta": 2,
    },
)


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d:
            continue
        low.append(d)
        if d * d != n:
            high.append(n // d)
    return low + high[::-1]


def formal_transition(
    pair: tuple[int, int], layer: int, R: int, q: int
) -> tuple[tuple[int, int], int]:
    A, B = pair
    if A % q:
        A, B = B, A
    assert A % q == 0 and B % q != 0
    assert R % q != 0 and layer % q != 0
    t = (-layer) % q
    assert 1 <= t < q
    A0 = A // q
    B0 = (B + R * t) // q
    layer0 = (layer + t) // q
    g = gcd(A0, B0)
    assert layer0 % g == 0
    return tuple(sorted((A0 // g, B0 // g))), layer0 // g


def canonical_chart(prime: int, M: int) -> tuple[int, int]:
    R_M = (-pow(prime, -1, 4 * M)) % (4 * M)
    assert 1 <= R_M < 4 * M
    K_M = (prime * R_M + 1) // 4
    assert R_M % 4 == 3 and K_M % M == 0
    return R_M, K_M


def analyze_slab(case: dict[str, int]) -> dict[str, object]:
    prime = case["prime"]
    R = case["R"]
    source_a = case["source_a"]
    source_s = case["source_s"]
    Q = case["Q"]
    alpha = case["alpha"]
    beta = case["beta"]
    X = Q * alpha
    Y = beta
    K = (prime * R + 1) // 4
    L = X * Y

    assert prime % 24 == 1
    assert prime == source_a + source_s + source_a * source_s * R
    assert R <= prime - 2
    assert X + Y == R and gcd(X, Y) == 1
    assert alpha * beta > 0 and K % (alpha * beta) == 0
    assert K % Q != 0 and 4 * Q > R
    assert alpha in (1, 2, 3)

    collision_T = [
        T
        for T in divisors(R)
        if (prime + T) % (4 * L) == 0
        or (prime * T + 1) % (4 * L) == 0
    ]
    absorption = []
    for M in divisors(L):
        if M % Q:
            continue
        R_M, K_M = canonical_chart(prime, M)
        d = M // Q
        rho_d = ((K // d) * pow(prime, -1, Q)) % Q
        assert 1 <= rho_d < Q
        formula_R = (
            R - 4 * d * rho_d
            if 4 * d * rho_d < R
            else R + 4 * d * (Q - rho_d)
        )
        assert R_M == formula_R
        absorption.append(
            {
                "M": M,
                "d": d,
                "rho_d": rho_d,
                "R_M": R_M,
                "K_M": K_M,
                "decreases_R": R_M < R,
            }
        )
    assert not collision_T
    assert not any(item["decreases_R"] for item in absorption)
    Q_chart = next(item for item in absorption if item["M"] == Q)
    c = (prime * Q_chart["R_M"] + 1) // (4 * Q)
    for item in absorption:
        d = item["d"]
        assert item["R_M"] >= Q_chart["R_M"]
        assert (item["R_M"] - Q_chart["R_M"]) % (4 * Q) == 0
        kappa_d = (item["R_M"] - Q_chart["R_M"]) // (4 * Q)
        assert 0 <= kappa_d < d
        assert kappa_d == (-c * pow(prime, -1, d)) % d
        item["kappa_d"] = kappa_d
    assert any(item["decreases_R"] for item in absorption) == Q_chart[
        "decreases_R"
    ]

    q = next(d for d in range(2, Q + 1) if Q % d == 0)
    q_power = Q
    while q_power % q == 0:
        q_power //= q
    assert q_power == 1
    peeling = [{"pair": sorted((X, Y)), "layer": 1}]
    pair = tuple(sorted((X, Y)))
    current_Q = Q
    while current_Q > 1:
        pair, layer = formal_transition(pair, 1, R, q)
        assert layer == 1
        current_Q //= q
        expected_pair = tuple(sorted((current_Q * alpha, R - current_Q * alpha)))
        assert pair == expected_pair
        peeling.append({"pair": list(pair), "layer": layer})
    assert pair == tuple(sorted((alpha, R - alpha)))

    return {
        **case,
        "K": K,
        "X": X,
        "Y": Y,
        "L": L,
        "collision_T": collision_T,
        "absorption": absorption,
        "peeling": peeling,
        "anchor": [alpha, R - alpha],
    }


def verify_p_cycle_boundary() -> dict[str, object]:
    prime = 73
    R = 75
    K = (prime * R + 1) // 4
    pair = (2, 73)
    labels = (73, 2, 19)
    nodes = [list(pair)]
    for q in labels:
        pair, layer = formal_transition(pair, 1, R, q)
        assert layer == 1
        nodes.append(list(pair))
    assert pair == (2, 73)
    return {"prime": prime, "R": R, "K": K, "labels": list(labels), "nodes": nodes}


def verify_linear_high_layer_p_edge() -> dict[str, object]:
    prime = 73
    R = 3
    K = 55
    pair = (1, 11**7)
    layer = sum(pair) // R
    labels = (11, 2, 73)
    nodes = [{"pair": list(pair), "layer": layer}]
    for q in labels:
        pair, layer = formal_transition(pair, layer, R, q)
        nodes.append({"pair": list(pair), "layer": layer})
    assert nodes[-1] == {"pair": [1, 12134], "layer": 4045}
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "labels": list(labels),
        "nodes": nodes,
    }


def verify_unique_self_loop_example() -> dict[str, object]:
    prime = 73
    R = 3
    K = 55
    pair, layer = formal_transition((1, 2), 1, R, 2)
    assert pair == (1, 2) and layer == 1
    return {"prime": prime, "R": R, "K": K, "Q": 2, "pair": list(pair)}


def verify_unphased_chart_two_cycle() -> dict[str, object]:
    prime = 73
    source = {"a": 2, "s": 1, "R": 35}
    sink = {"a": 1, "s": 1, "R": 71}
    Q = 2
    assert prime == source["a"] + source["s"] + source["a"] * source["s"] * source["R"]
    assert sink["a"] == source["a"] // Q
    assert sink["R"] == Q * source["R"] + (Q - 1) // source["s"]
    assert prime == sink["a"] + sink["s"] + sink["a"] * sink["s"] * sink["R"]
    source_K = (prime * source["R"] + 1) // 4
    sink_K = (prime * sink["R"] + 1) // 4
    assert (source_K, sink_K) == (639, 1296)

    t = (prime - 1) // 4
    u = t // Q
    reverse_R = 4 * u - 1
    reverse_K = u * (prime - Q)
    assert (reverse_R, reverse_K) == (source["R"], source_K)
    return {
        "prime": prime,
        "Q": Q,
        "source": {**source, "K": source_K},
        "sink": {**sink, "K": sink_K},
        "reverse_R": reverse_R,
        "reverse_K": reverse_K,
    }


def verify_terminal_free_binary_self_loop() -> dict[str, object]:
    prime = 1009
    R = 3
    K = (prime * R + 1) // 4
    assert K == 757
    target = (-K) % R
    center_divisors = divisors(K * K)
    assert not [d for d in center_divisors if d < K and d % R == target]
    pair, layer = formal_transition((1, 2), 1, R, 2)
    assert pair == (1, 2) and layer == 1
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "center_target": target,
        "center_divisors_below_K": [d for d in center_divisors if d < K],
        "pair": list(pair),
    }


def run() -> dict[str, object]:
    slab_records = [analyze_slab(case) for case in SLAB_CASES]
    observed = [
        (
            record["alpha"],
            record["prime"],
            record["R"],
            [(item["M"], item["R_M"]) for item in record["absorption"]],
            record["anchor"],
        )
        for record in slab_records
    ]
    expected = [
        (1, 241, 7, [(5, 19), (10, 39)], [1, 6]),
        (2, 193, 15, [(7, 19), (14, 47)], [2, 13]),
        (3, 337, 23, [(7, 27), (14, 55), (21, 83), (42, 167)], [3, 20]),
    ]
    if observed != expected:
        raise AssertionError(f"focused linear slab boundary changed: {observed}")

    return {
        "schema_version": "formal-linear-chart-slab-boundaries/v1",
        "scope_note": (
            "Focused exact checks for the p-edge scope boundary and three local "
            "large-slab misses. The slab examples are not asserted to arise from "
            "a specified F-witness Reach graph."
        ),
        "summary": {
            "large_slab_case_count": len(slab_records),
            "covered_alpha": [record["alpha"] for record in slab_records],
            "existing_menu_miss_count": sum(
                not record["collision_T"]
                and not any(item["decreases_R"] for item in record["absorption"])
                for record in slab_records
            ),
            "p_cycle_requires_non_linear_R_ge_p": True,
            "linear_high_layer_p_edge_present": True,
            "unique_binary_self_loop_reproduced": True,
            "unphased_chart_two_cycle_reproduced": True,
            "terminal_free_binary_self_loop_reproduced": True,
        },
        "large_slab_records": slab_records,
        "non_linear_p_cycle": verify_p_cycle_boundary(),
        "linear_high_layer_p_edge": verify_linear_high_layer_p_edge(),
        "binary_self_loop": verify_unique_self_loop_example(),
        "unphased_chart_two_cycle": verify_unphased_chart_two_cycle(),
        "terminal_free_binary_self_loop": verify_terminal_free_binary_self_loop(),
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
