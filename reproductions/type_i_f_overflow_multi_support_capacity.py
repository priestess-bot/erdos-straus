#!/usr/bin/env python3
"""Stress-test multi-support capacity for relation-lattice overflow witnesses."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
CROSS_SCRIPT = ROOT / "reproductions" / "type_i_f_full_cross_color_pair_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-multi-support-capacity-results.json"

EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
EXPECTED_SUPPORT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_module("multi_support_capacity_base", CAPACITY_SCRIPT)
cross = load_module("multi_support_cross_capacity", CROSS_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    return capacity.valuation(value, prime)


def factor_product(block: int, support: tuple[int, ...]) -> int:
    product = 1
    for q in support:
        product *= valuation(block, q)
    return product


def summarize(groups: list[dict[str, object]], field: str) -> dict[str, object]:
    ratios = [float(group[field]) for group in groups if group[field] is not None]
    overloads = [group for group in groups if group[field] is not None and group[field] > 1]
    return {
        "group_count": len(groups),
        "overload_count": len(overloads),
        "maximum_ratio": max(ratios) if ratios else None,
        "saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_groups": sorted(
            groups,
            key=lambda group: (group[field] is not None, group[field] or -1),
            reverse=True,
        )[:50],
    }


def run() -> dict[str, object]:
    for path, expected, label in (
        (FOURIER_INPUT, EXPECTED_FOURIER_SHA256, "Fourier"),
        (CROSS_INPUT, EXPECTED_CROSS_SHA256, "cross-color"),
        (SUPPORT_INPUT, EXPECTED_SUPPORT_SHA256, "support-boundary"),
    ):
        if sha256(path) != expected:
            raise AssertionError(f"the {label} input changed")

    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross_payload = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    support_payload = json.loads(SUPPORT_INPUT.read_text(encoding="utf-8"))
    Fourier_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in fourier["records"]
    }
    support_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in support_payload["records"]
        if record.get("within_radius_cap")
    }
    unresolved = [dict(record) for record in cross_payload["unresolved_records"]]

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    grouped: dict[tuple[int, tuple[int, ...], tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)
    assignment_count = 0
    support_record_count = 0
    for index, record in enumerate(unresolved, start=1):
        key = (int(record["prime"]), int(record["R"]))
        if key not in support_by_key:
            continue
        Fourier = Fourier_by_key[key]
        if Fourier["status"] != "bounded_fourier_certificate":
            raise AssertionError("support record is not threshold-met")
        prime = key[0]
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        support_record_count += 1
        overflow = support_by_key[key]
        excess_by_q = {
            int(q): int(amount)
            for q, amount in zip(
                (int(q) for q, _exponent in overflow["factorization"]),
                (
                    max(0, abs(int(value)) - int(exponent))
                    for value, (_q, exponent) in zip(
                        overflow["witness_exponents"], overflow["factorization"]
                    )
                ),
            )
        }
        for assignment in cross.cross_color_assignments(Fourier, source_cache[prime]):
            a, s, modulus = int(assignment["a"]), int(assignment["s"]), key[1]
            active_a = int(assignment["q_a"])
            active_s = int(assignment["q_s"])
            factorization = {
                int(q): int(exponent) for q, exponent in Fourier["factorization"]
            }
            required = {
                active_a: int(assignment["required_a"]),
                active_s: int(assignment["required_s"]),
            }
            support_a = {active_a}
            support_s = {active_s}
            for q, excess in excess_by_q.items():
                if not excess:
                    continue
                height_a = valuation(a * modulus + 1, q)
                height_s = valuation(s * modulus + 1, q)
                if q in (active_a, active_s):
                    label = "a" if q == active_a else "s"
                else:
                    label = "a" if height_a >= height_s else "s"
                (support_a if label == "a" else support_s).add(q)
            support_a_tuple = tuple(sorted(support_a))
            support_s_tuple = tuple(sorted(support_s))
            demand_base_a = {
                q: required.get(q, 1) for q in support_a_tuple
            }
            demand_base_s = {
                q: required.get(q, 1) for q in support_s_tuple
            }
            demand_extra_a = {
                q: demand_base_a[q] + excess_by_q.get(q, 0)
                for q in support_a_tuple
            }
            demand_extra_s = {
                q: demand_base_s[q] + excess_by_q.get(q, 0)
                for q in support_s_tuple
            }
            grouped[(prime, support_a_tuple, support_s_tuple)].append(
                {
                    "prime": prime,
                    "R": modulus,
                    "K": int(Fourier["K"]),
                    "support_a": list(support_a_tuple),
                    "support_s": list(support_s_tuple),
                    "base_demand": math.prod(demand_base_a.values())
                    * math.prod(demand_base_s.values()),
                    "overflow_demand": math.prod(demand_extra_a.values())
                    * math.prod(demand_extra_s.values()),
                    "overflow_support_size": sum(excess > 0 for excess in excess_by_q.values()),
                    "active_primes": [active_a, active_s],
                }
            )
            assignment_count += 1
        if index % 50 == 0:
            print(f"processed {index}/{len(unresolved)}", file=sys.stderr)

    groups = []
    for (prime, support_a, support_s), entries in sorted(grouped.items()):
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        base_demand = sum(int(entry["base_demand"]) for entry in entries)
        overflow_demand = sum(int(entry["overflow_demand"]) for entry in entries)
        capacity_value = 0
        state_count = 0
        for modulus, states in source_cache[prime].items():
            if not lo <= modulus <= hi:
                continue
            for a, s in states:
                capacity_value += factor_product(a * modulus + 1, support_a) * factor_product(
                    s * modulus + 1, support_s
                )
                state_count += 1
        groups.append(
            {
                "prime": prime,
                "support_a": list(support_a),
                "support_s": list(support_s),
                "record_count": len(entries),
                "R_min": lo,
                "R_max": hi,
                "base_demand": base_demand,
                "overflow_demand": overflow_demand,
                "capacity": capacity_value,
                "base_ratio": base_demand / capacity_value if capacity_value else None,
                "overflow_ratio": overflow_demand / capacity_value if capacity_value else None,
                "state_count": state_count,
            }
        )

    return {
        "arithmetic": (
            "For every split-color overflow witness found within radius six, assign inactive "
            "overflow primes to the higher U/V carrier and form a joint support pattern. Compare "
            "the product of base/overflow height demands with the exact same-R multi-support "
            "capacity over complete linear source states."
        ),
        "scope_note": (
            "Conditional stress test only. It assumes each overflow excess can be charged to the "
            "chosen carrier block and uses a deterministic tie rule; this arithmetic mapping is "
            "not proved. Missing witnesses and alternative carrier assignments are not negative "
            "certificates."
        ),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_input": CROSS_INPUT.name,
        "cross_input_sha256": sha256(CROSS_INPUT),
        "support_input": SUPPORT_INPUT.name,
        "support_input_sha256": sha256(SUPPORT_INPUT),
        "unresolved_record_count": len(unresolved),
        "support_record_count": support_record_count,
        "assignment_count": assignment_count,
        "group_count": len(groups),
        "base_capacity": summarize(groups, "base_ratio"),
        "overflow_capacity": summarize(groups, "overflow_ratio"),
        "groups": groups,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "unresolved_record_count",
                    "support_record_count",
                    "assignment_count",
                    "group_count",
                    "base_capacity",
                    "overflow_capacity",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
