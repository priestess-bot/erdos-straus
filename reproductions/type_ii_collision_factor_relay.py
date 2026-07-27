#!/usr/bin/env python3
"""Exact collision-factor relay audit for canonical Type II rays.

For a jointly failing finite canonical fan, each collision prime power and
every optional base-private prime power has a source shift. The collision
prime powers form a finite, p-dependent factor closure. This script searches
factors formed from that closure and a selected bounded number of distinct
base-private primes in the natural range h <= 2p. The congruence
h == -1 mod 4ac restricts the possible canonical target shifts a^2 c to a
finite divisor enumeration of (h+1)/4, so the audit contains no arbitrary
future-shift cap.

The result is a finite diagnostic only: a missing relay does not prove that no
other Type II certificate or descent exists.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-collision-factor-relay-h14-1m-results.json"
COLLISION_SCRIPT = ROOT / "reproductions" / "type_ii_multishift_collision.py"


def load_collision_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_collision_factor_relay_collision", COLLISION_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_multishift_collision.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


collision = load_collision_script()
canonical = collision.canonical
residue = canonical.residue_structure


def factorization_dict(
    value: int, smallest_factors: list[int]
) -> dict[int, int]:
    """Return the prime-power factorization of a positive in-range integer."""
    return dict(residue.factorization_from_spf(value, smallest_factors))


def divisors_limited(
    factorization: dict[int, int], upper_bound: int
) -> tuple[int, ...]:
    """Enumerate exactly the divisors not exceeding upper_bound."""
    values = [1]
    for factor, exponent in sorted(factorization.items()):
        previous = tuple(values)
        power = 1
        for _ in range(exponent):
            power *= factor
            values.extend(
                divisor * power
                for divisor in previous
                if divisor * power <= upper_bound
            )
    return tuple(sorted(values))


def divisors(value: int, smallest_factors: list[int]) -> tuple[int, ...]:
    """Return all positive divisors of value."""
    return divisors_limited(factorization_dict(value, smallest_factors), value)


def squarefree(value: int, smallest_factors: list[int]) -> bool:
    return all(
        exponent == 1
        for exponent in factorization_dict(value, smallest_factors).values()
    )


def canonical_targets_for_factor(
    factor: int, prime: int, smallest_factors: list[int]
) -> tuple[tuple[int, int, int], ...]:
    """Return natural canonical pairs whose modulus divides factor+1.

    If h == -1 mod 4ac, then d=ac divides (h+1)/4. Conversely every
    d | (h+1)/4 and a | d with c=d/a squarefree gives a canonical pair
    (a,c), shift a^2c=ad, and modulus 4ac | h+1.
    """
    if factor <= 1 or factor % 4 != 3:
        return ()
    base = (factor + 1) // 4
    targets: set[tuple[int, int, int]] = set()
    for ac in divisors(base, smallest_factors):
        for a in divisors(ac, smallest_factors):
            c = ac // a
            if not squarefree(c, smallest_factors):
                continue
            shift = a * ac
            if shift <= prime // 4:
                targets.add((shift, a, c))
    return tuple(sorted(targets))


def collision_closure(
    prime: int,
    pairs: tuple[tuple[int, int], ...],
    smallest_factors: list[int],
    collision_set: set[int],
) -> tuple[dict[int, int], dict[int, list[dict[str, int]]]]:
    """Return the lcm factorization and source-labelled collision prime powers."""
    closure = factorization_dict(24, smallest_factors)
    sources: dict[int, list[dict[str, int]]] = {}
    for a, c in pairs:
        shift = a * a * c
        factors = factorization_dict(prime + 4 * shift, smallest_factors)
        for factor, exponent in factors.items():
            if factor not in collision_set:
                continue
            closure[factor] = max(closure.get(factor, 0), exponent)
            sources.setdefault(factor, []).append(
                {"shift": shift, "exponent": exponent}
            )
    for factor in sources:
        sources[factor].sort(key=lambda row: row["shift"])
    return closure, sources


def private_source_factors(
    prime: int,
    pairs: tuple[tuple[int, int], ...],
    smallest_factors: list[int],
    collision_set: set[int],
) -> dict[int, list[dict[str, int]]]:
    """Return source-labelled prime powers private to the base fan.

    A prime outside collision_set can occur in only one base shifted integer,
    since an occurrence in two would divide their shift difference.
    """
    sources: dict[int, list[dict[str, int]]] = {}
    for a, c in pairs:
        shift = a * a * c
        for factor, exponent in factorization_dict(
            prime + 4 * shift, smallest_factors
        ).items():
            if factor in collision_set:
                continue
            sources.setdefault(factor, []).append(
                {"shift": shift, "exponent": exponent}
            )
    if any(len(rows) != 1 for rows in sources.values()):
        raise AssertionError("base-private prime has more than one source")
    return sources


def relay_candidate_factors(
    closure: dict[int, int],
    private_sources: dict[int, list[dict[str, int]]],
    private_source_prime_budget: int,
    upper_bound: int,
) -> tuple[int, ...]:
    """Return relay factors with a bounded number of private source primes.

    The zero-private layer is exactly the collision closure. In the
    positive-private layers, h is d times a product of prime powers from
    distinct base-private sources, where d divides the collision closure.
    This is complete for factors with at most the stated number of
    non-collision primes inherited from the base fan.
    """
    if private_source_prime_budget not in {0, 1, 2, 3}:
        raise ValueError(
            "only private-source-prime budgets 0, 1, 2, and 3 are supported"
        )
    collision_divisors = divisors_limited(closure, upper_bound)
    private_items = tuple(
        (factor, rows[0]["exponent"])
        for factor, rows in sorted(private_sources.items())
    )
    private_products: set[int] = {1}

    def extend(start: int, remaining: int, product: int) -> None:
        if remaining == 0:
            return
        for index in range(start, len(private_items)):
            factor, exponent = private_items[index]
            power = 1
            for _ in range(exponent):
                power *= factor
                next_product = product * power
                if next_product > upper_bound:
                    break
                private_products.add(next_product)
                extend(index + 1, remaining - 1, next_product)

    extend(0, private_source_prime_budget, 1)
    candidates = {
        divisor * private_product
        for divisor in collision_divisors
        for private_product in private_products
        if divisor * private_product <= upper_bound
    }
    return tuple(sorted(candidates))


def source_labels_for_factor(
    factorization: dict[int, int],
    target_shift: int,
    sources: dict[int, list[dict[str, int]]],
) -> list[dict[str, object]]:
    """Record source shifts compatible with every non-base prime power of h."""
    labels: list[dict[str, object]] = []
    for prime, exponent in sorted(factorization.items()):
        if prime not in sources:
            labels.append(
                {
                    "prime": prime,
                    "exponent": exponent,
                    "origin": "base_modulus",
                }
            )
            continue
        modulus = prime**exponent
        compatible = [
            row["shift"]
            for row in sources[prime]
            if row["exponent"] >= exponent
            and (prime == 2 or (target_shift - row["shift"]) % modulus == 0)
        ]
        if not compatible:
            raise AssertionError("target divisibility lost a collision source label")
        labels.append(
            {
                "prime": prime,
                "exponent": exponent,
                "source_shifts": compatible,
            }
        )
    return labels


def relay_for_prime(
    prime: int,
    base_shift_bound: int,
    smallest_factors: list[int],
    private_source_prime_budget: int = 0,
) -> dict[str, object]:
    """Find natural relays from collision factors and optional private sources."""
    pairs = tuple(
        canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_set = set(
        collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    closure, sources = collision_closure(
        prime, pairs, smallest_factors, collision_set
    )
    private_sources = private_source_factors(
        prime, pairs, smallest_factors, collision_set
    )
    all_sources = {**sources, **private_sources}
    closure_value = math.prod(
        factor**exponent for factor, exponent in closure.items()
    )
    relays: list[dict[str, object]] = []
    closure_divisors = divisors_limited(closure, 2 * prime)
    candidate_factors = relay_candidate_factors(
        closure, private_sources, private_source_prime_budget, 2 * prime
    )
    for factor in candidate_factors:
        if factor <= 1 or factor % 4 != 3:
            continue
        for shift, a, c in canonical_targets_for_factor(
            factor, prime, smallest_factors
        ):
            if shift <= base_shift_bound or (prime + 4 * shift) % factor:
                continue
            modulus = 4 * a * c
            if (factor + 1) % modulus:
                raise AssertionError("canonical target did not divide factor+1")
            k = (factor + 1) // modulus
            certificate = canonical.ray.short_certificate.type_ii_raw_ray_certificate(
                prime, a, c, k
            )
            if certificate is None:
                raise AssertionError("relay factor did not reconstruct a certificate")
            factorization = factorization_dict(factor, smallest_factors)
            relays.append(
                {
                    "h": factor,
                    "h_factorization": [
                        {"prime": q, "exponent": exponent}
                        for q, exponent in sorted(factorization.items())
                    ],
                    "shift": shift,
                    "a": a,
                    "c": c,
                    "k": k,
                    "gap": certificate.gap,
                    "divisor": certificate.divisor,
                    "source_labels": source_labels_for_factor(
                        factorization, shift, all_sources
                    ),
                }
            )
    relays.sort(key=lambda row: (row["shift"], row["h"], row["a"], row["c"]))
    return {
        "prime": prime,
        "collision_primes": sorted(collision_set),
        "closure_factorization": [
            {"prime": factor, "exponent": exponent}
            for factor, exponent in sorted(closure.items())
        ],
        "closure_value": closure_value,
        "closure_divisor_count_at_most_2p": len(closure_divisors),
        "private_source_prime_budget": private_source_prime_budget,
        "candidate_factor_count_at_most_2p": len(candidate_factors),
        "relay_count": len(relays),
        "relays": relays,
    }


def run_audit(
    limit: int, base_shift_bound: int, private_source_prime_budget: int = 0
) -> dict[str, object]:
    """Audit all common base-fan failures through the stated prime limit."""
    if limit < 73 or base_shift_bound < 2:
        raise ValueError("limit >= 73 and base_shift_bound >= 2 are required")
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        2 * limit + 4 * base_shift_bound
    )
    pairs = tuple(
        canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    common_failures = [
        prime
        for prime in core_primes
        if all(
            canonical.witness_for_pair(prime, pair, smallest_factors) is None
            for pair in pairs
        )
    ]
    profiles = [
        relay_for_prime(
            prime,
            base_shift_bound,
            smallest_factors,
            private_source_prime_budget,
        )
        for prime in common_failures
    ]
    relayed = [profile for profile in profiles if profile["relay_count"]]
    shift_histogram = Counter(
        relay["shift"] for profile in relayed for relay in profile["relays"]
    )
    first_relay_shift_histogram = Counter(
        profile["relays"][0]["shift"] for profile in relayed
    )
    return {
        "arithmetic": (
            "exact SPF factorization; all collision-closure divisors h <= 2p; "
            "optional one-private-source factors; and all canonical pairs "
            "4ac | h+1 in the natural range a^2c <= p/4"
        ),
        "scope_note": (
            "A finite relay audit. It searches collision-prime closure factors "
            "and, when selected, at most one source-labelled base-private prime. "
            "It does not exclude other certificates or descents."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "private_source_prime_budget": private_source_prime_budget,
        "core_prime_count": len(core_primes),
        "common_failure_count": len(common_failures),
        "common_failures": common_failures,
        "relayed_count": len(relayed),
        "unrelayed_count": len(profiles) - len(relayed),
        "unrelayed_primes": [
            profile["prime"] for profile in profiles if not profile["relay_count"]
        ],
        "first_relay_shift_histogram": dict(sorted(first_relay_shift_histogram.items())),
        "all_relay_shift_histogram": dict(sorted(shift_histogram.items())),
        "profiles": profiles,
    }


def run_single_prime(
    prime: int, base_shift_bound: int, private_source_prime_budget: int = 0
) -> dict[str, object]:
    """Return the same exact relay profile for one stated core prime."""
    if prime < 73 or prime % 24 != 1 or base_shift_bound < 2:
        raise ValueError(
            "prime must be a core candidate and base_shift_bound must be at least 2"
        )
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        2 * prime + 4 * base_shift_bound
    )
    profile = relay_for_prime(
        prime, base_shift_bound, smallest_factors, private_source_prime_budget
    )
    return {
        "arithmetic": (
            "exact SPF factorization; all collision-closure divisors h <= 2p; "
            "optional one-private-source factors; and all canonical pairs "
            "4ac | h+1 in the natural range a^2c <= p/4"
        ),
        "scope_note": (
            "A single-prime finite relay audit. A missing relay does not exclude "
            "other certificates or a strict descent."
        ),
        "base_shift_bound": base_shift_bound,
        "private_source_prime_budget": private_source_prime_budget,
        "profile": profile,
    }


def run_selected_primes(
    primes: tuple[int, ...],
    base_shift_bound: int,
    private_source_prime_budget: int = 0,
) -> dict[str, object]:
    """Audit a fixed list of core primes without re-screening the full range."""
    if not primes or any(prime < 73 or prime % 24 != 1 for prime in primes):
        raise ValueError("primes must be nonempty core candidates")
    if len(set(primes)) != len(primes) or base_shift_bound < 2:
        raise ValueError("primes must be distinct and base_shift_bound at least 2")
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        2 * max(primes) + 4 * base_shift_bound
    )
    profiles = [
        relay_for_prime(
            prime,
            base_shift_bound,
            smallest_factors,
            private_source_prime_budget,
        )
        for prime in primes
    ]
    relayed = [profile for profile in profiles if profile["relay_count"]]
    return {
        "arithmetic": (
            "exact SPF factorization; all stated collision/private-source relay "
            "factors h <= 2p; and all canonical pairs 4ac | h+1 in the "
            "natural range a^2c <= p/4"
        ),
        "scope_note": (
            "A fixed-list finite relay audit. It does not claim that the "
            "specified private-source budget covers all core primes."
        ),
        "base_shift_bound": base_shift_bound,
        "private_source_prime_budget": private_source_prime_budget,
        "input_primes": list(primes),
        "relayed_count": len(relayed),
        "unrelayed_count": len(profiles) - len(relayed),
        "unrelayed_primes": [
            profile["prime"] for profile in profiles if not profile["relay_count"]
        ],
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--prime", type=int)
    parser.add_argument(
        "--primes",
        help="comma-separated core-prime list; mutually exclusive with --prime",
    )
    parser.add_argument("--base-shift-bound", type=int, default=14)
    parser.add_argument("--private-source-prime-budget", type=int, default=0)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    if args.prime is not None and args.primes is not None:
        parser.error("--prime and --primes cannot be used together")
    if args.primes is not None:
        payload = run_selected_primes(
            tuple(int(value) for value in args.primes.split(",") if value),
            args.base_shift_bound,
            args.private_source_prime_budget,
        )
    elif args.prime is not None:
        payload = run_single_prime(
            args.prime, args.base_shift_bound, args.private_source_prime_budget
        )
    else:
        payload = run_audit(
            args.limit, args.base_shift_bound, args.private_source_prime_budget
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
