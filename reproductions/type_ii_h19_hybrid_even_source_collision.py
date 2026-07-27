#!/usr/bin/env python3
"""Audit finite collisions between the H19 rays and fallback even sources.

For a standard external source n_k=p-(p-1)/(4k), an odd-distance even
source m_c=p-c, and a Type II ray r_s=p+4s, every cross-family gcd is
controlled by a p-independent integer:

  gcd(n_k,m_c) | (4k-1)c+1,
  gcd(m_c,r_s) | c+4s,
  gcd(m_c,m_d) | |c-d|.

Together with the existing standard-source/ray bounds, this makes any finite
hybrid source family a finite collision state. This program instantiates the
part needed by the stored H19 quadratic-descent misses: their selected even
source, the H19 rays, and the later pure-new Type II fallback ray.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVEN_SOURCE = (
    ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-300m-results.json"
)
DEFAULT_FALLBACK = (
    ROOT / "reproductions" / "type-ii-h19-hybrid-short-or-descent-300m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-hybrid-even-source-collision-300m-results.json"
)


def prime_factors(value: int) -> tuple[int, ...]:
    """Return distinct prime factors of a positive collision bound."""
    if value < 1:
        raise ValueError("collision bound must be positive")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return tuple(factors)


def standard_even_collision_bound(scale: int, distance: int) -> int:
    """Return a bound for gcd(n_k, p-c)."""
    if scale < 1 or distance < 1 or distance % 2 == 0:
        raise ValueError("scale must be positive and distance must be positive odd")
    return (4 * scale - 1) * distance + 1


def even_ray_collision_bound(distance: int, shift: int) -> int:
    """Return a bound for gcd(p-c, p+4s)."""
    if distance < 1 or distance % 2 == 0 or shift < 1:
        raise ValueError("distance must be positive odd and shift must be positive")
    return distance + 4 * shift


def even_even_collision_bound(left: int, right: int) -> int:
    """Return a bound for gcd(p-c, p-d), for distinct odd distances."""
    if (
        left < 1
        or right < 1
        or left % 2 == 0
        or right % 2 == 0
        or left == right
    ):
        raise ValueError("distances must be distinct positive odd integers")
    return abs(left - right)


def strip_primes(value: int, primes: tuple[int, ...]) -> int:
    for prime in primes:
        while value % prime == 0:
            value //= prime
    return value


def fallback_shift(record: dict[str, object]) -> int:
    """Recover the canonical ray shift and ensure its witness agrees."""
    witness = record["selected_witness"]
    if not isinstance(witness, dict):
        raise TypeError("fallback witness must be a mapping")
    shift = int(record["shift"])
    expected = int(witness["a"]) ** 2 * int(witness["c"])
    if shift != expected:
        raise AssertionError("fallback shift does not equal a^2 c")
    h = int(witness["h"])
    prime = int(record["prime"])
    if (prime + 4 * shift) % h:
        raise AssertionError("fallback new factor does not divide its ray")
    return shift


def profile(prime: int, distance: int, shifts: tuple[int, ...]) -> dict[str, object]:
    """Strip all finite even-source/ray collisions for one selected source."""
    if tuple(sorted(set(shifts))) != shifts:
        raise ValueError("shifts must be increasing and distinct")
    source = prime - distance
    rays = {shift: prime + 4 * shift for shift in shifts}
    collision: set[int] = set()
    source_ray_bounds: list[dict[str, int]] = []
    actual_source_ray_gcds: list[dict[str, int]] = []
    for shift, ray in rays.items():
        bound = even_ray_collision_bound(distance, shift)
        gcd = math.gcd(source, ray)
        if bound % gcd:
            raise AssertionError("even-source/ray gcd violates its fixed bound")
        collision.update(prime_factors(bound))
        source_ray_bounds.append({"shift": shift, "bound": bound, "gcd": gcd})
        if gcd > 1:
            actual_source_ray_gcds.append({"shift": shift, "gcd": gcd})
    for index, left in enumerate(shifts):
        for right in shifts[index + 1 :]:
            collision.update(prime_factors(right - left))
            if (right - left) % math.gcd(rays[left], rays[right]):
                raise AssertionError("ray/ray gcd violates its fixed difference bound")
    primes = tuple(sorted(collision))
    values = {"even_source": source, **{f"ray:{shift}": ray for shift, ray in rays.items()}}
    private = {label: strip_primes(value, primes) for label, value in values.items()}
    ordered = list(private)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            if math.gcd(private[left], private[right]) != 1:
                raise AssertionError("stripped hybrid private parts must be pairwise coprime")
    return {
        "prime": prime,
        "distance": distance,
        "even_source": source,
        "shifts": list(shifts),
        "collision_primes": list(primes),
        "source_ray_bounds": source_ray_bounds,
        "actual_source_ray_gcds": actual_source_ray_gcds,
        "private_parts_pairwise_coprime": True,
    }


def run_audit(
    even_source_payload: dict[str, object], fallback_payload: dict[str, object]
) -> dict[str, object]:
    """Join selected strict lifts to their Type II fallback rays."""
    h19_bound = int(even_source_payload["base_shift_bound"])
    fallbacks = {
        int(row["prime"]): row for row in fallback_payload["fallback_records"]
    }
    records: list[dict[str, object]] = []
    for row in even_source_payload["fallbacks"]:
        prime = int(row["prime"])
        fallback = fallbacks.get(prime)
        if fallback is None:
            raise AssertionError("even-source fallback has no pure-new Type II record")
        direct_shift = fallback_shift(fallback)
        shifts = tuple(sorted(set(range(1, h19_bound + 1)) | {direct_shift}))
        audit = profile(prime, int(row["distance"]), shifts)
        direct_row = next(
            bound for bound in audit["source_ray_bounds"] if bound["shift"] == direct_shift
        )
        records.append(
            {
                **audit,
                "pure_new_type_ii_shift": direct_shift,
                "pure_new_type_ii_factor": int(fallback["selected_witness"]["h"]),
                "even_source_direct_ray_gcd": direct_row["gcd"],
            }
        )
    if set(fallbacks) != {record["prime"] for record in records}:
        raise AssertionError("the two layers disagree on their pressure primes")
    return {
        "arithmetic": (
            "exact gcd identities, trial factorization of fixed collision "
            "bounds, and pairwise-coprime checks after stripping those primes"
        ),
        "scope_note": (
            "A finite collision audit of the stored pressure points. "
            "It gives no universal bound on scales, distances, or shifts."
        ),
        "prime_limit": even_source_payload["prime_limit"],
        "h19_shift_bound": h19_bound,
        "pressure_point_count": len(records),
        "all_private_parts_pairwise_coprime": all(
            record["private_parts_pairwise_coprime"] for record in records
        ),
        "all_even_source_direct_ray_gcds_are_one": all(
            record["even_source_direct_ray_gcd"] == 1 for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--even-source", type=Path, default=DEFAULT_EVEN_SOURCE)
    parser.add_argument("--fallback", type=Path, default=DEFAULT_FALLBACK)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    even_source_payload = json.loads(args.even_source.read_text(encoding="utf-8"))
    fallback_payload = json.loads(args.fallback.read_text(encoding="utf-8"))
    result = run_audit(even_source_payload, fallback_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
