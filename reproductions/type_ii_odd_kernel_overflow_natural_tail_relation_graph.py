#!/usr/bin/env python3
"""Verify the natural-tail capacity and relation graph for two empty Type II boxes.

This is a focused verifier for the new relation-graph theorem.  It does not run
the historical prime-range scans.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import asdict
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions.short_certificate import (  # noqa: E402
    GapCertificate,
    certificate_at_gap,
    smallest_prime_factors,
    verify_certificate,
)


PRIME = 67_369


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def canonical_pair(first: int, second: int) -> tuple[int, int]:
    return tuple(sorted((first, second)))


def ratio_from_vector(
    primes: tuple[int, ...], vector: tuple[int, ...]
) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for prime, exponent in zip(primes, vector, strict=True):
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def physical_weight(
    factors: dict[int, int], vector: tuple[int, ...]
) -> int:
    weight = 1
    for (prime, exponent), coordinate in zip(factors.items(), vector, strict=True):
        weight *= prime ** max(abs(coordinate) - exponent, 0)
    return weight


def target_vectors_at_most_weight(
    modulus: int, factors: dict[int, int], maximum_weight: int
) -> list[tuple[int, ...]]:
    ranges = []
    for prime, exponent in factors.items():
        extra = 0
        power = prime
        while power <= maximum_weight:
            extra += 1
            power *= prime
        ranges.append(range(-exponent - extra, exponent + extra + 1))
    hits = []
    for vector in product(*ranges):
        if physical_weight(factors, vector) > maximum_weight:
            continue
        residue = 1
        for prime, coordinate in zip(factors, vector, strict=True):
            residue = residue * pow(prime, coordinate, modulus) % modulus
        if residue == modulus - 1:
            hits.append(vector)
    return sorted(hits)


def positive_divisors(value: int) -> list[int]:
    divisors = [1]
    for prime, exponent in factorization(value).items():
        old = tuple(divisors)
        power = 1
        for _ in range(exponent):
            power *= prime
            divisors.extend(divisor * power for divisor in old)
    return sorted(divisors)


def quotient_terminal_gaps(
    prime: int, kappa: int, spf
) -> list[tuple[int, object]]:
    terminals = []
    for gap in positive_divisors(kappa):
        if gap % 4 != 3 or not 3 <= gap <= prime - 2:
            continue
        certificate = certificate_at_gap(prime, gap, spf)
        if certificate is not None:
            if not verify_certificate(certificate):
                raise AssertionError("quotient terminal failed verification")
            terminals.append((gap, certificate))
    return terminals


def relation_receipt(prime: int, gap: int, first: int, second: int) -> dict[str, int | bool]:
    if prime % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise AssertionError("illegal prime or gap")
    x = (prime + gap) // 4
    if 4 * x != prime + gap or gcd(first, second) != 1:
        raise AssertionError("invalid reduced target relation")
    if (first + second) % gap:
        raise AssertionError("target relation has no integer quotient")
    kappa = (first + second) // gap
    if gcd(gap * kappa, first * second) != 1:
        raise AssertionError("modulus/quotient freshness failed")

    capacity = prime * x
    deficit_first = first // gcd(first, capacity)
    deficit_second = second // gcd(second, capacity)
    deficit = first * second // gcd(first * second, capacity)
    if deficit != deficit_first * deficit_second:
        raise AssertionError("split physical deficit did not multiply")
    if Fraction(4, prime) != (
        Fraction(1, x)
        + Fraction(first, prime * x * kappa)
        + Fraction(second, prime * x * kappa)
    ):
        raise AssertionError("natural-tail rational identity failed")

    integral = capacity % (first * second) == 0
    direct_integrality = (
        prime * x * kappa % first == 0 and prime * x * kappa % second == 0
    )
    if integral != direct_integrality or integral != (deficit == 1):
        raise AssertionError("natural-tail integrality equivalence failed")
    return {
        "x": x,
        "kappa": kappa,
        "capacity": capacity,
        "deficit_first": deficit_first,
        "deficit_second": deficit_second,
        "deficit": deficit,
        "integral": integral,
    }


def relation_terminal(prime: int, gap: int, first: int, second: int):
    receipt = relation_receipt(prime, gap, first, second)
    if not receipt["integral"]:
        return None
    x = int(receipt["x"])
    kappa = int(receipt["kappa"])
    if first % prime == 0:
        p_side, other = first, second
    elif second % prime == 0:
        p_side, other = second, first
    else:
        p_side = 0
        other = 0

    if p_side:
        reduced = p_side // prime
        divisor = x * other // reduced
        certificate_type = "I"
    else:
        small, large = canonical_pair(first, second)
        divisor = x * small // large
        certificate_type = "II"

    y = prime * x * kappa // first
    z = prime * x * kappa // second
    p_divisible_tails = (y % prime == 0) + (z % prime == 0)
    expected = 1 if certificate_type == "I" else 2
    if p_divisible_tails != expected:
        raise AssertionError("Type I/II natural-tail classification failed")

    # Reconstruct through the canonical gap certificate formulas as an
    # independent check of the unordered natural tails.
    if certificate_type == "I":
        canonical_y = (prime * x + divisor) // gap
        canonical_z = prime * (x + prime * x * x // divisor) // gap
    else:
        canonical_y = prime * (x + divisor) // gap
        canonical_z = prime * (x + x * x // divisor) // gap
    if sorted((y, z)) != sorted((canonical_y, canonical_z)):
        raise AssertionError("natural tails did not match the gap normal form")
    certificate = GapCertificate(
        prime,
        certificate_type,
        gap,
        x,
        divisor,
        canonical_y,
        canonical_z,
    )
    if not verify_certificate(certificate):
        raise AssertionError("natural-tail terminal failed the short-certificate verifier")
    return {
        "certificate_type": certificate_type,
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "tails": canonical_pair(y, z),
    }


def transition(
    prime: int, gap: int, first: int, second: int, carrier: int
) -> tuple[tuple[int, int], int, dict[str, int]]:
    receipt = relation_receipt(prime, gap, first, second)
    x = int(receipt["x"])
    kappa = int(receipt["kappa"])
    if first % carrier == 0:
        charged, other = first, second
    elif second % carrier == 0:
        charged, other = second, first
    else:
        raise AssertionError("chosen carrier divides neither side")
    if valuation(first * second, carrier) <= valuation(prime * x, carrier):
        raise AssertionError("chosen carrier is not above natural-tail capacity")

    shift = (-kappa) % carrier
    if not 1 <= shift < carrier:
        raise AssertionError("freshness did not give a nonzero shift")
    raw_first = charged // carrier
    raw_second = (other + gap * shift) // carrier
    raw_kappa = (kappa + shift) // carrier
    common = gcd(raw_first, raw_second)
    if gcd(common, gap) != 1 or raw_kappa % common:
        raise AssertionError("normalization factor does not divide the quotient")

    next_first = raw_first // common
    next_second = raw_second // common
    next_kappa = raw_kappa // common
    relation_receipt(prime, gap, next_first, next_second)
    if (next_first + next_second) // gap != next_kappa:
        raise AssertionError("transition quotient mismatch")
    if kappa > 1 and not next_kappa < kappa:
        raise AssertionError("quotient layer did not strictly decrease")
    if kappa == 1 and (next_kappa != 1 or common != 1):
        raise AssertionError("bottom-layer transition changed its layer")
    return canonical_pair(next_first, next_second), next_kappa, {
        "carrier": carrier,
        "shift": shift,
        "normalization": common,
    }


def bottom_graph(prime: int, gap: int, x: int):
    capacity_factors = factorization(prime * x)
    graph: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = {}
    for first in range(1, (gap + 1) // 2):
        second = gap - first
        if gcd(first, second) != 1:
            continue
        node = canonical_pair(first, second)
        graph[node] = []
        for charged in node:
            for carrier, exponent in factorization(charged).items():
                if exponent <= capacity_factors.get(carrier, 0):
                    continue
                target, next_kappa, _ = transition(
                    prime, gap, first, second, carrier
                )
                if next_kappa != 1:
                    raise AssertionError("bottom graph left kappa=1")
                graph[node].append((carrier, target))
    return graph


def reachable_nodes(graph, start: tuple[int, int]) -> set[tuple[int, int]]:
    reached = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for _, target in graph[node]:
            if target not in reached:
                reached.add(target)
                queue.append(target)
    return reached


def strongly_connected_components(graph, nodes: set[tuple[int, int]]):
    index = 0
    indices: dict[tuple[int, int], int] = {}
    lowlinks: dict[tuple[int, int], int] = {}
    stack: list[tuple[int, int]] = []
    on_stack: set[tuple[int, int]] = set()
    components: list[set[tuple[int, int]]] = []

    def visit(node: tuple[int, int]) -> None:
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for _, target in graph[node]:
            if target not in nodes:
                continue
            if target not in indices:
                visit(target)
                lowlinks[node] = min(lowlinks[node], lowlinks[target])
            elif target in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[target])
        if lowlinks[node] != indices[node]:
            return
        component: set[tuple[int, int]] = set()
        while True:
            member = stack.pop()
            on_stack.remove(member)
            component.add(member)
            if member == node:
                break
        components.append(component)

    for node in nodes:
        if node not in indices:
            visit(node)
    return components


def verify_path(
    prime: int,
    gap: int,
    start: tuple[int, int],
    carriers: tuple[int, ...],
) -> tuple[tuple[int, int], list[dict[str, int]]]:
    node = canonical_pair(*start)
    receipts: list[dict[str, int]] = []
    for carrier in carriers:
        node, _, edge = transition(prime, gap, *node, carrier)
        receipts.append(edge)
    return node, receipts


def verify() -> dict[str, object]:
    spf = smallest_prime_factors(PRIME // 2 + 2)
    cases = []

    q21_primes = (3, 7, 11, 73)
    q21_vector = (-2, 1, 0, -1)
    q21_pair = ratio_from_vector(q21_primes, q21_vector)
    q21 = relation_receipt(PRIME, 83, *q21_pair)
    if q21_pair != (7, 657) or q21["kappa"] != 8 or q21["deficit"] != 3:
        raise AssertionError("q=21 minimum relation changed")
    q21_bottom, q21_path = verify_path(
        PRIME, 83, q21_pair, (3, 2, 5, 2, 2)
    )
    if q21_bottom != (21, 62):
        raise AssertionError("q=21 terminal-label path changed")
    if valuation(21 * 62, 31) <= valuation(PRIME * int(q21["x"]), 31):
        raise AssertionError("gap 31 is not an overflowing edge label")
    cert31 = certificate_at_gap(PRIME, 31, spf)
    if cert31 is None or not verify_certificate(cert31):
        raise AssertionError("gap-31 terminal disappeared")
    if (cert31.certificate_type, cert31.x, cert31.divisor, cert31.y, cert31.z) != (
        "I",
        16_850,
        3_370,
        36_618_420,
        12_334_731_684_900,
    ):
        raise AssertionError("unexpected canonical gap-31 certificate")

    graph21 = bottom_graph(PRIME, 83, int(q21["x"]))
    reached21 = reachable_nodes(graph21, (10, 73))
    components21 = strongly_connected_components(graph21, reached21)
    if len(reached21) != 41 or sorted(map(len, components21)) != [41]:
        raise AssertionError("q=21 bottom SCC profile changed")
    cases.append(
        {
            "q": 21,
            "initial_pair": q21_pair,
            "initial_kappa": q21["kappa"],
            "physical_deficit": q21["deficit"],
            "terminal_node": q21_bottom,
            "path_carriers": [edge["carrier"] for edge in q21_path],
            "terminal_gap": 31,
            "terminal_certificate": asdict(cert31),
            "bottom_reachable_nodes": len(reached21),
            "bottom_scc_sizes": sorted(map(len, components21), reverse=True),
        }
    )

    q42_primes = (2, 3, 7, 67)
    q42_vector = (-2, 3, -1, 1)
    q42_pair = ratio_from_vector(q42_primes, q42_vector)
    q42 = relation_receipt(PRIME, 167, *q42_pair)
    if q42_pair != (1_809, 28) or q42["kappa"] != 11 or q42["deficit"] != 3:
        raise AssertionError("q=42 minimum relation changed")
    q42_bottom, q42_path = verify_path(
        PRIME, 167, q42_pair, (3, 5, 13, 83, 11, 2, 13, 2, 5)
    )
    if q42_bottom != (16, 151):
        raise AssertionError("q=42 terminal-label path changed")
    if valuation(16 * 151, 151) <= valuation(PRIME * int(q42["x"]), 151):
        raise AssertionError("gap 151 is not an overflowing edge label")
    cert151 = certificate_at_gap(PRIME, 151, spf)
    if cert151 is None or not verify_certificate(cert151):
        raise AssertionError("gap-151 terminal disappeared")
    if (cert151.certificate_type, cert151.x, cert151.divisor, cert151.y, cert151.z) != (
        "II",
        16_880,
        32,
        7_545_328,
        3_980_160_520,
    ):
        raise AssertionError("unexpected canonical gap-151 certificate")

    graph42 = bottom_graph(PRIME, 167, int(q42["x"]))
    reached42 = reachable_nodes(graph42, (13, 154))
    components42 = strongly_connected_components(graph42, reached42)
    cyclic42 = sorted(
        (
            len(component)
            for component in components42
            if len(component) > 1
            or any(target == next(iter(component)) for _, target in graph42[next(iter(component))])
        ),
        reverse=True,
    )
    if len(reached42) != 21 or cyclic42 != [19]:
        raise AssertionError("q=42 bottom SCC profile changed")
    cases.append(
        {
            "q": 42,
            "initial_pair": q42_pair,
            "initial_kappa": q42["kappa"],
            "physical_deficit": q42["deficit"],
            "terminal_node": q42_bottom,
            "path_carriers": [edge["carrier"] for edge in q42_path],
            "terminal_gap": 151,
            "terminal_certificate": asdict(cert151),
            "bottom_reachable_nodes": len(reached42),
            "bottom_cyclic_scc_sizes": cyclic42,
        }
    )

    q42_unweighted_pair = ratio_from_vector(q42_primes, (-2, 1, 2, 1))
    q42_unweighted = relation_receipt(PRIME, 167, *q42_unweighted_pair)
    q42_quotient_terminals = quotient_terminal_gaps(
        PRIME, int(q42_unweighted["kappa"]), spf
    )
    if (
        q42_unweighted_pair != (9_849, 4)
        or q42_unweighted["kappa"] != 59
        or q42_unweighted["deficit"] != 7
        or len(q42_quotient_terminals) != 1
    ):
        raise AssertionError("q=42 fresh quotient control changed")
    gap59, cert59 = q42_quotient_terminals[0]
    if (
        gap59,
        cert59.certificate_type,
        cert59.x,
        cert59.divisor,
        cert59.y,
        cert59.z,
    ) != (59, "I", 16_857, 151_713, 19_250_694, 144_100_000_454):
        raise AssertionError("gap-59 quotient terminal changed")
    if quotient_terminal_gaps(PRIME, int(q21["kappa"]), spf):
        raise AssertionError("q=21 quotient unexpectedly acquired a terminal")
    if quotient_terminal_gaps(PRIME, int(q42["kappa"]), spf):
        raise AssertionError("q=42 weighted quotient unexpectedly acquired a terminal")

    # A strict boundary for the edge-label-only strengthening.  This empty
    # noncyclic state has a terminal-free bottom SCC, but both minimum source
    # relations are preempted by fresh quotient terminals before entering it.
    boundary_prime = 1_153
    boundary_gap = 63
    boundary_x = 304
    boundary_factors = {2: 4, 19: 1}
    boundary_u = (boundary_prime - 1) // 4
    boundary_q = (boundary_gap + 1) // 4
    boundary_rank = boundary_u // boundary_q
    boundary_k0 = (boundary_rank + 5) // 4
    boundary_endpoint_cap = (
        boundary_k0
        * (boundary_k0 + 1)
        // (4 * boundary_k0 - boundary_rank - 1)
    )
    if (
        boundary_prime % 24 != 1
        or factorization(boundary_prime) != {boundary_prime: 1}
        or boundary_u != boundary_q * boundary_rank
        or boundary_q > boundary_endpoint_cap
        or 4 * boundary_x != boundary_prime + boundary_gap
    ):
        raise AssertionError("p=1153 is not the declared endpoint-allowed core state")
    boundary_hits = target_vectors_at_most_weight(
        boundary_gap, boundary_factors, 19**2
    )
    expected_boundary_hits = [
        (-3, -3),
        (-3, 3),
        (3, -3),
        (3, 3),
    ]
    if boundary_hits != expected_boundary_hits:
        raise AssertionError("p=1153 minimum physical target layer changed")
    if any(
        physical_weight(boundary_factors, vector) != 19**2
        for vector in boundary_hits
    ):
        raise AssertionError("p=1153 target appeared below weight 19^2")

    boundary_spf = smallest_prime_factors(boundary_prime // 2 + 2)
    first_boundary_pair = ratio_from_vector(boundary_factors.keys(), (-3, -3))
    second_boundary_pair = ratio_from_vector(boundary_factors.keys(), (-3, 3))
    first_boundary = relation_receipt(
        boundary_prime, boundary_gap, *first_boundary_pair
    )
    second_boundary = relation_receipt(
        boundary_prime, boundary_gap, *second_boundary_pair
    )
    if (
        first_boundary_pair,
        first_boundary["kappa"],
        second_boundary_pair,
        second_boundary["kappa"],
    ) != ((1, 54_872), 871, (6_859, 8), 109):
        raise AssertionError("p=1153 minimum relations changed")

    first_after_19, first_kappa, _ = transition(
        boundary_prime, boundary_gap, *first_boundary_pair, 19
    )
    second_after_19, second_kappa, _ = transition(
        boundary_prime, boundary_gap, *second_boundary_pair, 19
    )
    first_quotient = quotient_terminal_gaps(
        boundary_prime, first_kappa, boundary_spf
    )
    second_quotient = quotient_terminal_gaps(
        boundary_prime, second_kappa, boundary_spf
    )
    if (
        first_after_19,
        first_kappa,
        [(gap, cert.certificate_type) for gap, cert in first_quotient],
    ) != ((5, 1_444), 23, [(23, "II")]):
        raise AssertionError("p=1153 quotient-23 branch changed")
    if (
        second_after_19,
        second_kappa,
        [(gap, cert.certificate_type) for gap, cert in second_quotient],
    ) != ((17, 361), 6, [(3, "I")]):
        raise AssertionError("p=1153 quotient-3 branch changed")

    boundary_graph = bottom_graph(boundary_prime, boundary_gap, boundary_x)
    boundary_scc = {(1, 62), (2, 61)}
    boundary_components = strongly_connected_components(
        boundary_graph, set(boundary_graph)
    )
    if boundary_scc not in boundary_components:
        raise AssertionError("p=1153 two-cycle disappeared")
    internal_labels = sorted(
        carrier
        for node in boundary_scc
        for carrier, target in boundary_graph[node]
        if target in boundary_scc
    )
    if internal_labels != [31, 61]:
        raise AssertionError("p=1153 two-cycle labels changed")
    if certificate_at_gap(boundary_prime, 31, boundary_spf) is not None:
        raise AssertionError("p=1153 gap-31 no-go disappeared")
    if certificate_at_gap(boundary_prime, boundary_gap, boundary_spf) is not None:
        raise AssertionError("p=1153 original gap acquired a terminal")

    # Two direct controls exercise both parts of the p*x capacity.  The first
    # is Type II (A*B | x); the second spends the unique p slot and is Type I.
    direct_type_ii = relation_terminal(73, 7, 1, 20)
    direct_type_i = relation_terminal(13, 3, 13, 2)
    if direct_type_ii is None or direct_type_ii["certificate_type"] != "II":
        raise AssertionError("Type II natural-tail control failed")
    if direct_type_i is None or direct_type_i["certificate_type"] != "I":
        raise AssertionError("Type I p-slot natural-tail control failed")

    return {
        "status": "verified",
        "theorem_controls": {
            "type_ii_capacity_control": direct_type_ii,
            "type_i_p_slot_control": direct_type_i,
        },
        "fresh_quotient_control": {
            "relation_pair": q42_unweighted_pair,
            "kappa": q42_unweighted["kappa"],
            "physical_deficit": q42_unweighted["deficit"],
            "terminal_gap": gap59,
            "terminal_certificate": asdict(cert59),
        },
        "bottom_label_no_go": {
            "prime": boundary_prime,
            "gap": boundary_gap,
            "q": boundary_q,
            "rank": boundary_rank,
            "x": boundary_x,
            "minimum_weight": 19**2,
            "minimum_vectors": boundary_hits,
            "bottom_scc": sorted(boundary_scc),
            "internal_labels": internal_labels,
            "legal_internal_labels": [31],
            "edge_label_terminal": None,
            "preempting_quotient_terminals": [
                asdict(first_quotient[0][1]),
                asdict(second_quotient[0][1]),
            ],
        },
        "empty_box_cases": cases,
        "scope": "new natural-tail relation graph only; no historical range tests",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = verify()
    if args.verify:
        print(result)


if __name__ == "__main__":
    main()
