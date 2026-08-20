from __future__ import annotations

from math import gcd, isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    # deterministic Miller-Rabin for 64-bit integers
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factorization(n: int) -> dict[int, int]:
    if n <= 0:
        raise ValueError("factorization expects positive n")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def q_one_g(prime: int) -> bool:
    if not (is_prime(prime) and prime % 24 == 1):
        return False
    X = (prime + 3) // 4
    return all(q % 3 == 1 for q in factorization(X))


def r_three_g(prime: int) -> bool:
    if not (is_prime(prime) and prime % 24 == 1):
        return False
    N = (3 * prime + 1) // 4
    return all(q % 3 == 1 for q in factorization(N))


def root_chart(prime: int) -> tuple[int, int, int, int]:
    if prime % 24 != 1:
        raise ValueError("core congruence required")
    t = (prime - 1) // 24
    X = (prime + 3) // 4
    R = 16 * t + 3
    K = X * (16 * t + 1)
    return t, X, R, K


def universal_source(prime: int, R: int, K: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    U = prime
    V = R * (prime - 1) - prime
    m = prime - 1
    if min(U, V, m) <= 0:
        raise AssertionError("nonpositive source")
    if U + V != R * m:
        raise AssertionError("source equation failed")
    if gcd(U, V) != 1:
        raise AssertionError("source not primitive")
    if K % prime == 0:
        raise AssertionError("p unexpectedly divides K")
    if (V + R) % prime or (m + 1) % prime:
        raise AssertionError("p-edge shift 1 not integral")
    target = (U // prime, (V + R) // prime, (m + 1) // prime)
    if target != (1, R - 1, 1):
        raise AssertionError("unexpected anchor")
    return (U, V, m), target


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    if gcd(prime, modulus) != 1:
        raise ValueError("prime/support not coprime enough for inverse")
    R = (-pow(prime, -1, modulus)) % modulus
    if R == 0:
        R = modulus
    Knum = prime * R + 1
    if Knum % 4:
        raise AssertionError("nonintegral K")
    K = Knum // 4
    if K % support:
        raise AssertionError("support does not divide K")
    return R, K


def complete_excess(anchor: int, capacity: int) -> tuple[int, int, list[tuple[int, int]]]:
    af = factorization(anchor)
    cf = factorization(capacity)
    Q = 1
    blocks: list[tuple[int, int]] = []
    for q, e in af.items():
        if e > cf.get(q, 0):
            Q *= q ** e
            blocks.append((q, e))
    if anchor % Q:
        raise AssertionError("Q does not divide anchor")
    return Q, anchor // Q, blocks


def first_child(prime: int) -> dict[str, int | str]:
    t, X, R, K = root_chart(prime)
    M = R - 1
    if gcd(M, K) != 1:
        raise AssertionError("root anchor should be full excess")
    if t % 2:
        Rt = 20 * t + 3
        Kt = (8 * t + 1) * (15 * t + 1)
        A = M
        kind = "marked_absorb"
    else:
        Rt = 6 * t - 1
        A = 9 * t // 2
        Kt = A * (8 * t - 1)
        kind = "fixed_n_edge"
    if prime * Rt + 1 != 4 * Kt or Kt % A:
        raise AssertionError("first child identity failed")
    if not (3 <= Rt <= prime - 2 and A > 1):
        raise AssertionError("first child not low/strict")
    return {"kind": kind, "R": Rt, "K": Kt, "A": A}
