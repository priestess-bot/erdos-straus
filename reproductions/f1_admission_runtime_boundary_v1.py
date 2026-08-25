#!/usr/bin/env python3
"""Replay the F1 boundary between legacy arithmetic receipts and v1 runtime.

This is a negative-control reproducer.  It deliberately does not call the
selector runtime to manufacture an edge.  It checks that legacy arithmetic
descriptors fail before common header extraction, while the proposed adapter
boundary remains explicit.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_state_v1 as state_contract  # noqa: E402
import type_i_overflow_total_cofactor_typed_adapter as total_cofactor  # noqa: E402
import type_i_representation_dual_capacity_selector as dual  # noqa: E402
import type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier as h4  # noqa: E402


def _legacy_source(function: Callable[..., dict[str, Any]], payload: dict[str, Any]) -> dict[str, Any]:
    result = function(payload)
    rows = result.get("verified_receipts")
    if isinstance(rows, list) and rows:
        row = rows[0]
        if isinstance(row, dict) and isinstance(row.get("source_state"), dict):
            return dict(row["source_state"])
    if isinstance(result.get("source_state"), dict):
        return dict(result["source_state"])
    raise AssertionError(f"{function.__name__} did not expose a legacy source descriptor")


def _expect_header_rejection(name: str, raw: dict[str, Any]) -> dict[str, Any]:
    try:
        state_contract.extract_verified_selector_header_v1(raw, {})
    except state_contract.StateContractError as exc:
        return {
            "name": name,
            "rejected": True,
            "reason_code": exc.code.value,
            "detail": exc.detail,
        }
    raise AssertionError(f"legacy descriptor unexpectedly passed header extraction: {name}")


def build_report() -> dict[str, Any]:
    payload = json.loads(dual.OVERFLOW_INPUT.read_text(encoding="utf-8"))
    legacy_functions = (
        dual.overflow_fixed_n_outer_rank,
        dual.overflow_fixed_s_bounded_divisor_outer_rank,
        dual.overflow_fixed_s_outer_rank,
        dual.smooth23_k_one_fixed_n_saturation,
        dual.smooth23_low_k_fixed_n_cofactor,
        dual.verified_fixed_n_edge,
    )
    # Keep the extraction fixtures explicit because the two smooth functions
    # have a different top-level return shape from the overflow menu.
    legacy_sources: list[tuple[str, dict[str, Any]]] = []
    for function in legacy_functions:
        if function.__name__.startswith("smooth23_"):
            result = function()
            if function.__name__ == "smooth23_k_one_fixed_n_saturation":
                raw = result["receipts"][0]["source_state"]
            else:
                raw = result["seeds"][0]["checked_rows"][0]["source_state"]
            legacy_sources.append((function.__name__, dict(raw)))
        else:
            legacy_sources.append((function.__name__, _legacy_source(function, payload)))
    legacy_rejections = [_expect_header_rejection(name, raw) for name, raw in legacy_sources]

    source = total_cofactor.fixture_source(3, 45, 15, 37)
    total_cofactor_rejection = _expect_header_rejection("total_cofactor_fixture_source", source)

    h4_target = h4.verify_h4_macro(h4.make_control_input(**h4.CONTROL_FIXTURES[0]))["target"]
    h4_rejection = _expect_header_rejection("h4_pending_dispatch_target", h4_target)

    return {
        "schema_version": 1,
        "artifact_id": "f1_admission_runtime_boundary_v1",
        "legacy_descriptor_count": len(legacy_rejections),
        "legacy_descriptor_rejections": legacy_rejections,
        "total_cofactor_rejection": total_cofactor_rejection,
        "h4_rejection": h4_rejection,
        "runtime_authority_boundary": {
            "legacy_outputs_are_runtime_issued_candidates": False,
            "legacy_outputs_are_persistent_selector_states": False,
            "direct_queue_admission_allowed": False,
            "required_bridge": "SourceExecutionContextV1 -> registered scheduler -> CandidateTransitionV1 -> projector -> independent E1-E4 validator -> common admission"
        },
        "status": "BOUNDARY_CONFIRMED_NO_DIRECT_ADMISSION",
    }


def verify() -> None:
    report = build_report()
    if report["legacy_descriptor_count"] != 6:
        raise AssertionError("representation-dual legacy descriptor count changed")
    if not all(row["rejected"] for row in report["legacy_descriptor_rejections"]):
        raise AssertionError("a legacy descriptor crossed the common header boundary")
    if not report["total_cofactor_rejection"]["rejected"]:
        raise AssertionError("total-cofactor fixture crossed the common header boundary")
    if not report["h4_rejection"]["rejected"]:
        raise AssertionError("H4 pending target crossed the common header boundary")
    if report["runtime_authority_boundary"]["direct_queue_admission_allowed"]:
        raise AssertionError("legacy arithmetic output acquired queue authority")
    print("verified F1 legacy arithmetic boundary: no direct runtime admission")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.verify:
        verify()
    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True))
    if not args.verify and not args.json:
        parser.error("use --verify or --json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
