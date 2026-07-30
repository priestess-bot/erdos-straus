#!/usr/bin/env python3
"""Audit uniform scaling lifts from the six lower-modulus F-box hits."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPAIR_INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-scaled-type-i-lift-results.json"
)
EXPECTED_REPAIR_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supported_rational(
    factorization: list[tuple[int, int]], exponents: tuple[int, ...]
) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for (prime, _nu), exponent in zip(factorization, exponents):
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    return numerator, denominator


def target_vectors(
    modulus: int, factorization: list[tuple[int, int]]
) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    ranges = [range(-nu, nu + 1) for _prime, nu in factorization]
    for exponents in product(*ranges):
        residue = 1 % modulus
        for (prime, _nu), exponent in zip(factorization, exponents):
            if exponent >= 0:
                residue = residue * pow(prime, exponent, modulus) % modulus
            else:
                residue = residue * pow(pow(prime, -1, modulus), -exponent, modulus) % modulus
        if residue == modulus - 1:
            result.append(tuple(int(value) for value in exponents))
    return result


def recover_scaled_normal_form(
    prime: int,
    scaling_factor: int,
    modulus: int,
    K: int,
    target_divisor: int,
) -> dict[str, object]:
    common = math.gcd(target_divisor, K)
    B = target_divisor // common
    C = common * common // target_divisor
    H = K // common
    if math.gcd(B, H) != 1:
        raise AssertionError("normal form did not separate the coprime endpoints")
    if (B + H) % modulus:
        raise AssertionError("target divisor did not recover an integral A")
    A = (B + H) // modulus
    if (4 * B * B * C + 1) % modulus:
        raise AssertionError("target divisor did not recover an integral gap")
    gap = (4 * B * B * C + 1) // modulus
    scaled_numerator = prime * scaling_factor
    if scaled_numerator != 4 * A * B * C - gap:
        raise AssertionError("scaled Type I numerator identity failed")
    if math.gcd(A, B) != 1:
        raise AssertionError("scaled Type I normal form is not coprime")
    if not (0 < gap < scaled_numerator):
        raise AssertionError("scaled Type I gap is outside the natural range")

    denominators = [A * B * C, A * C * H, scaled_numerator * K]
    if sum((Fraction(1, value) for value in denominators), Fraction()) != Fraction(
        4, scaled_numerator
    ):
        raise AssertionError("scaled Type I decomposition failed")

    if math.gcd(scaling_factor, B * C * H) != 1:
        raise AssertionError("the scaling factor unexpectedly meets K")
    removable_factor = math.gcd(scaling_factor, A)
    if removable_factor != math.gcd(scaling_factor, A * C):
        raise AssertionError("C unexpectedly changed the removable factor")
    if removable_factor != math.gcd(scaling_factor, gap):
        raise AssertionError("the gap has a different removable factor")
    if removable_factor != math.gcd(modulus * scaling_factor, target_divisor + K) // modulus:
        raise AssertionError("the target congruence has a different removable factor")
    if any(value % removable_factor for value in denominators):
        raise AssertionError("the claimed common scaling factor is not removable")
    reduced_denominators = [value // removable_factor for value in denominators]
    reduced_numerator = scaled_numerator // removable_factor
    reduced_scaling_factor = scaling_factor // removable_factor
    enlarged_modulus = removable_factor * modulus
    reduced_A = A // removable_factor
    if (B + H) % enlarged_modulus:
        raise AssertionError("partial reduction did not enlarge the target modulus")
    if gap % removable_factor:
        raise AssertionError("partial reduction did not divide the normal-form gap")
    reduced_gap = gap // removable_factor
    if reduced_numerator != 4 * reduced_A * B * C - reduced_gap:
        raise AssertionError("reduced Type I normal form failed")
    if sum(
        (Fraction(1, value) for value in reduced_denominators), Fraction()
    ) != Fraction(4, reduced_numerator):
        raise AssertionError("partial scaling reduction failed")

    lifts_to_prime = removable_factor == scaling_factor
    if lifts_to_prime:
        if reduced_numerator != prime:
            raise AssertionError("full scaling lift did not reach the original prime")
        if reduced_denominators[-1] != prime * K:
            raise AssertionError("full scaling lift has the wrong third denominator")

    return {
        "target_divisor": target_divisor,
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "scaled_gap": gap,
        "scaled_denominators": denominators,
        "AC": A * C,
        "removable_factor": removable_factor,
        "reduced_scaling_factor": reduced_scaling_factor,
        "enlarged_modulus": enlarged_modulus,
        "reduced_A": reduced_A,
        "reduced_gap": reduced_gap,
        "reduced_numerator": reduced_numerator,
        "reduced_denominators": reduced_denominators,
        "lifts_to_prime": lifts_to_prime,
    }


def run() -> dict[str, object]:
    repair_sha = sha256(REPAIR_INPUT)
    source_sha = sha256(SOURCE_INPUT)
    if repair_sha != EXPECTED_REPAIR_SHA256:
        raise AssertionError("the frozen repair input changed")
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")

    repair_payload = json.loads(REPAIR_INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(int(x) for x in row["witness_exponents"])): row
        for row in source_payload["records"]
        if row.get("witness_exponents") is not None
    }

    records: list[dict[str, object]] = []
    for repair_row in repair_payload["records"]:
        key = (
            int(repair_row["prime"]),
            int(repair_row["R"]),
            tuple(int(x) for x in repair_row["witness_exponents"]),
        )
        source_row = source_rows[key]
        factorization = [
            (int(prime), int(exponent))
            for prime, exponent in source_row["factorization"]
        ]
        K = math.prod(prime**exponent for prime, exponent in factorization)
        prime = int(repair_row["prime"])
        R = int(repair_row["R"])
        if 4 * K != prime * R + 1:
            raise AssertionError("factorization does not reconstruct K")

        for candidate in repair_row["candidates"]:
            if candidate["lower_modulus_classification"] != "F_box_hit":
                continue
            scaling_factor = int(candidate["gap"])
            modulus = int(candidate["balanced_t"])
            if R != scaling_factor * modulus:
                raise AssertionError("lower modulus does not factor R")
            if 4 * K != prime * scaling_factor * modulus + 1:
                raise AssertionError("scaled numerator identity failed")

            vectors = target_vectors(modulus, factorization)
            if len(vectors) != int(candidate["lower_modulus_target_count"]):
                raise AssertionError("target-vector count does not match the frozen profile")

            normal_forms: dict[int, dict[str, object]] = {}
            vector_buckets: dict[int, list[list[int]]] = {}
            for vector in vectors:
                numerator, denominator = supported_rational(factorization, vector)
                if K * numerator % denominator:
                    raise AssertionError("box vector did not produce a divisor of K squared")
                divisor = K * numerator // denominator
                complement = K * K // divisor
                target_divisor = min(divisor, complement)
                if target_divisor >= K:
                    raise AssertionError("nontrivial target pair did not have a smaller member")
                normal_forms.setdefault(
                    target_divisor,
                    recover_scaled_normal_form(
                        prime, scaling_factor, modulus, K, target_divisor
                    ),
                )
                vector_buckets.setdefault(target_divisor, []).append(list(vector))

            forms: list[dict[str, object]] = []
            for target_divisor in sorted(normal_forms):
                form = normal_forms[target_divisor]
                form["target_vectors"] = sorted(vector_buckets[target_divisor])
                forms.append(form)
            if any(len(form["target_vectors"]) != 2 for form in forms):
                raise AssertionError("target vectors did not form inverse pairs")

            records.append(
                {
                    "prime": prime,
                    "orientation": repair_row["orientation"],
                    "R": R,
                    "scaling_factor_m": scaling_factor,
                    "lower_modulus_t": modulus,
                    "K": K,
                    "factorization": [list(item) for item in factorization],
                    "target_vector_count": len(vectors),
                    "normal_form_count": len(forms),
                    "full_lift_count": sum(int(form["lifts_to_prime"]) for form in forms),
                    "strict_partial_reduction_count": sum(
                        int(1 < int(form["removable_factor"]) < scaling_factor)
                        for form in forms
                    ),
                    "no_reduction_count": sum(
                        int(int(form["removable_factor"]) == 1) for form in forms
                    ),
                    "normal_forms": forms,
                }
            )

    removable_histogram = Counter(
        int(form["removable_factor"])
        for row in records
        for form in row["normal_forms"]
    )
    return {
        "arithmetic": (
            "A lower F-box hit for R=m*t is a Type I normal form for the scaled "
            "numerator P=p*m. Its denominators ABC, ACH, and PK can all be divided "
            "by m exactly when m divides A (equivalently m divides AC). More generally "
            "c=gcd(m,A) is the largest removable factor: the same target divisor then "
            "lifts from modulus t to c*t and gives a Type I normal form for p*(m/c)."
        ),
        "scope_note": (
            "This is a complete audit of the six frozen lower-modulus F-box hits and "
            "all vectors in their original K-exponent boxes. A partial reduction to "
            "p*m/gcd(m,AC) does not by itself solve p or define a closed descent."
        ),
        "repair_input": REPAIR_INPUT.name,
        "repair_input_sha256": repair_sha,
        "source_input": SOURCE_INPUT.name,
        "source_input_sha256": source_sha,
        "lower_hit_count": len(records),
        "target_vector_count": sum(int(row["target_vector_count"]) for row in records),
        "normal_form_count": sum(int(row["normal_form_count"]) for row in records),
        "full_lift_count": sum(int(row["full_lift_count"]) for row in records),
        "strict_partial_reduction_count": sum(
            int(row["strict_partial_reduction_count"]) for row in records
        ),
        "no_reduction_count": sum(int(row["no_reduction_count"]) for row in records),
        "removable_factor_histogram": {
            str(key): value for key, value in sorted(removable_histogram.items())
        },
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "lower_hit_count",
                    "target_vector_count",
                    "normal_form_count",
                    "full_lift_count",
                    "strict_partial_reduction_count",
                    "no_reduction_count",
                    "removable_factor_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
