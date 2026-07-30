#!/usr/bin/env python3
"""Audit whether conditional overflow charges fit the selected carrier heights."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
CROSS_SCRIPT = ROOT / "reproductions" / "type_i_f_full_cross_color_pair_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-multi-support-height-audit-results.json"

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


capacity = load_module("overflow_height_capacity", CAPACITY_SCRIPT)
cross = load_module("overflow_height_cross", CROSS_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    unresolved = [dict(record) for record in cross_payload["unresolved_records"]]
    assignment_count = 0
    support_record_count = 0
    overflow_layer_count = 0
    layer_height_at_least_excess = 0
    layer_height_at_least_baseline_plus_excess = 0
    assignment_all_excess_supported = 0
    assignment_all_baseline_plus_excess_supported = 0
    assignment_partial_excess_supported: Counter[str] = Counter()
    square_classification_counts: Counter[str] = Counter()
    failed_examples: list[dict[str, object]] = []

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
        excess_by_q = {q: amount for q, amount in excess_by_q.items() if amount}
        if not excess_by_q:
            continue

        for assignment in cross.cross_color_assignments(Fourier, source_cache[prime]):
            assignment_count += 1
            modulus = key[1]
            a, s = int(assignment["a"]), int(assignment["s"])
            U = s * modulus + 1
            V = a * modulus + 1
            if U < V and V % 2 == 1:
                square_classification = "mixed_parity_square_obstruction"
            elif min(U, V) % 2 == 0:
                square_classification = "even_smaller_block_square_terminal"
            else:
                square_classification = "odd_marked_descent"
            X = min(U, V)
            E = X * X
            if square_classification != "mixed_parity_square_obstruction":
                K = int(Fourier["K"])
                if (4 * K * K) % E:
                    raise AssertionError("smaller-block square is not a divisor")
                source, remainder = divmod(U * V - E, modulus)
                if remainder or not (0 < source < key[0]):
                    raise AssertionError("invalid smaller-block square source")
                if E % modulus != 1 or E <= 1 or E >= 4 * K:
                    raise AssertionError("invalid smaller-block square terminal")
                if (source * K) % E:
                    raise AssertionError("smaller-block square does not divide source product")
                if source % 2 != E % 2:
                    raise AssertionError("source parity does not match square parity")
            square_classification_counts[square_classification] += 1
            all_excess = True
            all_baseline_plus_excess = True
            supported_layers = 0
            baseline_supported_layers = 0
            layer_details = []
            for q, excess in sorted(excess_by_q.items()):
                height_a = capacity.valuation(a * modulus + 1, q)
                height_s = capacity.valuation(s * modulus + 1, q)
                if q == int(assignment["q_a"]):
                    color, height, baseline = "a", height_a, int(assignment["required_a"])
                elif q == int(assignment["q_s"]):
                    color, height, baseline = "s", height_s, int(assignment["required_s"])
                elif height_a >= height_s:
                    color, height, baseline = "a", height_a, 1
                else:
                    color, height, baseline = "s", height_s, 1

                overflow_layer_count += excess
                excess_layers = excess if height >= excess else 0
                baseline_layers = excess if height >= baseline + excess else 0
                layer_height_at_least_excess += excess_layers
                layer_height_at_least_baseline_plus_excess += baseline_layers
                supported_layers += excess_layers
                baseline_supported_layers += baseline_layers
                all_excess &= excess_layers == excess
                all_baseline_plus_excess &= baseline_layers == excess
                layer_details.append(
                    {
                        "q": q,
                        "excess": excess,
                        "color": color,
                        "selected_height": height,
                        "baseline": baseline,
                        "height_ge_excess": height >= excess,
                        "height_ge_baseline_plus_excess": height >= baseline + excess,
                    }
                )

            assignment_partial_excess_supported[
                "all" if supported_layers == sum(excess_by_q.values())
                else "some" if supported_layers
                else "none"
            ] += 1
            assignment_all_excess_supported += all_excess
            assignment_all_baseline_plus_excess_supported += all_baseline_plus_excess
            if (not all_excess or not all_baseline_plus_excess) and len(failed_examples) < 20:
                failed_examples.append(
                    {
                        "prime": key[0],
                        "R": key[1],
                        "a": a,
                        "s": s,
                        "q_a": int(assignment["q_a"]),
                        "q_s": int(assignment["q_s"]),
                        "layers": layer_details,
                    }
                )
        if index % 50 == 0:
            print(f"processed {index}/{len(unresolved)}", file=sys.stderr)

    return {
        "arithmetic": (
            "For each deterministic multi-support assignment, compare every overflow excess "
            "layer with the selected carrier's actual q-adic height. The audit tests whether "
            "the conditional overflow charge is already supported by the chosen source block."
        ),
        "scope_note": (
            "This is a local consistency boundary, not a search for alternative assignments. "
            "Failure means the tested deterministic charge is not supplied by the selected "
            "carrier; it does not rule out another carrier or a descent interpretation."
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
        "overflow_layer_count": overflow_layer_count,
        "layer_height_at_least_excess": layer_height_at_least_excess,
        "layer_height_at_least_baseline_plus_excess": layer_height_at_least_baseline_plus_excess,
        "assignment_all_excess_supported": assignment_all_excess_supported,
        "assignment_all_baseline_plus_excess_supported": assignment_all_baseline_plus_excess_supported,
        "assignment_partial_excess_supported": dict(assignment_partial_excess_supported),
        "square_classification_counts": dict(square_classification_counts),
        "failed_examples": failed_examples,
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
                    "overflow_layer_count",
                    "layer_height_at_least_excess",
                    "layer_height_at_least_baseline_plus_excess",
                    "assignment_all_excess_supported",
                    "assignment_all_baseline_plus_excess_supported",
                    "assignment_partial_excess_supported",
                    "square_classification_counts",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
