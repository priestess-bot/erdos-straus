from __future__ import annotations

import json
from math import gcd

from common import first_child, is_prime, q_one_g, root_chart, universal_source


CONTROLS = {
    73: {"root": (51, 931), "child": ("marked_absorb", 63, 1150, 50)},
    241: {"root": (163, 9821), "child": ("fixed_n_edge", 59, 3555, 45)},
    2521: {"root": (1683, 1060711), "child": ("marked_absorb", 2103, 1325416, 1682)},
    118801: {"root": (79203, 2352348901), "child": ("fixed_n_edge", 29699, 882067725, 22275)},
    76129: {"root": (50755, 965981849), "child": ("fixed_n_edge", 19031, 362202750, 14274)},
}


def verify_one(p: int) -> dict[str, object]:
    if not q_one_g(p):
        raise AssertionError(f"control p={p} is not q=1 G")
    t, X, R, K = root_chart(p)
    if 4 * K != p * R + 1:
        raise AssertionError("root chart identity")
    if not (3 <= R <= p - 2 and K % X == 0):
        raise AssertionError("root chart low/full-carrier")

    # Exhaust the entire low interval to independently check uniqueness.
    matches = []
    for r in range(3, p - 1, 4):
        num = p * r + 1
        if num % 4:
            continue
        k = num // 4
        if k % X == 0:
            matches.append((r, k))
    if matches != [(R, K)]:
        raise AssertionError(f"full-carrier uniqueness failed at p={p}: {matches}")

    source, anchor = universal_source(p, R, K)
    child = first_child(p)
    expected = CONTROLS.get(p)
    if expected:
        if (R, K) != expected["root"]:
            raise AssertionError(f"root control changed at {p}")
        ec = expected["child"]
        if (child["kind"], child["R"], child["K"], child["A"]) != ec:
            raise AssertionError(f"child control changed at {p}: {child}")

    return {
        "p": p,
        "t": t,
        "X": X,
        "root": [R, K],
        "source": list(source),
        "anchor": list(anchor),
        "first_child": child,
    }


def verify_scan(limit: int = 200_000) -> dict[str, int]:
    core = 0
    g_count = 0
    for p in range(73, limit + 1, 24):
        if not is_prime(p):
            continue
        core += 1
        if not q_one_g(p):
            continue
        g_count += 1
        t, X, R, K = root_chart(p)
        if 4 * K != p * R + 1 or not (3 <= R <= p - 2):
            raise AssertionError(f"root identity failed in scan p={p}")
        source, anchor = universal_source(p, R, K)
        if anchor != (1, R - 1, 1):
            raise AssertionError("source replay")
        if gcd(R - 1, K) != 1:
            raise AssertionError(f"first excess not full at p={p}")
        first_child(p)
    return {"limit": limit, "core_primes": core, "q_one_g_primes": g_count}


def verify() -> dict[str, object]:
    controls = {str(p): verify_one(p) for p in CONTROLS}
    scan = verify_scan()
    return {"status": "verified", "controls": controls, "finite_sanity_scan": scan}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
