#!/usr/bin/env python3
"""Replay the canonical high-support C=1 dual handoff algebra.

This verifier checks deterministic target equations only. It intentionally
does not fabricate a parent source receipt, terminal-first result, generic
ABSORB owner, or recursive re-entry.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = (
    ROOT
    / "data"
    / "t6-wave1"
    / "f2-high-support-c1-canonical-dual-absorb-handoff-v1.json"
)


def build_row(prime: int, support: int) -> dict[str, int]:
    """Reconstruct both symmetric dual charts from one C=1 high chart."""
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise AssertionError("control prime is outside the core domain")
    bound = (prime - 1) ** 2 // 4
    if support <= bound or (4 * support - 1) % prime:
        raise AssertionError("source is not a high-support C=1 chart")
    R = (4 * support - 1) // prime
    if not (prime < R < 4 * support and R % 4 == 3):
        raise AssertionError("source canonical chart changed")

    alpha = (3 * prime + 1) // 4
    k, residue = divmod(support, prime)
    if residue != alpha or R != 4 * k + 3:
        raise AssertionError("C=1 canonical residue normal form changed")

    M = support
    d = prime - 1
    n = (prime - 1) * R + 1
    if prime * n != 4 * M * d + 1 or 4 * M - n != R:
        raise AssertionError("derived determinant identity changed")
    s = n - 4 * k * d
    if s != 3 * prime - 2:
        raise AssertionError("symmetric-dual remainder changed")

    R_d, K_d = 4 * d - s, d * (prime - alpha)
    R_alpha, K_alpha = 4 * alpha - s, alpha * (prime - d)
    if (R_d, K_d) != (prime - 2, bound):
        raise AssertionError("d-side universal dual changed")
    if (R_alpha, K_alpha) != (3, alpha):
        raise AssertionError("R=3 canonical dual changed")
    if prime * R_d + 1 != 4 * K_d or prime * R_alpha + 1 != 4 * K_alpha:
        raise AssertionError("dual chart equation changed")

    return {
        "p": prime,
        "A": support,
        "R": R,
        "alpha": alpha,
        "k": k,
        "M": M,
        "d": d,
        "n": n,
        "s": s,
        "R_d": R_d,
        "K_d": K_d,
        "R_alpha": R_alpha,
        "K_alpha": K_alpha,
    }


def control_row(prime: int) -> dict[str, object]:
    support = (prime + 1) ** 2 // 4
    row = build_row(prime, support)
    result: dict[str, object] = {
        "p": prime,
        "A": support,
        "R": row["R"],
        "alpha_target": [row["R_alpha"], row["K_alpha"], row["K_alpha"]],
        "d_target": [row["R_d"], row["K_d"], row["K_d"]],
    }
    if prime == 241:
        result["r3_control"] = "G; target is not automatically terminal"
    return result


def build_receipt() -> dict[str, object]:
    controls = [control_row(prime) for prime in (73, 97, 241)]
    if controls[2]["alpha_target"] != [3, 181, 181]:
        raise AssertionError("p=241 R=3 G control changed")
    return {
        "artifact_id": "f2_high_support_c1_canonical_dual_absorb_handoff_v1",
        "status": "CONDITIONAL_E2_E4_E5_HANDOFF_E3_REENTRY_OPEN",
        "controls": controls,
        "conclusion": {
            "target": "R=3, K=A=(3p+1)/4",
            "E2": "ESTABLISHED",
            "E4": "IDENTITY_ON_Sol_4_p_RELATIVE_TO_ADMISSION",
            "E5": "CHARGED_TO_ABSORB_PHASE_DROP_RELATIVE_TO_ADMISSION",
            "E3_and_reentry": "OPEN",
        },
    }


def verify() -> dict[str, object]:
    receipt = build_receipt()
    stored = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if stored["artifact_id"] != receipt["artifact_id"]:
        raise AssertionError("stored artifact id changed")
    if stored["status"] != receipt["status"]:
        raise AssertionError("stored status changed")
    if stored["controls"] != receipt["controls"]:
        raise AssertionError("stored handoff controls changed")
    expected_status = {
        "E1": "RELATIVE_TO_ACTUAL_PARENT_AND_NEW_PRODUCER_REGISTRATION",
        "E2": "ESTABLISHED_BY_CANONICAL_DUAL_IDENTITIES",
        "E3": "OPEN_GENERIC_ORDINARY_ABSORB_OWNER_SERIALIZER_AND_CURSOR",
        "E4": "IDENTITY_ON_Sol_4_p_RELATIVE_TO_ADMISSION",
        "E5": "PHASE_DROP_CHARGED_TO_ABSORB_RELATIVE_TO_ADMISSION",
        "reentry": "OPEN",
    }
    if stored["obligation_status"] != expected_status:
        raise AssertionError("stored obligation boundary changed")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    receipt = verify() if args.verify else build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
