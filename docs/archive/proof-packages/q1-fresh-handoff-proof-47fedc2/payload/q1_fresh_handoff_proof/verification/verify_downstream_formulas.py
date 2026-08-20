from __future__ import annotations

import json
from math import gcd, lcm

from common import canonical_chart, complete_excess, first_child, q_one_g


def second_anchor(p: int) -> dict[str, object]:
    if not q_one_g(p):
        raise AssertionError("q=1 G required")
    t = (p - 1) // 24
    child = first_child(p)
    R = int(child["R"])
    K = int(child["K"])
    A = int(child["A"])
    anchor = R - 1
    Q, beta, blocks = complete_excess(anchor, K)
    M = lcm(A, Q)
    Rm, Km = canonical_chart(p, M)
    Bp = (p - 1) ** 2 // 4
    if Rm <= p:
        raise AssertionError(f"second anchor unexpectedly low at p={p}")

    row: dict[str, object] = {
        "p": p,
        "t": t,
        "child": child,
        "anchor": anchor,
        "Q": Q,
        "beta": beta,
        "blocks": blocks,
        "M": M,
        "B_p": Bp,
        "overflow_chart": [Rm, Km],
    }

    n = 4 * M - Rm
    C = Km // M
    d = p - C
    if p * n != 4 * M * d + 1 or not (1 <= d < p):
        raise AssertionError("overflow determinant failed")

    if t % 2:
        L = 2 * (10 * t + 1)
        if not (L > A and M % L == 0 and L <= Bp):
            raise AssertionError("odd fixed-n carrier")
    else:
        s = t // 2
        qs = [q for q, _ in blocks if (6 * s - 1) % q == 0]
        if not qs:
            raise AssertionError("missing forced even excess prime")
        qstar = min(qs)
        L = 9 * s * qstar
        row["q_star"] = qstar
        if not (L > A and M % L == 0 and L <= Bp):
            raise AssertionError("even fixed-n carrier")

    quotient = M * d // L
    if M * d % L:
        raise AssertionError("L does not divide Md")
    h, delta = divmod(quotient, p)
    if delta == 0:
        raise AssertionError("delta zero")
    nT = n - 4 * L * h
    RT = 4 * L - nT
    KT = L * (p - delta)
    if p * nT != 4 * L * delta + 1 or p * RT + 1 != 4 * KT or KT % L:
        raise AssertionError("quotient fold target failed")
    if delta == 1:
        raise AssertionError("unit defect should be excluded in q=1 module")
    if Bp // L >= Bp // A:
        raise AssertionError("fixed-n outer rank not strict")

    row["fixed_n"] = {
        "n": n,
        "d": d,
        "L": L,
        "h": h,
        "delta": delta,
        "target": [RT, KT],
        "target_n": nT,
        "target_kind": "low" if RT < p else "high",
    }

    if RT > p:
        S = L * delta
        RU = (p - 1) * nT - 1
        KU = S * (p - 1)
        if p * RU + 1 != 4 * KU:
            raise AssertionError("full-product d=1 receiver identity")
        if Bp // S >= Bp // L:
            # If S>Bp, both may be zero; the upstream unbounded contract uses another component.
            if S <= Bp:
                raise AssertionError("full-product local rank not strict")
        row["d_one_receiver"] = {"A": S, "R": RU, "K": KU, "n": nT}
    return row


def verify_regeneration_control() -> dict[str, object]:
    # p=193 is the standard even q*=23 regeneration control.
    row = second_anchor(193)
    if row.get("q_star") != 23:
        raise AssertionError("p=193 should have q*=23")
    d1 = row.get("d_one_receiver")
    if not d1:
        raise AssertionError("p=193 should reach d=1 receiver")
    p = 193
    n = int(d1["n"])
    alpha = (p + 1) // 2
    v = (n + 1) // 2
    g = gcd(alpha, v)
    a, b = alpha // g, v // g
    E = (p - 1) * b - a
    return {
        "p": p,
        "q_star": 23,
        "n": n,
        "g": g,
        "E_mod_p": E % p,
        "regeneration": E % p == 1,
    }


def verify() -> dict[str, object]:
    # Controls used in upstream cards, covering odd/even and large values.
    controls = [73, 2521, 193, 241, 769, 118801]
    rows = []
    for p in controls:
        if q_one_g(p):
            rows.append(second_anchor(p))
    regen = verify_regeneration_control()
    if not regen["regeneration"]:
        raise AssertionError("p=193 regeneration control changed")
    return {"status": "verified", "second_anchor_controls": rows, "regeneration_control": regen}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
