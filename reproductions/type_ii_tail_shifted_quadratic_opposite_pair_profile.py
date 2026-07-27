#!/usr/bin/env python3
"""Profile opposite ordinary-divisor pairs on minimal shifted quadratic rays.

For every complete normalized tail f | L^2 with f == -L (mod t), write
f / L = a / b in lowest signed-exponent form.  Then a,b | L and a == -b
(mod t).  This audit measures the smallest number of prime coordinates that
such an opposite pair needs; it is an exact restatement of the already
verified square-tail witnesses, not a heuristic factor search.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SQUARE_AUDIT = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_square_necessity.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
PARITY_GROUP_CAP = 10_000


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


square_audit = load_module("tail_shifted_opposite_pair_square_audit", SQUARE_AUDIT)


def signed_pair(factor: int, L: int, t: int, L_exponents: dict[int, int]) -> dict[str, object]:
    """Return the canonical coprime ordinary-divisor pair a/b = factor/L."""
    remaining = factor
    numerator = 1
    denominator = 1
    signed_support = 0
    signed_l1 = 0
    positive_support = 0
    negative_support = 0
    maximum_displacement = 0
    coordinates = []
    for prime, L_exponent in sorted(L_exponents.items()):
        factor_exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            factor_exponent += 1
        displacement = factor_exponent - L_exponent
        if displacement > 0:
            numerator *= prime**displacement
            positive_support += 1
        elif displacement < 0:
            denominator *= prime ** (-displacement)
            negative_support += 1
        if displacement:
            signed_support += 1
            signed_l1 += abs(displacement)
            maximum_displacement = max(maximum_displacement, abs(displacement))
            coordinates.append({"prime": prime, "displacement": displacement})
    if remaining != 1:
        raise AssertionError("tail factor has a prime outside L")
    if numerator * denominator and L * numerator != factor * denominator:
        raise AssertionError("signed factor coordinates did not reconstruct f/L")
    if L % numerator or L % denominator or (numerator + denominator) % t:
        raise AssertionError("canonical factors are not an opposite ordinary-divisor pair")
    return {
        "numerator_divisor": numerator,
        "denominator_divisor": denominator,
        "signed_prime_support_count": signed_support,
        "signed_l1_displacement": signed_l1,
        "maximum_coordinate_displacement": maximum_displacement,
        "positive_prime_support_count": positive_support,
        "negative_prime_support_count": negative_support,
        "coordinates": coordinates,
    }


def generated_subgroup_with_limit(primes, t: int, limit: int) -> tuple[set[int] | None, int | None]:
    """Generate a residue subgroup only until exceeding a decisive size bound."""
    subgroup = {1}
    for prime in primes:
        next_subgroup = set()
        power = 1
        while True:
            before = len(next_subgroup)
            next_subgroup.update(left * power % t for left in subgroup)
            if len(next_subgroup) > limit:
                return None, len(next_subgroup)
            if len(next_subgroup) == before:
                break
            power = power * prime % t
        subgroup = next_subgroup
    return subgroup, None


def ordinary_divisor_residue_profile(L_exponents: dict[int, int], t: int, spf) -> dict[str, int | bool | None]:
    """Measure the elementary more-than-half-density sufficient condition.

    For D = Pi_t(L), D and -D are disjoint if no opposite divisor pair exists.
    Thus |D| > |(Z/tZ)^*|/2 forces an opposite pair.  The enumeration here is
    exact and only over the ordinary divisors of L, not the square-tail set.
    """
    group_size = t
    remaining = t
    while remaining > 1:
        prime = spf[remaining]
        group_size = group_size // prime * (prime - 1)
        while remaining % prime == 0:
            remaining //= prime
    residues = {1}
    symmetric_residues = {1}
    for prime, exponent in L_exponents.items():
        residues = {
            residue * pow(prime, power, t) % t
            for residue in residues
            for power in range(exponent + 1)
        }
        negative_power = pow(pow(prime, exponent, t), -1, t)
        symmetric_residues = {
            residue * negative_power * pow(prime, power, t) % t
            for residue in symmetric_residues
            for power in range(2 * exponent + 1)
        }
    if any(math.gcd(residue, t) != 1 for residue in residues):
        raise AssertionError("ordinary divisor residue escaped the unit group")
    subgroup_limit = max(
        2 * len(residues), len(symmetric_residues), min(group_size, PARITY_GROUP_CAP)
    )
    generated_subgroup, overflow_size = generated_subgroup_with_limit(
        L_exponents, t, subgroup_limit
    )
    generated_exact = generated_subgroup is not None
    contains_minus_one = (-1) % t in generated_subgroup if generated_exact else None
    involutions = (
        [residue for residue in generated_subgroup if residue * residue % t == 1]
        if generated_exact
        else []
    )
    other_involutions = [residue for residue in involutions if residue != (-1) % t]
    complement_size = (
        len(generated_subgroup) - len(symmetric_residues) if generated_exact else None
    )
    if any(pow(residue, -1, t) not in symmetric_residues for residue in symmetric_residues):
        raise AssertionError("symmetric exponent box is not inverse closed")
    parity_forces_target = bool(
        contains_minus_one
        and complement_size is not None
        and complement_size % 2 == 0
        and all(residue in symmetric_residues for residue in other_involutions)
    )
    return {
        "ordinary_divisor_residue_count": len(residues),
        "unit_group_size": group_size,
        "more_than_half_density": 2 * len(residues) > group_size,
        "generated_subgroup_size": len(generated_subgroup) if generated_exact else None,
        "generated_subgroup_size_lower_bound": overflow_size,
        "minus_one_in_generated_subgroup": contains_minus_one,
        "more_than_half_generated_subgroup_density": (
            bool(contains_minus_one) and 2 * len(residues) > len(generated_subgroup)
        ),
        "symmetric_box_residue_count": len(symmetric_residues),
        "symmetric_box_fills_generated_subgroup": (
            bool(contains_minus_one) and len(symmetric_residues) == len(generated_subgroup)
        ),
        "symmetric_box_complement_size": complement_size,
        "generated_subgroup_involution_count": len(involutions) if generated_exact else None,
        "non_target_involutions_all_in_symmetric_box": (
            all(residue in symmetric_residues for residue in other_involutions)
            if generated_exact
            else None
        ),
        "inverse_pairing_parity_forces_target": parity_forces_target,
    }


def ray_profile(prime: int, shift: int, spf) -> dict[str, object]:
    """Exhaust all complete tails at one stored minimal offset."""
    base = (prime - shift) // 4
    witnesses = []
    density_rows = []
    compatible_k_count = 0
    for k in square_audit.short_certificate.positive_divisors_from_spf(base, spf):
        if (4 * k - 1) % shift:
            continue
        compatible_k_count += 1
        q = 4 * k - 1
        source = (q * prime + shift) // (q + 1)
        if (q + 1) * source != q * prime + shift or source % shift:
            raise AssertionError("minimal-offset ray failed source normalization")
        tail_source = source // shift
        t = q // shift
        L = k * tail_source
        L_exponents = square_audit.factor_exponents((k, tail_source), spf)
        density = ordinary_divisor_residue_profile(L_exponents, t, spf)
        density_rows.append({"k": k, "t": t, "L": L, **density})
        for row in square_audit.tail_factors(prime, shift, k, spf):
            pair = signed_pair(int(row["factor"]), L, t, L_exponents)
            witnesses.append({**row, **pair})
    if not witnesses:
        raise AssertionError("minimal offset has no complete square-tail witness")

    def best(key: str) -> dict[str, object]:
        return min(witnesses, key=lambda row: (int(row[key]), int(row["factor"]), int(row["k"])))

    minimum_support = best("signed_prime_support_count")
    minimum_l1 = best("signed_l1_displacement")
    one_prime = [row for row in witnesses if int(row["signed_prime_support_count"]) == 1]
    two_prime = [row for row in witnesses if int(row["signed_prime_support_count"]) <= 2]
    density_hits = [row for row in density_rows if row["more_than_half_density"]]
    generated_density_hits = [
        row for row in density_rows if row["more_than_half_generated_subgroup_density"]
    ]
    symmetric_saturation_hits = [
        row for row in density_rows if row["symmetric_box_fills_generated_subgroup"]
    ]
    parity_hits = [row for row in density_rows if row["inverse_pairing_parity_forces_target"]]
    return {
        "prime": prime,
        "minimal_offset": shift,
        "compatible_k_count": compatible_k_count,
        "complete_opposite_pair_witness_count": len(witnesses),
        "minimum_signed_prime_support_count": int(minimum_support["signed_prime_support_count"]),
        "minimum_support_witness": minimum_support,
        "minimum_signed_l1_displacement": int(minimum_l1["signed_l1_displacement"]),
        "minimum_l1_witness": minimum_l1,
        "one_prime_opposite_pair_witness_count": len(one_prime),
        "two_prime_opposite_pair_witness_count": len(two_prime),
        "first_one_prime_opposite_pair_witness": one_prime[0] if one_prime else None,
        "more_than_half_density_witness_count": len(density_hits),
        "first_more_than_half_density_witness": density_hits[0] if density_hits else None,
        "more_than_half_generated_subgroup_density_witness_count": len(generated_density_hits),
        "first_more_than_half_generated_subgroup_density_witness": (
            generated_density_hits[0] if generated_density_hits else None
        ),
        "symmetric_box_subgroup_saturation_witness_count": len(symmetric_saturation_hits),
        "first_symmetric_box_subgroup_saturation_witness": (
            symmetric_saturation_hits[0] if symmetric_saturation_hits else None
        ),
        "inverse_pairing_parity_witness_count": len(parity_hits),
        "first_inverse_pairing_parity_witness": parity_hits[0] if parity_hits else None,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    records_in = payload["records"]
    if not records_in:
        raise ValueError("input has no minimal-offset rays")
    primes = [int(record["prime"]) for record in records_in]
    spf = square_audit.targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    square_essential = {
        int(record["prime"])
        for record in records_in
        if bool(record["square_tail_essential_at_minimal_offset"])
    }
    for record in records_in:
        profile = ray_profile(int(record["prime"]), int(record["minimal_offset"]), spf)
        profile["square_tail_essential_at_minimal_offset"] = int(record["prime"]) in square_essential
        records.append(profile)
    support_histogram = Counter(int(record["minimum_signed_prime_support_count"]) for record in records)
    essential_records = [record for record in records if record["square_tail_essential_at_minimal_offset"]]
    essential_histogram = Counter(
        int(record["minimum_signed_prime_support_count"]) for record in essential_records
    )
    one_prime_misses = [
        int(record["prime"]) for record in records if not record["one_prime_opposite_pair_witness_count"]
    ]
    two_prime_misses = [
        int(record["prime"]) for record in records if not record["two_prime_opposite_pair_witness_count"]
    ]
    density_misses = [
        int(record["prime"])
        for record in records
        if not record["more_than_half_density_witness_count"]
    ]
    essential_density_hits = [
        record
        for record in essential_records
        if record["more_than_half_density_witness_count"]
    ]
    generated_density_misses = [
        int(record["prime"])
        for record in records
        if not record["more_than_half_generated_subgroup_density_witness_count"]
    ]
    essential_generated_density_hits = [
        record
        for record in essential_records
        if record["more_than_half_generated_subgroup_density_witness_count"]
    ]
    symmetric_saturation_misses = [
        int(record["prime"])
        for record in records
        if not record["symmetric_box_subgroup_saturation_witness_count"]
    ]
    essential_symmetric_saturation_hits = [
        record
        for record in essential_records
        if record["symmetric_box_subgroup_saturation_witness_count"]
    ]
    parity_misses = [
        int(record["prime"])
        for record in records
        if not record["inverse_pairing_parity_witness_count"]
    ]
    parity_beyond_saturation = [
        int(record["prime"])
        for record in records
        if record["inverse_pairing_parity_witness_count"]
        and not record["symmetric_box_subgroup_saturation_witness_count"]
    ]
    return {
        "arithmetic": (
            "complete enumeration of every compatible k and every verified normalized f | L^2 "
            "tail at each stored minimal offset; each tail is converted exactly to the "
            "coprime ordinary-divisor pair a,b | L with a == -b (mod t)"
        ),
        "scope_note": (
            "This is a finite minimal-offset profile. It neither proves a uniform support "
            "bound at larger offsets nor asserts that the displayed witnesses are unique. "
            "Generated-subgroup half-density failures are certified once the subgroup "
            "exceeds twice the ordinary divisor-residue count; no large subgroup is truncated "
            "as a possible hit."
        ),
        "prime_limit": payload["prime_limit"],
        "minimal_offset_ray_count": len(records),
        "minimum_signed_support_histogram": {
            str(support): count for support, count in sorted(support_histogram.items())
        },
        "square_essential_minimum_signed_support_histogram": {
            str(support): count for support, count in sorted(essential_histogram.items())
        },
        "one_prime_opposite_pair_hit_count": len(records) - len(one_prime_misses),
        "one_prime_opposite_pair_miss_primes": one_prime_misses,
        "two_prime_opposite_pair_hit_count": len(records) - len(two_prime_misses),
        "two_prime_opposite_pair_miss_primes": two_prime_misses,
        "more_than_half_density_hit_count": len(records) - len(density_misses),
        "square_essential_more_than_half_density_hit_count": len(essential_density_hits),
        "more_than_half_density_miss_primes": density_misses,
        "more_than_half_generated_subgroup_density_hit_count": len(records) - len(generated_density_misses),
        "square_essential_more_than_half_generated_subgroup_density_hit_count": len(
            essential_generated_density_hits
        ),
        "more_than_half_generated_subgroup_density_miss_primes": generated_density_misses,
        "symmetric_box_subgroup_saturation_hit_count": len(records) - len(symmetric_saturation_misses),
        "square_essential_symmetric_box_subgroup_saturation_hit_count": len(
            essential_symmetric_saturation_hits
        ),
        "symmetric_box_subgroup_saturation_miss_primes": symmetric_saturation_misses,
        "inverse_pairing_parity_hit_count": len(records) - len(parity_misses),
        "inverse_pairing_parity_beyond_saturation_primes": parity_beyond_saturation,
        "inverse_pairing_parity_miss_primes": parity_misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
