#!/usr/bin/env python3
"""Audit the block-imbalance relation/dyadic trichotomy on the full spectrum."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from sympy import divisors, factorint, n_order


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-trichotomy-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def linear_states(prime: int, modulus: int, K: int) -> list[dict[str, int]]:
    """Recover all directed (a,s) states from the two factors of 4K."""
    states: set[tuple[int, int, int, int]] = set()
    for block in divisors(4 * K):
        U = int(block)
        if U <= 1 or U % modulus != 1:
            continue
        V = (4 * K) // U
        if V % modulus != 1:
            continue
        s0 = (U - 1) // modulus
        a0 = (V - 1) // modulus
        if s0 <= 0 or a0 <= 0 or a0 + s0 + a0 * s0 * modulus != prime:
            continue
        for a, s, left, right in ((a0, s0, U, V), (s0, a0, V, U)):
            if s % 2 == 1:
                states.add((a, s, left, right))
    return [
        {"a": a, "s": s, "U": U, "V": V}
        for a, s, U, V in sorted(states)
    ]


def factor_vector(value: int) -> dict[int, int]:
    return {int(q): int(e) for q, e in factorint(value).items()}


def kernel_terminal(
    prime: int, modulus: int, K: int, factors: list[tuple[int, int]], lam: dict[int, int]
) -> dict[str, int]:
    ratio = Fraction(1, 1)
    for q, exponent in factors:
        power = lam.get(q, 0)
        ratio *= q**power if power >= 0 else Fraction(1, q ** (-power))
    if ratio == 1:
        raise AssertionError("kernel branch received a zero relation")
    if ratio > 1:
        ratio = 1 / ratio
        lam = {q: -value for q, value in lam.items()}
    U = ratio * K
    if U.denominator != 1:
        raise AssertionError("oriented kernel relation did not produce an integer")
    U = U.numerator
    E = 4 * U
    if not (0 < U < K and E % 2 == 0 and (4 * K * K) % E == 0):
        raise AssertionError("invalid kernel terminal divisor")
    if E % modulus != 1:
        raise AssertionError("kernel terminal has the wrong residue")
    numerator = 4 * K - E
    n, remainder = divmod(numerator, modulus)
    if remainder or n <= 0 or n >= prime or n % 4:
        raise AssertionError("invalid kernel terminal source")
    return {"U_terminal": U, "E": E, "source": n, "relation_linf": max(abs(v) for v in lam.values())}


def dyadic_terminal(
    prime: int,
    modulus: int,
    K: int,
    U: int,
    V: int,
    lambda_two: int,
) -> dict[str, int] | None:
    """Find the smallest admissible positive J in the generalized 2^J transfer."""
    U_factors = factor_vector(U)
    V_factors = factor_vector(V)
    U_odd = U // (2 ** U_factors.get(2, 0))
    V_odd = V // (2 ** V_factors.get(2, 0))
    common = math.gcd(U_odd, V_odd)
    if lambda_two > 0:
        A, B = V_odd // common, U_odd // common
    else:
        A, B = U_odd // common, V_odd // common
    j0 = abs(lambda_two)
    nu_two = factor_vector(K).get(2, 0)
    max_J = nu_two + 1  # v_2(2K), with A and B odd
    order_two = int(n_order(2, modulus))
    candidates = [J for J in range(1, max_J + 1) if (J - j0) % order_two == 0]
    candidates = [J for J in candidates if A < (2**J) * B]
    if not all((A - (2**J) * B) % modulus == 0 for J in candidates):
        raise AssertionError("dyadic relation did not reconstruct the block residue")
    if not candidates:
        return None
    J = min(candidates)
    L = 2 * K
    E_fraction = Fraction(L * A, B * (2 ** (J - 1)))
    if E_fraction.denominator != 1:
        raise AssertionError("dyadic transfer produced a nonintegral terminal")
    E = E_fraction.numerator
    if E % 2 or (L * L) % E or E % modulus != 1:
        raise AssertionError("invalid generalized dyadic terminal")
    source, remainder = divmod(2 * L - E, modulus)
    if remainder or source <= 0 or source >= prime or source % 2:
        raise AssertionError("invalid generalized dyadic source")
    return {
        "A": A,
        "B": B,
        "j0": j0,
        "J": J,
        "E": E,
        "source": source,
        "order_two": order_two,
    }


def audit_state(prime: int, modulus: int, K: int, state: dict[str, int]) -> dict[str, object]:
    U, V = int(state["U"]), int(state["V"])
    K_factors = factor_vector(K)
    U_factors = factor_vector(U)
    V_factors = factor_vector(V)
    lambda_two = U_factors.get(2, 0) - V_factors.get(2, 0)
    odd_lambda = {
        q: U_factors.get(q, 0) - V_factors.get(q, 0)
        for q in K_factors
        if q != 2
    }
    factors = sorted(K_factors.items())
    if lambda_two == 0 and any(odd_lambda.values()):
        exponents = [max(0, abs(odd_lambda.get(q, 0)) - exponent) for q, exponent in factors]
        if any(exponents):
            raise AssertionError("odd block imbalance left the K exponent box")
        witness = kernel_terminal(prime, modulus, K, factors, odd_lambda)
        return {
            **state,
            "classification": "kernel_relation",
            "lambda_two": 0,
            "odd_relation": odd_lambda,
            "terminal": witness,
        }
    if lambda_two == 0:
        if U != V:
            raise AssertionError("zero block imbalance did not reconstruct U=V")
        return {
            **state,
            "classification": "symmetric",
            "lambda_two": 0,
            "odd_relation": odd_lambda,
        }
    witness = dyadic_terminal(prime, modulus, K, U, V, lambda_two)
    return {
        **state,
        "classification": "dyadic_terminal" if witness else "dyadic_unresolved",
        "lambda_two": lambda_two,
        "odd_relation": odd_lambda,
        "terminal": witness,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records: list[dict[str, object]] = []
    classification = Counter()
    prime_summary: dict[int, dict[str, int]] = {}
    for profile in payload["profiles"]:
        prime = int(profile["prime"])
        summary = prime_summary.setdefault(
            prime,
            {"state_count": 0, "kernel_relation": 0, "dyadic_terminal": 0, "dyadic_unresolved": 0, "symmetric": 0},
        )
        for row in profile["records"]:
            modulus, K = int(row["R"]), int(row["K"])
            states = linear_states(prime, modulus, K)
            if len(states) != int(row["source_state_count"]):
                raise AssertionError("linear state reconstruction count changed")
            for state in states:
                audited = audit_state(prime, modulus, K, state)
                audited.update({"prime": prime, "R": modulus, "K": K})
                records.append(audited)
                kind = str(audited["classification"])
                classification[kind] += 1
                summary["state_count"] += 1
                summary[kind] += 1
    if len(records) != int(payload["complete_directed_linear_source_count"]):
        raise AssertionError("directed source state total changed")
    return {
        "arithmetic": (
            "Recover every directed linear state from U=sR+1 and V=aR+1. The exponent "
            "difference is a kernel relation when the 2-adic difference vanishes; otherwise "
            "it is audited by the generalized 2^J transfer."
        ),
        "scope_note": (
            "Finite complete-spectrum audit for 200 selected pressure primes. Kernel and dyadic "
            "terminal witnesses are strict local exits; symmetric and unresolved dyadic states "
            "remain open and no global selector theorem is claimed."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "prime_count": len(prime_summary),
        "linear_R_count": int(payload["complete_linear_R_count"]),
        "directed_state_count": len(records),
        "classification_counts": {key: int(value) for key, value in sorted(classification.items())},
        "terminal_state_count": int(classification["kernel_relation"] + classification["dyadic_terminal"]),
        "terminal_prime_count": len(
            {
                int(record["prime"])
                for record in records
                if record["classification"] in {"kernel_relation", "dyadic_terminal"}
            }
        ),
        "prime_summary": {str(prime): summary for prime, summary in sorted(prime_summary.items())},
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "prime_count", "linear_R_count", "directed_state_count", "classification_counts",
        "terminal_state_count", "terminal_prime_count",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
