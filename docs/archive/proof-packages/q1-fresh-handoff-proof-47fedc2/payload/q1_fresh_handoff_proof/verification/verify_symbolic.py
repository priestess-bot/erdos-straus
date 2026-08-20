from __future__ import annotations

import json
import sympy as sp


def z(expr):
    out = sp.factor(sp.simplify(expr))
    if out != 0:
        raise AssertionError(f"symbolic identity failed: {out}")


def verify() -> dict[str, object]:
    t = sp.symbols("t", integer=True, positive=True)
    p = 24 * t + 1
    X = 6 * t + 1
    Rx = 16 * t + 3
    Kx = X * (16 * t + 1)
    M = 16 * t + 2

    # Root formulas and uniqueness congruence witness.
    z(4 * Kx - p * Rx - 1)
    z(3 * Rx - (8 * X + 1))
    z(p - (4 * X - 3))
    z(3 * M - 8 * X + 2)

    # Odd first child.
    Ro = 20 * t + 3
    Ko = (8 * t + 1) * (15 * t + 1)
    z(4 * Ko - p * Ro - 1)

    # Even first branch: transient overflow and fixed-n target.
    Rm = 52 * t + 7
    Km = (8 * t + 1) * (39 * t + 2)
    n = 12 * t + 1
    d = sp.Rational(9, 2) * t
    Re = 6 * t - 1
    Ke = d * (8 * t - 1)
    z(4 * Km - p * Rm - 1)
    z(n - (4 * M - Rm))
    z(p * n - 4 * M * d - 1)
    z(Re - (4 * d - n))
    z(4 * Ke - p * Re - 1)

    # Odd second anchor complete-excess closed formulas.
    Qo = 10 * t + 1
    Mo = 2 * (8 * t + 1) * Qo
    B = 144 * t**2
    z(Mo - (160 * t**2 + 36 * t + 2))
    assert sp.expand(Mo - B) == 16 * t**2 + 36 * t + 2
    z((Ro - 1) - 2 * Qo)
    z((Ro - 4 * (16 * t + 2)) - (-44 * t - 5))
    z((Ro + 4 * (16 * t + 2)) - (84 * t + 11))

    # General fixed-n quotient-fold identity.
    P, N, L, H, D = sp.symbols("P N L H D", integer=True)
    # Assume PN = 4L(PH+D)+1.
    NT = N - 4 * L * H
    RT = 4 * L - NT
    KT = L * (P - D)
    relation = {P * N: 4 * L * (P * H + D) + 1}
    expr1 = sp.expand(P * NT - 4 * L * D - 1).subs(relation)
    expr2 = sp.expand(P * RT + 1 - 4 * KT).subs(relation)
    z(expr1)
    z(expr2)

    # Odd p-free-gate algebra.
    j, delta = sp.symbols("j delta", integer=True)
    Lodd = (5 * P + 7) / 6
    delta_j = (j * P - 3) / 14
    Nodd = sp.simplify((4 * Lodd * delta_j + 1) / P)
    z(21 * Nodd - (5 * j * P + 7 * j - 15))

    # Even p-free-gate algebra.
    q = sp.symbols("q", integer=True, positive=True)
    delta_e = (j * P + 4) / (3 * q)
    # 4L = 3q(P-1)/4
    Le = 3 * q * (P - 1) / 16
    Ne = sp.simplify((4 * Le * delta_e + 1) / P)
    z(4 * Ne - (j * P + 4 - j))

    # Even regeneration rigid row identities.
    # If n=5p-4, a=(p+1)/2, b=(5p-3)/2.
    a = (P + 1) / 2
    b = (5 * P - 3) / 2
    E = (P - 1) * b - a
    z(E - (5 * P**2 - 9 * P + 2) / 2)
    z((E - 1) - P * (5 * P - 9) / 2)

    return {
        "status": "verified",
        "checks": [
            "full-carrier root identities",
            "root uniqueness congruence witness",
            "odd first-child identity",
            "even overflow/fixed-n identity",
            "odd second-anchor formulas",
            "general fixed-n quotient-fold identity",
            "odd/even p-free gate closed forms",
            "even regeneration multiplier identity",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
