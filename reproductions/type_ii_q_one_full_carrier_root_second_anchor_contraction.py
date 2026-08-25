#!/usr/bin/env python3
"""Replay q=1 root-to-final second-anchor checkpoint contraction."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_runtime_v1 as runtime  # noqa: E402
import type_ii_q_one_full_carrier_phase_root_entry as q_one  # noqa: E402
import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as second_anchor  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


ADAPTER = "q_one_full_carrier_root_second_anchor_contraction_v1"


def root_potential(prime: int, root_k: int) -> tuple[int, ...]:
    return runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "support_A": 1,
            "chart_K": root_k,
            "t5_eta_p": 0,
        },
        root_context=prime,
        equation_rank=prime,
    )


def final_projection(
    prime: int, target_r: int, target_k: int, support: int
) -> tuple[dict[str, object], runtime.T5StateDescriptorV1, str]:
    if target_r > prime:
        facts: dict[str, object] = {
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "provenance_kind": "OVERFLOW",
            "is_overflow": True,
            "support_A": support,
            "chart_R": target_r,
            "chart_K": target_k,
            "t5_eta_p": 0,
        }
        descriptor = runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        )
        return facts, descriptor, "LOCAL_DROP"

    target_source = q_one.universal_root_source(prime, target_r, target_k)
    if target_source["destination"] != [1, target_r - 1, 1]:
        raise AssertionError("low final target lost its universal cursor")
    facts = {
        "major_phase": "TYPEI",
        "type_i_protocol": "ABSORB",
        "provenance_kind": "MARKED_ABSORB",
        "is_overflow": False,
        "support_A": support,
        "chart_R": target_r,
        "chart_K": target_k,
        "absorb_m": 1,
        "absorb_r_epsilon": 1,
    }
    descriptor = runtime.T5StateDescriptorV1(
        induction_rank=prime,
        major_phase="TYPEI",
        type_i_protocol="ABSORB",
        absorb_m=1,
        absorb_r_epsilon=1,
    )
    return facts, descriptor, "PHASE_DROP"


def root_second_anchor_contraction(prime: int) -> dict[str, object]:
    """Compute the final macro target without queueing its two checkpoints."""
    if not (rail.is_prime(prime) and prime % 24 == 1):
        raise AssertionError("contraction requires a core prime")
    t = (prime - 1) // 24
    if not rail.q_one_g(6 * t + 1):
        raise AssertionError("contraction applies only to an ordinary q=1 G root")
    root = dict(rail.full_carrier_dispatch(prime)["root"])
    row = second_anchor.odd_macro(t) if t % 2 else second_anchor.even_macro(t)
    child = dict(row["parent"])
    final = dict(row["target"])
    root_r, root_k = int(root["R"]), int(root["K"])
    child_r, child_k, child_a = (
        int(child["R"]),
        int(child["K"]),
        int(child["support"]),
    )
    target_r, target_k, support = (
        int(final["R"]),
        int(final["K"]),
        int(final["support"]),
    )
    rail_child = rail.full_carrier_dispatch(prime)["dispatch"]
    if not (
        root == {"p": prime, "X": 6 * t + 1, "carrier": 6 * t + 1, "z": 0, "R": root_r, "K": root_k, "overlap": 6 * t + 1}
        and root_r == 16 * t + 3
        and root_k == (6 * t + 1) * (16 * t + 1)
        and (child_r, child_k, child_a)
        == (int(rail_child["R"]), int(rail_child["K"]), int(rail_child["support"]))
        and row["e1_e5"]["E1"]
        and row["e1_e5"]["E2"]
        and row["e1_e5"]["E3"]
        and row["e1_e5"]["E4"]
        and row["e1_e5"]["E5"]
        and 4 * target_k == prime * target_r + 1
        and target_k % support == 0
        and support > 1
    ):
        raise AssertionError("root-to-final macro arithmetic changed")

    target_facts, descriptor, ticket = final_projection(
        prime, target_r, target_k, support
    )
    parent_potential = root_potential(prime, root_k)
    target_potential = runtime.compute_t5_potential_v1(
        descriptor=descriptor,
        facts=target_facts,
        root_context=prime,
        equation_rank=prime,
    )
    runtime.verify_t5_ticket_v1(ticket, parent_potential, target_potential)

    return {
        "adapter": ADAPTER,
        "prime": prime,
        "t": t,
        "persistent_parent": {"R": root_r, "K": root_k, "support": 1},
        "checkpoints": {
            "first_child": {"R": child_r, "K": child_k, "support": child_a},
            "second_anchor_high_determinant": row["transient_overflow"],
            "queued": False,
        },
        "final_target": {
            "R": target_r,
            "K": target_k,
            "support": support,
            "facts": target_facts,
            "ticket": ticket,
        },
        "contract_status": {
            "E1": "relative_to_actual_root_path_and_terminal_misses",
            "E2": True,
            "E3_pre_admission": True,
            "E4": "identity: Sol(p) -> Sol(p)",
            "E5": ticket,
            "reentry": "open",
        },
        "potentials": {"root": parent_potential, "final": target_potential},
    }


def verify() -> None:
    controls = {
        prime: root_second_anchor_contraction(prime)
        for prime in (73, 241, 601, 2521, 118801)
    }
    expected = {
        73: (231, 4216, 62, "LOCAL_DROP", "OVERFLOW"),
        241: (3119, 187920, 1305, "LOCAL_DROP", "OVERFLOW"),
        601: (431, 64758, 502, "PHASE_DROP", "MARKED_ABSORB"),
        2521: (6607, 4164062, 2102, "LOCAL_DROP", "OVERFLOW"),
        118801: (831599, 24698698200, 690525, "LOCAL_DROP", "OVERFLOW"),
    }
    for prime, receipt in controls.items():
        target = receipt["final_target"]
        target_r, target_k, support, ticket, provenance = expected[prime]
        if not (
            (target["R"], target["K"], target["support"])
            == (target_r, target_k, support)
            and target["ticket"] == ticket
            and target["facts"]["provenance_kind"] == provenance
            and receipt["potentials"]["root"] > receipt["potentials"]["final"]
        ):
            raise AssertionError(f"root contraction control changed for p={prime}")
    print("verified q=1 root-to-second-anchor checkpoint contraction")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
