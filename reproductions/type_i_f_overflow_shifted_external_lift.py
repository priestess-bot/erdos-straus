#!/usr/bin/env python3
"""Search the shifted external-source lift family from square-terminal sources."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from sympy import divisors


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-shifted-external-lift-results.json"
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_parameter(
    prime: int,
    source: int,
    terminal_R: int,
    terminal_E: int,
    k: int,
    d: int,
    f: int,
) -> dict[str, int] | None:
    distance = prime - source
    q = 4 * k - 1
    if d <= 0 or d >= prime or d != prime - 4 * k * distance:
        return None
    if prime % (4 * k) != d % (4 * k) or (k * source) % d:
        return None
    if source % f:
        return None
    complementary = source // f
    if complementary <= 0 or complementary % q != q - 1:
        return None
    r = (complementary + 1) // q
    if r <= 0 or (k * f) % d:
        return None
    x = k * f * r
    m_numerator = 4 * k * f + d
    if m_numerator % q:
        return None
    m = m_numerator // q
    if not 3 <= m <= prime - 2 or 4 * x - prime != m:
        return None
    target_first = k * source * prime // d
    if d * target_first != k * source * prime:
        return None
    target_third = k * source * r
    source_solution = (k * source, x, target_third)
    target_solution = (target_first, x, target_third)
    if Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction()):
        raise AssertionError("shifted source identity failed")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction()):
        raise AssertionError("shifted target identity failed")
    certificate_divisor = d * k * f * r * r
    if x * x % certificate_divisor:
        raise AssertionError("shifted Type I divisor does not divide the target square")
    return {
        "prime": prime,
        "source": source,
        "distance": distance,
        "terminal_R": terminal_R,
        "terminal_E": terminal_E,
        "k": k,
        "d": d,
        "q": q,
        "f": f,
        "r": r,
        "x": x,
        "m": m,
        "D": certificate_divisor,
        "source_first": k * source,
        "target_first": target_first,
        "shared_second": x,
        "shared_third": target_third,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the square-terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = list(payload.get("candidates", []))
    if len(candidates) != 253:
        raise AssertionError(f"unexpected candidate count: {len(candidates)}")

    divisor_cache: dict[int, list[int]] = {}
    parameters: list[dict[str, int]] = []
    candidate_parameter_counts: Counter[int] = Counter()
    k_counts: Counter[int] = Counter()
    for index, candidate in enumerate(candidates, start=1):
        prime = int(candidate["prime"])
        source = int(candidate["source"])
        terminal_R = int(candidate["R"])
        terminal_E = int(candidate["E"])
        distance = prime - source
        if distance <= 0 or source % 2:
            raise AssertionError("invalid square-terminal source")
        if source not in divisor_cache:
            divisor_cache[source] = [int(value) for value in divisors(source)]
        local: list[dict[str, int]] = []
        max_k = prime // (4 * distance)
        for k in range(1, max_k + 1):
            q = 4 * k - 1
            d = prime - 4 * k * distance
            if d <= 0 or (k * source) % d:
                continue
            for f in divisor_cache[source]:
                parameter = verify_parameter(
                    prime, source, terminal_R, terminal_E, k, d, f
                )
                if parameter is None:
                    continue
                local.append(parameter)
                k_counts[k] += 1
            if local and len(local) > 1000:
                raise AssertionError("unexpectedly large local parameter family")
        parameters.extend(local)
        candidate_parameter_counts[index] = len(local)

    hit_primes = sorted({int(item["prime"]) for item in parameters})
    return {
        "arithmetic": (
            "For every deduplicated square-terminal source, enumerate every positive k with "
            "q=4k-1 and d=p-4k(p-n)>0, enforce d|kn, then enumerate all f|n with "
            "n/f=-1 mod q. Verify the complete shifted external-source identity and Type I "
            "certificate."
        ),
        "scope_note": (
            "Finite targeted audit of the shifted external-source family. It is complete in k "
            "and f for the 253 saved square-terminal sources, but a miss does not rule out "
            "other source families or a global selector."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_count": len(candidates),
        "k_loop_count": sum(
            int(candidate["prime"]) // (4 * (int(candidate["prime"]) - int(candidate["source"])))
            for candidate in candidates
        ),
        "parameter_count": len(parameters),
        "hit_count": len(parameters),
        "hit_prime_count": len(hit_primes),
        "hit_primes": hit_primes,
        "parameter_k_histogram": {
            str(k): int(count) for k, count in sorted(k_counts.items())
        },
        "candidate_parameter_counts": {
            str(index): int(count) for index, count in sorted(candidate_parameter_counts.items())
        },
        "parameters": parameters,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "candidate_count",
                    "k_loop_count",
                    "parameter_count",
                    "hit_prime_count",
                    "hit_primes",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
