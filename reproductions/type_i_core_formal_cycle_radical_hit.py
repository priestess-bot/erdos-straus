#!/usr/bin/env python3
"""Audit universal m=1 formal cycles and squarefree centered hits."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-core-formal-cycle-radical-hit-results.json"
)
DEFAULT_LIMIT = 9_999


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def histogram(values: list[int]) -> dict[str, int]:
    return {
        str(value): count
        for value, count in sorted(Counter(values).items())
    }


def sieve_factor_data(
    limit: int,
) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    spf = list(range(limit + 1))
    for q in range(2, math.isqrt(limit) + 1):
        if spf[q] != q:
            continue
        for value in range(q * q, limit + 1, q):
            if spf[value] == value:
                spf[value] = q
    supports: list[tuple[int, ...]] = [tuple() for _ in range(limit + 1)]
    square_primes: list[tuple[int, ...]] = [tuple() for _ in range(limit + 1)]
    for value in range(2, limit + 1):
        residual = value
        support: list[int] = []
        squares: list[int] = []
        while residual > 1:
            q = spf[residual]
            exponent = 0
            while residual % q == 0:
                residual //= q
                exponent += 1
            support.append(q)
            if exponent >= 2:
                squares.append(q)
        supports[value] = tuple(support)
        square_primes[value] = tuple(squares)
    return supports, square_primes


def universal_graph(
    modulus: int, square_primes: list[tuple[int, ...]]
) -> dict[int, tuple[int, ...]]:
    """Build U_R on unordered pairs {x,R-x} with gcd(x,R)=1."""
    adjacency: dict[int, tuple[int, ...]] = {}
    for x in range(1, (modulus + 1) // 2):
        if math.gcd(x, modulus) != 1:
            continue
        destinations: set[int] = set()
        for coordinate in (x, modulus - x):
            for q in square_primes[coordinate]:
                reduced = coordinate // q
                destination = min(reduced, modulus - reduced)
                if math.gcd(destination, modulus) != 1:
                    raise AssertionError("universal edge left the coprime graph")
                destinations.add(destination)
        adjacency[x] = tuple(sorted(destinations))
    return adjacency


def cyclic_components(
    adjacency: dict[int, tuple[int, ...]]
) -> list[list[int]]:
    index: dict[int, int] = {}
    lowlink: dict[int, int] = {}
    stack: list[int] = []
    on_stack: set[int] = set()
    components: list[list[int]] = []
    next_index = 0

    def visit(node: int) -> None:
        nonlocal next_index
        index[node] = next_index
        lowlink[node] = next_index
        next_index += 1
        stack.append(node)
        on_stack.add(node)
        for destination in adjacency[node]:
            if destination not in index:
                visit(destination)
                lowlink[node] = min(lowlink[node], lowlink[destination])
            elif destination in on_stack:
                lowlink[node] = min(lowlink[node], index[destination])
        if lowlink[node] != index[node]:
            return
        component: list[int] = []
        while True:
            member = stack.pop()
            on_stack.remove(member)
            component.append(member)
            if member == node:
                break
        if len(component) > 1 or node in adjacency[node]:
            components.append(sorted(component))

    for node in adjacency:
        if node not in index:
            visit(node)
    return components


def simple_cycles(
    adjacency: dict[int, tuple[int, ...]]
) -> list[tuple[int, ...]]:
    """Enumerate each directed simple cycle once, anchored at its least node."""
    cycles: list[tuple[int, ...]] = []
    for component in cyclic_components(adjacency):
        members = set(component)
        for start in component:
            path = [start]
            visited = {start}

            def search(node: int) -> None:
                for destination in adjacency[node]:
                    if destination not in members or destination < start:
                        continue
                    if destination == start:
                        cycles.append(tuple(path))
                        continue
                    if destination in visited:
                        continue
                    visited.add(destination)
                    path.append(destination)
                    search(destination)
                    path.pop()
                    visited.remove(destination)

            search(start)
    if len(cycles) != len(set(cycles)):
        raise AssertionError("simple-cycle enumeration produced duplicates")
    return sorted(cycles)


def radical_cube_witness(
    modulus: int, support: list[int]
) -> tuple[int, int] | None:
    """Return squarefree coprime a,b with a/b=-1 mod R, if one exists."""
    residues: dict[int, tuple[int, int]] = {1: (1, 1)}
    for q in support:
        if math.gcd(q, modulus) != 1:
            raise AssertionError("cycle support was not invertible modulo R")
        inverse = pow(q, -1, modulus)
        previous = list(residues.items())
        for residue, (numerator, denominator) in previous:
            residues.setdefault(
                residue * q % modulus,
                (numerator * q, denominator),
            )
            residues.setdefault(
                residue * inverse % modulus,
                (numerator, denominator * q),
            )
    witness = residues.get(modulus - 1)
    if witness is None:
        return None
    numerator, denominator = witness
    if (
        math.gcd(numerator, denominator) != 1
        or (numerator + denominator) % modulus
    ):
        raise AssertionError("radical-cube witness did not verify")
    return witness


def cycle_profile(
    modulus: int,
    cycle: tuple[int, ...],
    supports: list[tuple[int, ...]],
) -> dict[str, object]:
    support = sorted(
        {
            q
            for x in cycle
            for coordinate in (x, modulus - x)
            for q in supports[coordinate]
        }
    )
    witness = radical_cube_witness(modulus, support)
    return {
        "R": modulus,
        "cycle": list(cycle),
        "cycle_pairs": [[x, modulus - x] for x in cycle],
        "support": support,
        "support_size": len(support),
        "radical_cube_hit": witness is not None,
        "witness": (
            None
            if witness is None
            else {
                "a": witness[0],
                "b": witness[1],
                "m": (witness[0] + witness[1]) // modulus,
            }
        ),
    }


def run(limit: int) -> dict[str, object]:
    if limit != DEFAULT_LIMIT:
        raise ValueError("the committed audit is locked to limit 9999")
    sys.setrecursionlimit(max(20_000, limit * 2))
    supports, square_primes = sieve_factor_data(limit)
    core_profiles: list[dict[str, object]] = []
    core_cycle_moduli: set[int] = set()
    for modulus in range(7, limit + 1, 8):
        cycles = simple_cycles(universal_graph(modulus, square_primes))
        if cycles:
            core_cycle_moduli.add(modulus)
        for cycle in cycles:
            profile = cycle_profile(modulus, cycle, supports)
            core_profiles.append(profile)

    core_misses = [
        profile for profile in core_profiles if not profile["radical_cube_hit"]
    ]
    noncore_R = 7_219
    noncore_cycle = (19, 3_600, 1_800, 360, 361)
    noncore_graph = universal_graph(noncore_R, square_primes)
    if any(
        destination not in noncore_graph[source]
        for source, destination in zip(
            noncore_cycle,
            noncore_cycle[1:] + noncore_cycle[:1],
        )
    ):
        raise AssertionError("declared non-core cycle was not in the universal graph")
    noncore_profile = cycle_profile(noncore_R, noncore_cycle, supports)
    noncore_K = 12_298_570_220_629_770
    noncore_prime = (4 * noncore_K - 1) // noncore_R
    noncore_K_factors = {
        int(q): int(exponent)
        for q, exponent in sympy.factorint(noncore_K).items()
    }
    if any(exponent != 1 for exponent in noncore_K_factors.values()):
        raise AssertionError("non-core boundary K ceased to be squarefree")
    noncore_full_K_witness = radical_cube_witness(
        noncore_R, sorted(noncore_K_factors)
    )
    noncore_steps = [
        (7_200, 2),
        (3_600, 2),
        (1_800, 5),
        (6_859, 19),
        (361, 19),
    ]
    for source, destination, (coordinate, q) in zip(
        noncore_cycle,
        noncore_cycle[1:] + noncore_cycle[:1],
        noncore_steps,
    ):
        if (
            coordinate not in {source, noncore_R - source}
            or q not in noncore_K_factors
            or supports[coordinate].count(q) != 1
            or coordinate % (q ** (noncore_K_factors[q] + 1))
            or min(coordinate // q, noncore_R - coordinate // q) != destination
        ):
            raise AssertionError("non-core edge failed the actual K-height rule")
    if (
        noncore_profile["radical_cube_hit"]
        or noncore_full_K_witness is not None
        or 4 * noncore_K != noncore_prime * noncore_R + 1
        or noncore_prime % 24 != 5
        or not sympy.isprime(noncore_prime)
    ):
        raise AssertionError("non-core radical-cube counterexample changed")
    summary = {
        "limit": limit,
        "core_compatible_R_7_mod_8_count": len(range(7, limit + 1, 8)),
        "core_cycle_modulus_count": len(core_cycle_moduli),
        "core_simple_cycle_count": len(core_profiles),
        "core_radical_cube_hit_count": len(core_profiles) - len(core_misses),
        "core_radical_cube_miss_count": len(core_misses),
        "core_support_size_histogram": histogram(
            [int(profile["support_size"]) for profile in core_profiles]
        ),
    }
    expected = {
        "core_simple_cycle_count": 435,
        "core_radical_cube_hit_count": 435,
        "core_radical_cube_miss_count": 0,
    }
    actual = {field: summary[field] for field in expected}
    if actual != expected:
        raise AssertionError(f"cycle audit changed: {actual}")

    return {
        "arithmetic": (
            "For every R=7 mod 8 up to 9999 build the universal unordered m=1 graph with "
            "an edge whenever q^2 divides the selected coordinate; enumerate every "
            "directed simple cycle; collect all coordinate primes S; and exhaust the "
            "squarefree signed cube with exponents in {-1,0,1} for a residue -1."
        ),
        "scope_note": (
            "Every actual K-supported m=1 formal cycle embeds in this universal graph. "
            "The R<=9999 result is complete finite evidence, not a proof for all R. "
            "For core p=1 mod 24, the separate parity argument makes the R=3 mod 8 "
            "m=1 K-supported graph empty, so only R=7 mod 8 is relevant."
        ),
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "noncore_boundary": {
            "prime": noncore_prime,
            "prime_mod_24": noncore_prime % 24,
            "K": noncore_K,
            "K_factorization": [
                [q, exponent] for q, exponent in sorted(noncore_K_factors.items())
            ],
            "full_K_centered_box_hit": noncore_full_K_witness is not None,
            "edge_labels": [
                {"selected_coordinate": coordinate, "q": q}
                for coordinate, q in noncore_steps
            ],
            **noncore_profile,
        },
        "core_cycle_profiles": core_profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.limit)
    args.output.write_text(
        json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
