#!/usr/bin/env python3
"""Audit odd-distance even-source lifts from the short-relation terminals."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from sympy import divisors, factorint


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-short-relation-even-terminal-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-short-relation-odd-distance-even-source-results.json"
EXPECTED_INPUT_SHA256 = "41bdb1c1c9c724731db27b81cbd1a8e6d9a7cc298028b16370338a75df01d368"
EXPECTED_RECORD_COUNT = 291


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def square_divisors(value: int) -> list[int]:
    factors = factorint(value)
    result = [1]
    for prime, exponent in factors.items():
        result = [item * prime**power for item in result for power in range(2 * exponent + 1)]
    return sorted(result)


def verify_parameter(prime: int, source: int, distance: int, d: int) -> dict[str, int] | None:
    if d <= 0 or source % d:
        return None
    scale = source // d
    if scale <= 1 or (scale - 1) % distance:
        return None
    r = (scale - 1) // distance
    if r <= 0 or (d * r + 1) % 4:
        return None
    k = (d * r + 1) // 4
    m1 = k * scale
    if 4 * m1 != r * prime + 1:
        raise AssertionError("odd-distance source identity did not reconstruct")
    return {"d": d, "s": scale, "r": r, "k": k, "M1": m1}


def verify_tail(
    prime: int,
    source: int,
    distance: int,
    parameter: dict[str, int],
    e1: int,
) -> dict[str, int] | None:
    m1 = parameter["M1"]
    r = parameter["r"]
    if e1 <= 0 or e1 > m1 or (m1 + e1) % r:
        return None
    if m1 * m1 % e1:
        raise AssertionError("tail factor did not divide M1^2")
    u = (m1 + e1) // r
    if m1 * u % e1:
        raise AssertionError("complementary tail was not integral")
    v = m1 * u // e1
    gap = (4 * e1 + 1) // r
    if 4 * u - prime != gap or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise AssertionError("recovered Type I gap was not natural")
    if u * u % e1:
        raise AssertionError("recovered Type I divisor was not integral")
    divisor = u * u // e1
    if (prime * u + divisor) % gap or prime % v == 0:
        raise AssertionError("recovered Type I congruence failed")
    source_solution = (parameter["d"] * m1, u, v)
    target_solution = (prime * m1, u, v)
    if Fraction(4, source) != sum((Fraction(1, x) for x in source_solution), Fraction()):
        raise AssertionError("source identity failed")
    if Fraction(4, prime) != sum((Fraction(1, x) for x in target_solution), Fraction()):
        raise AssertionError("target identity failed")
    return {
        "e1": e1,
        "u": u,
        "v": v,
        "gap": gap,
        "target_divisor": divisor,
        "source_first": parameter["d"] * m1,
        "target_third": prime * m1,
    }


def audit_record(index: int, record: dict[str, object]) -> tuple[list[dict[str, int]], list[dict[str, int]]]:
    prime = int(record["prime"])
    source = int(record["n"])
    distance = prime - source
    if distance <= 0 or distance % 2 == 0:
        return [], []
    parameters: list[dict[str, int]] = []
    hits: list[dict[str, int]] = []
    for d in divisors(source):
        parameter = verify_parameter(prime, source, distance, int(d))
        if parameter is None:
            continue
        parameter = {"record_index": index, "prime": prime, "source": source, "distance": distance, **parameter}
        tails = 0
        for e1 in square_divisors(parameter["M1"]):
            candidate = verify_tail(prime, source, distance, parameter, e1)
            if candidate is None:
                continue
            tails += 1
            hits.append({**parameter, **candidate})
        parameters.append({**parameter, "tail_candidate_count": tails})
    return parameters, hits


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the short-relation input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_RECORD_COUNT:
        raise AssertionError("unexpected short-relation record count")

    parameters: list[dict[str, int]] = []
    hits: list[dict[str, int]] = []
    for index, record in enumerate(records):
        local_parameters, local_hits = audit_record(index, record)
        parameters.extend(local_parameters)
        hits.extend(local_hits)

    parameter_distances = Counter(str(item["distance"]) for item in parameters)
    hit_primes = sorted({int(item["prime"]) for item in hits})
    return {
        "arithmetic": (
            "For every short-relation even terminal, set c=p-n and enumerate every d|n "
            "with n/d=1+c*r and d*r=-1 mod 4. For each parameter, enumerate all "
            "e1|M1^2 with e1<=M1 and e1=-M1 mod r, and verify the exact odd-distance "
            "even-source Type I lift."
        ),
        "scope_note": (
            "Finite audit of the odd-distance even-source branch on the 291 frozen "
            "short-relation terminals. A hit is a strict marked descent and a Type I "
            "certificate; misses do not rule out another distance, source family, or lift."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "record_count": len(records),
        "parameter_count": len(parameters),
        "parameter_state_count": len({int(item["record_index"]) for item in parameters}),
        "parameter_distance_histogram": dict(sorted(parameter_distances.items(), key=lambda item: int(item[0]))),
        "tail_candidate_count": len(hits),
        "hit_state_count": len({int(item["record_index"]) for item in hits}),
        "hit_prime_count": len(hit_primes),
        "hit_primes": hit_primes,
        "parameters": parameters,
        "hits": hits,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "record_count", "parameter_count", "parameter_state_count",
        "tail_candidate_count", "hit_state_count", "hit_prime_count", "hit_primes",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
