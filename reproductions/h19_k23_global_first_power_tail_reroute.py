#!/usr/bin/env python3
"""Reroute same-tail prime-power misses to later first-power global tail witnesses."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_PROFILE_INPUT = ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-first-power-tail-reroute-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
POWER_PROFILE = ROOT / "reproductions" / "h19_k23_global_one_prime_power_descent_profile.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_first_power_reroute_global", GLOBAL_CLOSURE)
power_profile = load_module("h19_k23_first_power_reroute_profile", POWER_PROFILE)


def later_first_power_witness(
    prime: int, current_gap: int, bases: dict[int, set[int]]
) -> tuple[int, int] | None:
    """Return the first later global tail with a one-nonbase-prime first-power witness."""
    for gap in sorted(gap for gap in bases if gap > current_gap):
        divisor = power_profile.first_power_one_witness(prime, gap, bases[gap])
        if divisor is not None:
            return gap, divisor
    return None


def run_audit(profile_payload: dict[str, object]) -> dict[str, object]:
    """Keep same-tail first powers and reroute each remaining record to a later tail."""
    _, bases = global_closure.global_tail_bases()
    same_tail_count = 0
    reroutes = []
    final_tail_histogram: Counter[int] = Counter()
    for row in profile_payload["records"]:
        prime = int(row["prime"])
        current_gap = int(row["tail_gap"])
        divisor = row["first_power_one_witness"]
        if divisor is not None:
            divisor = int(divisor)
            verified = power_profile.profile_witness(
                prime,
                current_gap,
                divisor,
                {int(factor) for factor in row["base_primes"]},
                "same-tail-first-power",
            )
            if int(verified["new_prime_exponent"]) != 1:
                raise AssertionError("stored first-power witness is not first power")
            same_tail_count += 1
            final_tail_histogram[current_gap] += 1
            continue
        selected = later_first_power_witness(prime, current_gap, bases)
        if selected is None:
            raise AssertionError("prime-power row has no later global first-power rescue")
        new_gap, new_divisor = selected
        verified = power_profile.profile_witness(
            prime,
            new_gap,
            new_divisor,
            bases[new_gap],
            "later-tail-first-power",
        )
        if int(verified["new_prime_exponent"]) != 1:
            raise AssertionError("later-tail witness is not first power")
        final_tail_histogram[new_gap] += 1
        reroutes.append(
            {
                "prime": prime,
                "old_tail_gap": current_gap,
                "old_divisor": int(row["divisor"]),
                "old_new_prime": int(row["new_prime"]),
                "old_new_prime_exponent": int(row["new_prime_exponent"]),
                "new_tail_gap": new_gap,
                "new_divisor": new_divisor,
                "new_prime": int(verified["new_prime"]),
                "source_denominator": int(verified["source_denominator"]),
            }
        )
    if same_tail_count + len(reroutes) != int(
        profile_payload["final_one_support_count"]
    ):
        raise AssertionError("first-power reroute did not partition the profile")
    return {
        "arithmetic": (
            "for every one-support record, exhaustive first-power divisor enumeration "
            "at its selected tail; only when this is empty, exhaustive increasing "
            "global-tail search with exact Type II and strict two-tail reconstruction"
        ),
        "scope_note": (
            "A complete finite exponent-one reroute of the rewritten portion of the "
            "2097152-layer H19-k23 artifact. It does not prove a global cross-tail "
            "first-power selector."
        ),
        "input_final_one_support_count": profile_payload["final_one_support_count"],
        "same_tail_first_power_count": same_tail_count,
        "later_tail_first_power_reroute_count": len(reroutes),
        "final_first_power_tail_histogram": {
            str(gap): count for gap, count in sorted(final_tail_histogram.items())
        },
        "reroutes": reroutes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-input", type=Path, default=DEFAULT_PROFILE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    profile_payload = json.loads(args.profile_input.read_text(encoding="utf-8"))
    result = run_audit(profile_payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "reroutes"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
