#!/usr/bin/env python3
"""Replay the exact high-anchor c=1 menu boundaries.

This is intentionally a three-example integer replay.  It does not import or
run the global selector.  It verifies:

* the divisor-label iff criterion for arithmetic h=0, c=1 returns;
* the singleton full-excess action of high_R_path_anchored_bundle_v1;
* why a partial bundle and the weaker H2 conditions must not be silently
  identified with that singleton action.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-high-anchor-direct-c1-finite-menu-exhaustion-results.json"
)
CLAIM_ID = "type-I-high-anchor-direct-c1-finite-menu-exhaustion"


def factorization(value: int) -> list[tuple[int, int]]:
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return factors


def is_prime(value: int) -> bool:
    return value >= 2 and factorization(value) == [(value, 1)]


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factorization(value):
        result = [divisor * prime**power for divisor in result for power in range(exponent + 1)]
    return sorted(result)


def divisor_count(value: int) -> int:
    count = 1
    for _prime, exponent in factorization(value):
        count *= exponent + 1
    return count


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    if support <= 0 or gcd(prime, 4 * support) != 1:
        raise AssertionError("canonical chart needs a positive carrier coprime to p")
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    K = (prime * R + 1) // 4
    if not (1 <= R < modulus and K % support == 0 and prime * R + 1 == 4 * K):
        raise AssertionError("canonical chart normalization failed")
    return R, K


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def full_excess_bundle(anchor_side: int, parent_K: int) -> tuple[int, int]:
    """H1: retain exactly prime powers whose valuation exceeds that in K."""
    Q = 1
    for prime, exponent in factorization(anchor_side):
        if exponent > valuation(parent_K, prime):
            Q *= prime**exponent
    if anchor_side % Q:
        raise AssertionError("full excess Q did not divide its anchor side")
    return Q, anchor_side // Q


def h2_predicate(prime: int, R: int, K: int, Q: int) -> dict[str, object]:
    """The H2 consequences, deliberately weaker than the H1 definition."""
    if Q <= 0 or (R - 1) % Q:
        return {"Q": Q, "defined": False, "holds": False}
    beta = (R - 1) // Q
    conditions = {
        "Q_gt_1": Q > 1,
        "beta_divides_K": K % beta == 0,
        "coprime_Q_beta": gcd(Q, beta) == 1,
        "Q_not_dividing_K": K % Q != 0,
        "Q_below_R": Q < R,
        "p_coprime_to_Q": Q % prime != 0,
    }
    return {
        "Q": Q,
        "beta": beta,
        "conditions": conditions,
        "holds": all(conditions.values()),
    }


def cofactor_replay(prime: int, R: int, K: int, A: int, Q: int) -> dict[str, object]:
    """Recompute the carrier, cofactor chart, gate, and possible c=1 return."""
    M = lcm(A, Q)
    R_M, K_M = canonical_chart(prime, M)
    if K_M % M:
        raise AssertionError("rechart carrier did not divide its K")
    C = K_M // M
    r = M % prime
    A_target = lcm(A, C)
    gate = r * C % A_target == 0
    difference = r * C - K
    phase_integral = difference % (prime * A) == 0
    h = difference // (prime * A) if phase_integral else None
    c = C // gcd(A, C)
    R_target, K_target = canonical_chart(prime, A_target)
    exact_c1_return = (
        gate
        and phase_integral
        and h == 0
        and c == 1
        and (R_target, K_target, A_target) == (R, K, A)
    )
    return {
        "Q": Q,
        "M": M,
        "canonical_rechart": {"R": R_M, "K": K_M},
        "r": r,
        "C": C,
        "A_target": A_target,
        "gate": gate,
        "phase_integral": phase_integral,
        "h": h,
        "c": c,
        "target": {"R": R_target, "K": K_target, "A": A_target},
        "exact_c1_return": exact_c1_return,
    }


def arithmetic_c1_labels(prime: int, R: int, K: int, A: int) -> list[dict[str, int]]:
    """Enumerate precisely the u labels in the c=1 iff criterion."""
    if K % A:
        raise AssertionError("charged support must divide K")
    B = K // A
    records: list[dict[str, int]] = []
    for u in divisors(A):
        r = B * u
        C = A // u
        if not (r < prime and C < prime and R < 4 * r):
            continue
        A_target = lcm(A, C)
        if not (r * C == K and A_target == A and r * C % A_target == 0):
            raise AssertionError("u label failed its algebraic c=1 reconstruction")
        h_numerator = r * C - K
        if h_numerator != 0 or h_numerator % (prime * A):
            raise AssertionError("u label failed the exact zero-phase equation")
        c = C // gcd(A, C)
        if c != 1:
            raise AssertionError("u label failed c=1")
        R_target, K_target = canonical_chart(prime, A_target)
        if (R_target, K_target, A_target) != (R, K, A):
            raise AssertionError("u label did not return to the source checkpoint")
        records.append({"u": u, "r": r, "C": C})
    return records


def high_r_v1_action(prime: int, R: int, K: int, A: int) -> dict[str, object]:
    """Freeze the one canonical H1/v1 action when its source conditions hold."""
    Q, beta = full_excess_bundle(R - 1, K)
    h2 = h2_predicate(prime, R, K, Q)
    source_conditions = {
        "prime_is_core": is_prime(prime) and prime % 24 == 1,
        "high_R_raw_source": R >= 3 and R % 4 == 3 and R % prime != 0,
        "charged_support": K % A == 0,
        "full_excess_nontrivial": Q > 1,
        "H2_consequences": bool(h2["holds"]),
    }
    if not all(source_conditions.values()):
        return {
            "Q": Q,
            "beta": beta,
            "registered_action_menu": [],
            "source_conditions": source_conditions,
        }
    replay = cofactor_replay(prime, R, K, A, Q)
    descriptor = {
        "adapter": "high_R_path_anchored_bundle_v1",
        "adapter_version": 1,
        "canonical_raw_source": "universal_p_source_v1",
        "canonical_path": "raw_p_edge_shift_1_to_(1,R-1,1)",
        "input": {"p": prime, "R": R, "K": K, "A": A},
        "complete_excess": {"Q": Q, "beta": beta, "factorization_R_minus_1": factorization(R - 1)},
        "carrier_and_cofactor": {key: replay[key] for key in ("M", "r", "C")},
        "verifier_version": "c1_finite_menu_fixture_v1",
    }
    action = {
        "action_id": "action:" + canonical_hash(descriptor),
        "descriptor": descriptor,
        "replay": replay,
    }
    return {
        "Q": Q,
        "beta": beta,
        "source_conditions": source_conditions,
        "registered_action_menu": [action],
    }


def require_chart(prime: int, R: int, K: int, A: int) -> None:
    if not (is_prime(prime) and prime % 24 == 1 and prime * R + 1 == 4 * K):
        raise AssertionError("fixture is not a core-prime chart")
    if not (A > 0 and K % A == 0 and prime < R < 4 * A):
        raise AssertionError("fixture is not a charged high anchor")


def p97_case() -> dict[str, object]:
    prime, R, K, A = 97, 99, 2401, 2401
    require_chart(prime, R, K, A)
    labels = arithmetic_c1_labels(prime, R, K, A)
    if labels != [{"u": 49, "r": 49, "C": 49}]:
        raise AssertionError("p=97 arithmetic c=1 label changed")
    v1 = high_r_v1_action(prime, R, K, A)
    if not (v1["Q"] == 2 and v1["beta"] == 49 and len(v1["registered_action_menu"]) == 1):
        raise AssertionError("p=97 H1/v1 singleton changed")
    action = v1["registered_action_menu"][0]
    if not isinstance(action, dict) or not action["replay"]["exact_c1_return"]:
        raise AssertionError("p=97 no longer realizes the c=1 self-loop")
    return {
        "input": {"p": prime, "R": R, "K": K, "A": A, "B": K // A},
        "tau_A": divisor_count(A),
        "arithmetic_c1_labels": labels,
        "H1_v1": v1,
        "conclusion": "The canonical v1 action is an actual arithmetic c=1 self-loop.",
    }


def p1657_case() -> dict[str, object]:
    prime, R, K, A = 1657, 1991, 824772, 824772
    require_chart(prime, R, K, A)
    labels = arithmetic_c1_labels(prime, R, K, A)
    expected = [
        {"u": 622, "r": 622, "C": 1326},
        {"u": 663, "r": 663, "C": 1244},
        {"u": 884, "r": 884, "C": 933},
        {"u": 933, "r": 933, "C": 884},
        {"u": 1244, "r": 1244, "C": 663},
        {"u": 1326, "r": 1326, "C": 622},
    ]
    if labels != expected:
        raise AssertionError("p=1657 arithmetic c=1 label census changed")
    v1 = high_r_v1_action(prime, R, K, A)
    if not (v1["Q"] == 995 and v1["beta"] == 2 and len(v1["registered_action_menu"]) == 1):
        raise AssertionError("p=1657 H1/v1 singleton changed")
    action = v1["registered_action_menu"][0]
    if not isinstance(action, dict) or not action["replay"]["exact_c1_return"]:
        raise AssertionError("p=1657 H1/v1 action no longer returns c=1")
    partial = cofactor_replay(prime, R, K, A, 5)
    partial_h2 = h2_predicate(prime, R, K, 5)
    if not partial["exact_c1_return"]:
        raise AssertionError("p=1657 partial-Q arithmetic boundary changed")
    if bool(partial_h2["holds"]) or partial_h2.get("beta") != 398:
        raise AssertionError("p=1657 partial Q unexpectedly satisfies H2")
    return {
        "input": {"p": prime, "R": R, "K": K, "A": A, "B": K // A},
        "factorization": {"R_minus_1": factorization(R - 1), "K": factorization(K)},
        "tau_A": divisor_count(A),
        "arithmetic_c1_labels": labels,
        "H1_v1": v1,
        "unregistered_partial_Q_5": {
            "H2_check": partial_h2,
            "replay": partial,
            "conclusion": (
                "Q=5 gives an arithmetic c=1 return, but beta=398 does not divide K; "
                "it is not the H1/v1 complete-excess action."
            ),
        },
    }


def p73_h2_boundary() -> dict[str, object]:
    prime, R, K, A = 73, 159, 2902, 1451
    require_chart(prime, R, K, A)
    Q_star, beta_star = full_excess_bundle(R - 1, K)
    if (Q_star, beta_star) != (79, 2):
        raise AssertionError("p=73 H1 full-excess result changed")
    h2_star = h2_predicate(prime, R, K, Q_star)
    h2_larger = h2_predicate(prime, R, K, 158)
    if not (bool(h2_star["holds"]) and bool(h2_larger["holds"])):
        raise AssertionError("p=73 H2 nonuniqueness boundary changed")
    v1 = high_r_v1_action(prime, R, K, A)
    if len(v1["registered_action_menu"]) != 1:
        raise AssertionError("p=73 v1 action menu should be singleton")
    return {
        "input": {"p": prime, "R": R, "K": K, "A": A, "B": K // A},
        "H1_full_excess": {"Q_star": Q_star, "beta_star": beta_star},
        "H2_candidates": [h2_star, h2_larger],
        "H1_v1": v1,
        "conclusion": (
            "Q*=79 is the unique H1 full-excess choice, while Q'=158 also passes the "
            "weaker H2 checks. H2 therefore cannot define a singleton action menu."
        ),
    }


def build_result() -> dict[str, object]:
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "purpose": "focused exact c=1 action-menu replay; it does not run the global selector",
        "contracts": {
            "arithmetic_label_iff": (
                "u divides A, r=(K/A)u<p, C=A/u<p, and R<4r iff the direct "
                "candidate has h=0, c=1 and returns the same arithmetic checkpoint"
            ),
            "finite_rank": "Xi=(floor(B_p/A), Omega(K/A), remaining_registered_actions)",
            "exhaustion_rule": (
                "Only a fully verified, terminal/alternate-complete no-progress action can be "
                "exhausted; unresolved actions are not exhausted."
            ),
        },
        "cases": {
            "p97_actual_c1_loop": p97_case(),
            "p1657_partial_excess_boundary": p1657_case(),
            "p73_H1_vs_H2_nonuniqueness": p73_h2_boundary(),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified c=1 arithmetic labels and H1/H2 finite-menu boundaries")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
