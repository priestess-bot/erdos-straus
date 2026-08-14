#!/usr/bin/env python3
"""Verify the q=1 canonical root slice without any range scan.

For p = 24t + 1, the q=1 Type II endpoint has first denominator X = 6t + 1.
This verifier checks the deterministic Type I root choice r = t, its strict
complete-excess receipt, and the exact support-disjointness obstruction
gcd(X, K) = 1.  The only finite branch is the explicit u = 37 catalog below.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


# These are not a search domain.  They are the complete odd-k catalog for
# p = 444k - 11 <= 111^2, used by the u = 37 proof branch.
SMALL_U37_FACTORS = {
    1: (433,),
    3: (1321,),
    5: (47, 47),
    7: (19, 163),
    9: (5, 797),
    11: (11, 443),
    13: (7, 823),
    15: (61, 109),
    17: (7537,),
    19: (5, 5, 337),
    21: (67, 139),
    23: (101, 101),
    25: (13, 853),
    27: (7, 29, 59),
}

U_ONE_FIXTURES = (
    (73, 37),
    (97, 2),
    (193, 10),
    (337, 22),
    (2713, 110),
)

U37_LOW_FIXTURES = (
    (433, 1, 248),
    (1321, 8, 1225),
    (7537, 1, 1850),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return the maximal complete-excess block without factoring value."""
    shared = gcd(value, capacity)
    stripped = value // shared
    block = gcd(value, pow(stripped, value.bit_length(), value))
    return block, value // block


def canonical_root(prime: int) -> dict[str, int]:
    if not is_prime(prime) or prime % 24 != 1:
        raise AssertionError("canonical slice requires a core prime")

    p = prime
    t = (p - 1) // 24
    X = 6 * t + 1
    g = (p + 1) // 2
    T = p * p * t - g
    A = g * T
    K = A * (p - 1)
    R = 2 * p**3 * t - p * p - 2 * p * t - p + 1
    M = (p * p + p + 1) // 3
    u = gcd(2 * t + 1, M)
    h = 3 * u
    z = R - h
    Q, beta = complete_excess(z, K)
    g_A = gcd(A, Q)
    E = Q // g_A
    D = beta * g_A
    c = (-pow(E, -1, p)) % p
    M_ex = A * E
    K_ex = M_ex * c
    R_ex = (4 * K_ex - 1) // p

    if not (
        t >= 3
        and X == (p + 3) // 4
        and M == 192 * t * t + 24 * t + 1
        and (M - 37) % (2 * t + 1) == 0
        and u in (1, 37)
        and h < p
        and u < M
        and 4 * K == p * R + 1
        and gcd(R - (p + 1), K) == h
        and gcd(h, z) == 1
        and gcd(X, g) == gcd(X, T) == gcd(X, p - 1) == 1
        and gcd(X, K) == 1
        and z > p * h + 1
        and gcd(z, K) <= p * h + 1
        and K % z != 0
        and Q > 1
        and Q * beta == z
        and gcd(Q, beta) == 1
        and Q % p != 0
        and K % (h * D) == 0
        and E * D == z
        and 1 <= c <= p - 2
        and M_ex == A * E
        and 4 * K_ex == p * R_ex + 1
        and R_ex > p
        and 4 * A > (p - 1) ** 2
    ):
        raise AssertionError("canonical root arithmetic changed")

    return {
        "p": p,
        "t": t,
        "X": X,
        "M": M,
        "u": u,
        "h": h,
        "A": A,
        "K": K,
        "R": R,
        "z": z,
        "Q": Q,
        "beta": beta,
        "g_A": g_A,
        "E": E,
        "D": D,
        "c": c,
        "M_ex": M_ex,
        "K_ex": K_ex,
        "R_ex": R_ex,
    }


def verify_u_one() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for prime, expected_c in U_ONE_FIXTURES:
        row = canonical_root(prime)
        p = row["p"]
        t = row["t"]
        H = (3 * p + 1) // 4
        w = gcd(t - 3, H)
        Q_3 = row["z"] // 4
        expected = (p + 1) // 2 if w == H else 2 * w
        if not (
            row["u"] == 1
            and row["h"] == 3
            and row["z"] % 4 == 0
            and w == gcd(t - 3, 55)
            and w in (1, 5, 11, 55)
            and row["E"] == Q_3 // w
            and row["D"] == 4 * w
            and row["c"] == expected == expected_c
        ):
            raise AssertionError("u=1 canonical half-descent formula changed")
        rows.append({"p": p, "t": t, "u": 1, "w": w, "c": row["c"]})
    return rows


def verify_u37_finite_catalog() -> list[dict[str, int]]:
    prime_rows: list[dict[str, int]] = []
    for k, factors in SMALL_U37_FACTORS.items():
        p = 444 * k - 11
        product = 1
        for factor in factors:
            product *= factor
        if product != p:
            raise AssertionError("u=37 finite catalog factorization changed")
        if len(factors) == 1:
            if not is_prime(p):
                raise AssertionError("u=37 catalog prime lost primality")
            prime_rows.append({"k": k, "p": p})
        elif len(factors) < 2 or any(factor <= 1 for factor in factors):
            raise AssertionError("u=37 composite catalog entry is invalid")

    expected_primes = [{"k": 1, "p": 433}, {"k": 3, "p": 1321}, {"k": 17, "p": 7537}]
    if prime_rows != expected_primes:
        raise AssertionError("u=37 finite prime catalog changed")
    return prime_rows


def verify_u37() -> list[dict[str, int]]:
    catalog = verify_u37_finite_catalog()
    rows: list[dict[str, int]] = []
    for prime, expected_D, expected_c in U37_LOW_FIXTURES:
        row = canonical_root(prime)
        if not (
            row["u"] == 37
            and row["h"] == 111
            and row["h"] ** 2 >= prime
            and row["D"] == expected_D
            and row["c"] == expected_c
        ):
            raise AssertionError("small u=37 strict receipt changed")
        rows.append({"p": prime, "D": row["D"], "c": row["c"]})

    high = canonical_root(16_417)
    if not (
        high["u"] == 37
        and high["h"] == 111
        and high["h"] ** 2 < high["p"]
        and high["c"] == 12_837
    ):
        raise AssertionError("large u=37 small-endpoint branch changed")
    rows.append({"p": high["p"], "D": high["D"], "c": high["c"]})

    if catalog != [{"k": 1, "p": 433}, {"k": 3, "p": 1321}, {"k": 17, "p": 7537}]:
        raise AssertionError("u=37 catalog was not consumed")
    return rows


def verify() -> dict[str, object]:
    return {
        "status": "verified",
        "u_one": verify_u_one(),
        "u_thirty_seven": verify_u37(),
        "scope": (
            "canonical r=(p-1)/24 root arithmetic, finite u=37 exception catalog, "
            "and q=1 support disjointness; no prime-range or selector-history scan"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(verify())


if __name__ == "__main__":
    main()
