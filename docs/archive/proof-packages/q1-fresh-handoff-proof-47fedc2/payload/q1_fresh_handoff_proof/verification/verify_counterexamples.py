from __future__ import annotations

import json
from math import gcd

from common import factorization, q_one_g, r_three_g


def old_root_support_disjoint(p: int) -> dict[str, int]:
    t = (p - 1) // 24
    X = (p + 3) // 4
    g = (p + 1) // 2
    T = p * p * t - g
    A = g * T
    K = A * (p - 1)
    if gcd(X, K) != 1:
        raise AssertionError("old canonical root support disjointness failed")
    return {"p": p, "X": X, "old_K": K, "gcd": gcd(X, K)}


def verify() -> dict[str, object]:
    # Strict double-G counterexample to q=1 G -> R=3 non-G.
    p = 241
    X = (p + 3) // 4
    N = (3 * p + 1) // 4
    if not (q_one_g(p) and r_three_g(p)):
        raise AssertionError("p=241 lost double-G status")
    if factorization(X) != {61: 1} or factorization(N) != {181: 1}:
        raise AssertionError("p=241 factorization control changed")

    # Stronger double-G control.
    p2 = 2521
    if not (q_one_g(p2) and r_three_g(p2)):
        raise AssertionError("p=2521 lost double-G status")

    old_controls = [old_root_support_disjoint(p) for p in (73, 241, 2521, 76129)]

    return {
        "status": "verified",
        "double_g_min_control": {
            "p": 241,
            "X": X,
            "N": N,
            "conclusion": "q=1 G does not force R=3 Type I non-G",
        },
        "double_g_stronger_control": {"p": p2},
        "old_root_support_disjointness": old_controls,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
