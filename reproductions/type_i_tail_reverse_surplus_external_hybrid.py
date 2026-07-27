#!/usr/bin/env python3
"""Close the multi-prime reverse-surplus boundary with quadratic external descents."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-500m-results.json"
EXTERNAL = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-500m-results.json"
OFFSET = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-surplus-external-hybrid-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


external_audit = load_module(
    "tail_reverse_surplus_external_audit", ROOT / "reproductions" / "type_ii_tail_deflation_external_boundary.py"
)
offset_profile = load_module(
    "tail_reverse_surplus_offset_profile", ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py"
)


def run_audit(profile: dict[str, object], external: dict[str, object], offset: dict[str, object]) -> dict[str, object]:
    """Rebuild an independent external strict descent for every multi-prime residual."""
    residuals = [int(prime) for prime in profile["single_surplus_misses"]]
    if len(residuals) != 34:
        raise ValueError("input must be the verified 34-point multi-prime surplus boundary")
    external_records = {int(record["prime"]): record for record in external["records"]}
    offset_records = {int(record["prime"]): record for record in offset["records"]}
    missing_external = sorted(set(residuals) - set(external_records))
    if missing_external:
        raise AssertionError(f"boundary points absent from external audit: {missing_external}")
    spf = external_audit.targeted_descent.TrialSmallestFactors(max(residuals))
    records: list[dict[str, object]] = []
    direct_count = 0
    shifted_count = 0
    for prime in residuals:
        stored_direct = external_records[prime]["quadratic_factor_descent"]
        rebuilt_direct = external_audit.serialize_witness(
            external_audit.short_certificate.quadratic_factor_external_source_descent_witness(prime, spf)
        )
        if rebuilt_direct != stored_direct:
            raise AssertionError("stored zero-offset quadratic witness did not rebuild")
        if rebuilt_direct is not None:
            direct_count += 1
            records.append(
                {
                    "prime": prime,
                    "branch": "zero_offset_quadratic_external",
                    "external_descent": rebuilt_direct,
                }
            )
            continue
        stored_offset = offset_records.get(prime, {}).get("offset_descent")
        if stored_offset is None:
            raise AssertionError("quadratic residual had no stored shifted external descent")
        witness, shift, candidates = offset_profile.first_offset_witness(prime, spf, int(stored_offset["shift"]))
        if witness is None or shift != int(stored_offset["shift"]):
            raise AssertionError("least shifted external witness did not rebuild")
        rebuilt_offset = offset_profile.serialize_witness(witness, shift, candidates)
        if rebuilt_offset != stored_offset:
            raise AssertionError("stored shifted external witness did not rebuild")
        shifted_count += 1
        records.append(
            {
                "prime": prime,
                "branch": "shifted_quadratic_external",
                "external_descent": rebuilt_offset,
            }
        )
    shift_histogram: dict[str, int] = {}
    for record in records:
        if record["branch"] != "shifted_quadratic_external":
            continue
        shift = str(record["external_descent"]["shift"])
        shift_histogram[shift] = shift_histogram.get(shift, 0) + 1
    return {
        "arithmetic": (
            "take the exact 34 multi-prime reverse-surplus residuals; rebuild the complete "
            "zero-offset quadratic external witness, then for its misses rebuild every compatible "
            "divisor state through the stored first shifted offset, with exact rational verification"
        ),
        "scope_note": (
            "A finite hybrid closure of a target-side reverse-selector boundary by independent "
            "external-source descents. It does not yield a global source-side selector."
        ),
        "prime_limit": profile["prime_limit"],
        "input_multi_prime_boundary_count": len(residuals),
        "zero_offset_quadratic_external_count": direct_count,
        "shifted_quadratic_external_count": shifted_count,
        "shifted_offset_histogram": dict(sorted(shift_histogram.items(), key=lambda item: int(item[0]))),
        "unclosed_primes": [],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--external", type=Path, default=EXTERNAL)
    parser.add_argument("--offset", type=Path, default=OFFSET)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.profile.read_text(encoding="utf-8")),
        json.loads(args.external.read_text(encoding="utf-8")),
        json.loads(args.offset.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
