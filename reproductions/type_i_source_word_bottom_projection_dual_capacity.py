#!/usr/bin/env python3
"""Verify focused source-word projection and dual-capacity examples."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)
CLOSURE_SCRIPT = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-source-word-bottom-projection-dual-capacity-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "eb0ef6c4fe5103d907916ebb4d2fc0bc97913344d3cb143e1f17cb582fa0adc2"
)
EXPECTED_CLOSURE_SHA256 = (
    "cd76a4f2c0e602324f87d91ab4be86754feb2c256ab9553a6a05615f91286846"
)

PATH_CASES = (
    {
        "name": "minimum_source_anchored_residual",
        "prime": 5_596_369,
        "R": 35,
        "K": 48_968_229,
        "source": (107, 18_723, 538),
        "first_edge": (79, 1),
        "post_first": (8, 237, 7),
        "U": 237,
        "V": 8,
        "suffix": (
            ((8, 237, 7), 2, 4, (1, 34, 1)),
            ((1, 34, 1), 17, 1, (2, 33, 1)),
            ((2, 33, 1), 11, 1, (3, 32, 1)),
        ),
        "X": 32,
        "Y": 3,
    },
    {
        "name": "alpha_three_four_cycle_entry",
        "prime": 212_973_049,
        "R": 215,
        "K": 11_447_301_384,
        "source": (1_585_081, 2_273_094, 17_945),
        "first_edge": (1_259, 1),
        "post_first": (1_259, 1_966, 15),
        "U": 1_259,
        "V": 1_966,
        "suffix": (
            ((1_259, 1_966, 15), 983, 1, (2, 213, 1)),
        ),
        "X": 213,
        "Y": 2,
    },
)

DELTA_CASES = (
    {
        "name": "both_type_i_and_ii",
        "prime": 5_596_369,
        "R": 35,
        "r": 1,
        "s": 3,
        "expected_delta": 31,
        "divisor": 85,
        "types": ("Type_I", "Type_II"),
    },
    {
        "name": "type_i_only_selected_divisor",
        "prime": 212_973_049,
        "R": 215,
        "r": 2,
        "s": 3,
        "expected_delta": 35,
        "divisor": 66_471,
        "types": ("Type_I",),
    },
    {
        "name": "minimum_core_ambient_counterexample",
        "prime": 73,
        "R": 11,
        "r": 1,
        "s": 4,
        "expected_delta": 3,
        "divisor": None,
        "types": (),
    },
    {
        "name": "complete_gap_miss",
        "prime": 212_973_049,
        "R": 215,
        "r": 3,
        "s": 1,
        "expected_delta": 211,
        "divisor": None,
        "types": (),
    },
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("source_word_dual_capacity_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for divisor in range(1, math.isqrt(n) + 1):
        if n % divisor:
            continue
        low.append(divisor)
        if divisor * divisor != n:
            high.append(n // divisor)
    return low + high[::-1]


def require_edge(
    source: tuple[int, int, int],
    destination: tuple[int, int, int],
    q: int,
    gcd_reduction: int,
    R: int,
    bounds: dict[int, int],
) -> None:
    matches = [
        edge
        for edge in closure.raw_transitions(source, R, bounds)
        if tuple(int(value) for value in edge["destination"]) == destination
        and int(edge["q"]) == q
        and int(edge["gcd_reduction"]) == gcd_reduction
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one edge {source} --{q},{gcd_reduction}--> {destination}"
        )


def bottom_projection(A: int, B: int, layer: int, R: int) -> tuple[int, int]:
    assert math.gcd(A, B) == 1 and A + B == R * layer
    residue = A % R
    assert residue and math.gcd(residue, R) == 1
    r = min(residue, R - residue)
    assert 1 <= r < R / 2
    assert math.gcd(r, R - r) == 1
    return r, R - r


def capacity_deficits(product: int, capacity: int) -> dict[str, int]:
    product_factors = closure.factorization(product)
    capacity_factors = closure.factorization(capacity)
    return {
        str(q): exponent - capacity_factors.get(q, 0)
        for q, exponent in product_factors.items()
        if exponent > capacity_factors.get(q, 0)
    }


def normalized_cross_pair(
    left: int, right: int, R: int
) -> dict[str, int]:
    common = math.gcd(left, right)
    assert math.gcd(common, R) == 1
    P = left // common
    Q = right // common
    assert math.gcd(P, Q) == 1 and (P + Q) % R == 0
    return {
        "common": common,
        "P": P,
        "Q": Q,
        "layer": (P + Q) // R,
        "product": P * Q,
    }


def analyze_path_case(
    case: dict[str, object], frozen_records: list[dict[str, object]]
) -> dict[str, object]:
    prime = int(case["prime"])
    R = int(case["R"])
    K = int(case["K"])
    source = tuple(int(value) for value in case["source"])
    post_first = tuple(int(value) for value in case["post_first"])
    U = int(case["U"])
    V = int(case["V"])
    X = int(case["X"])
    Y = int(case["Y"])
    record_matches = [
        record
        for record in frozen_records
        if int(record["prime"]) == prime and int(record["R"]) == R
    ]
    assert len(record_matches) == 1 and int(record_matches[0]["K"]) == K
    assert 4 * K == prime * R + 1
    bounds = closure.factorization(K)

    first_q, first_g = (int(value) for value in case["first_edge"])
    require_edge(source, post_first, first_q, first_g, R, bounds)
    assert U + V == R * post_first[2]
    assert sorted((U, V)) == sorted(post_first[:2])

    theta = 1
    suffix_rows: list[dict[str, object]] = []
    for source_node, q, common, destination in case["suffix"]:
        source_node = tuple(int(value) for value in source_node)
        destination = tuple(int(value) for value in destination)
        q = int(q)
        common = int(common)
        require_edge(source_node, destination, q, common, R, bounds)
        theta *= q * common
        suffix_rows.append(
            {
                "source": list(source_node),
                "q": q,
                "gcd_reduction": common,
                "destination": list(destination),
            }
        )

    endpoint = tuple(int(value) for value in case["suffix"][-1][3])
    assert sorted((X, Y)) == sorted(endpoint[:2]) and X + Y == R
    assert (theta * X - U) % R == 0
    assert (theta * Y - V) % R == 0
    u = (theta * X - U) // R
    v = (theta * Y - V) // R
    assert u >= 0 and v >= 0
    assert u + v + post_first[2] == theta

    cross_pairs = (
        normalized_cross_pair(U, theta * Y, R),
        normalized_cross_pair(V, theta * X, R),
    )
    x_R = (prime + R) // 4
    assert 4 * x_R == prime + R and 3 <= R <= prime - 2
    for pair in cross_pairs:
        product = int(pair["product"])
        pair["divides_K"] = K % product == 0
        pair["divides_x_R"] = x_R % product == 0
        pair["K_deficits"] = capacity_deficits(product, K)
        pair["x_R_deficits"] = capacity_deficits(product, x_R)
        assert not pair["divides_K"] and pair["K_deficits"]
        assert not pair["divides_x_R"] and pair["x_R_deficits"]

    same_modulus_candidates = [
        mu for mu in divisors(R) if mu % 4 == 3
    ]
    size_threshold = 2 * math.sqrt(prime) - 1
    assert same_modulus_candidates
    assert all(mu <= size_threshold for mu in same_modulus_candidates)

    return {
        "name": str(case["name"]),
        "prime": prime,
        "R": R,
        "K": K,
        "source": list(source),
        "post_first_oriented": [U, V, post_first[2]],
        "suffix_edges": suffix_rows,
        "endpoint_oriented": [X, Y, 1],
        "theta": theta,
        "u": u,
        "v": v,
        "bottom_projection_of_post_first": list(
            bottom_projection(U, V, post_first[2], R)
        ),
        "cross_pairs": list(cross_pairs),
        "x_R": x_R,
        "same_modulus_d_only_size_obstruction": {
            "mu_candidates": same_modulus_candidates,
            "necessary_lower_bound": "mu > 2*sqrt(p)-1",
            "threshold_approx": size_threshold,
            "all_candidates_excluded": True,
        },
    }


def analyze_delta_case(case: dict[str, object]) -> dict[str, object]:
    prime = int(case["prime"])
    R = int(case["R"])
    r = int(case["r"])
    s = int(case["s"])
    assert 1 <= r < R / 2 and 1 <= s < R / 2
    common = math.gcd(r * s, (R - r) * (R - s))
    assert math.gcd(common, R) == 1
    assert (R - r - s) % common == 0
    delta = (R - r - s) // common
    P = r * s // common
    Q = (R - r) * (R - s) // common
    assert math.gcd(P, Q) == 1 and Q - P == R * delta
    assert delta == int(case["expected_delta"]) and 1 <= delta < R

    cross_left = r * (R - s)
    cross_right = (R - r) * s
    cross_common = math.gcd(cross_left, cross_right)
    assert math.gcd(cross_common, R) == 1
    assert (cross_right - cross_left) == R * (s - r)
    assert abs(s - r) % cross_common == 0
    cross_delta = abs(s - r) // cross_common
    assert abs(cross_right - cross_left) // cross_common == R * cross_delta
    assert 0 <= cross_delta < R

    selected: list[dict[str, object]] = []
    divisor_value = case["divisor"]
    if divisor_value is None:
        assert closure.exact_gap_certificate(prime, delta) is None
    else:
        divisor = int(divisor_value)
        x = (prime + delta) // 4
        for certificate_type in case["types"]:
            if certificate_type == "Type_I":
                certificate = closure.type_i_certificate(prime, delta, x, divisor)
            elif certificate_type == "Type_II":
                certificate = closure.type_ii_certificate(prime, delta, x, divisor)
            else:
                raise AssertionError(f"unknown certificate type {certificate_type}")
            assert certificate is not None
            selected.append(certificate)
        assert closure.exact_gap_certificate(prime, delta) is not None

    return {
        "name": str(case["name"]),
        "prime": prime,
        "R": R,
        "bottom_coordinates": [[r, R - r], [s, R - s]],
        "gcd_normalization": common,
        "difference_pair": [P, Q],
        "delta": delta,
        "cross_gcd_normalization": cross_common,
        "cross_difference_pair": [
            cross_left // cross_common,
            cross_right // cross_common,
        ],
        "cross_delta": cross_delta,
        "complete_gap_hit": divisor_value is not None,
        "selected_certificates": selected,
    }


def fixed_tail_size_boundary() -> dict[str, int]:
    prime = 5_596_369
    K = 48_968_229
    alpha = 1
    beta = 3
    c = K // (alpha * beta)
    U = alpha * c
    h = 4 * U - prime
    minimum_lambda = math.isqrt(prime) // 2 + 1
    assert 4 * minimum_lambda * minimum_lambda > prime
    if minimum_lambda > 1:
        assert 4 * (minimum_lambda - 1) ** 2 < prime
    minimum_delta = minimum_lambda * h - U
    assert (U, h, minimum_lambda, minimum_delta) == (
        16_322_743,
        59_694_603,
        1_183,
        70_602_392_606,
    )
    return {
        "prime": prime,
        "U": U,
        "h": h,
        "minimum_lambda_from_H_gt_p": minimum_lambda,
        "minimum_delta": minimum_delta,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("frozen Psi-one input hash changed")
    if sha256(CLOSURE_SCRIPT) != EXPECTED_CLOSURE_SHA256:
        raise AssertionError("formal closure script hash changed")
    frozen = json.loads(INPUT.read_text(encoding="utf-8"))
    path_records = [
        analyze_path_case(case, frozen["records"]) for case in PATH_CASES
    ]
    delta_records = [analyze_delta_case(case) for case in DELTA_CASES]
    observed = [
        (
            record["prime"],
            record["R"],
            record["theta"],
            record["u"],
            record["v"],
            [pair["product"] for pair in record["cross_pairs"]],
        )
        for record in path_records
    ]
    expected = [
        (5_596_369, 35, 1_496, 1_361, 128, [118_184, 5_984]),
        (212_973_049, 215, 983, 968, 0, [2_475_194, 426]),
    ]
    if observed != expected:
        raise AssertionError(f"focused source-word boundary changed: {observed}")

    return {
        "schema_version": "type-i-source-word-bottom-dual-capacity/v1",
        "scope_note": (
            "Focused exact verification of two frozen source paths, two-node "
            "difference normalization, dual K/x_R capacity misses, and one "
            "complete exact-gap counterexample. It is not a universal selector "
            "or a formal-edge-to-E4 upgrade."
        ),
        "inputs": {
            "frozen_psi_one_sha256": EXPECTED_INPUT_SHA256,
            "formal_closure_sha256": EXPECTED_CLOSURE_SHA256,
        },
        "summary": {
            "path_case_count": len(path_records),
            "cross_pair_count": sum(
                len(record["cross_pairs"]) for record in path_records
            ),
            "delta_case_count": len(delta_records),
            "delta_terminal_count": sum(
                bool(record["complete_gap_hit"]) for record in delta_records
            ),
            "delta_complete_miss_count": sum(
                not bool(record["complete_gap_hit"]) for record in delta_records
            ),
        },
        "path_records": path_records,
        "delta_records": delta_records,
        "fixed_tail_d_only_size_boundary": fixed_tail_size_boundary(),
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
