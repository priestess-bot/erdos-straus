#!/usr/bin/env python3
"""Close 1b H19 residuals by quadratic descent or a bounded-r even-source lift."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTIVE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_adaptive_even_source_descent.py"
QUADRATIC_SCRIPT = ROOT / "reproductions" / "type_ii_h19_hybrid_short_or_descent.py"
DEFAULT_DESCENT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_SMALL_R = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-hybrid-small-r-descent-1b-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


adaptive = load_script("type_ii_h19_hybrid_small_r_adaptive", ADAPTIVE_SCRIPT)
hybrid = load_script("type_ii_h19_hybrid_small_r_quadratic", QUADRATIC_SCRIPT)


def serialize_witness(witness) -> dict[str, object]:
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "source_solution": list(witness.source_solution),
        "target_solution": list(witness.target_solution),
        "certificate": {
            "type": witness.certificate.certificate_type,
            "gap": witness.certificate.gap,
            "x": witness.certificate.x,
            "divisor": witness.certificate.divisor,
            "y": witness.certificate.y,
            "z": witness.certificate.z,
        },
    }


def run_audit(
    descent_payload: dict[str, object], small_r_payload: dict[str, object]
) -> dict[str, object]:
    """Verify every quadratic miss through its first bounded-r source lift."""
    records = descent_payload["records"]
    pressures = {
        int(row["prime"]): row["first_small_r_tail_hit"]
        for row in small_r_payload["records"]
    }
    spf = adaptive.targeted.TrialSmallestFactors(
        max(int(row["prime"]) for row in records)
    )
    small_r_records: list[dict[str, object]] = []
    quadratic_count = 0
    unclosed: list[int] = []
    for record in records:
        prime = int(record["prime"])
        quadratic = record["quadratic_factor_external_source_descent"]
        if quadratic is not None:
            hybrid.verify_descent(prime, quadratic)
            quadratic_count += 1
            continue
        state = pressures.get(prime)
        if state is None:
            unclosed.append(prime)
            continue
        r = int(state["r"])
        selected_ray = state["compatible_rays"][0]
        distance = int(selected_ray["distance"])
        divisor = int(selected_ray["d"])
        witness = adaptive.short_certificate.even_source_distance_descent_witness(
            prime, distance, spf
        )
        if witness is None:
            raise AssertionError("small-r state did not reconstruct an even-source lift")
        adaptive.verify_witness(prime, distance, witness)
        if witness.q != divisor * r or witness.k != (divisor * r + 1) // 4:
            raise AssertionError("reconstructed lift disagrees with the selected r state")
        small_r_records.append(
            {
                "prime": prime,
                "r": r,
                "distance": distance,
                "d": divisor,
                "witness": serialize_witness(witness),
            }
        )
    if set(pressures) != {row["prime"] for row in small_r_records}:
        raise AssertionError("bounded-r profile and quadratic misses disagree")
    return {
        "arithmetic": (
            "exact rational verification of every quadratic lift and every "
            "bounded-r even-source source/target lift"
        ),
        "scope_note": (
            "A finite H19 closure over stored 1b residuals. It does not "
            "establish a universal r bound or descent selector."
        ),
        "prime_limit": descent_payload["prime_limit"],
        "r_cap": small_r_payload["r_cap"],
        "h19_residual_count": len(records),
        "quadratic_descent_count": quadratic_count,
        "bounded_r_even_source_count": len(small_r_records),
        "unclosed_primes": unclosed,
        "bounded_r_records": small_r_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--descent", type=Path, default=DEFAULT_DESCENT)
    parser.add_argument("--small-r", type=Path, default=DEFAULT_SMALL_R)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    descent_payload = json.loads(args.descent.read_text(encoding="utf-8"))
    small_r_payload = json.loads(args.small_r.read_text(encoding="utf-8"))
    result = run_audit(descent_payload, small_r_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
