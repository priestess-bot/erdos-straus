#!/usr/bin/env python3
"""Replay the q=1 full-carrier first-child ABSORB entry interface."""

from __future__ import annotations

import argparse
import sys
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_runtime_v1 as runtime  # noqa: E402
import type_ii_q_one_full_carrier_phase_root_entry as q_one  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


ADAPTER = "q_one_full_carrier_first_child_absorb_entry_v1"


def _charged_potential(prime: int, root_k: int) -> tuple[int, ...]:
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


def _absorb_potential(prime: int, target_r: int) -> tuple[int, ...]:
    return runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="ABSORB",
            absorb_m=1,
            absorb_r_epsilon=1,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "ABSORB",
            "chart_R": target_r,
            "absorb_m": 1,
            "absorb_r_epsilon": 1,
        },
        root_context=prime,
        equation_rank=prime,
    )


def first_child_absorb_entry(prime: int) -> dict[str, object]:
    """Recompute the pre-admission ABSORB projection on a terminal MISS."""
    phase_root = q_one.phase_root_entry(prime)
    root = dict(phase_root["root"])
    dispatch = rail.full_carrier_dispatch(prime)
    t = (prime - 1) // 24
    root_r, root_k = int(root["chart"]["R"]), int(root["chart"]["K"])
    target = dict(dispatch["dispatch"])
    target_r, target_k, support = (
        int(target["R"]),
        int(target["K"]),
        int(target["support"]),
    )
    root_source = q_one.universal_root_source(prime, root_r, root_k)
    target_source = q_one.universal_root_source(prime, target_r, target_k)
    bundle = int(dispatch["full_external_bundle"])

    if not (
        root_r == 16 * t + 3
        and root_k == (6 * t + 1) * (16 * t + 1)
        and bundle == root_r - 1 == 16 * t + 2
        and gcd(bundle, root_k) == 1
        and root_source["destination"] == [1, root_r - 1, 1]
        and target_source["destination"] == [1, target_r - 1, 1]
        and 3 <= target_r < prime
        and 4 * target_k == prime * target_r + 1
        and target_k % support == 0
    ):
        raise AssertionError("full-carrier source or target formula changed")

    if t % 2:
        if not (
            target["kind"] == "marked_absorb"
            and target_r == 20 * t + 3
            and target_k == (8 * t + 1) * (15 * t + 1)
            and support == 16 * t + 2
        ):
            raise AssertionError("odd first-child ABSORB formula changed")
        branch = "odd_complete_excess"
    else:
        overflow = dict(dispatch["overflow"])
        if not (
            target["kind"] == "fixed_n_edge"
            and overflow
            == {
                "R": 52 * t + 7,
                "K": (16 * t + 2) * ((39 * t + 2) // 2),
                "n": 12 * t + 1,
                "d": 9 * t // 2,
            }
            and target_r == 6 * t - 1
            and target_k == (9 * t // 2) * (8 * t - 1)
            and support == 9 * t // 2
        ):
            raise AssertionError("even first-child ABSORB formula changed")
        branch = "even_fixed_n_fold"

    source_potential = _charged_potential(prime, root_k)
    target_potential = _absorb_potential(prime, target_r)
    runtime.verify_t5_ticket_v1("PHASE_DROP", source_potential, target_potential)

    return {
        "adapter": ADAPTER,
        "prime": prime,
        "branch": branch,
        "parent": {
            "chart": {"R": root_r, "K": root_k},
            "protocol": "CHARGED",
            "bundle": bundle,
            "source": root_source,
        },
        "target": {
            "chart": {"R": target_r, "K": target_k},
            "support_A": support,
            "major_phase": "TYPEI",
            "type_i_protocol": "ABSORB",
            "provenance_kind": "MARKED_ABSORB",
            "is_overflow": False,
            "source": target_source,
            "cursor": {"formal_pair": [1, target_r - 1, 1], "epsilon": "min"},
            "absorb_m": 1,
            "absorb_r_epsilon": 1,
        },
        "contract_status": {
            "E1": "relative_to_admitted_parent_bundle_and_terminal_miss",
            "E2": True,
            "E3_pre_admission": True,
            "E4": "identity: Sol(p) -> Sol(p)",
            "E5": "PHASE_DROP",
            "reentry": "open",
        },
        "potentials": {"parent": source_potential, "target": target_potential},
    }


def verify() -> None:
    controls = {prime: first_child_absorb_entry(prime) for prime in (73, 241, 2521, 118801)}
    expected = {
        73: ("odd_complete_excess", 63, 1150, 50),
        241: ("even_fixed_n_fold", 59, 3555, 45),
        2521: ("odd_complete_excess", 2103, 1325416, 1682),
        118801: ("even_fixed_n_fold", 29699, 882067725, 22275),
    }
    for prime, entry in controls.items():
        branch, target_r, target_k, support = expected[prime]
        target = entry["target"]
        if not (
            entry["branch"] == branch
            and target["chart"] == {"R": target_r, "K": target_k}
            and target["support_A"] == support
            and target["cursor"] == {"formal_pair": [1, target_r - 1, 1], "epsilon": "min"}
            and entry["potentials"]["parent"] > entry["potentials"]["target"]
        ):
            raise AssertionError(f"ABSORB entry control changed for p={prime}")
    print("verified q=1 full-carrier first-child ABSORB entry")


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
