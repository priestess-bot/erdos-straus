#!/usr/bin/env python3
"""Globally exclude linear shifted-source B=1 states at p=878089.

If ``E | n`` and ``E=s*R+1`` for ``n=p-s``, writing ``a=n/E`` gives
``p=a+s+a*s*R``.  Every such state has
``min(a,s) <= floor(sqrt((p-2)/3))``.  This audit uses that bound to
enumerate every state, exhausts every B=1 target divisor for each induced
``R``, recomputes the ordinary Type II p-1 tail failure, and replays the
stored successful nonlinear upper-half B=1 bridge.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions import short_certificate  # noqa: E402


PRIME = 878_089
TAIL_ARTIFACT = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
BRIDGE_ARTIFACT = (
    ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-I-linear-shifted-source-counterexample-878089.json"
)


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Return and verify the complete prime factorization of ``value``."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("factorization did not reconstruct its input")
    if any(not sympy.isprime(prime) for prime, _ in factors):
        raise AssertionError("factorization contains a composite base")
    return factors


def divisors_from_factorization(factors: list[tuple[int, int]]) -> list[int]:
    """Return every positive divisor represented by ``factors``."""
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def source_normalization(source: int, bridge: int) -> dict[str, int]:
    """Return the unique normalized ``u=alpha*beta*gamma`` source factors."""
    scale = math.gcd(bridge, 4)
    if source % scale or bridge % scale:
        raise AssertionError("source normalization is not integral")
    normalized_source = source // scale
    normalized_bridge = bridge // scale
    common = math.gcd(normalized_source, normalized_bridge)
    beta = normalized_bridge // common
    if common % beta:
        raise AssertionError("normalized square divisor has nonintegral gamma")
    gamma = common // beta
    alpha = normalized_source // common
    if (
        normalized_source != alpha * beta * gamma
        or normalized_bridge != beta * beta * gamma
        or math.gcd(alpha, beta) != 1
    ):
        raise AssertionError("normalized source factors did not reconstruct")
    return {
        "lambda": scale,
        "u": normalized_source,
        "D": normalized_bridge,
        "g": common,
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "eta": 4 // scale,
    }


def oriented_linear_states(
    prime: int, minimum: int, maximum: int, R: int
) -> list[dict[str, object]]:
    """Orient one unordered pair by every odd shifted-source coordinate."""
    orientations: list[tuple[int, int]] = []
    if minimum % 2:
        orientations.append((maximum, minimum))
    if maximum != minimum and maximum % 2:
        orientations.append((minimum, maximum))
    if not orientations:
        raise AssertionError("an odd prime state has no odd orientation")

    records: list[dict[str, object]] = []
    for a, shift in orientations:
        source = prime - shift
        bridge = shift * R + 1
        if (
            prime != a + shift + a * shift * R
            or source != a * bridge
            or source % bridge
            or shift > (prime - 1) // 2
        ):
            raise AssertionError("linear shifted-source state did not reconstruct")
        normalization = source_normalization(source, bridge)
        if normalization["beta"] != 1:
            raise AssertionError("E|n did not normalize to beta=1")
        records.append(
            {
                "a": a,
                "s": shift,
                "R": R,
                "E": bridge,
                "n": source,
                "unordered_pair": [minimum, maximum],
                "source_normalization": normalization,
            }
        )
    return records


def enumerate_linear_states(
    prime: int,
) -> tuple[int, list[dict[str, int]], list[dict[str, object]]]:
    """Exhaust all ``E|n`` source states through the square-root bound."""
    bound = math.isqrt((prime - 2) // 3)
    pairs: list[dict[str, int]] = []
    states: list[dict[str, object]] = []
    seen_pairs: set[tuple[int, int, int]] = set()

    for minimum in range(1, bound + 1):
        difference = prime - minimum
        for divisor in divisors_from_factorization(exact_factorization(difference)):
            maximum = difference // divisor
            if maximum < minimum or (divisor - 1) % minimum:
                continue
            R = (divisor - 1) // minimum
            if R < 3 or R % 4 != 3:
                continue
            if prime != minimum + maximum + minimum * maximum * R:
                raise AssertionError("divisor state did not recover p")
            key = (minimum, maximum, R)
            if key in seen_pairs:
                raise AssertionError("unordered source pair was enumerated twice")
            seen_pairs.add(key)
            orientations = oriented_linear_states(prime, minimum, maximum, R)
            pairs.append(
                {
                    "u": minimum,
                    "v": maximum,
                    "R": R,
                    "orientation_count": len(orientations),
                }
            )
            states.extend(orientations)

    pairs.sort(key=lambda row: (row["R"], row["u"], row["v"]))
    states.sort(
        key=lambda row: (
            int(row["R"]),
            int(row["s"]),
            int(row["a"]),
        )
    )
    for state_id, state in enumerate(states, 1):
        state["state_id"] = state_id
    return bound, pairs, states


def audit_target_modulus(
    prime: int, R: int, source_state_ids: list[int]
) -> dict[str, object]:
    """Exhaust every B=1 target divisor for one induced modulus ``R``."""
    K, remainder = divmod(prime * R + 1, 4)
    if remainder:
        raise AssertionError("target K is not integral")
    factors = exact_factorization(K)
    divisors = divisors_from_factorization(factors)
    reachable_residues = sorted({divisor % R for divisor in divisors})
    target_C_residue = (-pow(4, -1, R)) % R
    target_H_residue = R - 1
    C_hits = [divisor for divisor in divisors if divisor % R == target_C_residue]
    H_hits = [divisor for divisor in divisors if divisor % R == target_H_residue]
    if len(C_hits) != len(H_hits):
        raise AssertionError("complementary C/H target counts disagree")
    return {
        "R": R,
        "K": K,
        "K_factorization": [
            {"prime": prime_factor, "exponent": exponent}
            for prime_factor, exponent in factors
        ],
        "source_state_count": len(source_state_ids),
        "source_state_ids": source_state_ids,
        "divisor_count": len(divisors),
        "reachable_divisor_residue_count": len(reachable_residues),
        "reachable_divisor_residues": reachable_residues,
        "target_C_residue": target_C_residue,
        "target_H_residue": target_H_residue,
        "target_C_hit_count": len(C_hits),
        "target_H_hit_count": len(H_hits),
        "target_reachable": bool(C_hits),
    }


def target_audits(
    prime: int, states: list[dict[str, object]]
) -> list[dict[str, object]]:
    """Audit every distinct target modulus induced by ``states``."""
    state_ids_by_R: dict[int, list[int]] = {}
    for state in states:
        R = int(state["R"])
        state_ids_by_R.setdefault(R, []).append(int(state["state_id"]))
    return [
        audit_target_modulus(prime, R, state_ids_by_R[R])
        for R in sorted(state_ids_by_R)
    ]


def first_linear_b1_witness(prime: int) -> dict[str, object] | None:
    """Return a deterministic global linear B=1 witness, if one exists."""
    _, _, states = enumerate_linear_states(prime)
    first_state_by_R: dict[int, dict[str, object]] = {}
    for state in states:
        first_state_by_R.setdefault(int(state["R"]), state)
    for R, state in sorted(first_state_by_R.items()):
        K = (prime * R + 1) // 4
        target = (-pow(4, -1, R)) % R
        for C in divisors_from_factorization(exact_factorization(K)):
            if C % R != target:
                continue
            H = K // C
            A = (H + 1) // R
            gap = (4 * C + 1) // R
            source = int(state["n"])
            bridge = int(state["E"])
            source_term = source * K // bridge
            target_solution = [A * C, A * C * H, prime * K]
            source_solution = [source_term, target_solution[0], target_solution[1]]
            if (
                prime != 4 * A * C - gap
                or Fraction(4, prime)
                != sum(
                    (Fraction(1, denominator) for denominator in target_solution),
                    Fraction(),
                )
                or Fraction(4, source)
                != sum(
                    (Fraction(1, denominator) for denominator in source_solution),
                    Fraction(),
                )
            ):
                raise AssertionError("linear B=1 witness did not replay")
            return {
                "prime": prime,
                "a": int(state["a"]),
                "s": int(state["s"]),
                "R": R,
                "E": bridge,
                "n": source,
                "K": K,
                "C": C,
                "H": H,
                "A": A,
                "B": 1,
                "m": gap,
            }
    return None


def load_json(path: Path) -> dict[str, object]:
    """Load a repository JSON object."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise AssertionError(f"{path.name} is not a JSON object")
    return payload


def artifact_sha256(path: Path) -> str:
    """Return the exact content hash of an input artifact."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ordinary_tail_and_prefix_audit(prime: int) -> dict[str, object]:
    """Recompute the ordinary tail miss and close every smaller stored miss."""
    payload = load_json(TAIL_ARTIFACT)
    raw_misses = payload["misses"]
    if not isinstance(raw_misses, list):
        raise AssertionError("tail artifact has no miss list")
    prefix_rows = [
        row
        for row in raw_misses
        if isinstance(row, dict) and int(row["prime"]) <= prime
    ]
    prefix_primes = [int(row["prime"]) for row in prefix_rows]
    if not prefix_primes or prefix_primes[-1] != prime:
        raise AssertionError("target is not the final point of its stored prefix")
    smaller_witnesses = []
    for smaller_prime in prefix_primes[:-1]:
        witness = first_linear_b1_witness(smaller_prime)
        if witness is None:
            raise AssertionError("a smaller stored tail miss has no linear witness")
        smaller_witnesses.append(witness)

    factors = exact_factorization(prime - 1)
    eligible_gaps = [
        divisor - 1
        for divisor in divisors_from_factorization(factors)
        if divisor % 4 == 0
    ]
    spf = short_certificate.smallest_prime_factors(prime)
    witnesses = short_certificate.type_ii_tail_deflation_scan(prime, spf)
    stored_target = prefix_rows[-1]
    if (
        stored_target.get("eligible_gaps") != eligible_gaps
        or witnesses
        or int(stored_target["eligible_gap_count"]) != len(eligible_gaps)
    ):
        raise AssertionError("ordinary tail recomputation disagrees with its artifact")
    return {
        "input_artifact": TAIL_ARTIFACT.name,
        "input_sha256": artifact_sha256(TAIL_ARTIFACT),
        "stored_miss_prefix_primes": prefix_primes,
        "smaller_stored_miss_count": len(smaller_witnesses),
        "smaller_linear_B_eq_1_witnesses": smaller_witnesses,
        "target_is_first_strict_linear_failure_in_stored_prefix": True,
        "p_minus_one_factorization": [
            {"prime": prime_factor, "exponent": exponent}
            for prime_factor, exponent in factors
        ],
        "eligible_gap_count": len(eligible_gaps),
        "eligible_gaps": eligible_gaps,
        "ordinary_type_ii_tail_witness_count": len(witnesses),
        "ordinary_type_ii_tail_witnesses": [asdict(witness) for witness in witnesses],
    }


def nonlinear_b1_bridge_audit(prime: int) -> dict[str, object]:
    """Replay the authoritative successful nonlinear upper-half B=1 bridge."""
    payload = load_json(BRIDGE_ARTIFACT)
    raw_records = payload["records"]
    if not isinstance(raw_records, list):
        raise AssertionError("B=1 artifact has no record list")
    matches = [
        row
        for row in raw_records
        if isinstance(row, dict) and int(row["prime"]) == prime
    ]
    if len(matches) != 1:
        raise AssertionError("authoritative B=1 record is not unique")
    stored_record = matches[0]
    witness = stored_record["minimum_b1_source_witness"]
    if not isinstance(witness, dict):
        raise AssertionError("authoritative B=1 witness is malformed")
    lift = witness["reverse_two_tail_lift"]
    normal_form = witness["normal_form"]
    if not isinstance(lift, dict) or not isinstance(normal_form, list):
        raise AssertionError("authoritative bridge parameters are malformed")

    gap = int(witness["gap"])
    A, B, C = (int(value) for value in normal_form)
    R = int(witness["R"])
    K = int(witness["K"])
    bridge = int(witness["E"])
    source = int(lift["source_denominator"])
    source_term = int(lift["source_term"])
    bridge_divisor = int(lift["bridge_divisor"])
    shift = prime - source
    H = K // C
    certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
    if certificate is None:
        raise AssertionError("authoritative Type I certificate did not reconstruct")
    target_solution = [certificate.x, certificate.y, certificate.z]
    source_solution = [source_term, certificate.x, certificate.y]
    normalization = source_normalization(source, bridge)
    linear_remainder = source % bridge
    L, L_remainder = divmod(
        normalization["alpha"] * R + normalization["beta"],
        normalization["eta"],
    )
    if L_remainder:
        raise AssertionError("nonlinear K factorization has nonintegral L")
    normalization["L"] = L

    conditions = {
        "B_equals_one": B == 1,
        "source_is_strict_even_upper_half": (
            2 <= source < prime and source % 2 == 0 and 2 * source >= prime + 1
        ),
        "E_equals_sR_plus_one": bridge == shift * R + 1,
        "E_does_not_divide_n": linear_remainder != 0,
        "normalized_beta_exceeds_one": normalization["beta"] > 1,
        "source_square_compatible": (source * source // math.gcd(bridge, 4)) % bridge
        == 0,
        "E_divides_4K_squared": (4 * K * K) % bridge == 0,
        "target_divisor_condition": K % C == 0 and (4 * C + 1) % R == 0,
        "normal_form_reconstructs": (
            gap * R == 4 * B * B * C + 1
            and H == A * R - B
            and K == B * C * H
            and 4 * K == prime * R + 1
            and prime == 4 * A * B * C - gap
        ),
        "stored_bridge_divisor_reconstructs": bridge_divisor == prime * prime * bridge,
        "stored_source_term_reconstructs": source_term * bridge == source * K,
        "normalized_K_factorization": (
            K == normalization["beta"] * normalization["gamma"] * L
        ),
        "target_identity": Fraction(4, prime)
        == sum(
            (Fraction(1, denominator) for denominator in target_solution),
            Fraction(),
        ),
        "source_identity": Fraction(4, source)
        == sum(
            (Fraction(1, denominator) for denominator in source_solution),
            Fraction(),
        ),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"authoritative nonlinear bridge failed: {failed}")
    return {
        "input_artifact": BRIDGE_ARTIFACT.name,
        "input_sha256": artifact_sha256(BRIDGE_ARTIFACT),
        "shift": shift,
        "source_denominator": source,
        "R": R,
        "E": bridge,
        "E_mod_n_remainder": linear_remainder,
        "K": K,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "source_term": source_term,
        "bridge_divisor": bridge_divisor,
        "source_normalization": normalization,
        "target_certificate": asdict(certificate),
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def general_B_linear_bridge_audit(prime: int) -> dict[str, object]:
    """Replay a linear general-B bridge that isolates the B=1 boundary."""
    a = 4
    shift = 3_705
    R = 59
    bridge = 218_596
    K = 12_951_813
    A, B, C = 2, 7, 16_669
    H = 111
    gap = 55_375
    source = prime - shift
    source_term = source * K // bridge
    square_divisor = B * B * C
    certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
    if certificate is None:
        raise AssertionError("general-B linear certificate did not reconstruct")
    target_solution = [certificate.x, certificate.y, certificate.z]
    source_solution = [source_term, certificate.x, certificate.y]
    normalization = source_normalization(source, bridge)
    conditions = {
        "B_exceeds_one": B > 1,
        "linear_source_identity": (
            source == a * bridge
            and source % bridge == 0
            and prime == a + shift + a * shift * R
        ),
        "normalized_beta_equals_one": normalization["beta"] == 1,
        "E_equals_sR_plus_one": bridge == shift * R + 1,
        "K_reconstructs": 4 * K == prime * R + 1,
        "square_divisor_divides_K_squared": (K * K) % square_divisor == 0,
        "general_B_target_condition": (4 * square_divisor + 1) % R == 0,
        "normal_form_reconstructs": (
            B * C * H == K
            and H == A * R - B
            and gap * R == 4 * square_divisor + 1
            and prime == 4 * A * B * C - gap
            and math.gcd(A, B) == 1
        ),
        "gap_is_natural": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "source_term_reconstructs": source_term * bridge == source * K,
        "target_identity": Fraction(4, prime)
        == sum(
            (Fraction(1, denominator) for denominator in target_solution),
            Fraction(),
        ),
        "source_identity": Fraction(4, source)
        == sum(
            (Fraction(1, denominator) for denominator in source_solution),
            Fraction(),
        ),
    }
    if not all(conditions.values()):
        failed = [name for name, passed in conditions.items() if not passed]
        raise AssertionError(f"general-B linear bridge failed: {failed}")
    return {
        "a": a,
        "shift": shift,
        "source_denominator": source,
        "R": R,
        "E": bridge,
        "K": K,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "square_divisor": square_divisor,
        "source_term": source_term,
        "source_normalization": normalization,
        "target_certificate": asdict(certificate),
        "target_solution": target_solution,
        "source_solution": source_solution,
        "conditions": conditions,
    }


def run_audit() -> dict[str, object]:
    """Run the complete counterexample audit and its positive controls."""
    prime = PRIME
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise AssertionError("target is not a core prime")
    bound, pairs, states = enumerate_linear_states(prime)
    targets = target_audits(prime, states)
    totals = {
        "search_bound": bound,
        "unordered_parameter_pair_count": len(pairs),
        "oriented_linear_source_state_count": len(states),
        "distinct_R_count": len(targets),
        "target_divisor_count_sum": sum(
            int(target["divisor_count"]) for target in targets
        ),
        "reachable_divisor_residue_count_sum": sum(
            int(target["reachable_divisor_residue_count"]) for target in targets
        ),
        "target_C_hit_count": sum(
            int(target["target_C_hit_count"]) for target in targets
        ),
        "target_H_hit_count": sum(
            int(target["target_H_hit_count"]) for target in targets
        ),
    }
    expected = {
        "search_bound": 541,
        "unordered_parameter_pair_count": 42,
        "oriented_linear_source_state_count": 54,
        "distinct_R_count": 24,
        "target_divisor_count_sum": 1_655,
        "reachable_divisor_residue_count_sum": 1_244,
        "target_C_hit_count": 0,
        "target_H_hit_count": 0,
    }
    if totals != expected or any(
        bool(target["target_reachable"]) for target in targets
    ):
        raise AssertionError("linear shifted-source exclusion totals changed")

    ordinary_tail = ordinary_tail_and_prefix_audit(prime)
    nonlinear_bridge = nonlinear_b1_bridge_audit(prime)
    general_B_linear_bridge = general_B_linear_bridge_audit(prime)
    return {
        "arithmetic": (
            "for p=878089, E|n and E=sR+1 imply p=a+s+asR; enumerate "
            "u=min(a,s)<=floor(sqrt((p-2)/3)), factor every p-u, and recover "
            "all divisor states p-u=v(1+uR); orient every odd s, then for each "
            "induced R factor K=(pR+1)/4 and exhaust every B=1 divisor C|K "
            "against 4C=-1 mod R; independently recompute the ordinary Type II "
            "tail miss, replay the stored nonlinear upper-half B=1 bridge, and "
            "replay a linear general-B positive control"
        ),
        "scope_note": (
            "This globally excludes the E|n branch only for B=1 shifted-source "
            "maximum-tail realizations at p=878089. It refutes the proposed B=1 "
            "linear strengthening, not the adaptive B=1 selector, the general-B "
            "mixed terminal selector, or the Erdos-Straus conjecture. First means "
            "first within the stored ordinary-tail-miss prefix named in the output."
        ),
        "prime": prime,
        "prime_is_core": True,
        "completeness_argument": {
            "identity": "p=a+s+a*s*R",
            "bound": "min(a,s)^2 <= a*s <= (p-2)/3",
            "enumeration": "for u=min(a,s), enumerate d=1+u*R dividing p-u and set v=(p-u)/d",
        },
        "candidate_totals": totals,
        "unordered_parameter_pairs": pairs,
        "oriented_linear_source_states": states,
        "target_modulus_audits": targets,
        "ordinary_type_ii_tail_and_stored_prefix": ordinary_tail,
        "successful_nonlinear_upper_B_eq_1_bridge": nonlinear_bridge,
        "successful_general_B_linear_bridge": general_B_linear_bridge,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "unordered_parameter_pairs",
            "oriented_linear_source_states",
            "target_modulus_audits",
        }
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
