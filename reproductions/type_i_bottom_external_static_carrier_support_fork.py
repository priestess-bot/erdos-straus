#!/usr/bin/env python3
"""Verify the bottom external-support fork and static-carrier boundaries."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CLOSURE_SCRIPT = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-bottom-external-static-carrier-support-fork-results.json"
)
EXPECTED_CLOSURE_SHA256 = (
    "cd76a4f2c0e602324f87d91ab4be86754feb2c256ab9553a6a05615f91286846"
)

Node = tuple[int, int, int]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("static_support_fork_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> dict[int, int]:
    return closure.factorization(value)


def factorization_json(value: int) -> dict[str, int]:
    return {str(q): e for q, e in factorization(value).items()}


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def modular_product(exponents: dict[int, int], modulus: int) -> int:
    result = 1
    for base, exponent in exponents.items():
        if exponent >= 0:
            result = result * pow(base, exponent, modulus) % modulus
        else:
            result = result * pow(pow(base, -1, modulus), -exponent, modulus) % modulus
    return result


def verify_edge(source: Node, destination: Node, q: int, R: int, K: int) -> None:
    matches = [
        edge
        for edge in closure.raw_transitions(source, R, factorization(K))
        if tuple(int(value) for value in edge["destination"]) == destination
        and int(edge["q"]) == q
        and int(edge["gcd_reduction"]) == 1
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one raw edge {source} --{q}--> {destination}")


def exact_external_hits(node: Node, prime: int, R: int, K: int) -> list[int]:
    gaps, _origins = closure.external_gap_candidates({node}, prime, K)
    return [
        gap for gap in gaps if closure.exact_gap_certificate(prime, gap) is not None
    ]


def support_fork_profile(prime: int, R: int, node: Node, q: int) -> dict[str, object]:
    K = (prime * R + 1) // 4
    if q in factorization(K):
        raise AssertionError("fork prime must be outside K support")
    left, right, layer = node
    if layer != 1 or left + right != R or math.gcd(left, right) != 1:
        raise AssertionError("fork requires a primitive bottom node")
    if left % q == 0:
        selected, other = left, right
        selected_side = "left"
    elif right % q == 0:
        selected, other = right, left
        selected_side = "right"
    else:
        raise AssertionError("fork prime did not divide either coordinate")
    exponent = valuation(selected, q)
    Q = q**exponent
    alpha = selected // Q
    residual = alpha * other
    if math.gcd(Q, residual) != 1:
        raise AssertionError("full external prime power was not removed")
    competing = [
        r
        for r, exponent_r in factorization(residual).items()
        if exponent_r > valuation(K, r)
    ]
    raw_labels = sorted(
        {
            int(edge["q"])
            for edge in closure.raw_transitions(node, R, factorization(K))
        }
    )
    payload: dict[str, object] = {
        "prime": prime,
        "R": R,
        "K": K,
        "node": list(node),
        "selected_side": selected_side,
        "q": q,
        "exponent": exponent,
        "Q": Q,
        "alpha": alpha,
        "beta": other,
        "residual_product": residual,
        "residual_divides_K": K % residual == 0,
        "competing_excess_primes": competing,
        "raw_out_labels": raw_labels,
    }
    if competing:
        if K % residual == 0 or any(r == q or r not in raw_labels for r in competing):
            raise AssertionError("competing-excess fork changed")
        payload["branch"] = "COMPETING_EXCESS"
        return payload
    if K % residual:
        raise AssertionError("unsupported residual lost its competing prime")

    R_Q = (-pow(prime, -1, 4 * Q)) % (4 * Q)
    K_Q = (prime * R_Q + 1) // 4
    if R_Q == R or K_Q % Q:
        raise AssertionError("canonical slab chart changed")
    L = selected * other
    direct = [T for T in closure.divisors(R) if (prime + T) % (4 * L) == 0]
    cross = [T for T in closure.divisors(R) if (prime * T + 1) % (4 * L) == 0]
    anchor = tuple(sorted((alpha, R - alpha))) + (1,)
    center_size, center_hits = closure.centered_type_i_hits(prime, R_Q, K_Q)
    payload.update(
        {
            "branch": "VERIFIED_ABSORB" if R_Q < R else "LARGE_SLAB",
            "R_Q": R_Q,
            "K_Q": K_Q,
            "Q_over_R_fourth": 4 * Q > R,
            "large_alpha_class": alpha if R_Q > R else None,
            "direct_collision_T": direct,
            "cross_collision_T": cross,
            "node_external_hits": exact_external_hits(node, prime, R, K),
            "anchor": list(anchor),
            "anchor_external_hits": exact_external_hits(anchor, prime, R, K),
            "new_centered_space_size": center_size,
            "new_centered_hits": center_hits,
        }
    )
    if R_Q > R and (4 * Q <= R or alpha not in (1, 2, 3)):
        raise AssertionError("large-slab compression changed")
    return payload


def static_cycle_profile(prime: int) -> dict[str, object]:
    R = 207
    K = (prime * R + 1) // 4
    x_R = (prime + R) // 4
    U, V = 68, 139
    X, Y = 2, 205
    theta = 139 * 103
    cycle_Q = 41 * 101
    d_U = valuation(U, 103) - valuation(theta * Y, 103)
    d_V = valuation(V, 103) - valuation(theta * X, 103)
    budgets = {"K": valuation(K, 103), "x_R": valuation(x_R, 103)}
    if (d_U, d_V, valuation(cycle_Q, 103), budgets) != (
        -1,
        -1,
        0,
        {"K": 0, "x_R": 0},
    ):
        raise AssertionError("four-channel static receipt changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "x_R": x_R,
        "source_ancestry": [U, V],
        "endpoint": [X, Y],
        "theta": theta,
        "cycle_Q": cycle_Q,
        "q": 103,
        "d_U": d_U,
        "d_V": d_V,
        "budgets": budgets,
        "receipt": "four_channel_MISS_STATIC",
    }


def verify_skeleton(prime: int) -> None:
    R = 207
    K = (prime * R + 1) // 4
    for source, destination, q in (
        ((1_156, 1_535, 13), (68, 139, 1), 17),
        ((68, 139, 1), (1, 206, 1), 139),
        ((1, 206, 1), (2, 205, 1), 103),
        ((2, 205, 1), (5, 202, 1), 41),
        ((5, 202, 1), (2, 205, 1), 101),
    ):
        verify_edge(source, destination, q, R, K)


def p2017_profile() -> dict[str, object]:
    prime, R = 2_017, 207
    verify_skeleton(prime)
    q103 = support_fork_profile(prime, R, (1, 206, 1), 103)
    q101 = support_fork_profile(prime, R, (5, 202, 1), 101)
    if q103["branch"] != "VERIFIED_ABSORB" or q103["R_Q"] != 115:
        raise AssertionError("p=2017 q=103 absorption changed")
    if q103["new_centered_hits"]:
        raise AssertionError("p=2017 q=103 chart unexpectedly became terminal")
    if (
        q101["branch"] != "VERIFIED_ABSORB"
        or q101["R_Q"] != 135
        or not q101["new_centered_hits"]
        or q101["new_centered_hits"][0]["gap"] != 3
    ):
        raise AssertionError("p=2017 q=101 direct exit changed")
    gap15 = []
    x15 = (prime + 15) // 4
    for divisor in closure.divisors(x15 * x15):
        for function in (closure.type_i_certificate, closure.type_ii_certificate):
            certificate = function(prime, 15, x15, divisor)
            if certificate is not None:
                gap15.append(certificate)
    if {certificate["type"] for certificate in gap15} != {"Type_I", "Type_II"}:
        raise AssertionError("p=2017 gap-15 terminal boundary changed")
    return {
        "prime": prime,
        "static_cycle": static_cycle_profile(prime),
        "q103_birth_slab": q103,
        "q101_cycle_slab": q101,
        "gap15_certificates": gap15,
        "correct_semantics": (
            "ray-static but prefix-absorbable and globally terminal; not a "
            "terminal-first-unresolved state"
        ),
    }


def p107722177_profile() -> dict[str, object]:
    prime, R = 107_722_177, 207
    K = (prime * R + 1) // 4
    x_R = (prime + R) // 4
    if factorization(prime) != {prime: 1}:
        raise AssertionError("focused large parameter ceased to be prime")
    if factorization(K) != {2: 2, 5: 1, 17: 1, 307: 1, 53_407: 1}:
        raise AssertionError("focused K factorization changed")
    if factorization(x_R) != {2: 2, 7: 2, 11: 1, 12_491: 1}:
        raise AssertionError("focused x_R factorization changed")
    if 53_407 % R != 1:
        raise AssertionError("identity-residue K extension changed")
    verify_skeleton(prime)
    center_size, center_hits = closure.centered_type_i_hits(prime, R, K)
    if center_size != 405 or center_hits:
        raise AssertionError("focused state ceased to be centered F")
    q103 = support_fork_profile(prime, R, (1, 206, 1), 103)
    if (
        q103["branch"] != "LARGE_SLAB"
        or q103["R_Q"] != 375
        or q103["large_alpha_class"] != 2
        or q103["direct_collision_T"]
        or q103["cross_collision_T"]
        or q103["node_external_hits"]
        or q103["anchor_external_hits"]
        or q103["new_centered_hits"]
        or closure.exact_gap_certificate(prime, 103) is not None
    ):
        raise AssertionError("focused q=103 strong local miss changed")
    q41 = support_fork_profile(prime, R, (2, 205, 1), 41)
    q101 = support_fork_profile(prime, R, (5, 202, 1), 101)
    if (
        q41["branch"] != "VERIFIED_ABSORB"
        or q41["R_Q"] != 35
        or not q41["new_centered_hits"]
    ):
        raise AssertionError("global q=41 caveat changed")
    if q101["R_Q"] != 327 or not q101["new_centered_hits"]:
        raise AssertionError("global q=101 caveat changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "K_factorization": factorization_json(K),
        "x_R": x_R,
        "x_R_factorization": factorization_json(x_R),
        "centered_square_space_size": center_size,
        "centered_hits": [],
        "static_cycle": static_cycle_profile(prime),
        "q103_static_birth_slab": q103,
        "q41_alternative_cycle_exit": q41,
        "q101_alternative_cycle_exit": q101,
        "correct_semantics": (
            "counterexample only to a prescribed static prime forcing its own "
            "local terminal or absorption; the SCC has other exits"
        ),
    }


def competing_excess_profile() -> dict[str, object]:
    prime, R = 5_596_369, 35
    K = (prime * R + 1) // 4
    profile = support_fork_profile(prime, R, (8, 27, 1), 2)
    verify_edge((8, 27, 1), (4, 31, 1), 2, R, K)
    verify_edge((8, 27, 1), (9, 26, 1), 3, R, K)
    if (
        profile["branch"] != "COMPETING_EXCESS"
        or profile["Q"] != 8
        or profile["residual_product"] != 27
        or profile["competing_excess_primes"] != [3]
    ):
        raise AssertionError("competing-excess example changed")
    return profile


def full_fiber_forced_height_boundary() -> dict[str, object]:
    R = 207
    support = (2, 5, 17, 307, 139, 41, 101)
    budgets = {2: 2, 5: 1, 17: 1, 307: 1, 139: 1, 41: 0, 101: 0}
    witnesses = {
        2: {5: -1, 307: 2, 139: 1},
        5: {2: -2, 17: -1, 139: 1},
        17: {2: -1, 5: 1, 41: 1},
        307: {2: -1, 5: 1, 41: 1},
        139: {2: -1, 5: 1, 41: 1},
        41: {2: -1, 5: 1, 101: -1},
        101: {2: -1, 5: 1, 41: 1},
    }
    rows = []
    for avoided in support:
        witness = witnesses[avoided]
        if witness.get(avoided, 0) != 0 or modular_product(witness, R) != R - 1:
            raise AssertionError("coordinate-avoidance target witness changed")
        rows.append(
            {
                "avoided_prime": avoided,
                "witness": {str(q): exponent for q, exponent in witness.items()},
                "target_residue": R - 1,
                "avoided_coordinate_overflow": max(
                    abs(witness.get(avoided, 0)) - budgets[avoided], 0
                ),
            }
        )
    if any(row["avoided_coordinate_overflow"] for row in rows):
        raise AssertionError("single-coordinate forced-height boundary changed")
    return {
        "R": R,
        "support": list(support),
        "joint_budgets": {str(q): budgets[q] for q in support},
        "coordinate_avoidance_witnesses": rows,
        "forced_height_by_coordinate": {str(q): 0 for q in support},
        "support_expansion_corollary": (
            "adding q=103 with exponent zero also has forced height zero"
        ),
        "path_fiber_distinction": (
            "the restricted path language has MISS_STATIC(103), while the full "
            "target fiber has zero forced height in every coordinate"
        ),
    }


def positive_multicoordinate_price_example() -> dict[str, object]:
    prime, R = 214_729, 43
    K = (prime * R + 1) // 4
    if K != 151 * 15_287 or 151 % R != 22 or 15_287 % R != 22:
        raise AssertionError("two-coordinate price example changed")
    if pow(22, 14, R) != 1 or any(pow(22, d, R) == 1 for d in (1, 2, 7)):
        raise AssertionError("common generator no longer has order 14")
    candidates = []
    for z1 in range(-14, 15):
        for z2 in range(-14, 15):
            if modular_product({151: z1, 15_287: z2}, R) != R - 1:
                continue
            candidates.append((max(abs(z1) - 1, 0), max(abs(z2) - 1, 0)))
    pareto = sorted(
        {
            point
            for point in candidates
            if not any(
                other != point
                and other[0] <= point[0]
                and other[1] <= point[1]
                for other in candidates
            )
        }
    )
    expected = [(k, 5 - k) for k in range(6)]
    if pareto != expected:
        raise AssertionError(f"two-coordinate Pareto boundary changed: {pareto}")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "generators": [151, 15_287],
        "budgets": [1, 1],
        "unsigned_pareto": [list(point) for point in pareto],
        "single_coordinate_forced_heights": [0, 0],
        "minimum_unit_weight_price": min(sum(point) for point in pareto),
    }


def run() -> dict[str, object]:
    closure_hash = sha256(CLOSURE_SCRIPT)
    if closure_hash != EXPECTED_CLOSURE_SHA256:
        raise AssertionError(f"formal closure helper changed: {closure_hash}")
    p2017 = p2017_profile()
    p107 = p107722177_profile()
    competing = competing_excess_profile()
    fiber = full_fiber_forced_height_boundary()
    price = positive_multicoordinate_price_example()
    summary = {
        "support_fork_branches_verified": [
            p2017["q103_birth_slab"]["branch"],
            p107["q103_static_birth_slab"]["branch"],
            competing["branch"],
        ],
        "four_channel_static_profiles": 2,
        "static_local_counterexamples": 1,
        "alternative_global_exits_in_counterexample": 2,
        "full_fiber_zero_forced_coordinates": len(
            fiber["forced_height_by_coordinate"]
        ),
        "positive_multicoordinate_price": price["minimum_unit_weight_price"],
    }
    expected = {
        "support_fork_branches_verified": [
            "VERIFIED_ABSORB",
            "LARGE_SLAB",
            "COMPETING_EXCESS",
        ],
        "four_channel_static_profiles": 2,
        "static_local_counterexamples": 1,
        "alternative_global_exits_in_counterexample": 2,
        "full_fiber_zero_forced_coordinates": 7,
        "positive_multicoordinate_price": 5,
    }
    if summary != expected:
        raise AssertionError(f"focused static-support summary changed: {summary}")
    return {
        "schema_version": "type-i-bottom-external-static-carrier-support-fork/v1",
        "scope_note": (
            "Focused exact verification of the three support-fork branches, two "
            "four-channel static receipts, the p=107722177 local counterexample, "
            "and full-fiber forced-height boundaries. It does not rerun historical "
            "censuses or prove universal sink-SCC escape."
        ),
        "inputs": {
            "formal_closure_script": CLOSURE_SCRIPT.name,
            "sha256": closure_hash,
        },
        "summary": summary,
        "p2017_prefix_absorption_correction": p2017,
        "p107722177_static_large_slab_boundary": p107,
        "competing_excess_branch": competing,
        "full_fiber_forced_height_boundary": fiber,
        "positive_multicoordinate_price_example": price,
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
            json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
