#!/usr/bin/env python3
"""Profile fixed universal p-1 B=1 rays on the frozen 600M tail pressure set.

For p=24t+1, each E in the fixed menu below divides (p-1)^2/4=144t^2.
The p-1 source-state criterion therefore reduces every menu entry to one
divisor-residue search in K=((E-1)p+1)/4.  The script joins these rays with
the explicit p+1 factor bridge and records the first branch in a fixed order.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
DENSE = ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-fixed-pminusone-ray-pressure-profile-600m-results.json"

# These are exactly the positive divisors of 144 that are divisible by four.
UNIVERSAL_E_VALUES = (4, 8, 12, 16, 24, 36, 48, 72, 144)
UNIVERSAL_R_VALUES = tuple(E - 1 for E in UNIVERSAL_E_VALUES)


def divisors(value: int) -> list[int]:
    """Return the positive divisors of value in deterministic increasing order."""
    values = [1]
    for prime, exponent in sympy.factorint(value).items():
        values = [entry * int(prime) ** power for entry in values for power in range(int(exponent) + 1)]
    return sorted(values)


def validate_target_and_source(
    prime: int,
    A: int,
    C: int,
    H: int,
    K: int,
    E: int,
    source: int,
) -> int:
    """Check both exact unit-fraction identities and return the source tail."""
    source_term, remainder = divmod(source * K, E)
    if remainder:
        raise AssertionError("selected bridge has a nonintegral source tail")
    if Fraction(4, prime) != Fraction(1, A * C) + Fraction(1, A * C * H) + Fraction(1, prime * K):
        raise AssertionError("Type I target identity did not reconstruct")
    if Fraction(4, source) != Fraction(1, source_term) + Fraction(1, A * C) + Fraction(1, A * C * H):
        raise AssertionError("reverse bridge source identity did not reconstruct")
    return source_term


def p_plus_one_witness(prime: int) -> dict[str, int] | None:
    """Return the least q=3 mod 4 p+1 factor bridge, if present."""
    if prime % 24 != 1:
        raise AssertionError("pressure input contains a non-core prime")
    for q in sorted(sympy.factorint((prime + 1) // 2)):
        q = int(q)
        if q % 4 != 3:
            continue
        h = (prime + 1) // q
        C = (prime + q) // 4
        R = h + 1
        K = C * h
        E = h * h
        source = (q - 1) * h
        if (
            h % 4 != 2
            or q * R != 4 * C + 1
            or 4 * K != prime * R + 1
            or (4 * K - E) % R
            or (4 * K - E) // R != source
            or (4 * K * K) % E
            or E % R != 1
            or E % 2
            or E >= 2 * K
            or not ((prime + 1) // 2 < source < prime)
        ):
            raise AssertionError("p+1 factor did not reconstruct its stated upper bridge")
        source_term = validate_target_and_source(prime, 1, C, h, K, E, source)
        return {
            "q": q,
            "h": h,
            "A": 1,
            "B": 1,
            "C": C,
            "H": h,
            "m": q,
            "R": R,
            "K": K,
            "E": E,
            "source_denominator": source,
            "source_term": source_term,
        }
    return None


def fixed_pminusone_witness(prime: int, R: int) -> dict[str, int] | None:
    """Return the least divisor-residue witness for one fixed p-1 ray."""
    if prime % 24 != 1 or R not in UNIVERSAL_R_VALUES:
        raise AssertionError("invalid core prime or fixed ray")
    E = R + 1
    if ((prime - 1) * (prime - 1) // 4) % E:
        raise AssertionError("universal E did not divide the p-1 square state")
    K, remainder = divmod(prime * R + 1, 4)
    if remainder:
        raise AssertionError("K was not integral")
    target = -pow(4, -1, R) % R
    for C in divisors(K):
        if C % R != target:
            continue
        H, remainder = divmod(K, C)
        if remainder or (H + 1) % R or (4 * C + 1) % R:
            raise AssertionError("fixed ray divisor did not satisfy the complementary residues")
        A = (H + 1) // R
        m = (4 * C + 1) // R
        source = prime - 1
        if (
            A <= 0
            or m < 3
            or m % 4 != 3
            or prime != 4 * A * C - m
            or (4 * K - E) % R
            or (4 * K - E) // R != source
            or (4 * K * K) % E
            or E % R != 1
            or E % 2
            or E > 4 * K - 2 * R
            or not ((prime + 1) // 2 <= source < prime)
        ):
            raise AssertionError("fixed p-1 ray did not reconstruct an upper B=1 bridge")
        source_term = validate_target_and_source(prime, A, C, H, K, E, source)
        return {
            "A": A,
            "B": 1,
            "C": C,
            "H": H,
            "m": m,
            "R": R,
            "K": K,
            "E": E,
            "source_denominator": source,
            "source_term": source_term,
        }
    return None


def pressure_primes(tail: dict[str, object], dense: dict[str, object]) -> list[int]:
    """Recover the frozen 1,717 + 247 ordinary Type II tail-miss pressure set."""
    early_records = tail["records"]
    early_misses = tail["misses"]
    late_records = dense["records"]
    if not isinstance(early_records, list) or not isinstance(early_misses, list) or not isinstance(late_records, list):
        raise TypeError("pressure artifacts have an invalid record collection")
    early = {int(row["prime"]) for row in early_records} | {int(prime) for prime in early_misses}
    late = {int(row["prime"]) for row in late_records}
    if len(early) != int(tail["ordinary_tail_miss_count"]) or len(late) != int(dense["tail_miss_count"]):
        raise AssertionError("input artifacts do not reconstruct their stored ordinary-tail counts")
    if early & late or len(early) != 1717 or len(late) != 247:
        raise AssertionError("the frozen pressure ranges no longer have the expected disjoint partition")
    primes = sorted(early | late)
    if len(primes) != 1964:
        raise AssertionError("pressure set does not have 1,964 targets")
    return primes


def run_audit(tail_path: Path = TAIL, dense_path: Path = DENSE) -> dict[str, object]:
    """Join the p+1 bridge and fixed p-1 rays on the frozen pressure set."""
    tail = json.loads(tail_path.read_text(encoding="utf-8"))
    dense = json.loads(dense_path.read_text(encoding="utf-8"))
    primes = pressure_primes(tail, dense)

    p_plus_one = {prime: witness for prime in primes if (witness := p_plus_one_witness(prime)) is not None}
    fixed_rays = {
        R: {prime: witness for prime in primes if (witness := fixed_pminusone_witness(prime, R)) is not None}
        for R in UNIVERSAL_R_VALUES
    }

    records: list[dict[str, object]] = []
    unresolved: list[int] = []
    branch_counts: Counter[str] = Counter()
    for prime in primes:
        if prime in p_plus_one:
            branch = "p_plus_one_factor"
            witness = p_plus_one[prime]
        else:
            branch = ""
            witness = None
            for R in UNIVERSAL_R_VALUES:
                if prime in fixed_rays[R]:
                    branch = f"pminusone_R_{R}"
                    witness = fixed_rays[R][prime]
                    break
            if witness is None:
                unresolved.append(prime)
                continue
        branch_counts[branch] += 1
        records.append({"prime": prime, "branch": branch, "witness": witness})

    if len(records) + len(unresolved) != len(primes):
        raise AssertionError("branch choices do not partition the pressure set")
    branch_order = ["p_plus_one_factor", *(f"pminusone_R_{R}" for R in UNIVERSAL_R_VALUES)]
    return {
        "arithmetic": (
            "on the frozen ordinary Type II p-1-tail misses through 600M, first use the explicit p+1 "
            "q=3 mod 4 factor bridge, then test the p-1 B=1 divisor-residue criterion in the fixed "
            "universal E menu dividing 144"
        ),
        "scope_note": (
            "This is a finite decomposition of a frozen pressure set. A finite fixed ray menu is not a "
            "universal selector, and its unresolved list is not a list of Erdos--Straus counterexamples."
        ),
        "early_input": tail_path.name,
        "late_input": dense_path.name,
        "ordinary_tail_miss_count": len(primes),
        "universal_E_values": list(UNIVERSAL_E_VALUES),
        "universal_R_values": list(UNIVERSAL_R_VALUES),
        "p_plus_one_factor_coverage_count": len(p_plus_one),
        "fixed_ray_individual_coverage_counts": {str(R): len(fixed_rays[R]) for R in UNIVERSAL_R_VALUES},
        "p_plus_one_and_R_3_overlap_count": len(set(p_plus_one) & set(fixed_rays[3])),
        "branch_counts_in_priority_order": {
            branch: branch_counts[branch] for branch in branch_order if branch_counts[branch]
        },
        "covered_count": len(records),
        "unresolved_count": len(unresolved),
        "unresolved_primes": unresolved,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--dense", type=Path, default=DENSE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.tail, args.dense)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
