#!/usr/bin/env python3
"""Verify the q=1 second-anchor fixed-n escape macro.

The macro starts at the low first Type I child, records the forced high
complete-excess chart only as a transient determinant, and applies one
explicit quotient-fold carrier.  It checks the two symbolic carrier choices
on focused q=1 G controls; it does not search for Egyptian-fraction proofs or
claim a total Type I selector.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm

import type_ii_q_one_full_carrier_second_anchor_overflow as second_anchor
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


ADAPTER = "q_one_full_carrier_second_anchor_fixed_n_escape_v1"
SOURCE_SCOPE = "fresh_source_tree_only"


def digest(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def macro_state(
    prime: int, R: int, K: int, support: int, state_class: str, normal_form: str
) -> dict[str, object]:
    """Materialize the q=1 macro state with chart-independent marking."""
    state: dict[str, object] = {
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "R": R,
        "K": K,
        "support": support,
        "state_class": state_class,
        "source_tree_scope": SOURCE_SCOPE,
        "normal_form": normal_form,
        "target_fiber": {
            "status": "inherited_full_solution_set",
            "reason": "q=1 macro uses chart-independent Sol(p) marking",
        },
        "signed_defect": {
            "status": "not_applicable",
            "reason": "identity lift uses the full solution set",
        },
        "potential_record": {
            "B_p": (prime - 1) ** 2 // 4,
            "value": (prime - 1) ** 2 // (4 * support),
        },
    }
    state["state_id"] = "state:" + digest(state)
    return state


def universal_p_source(prime: int, R: int, K: int) -> dict[str, object]:
    """Rebuild the actual p-source and its unique edge to the anchor."""
    source = (prime, R * (prime - 1) - prime, prime - 1)
    anchor = (1, R - 1, 1)
    if not (
        min(source) > 0
        and source[0] + source[1] == R * source[2]
        and gcd(source[0], source[1]) == 1
        and K % prime != 0
        and source[0] % prime == 0
        and (source[1] + R) % prime == 0
        and (source[2] + 1) % prime == 0
        and (source[0] // prime, (source[1] + R) // prime, (source[2] + 1) // prime)
        == anchor
    ):
        raise AssertionError("universal p-source did not replay")
    return {
        "source": list(source),
        "q": prime,
        "shift": 1,
        "gcd_reduction": 1,
        "destination": list(anchor),
    }


def quotient_fold(
    prime: int, carrier: int, defect: int, n: int, support: int, L: int
) -> dict[str, int]:
    """Apply the existing fixed-n quotient-fold identity to one chosen carrier."""
    S = carrier * defect
    if not (S % L == 0 and support < L <= (prime - 1) ** 2 // 4):
        raise AssertionError("chosen carrier is outside the quotient-fold domain")
    quotient = S // L
    h, delta = divmod(quotient, prime)
    if delta == 0:
        raise AssertionError("p unexpectedly divided the quotient")
    target_n = n - 4 * L * h
    target_R = 4 * L - target_n
    target_K = L * (prime - delta)
    expected_chart = second_anchor.canonical_chart(prime, L)
    expected_R, expected_K = int(expected_chart["R"]), int(expected_chart["K"])
    if not (
        target_n > 0
        and target_n < 4 * L
        and prime * target_n == 4 * L * delta + 1
        and prime * target_R + 1 == 4 * target_K
        and target_K % L == 0
        and (target_R, target_K) == (expected_R, expected_K)
    ):
        raise AssertionError("fixed-n quotient fold did not rebuild a canonical target")
    return {
        "S": S,
        "L": L,
        "quotient": quotient,
        "h": h,
        "delta": delta,
        "n": target_n,
        "R": target_R,
        "K": target_K,
    }


def transient_overflow(
    prime: int, R: int, K: int, support: int
) -> dict[str, object]:
    """Build the actual anchor bundle and its high determinant without queueing it."""
    source = universal_p_source(prime, R, K)
    anchor = R - 1
    excess = second_anchor.complete_excess(anchor, K)
    Q, beta = int(excess["Q"]), int(excess["beta"])
    carrier = lcm(support, Q)
    chart = second_anchor.canonical_chart(prime, carrier)
    high_R, high_K = int(chart["R"]), int(chart["K"])
    C, remainder = divmod(high_K, carrier)
    n = 4 * carrier - high_R
    defect = prime - C
    if not (
        source["destination"] == [1, anchor, 1]
        and Q > 1
        and anchor % Q == 0
        and K % beta == 0
        and gcd(Q, beta) == 1
        and K % Q != 0
        and Q < R < prime
        and high_R > prime
        and remainder == 0
        and 1 <= C < prime
        and n > 0
        and 1 <= defect < prime
        and prime * n == 4 * carrier * defect + 1
    ):
        raise AssertionError("second-anchor high determinant did not replay")
    return {
        "raw_source": source,
        "anchor": anchor,
        "complete_excess": excess,
        "carrier": carrier,
        "R": high_R,
        "K": high_K,
        "C": C,
        "n": n,
        "d": defect,
        "charged_support_retained_from_parent": support,
        "queued": False,
    }


def parent_child(prime: int) -> dict[str, int | str]:
    """Recover the forced low child from the target-independent carrier rail."""
    t = (prime - 1) // 24
    dispatch = rail.full_carrier_dispatch(prime)["dispatch"]
    R, K, A = (int(dispatch[field]) for field in ("R", "K", "support"))
    if not (
        rail.is_prime(prime)
        and prime % 24 == 1
        and rail.q_one_g(6 * t + 1)
        and 3 <= R <= prime - 2
        and prime * R + 1 == 4 * K
        and K % A == 0
    ):
        raise AssertionError("full-carrier first child did not replay")
    return {"t": t, "kind": str(dispatch["kind"]), "R": R, "K": K, "A": A}


def odd_macro(t: int) -> dict[str, object]:
    prime = 24 * t + 1
    parent = parent_child(prime)
    R, K, A = (int(parent[field]) for field in ("R", "K", "A"))
    transient = transient_overflow(prime, R, K, A)
    Q = int(transient["complete_excess"]["Q"])
    carrier = int(transient["carrier"])
    B_p = (prime - 1) ** 2 // 4
    L = 2 * Q
    folded = quotient_fold(
        prime, carrier, int(transient["d"]), int(transient["n"]), A, L
    )
    target_R = int(folded["R"])
    parent_state = macro_state(
        prime, R, K, A, "marked_absorb", "q_one_full_carrier_first_child_v1"
    )
    target_state = macro_state(
        prime,
        target_R,
        int(folded["K"]),
        L,
        "marked_absorb" if target_R < prime else "overflow",
        "overflow_fixed_n_quotient_fold_outer_rank_v1",
    )
    source_potential, target_potential = B_p // A, B_p // L
    proof_gap_numerator = 144 * t**3
    proof_gap_denominator = (8 * t + 1) * (10 * t + 1)
    unit_remainder = 4 * L + 1 - 3 * prime
    e1_e5 = {
        "E1": bool(
            transient["raw_source"]["destination"] == [1, R - 1, 1]
            and Q == 10 * t + 1
            and transient["complete_excess"]["beta"] == 2
        ),
        "E2": bool(
            prime * int(folded["n"]) == 4 * L * int(folded["delta"]) + 1
            and prime * int(folded["R"]) + 1 == 4 * int(folded["K"])
        ),
        "E3": bool(
            carrier == A * Q
            and L > A
            and L <= B_p
            and int(folded["K"]) % L == 0
            and parent_state["state_id"] != target_state["state_id"]
            and parent_state["equation_target"] == target_state["equation_target"]
            and target_state["normal_form"]
            == "overflow_fixed_n_quotient_fold_outer_rank_v1"
        ),
        "E4": bool(
            parent_state["marked_solution_set"]
            == target_state["marked_solution_set"]
            == "Sol(p)"
        ),
        "E5": target_potential < source_potential,
    }
    if not (
        t >= 3
        and t % 2 == 1
        and parent["kind"] == "marked_absorb"
        and (R, K, A)
        == (20 * t + 3, (8 * t + 1) * (15 * t + 1), 2 * (8 * t + 1))
        and Q == 10 * t + 1
        and gcd(8 * t + 1, Q) == 1
        and carrier == A * Q
        and L == 2 * Q
        and carrier % L == 0
        and L % A != 0
        and L <= B_p
        and proof_gap_numerator > proof_gap_denominator
        and unit_remainder == 8 * t + 6
        and 0 < unit_remainder < prime
        and (4 * L + 1) % prime != 0
        and int(folded["delta"]) >= 2
        and all(e1_e5.values())
    ):
        raise AssertionError("odd second-anchor macro failed")
    result = {
        "branch": "odd",
        "prime": prime,
        "t": t,
        "parent": {**parent_state, "dispatch_kind": parent["kind"]},
        "transient_overflow": transient,
        "selected_carrier": {
            "rule": "L=2*(10t+1)",
            "L": L,
            "support_semantics": "paid_outer_rank_reset",
            "support_reset_paid": True,
            "strict_gap": {
                "numerator": proof_gap_numerator,
                "denominator": proof_gap_denominator,
                "greater_than_one": True,
            },
            "unit_defect_exclusion": {
                "four_L_plus_one": 4 * L + 1,
                "remainder_after_three_p": unit_remainder,
                "delta_at_least_two": True,
            },
        },
        "fold": folded,
        "target": target_state,
        "potential": {"source": source_potential, "target": target_potential},
        "e1_e5": e1_e5,
    }
    result["macro_edge_id"] = "edge:" + digest(result)
    return result


def even_macro(t: int) -> dict[str, object]:
    prime = 24 * t + 1
    s = t // 2
    parent = parent_child(prime)
    R, K, A = (int(parent[field]) for field in ("R", "K", "A"))
    transient = transient_overflow(prime, R, K, A)
    blocks = transient["complete_excess"]["blocks"]
    excess_primes = sorted(
        int(block["prime"])
        for block in blocks
        if (6 * s - 1) % int(block["prime"]) == 0
    )
    if not excess_primes:
        raise AssertionError("missing forced second-anchor excess prime")
    q_star = excess_primes[0]
    carrier = int(transient["carrier"])
    B_p = (prime - 1) ** 2 // 4
    L = A * q_star
    folded = quotient_fold(
        prime, carrier, int(transient["d"]), int(transient["n"]), A, L
    )
    target_R = int(folded["R"])
    parent_state = macro_state(
        prime, R, K, A, "marked_absorb", "q_one_full_carrier_first_child_v1"
    )
    target_state = macro_state(
        prime,
        target_R,
        int(folded["K"]),
        L,
        "marked_absorb" if target_R < prime else "overflow",
        "overflow_fixed_n_quotient_fold_outer_rank_v1",
    )
    source_potential, target_potential = B_p // A, B_p // L
    unit_obstruction = 4 * (4 * L + 1) - 3 * q_star * prime
    e1_e5 = {
        "E1": bool(
            transient["raw_source"]["destination"] == [1, R - 1, 1]
            and q_star in [int(block["prime"]) for block in blocks]
            and (6 * s - 1) % q_star == 0
        ),
        "E2": bool(
            prime * int(folded["n"]) == 4 * L * int(folded["delta"]) + 1
            and prime * int(folded["R"]) + 1 == 4 * int(folded["K"])
        ),
        "E3": bool(
            L > A
            and carrier % L == 0
            and L <= B_p
            and int(folded["K"]) % L == 0
            and parent_state["state_id"] != target_state["state_id"]
            and parent_state["equation_target"] == target_state["equation_target"]
            and target_state["normal_form"]
            == "overflow_fixed_n_quotient_fold_outer_rank_v1"
        ),
        "E4": bool(
            parent_state["marked_solution_set"]
            == target_state["marked_solution_set"]
            == "Sol(p)"
        ),
        "E5": target_potential < source_potential,
    }
    if not (
        t >= 4
        and t % 2 == 0
        and s >= 2
        and parent["kind"] == "fixed_n_edge"
        and (R, K, A) == (12 * s - 1, 9 * s * (16 * s - 1), 9 * s)
        and gcd(6 * s - 1, A) == 1
        and rail.is_prime(q_star)
        and q_star <= 6 * s - 1 < 64 * s
        and B_p == 576 * s * s
        and B_p // A == 64 * s
        and L == A * q_star
        and carrier % L == 0
        and L <= B_p
        and L % A == 0
        and unit_obstruction == 4 - 3 * q_star
        and 0 < -unit_obstruction < prime
        and (4 * L + 1) % prime != 0
        and int(folded["delta"]) >= 2
        and all(e1_e5.values())
    ):
        raise AssertionError("even second-anchor macro failed")
    result = {
        "branch": "even",
        "prime": prime,
        "t": t,
        "s": s,
        "parent": {**parent_state, "dispatch_kind": parent["kind"]},
        "transient_overflow": transient,
        "selected_carrier": {
            "rule": "L=A*q_star, q_star=min(q | Q and q | 6s-1)",
            "q_star": q_star,
            "L": L,
            "support_semantics": "support_preserving_growth",
            "support_retained": True,
            "unit_defect_exclusion": {
                "four_L_plus_one": 4 * L + 1,
                "linear_obstruction": unit_obstruction,
                "delta_at_least_two": True,
            },
        },
        "fold": folded,
        "target": target_state,
        "potential": {"source": source_potential, "target": target_potential},
        "e1_e5": e1_e5,
    }
    result["macro_edge_id"] = "edge:" + digest(result)
    return result


def postmacro_full_product(row: dict[str, object]) -> dict[str, object]:
    """Close every high macro target with its forced full-product fold."""
    prime = int(row["prime"])
    fold = row["fold"]
    support = int(row["target"]["support"])
    defect = int(fold["delta"])
    n = int(fold["n"])
    B_p = (prime - 1) ** 2 // 4
    target_R = int(row["target"]["R"])
    if not (
        defect >= 2
        and prime * n == 4 * support * defect + 1
        and n % 4 == 1
    ):
        raise AssertionError("postmacro input lost its nonunit determinant")
    if target_R < prime:
        return {
            "status": "marked_absorb_exit",
            "reason": "the first macro already left the high-overflow interface",
            "n_T": n,
            "prime": prime,
            "defect": defect,
        }

    S = support * defect
    successor_R = 4 * S - n
    successor_K = S * (prime - 1)
    expected_chart = second_anchor.canonical_chart(prime, S)
    source_potential, successor_potential = B_p // support, B_p // S
    successor_state = macro_state(
        prime,
        successor_R,
        successor_K,
        S,
        "marked_absorb" if successor_R < prime else "overflow",
        "overflow_fixed_n_full_product_quotient_fold_v1",
    )
    bounded_saturation = n < prime
    if not (
        target_R > prime
        and S == (prime * n - 1) // 4
        and support < S
        and prime * successor_R + 1 == 4 * successor_K
        and (successor_R, successor_K)
        == (int(expected_chart["R"]), int(expected_chart["K"]))
        and successor_potential < source_potential
        and successor_state["state_id"]
        != row["target"]["state_id"]
    ):
        raise AssertionError("postmacro full-product fold did not replay")
    if bounded_saturation and not (
        n <= prime - 4 and S <= B_p and target_R > prime
    ):
        raise AssertionError("bounded saturation specialization did not replay")
    return {
        "status": "strict_full_product_fold",
        "bounded_saturation_specialization": bounded_saturation,
        "source": {"support": support, "n": n, "d": defect, "R": target_R},
        "selected_divisor": S,
        "successor": successor_state,
        "potential": {"source": source_potential, "successor": successor_potential},
        "e1_e5": {f"E{index}": True for index in range(1, 6)},
    }


def verify() -> dict[str, object]:
    odd_rows = [odd_macro(t) for t in (3, 25, 105)]
    even_rows = [even_macro(t) for t in (8, 10, 32, 4950)]
    expected = {
        73: {"L": 62, "delta": 5, "n": 17, "R": 231, "K": 4216},
        601: {"L": 502, "delta": 472, "n": 1577, "R": 431, "K": 64758},
        193: {"L": 828, "delta": 56, "n": 961, "R": 2351, "K": 113436},
        241: {"L": 1305, "delta": 97, "n": 2101, "R": 3119, "K": 187920},
    }
    for row in [*odd_rows, *even_rows]:
        row["postmacro_full_product"] = postmacro_full_product(row)
        prime = int(row["prime"])
        if not all(row["e1_e5"].values()):
            raise AssertionError(f"macro E1--E5 failed for p={prime}")
        if not int(row["potential"]["target"]) < int(row["potential"]["source"]):
            raise AssertionError(f"macro potential did not decrease for p={prime}")
        if prime not in expected:
            continue
        fold = row["fold"]
        check = expected[prime]
        if any(int(fold[field]) != value for field, value in check.items()):
            raise AssertionError(f"focused macro control changed for p={prime}")
    if not (
        odd_rows[1]["selected_carrier"]["support_reset_paid"]
        and odd_rows[1]["parent"]["support"] < odd_rows[1]["selected_carrier"]["L"]
        and even_rows[0]["selected_carrier"]["support_retained"]
    ):
        raise AssertionError("reset and support-preserving control split changed")
    full_product_primes = {
        int(row["prime"])
        for row in [*odd_rows, *even_rows]
        if row["postmacro_full_product"]["status"] == "strict_full_product_fold"
    }
    bounded_saturation_primes = {
        int(row["prime"])
        for row in [*odd_rows, *even_rows]
        if row["postmacro_full_product"].get("bounded_saturation_specialization")
    }
    if full_product_primes != {73, 193, 241, 769, 2521, 118801}:
        raise AssertionError("postmacro full-product controls changed")
    if bounded_saturation_primes != {73, 2521}:
        raise AssertionError("postmacro bounded-saturation controls changed")
    if odd_rows[1]["postmacro_full_product"]["status"] != "marked_absorb_exit":
        raise AssertionError("postmacro low-chart exit control changed")
    return {
        "status": "verified",
        "adapter": ADAPTER,
        "odd_controls": odd_rows,
        "even_controls": even_rows,
        "postmacro_full_product_controls": sorted(full_product_primes),
        "bounded_saturation_controls": sorted(bounded_saturation_primes),
        "scope": (
            "A strict macro through the second-anchor transient overflow only; no "
            "terminal membership, total Type I selector, or final n<p exit is asserted."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
