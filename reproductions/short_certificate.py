#!/usr/bin/env python3
"""Exact search for small-gap Bradford divisor certificates.

For an odd prime p == 1 (mod 4), write m = 4x - p.  The smallest
denominator range in Bradford's correspondence is then equivalent to
3 <= m <= p - 2 and m == 3 (mod 4).  This script searches those m in
increasing order; it is a finite experiment, not a proof of a uniform bound.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "short-certificate-results.json"


@dataclass(frozen=True)
class GapCertificate:
    """A Bradford Type I/II certificate written with m = 4x - p."""

    prime: int
    certificate_type: str
    gap: int
    x: int
    divisor: int
    y: int
    z: int


@dataclass(frozen=True)
class ExternalSourceDescentWitness:
    """A marked source solution and its strict one-coordinate lift."""

    prime: int
    source_denominator: int
    k: int
    q: int
    factor: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class ScaledSourceDescentWitness:
    """A one-coordinate lift with first source denominator ``a*n/b``."""

    prime: int
    source_denominator: int
    numerator: int
    ratio_denominator: int
    shift: int
    distance: int
    q: int
    factor: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class EvenSplitDescentWitness:
    """A lift from a nonstandard two-unit split of the even source tail."""

    prime: int
    source_denominator: int
    factor: int
    replaced_denominator: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class ResidualSplitDescentWitness:
    """A lift from the complete split of ``(4-r)/n`` after keeping ``n/r``."""

    prime: int
    source_denominator: int
    retained_numerator: int
    factor: int
    replaced_denominator: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class EvenStandardTwoTailDescentWitness:
    """A lift preserving one ``n`` from the standard even source solution."""

    prime: int
    source_denominator: int
    factor: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class ThreeDivisibleStandardTwoTailDescentWitness:
    """A lift preserving one ``2*n`` from the standard three-divisible source."""

    prime: int
    source_denominator: int
    factor: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class AffineStandardTailDescentWitness:
    """A Type I ray lifted from an even or three-divisible standard source."""

    prime: int
    source_kind: str
    source_denominator: int
    first_scale: int
    retained_scale: int
    divisor_scale: int
    scale: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class TypeIITailDeflationWitness:
    """A strict descent obtained by removing `p` from both Type II tails."""

    prime: int
    source_denominator: int
    gap: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class TypeIIScaledFirstTailDeflationWitness:
    """A Type II descent that scales the source first term by a factor k."""

    prime: int
    first_scale: int
    source_denominator: int
    gap: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


@dataclass(frozen=True)
class TypeINormalTailDeflationWitness:
    """A Type I normal form whose p-divisible tail deflates to a source."""

    prime: int
    source_denominator: int
    normal_a: int
    normal_b: int
    normal_c: int
    quotient: int
    source_solution: tuple[int, int, int]
    target_solution: tuple[int, int, int]
    certificate: GapCertificate


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        for value in range(prime * prime, limit + 1, prime):
            if spf[value] == value:
                spf[value] = prime
    return spf


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (((limit - prime * prime) // prime) + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def divisors_of_square(value: int, spf: list[int]) -> list[int]:
    if value <= 0 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    factors: dict[int, int] = {}
    while value > 1:
        prime = spf[value]
        factors[prime] = factors.get(prime, 0) + 2
        value //= prime

    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def positive_divisors_from_spf(value: int, spf: list[int]) -> list[int]:
    """Return sorted positive divisors using a table of smallest prime factors."""
    if value <= 0 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    factors: dict[int, int] = {}
    while value > 1:
        prime = spf[value]
        factors[prime] = factors.get(prime, 0) + 1
        value //= prime
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def positive_divisors_product_from_spf(
    first: int, second: int, spf: list[int]
) -> list[int]:
    """Return the divisors of ``first * second`` without sizing SPF to its product."""
    if (
        first <= 0
        or second <= 0
        or first >= len(spf)
        or second >= len(spf)
    ):
        raise ValueError("SPF table does not cover the requested factors")

    factors: dict[int, int] = {}
    for value in (first, second):
        while value > 1:
            prime = spf[value]
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime

    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def positive_divisors_square_product_from_spf(
    first: int, second: int, spf: list[int]
) -> list[int]:
    """Return the divisors of ``(first * second)^2`` from separately factored inputs."""
    if (
        first <= 0
        or second <= 0
        or first >= len(spf)
        or second >= len(spf)
    ):
        raise ValueError("SPF table does not cover the requested factors")

    factors: dict[int, int] = {}
    for value in (first, second):
        while value > 1:
            prime = spf[value]
            factors[prime] = factors.get(prime, 0) + 2
            value //= prime

    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def positive_divisors_square_factors_from_spf(
    values: tuple[int, ...], spf: list[int]
) -> list[int]:
    """Return divisors of the square of a product from its separate factors."""
    if not values or any(value <= 0 or value >= len(spf) for value in values):
        raise ValueError("SPF table does not cover the requested factors")

    factors: dict[int, int] = {}
    for value in values:
        while value > 1:
            prime = spf[value]
            factors[prime] = factors.get(prime, 0) + 2
            value //= prime

    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def two_term_unit_fraction_pairs(
    numerator: int, denominator: int, spf: list[int]
) -> list[tuple[int, int]]:
    """Enumerate positive u<=v with numerator/denominator = 1/u + 1/v."""
    if numerator <= 0 or denominator <= 0:
        return []
    pairs: set[tuple[int, int]] = set()
    for factor in divisors_of_square(denominator, spf):
        complement = denominator * denominator // factor
        if (denominator + factor) % numerator or (denominator + complement) % numerator:
            continue
        first = (denominator + factor) // numerator
        second = (denominator + complement) // numerator
        if first > 0 and second > 0:
            pairs.add(tuple(sorted((first, second))))
    return sorted(pairs)


def verify_certificate(certificate: GapCertificate) -> bool:
    """Check the divisibility conditions and reconstructed identity exactly."""
    p = certificate.prime
    m = certificate.gap
    x = certificate.x
    d = certificate.divisor
    y = certificate.y
    z = certificate.z
    if p < 3 or p % 4 != 1 or m % 4 != 3 or not 3 <= m <= p - 2:
        return False
    if 4 * x - p != m or x * 4 != p + m or x * 2 > p or d <= 0 or x * x % d:
        return False
    if certificate.certificate_type == "I":
        if (p * x + d) % m or p % y == 0:
            return False
    elif certificate.certificate_type == "II":
        if d > x or (x + d) % m or y % p:
            return False
    else:
        return False
    return Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)


def certificate_at_gap(p: int, gap: int, spf: list[int]) -> GapCertificate | None:
    """Return a certificate at one prescribed gap, if one exists."""
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap:
        return None
    for divisor in divisors_of_square(x, spf):
        if (p * x + divisor) % gap == 0:
            y = (p * x + divisor) // gap
            numerator = p * (x + p * x * x // divisor)
            if numerator % gap == 0:
                certificate = GapCertificate(p, "I", gap, x, divisor, y, numerator // gap)
                if verify_certificate(certificate):
                    return certificate
        if divisor <= x and (x + divisor) % gap == 0:
            y = p * (x + divisor) // gap
            numerator = p * (x + x * x // divisor)
            if numerator % gap == 0:
                certificate = GapCertificate(p, "II", gap, x, divisor, y, numerator // gap)
                if verify_certificate(certificate):
                    return certificate
    return None


def type_i_residue_certificate(p: int, gap: int, spf: list[int]) -> GapCertificate | None:
    """Find Type I through the equivalent residue -1/4 among divisors of x^2."""
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap:
        return None
    target = (-pow(4, -1, gap)) % gap
    for complement in divisors_of_square(x, spf):
        if complement % gap != target:
            continue
        divisor = x * x // complement
        y = (p * x + divisor) // gap
        numerator = p * (x + p * complement)
        if numerator % gap:
            continue
        certificate = GapCertificate(p, "I", gap, x, divisor, y, numerator // gap)
        if verify_certificate(certificate):
            return certificate
    return None


def type_ii_residue_certificate(p: int, gap: int, spf: list[int]) -> GapCertificate | None:
    """Find Type II through the equivalent residue -x among divisors of x^2."""
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap:
        return None
    target = (-x) % gap
    for candidate in divisors_of_square(x, spf):
        if candidate % gap != target:
            continue
        divisor = min(candidate, x * x // candidate)
        y = p * (x + divisor) // gap
        numerator = p * (x + x * x // divisor)
        if numerator % gap:
            continue
        certificate = GapCertificate(p, "II", gap, x, divisor, y, numerator // gap)
        if verify_certificate(certificate):
            return certificate
    return None


def type_ii_tail_deflation_witness(
    p: int, gap: int, spf: list[int]
) -> TypeIITailDeflationWitness | None:
    """Return the two-tail Type II descent witness at one prescribed gap.

    If a Type II certificate has gap m and m+1 divides p-1, its two
    p-divisible denominators may both be divided by p.  The resulting source
    denominator is n=(p+m)/(m+1), which is strictly smaller than p.
    """
    if (p - 1) % (gap + 1):
        return None
    certificate = type_ii_residue_certificate(p, gap, spf)
    if certificate is None:
        return None
    if certificate.y % p or certificate.z % p:
        raise AssertionError("Type II certificate does not have two p-divisible tails")
    source_denominator = (p + gap) // (gap + 1)
    if (gap + 1) * source_denominator != p + gap:
        raise AssertionError("nonintegral two-tail deflation source")
    if not 2 <= source_denominator < p:
        raise AssertionError("two-tail deflation source is not strictly smaller")
    source_solution = (
        certificate.x,
        certificate.y // p,
        certificate.z // p,
    )
    target_solution = (certificate.x, certificate.y, certificate.z)
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("two-tail deflation source did not verify")
    return TypeIITailDeflationWitness(
        p,
        source_denominator,
        gap,
        source_solution,
        target_solution,
        certificate,
    )


def type_ii_tail_deflation_scan(
    p: int, spf: list[int]
) -> list[TypeIITailDeflationWitness]:
    """Enumerate all Type II tail-deflation witnesses indexed by divisors of p-1."""
    if p % 24 != 1:
        return []
    witnesses: list[TypeIITailDeflationWitness] = []
    for divisor in positive_divisors_from_spf(p - 1, spf):
        if divisor % 4:
            continue
        witness = type_ii_tail_deflation_witness(p, divisor - 1, spf)
        if witness is not None:
            witnesses.append(witness)
    return witnesses


def first_type_ii_tail_deflation_witness(
    p: int, spf: list[int]
) -> TypeIITailDeflationWitness | None:
    """Return the least-gap two-tail deflation witness, if the selector hits."""
    if p % 24 != 1:
        return None
    for divisor in positive_divisors_from_spf(p - 1, spf):
        if divisor % 4:
            continue
        witness = type_ii_tail_deflation_witness(p, divisor - 1, spf)
        if witness is not None:
            return witness
    return None


def type_ii_scaled_first_tail_deflation_witness(
    p: int, gap: int, first_scale: int, spf: list[int]
) -> TypeIIScaledFirstTailDeflationWitness | None:
    """Return a Type II lift (k*x, Y, Z) -> (x, p*Y, p*Z).

    With m=gap, the source denominator is
    n=k*(p+m)/(k*m+1).  Its integrality is exactly k*m+1 | k*p-1.
    The k=1 specialization is ordinary two-tail deflation.
    """
    if first_scale < 1:
        return None
    denominator = first_scale * gap + 1
    if (first_scale * p - 1) % denominator:
        return None
    certificate = type_ii_residue_certificate(p, gap, spf)
    if certificate is None:
        return None
    if certificate.y % p or certificate.z % p:
        raise AssertionError("Type II certificate does not have two p-divisible tails")
    source_denominator = first_scale * (p + gap) // denominator
    if denominator * source_denominator != first_scale * (p + gap):
        raise AssertionError("nonintegral scaled-first tail source")
    if not 2 <= source_denominator < p:
        raise AssertionError("scaled-first tail source is not strictly smaller")
    source_solution = (
        first_scale * certificate.x,
        certificate.y // p,
        certificate.z // p,
    )
    target_solution = (certificate.x, certificate.y, certificate.z)
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("scaled-first tail source did not verify")
    return TypeIIScaledFirstTailDeflationWitness(
        p,
        first_scale,
        source_denominator,
        gap,
        source_solution,
        target_solution,
        certificate,
    )


def type_ii_scaled_first_tail_deflation_scan(
    p: int, first_scale_cap: int, gap_cap: int, spf: list[int]
) -> TypeIIScaledFirstTailDeflationWitness | None:
    """Find the first witness in a finite (first-scale, gap) parameter box."""
    if p % 24 != 1 or first_scale_cap < 1 or gap_cap < 3:
        return None
    for first_scale in range(1, first_scale_cap + 1):
        for gap in range(3, min(gap_cap, p - 2) + 1, 4):
            witness = type_ii_scaled_first_tail_deflation_witness(
                p, gap, first_scale, spf
            )
            if witness is not None:
                return witness
    return None


def type_ii_shared_divisor_tail_deflation_scan(
    p: int, gap_cap: int, spf: list[int]
) -> TypeIIScaledFirstTailDeflationWitness | None:
    """Find a least-gap scaled-first witness by factoring p+m directly.

    For each gap m, D=k*m+1 must divide p+m and be 1 modulo m. Enumerating
    divisors of p+m therefore examines every positive first scale k at that
    gap, without an artificial k cutoff.
    """
    if p % 24 != 1 or gap_cap < 3:
        return None
    last_gap = min(gap_cap, p - 2)
    if p + last_gap >= len(spf):
        raise ValueError("SPF table does not cover the shifted values p+m")
    for gap in range(3, last_gap + 1, 4):
        for shared_divisor in positive_divisors_from_spf(p + gap, spf):
            if shared_divisor == 1 or (shared_divisor - 1) % gap:
                continue
            first_scale = (shared_divisor - 1) // gap
            witness = type_ii_scaled_first_tail_deflation_witness(
                p, gap, first_scale, spf
            )
            if witness is not None:
                return witness
    return None


def p_plus_one_type_i_certificate(p: int, spf: list[int]) -> GapCertificate | None:
    """Use the least 3 (mod 4) prime factor of (p+1)/2 as a Type I gap."""
    if p % 24 != 1:
        return None
    half_plus_one = (p + 1) // 2
    value = half_plus_one
    candidate_gap: int | None = None
    while value > 1:
        prime = spf[value]
        if prime % 4 == 3:
            candidate_gap = prime if candidate_gap is None else min(candidate_gap, prime)
        while value % prime == 0:
            value //= prime
    if candidate_gap is None:
        return None
    if candidate_gap * candidate_gap > half_plus_one:
        raise AssertionError("a 3 mod 4 factor of N == 1 mod 4 must occur below sqrt(N)")
    x = (p + candidate_gap) // 4
    divisor = x
    y = x * (p + 1) // candidate_gap
    z = p * x * (p + 1) // candidate_gap
    certificate = GapCertificate(p, "I", candidate_gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed p+1 certificate did not verify")
    return certificate


def p_plus_two_type_i_certificate(p: int, spf: list[int]) -> GapCertificate | None:
    """Use a 7 (mod 8) divisor of p+2 as an external-source i=2 gap.

    For p == 1 (mod 24), such a divisor m gives p+m == 0 (mod 8).
    Thus x=(p+m)/4 is even and d=2*x divides x^2, while
    m divides x*(p+2)=p*x+d.  The least qualifying divisor is used only
    for determinism; no square-root bound is claimed for this family.
    """
    if p % 24 != 1 or p + 2 >= len(spf):
        return None
    for gap in positive_divisors_from_spf(p + 2, spf):
        if gap % 8 != 7:
            continue
        certificate = external_source_type_i_certificate(p, 2, gap)
        if certificate is None:
            raise AssertionError("constructed p+2 certificate did not verify")
        return certificate
    return None


def p_plus_six_type_i_certificate(p: int, spf: list[int]) -> GapCertificate | None:
    """Use a 23 (mod 24) divisor of p+6 as an external-source i=6 gap.

    Here p+m is divisible by 24, so x=(p+m)/4 is a multiple of 6 and
    d=6*x divides x^2.  The construction accepts composite gap divisors;
    this is essential to the exact residue classification of its failure.
    """
    if p % 24 != 1 or p + 6 >= len(spf):
        return None
    for gap in positive_divisors_from_spf(p + 6, spf):
        if gap % 24 != 23:
            continue
        certificate = external_source_type_i_certificate(p, 6, gap)
        if certificate is None:
            raise AssertionError("constructed p+6 certificate did not verify")
        return certificate
    return None


def lcm_boundary_type_i_certificate(
    p: int, gap: int, spf: list[int]
) -> GapCertificate | None:
    """Find the A=1 Type I face, equivalently z=p*lcm(x,y).

    This is stricter than an arbitrary Type I certificate: its divisor must
    divide x rather than merely x^2.  The recovered solution then has
    gcd(x,y)=d and z=p*lcm(x,y), the geometric lcm-boundary pattern.
    """
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap:
        return None
    for divisor in positive_divisors_from_spf(x, spf):
        if (p * x + divisor) % gap:
            continue
        y = (p * x + divisor) // gap
        z = p * (x + p * x * x // divisor) // gap
        certificate = GapCertificate(p, "I", gap, x, divisor, y, z)
        if not verify_certificate(certificate):
            raise AssertionError("constructed lcm-boundary certificate did not verify")
        if math.gcd(x, y) != divisor or z != p * math.lcm(x, y):
            raise AssertionError("lcm-boundary certificate did not reconstruct its geometry")
        return certificate
    return None


def gap_seven_congruence_certificate(p: int) -> GapCertificate | None:
    """Return the unconditional m=7 certificate in three core residue classes.

    For p == 1 (mod 24), x=(p+7)/4 is even. The choices
    p == 3, 5, 6 (mod 7) respectively use (II,d)=(II,1), (I,2*x),
    and (II,2). The other three nonzero residue classes are intentionally
    left unresolved by this fixed-divisor construction.
    """
    if p % 24 != 1:
        return None
    x = (p + 7) // 4
    residue = p % 7
    if residue == 3:
        certificate_type, divisor = "II", 1
    elif residue == 5:
        certificate_type, divisor = "I", 2 * x
    elif residue == 6:
        certificate_type, divisor = "II", 2
    else:
        return None

    if certificate_type == "I":
        y = (p * x + divisor) // 7
        z = p * (x + p * x * x // divisor) // 7
    else:
        y = p * (x + divisor) // 7
        z = p * (x + x * x // divisor) // 7
    certificate = GapCertificate(p, certificate_type, 7, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed gap-seven congruence certificate did not verify")
    return certificate


def positive_divisors(value: int) -> list[int]:
    """Return the sorted positive divisors of a small positive integer."""
    if value <= 0:
        raise ValueError("value must be positive")
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, math.isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        complement = value // divisor
        if complement != divisor:
            upper.append(complement)
    return lower + list(reversed(upper))


def fixed_divisor_gap_certificate(p: int, gap: int) -> GapCertificate | None:
    """Use divisors forced by x=(p+gap)/4 for a fixed gap.

    For p=24*t+1 and gap=4*j-1, every x=6*t+j is divisible by
    g=gcd(6,j). Each s|g^2 gives a Type II candidate d=s, while each
    s|g gives a Type I candidate d=s*x. This is a deliberately restricted
    family: it isolates congruence-only certificates without factoring x.
    """
    if p % 24 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    j = (gap + 1) // 4
    g = math.gcd(6, j)

    for divisor in positive_divisors(g * g):
        if divisor > x or (x + divisor) % gap:
            continue
        y = p * (x + divisor) // gap
        z = p * (x + x * x // divisor) // gap
        certificate = GapCertificate(p, "II", gap, x, divisor, y, z)
        if not verify_certificate(certificate):
            raise AssertionError("constructed fixed-divisor Type II certificate did not verify")
        return certificate

    for multiplier in positive_divisors(g):
        divisor = multiplier * x
        if (p * x + divisor) % gap:
            continue
        y = (p * x + divisor) // gap
        z = p * (x + p * x * x // divisor) // gap
        certificate = GapCertificate(p, "I", gap, x, divisor, y, z)
        if not verify_certificate(certificate):
            raise AssertionError("constructed fixed-divisor Type I certificate did not verify")
        return certificate
    return None


def fixed_divisor_gap_avoidance_modulus(gaps: list[int]) -> int:
    """Return a core progression avoiding every fixed-divisor gap template.

    The mathematical proof uses p == 1 modulo every listed gap. This helper
    validates gap syntax and returns the combined Dirichlet modulus.
    """
    modulus = 24
    for gap in gaps:
        if gap % 4 != 3 or gap < 3:
            raise ValueError("gaps must be positive and 3 modulo 4")
        modulus = math.lcm(modulus, gap)
    return modulus


def three_p_plus_one_descent_certificate(
    p: int, spf: list[int]
) -> GapCertificate | None:
    """Build a Type I certificate from a lift out of n=(3*p+1)/4.

    If the least prime q == 2 (mod 3) divides n, then n == 1 (mod 3)
    forces q^2 <= n. Put r=(n/q+1)/3. The marked source solution
    4/n = 1/n + 1/(q*r) + 1/(n*r) lifts by replacing 1/n with 1/(n*p).
    Its target first denominator q*r has Type I gap (4*q+1)/3.
    """
    if p % 24 != 1:
        return None
    n = (3 * p + 1) // 4
    value = n
    candidate_q: int | None = None
    while value > 1:
        prime = spf[value]
        if prime % 3 == 2:
            candidate_q = prime if candidate_q is None else min(candidate_q, prime)
        while value % prime == 0:
            value //= prime
    if candidate_q is None:
        return None
    if candidate_q * candidate_q > n:
        raise AssertionError("a 2 mod 3 factor of n == 1 mod 3 must occur below sqrt(n)")

    q = candidate_q
    quotient = n // q
    if n % q or (quotient + 1) % 3 or (4 * q + 1) % 3:
        raise AssertionError("three-p-plus-one descent congruences failed")
    r = (quotient + 1) // 3
    gap = (4 * q + 1) // 3
    certificate = type_i_normal_form_certificate(p, gap, r, 1)
    if certificate is None:
        raise AssertionError("constructed three-p-plus-one certificate did not verify")
    if certificate.x != q * r or certificate.divisor != q * r * r:
        raise AssertionError("three-p-plus-one certificate parameters did not reconstruct")
    return certificate


def external_source_descent_witness(
    p: int, spf: list[int], k: int | None = None
) -> ExternalSourceDescentWitness | None:
    """Construct a marked descent from n=(q*p+1)/(q+1), q=4*k-1.

    A permitted k divides (p-1)/4. If n has a divisor f=-1 modulo q,
    choose the smaller complementary such divisor and write
    n=f*(q*r-1). The explicit source solution

        4/n = 1/(k*n) + 1/(k*f*r) + 1/(k*n*r)

    lifts by replacing 1/(k*n) with 1/(k*n*p). The same data gives the
    external-source Type I certificate with (x,d)=(k*f*r, k*f*r^2).
    With k omitted, all divisors of (p-1)/4 are searched in increasing
    order; this is an adaptive family, not a coverage theorem.
    """
    if p % 24 != 1 or p >= len(spf):
        return None
    base = (p - 1) // 4
    if k is None:
        candidates = positive_divisors_from_spf(base, spf)
    elif k > 0 and base % k == 0:
        candidates = [k]
    else:
        return None

    for candidate_k in candidates:
        q = 4 * candidate_k - 1
        n = (q * p + 1) // (q + 1)
        if (q + 1) * n != q * p + 1 or not 2 <= n < p:
            raise AssertionError("external-source descent source denominator failed")
        for factor in positive_divisors_from_spf(n, spf):
            complement = n // factor
            if factor % q != q - 1 or factor > complement:
                continue
            if complement % q != q - 1 or (complement + 1) % q:
                raise AssertionError("external-source descent factor residue failed")
            r = (complement + 1) // q
            x = candidate_k * factor * r
            gap = 4 * x - p
            divisor = candidate_k * factor * r * r
            certificate = type_i_normal_form_certificate(p, gap, r, 1)
            if certificate is None:
                raise AssertionError("external-source descent certificate did not verify")
            if (
                certificate.x != x
                or certificate.divisor != divisor
                or gap != (4 * candidate_k * factor + 1) // q
            ):
                raise AssertionError("external-source descent parameters did not reconstruct")

            source_solution = (
                candidate_k * n,
                x,
                candidate_k * n * r,
            )
            target_solution = (
                candidate_k * n * p,
                x,
                candidate_k * n * r,
            )
            if (
                Fraction(4, n)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("external-source descent identities did not verify")
            return ExternalSourceDescentWitness(
                p,
                n,
                candidate_k,
                q,
                factor,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def mixed_factor_external_source_descent_witness(
    p: int, spf: list[int], k: int | None = None
) -> ExternalSourceDescentWitness | None:
    """Construct a mixed-factor strict lift from ``n=(q*p+1)/(q+1)``.

    Let ``q=4*k-1`` and let ``g`` be a divisor of ``k*n`` that is at
    most ``n`` and is ``-1`` modulo ``q``.  The usual external-source
    descent restricts ``g`` to a divisor of ``n``.  Allowing the factors
    contributed by ``k`` gives the explicit source solution

        4/n = 1/(k*n) + 1/u + 1/v,
        u = k*(n+g)/q,  v = n*u/g,

    and replacing ``1/(k*n)`` by ``1/(k*n*p)`` lifts it to ``4/p``.
    The target has the Type I certificate
    ``m=(4*k*g+1)/q, x=u, d=u^2/(k*g)``.  This is a strict extension of
    the earlier branch, not a claim that some admissible ``k,g`` exists
    for every core prime.
    """
    if p % 24 != 1 or p >= len(spf):
        return None
    base = (p - 1) // 4
    if k is None:
        candidates = positive_divisors_from_spf(base, spf)
    elif k > 0 and base % k == 0:
        candidates = [k]
    else:
        return None

    for candidate_k in candidates:
        q = 4 * candidate_k - 1
        n = (q * p + 1) // (q + 1)
        if (q + 1) * n != q * p + 1 or not 2 <= n < p:
            raise AssertionError("mixed-factor source denominator failed")
        for g in positive_divisors_product_from_spf(candidate_k, n, spf):
            if g > n or g % q != q - 1:
                continue
            e = candidate_k * g
            companion = (candidate_k * n) ** 2 // e
            if (candidate_k * n + e) % q or (candidate_k * n + companion) % q:
                raise AssertionError("mixed-factor unit-fraction divisors failed")
            u = (candidate_k * n + e) // q
            v = (candidate_k * n + companion) // q
            if u > v or v != n * u // g:
                raise AssertionError("mixed-factor source ordering failed")

            gap = (4 * candidate_k * g + 1) // q
            if 4 * u - p != gap or not 3 <= gap <= p - 2:
                raise AssertionError("mixed-factor gap failed its natural range")
            if u * u % e:
                raise AssertionError("mixed-factor Type I divisor is not integral")
            divisor = u * u // e
            certificate = GapCertificate(p, "I", gap, u, divisor, v, candidate_k * n * p)
            if not verify_certificate(certificate):
                raise AssertionError("mixed-factor Type I certificate did not verify")

            source_solution = (candidate_k * n, u, v)
            target_solution = (candidate_k * n * p, u, v)
            if (
                Fraction(4, n)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("mixed-factor descent identities did not verify")
            return ExternalSourceDescentWitness(
                p,
                n,
                candidate_k,
                q,
                g,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def quadratic_factor_external_source_descent_witness(
    p: int, spf: list[int], k: int | None = None
) -> ExternalSourceDescentWitness | None:
    """Construct the complete two-term-tail lift for one external source.

    With ``q=4*k-1``, ``n=(q*p+1)/(q+1)``, and ``M=k*n``, every ordered
    two-unit-fraction tail of ``q/M`` is parametrized by a divisor
    ``e | M^2`` with ``e <= M`` and ``e == -M (mod q)``.  It yields

        4/n = 1/M + 1/u + 1/v,
        u=(M+e)/q, v=M*u/e,

    and changing only ``1/M`` to ``1/(M*p)`` gives a strict lift to ``4/p``.
    The target certificate is Type I with
    ``m=(4*e+1)/q, x=u, d=u^2/e``.  This is an exact parametrization for
    the fixed source and preserved denominator, but does not select a
    successful ``k,e`` for every core prime.
    """
    if p % 24 != 1 or p >= len(spf):
        return None
    base = (p - 1) // 4
    if k is None:
        candidates = positive_divisors_from_spf(base, spf)
    elif k > 0 and base % k == 0:
        candidates = [k]
    else:
        return None

    for candidate_k in candidates:
        q = 4 * candidate_k - 1
        n = (q * p + 1) // (q + 1)
        if (q + 1) * n != q * p + 1 or not 2 <= n < p:
            raise AssertionError("quadratic-factor source denominator failed")
        preserved = candidate_k * n
        for factor in positive_divisors_square_product_from_spf(
            candidate_k, n, spf
        ):
            if factor > preserved or factor % q != (-preserved) % q:
                continue
            companion = preserved * preserved // factor
            if (preserved + factor) % q or (preserved + companion) % q:
                raise AssertionError("quadratic-factor unit-fraction divisors failed")
            u = (preserved + factor) // q
            v = (preserved + companion) // q
            if u > v or v != preserved * u // factor:
                raise AssertionError("quadratic-factor source ordering failed")

            gap = (4 * factor + 1) // q
            if 4 * u - p != gap or not 3 <= gap <= p - 2:
                raise AssertionError("quadratic-factor gap failed its natural range")
            if u * u % factor:
                raise AssertionError("quadratic-factor Type I divisor is not integral")
            divisor = u * u // factor
            certificate = GapCertificate(
                p, "I", gap, u, divisor, v, preserved * p
            )
            if not verify_certificate(certificate):
                raise AssertionError("quadratic-factor Type I certificate did not verify")

            source_solution = (preserved, u, v)
            target_solution = (preserved * p, u, v)
            if (
                Fraction(4, n)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("quadratic-factor descent identities did not verify")
            return ExternalSourceDescentWitness(
                p,
                n,
                candidate_k,
                q,
                factor,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def shifted_quadratic_factor_external_source_descent_witness(
    p: int, k: int, shift: int, spf: list[int]
) -> ExternalSourceDescentWitness | None:
    """Construct a shifted Type I lift from a complete two-term source tail.

    Let ``q=4*k-1`` and ``n=(q*p+shift)/(q+1)``.  The retained source
    denominator is ``M=k*n`` and its replacement is ``M*p/shift``.  Write
    ``q=shift*t``, ``n=shift*N``, and ``M=shift*L``.  The required divisor
    has the unique form ``e=shift*f``.  The second tail congruence forces
    ``f | L^2``, so the complete search normalizes exactly to the two-term
    tail ``t/L``.  For ``shift=1`` this is the quadratic-factor
    external-source family; it also contains the older shifted branch as
    its e=k*f subfamily.
    """
    if (
        p % 24 != 1
        or k <= 0
        or shift <= 0
        or shift >= p
        or (p - shift) % (4 * k)
        or p >= len(spf)
    ):
        return None
    q = 4 * k - 1
    if q % shift:
        return None
    n = (q * p + shift) // (q + 1)
    if (q + 1) * n != q * p + shift or not 2 <= n < p:
        raise AssertionError("shifted quadratic-factor source denominator failed")
    preserved = k * n
    if n % shift:
        raise AssertionError("compatible shifted source must contain the shift")
    tail_source = n // shift
    tail_preserved = k * tail_source
    if preserved != shift * tail_preserved:
        raise AssertionError("shifted tail normalization did not reconstruct")

    for tail_factor in positive_divisors_square_product_from_spf(k, tail_source, spf):
        factor = shift * tail_factor
        if factor > preserved or factor % shift or (preserved + factor) % q:
            continue
        companion = preserved * preserved // factor
        if (preserved + companion) % q:
            raise AssertionError("normalized first tail congruence must force its companion")
        normalized_gcd = math.gcd(tail_factor, tail_preserved)
        if (tail_factor // normalized_gcd + tail_preserved // normalized_gcd) % (q // shift):
            raise AssertionError("normalized tail did not yield an opposite divisor pair")
        u = (preserved + factor) // q
        v = (preserved + companion) // q
        if u > v or v != preserved * u // factor:
            raise AssertionError("shifted quadratic-factor source ordering failed")

        gap = (4 * factor + shift) // q
        if 4 * u - p != gap or not 3 <= gap <= p - 2:
            raise AssertionError("shifted quadratic-factor gap failed its natural range")
        if gap != (4 * tail_factor + 1) // (q // shift):
            raise AssertionError("shifted quadratic-factor normalized gap failed")
        if (shift * u * u) % factor:
            raise AssertionError("shifted quadratic-factor divisor is not integral")
        divisor = shift * u * u // factor
        certificate = GapCertificate(
            p, "I", gap, u, divisor, v, preserved * p // shift
        )
        if not verify_certificate(certificate):
            raise AssertionError("shifted quadratic-factor Type I certificate did not verify")

        source_solution = (preserved, u, v)
        target_solution = (preserved * p // shift, u, v)
        if (
            Fraction(4, n)
            != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, p)
            != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("shifted quadratic-factor descent identities did not verify")
        return ExternalSourceDescentWitness(
            p,
            n,
            k,
            q,
            factor,
            source_solution,
            target_solution,
            certificate,
        )
    return None


def even_source_distance_descent_witness(
    p: int, distance: int, spf: list[int]
) -> ExternalSourceDescentWitness | None:
    """Enumerate a complete shifted quadratic-factor fan from ``p-distance``.

    The distance must be positive and odd, so the smaller source denominator
    is even. For every divisor ``shift`` of ``p-distance``, write
    ``s=(p-distance)/shift``. The compatible rays are exactly
    ``s=1+distance*r`` with ``shift*r == -1 (mod 4)``. Put
    ``k=(shift*r+1)/4`` and ``M1=k*s``. Their complete two-term tail is
    equivalent to ``e1 | M1^2``, ``e1 <= M1``, and
    ``e1 == -M1 (mod r)``.

    The source and target triples are ``(shift*M1,u,v)`` and ``(p*M1,u,v)``.
    This returns an explicit marked strict lift from an even smaller source;
    it does not assert that any distance or factor works for every core
    prime. At distance one it is the p-minus-one fan.
    """
    if (
        p % 24 != 1
        or distance <= 0
        or distance % 2 != 1
        or distance >= p
        or p >= len(spf)
    ):
        return None

    source = p - distance
    for shift in positive_divisors_from_spf(source, spf):
        s = source // shift
        if s <= 1 or (s - 1) % distance:
            continue
        r = (s - 1) // distance
        if (shift * r + 1) % 4:
            continue
        k = (shift * r + 1) // 4
        if (
            r <= 0
            or r % 2 != 1
            or p != shift * s + distance
            or p != shift + 4 * k * distance
            or shift % 4 != 1
        ):
            raise AssertionError("even-source distance parameters failed")
        m1 = k * s
        if 4 * m1 != r * p + 1 or math.gcd(r, m1) != 1:
            raise AssertionError("even-source distance tail lost coprimality")

        for factor in positive_divisors_square_product_from_spf(k, s, spf):
            if factor > m1 or (m1 + factor) % r:
                continue
            companion = m1 * m1 // factor
            if (m1 + companion) % r:
                raise AssertionError("even-source complementary congruence failed")
            u = (m1 + factor) // r
            v = (m1 + companion) // r
            if u > v or v != m1 * u // factor:
                raise AssertionError("even-source source ordering failed")

            gap = (4 * factor + 1) // r
            if 4 * u - p != gap or not 3 <= gap <= p - 2:
                raise AssertionError("even-source gap failed")
            if u * u % factor:
                raise AssertionError("even-source Type I divisor is not integral")
            divisor = u * u // factor
            certificate = GapCertificate(p, "I", gap, u, divisor, v, p * m1)
            if not verify_certificate(certificate):
                raise AssertionError("even-source Type I certificate did not verify")

            source_solution = (shift * m1, u, v)
            target_solution = (p * m1, u, v)
            if (
                Fraction(4, source)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("even-source descent identities did not verify")
            return ExternalSourceDescentWitness(
                p,
                source,
                k,
                shift * r,
                shift * factor,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def p_minus_one_source_descent_witness(
    p: int, spf: list[int]
) -> ExternalSourceDescentWitness | None:
    """Compatibility entry point for the distance-one even-source fan."""
    return even_source_distance_descent_witness(p, 1, spf)


def scaled_source_descent_witness(
    p: int, a: int, b: int, shift: int, spf: list[int]
) -> ScaledSourceDescentWitness | None:
    """Construct a Type I lift with a scaled source denominator ``a*n/b``.

    The target replacement is ``a*n*p/(b*shift)``.  Its defining equality
    forces ``b*(p-shift)=4*a*(p-n)``.  For integral source denominators and
    prime p, the reduced ratio denominator can only be 1, 2, or 4; this
    routine accepts exactly those cases.  A factor of ``(a*n)^2`` satisfying
    both tail congruences produces the two preserved unit fractions.  The
    factor must be divisible by ``b*shift`` for the induced target solution
    to be a Type I certificate.
    """
    if (
        p % 24 != 1
        or a <= 0
        or b not in (1, 2, 4)
        or math.gcd(a, b) != 1
        or shift <= 0
        or shift >= p
        or p >= len(spf)
    ):
        return None
    numerator = b * (p - shift)
    denominator = 4 * a
    if numerator % denominator:
        return None
    distance = numerator // denominator
    n = p - distance
    if not 2 <= n < p or n % b:
        return None
    first = a * n // b
    if first % shift:
        return None
    q = 4 * a - b
    if q <= 0:
        return None
    tail_denominator = a * n

    for factor in positive_divisors_square_product_from_spf(a, n, spf):
        if (
            factor > tail_denominator
            or factor % (b * shift)
            or (tail_denominator + factor) % q
        ):
            continue
        companion = tail_denominator * tail_denominator // factor
        if (tail_denominator + companion) % q:
            continue
        u = (tail_denominator + factor) // q
        v = (tail_denominator + companion) // q
        if u > v or v != tail_denominator * u // factor:
            raise AssertionError("scaled-source tail ordering failed")

        gap = (4 * factor + b * shift) // q
        if 4 * u - p != gap or not 3 <= gap <= p - 2:
            continue
        if (b * shift * u * u) % factor:
            raise AssertionError("scaled-source Type I divisor is not integral")
        divisor = b * shift * u * u // factor
        certificate = GapCertificate(
            p, "I", gap, u, divisor, v, first * p // shift
        )
        if not verify_certificate(certificate):
            raise AssertionError("scaled-source Type I certificate did not verify")

        source_solution = (first, u, v)
        target_solution = (first * p // shift, u, v)
        if (
            Fraction(4, n)
            != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, p)
            != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("scaled-source descent identities did not verify")
        return ScaledSourceDescentWitness(
            p,
            n,
            a,
            b,
            shift,
            distance,
            q,
            factor,
            source_solution,
            target_solution,
            certificate,
        )
    return None


def even_split_descent_witness(
    p: int, n: int, spf: list[int]
) -> EvenSplitDescentWitness | None:
    """Lift a nonstandard split ``4/n = 1/(n/2) + 1/a + 1/b``.

    For even ``n``, all ordered splits of its residual ``2/n`` arise from
    an even divisor ``e <= n`` of ``n^2`` through
    ``a=(n+e)/2`` and ``b=(n+n^2/e)/2``.  This routine tests either tail
    denominator against the exact two-denominator lift criterion.  It keeps
    only ``p/2 < n < p`` so ``n/2`` is the target's natural first denominator
    and simultaneously returns a Type I/II certificate at gap ``2*n-p``.
    The e=n standard split is included in the search and normally rejected by
    the known obstruction; successful witnesses are genuinely nonstandard.
    """
    if (
        p % 24 != 1
        or n <= p // 2
        or n >= p
        or n % 2
        or n >= len(spf)
    ):
        return None
    gap = 2 * n - p
    if gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    first = n // 2
    for factor in divisors_of_square(n, spf):
        if factor > n or factor % 2:
            continue
        companion = n * n // factor
        if (n + factor) % 2 or (n + companion) % 2:
            continue
        a = (n + factor) // 2
        b = (n + companion) // 2
        if a > b:
            raise AssertionError("even-split source ordering failed")
        for replaced, preserved in ((a, b), (b, a)):
            lifted = two_denominator_lift_candidate(p, n, replaced)
            if lifted is None or lifted < first:
                continue
            certificate = certificate_at_gap(p, gap, spf)
            if certificate is None:
                raise AssertionError("even-split lift lacked its natural certificate")
            source_solution = (first, a, b)
            target_solution = (first, preserved, lifted)
            if (
                Fraction(4, n)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("even-split descent identities did not verify")
            return EvenSplitDescentWitness(
                p,
                n,
                factor,
                replaced,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def residual_split_descent_witness(
    p: int, n: int, r: int, spf: list[int]
) -> ResidualSplitDescentWitness | None:
    """Lift a complete two-term split after retaining ``n/r``.

    For ``r`` in ``{1, 2, 3}`` with ``r | n``, all source solutions of the
    form ``4/n = 1/(n/r) + 1/a + 1/b`` are parameterized by an ``e | n^2``:
    writing ``s=4-r``, one has
    ``a=(n+e)/s`` and ``b=(n+n^2/e)/s`` whenever both are integral.  This
    function checks each tail denominator against the exact one-coordinate
    lift criterion.  It retains only targets for which ``n/r`` is in the
    natural first-denominator range, so the returned target carries its
    recovered Type I/II certificate.
    """
    if (
        p % 24 != 1
        or r not in (1, 2, 3)
        or n <= 1
        or n >= p
        or n % r
        or n >= len(spf)
    ):
        return None
    first = n // r
    gap = 4 * first - p
    if gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    split_numerator = 4 - r
    for factor in divisors_of_square(n, spf):
        if factor > n:
            continue
        companion = n * n // factor
        if (n + factor) % split_numerator or (n + companion) % split_numerator:
            continue
        a = (n + factor) // split_numerator
        b = (n + companion) // split_numerator
        if a > b:
            raise AssertionError("residual-split source ordering failed")
        for replaced, preserved in ((a, b), (b, a)):
            lifted = two_denominator_lift_candidate(p, n, replaced)
            if lifted is None or preserved < first or lifted < first:
                continue
            certificate = certificate_at_gap(p, gap, spf)
            if certificate is None:
                raise AssertionError("residual-split lift lacked its natural certificate")
            source_solution = (first, a, b)
            target_solution = (first, preserved, lifted)
            if (
                Fraction(4, n)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, p)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("residual-split descent identities did not verify")
            return ResidualSplitDescentWitness(
                p,
                n,
                r,
                factor,
                replaced,
                source_solution,
                target_solution,
                certificate,
            )
    return None


def even_standard_two_tail_descent_witness(
    p: int, n: int, spf: list[int]
) -> EvenStandardTwoTailDescentWitness | None:
    """Lift the standard even source while retaining one large denominator.

    The source identity is ``4/n = 1/(n/2) + 1/n + 1/n``.  It retains one
    of its two ``n`` denominators and reassembles the other two terms into
    ``1/u + 1/v`` for the target.  Writing ``R=4*n-p`` and ``S=n*p``, every
    ordered target tail is represented exactly by ``e | S^2`` with
    ``R | S+e`` and ``R | S+S^2/e``.  Requiring ``p/2 < n < p`` makes this a
    strict descent from a universally explicit even source; the additional
    first-denominator test returns only witnesses that also reconstruct a
    natural Type I/II certificate.
    """
    if (
        p % 24 != 1
        or n <= p // 2
        or n >= p
        or n % 2
        or p >= len(spf)
    ):
        return None
    residual_numerator = 4 * n - p
    tail_denominator = n * p
    if math.gcd(residual_numerator, tail_denominator) != 1:
        raise AssertionError("even-standard tail numerator and denominator were not coprime")
    for factor in positive_divisors_square_product_from_spf(p, n, spf):
        if factor > tail_denominator or (tail_denominator + factor) % residual_numerator:
            continue
        tail = coprime_one_denominator_lift(p, n, factor)
        if tail is None:
            raise AssertionError("coprime even-standard tail did not reconstruct")
        u, v = tail
        if u > v:
            raise AssertionError("even-standard two-tail ordering failed")
        source_solution = (n // 2, n, n)
        target_solution = (n, u, v)
        if u < n:
            gap_from_factor = 4 * u - p
            factor_certificate = GapCertificate(
                p, "I", gap_from_factor, u, factor, n, v
            )
            if not verify_certificate(factor_certificate):
                raise AssertionError("even-standard factor did not give its Type I certificate")
        first = min(target_solution)
        gap = 4 * first - p
        if gap % 4 != 3 or not 3 <= gap <= p - 2:
            continue
        if 3 * gap <= p:
            raise AssertionError("a retained large even denominator gave a too-short gap")
        certificate = certificate_at_gap(p, gap, spf)
        if certificate is None:
            raise AssertionError("even-standard two-tail lift lacked its natural certificate")
        if (
            Fraction(4, n)
            != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, p)
            != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("even-standard two-tail descent identities did not verify")
        return EvenStandardTwoTailDescentWitness(
            p,
            n,
            factor,
            source_solution,
            target_solution,
            certificate,
        )
    return None


def three_divisible_standard_two_tail_descent_witness(
    p: int, n: int, spf: list[int]
) -> ThreeDivisibleStandardTwoTailDescentWitness | None:
    """Lift the standard ``3 | n`` source while retaining one large tail.

    The source identity is ``4/n = 1/(n/3) + 1/(2*n) + 1/(2*n)``.  Retain
    one denominator ``2*n`` and reassemble the other two terms.  With
    ``R=8*n-p`` and ``S=2*n*p``, the ordered target tails are exactly the
    factors ``e | S^2`` with ``R | S+e`` and ``R | S+S^2/e``.  Taking
    ``p/2 < n < p`` makes the source strictly smaller while the retained
    denominator exceeds ``p``; unlike the analogous even-source branch,
    this does not force the recovered gap above ``p/3``.
    """
    if (
        p % 24 != 1
        or n <= p // 2
        or n >= p
        or n % 3
        or p >= len(spf)
    ):
        return None
    residual_numerator = 8 * n - p
    tail_denominator = 2 * n * p
    if math.gcd(residual_numerator, tail_denominator) != 1:
        raise AssertionError(
            "three-divisible standard tail numerator and denominator were not coprime"
        )
    for factor in positive_divisors_square_factors_from_spf((2, p, n), spf):
        if factor > tail_denominator or (tail_denominator + factor) % residual_numerator:
            continue
        tail = coprime_one_denominator_lift(p, 2 * n, factor)
        if tail is None:
            raise AssertionError("coprime three-divisible tail did not reconstruct")
        u, v = tail
        if u > v:
            raise AssertionError("three-divisible standard two-tail ordering failed")
        source_solution = (n // 3, 2 * n, 2 * n)
        target_solution = (2 * n, u, v)
        if u < 2 * n:
            gap_from_factor = 4 * u - p
            factor_certificate = GapCertificate(
                p, "I", gap_from_factor, u, factor, 2 * n, v
            )
            if not verify_certificate(factor_certificate):
                raise AssertionError(
                    "three-divisible standard factor did not give its Type I certificate"
                )
        first = min(target_solution)
        gap = 4 * first - p
        if gap % 4 != 3 or not 3 <= gap <= p - 2:
            continue
        certificate = certificate_at_gap(p, gap, spf)
        if certificate is None:
            raise AssertionError("three-divisible standard two-tail lift lacked its certificate")
        if (
            Fraction(4, n)
            != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, p)
            != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("three-divisible standard two-tail descent identities did not verify")
        return ThreeDivisibleStandardTwoTailDescentWitness(
            p,
            n,
            factor,
            source_solution,
            target_solution,
            certificate,
        )
    return None


def standard_tail_descent_audit(limit: int) -> dict[str, object]:
    """Exhaustively audit the two standard large-tail descent families.

    For each core prime up to ``limit``, this checks every admissible even
    source and every admissible source divisible by three in ``(p/2, p)``.
    It is an exact finite audit: a miss means only that these two fixed source
    families fail, not that ``4/p`` lacks a solution.
    """
    if limit < 2:
        raise ValueError("limit must be at least 2")
    spf = smallest_prime_factors(limit + 1)
    core_primes = [prime for prime in primes_up_to(limit) if prime % 24 == 1]
    even_hits = 0
    three_hits = 0
    combined_hits = 0
    combined_misses: list[int] = []

    for prime in core_primes:
        even_witness = None
        first_even = prime // 2 + 1
        if first_even % 2:
            first_even += 1
        for source in range(first_even, prime, 2):
            even_witness = even_standard_two_tail_descent_witness(
                prime, source, spf
            )
            if even_witness is not None:
                break

        three_witness = None
        first_three = prime // 2 + 1
        first_three += (-first_three) % 3
        for source in range(first_three, prime, 3):
            three_witness = three_divisible_standard_two_tail_descent_witness(
                prime, source, spf
            )
            if three_witness is not None:
                break

        even_hits += even_witness is not None
        three_hits += three_witness is not None
        combined_hits += even_witness is not None or three_witness is not None
        if even_witness is None and three_witness is None:
            combined_misses.append(prime)

    return {
        "arithmetic": "exact integer arithmetic and fractions.Fraction",
        "scope_note": (
            "A finite audit of two standard-source descent families. "
            "A combined miss is not a counterexample to the Erdős--Straus conjecture."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes),
        "even_standard_hits": even_hits,
        "three_divisible_standard_hits": three_hits,
        "combined_hits": combined_hits,
        "combined_misses": combined_misses,
    }


def affine_standard_tail_type_i_witness(
    p: int, a: int, b: int, h: int, source_kind: str
) -> AffineStandardTailDescentWitness | None:
    """Construct a shared-scale Type I lift from a standard source.

    Put ``x=a*t``, retained target denominator ``y=b*t``, and ``d=h*t``.
    The Type I identities force

        p=(4*a*b*t-h)/(a+b),   m=(4*a*a*t+h)/(a+b).

    For ``source_kind='even'``, take the standard source at ``n=y`` and
    require it to be even with ``p/2<n<p``.  For ``'three'``, take the
    standard three-divisible source at ``n=y/2`` and require ``3 | n`` and
    ``p/2<n<p``.  The constructed target keeps ``y`` and reassembles the
    other two source terms.  This is a direct parameter ray, not a search
    over divisors of the target tail.
    """
    if (
        p % 24 != 1
        or a <= 0
        or b <= a
        or h <= 0
        or source_kind not in ("even", "three")
    ):
        return None
    scale_numerator = p * (a + b) + h
    scale_denominator = 4 * a * b
    if scale_numerator % scale_denominator:
        return None
    t = scale_numerator // scale_denominator
    if t <= 0 or (4 * a * a * t + h) % (a + b):
        return None
    gap = (4 * a * a * t + h) // (a + b)
    x = a * t
    retained = b * t
    divisor = h * t
    if (
        h * t == 0
        or x * x % divisor
        or 4 * x != p + gap
        or gap % 4 != 3
        or not 3 <= gap <= p - 2
    ):
        return None
    if source_kind == "even":
        n = retained
        if n % 2 or not p // 2 < n < p:
            return None
        source_solution = (n // 2, n, n)
    else:
        if retained % 2:
            return None
        n = retained // 2
        if n % 3 or not p // 2 < n < p:
            return None
        source_solution = (n // 3, retained, retained)

    numerator_y = p * x + divisor
    if numerator_y % gap:
        raise AssertionError("affine standard-tail Type I numerator was not integral")
    y = numerator_y // gap
    numerator_z = p * (x + p * x * x // divisor)
    if numerator_z % gap:
        raise AssertionError("affine standard-tail Type I tail was not integral")
    z = numerator_z // gap
    if y != retained:
        raise AssertionError("affine standard-tail retained denominator did not reconstruct")
    certificate = GapCertificate(p, "I", gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("affine standard-tail Type I certificate did not verify")
    target_solution = (retained, x, z)
    if min(target_solution) != x:
        raise AssertionError("affine standard-tail target first denominator changed")
    if (
        Fraction(4, n)
        != sum((Fraction(1, value) for value in source_solution), Fraction())
        or Fraction(4, p)
        != sum((Fraction(1, value) for value in target_solution), Fraction())
    ):
        raise AssertionError("affine standard-tail descent identities did not verify")
    return AffineStandardTailDescentWitness(
        p,
        source_kind,
        n,
        a,
        b,
        h,
        t,
        source_solution,
        target_solution,
        certificate,
    )


def shifted_external_source_descent_witness(
    p: int, k: int, shift: int, spf: list[int]
) -> ExternalSourceDescentWitness | None:
    """Build the shifted-d external-source descent for one (k, shift) pair.

    Put q=4*k-1 and n=(q*p+shift)/(q+1). The target replacement
    1/(k*n) -> 1/(k*n*p/shift) is integral exactly when shift divides
    k*n. A factorization n=f*(q*r-1) then supplies the marked source
    solution and a Type I certificate with normal form
    (shift*r, 1, k*f/shift).
    """
    if (
        p % 24 != 1
        or k <= 0
        or shift <= 0
        or shift >= p
        or (p - shift) % (4 * k)
        or p >= len(spf)
    ):
        return None
    q = 4 * k - 1
    n = (q * p + shift) // (q + 1)
    if (q + 1) * n != q * p + shift or not 2 <= n < p:
        raise AssertionError("shifted external-source source denominator failed")
    if (k * n) % shift:
        return None

    for factor in positive_divisors_from_spf(n, spf):
        complement = n // factor
        if complement % q != q - 1:
            continue
        if factor % q != (-shift) % q:
            raise AssertionError("shifted external-source factor residue failed")
        r = (complement + 1) // q
        if (k * factor) % shift:
            raise AssertionError("shifted external-source certificate divisor failed")
        x = k * factor * r
        gap = 4 * x - p
        divisor = shift * k * factor * r * r
        certificate = type_i_normal_form_certificate(p, gap, shift * r, 1)
        if certificate is None:
            raise AssertionError("shifted external-source certificate did not verify")
        if (
            certificate.x != x
            or certificate.divisor != divisor
            or gap != (4 * k * factor + shift) // q
        ):
            raise AssertionError("shifted external-source parameters did not reconstruct")

        source_solution = (k * n, x, k * n * r)
        target_solution = (k * n * p // shift, x, k * n * r)
        if (
            Fraction(4, n)
            != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, p)
            != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("shifted external-source identities did not verify")
        return ExternalSourceDescentWitness(
            p,
            n,
            k,
            q,
            factor,
            source_solution,
            target_solution,
            certificate,
        )
    return None


def shifted_external_polynomial_ray_parameters(
    shift: int, quotient: int, tail_index: int
) -> tuple[int, int, int, int, int] | None:
    """Generate a fixed-factor subray of the shifted external-source family.

    Write q=shift*quotient=4*k-1 and choose the source factor
    f=shift*(quotient-1), whose complement is q*tail_index-1. The
    source-to-target identity then determines p polynomially. The returned
    tuple is (p, k, n, f, gap); primality is deliberately left to the caller.
    """
    if (
        shift <= 0
        or quotient < 2
        or tail_index <= 0
        or (shift * quotient) % 4 != 3
    ):
        return None
    k = (shift * quotient + 1) // 4
    factor = shift * (quotient - 1)
    n = factor * (shift * quotient * tail_index - 1)
    prime = (
        shift * shift * quotient * quotient * tail_index
        - shift * (shift - 1) * quotient * tail_index
        - shift * tail_index
        - shift * quotient
        + shift
        - 1
    )
    gap = factor + 1
    if (
        prime <= shift
        or n < 2
        or prime - n != shift * tail_index * (quotient - 1) - 1
        or (prime - shift) % (4 * k)
        or (4 * k - 1) * prime + shift != 4 * k * n
    ):
        raise AssertionError("shifted external polynomial ray parameters failed")
    return prime, k, n, factor, gap


def p_plus_four_type_ii_certificate(p: int, spf: list[int]) -> GapCertificate | None:
    """Use the least 3 (mod 4) prime factor of p+4 as a Type II gap."""
    if p % 24 != 1:
        return None
    value = p + 4
    candidate_gap: int | None = None
    while value > 1:
        prime = spf[value]
        if prime % 4 == 3:
            candidate_gap = prime if candidate_gap is None else min(candidate_gap, prime)
        while value % prime == 0:
            value //= prime
    if candidate_gap is None:
        return None
    if candidate_gap * candidate_gap > p + 4:
        raise AssertionError("a 3 mod 4 factor of p+4 == 1 mod 4 must occur below sqrt(p+4)")
    x = (p + candidate_gap) // 4
    y = p * (x + 1) // candidate_gap
    z = p * x * (x + 1) // candidate_gap
    certificate = GapCertificate(p, "II", candidate_gap, x, 1, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed p+4 certificate did not verify")
    return certificate


def p_plus_eight_type_ii_certificate(
    p: int, spf: list[int]
) -> GapCertificate | None:
    """Use a 7 (mod 8) divisor of p+8 on the (A,C)=(1,2) Type II ray.

    If h=8*k-1 divides p+8, then h divides k*p+1.  The raw ray
    constructor therefore has A=1, C=2, K=k.  Composite h is allowed:
    the ray identity, rather than primality, is the certificate condition.
    """
    if p % 24 != 1 or p + 8 >= len(spf):
        return None
    for factor in positive_divisors_from_spf(p + 8, spf):
        if factor % 8 != 7:
            continue
        certificate = type_ii_raw_ray_certificate(p, 1, 2, (factor + 1) // 8)
        if certificate is None:
            raise AssertionError("constructed p+8 Type II certificate did not verify")
        return certificate
    return None


def four_p_plus_one_type_ii_certificate(p: int, q: int) -> GapCertificate | None:
    """Construct a Type II certificate from q == 3 (mod 4) dividing 4p+1.

    For a core prime, choosing the least such prime q ensures the resulting
    gap is in Bradford's natural range. Primality of q is only needed for
    that range argument, not for the algebraic construction below.
    """
    if p % 24 != 1 or q < 3 or q % 4 != 3 or (4 * p + 1) % q:
        return None
    h = (q + 1) // 4
    gap = (p + 4 * h * h) // q
    if q * gap != p + 4 * h * h or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap:
        return None

    # x=h(gap-h); the complementary divisors share residue -x modulo gap.
    divisor = min(h * h, (gap - h) * (gap - h))
    y = p * (x + divisor) // gap
    z = p * (x + x * x // divisor) // gap
    certificate = GapCertificate(p, "II", gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed 4p+1 certificate did not verify")
    return certificate


def external_source_type_i_certificate(p: int, source: int, gap: int) -> GapCertificate | None:
    """Construct a Type I certificate from a Ventas external-source witness.

    The witness conditions are gap | p+source, gap == 3 (mod 4), and
    4*source | p+gap. The final range condition makes gap a Bradford gap.
    """
    if (
        p % 4 != 1
        or source <= 0
        or gap % 4 != 3
        or not 3 <= gap <= p - 2
        or (p + source) % gap
        or (p + gap) % (4 * source)
    ):
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap or x % source:
        return None
    divisor = source * x
    y = x * (p + source) // gap
    z = p * x * (p + source) // (source * gap)
    certificate = GapCertificate(p, "I", gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed external-source certificate did not verify")
    return certificate


def type_i_normal_form(p: int, gap: int, divisor: int) -> tuple[int, int, int] | None:
    """Normalize a Type I divisor as x=A*B*C, divisor=A^2*C.

    This is the coprime-factor form underlying the standard four-parameter
    Type I parametrization. It returns None unless divisor is a Type I
    certificate at the specified gap.
    """
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap or divisor <= 0 or x * x % divisor or (p * x + divisor) % gap:
        return None
    common = math.gcd(divisor, x)
    a = divisor // common
    b = x // common
    if math.gcd(a, b) != 1 or common % a:
        raise AssertionError("Type I divisor failed its coprime-factor normalization")
    c = common // a
    if x != a * b * c or divisor != a * a * c:
        raise AssertionError("Type I divisor normalization did not reconstruct")
    return a, b, c


def target_divisor_overflow_factor(x: int, target_divisor: int) -> int:
    """Return the prime-power overflow of ``target_divisor`` beyond ``x``.

    The input must be a positive divisor of x^2. Its quotient by gcd(e,x)
    is the B parameter in the associated Type I normal form.
    """
    if x <= 0 or target_divisor <= 0 or x * x % target_divisor:
        raise ValueError("target divisor must be a positive divisor of x^2")
    return target_divisor // math.gcd(target_divisor, x)


def type_i_normal_form_certificate(p: int, gap: int, a: int, b: int) -> GapCertificate | None:
    """Build a Type I certificate from x=A*B*C and m | B*p+A."""
    if (
        p % 4 != 1
        or gap % 4 != 3
        or not 3 <= gap <= p - 2
        or a <= 0
        or b <= 0
        or math.gcd(a, b) != 1
    ):
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap or x % (a * b) or (b * p + a) % gap:
        return None
    c = x // (a * b)
    divisor = a * a * c
    y = (p * x + divisor) // gap
    z = p * (x + p * x * x // divisor) // gap
    certificate = GapCertificate(p, "I", gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed normal-form Type I certificate did not verify")
    return certificate


def type_i_normal_form_from_target_divisor(
    p: int, gap: int, target_divisor: int
) -> tuple[int, int, int] | None:
    """Normalize a target-residue divisor ``e`` of ``x^2`` for Type I.

    Type I residue certificates use e=x^2/d with e == -1/4 (mod gap).
    In the resulting normal form x=A*B*C, this complementary divisor is
    exactly e=B^2*C. Thus B is the prime-power overflow of e beyond x.
    """
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if (
        4 * x != p + gap
        or target_divisor <= 0
        or x * x % target_divisor
        or target_divisor % gap != (-pow(4, -1, gap)) % gap
    ):
        return None
    common = math.gcd(target_divisor, x)
    a = x // common
    b = target_divisor_overflow_factor(x, target_divisor)
    if common % b:
        raise AssertionError("target divisor overflow did not divide its overlap")
    c = common // b
    normal_form = (a, b, c)
    certificate = type_i_normal_form_certificate(p, gap, a, b)
    if certificate is None:
        raise AssertionError("target divisor did not produce a Type I normal form")
    if target_divisor != b * b * c:
        raise AssertionError("target divisor did not reconstruct as B^2*C")
    return normal_form


def type_i_normal_tail_deflation_witness(
    p: int, gap: int, a: int, b: int
) -> TypeINormalTailDeflationWitness | None:
    """Deflate the p-divisible Type I tail when its normal form permits it.

    Put x=A*B*C and R=(4*B^2*C+1)/m. The Type I target has third
    denominator p*u, where u=B*C*(A*R-B). It reads as a strict one-tail
    lift exactly when R+1 divides 4*u; then n=4*u/(R+1) and the source
    solution is (x,y,u). Every quantity is determined by the Type I normal
    form, so this does not search backwards from a target solution. When it
    succeeds it is the certificate-side parametrization of the existing
    complete quadratic external-source descent family, not a new family.
    """
    certificate = type_i_normal_form_certificate(p, gap, a, b)
    if certificate is None:
        return None
    x = certificate.x
    c = x // (a * b)
    numerator = 4 * b * b * c + 1
    if numerator % gap:
        raise AssertionError("normal-form Type I congruence did not reconstruct")
    quotient = numerator // gap
    u = b * c * (a * quotient - b)
    if u <= 0 or certificate.z != p * u:
        raise AssertionError("normal-form Type I tail did not reconstruct")
    if (4 * u) % (quotient + 1):
        return None
    source_denominator = 4 * u // (quotient + 1)
    if not 2 <= source_denominator < p:
        raise AssertionError("normal-form tail deflation was not strict")
    source_solution = (certificate.x, certificate.y, u)
    target_solution = (certificate.x, certificate.y, certificate.z)
    if (
        Fraction(4, source_denominator)
        != sum((Fraction(1, value) for value in source_solution), Fraction())
        or Fraction(4, p)
        != sum((Fraction(1, value) for value in target_solution), Fraction())
    ):
        raise AssertionError("normal-form tail deflation identities did not verify")
    return TypeINormalTailDeflationWitness(
        p,
        source_denominator,
        a,
        b,
        c,
        quotient,
        source_solution,
        target_solution,
        certificate,
    )


def three_p_plus_four_internal_type_i_certificate(
    p: int, spf: list[int]
) -> GapCertificate | None:
    """Use the internal Type I slice (A,B)=(4,3) of 3*p+4.

    A divisor m of 3*p+4 with m == -p (mod 48) makes
    x=(p+m)/4=12*C and d=(p+m)/3=16*C.  Thus the Type I normal form
    has (A,B,C)=(4,3,(p+m)/48).  Unlike an external source, B is three.
    All qualifying divisors are considered because a composite divisor can
    be the first witness (for example p=1297, m=95).
    """
    value = 3 * p + 4
    if p % 24 != 1 or value >= len(spf):
        return None
    target = (-p) % 48
    for gap in positive_divisors_from_spf(value, spf):
        if gap % 48 != target:
            continue
        certificate = type_i_normal_form_certificate(p, gap, 4, 3)
        if certificate is None:
            raise AssertionError("constructed (A,B)=(4,3) certificate did not verify")
        return certificate
    return None


def three_p_plus_power_two_internal_type_i_certificate(
    p: int, a: int, spf: list[int]
) -> GapCertificate | None:
    """Use the Type I normal-form ray (A,B)=(a,3), a a power of two.

    For a=2^k at least four, a divisor m of 3*p+a with
    m == -p (mod 12*a) gives C=(p+m)/(12*a), x=3*a*C and d=a^2*C.
    The companion theorem proves that every such gap is natural.  The a=4
    case is the separately named ``three_p_plus_four`` internal branch.
    """
    value = 3 * p + a
    if (
        p % 24 != 1
        or a < 4
        or a & (a - 1)
        or value >= len(spf)
    ):
        return None
    modulus = 12 * a
    target = (-p) % modulus
    for gap in positive_divisors_from_spf(value, spf):
        if gap % modulus != target:
            continue
        certificate = type_i_normal_form_certificate(p, gap, a, 3)
        if certificate is None:
            raise AssertionError("constructed power-of-two (A,3) certificate did not verify")
        return certificate
    return None


def wide_internal_type_i_factor_ray_certificate(
    p: int, a: int, b: int, spf: list[int]
) -> GapCertificate | None:
    """Use the broad internal Type I ray ``(A,B)=(a,b)``.

    The proved range criterion is deliberately part of the API: ``a`` is a
    multiple of four, ``b`` is odd and at least three, ``gcd(a,b)=1``, and
    ``a > 2*b``.  For p > a+2*b+2, a divisor m of b*p+a in the class
    -p modulo 4*a*b has cofactor at least a-b>b.  It consequently gives a
    natural-gap Type I certificate with normal form
    (a,b,(p+m)/(4*a*b)).
    """
    value = b * p + a
    if (
        p % 24 != 1
        or a < 4
        or a % 4
        or b < 3
        or b % 2 == 0
        or math.gcd(a, b) != 1
        or a <= 2 * b
        or p <= a + 2 * b + 2
        or value >= len(spf)
    ):
        return None
    modulus = 4 * a * b
    target = (-p) % modulus
    for gap in positive_divisors_from_spf(value, spf):
        if gap % modulus != target:
            continue
        cofactor = value // gap
        if cofactor < a - b:
            raise AssertionError("broad internal ray cofactor bound failed")
        certificate = type_i_normal_form_certificate(p, gap, a, b)
        if certificate is None:
            raise AssertionError("constructed broad internal Type I certificate did not verify")
        return certificate
    return None


def fixed_gap_type_ii_factor_certificate(
    p: int, gap: int, spf: list[int]
) -> GapCertificate | None:
    """Use an A=1 Type II certificate from a -1 (mod gap) factor of x.

    Here ``gap`` must be a prime that is 3 modulo four.  If B divides
    x=(p+gap)/4 and B=-1 modulo gap, then the Type II normal form
    (A,B,C)=(1,B,x/B) has divisor C and gap | A+B.  The divisor B is
    intentionally variable; this is not a fixed-divisor gap template.
    """
    if (
        p % 24 != 1
        or gap < 3
        or gap % 4 != 3
        or gap > p - 2
    ):
        return None
    for divisor in range(2, math.isqrt(gap) + 1):
        if gap % divisor == 0:
            return None
    x = (p + gap) // 4
    if 4 * x != p + gap or x >= len(spf):
        return None
    for factor in positive_divisors_from_spf(x, spf):
        if factor % gap != gap - 1:
            continue
        certificate = type_ii_normal_form_certificate(p, gap, 1, factor)
        if certificate is None:
            raise AssertionError("constructed fixed-gap A=1 Type II certificate did not verify")
        return certificate
    return None


def type_ii_normal_form(p: int, gap: int, divisor: int) -> tuple[int, int, int] | None:
    """Normalize a Type II divisor as x=A*B*C, divisor=A^2*C.

    The extra Type II conditions become A <= B and gap | A+B.  This is
    the Type II counterpart to ``type_i_normal_form`` and returns None
    unless divisor is a Type II certificate at the specified gap.
    """
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return None
    x = (p + gap) // 4
    if (
        4 * x != p + gap
        or divisor <= 0
        or divisor > x
        or x * x % divisor
        or (x + divisor) % gap
    ):
        return None
    common = math.gcd(divisor, x)
    a = divisor // common
    b = x // common
    if math.gcd(a, b) != 1 or common % a:
        raise AssertionError("Type II divisor failed its coprime-factor normalization")
    c = common // a
    if x != a * b * c or divisor != a * a * c:
        raise AssertionError("Type II divisor normalization did not reconstruct")
    if a > b or (a + b) % gap:
        raise AssertionError("Type II divisor failed its normalized conditions")
    return a, b, c


def type_ii_normal_form_certificate(p: int, gap: int, a: int, b: int) -> GapCertificate | None:
    """Build a Type II certificate from x=A*B*C and gap | A+B."""
    if (
        p % 4 != 1
        or gap % 4 != 3
        or not 3 <= gap <= p - 2
        or a <= 0
        or b <= 0
        or a > b
        or math.gcd(a, b) != 1
    ):
        return None
    x = (p + gap) // 4
    if 4 * x != p + gap or x % (a * b) or (a + b) % gap:
        return None
    c = x // (a * b)
    divisor = a * a * c
    y = p * (x + divisor) // gap
    z = p * (x + x * x // divisor) // gap
    certificate = GapCertificate(p, "II", gap, x, divisor, y, z)
    if not verify_certificate(certificate):
        raise AssertionError("constructed normal-form Type II certificate did not verify")
    return certificate


def type_ii_factor_certificate(p: int, a: int, c: int, k: int) -> GapCertificate | None:
    """Build Type II from (4*A*C*K-1) | (K*p+A).

    If q=4*A*C*K-1 divides K*p+A, its quotient is B. Subject only to
    gcd(A,B)=1 and A<=B, the induced gap (A+B)/K is automatically integral
    and lies in Bradford's natural range. This parametrizes every Type II
    certificate after K=(A+B)/gap is recovered from its normal form.
    """
    if p % 4 != 1 or a <= 0 or c <= 0 or k <= 0:
        return None
    factor = 4 * a * c * k - 1
    numerator = k * p + a
    if numerator % factor:
        return None
    b = numerator // factor
    if b <= 0 or a > b or math.gcd(a, b) != 1 or (a + b) % k:
        return None
    gap = (a + b) // k
    return type_ii_normal_form_certificate(p, gap, a, b)


def type_ii_raw_ray_certificate(
    p: int, a: int, c: int, k: int
) -> GapCertificate | None:
    """Build a Type II certificate from a possibly non-coprime ray witness.

    The normalized generator additionally requires gcd(A,B)=1 so that its
    parameters are unique. That condition is not needed for the direct
    certificate: if h=4*A*C*K-1 divides K*p+A, B=(K*p+A)/h, and A<=B,
    then x=A*B*C, d=A^2*C, and m=(A+B)/K satisfy the Type II conditions.
    Non-coprime inputs merely normalize to different (A,B,C) coordinates.
    """
    if p % 4 != 1 or a <= 0 or c <= 0 or k <= 0:
        return None
    factor = 4 * a * c * k - 1
    numerator = k * p + a
    if numerator % factor:
        return None
    b = numerator // factor
    if b <= 0 or a > b or (a + b) % k:
        return None
    gap = (a + b) // k
    x = a * b * c
    divisor = a * a * c
    if (p * (x + divisor)) % gap or (p * (x + x * x // divisor)) % gap:
        return None
    certificate = GapCertificate(
        p,
        "II",
        gap,
        x,
        divisor,
        p * (x + divisor) // gap,
        p * (x + x * x // divisor) // gap,
    )
    return certificate if verify_certificate(certificate) else None


def type_ii_factor_template_avoidance_modulus(
    templates: list[tuple[int, int, int]],
) -> int:
    """Return a core residue modulus avoiding every listed factor template.

    For (A,C,K), the factor generator requires 4*A*C*K-1 to divide K*p+A.
    Every p == 1 modulo the returned modulus avoids all of those divisibility
    conditions. Dirichlet's theorem then supplies infinitely many prime terms
    in that residue class; the arithmetic avoidance itself needs no primality.
    """
    modulus = 24
    for a, c, k in templates:
        if a <= 0 or c <= 0 or k <= 0:
            raise ValueError("Type II factor templates must be positive")
        factor = 4 * a * c * k - 1
        modulus = math.lcm(modulus, factor)
    return modulus


def two_denominator_lift_candidate(
    target_denominator: int, source_denominator: int, replaced_denominator: int
) -> int | None:
    """Replace one term while retaining two source denominators in a strict lift.

    If 4/source = 1/a + 1/b + 1/c, this returns a' precisely when
    4/target = 1/a' + 1/b + 1/c. The target must be strictly larger
    than the source, so it is suitable for descent experiments.
    """
    if (
        target_denominator <= source_denominator
        or source_denominator < 2
        or replaced_denominator <= 0
    ):
        return None
    numerator = source_denominator * target_denominator * replaced_denominator
    denominator = source_denominator * target_denominator - 4 * (
        target_denominator - source_denominator
    ) * replaced_denominator
    if denominator <= 0 or numerator % denominator:
        return None
    return numerator // denominator


def gap_three_two_denominator_lift_candidate(p: int, source_denominator: int) -> int | None:
    """Return the forced replacement denominator in the m=3 descent step.

    Put n=(p+3)/4. If a solution for 4/n retained its other two denominators
    when lifted to 4/p, replacing source_denominator would have to yield the
    returned value. For prime p == 1 (mod 24), the accompanying obstruction
    theorem proves this function always returns None; primality is deliberately
    not checked here so composite boundary cases remain auditable.
    """
    if p % 24 != 1 or source_denominator <= 0:
        return None
    n = (p + 3) // 4
    if 4 * n != p + 3:
        return None
    return two_denominator_lift_candidate(p, n, source_denominator)


def three_mod_four_standard_source_lift_candidate(
    p: int, source_denominator: int, replaced_denominator: int | None = None
) -> int | None:
    """Try either distinct coordinate of the standard n == 3 (mod 4) source.

    The source decomposition is
    4/n = 1/((n+1)/4) + 2/(n(n+1)/2).  With the default, the small
    denominator is replaced for backwards compatibility.  Supplying the
    repeated large denominator instead tests that distinct coordinate too.
    For a core target and n<p, neither replacement can be integral: the
    small-coordinate case is a coprimality obstruction, while the large
    coordinate makes the forced denominator nonpositive.
    """
    if (
        p % 24 != 1
        or source_denominator < 3
        or source_denominator >= p
        or source_denominator % 4 != 3
    ):
        return None
    small = (source_denominator + 1) // 4
    large = source_denominator * (source_denominator + 1) // 2
    if replaced_denominator is None:
        replaced_denominator = small
    if replaced_denominator not in (small, large):
        return None
    return two_denominator_lift_candidate(
        p, source_denominator, replaced_denominator
    )


def three_divisible_standard_source_lift_candidate(
    p: int, source_denominator: int, replaced_denominator: int
) -> int | None:
    """Try a one-term replacement from 4/n=1/(n/3)+2/(2n).

    For a core prime target, n<p and 3 | n, the associated obstruction
    theorem proves that neither distinct source coordinate can be replaced
    while retaining the other two terms.
    """
    if (
        p % 24 != 1
        or source_denominator < 3
        or source_denominator >= p
        or source_denominator % 3
        or replaced_denominator not in (source_denominator // 3, 2 * source_denominator)
    ):
        return None
    return two_denominator_lift_candidate(p, source_denominator, replaced_denominator)


def gap_three_fab_translation_product(p: int) -> int | None:
    """Return abk forced by a fab translation from n=(p+3)/4 to p.

    Proposition 20 can only move n to n+4*a*b*k. For the natural m=3
    candidate p=4*n-3, this is possible only when p-n is divisible by 4.
    The returned value is (p-n)/4; None records the parity obstruction.
    """
    if p % 24 != 1:
        return None
    n = (p + 3) // 4
    if 4 * n != p + 3 or (p - n) % 4:
        return None
    return (p - n) // 4


def one_denominator_lift(p: int, preserved_denominator: int, factor: int) -> tuple[int, int] | None:
    """Replace two terms while retaining one denominator in a lift to 4/p.

    Put R=4*c-p and S=p*c. A positive divisor e of S^2 gives
    1/u+1/v=R/S exactly when R divides both S+e and S+S^2/e. The caller may
    use (u, v, c) with any source solution that contains c.
    """
    if p <= 0 or preserved_denominator <= 0 or factor <= 0:
        return None
    remainder = 4 * preserved_denominator - p
    product = p * preserved_denominator
    if remainder <= 0 or product * product % factor:
        return None
    complement = product * product // factor
    if (product + factor) % remainder or (product + complement) % remainder:
        return None
    first = (product + factor) // remainder
    second = (product + complement) // remainder
    if first <= 0 or second <= 0:
        return None
    return tuple(sorted((first, second)))


def coprime_one_denominator_lift(
    p: int, preserved_denominator: int, factor: int
) -> tuple[int, int] | None:
    """Use the reduced factor test when the residual numerator is coprime.

    Put R=4*c-p and S=p*c. If gcd(R,S)=1, then an e dividing S^2 and
    satisfying e=-S modulo R automatically makes S^2/e=-S modulo R.
    """
    if p <= 0 or preserved_denominator <= 0 or factor <= 0:
        return None
    remainder = 4 * preserved_denominator - p
    product = p * preserved_denominator
    if (
        remainder <= 0
        or math.gcd(remainder, product) != 1
        or product * product % factor
        or (product + factor) % remainder
    ):
        return None
    complement = product * product // factor
    if (product + complement) % remainder:
        raise AssertionError("coprime one-denominator complement congruence failed")
    first = (product + factor) // remainder
    second = (product + complement) // remainder
    if first <= 0 or second <= 0:
        return None
    return tuple(sorted((first, second)))


def gap_three_criterion(p: int, spf: list[int]) -> bool:
    """Whether m=3 works for a core prime, by its exact factor criterion.

    For p == 1 (mod 24), x=(p+3)/4 is 1 modulo 3. The two Bradford
    congruences at m=3 both require a divisor of x^2 that is 2 modulo 3,
    which exists exactly when x has a prime factor that is 2 modulo 3.
    """
    if p % 24 != 1:
        return False
    value = (p + 3) // 4
    if 4 * value != p + 3:
        return False
    while value > 1:
        prime = spf[value]
        if prime % 3 == 2:
            return True
        while value % prime == 0:
            value //= prime
    return False


def shortest_gap_certificate(p: int, gap_limit: int, spf: list[int]) -> GapCertificate | None:
    """Search 3, 7, ... in order, up to both gap_limit and the natural range."""
    for gap in range(3, min(gap_limit, p - 2) + 1, 4):
        certificate = certificate_at_gap(p, gap, spf)
        if certificate is not None:
            return certificate
    return None


def run_experiment(limit: int, gap_limit: int) -> dict[str, object]:
    if limit < 2 or gap_limit < 3:
        raise ValueError("limit must be at least 2 and gap_limit must be at least 3")
    max_x = (limit + min(limit - 2, gap_limit)) // 4 + 1
    spf = smallest_prime_factors(max_x)
    core_primes = [p for p in primes_up_to(limit) if p % 24 == 1]
    found: list[GapCertificate] = []
    missing: list[int] = []
    record_holders: list[dict[str, int | str]] = []
    largest_gap = -1
    by_type = {"I": 0, "II": 0}

    for p in core_primes:
        certificate = shortest_gap_certificate(p, gap_limit, spf)
        if certificate is None:
            missing.append(p)
            continue
        found.append(certificate)
        by_type[certificate.certificate_type] += 1
        if certificate.gap > largest_gap:
            largest_gap = certificate.gap
            record_holders.append(
                {
                    "prime": p,
                    "gap": certificate.gap,
                    "type": certificate.certificate_type,
                    "x": certificate.x,
                    "divisor": certificate.divisor,
                }
            )

    return {
        "arithmetic": "exact integer arithmetic and fractions.Fraction",
        "scope_note": "A finite small-gap search. Absence below the chosen gap limit is not a counterexample to the conjecture.",
        "prime_limit": limit,
        "gap_limit": gap_limit,
        "core_prime_count": len(core_primes),
        "certified_count": len(found),
        "uncertified_within_gap_limit": missing,
        "certificate_types": by_type,
        "largest_minimal_gap_found": largest_gap if found else None,
        "record_holders": record_holders,
        "sample_certificates": [asdict(item) for item in found[:5]],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--gap-limit", type=int, default=4_095)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(args.limit, args.gap_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
