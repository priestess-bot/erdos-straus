#!/usr/bin/env python3
"""Close the support-four even-bridge boundary with shifted external descents."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"
OFFSET = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-500m-results.json"
OFFSET_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-even-source-support-external-hybrid-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


offset_profile = load_module("even_support_external_offset_profile", OFFSET_PROFILE)


def run_audit(support: dict[str, object], offset: dict[str, object]) -> dict[str, object]:
    boundary = [
        int(record["prime"])
        for record in support["records"]
        if int(record["selected_edge"]["E_prime_support_count"]) >= 4
    ]
    if boundary != [42_622_969, 357_834_409]:
        raise AssertionError("support-four boundary did not reconstruct")
    offset_records = {int(record["prime"]): record for record in offset["records"]}
    spf = offset_profile.targeted_descent.TrialSmallestFactors(max(boundary))
    records: list[dict[str, object]] = []
    for prime in boundary:
        stored = offset_records.get(prime, {}).get("offset_descent")
        if stored is None:
            raise AssertionError("support-four boundary had no shifted external witness")
        witness, shift, candidates = offset_profile.first_offset_witness(prime, spf, int(stored["shift"]))
        if witness is None or shift != int(stored["shift"]):
            raise AssertionError("stored shifted witness did not rebuild")
        rebuilt = offset_profile.serialize_witness(witness, shift, candidates)
        if rebuilt != stored:
            raise AssertionError("stored shifted witness did not match exact reconstruction")
        if int(rebuilt["source_denominator"]) % 2:
            raise AssertionError("shifted external source was not even")
        records.append({"prime": prime, "shifted_external_descent": rebuilt})
    shift_histogram: dict[str, int] = {}
    for record in records:
        shift = str(record["shifted_external_descent"]["shift"])
        shift_histogram[shift] = shift_histogram.get(shift, 0) + 1
    return {
        "arithmetic": (
            "take the exact support-four even-bridge boundary; rebuild every compatible shifted "
            "quadratic external divisor state through its stored first offset and verify the "
            "strict source and target identities"
        ),
        "scope_note": (
            "A finite hybrid replacement for the two support-four bridge factors. It does not "
            "prove a global rule for selecting bridge factors or shifted offsets."
        ),
        "prime_limit": support["prime_limit"],
        "support_at_most_three_even_bridge_count": int(support["captured_count"]) - len(boundary),
        "shifted_external_boundary_count": len(records),
        "shifted_offset_histogram": dict(sorted(shift_histogram.items(), key=lambda item: int(item[0]))),
        "unclosed_primes": [],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--offset", type=Path, default=OFFSET)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.support.read_text(encoding="utf-8")),
        json.loads(args.offset.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
