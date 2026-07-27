#!/usr/bin/env python3
"""Close H19 residuals by r<=103 lifts or p-minus-one scaled lifts."""

from __future__ import annotations

import argparse
import gc
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-hybrid-small-r-p-minus-one-descent-1b-results.json"
R_CAP = 103
DEFAULT_CHUNK_SIZE = 10


def load_script():
    spec = importlib.util.spec_from_file_location(
        "hybrid_small_r_p_minus_one", P_MINUS_ONE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {P_MINUS_ONE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p_minus_one = load_script()


def stage_at_cap(payload: dict[str, object], r_cap: int) -> dict[str, object]:
    """Return the stored bounded-r selector stage."""
    for stage in payload["stages"]:
        if int(stage["r_cap"]) == r_cap:
            return stage
    raise ValueError(f"missing r={r_cap} selector stage")


def run_audit(
    boundary_payload: dict[str, object], chunk_size: int = DEFAULT_CHUNK_SIZE
) -> dict[str, object]:
    """Stream the p-minus-one audit over the exact r<=103 residual."""
    if chunk_size < 1:
        raise ValueError("chunk size must be positive")
    stage = stage_at_cap(boundary_payload, R_CAP)
    residual = [int(prime) for prime in stage["uncovered_primes"]]
    records: list[dict[str, object]] = []
    candidate_count = 0
    tail_divisor_test_count = 0
    hit_candidate_count = 0

    for start in range(0, len(residual), chunk_size):
        partial = p_minus_one.audit_primes(residual[start : start + chunk_size])
        records.extend(partial["records"])
        candidate_count += int(partial["unique_scaled_source_candidate_count"])
        tail_divisor_test_count += int(partial["tail_divisor_test_count"])
        hit_candidate_count += int(partial["hit_candidate_count"])
        # Factorization and divisor enumeration are intentionally large here.
        # Clear SymPy's process-wide caches between independent residual chunks.
        del partial
        gc.collect()
        p_minus_one.candidates.sympy.core.cache.clear_cache()

    if {int(record["prime"]) for record in records} != set(residual):
        raise AssertionError("streamed p-minus-one audit lost a residual prime")
    unclosed = [
        int(record["prime"]) for record in records if record["first_witness"] is None
    ]
    return {
        "arithmetic": (
            "set-exact composition of the r<=103 compatible-ray audit and "
            "streamed complete b=2,4 p-minus-one candidate/tail enumeration "
            "with exact rational and Type I certificate verification"
        ),
        "scope_note": (
            "A finite H19 closure over stored p<=10^9 residuals. It does not "
            "prove a universal r bound or p-minus-one selector."
        ),
        "prime_limit": boundary_payload["prime_limit"],
        "r_cap": R_CAP,
        "h19_residual_count": boundary_payload["h19_residual_count"],
        "bounded_r_strict_lift_count": int(stage["covered_count"]),
        "p_minus_one_residual_count": len(residual),
        "p_minus_one_scaled_source_candidate_count": candidate_count,
        "p_minus_one_tail_divisor_test_count": tail_divisor_test_count,
        "p_minus_one_hit_candidate_count": hit_candidate_count,
        "p_minus_one_strict_lift_count": len(residual) - len(unclosed),
        "unclosed_primes": unclosed,
        "p_minus_one_records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary", type=Path, default=BOUNDARY_INPUT)
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    boundary_payload = json.loads(args.boundary.read_text(encoding="utf-8"))
    result = run_audit(boundary_payload, args.chunk_size)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
