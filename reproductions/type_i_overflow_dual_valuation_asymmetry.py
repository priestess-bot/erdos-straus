#!/usr/bin/env python3
"""Check the weighted q-adic phase normal form for overflow dual channels.

For pn = 4*M*d + 1 and M = k*p + r, write

    L_d = k + 1,       L_r = d*n - 1,
    beta_t = v_q(L_t),  u_t = v_q(t),
    h_t = (a - u_t - beta_t)_+       (q**a || A).

After beta = min(beta_d, beta_r), the determinant identity gives the exact
weighted phase relation

    p*(q**(beta_d-beta)*eta_d - q**(beta_r-beta)*eta_r)
        == (2*p-r-d)/q**beta       (mod q**(a-beta)),

where eta_t = L_t/q**beta_t.  Unequal beta therefore forces a first-layer
split in the weighted phases, while equal beta recovers the usual gap test.
This is a focused arithmetic check, not a recursive-edge verifier.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reproductions" / "type-i-overflow-dual-valuation-asymmetry-results.json"


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def valuation(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise AssertionError("valuation requires a nonzero value")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return factors


def canonical_R(prime: int, support: int) -> int:
    modulus = 4 * support
    if support <= 0 or prime % support == 0:
        raise AssertionError("canonical chart needs coprime prime and support")
    result = (-pow(prime, -1, modulus)) % modulus
    if not 1 <= result < modulus or result % 4 != 3:
        raise AssertionError("canonical representative changed")
    return result


def check_row(prime: int, M: int, d: int, n: int, A: int, q: int) -> dict[str, int | str]:
    if prime % 24 != 1 or not is_prime(prime):
        raise AssertionError("core prime must be 1 modulo 24")
    if prime * n != 4 * M * d + 1:
        raise AssertionError("overflow identity failed")
    if M <= prime or M % prime == 0 or A <= 0 or M % A:
        raise AssertionError("invalid overflow support")
    if M % q:
        raise AssertionError("q must divide the old support")
    a = valuation(A, q)
    if q**a != A:
        raise AssertionError("focused rows use a single q-primary support")
    if prime == q:
        raise AssertionError("q cannot equal p")

    r = M % prime
    k = M // prime
    label_d = k + 1
    label_r = d * n - 1
    beta_d = valuation(label_d, q)
    beta_r = valuation(label_r, q)
    u_d = valuation(d, q)
    u_r = valuation(r, q)
    h_d = max(0, a - u_d - beta_d)
    h_r = max(0, a - u_r - beta_r)
    if not h_d or not h_r:
        raise AssertionError("both channels must have positive unpaid height")

    beta = min(beta_d, beta_r)
    gap = 2 * prime - r - d
    if gap % q**beta:
        raise AssertionError("the determinant gap is not divisible by q**beta")
    eta_d = label_d // q**beta_d
    eta_r = label_r // q**beta_r
    zeta_d = q ** (beta_d - beta) * eta_d
    zeta_r = q ** (beta_r - beta) * eta_r
    modulus = q ** (a - beta)
    if (prime * (zeta_d - zeta_r) - gap // q**beta) % modulus:
        raise AssertionError("weighted phase congruence failed")

    common_height = min(h_d, h_r)
    for level in range(common_height + 1):
        expected = (gap // q**beta) % q**level == 0
        actual = (zeta_d - zeta_r) % q**level == 0
        if expected != actual:
            raise AssertionError("weighted phase level test failed")

    weighted_depth = (
        common_height
        if zeta_d == zeta_r
        else min(common_height, valuation(zeta_d - zeta_r, q))
    )
    phase_cell_profile: list[int] = []
    for level in range(1, max(h_d, h_r) + 1):
        residues = set()
        if h_d >= level:
            residues.add(zeta_d % (q**level))
        if h_r >= level:
            residues.add(zeta_r % (q**level))
        expected_cells = 1 if level <= weighted_depth or level > common_height else 2
        if len(residues) != expected_cells:
            raise AssertionError("weighted phase-cell census changed")
        phase_cell_profile.append(len(residues))
    unequal = beta_d != beta_r
    if unequal:
        if gap == 0 or valuation(gap, q) != beta:
            raise AssertionError("unequal label valuations must expose the exact gap valuation")
        if (zeta_d - zeta_r) % q == 0:
            raise AssertionError("unequal label valuations must split at weighted level one")
        if weighted_depth != 0:
            raise AssertionError("unequal label valuations must have zero weighted prefix")
    else:
        gap_height = common_height if gap == 0 else max(0, valuation(gap, q) - beta)
        direct = 0
        while direct < common_height and (eta_d - eta_r) % (q ** (direct + 1)) == 0:
            direct += 1
        if direct != min(common_height, gap_height):
            raise AssertionError("equal label valuation gap depth changed")
        if weighted_depth != direct:
            raise AssertionError("weighted prefix did not recover equal-label depth")

    return {
        "p": prime,
        "M": M,
        "d": d,
        "n": n,
        "r": r,
        "A": A,
        "q": q,
        "a": a,
        "u_d": u_d,
        "beta_d": beta_d,
        "h_d": h_d,
        "u_r": u_r,
        "beta_r": beta_r,
        "h_r": h_r,
        "gap": gap,
        "gap_valuation": valuation(gap, q) if gap else -1,
        "weighted_common_depth": weighted_depth,
        "weighted_split_layers": common_height - weighted_depth,
        "weighted_phase_cell_profile": phase_cell_profile,
        "weighted_first_layer_split": int(unequal),
        "branch": "valuation_asymmetry" if unequal else "equal_label_gap",
    }


def explicit_rows() -> list[tuple[int, int, int, int, int, int]]:
    return [
        # Unequal beta: (p,M,d,n,r,k,q,a)=(73,675,1,37,18,9,5,2).
        (73, 675, 1, 37, 25, 5),
        # Equal beta, nontrivial 5-adic common prefix.
        (73, 75, 9, 37, 25, 5),
        # Equal beta with q dividing both carriers; odd-q first-layer split.
        (73, 225, 3, 37, 9, 3),
        # Equal beta at q=2 with carrier payments on both sides.
        (241, 568, 124, 1169, 8, 2),
    ]


def generated_rows(limit: int = 180) -> list[tuple[int, int, int, int, int, int]]:
    rows: list[tuple[int, int, int, int, int, int]] = []
    for prime in range(73, 500):
        if prime % 24 != 1 or not is_prime(prime):
            continue
        for n in range(1, 8 * prime + 1, 4):
            numerator = prime * n - 1
            if numerator % 4:
                continue
            base = numerator // 4
            for d in range(1, prime):
                if base % d:
                    continue
                M = base // d
                if M <= prime or M % prime == 0:
                    continue
                try:
                    R = canonical_R(prime, M)
                except AssertionError:
                    continue
                if R <= prime:
                    continue
                for q, exponent in factorization(M):
                    for a in range(1, exponent + 1):
                        A = q**a
                        if q == prime:
                            continue
                        beta_d = valuation(M // prime + 1, q)
                        beta_r = valuation(d * n - 1, q)
                        h_d = max(0, a - valuation(d, q) - beta_d)
                        h_r = max(0, a - valuation(M % prime, q) - beta_r)
                        if h_d and h_r and beta_d != beta_r:
                            rows.append((prime, M, d, n, A, q))
                        if len(rows) >= limit:
                            return rows
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    rows = explicit_rows() + generated_rows()
    records = [check_row(*row) for row in rows]
    unequal = sum(record["branch"] == "valuation_asymmetry" for record in records)
    equal = sum(record["branch"] == "equal_label_gap" for record in records)
    result = {
        "row_count": len(records),
        "unequal_valuation_rows": unequal,
        "equal_valuation_rows": equal,
        "weighted_first_layer_split_rows": sum(
            record["weighted_first_layer_split"] for record in records
        ),
        "weighted_split_layers": sum(record["weighted_split_layers"] for record in records),
        "scope_note": (
            "Exact local dual-channel phase identity. It does not construct a marked lift, "
            "a Type I/II certificate, or an E1--E5 recursive edge."
        ),
        "rows": records,
    }
    if args.verify:
        if len(records) < 50 or unequal == 0 or equal == 0:
            raise AssertionError("focused rows do not cover both phase branches")
        if unequal != sum(record["weighted_first_layer_split"] for record in records):
            raise AssertionError("every unequal-valuation row must split in weighted phase")
        for record in records:
            if record["branch"] == "valuation_asymmetry" and record["weighted_common_depth"] != 0:
                raise AssertionError("an unequal row retained a weighted common prefix")
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "row_count": result["row_count"],
                "unequal_valuation_rows": unequal,
                "equal_valuation_rows": equal,
                "weighted_first_layer_split_rows": result["weighted_first_layer_split_rows"],
                "weighted_split_layers": result["weighted_split_layers"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
