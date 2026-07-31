#!/usr/bin/env python3
"""Verify the bottom-word lattice, cycle capacity, and focused boundaries."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
CLOSURE_SCRIPT = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-bottom-word-lattice-pareto-cycle-capacity-results.json"
)
EXPECTED_CLOSURE_SHA256 = (
    "cd76a4f2c0e602324f87d91ab4be86754feb2c256ab9553a6a05615f91286846"
)

Node = tuple[int, int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]
Word = tuple[tuple[str, int], ...]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("bottom_word_cycle_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    if value < 1:
        raise ValueError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> dict[int, int]:
    return closure.factorization(value)


def factorization_json(value: int) -> dict[str, int]:
    return {str(q): e for q, e in factorization(value).items()}


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_vector(matrix: Matrix, vector: tuple[int, int]) -> tuple[int, int]:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def matrix_form(Q: int, A: int, B: int) -> Matrix:
    if min(Q, A, B) < 0 or Q < 1 or A + B != Q - 1:
        raise ValueError("invalid bottom-word normal form")
    return ((A + 1, A), (B, B + 1))


def generator(side: str, q: int) -> Matrix:
    if q < 2:
        raise ValueError("edge label must exceed one")
    if side == "X":
        return ((1, 0), (q - 1, q))
    if side == "Y":
        return ((q, q - 1), (0, 1))
    raise ValueError(f"unknown ancestry side: {side}")


def compress_word(word: Word) -> tuple[int, int, int, Matrix]:
    Q, A, B = 1, 0, 0
    matrix: Matrix = ((1, 0), (0, 1))
    for side, q in word:
        edge = generator(side, q)
        matrix = matrix_multiply(edge, matrix)
        edge_A = 0 if side == "X" else q - 1
        edge_B = q - 1 if side == "X" else 0
        A, B = A + Q * edge_A, B + Q * edge_B
        Q *= q
    expected = matrix_form(Q, A, B)
    if matrix != expected:
        raise AssertionError("word matrix and semigroup recurrence disagreed")
    return Q, A, B, matrix


def ordered_step(X: int, Y: int, R: int, side: str, q: int) -> tuple[int, int]:
    if X + Y != R or math.gcd(X, Y) != 1:
        raise AssertionError("invalid oriented bottom node")
    if side == "X":
        if X % q or math.gcd(q, Y) != 1:
            raise AssertionError("invalid X edge")
        result = X // q, R - X // q
    elif side == "Y":
        if Y % q or math.gcd(q, X) != 1:
            raise AssertionError("invalid Y edge")
        result = R - Y // q, Y // q
    else:
        raise ValueError(f"unknown ancestry side: {side}")
    if math.gcd(*result) != 1:
        raise AssertionError("bottom edge left the primitive layer")
    return result


def word_profile(X: int, Y: int, R: int, word: Word) -> dict[str, object]:
    Q, A, B, matrix = compress_word(word)
    oriented = (X, Y)
    for side, q in word:
        oriented = ordered_step(*oriented, R, side, q)
    scaled = matrix_vector(matrix, (X, Y))
    if scaled != (Q * oriented[0], Q * oriented[1]):
        raise AssertionError("word action failed the scaled-coordinate identity")
    if scaled != (X + A * R, Y + B * R):
        raise AssertionError("word action failed the affine normal form")
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    entry_gcd = math.gcd(*(entry for row in matrix for entry in row))
    if determinant != Q or entry_gcd != 1:
        raise AssertionError("Smith invariants changed")
    roots = [root for root in range(1, R) if (root + A * R) % Q == 0]
    root_bound = math.ceil((R - 1) / Q)
    if len(roots) > root_bound:
        raise AssertionError("root-lattice capacity bound failed")
    return {
        "R": R,
        "root": [X, Y],
        "word": [[side, q] for side, q in word],
        "Q": Q,
        "A": A,
        "B": B,
        "matrix": [list(row) for row in matrix],
        "endpoint": list(oriented),
        "smith_diagonal": [1, Q],
        "admissible_root_congruence_class": roots,
        "root_capacity_bound": root_bound,
    }


def require_edge(source: Node, destination: Node, q: int, g: int, R: int, K: int) -> None:
    matches = [
        edge
        for edge in closure.raw_transitions(source, R, factorization(K))
        if tuple(int(value) for value in edge["destination"]) == destination
        and int(edge["q"]) == q
        and int(edge["gcd_reduction"]) == g
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one edge {source} --{q},{g}--> {destination}")


def complete_reach(starts: Iterable[Node], R: int, K: int) -> tuple[set[Node], list[dict[str, object]]]:
    bounds = factorization(K)
    visited: set[Node] = set()
    edges: list[dict[str, object]] = []
    frontier = list(starts)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for edge in closure.raw_transitions(node, R, bounds):
            destination = tuple(int(value) for value in edge["destination"])
            edges.append(
                {"source": list(node), "q": int(edge["q"]), "destination": list(destination)}
            )
            if destination not in visited:
                frontier.append(destination)
        if len(visited) > 100:
            raise AssertionError("focused complete Reach exceeded its safety bound")
    edges.sort(key=lambda row: (row["source"], row["q"], row["destination"]))
    return visited, edges


def verify_solution(prime: int, solution: Iterable[int]) -> None:
    x, y, z = (int(value) for value in solution)
    if min(x, y, z) <= 0:
        raise AssertionError("unit-fraction denominator was not positive")
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, prime):
        raise AssertionError("unit-fraction identity failed")


def internal_gap_profile(prime: int, R: int, K: int) -> dict[str, object]:
    gaps = [
        gap
        for gap in closure.divisors(K)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]
    hits = []
    for gap in gaps:
        certificate = closure.exact_gap_certificate(prime, gap)
        if certificate is not None:
            verify_solution(prime, certificate["solution"])
            hits.append(certificate)
    return {"R": R, "gaps": gaps, "hits": hits}


def affine_hits(node: Node, prime: int, R: int, K: int) -> list[int]:
    gaps, _origins = closure.external_gap_candidates({node}, prime, K)
    return [gap for gap in gaps if closure.exact_gap_certificate(prime, gap) is not None]


def focused_slab_profile(
    prime: int,
    R: int,
    node: Node,
    q: int,
    exponent: int,
    alpha: int,
    beta: int,
) -> dict[str, object]:
    K = (prime * R + 1) // 4
    Q = q**exponent
    A, B, layer = node
    if layer != 1 or sorted((Q * alpha, beta)) != [A, B]:
        raise AssertionError("focused slab coordinates changed")
    if K % (alpha * beta) or math.gcd(Q, alpha * beta) != 1:
        raise AssertionError("focused slab support split failed")
    L = A * B
    direct = [T for T in closure.divisors(R) if (prime + T) % (4 * L) == 0]
    cross = [T for T in closure.divisors(R) if (prime * T + 1) % (4 * L) == 0]
    node_hits = affine_hits(node, prime, R, K)
    anchor = tuple(sorted((alpha, R - alpha))) + (1,)
    anchor_hits = affine_hits(anchor, prime, R, K)
    R_Q = (-pow(prime, -1, 4 * Q)) % (4 * Q)
    menu_miss = not (direct or cross or node_hits or anchor_hits)
    strong_miss = menu_miss and R_Q >= R
    return {
        "node": list(node),
        "q": q,
        "exponent": exponent,
        "Q": Q,
        "alpha": alpha,
        "beta": beta,
        "direct_collision_T": direct,
        "cross_collision_T": cross,
        "node_affine_hit_gaps": node_hits,
        "anchor": list(anchor),
        "anchor_affine_hit_gaps": anchor_hits,
        "R_Q": R_Q,
        "pre_absorption_menu_miss": menu_miss,
        "strong_miss": strong_miss,
    }


def joint_capacity_profile(P: int, Q: int, R: int, K: int, x_R: int) -> dict[str, object]:
    if math.gcd(P, Q) != 1 or (P + Q) % R:
        raise AssertionError("pair was not a primitive phase-minus-one representation")
    primes = sorted(set(factorization(P)) | set(factorization(Q)) | set(factorization(K)) | set(factorization(x_R)))
    z = {prime: valuation(P, prime) - valuation(Q, prime) for prime in primes}
    nu = {prime: valuation(K, prime) for prime in primes}
    sigma = {prime: valuation(x_R, prime) for prime in primes}
    mu = {prime: max(nu[prime], sigma[prime]) for prime in primes}
    product = P * Q
    defects = {
        "K": product // math.gcd(product, K),
        "x_R": product // math.gcd(product, x_R),
        "joint": product // math.gcd(product, math.lcm(K, x_R)),
    }
    expected = {
        "K": math.prod(prime ** max(abs(z[prime]) - nu[prime], 0) for prime in primes),
        "x_R": math.prod(prime ** max(abs(z[prime]) - sigma[prime], 0) for prime in primes),
        "joint": math.prod(prime ** max(abs(z[prime]) - mu[prime], 0) for prime in primes),
    }
    if defects != expected:
        raise AssertionError("signed target-fiber and joint-capacity dictionaries disagreed")
    positive = {
        str(prime): max(z[prime] - mu[prime], 0)
        for prime in primes
        if z[prime] > mu[prime]
    }
    negative = {
        str(prime): max(-z[prime] - mu[prime], 0)
        for prime in primes
        if -z[prime] > mu[prime]
    }
    if math.prod(int(q) ** e for q, e in positive.items()) * math.prod(
        int(q) ** e for q, e in negative.items()
    ) != defects["joint"]:
        raise AssertionError("signed carrier encoding failed")
    double_miss = defects["K"] > 1 and defects["x_R"] > 1
    branch = "not_double_miss"
    if double_miss:
        branch = "common_overload" if defects["joint"] > 1 else "strict_split"
    return {
        "P": P,
        "Q": Q,
        "product": product,
        "signed_exponents": {str(q): z[q] for q in primes if z[q]},
        "budgets": {
            "K": {str(q): nu[q] for q in primes if nu[q]},
            "x_R": {str(q): sigma[q] for q in primes if sigma[q]},
            "joint": {str(q): mu[q] for q in primes if mu[q]},
        },
        "defects": defects,
        "signed_common_overload": {"P_side": positive, "Q_side": negative},
        "branch": branch,
    }


def reduced_cross_product(left: int, right: int) -> int:
    common = math.gcd(left, right)
    return left * right // common**2


def cycle_receipt(
    d: dict[int, int],
    moving: dict[int, int],
    budget: dict[int, int],
    preferred_static: int | None = None,
) -> dict[str, object]:
    primes = sorted(set(d) | set(moving) | set(budget))
    static = [
        q for q in primes if moving.get(q, 0) == 0 and abs(d.get(q, 0)) > budget.get(q, 0)
    ]
    if static:
        q = preferred_static if preferred_static in static else static[0]
        return {
            "kind": "MISS_STATIC",
            "prime": q,
            "d": d.get(q, 0),
            "budget": budget.get(q, 0),
            "all_static_primes": static,
        }
    if not any(moving.get(q, 0) for q in primes):
        return {"kind": "CYCLE_RAY_HIT", "n": 0, "intervals": {}}
    lower = 0
    upper: int | None = None
    intervals: dict[str, list[int | None]] = {}
    for q in primes:
        weight = moving.get(q, 0)
        if weight == 0:
            continue
        allowance = budget.get(q, 0)
        lo = -(-(d.get(q, 0) - allowance) // weight)
        hi = (d.get(q, 0) + allowance) // weight
        lo = max(lo, 0)
        intervals[str(q)] = [lo, hi]
        lower = max(lower, lo)
        upper = hi if upper is None else min(upper, hi)
    if upper is not None and lower <= upper:
        return {"kind": "CYCLE_RAY_HIT", "n": lower, "intervals": intervals}
    return {
        "kind": "MISS_INTERVAL",
        "maximum_lower_bound": lower,
        "minimum_upper_bound": upper,
        "intervals": intervals,
    }


def cycle_capacity_profile() -> dict[str, object]:
    prime, R = 2_017, 207
    K, x_R = 104_380, 556
    U, V = 68, 139
    theta = 139 * 103
    X, Y = 2, 205
    cycle_Q = 41 * 101
    moving = factorization(cycle_Q)
    primes = sorted(
        set(factorization(U))
        | set(factorization(V))
        | set(factorization(theta))
        | set(factorization(X))
        | set(factorization(Y))
        | set(moving)
        | set(factorization(K))
        | set(factorization(x_R))
    )
    d_U = {q: valuation(U, q) - valuation(theta * Y, q) for q in primes}
    d_V = {q: valuation(V, q) - valuation(theta * X, q) for q in primes}
    receipts: dict[str, dict[str, object]] = {}
    for name, d in (("U", d_U), ("V", d_V)):
        for capacity_name, capacity in (("K", K), ("x_R", x_R)):
            budget = {q: valuation(capacity, q) for q in primes}
            receipt = cycle_receipt(d, moving, budget, preferred_static=103)
            if (
                receipt["kind"] != "MISS_STATIC"
                or receipt["prime"] != 103
                or receipt["d"] != -1
                or receipt["budget"] != 0
            ):
                raise AssertionError("p=2017 cycle lost its static 103 separator")
            receipts[f"{name}_to_{capacity_name}"] = receipt

    for n in range(4):
        actual_U = reduced_cross_product(U, theta * cycle_Q**n * Y)
        actual_V = reduced_cross_product(V, theta * cycle_Q**n * X)
        for q in primes:
            if valuation(actual_U, q) != abs(d_U[q] - n * moving.get(q, 0)):
                raise AssertionError("U cycle-ray valuation identity failed")
            if valuation(actual_V, q) != abs(d_V[q] - n * moving.get(q, 0)):
                raise AssertionError("V cycle-ray valuation identity failed")

    interval_examples = {
        "hit": cycle_receipt({2: 4, 3: 6}, {2: 1, 3: 2}, {2: 1, 3: 0}),
        "miss": cycle_receipt({2: 4, 3: 6}, {2: 1, 3: 2}, {2: 0, 3: 0}),
    }
    if interval_examples["hit"].get("kind") != "CYCLE_RAY_HIT":
        raise AssertionError("cycle interval hit receipt failed")
    if interval_examples["miss"].get("kind") != "MISS_INTERVAL":
        raise AssertionError("cycle interval miss receipt failed")
    return {
        "entry": {"U": U, "V": V, "theta": theta, "endpoint": [X, Y]},
        "cycle_Q": cycle_Q,
        "moving_valuations": {str(q): e for q, e in moving.items()},
        "static_receipts": receipts,
        "interval_receipt_unit_examples": interval_examples,
    }


def rechart_profile(prime: int, old_R: int, Q: int, expected_divisor: int, semantics: str) -> dict[str, object]:
    new_R = (-pow(prime, -1, 4 * Q)) % (4 * Q)
    new_K = (prime * new_R + 1) // 4
    if new_K % Q:
        raise AssertionError("path-selected chart lost Q divisibility")
    search_space, hits = closure.centered_type_i_hits(prime, new_R, new_K)
    selected = [hit for hit in hits if int(hit["centered_divisor"]) == expected_divisor]
    if len(selected) != 1:
        raise AssertionError("expected rechart center divisor was not unique")
    verify_solution(prime, selected[0]["solution"])
    return {
        "Q": Q,
        "old_R": old_R,
        "new_R": new_R,
        "new_K": new_K,
        "centered_search_space": search_space,
        "centered_hit_count": len(hits),
        "selected_hit": selected[0],
        "semantics": semantics,
    }


def analyze_linear_strong_miss_counterexample() -> dict[str, object]:
    prime, R = 57_073, 23
    K, x_R = 328_170, 14_274
    a, s = 2_378, 1
    if prime != a + s + a * s * R or (a * R + 1) * (s * R + 1) != 4 * K:
        raise AssertionError("linear source identity failed")
    centered_space, centered_hits = closure.centered_type_i_hits(prime, R, K)
    if centered_space != 81 or centered_hits:
        raise AssertionError("p=57073 ceased to be a centered F state")
    require_edge((3, 20, 1), (10, 13, 1), 2, 1, R, K)
    slab = focused_slab_profile(prime, R, (10, 13, 1), 13, 1, 1, 10)
    if not slab["strong_miss"] or slab["R_Q"] != 43:
        raise AssertionError("p=57073 strong-slab boundary changed")
    capacity = joint_capacity_profile(10, 13, R, K, x_R)
    if capacity["branch"] != "strict_split" or capacity["defects"] != {"K": 13, "x_R": 5, "joint": 1}:
        raise AssertionError("p=57073 empty-suffix capacity changed")

    nodes, edges = complete_reach(((10, 13, 1),), R, K)
    expected_nodes = {(10, 13, 1), (1, 22, 1), (2, 21, 1), (3, 20, 1)}
    if nodes != expected_nodes or len(edges) != 4:
        raise AssertionError("p=57073 complete Reach changed")
    gaps, _origins = closure.external_gap_candidates(nodes, prime, K)
    if gaps != [7, 11]:
        raise AssertionError("p=57073 external gap menu changed")
    external_hit = closure.exact_gap_certificate(prime, 7)
    if external_hit is None or closure.exact_gap_certificate(prime, 11) is not None:
        raise AssertionError("p=57073 external terminal boundary changed")
    verify_solution(prime, external_hit["solution"])
    internal = internal_gap_profile(prime, R, K)
    if [hit["gap"] for hit in internal["hits"]] != [15]:
        raise AssertionError("p=57073 internal terminal boundary changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "x_R": x_R,
        "linear_source": {"a": a, "s": s},
        "centered_square_spectrum_size": centered_space,
        "centered_hits": [],
        "source_edge": {"source": [3, 20, 1], "q": 2, "g": 1, "destination": [10, 13, 1]},
        "strong_slab": slab,
        "empty_suffix_cross_pair": capacity,
        "complete_reach": {"nodes": [list(node) for node in sorted(nodes)], "edges": edges},
        "external_gaps": gaps,
        "external_hit": external_hit,
        "internal_profile": internal,
        "boundary": "counterexample_to_shortest_source_path_slab_q_carrier_even_with_linear_source",
    }


def analyze_internal_free_cycle_counterexample() -> dict[str, object]:
    prime, R = 2_017, 207
    K, x_R = 104_380, 556
    linear_sources = []
    linear_target = R * prime + 1
    for a in range(1, (math.isqrt(linear_target) - 1) // R + 1):
        left = R * a + 1
        if linear_target % left:
            continue
        right = linear_target // left
        if (right - 1) % R == 0:
            linear_sources.append((a, (right - 1) // R))
    if linear_sources:
        raise AssertionError("p=2017 unexpectedly acquired a positive linear source")
    centered_space, centered_hits = closure.centered_type_i_hits(prime, R, K)
    if centered_space != 135 or centered_hits:
        raise AssertionError("p=2017 ceased to be a centered F state")
    require_edge((1_156, 1_535, 13), (68, 139, 1), 17, 1, R, K)
    slab = focused_slab_profile(prime, R, (68, 139, 1), 139, 1, 1, 68)
    if not slab["strong_miss"] or slab["R_Q"] != 231:
        raise AssertionError("p=2017 strong-slab boundary changed")
    capacity = joint_capacity_profile(68, 139, R, K, x_R)
    if capacity["branch"] != "strict_split" or capacity["defects"] != {"K": 139, "x_R": 17, "joint": 1}:
        raise AssertionError("p=2017 entry capacity changed")
    internal = internal_gap_profile(prime, R, K)
    if internal["hits"]:
        raise AssertionError("p=2017 ceased to be internal-free")
    nodes, edges = complete_reach(((68, 139, 1),), R, K)
    if nodes != {(68, 139, 1), (1, 206, 1), (2, 205, 1), (5, 202, 1)} or len(edges) != 4:
        raise AssertionError("p=2017 complete Reach changed")
    gaps, _origins = closure.external_gap_candidates(nodes, prime, K)
    if gaps != [103, 139] or any(closure.exact_gap_certificate(prime, gap) for gap in gaps):
        raise AssertionError("p=2017 external terminal boundary changed")
    cycle_word = word_profile(2, 205, R, (("Y", 41), ("X", 101)))
    if cycle_word["Q"] != 4_141 or cycle_word["matrix"] != [[41, 40], [4_100, 4_101]] or cycle_word["endpoint"] != [2, 205]:
        raise AssertionError("p=2017 cycle normal form changed")
    cycle = cycle_capacity_profile()
    entry_theta = 139 * 103
    cross_U = reduced_cross_product(68, entry_theta * 205)
    cross_V = reduced_cross_product(139, entry_theta * 2)
    entry_common = [
        joint_capacity_profile(
            68 // math.gcd(68, entry_theta * 205),
            entry_theta * 205 // math.gcd(68, entry_theta * 205),
            R,
            K,
            x_R,
        ),
        joint_capacity_profile(
            139 // math.gcd(139, entry_theta * 2),
            entry_theta * 2 // math.gcd(139, entry_theta * 2),
            R,
            K,
            x_R,
        ),
    ]
    if [profile["product"] for profile in entry_common] != [cross_U, cross_V]:
        raise AssertionError("p=2017 normalized entry products changed")
    if any(profile["branch"] != "common_overload" for profile in entry_common):
        raise AssertionError("p=2017 cycle entry lost common overload")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "x_R": x_R,
        "positive_linear_sources": [],
        "centered_square_spectrum_size": centered_space,
        "centered_hits": [],
        "source_edge": {"source": [1_156, 1_535, 13], "q": 17, "g": 1, "destination": [68, 139, 1]},
        "strong_slab": slab,
        "empty_suffix_cross_pair": capacity,
        "internal_profile": internal,
        "complete_reach": {"nodes": [list(node) for node in sorted(nodes)], "edges": edges, "external_gaps": gaps},
        "cycle_word": cycle_word,
        "cycle_capacity": cycle,
        "cycle_entry_common_overload_pairs": entry_common,
        "boundary": "internal_free_split_entry_with_static_cycle_separator_not_a_linear_source",
    }


def analyze_path_selected_terminals() -> list[dict[str, object]]:
    p1, R1 = 5_596_369, 35
    K1 = (p1 * R1 + 1) // 4
    p1_nodes = ((3, 32, 1), (16, 19, 1), (8, 27, 1), (4, 31, 1))
    for source, destination in zip(p1_nodes, p1_nodes[1:]):
        require_edge(source, destination, 2, 1, R1, K1)
    dyadic_word = word_profile(32, 3, R1, (("X", 2), ("X", 2), ("X", 2)))
    if dyadic_word["endpoint"] != [4, 31]:
        raise AssertionError("p=5596369 dyadic word changed")
    gap31 = closure.exact_gap_certificate(p1, 31)
    if gap31 is None or gap31["type"] != "Type_I" or gap31["divisor"] != 85:
        raise AssertionError("p=5596369 gap-31 terminal changed")
    verify_solution(p1, gap31["solution"])
    require_edge((3, 32, 1), (16, 19, 1), 2, 1, R1, K1)
    require_edge((16, 19, 1), (1, 34, 1), 19, 1, R1, K1)
    Q38 = rechart_profile(
        p1,
        R1,
        38,
        684,
        "path_selected_terminal_not_existing_E4",
    )
    if Q38["new_R"] != 23:
        raise AssertionError("p=5596369 path-selected chart changed")

    p2, R2 = 212_973_049, 215
    K2 = (p2 * R2 + 1) // 4
    require_edge((2, 213, 1), (3, 212, 1), 71, 1, R2, K2)
    require_edge((3, 212, 1), (4, 211, 1), 53, 1, R2, K2)
    if 212 != 53 * 4 or K2 % 12 or K2 % 53 == 0:
        raise AssertionError("p=212973049 single-slab support changed")
    Q53 = rechart_profile(
        p2,
        R2,
        53,
        1_325,
        "support_derived_verified_rechart_from_node_3_212",
    )
    if Q53["new_R"] != 171:
        raise AssertionError("p=212973049 support-derived chart changed")
    return [
        {
            "prime": p1,
            "R": R1,
            "dyadic_path": [list(node) for node in p1_nodes],
            "dyadic_word": dyadic_word,
            "direct_gap_terminal": gap31,
            "alternative_path_labels": [2, 19],
            "rechart": Q38,
            "formal_edge_semantics": "candidate_generation_only",
        },
        {
            "prime": p2,
            "R": R2,
            "path": [[2, 213, 1], [3, 212, 1], [4, 211, 1]],
            "path_labels": [71, 53],
            "single_slab_at_middle_node": {"Q": 53, "alpha": 4, "beta": 3, "alpha_beta_divides_K": True},
            "rechart": Q53,
            "leading_q71_edge_semantics": "candidate_generation_only",
        },
    ]


def pareto_finite_bound_example() -> dict[str, object]:
    # The two-node p=2017 bottom SCC; only labels 41 and 101 move.
    U, V, X, Y = 2, 205, 2, 205
    moving_primes = (41, 101)
    a = {q: valuation(U, q) - valuation(Y, q) for q in moving_primes}
    b = {q: valuation(V, q) - valuation(X, q) for q in moving_primes}
    m = {q: max(0, a[q], b[q]) for q in moving_primes}
    vertex_count = 2
    bound = vertex_count * math.prod(m[q] + 1 for q in moving_primes)
    if m != {41: 1, 101: 0} or bound != 4:
        raise AssertionError("focused Pareto lifted-state bound changed")
    return {
        "lifted_vertex_count": vertex_count,
        "moving_primes": list(moving_primes),
        "a": {str(q): a[q] for q in moving_primes},
        "b": {str(q): b[q] for q in moving_primes},
        "clip_thresholds": {str(q): m[q] for q in moving_primes},
        "witness_length_bound_B": bound,
        "theorem_semantics": "illustration_of_the_general_proof_not_a_finite_substitute_for_it",
    }


def run() -> dict[str, object]:
    closure_hash = sha256(CLOSURE_SCRIPT)
    if closure_hash != EXPECTED_CLOSURE_SHA256:
        raise AssertionError(f"formal closure helper changed: {closure_hash}")

    generic_word = word_profile(32, 3, 35, (("X", 2), ("X", 2), ("X", 2)))
    p2017 = analyze_internal_free_cycle_counterexample()
    p57073 = analyze_linear_strong_miss_counterexample()
    terminals = analyze_path_selected_terminals()
    pareto = pareto_finite_bound_example()
    summary = {
        "word_profiles": 2,
        "strong_miss_counterexamples": 2,
        "linear_source_counterexamples": 1,
        "cycle_static_receipts": len(p2017["cycle_capacity"]["static_receipts"]),
        "focused_direct_terminal_primes": [record["prime"] for record in terminals],
        "verified_rechart_count": sum(
            record["rechart"]["semantics"].startswith("support_derived_verified")
            for record in terminals
        ),
        "candidate_rechart_count": sum(
            "not_existing_E4" in record["rechart"]["semantics"] for record in terminals
        ),
        "pareto_example_bound": pareto["witness_length_bound_B"],
    }
    expected = {
        "word_profiles": 2,
        "strong_miss_counterexamples": 2,
        "linear_source_counterexamples": 1,
        "cycle_static_receipts": 4,
        "focused_direct_terminal_primes": [5_596_369, 212_973_049],
        "verified_rechart_count": 1,
        "candidate_rechart_count": 1,
        "pareto_example_bound": 4,
    }
    if summary != expected:
        raise AssertionError(f"focused bottom-word summary changed: {summary}")
    return {
        "schema_version": "type-i-bottom-word-lattice-pareto-cycle-capacity/v1",
        "scope_note": (
            "Focused exact checks of the bottom-word matrix normal form, two strong-miss "
            "boundaries, one cycle-ray separator, and two path-selected direct terminals. "
            "This does not rerun historical state/slab censuses, prove the universal sink-SCC "
            "escape, or upgrade an unanchored formal path to a legal descent edge."
        ),
        "inputs": {"formal_closure_script": CLOSURE_SCRIPT.name, "sha256": closure_hash},
        "summary": summary,
        "generic_bottom_word": generic_word,
        "linear_strong_miss_counterexample": p57073,
        "internal_free_cycle_counterexample": p2017,
        "path_selected_terminals": terminals,
        "pareto_finite_bound_example": pareto,
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
