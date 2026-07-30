#!/usr/bin/env python3
"""Map mixed-parity square obstructions to canonical Fourier carriers."""

from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SQUARE_INPUT = ROOT / "reproductions" / "type-i-linear-block-square-boundary-results.json"
SPECTRUM_INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-square-obstruction-carrier-census-results.json"
TRICHOTOMY_SCRIPT = ROOT / "reproductions" / "type_i_linear_block_imbalance_trichotomy.py"

EXPECTED_SQUARE_SHA256 = "bd441dd873cda9e527042779eeb87229291de0136fb11588708e1c20566f1070"
EXPECTED_SPECTRUM_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


trichotomy = load_module("carrier_census_trichotomy", TRICHOTOMY_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def load_inputs() -> tuple[list[dict[str, object]], dict[tuple[int, int, int], str], dict[tuple[int, int, int], dict[str, object]], dict]:
    if not EXPECTED_SQUARE_SHA256:
        raise AssertionError("square-boundary input hash is not frozen")
    if sha256(SQUARE_INPUT) != EXPECTED_SQUARE_SHA256:
        raise AssertionError("the square-boundary input changed")
    if sha256(SPECTRUM_INPUT) != EXPECTED_SPECTRUM_SHA256:
        raise AssertionError("the full-spectrum input changed")
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the corrected Fourier input changed")

    square = json.loads(SQUARE_INPUT.read_text(encoding="utf-8"))
    spectrum = json.loads(SPECTRUM_INPUT.read_text(encoding="utf-8"))
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    status: dict[tuple[int, int, int], str] = {}
    finite_keys: set[tuple[int, int, int]] = set()
    for profile in spectrum["profiles"]:
        prime = int(profile["prime"])
        for record in profile["records"]:
            key = (prime, int(record["R"]), int(record["K"]))
            status[key] = str(record["classification"])
            if record["classification"] == "finite_exponent":
                finite_keys.add(key)

    fourier_records = {
        (int(record["prime"]), int(record["R"]), int(record["K"])): dict(record)
        for record in fourier["records"]
    }
    if set(fourier_records) != finite_keys:
        raise AssertionError("Fourier records do not preserve all finite-exponent state keys")
    for key, record in fourier_records.items():
        prime, modulus, K = key
        if 4 * K != prime * modulus + 1:
            raise AssertionError("Fourier record failed 4K=pR+1")
        factor_product = 1
        for q, exponent in record["factorization"]:
            factor_product *= int(q) ** int(exponent)
        if factor_product != K:
            raise AssertionError("Fourier factorization does not reconstruct K")

    obstruction = [
        dict(record)
        for record in square["records"]
        if record["square_classification"] == "mixed_parity_square_obstruction"
    ]
    return obstruction, status, fourier_records, spectrum


def required_height(exponent: int, prime: int) -> int:
    return (exponent + (2 if prime == 2 else 0) + 1) // 2


def carrier_groups(
    rows: list[dict[str, object]],
    states_by_prime: dict[int, list[tuple[int, dict[str, int]]]],
    mode: str,
    deduplicate: bool,
) -> list[dict[str, object]]:
    selected = rows
    if deduplicate:
        seen: set[tuple[int, int, int, int, str]] = set()
        selected = []
        for row in rows:
            identity = (
                int(row["prime"]),
                int(row["R"]),
                int(row["K"]),
                int(row["q"]),
                str(row["label"]),
            )
            if identity in seen:
                continue
            seen.add(identity)
            selected.append(row)

    grouped: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in selected:
        base = (int(row["prime"]), int(row["q"]), str(row["label"]))
        if mode == "pql":
            key = base
        elif mode == "pql-order":
            key = base + (int(row["character_order"]),)
        elif mode == "pql-phase":
            key = base + (
                tuple(int(q) for q in row["active_primes"]),
                tuple(int(value) for value in row["target_phase_mod_one"]),
            )
        else:
            raise ValueError(f"unknown grouping mode: {mode}")
        grouped[key].append(row)

    result = []
    for key, entries in sorted(grouped.items(), key=lambda item: item[0]):
        prime = int(entries[0]["prime"])
        q = int(entries[0]["q"])
        label = str(entries[0]["label"])
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        demand = sum(int(entry["required_height"]) for entry in entries)
        capacity = 0
        state_block_count = 0
        for modulus, state in states_by_prime[prime]:
            if not lo <= modulus <= hi:
                continue
            block = state["s"] * modulus + 1 if label == "s" else state["a"] * modulus + 1
            capacity += valuation(block, q)
            state_block_count += 1
        result.append(
            {
                "group_key": list(key),
                "prime": prime,
                "q": q,
                "label": label,
                "record_count": len(entries),
                "R_min": lo,
                "R_max": hi,
                "demand": demand,
                "capacity": capacity,
                "ratio": demand / capacity if capacity else None,
                "state_block_count": state_block_count,
            }
        )
    return result


def summarize_groups(groups: list[dict[str, object]]) -> dict[str, object]:
    ratios = [float(group["ratio"]) for group in groups if group["ratio"] is not None]
    overloads = [group for group in groups if group["ratio"] is not None and group["ratio"] > 1]
    return {
        "group_count": len(groups),
        "overload_count": len(overloads),
        "maximum_ratio": max(ratios) if ratios else None,
        "saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_groups": sorted(
            groups,
            key=lambda group: (group["ratio"] is not None, group["ratio"] or -1),
            reverse=True,
        )[:50],
    }


def run() -> dict[str, object]:
    obstruction, status, fourier_records, spectrum = load_inputs()
    status_counts = Counter()
    Fourier_status_counts = Counter()
    carrier_rows: list[dict[str, object]] = []
    phase_keys = Counter()
    active_support_counts = Counter()
    tie_count = 0
    height_deficit_count = 0
    f_keys: set[tuple[int, int, int]] = set()

    for record in obstruction:
        key = (int(record["prime"]), int(record["R"]), int(record["K"]))
        kind = status[key]
        status_counts[kind] += 1
        if kind != "finite_exponent":
            continue
        f_keys.add(key)
        Fourier = fourier_records[key]
        Fourier_status_counts[str(Fourier["status"])] += 1
        active = tuple(int(q) for q in Fourier["active_primes"])
        active_support_counts[len(active)] += 1
        phase_key = (
            key[0],
            active,
            int(Fourier["character_order"]),
            tuple(int(value) for value in Fourier["target_phase_mod_one"]),
        )
        phase_keys[phase_key] += 1
        U, V = int(record["U"]), int(record["V"])
        factors = {int(q): int(exponent) for q, exponent in Fourier["factorization"]}
        for q in active:
            h_s = valuation(U, q)
            h_a = valuation(V, q)
            if h_s == h_a:
                tie_count += 1
            label = "s" if h_s > h_a else "a"
            actual = max(h_s, h_a)
            required = required_height(factors[q], q)
            if actual < required:
                height_deficit_count += 1
            carrier_rows.append(
                {
                    "prime": key[0],
                    "R": key[1],
                    "K": key[2],
                    "q": q,
                    "label": label,
                    "required_height": required,
                    "actual_height": actual,
                    "height_s": h_s,
                    "height_a": h_a,
                    "active_primes": list(active),
                    "character_order": int(Fourier["character_order"]),
                    "target_phase_mod_one": list(Fourier["target_phase_mod_one"]),
                    "fourier_status": str(Fourier["status"]),
                }
            )

    states_by_prime: dict[int, list[tuple[int, dict[str, int]]]] = defaultdict(list)
    for profile in spectrum["profiles"]:
        prime = int(profile["prime"])
        for record in profile["records"]:
            modulus, K = int(record["R"]), int(record["K"])
            for state in trichotomy.linear_states(prime, modulus, K):
                states_by_prime[prime].append((modulus, state))

    group_summaries = {}
    for mode in ("pql", "pql-order", "pql-phase"):
        raw = carrier_groups(carrier_rows, states_by_prime, mode, False)
        deduplicated = carrier_groups(carrier_rows, states_by_prime, mode, True)
        group_summaries[mode] = {
            "raw": summarize_groups(raw),
            "deduplicated": summarize_groups(deduplicated),
        }

    repeated_phase = [count for count in phase_keys.values() if count > 1]
    return {
        "arithmetic": (
            "Map every mixed-parity smaller-block-square obstruction to its exact full-spectrum "
            "G/F/hit state. For F rows, attach each bounded Fourier active prime to the higher "
            "valuation carrier among U=sR+1 and V=aR+1, then compare conservative height demand "
            "with complete same-color linear-block capacity."
        ),
        "scope_note": (
            "Finite diagnostic boundary only. The carrier is a deterministic height-priority choice; "
            "capacity is generous and ignores phase quality, joint directions, and proof-level "
            "certificate uniqueness. No overload does not prove a selector or descent theorem."
        ),
        "square_input": SQUARE_INPUT.name,
        "square_input_sha256": sha256(SQUARE_INPUT),
        "spectrum_input": SPECTRUM_INPUT.name,
        "spectrum_input_sha256": sha256(SPECTRUM_INPUT),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "obstruction_record_count": len(obstruction),
        "obstruction_unique_state_count": len(
            {(int(record["prime"]), int(record["R"]), int(record["K"])) for record in obstruction}
        ),
        "state_classification_counts": dict(sorted(status_counts.items())),
        "f_obstruction_record_count": int(status_counts["finite_exponent"]),
        "f_obstruction_unique_state_count": len(f_keys),
        "fourier_status_counts": dict(sorted(Fourier_status_counts.items())),
        "active_support_counts": {str(key): int(value) for key, value in sorted(active_support_counts.items())},
        "carrier_row_count": len(carrier_rows),
        "carrier_tie_count": tie_count,
        "local_height_deficit_count": height_deficit_count,
        "phase_key_count": len(phase_keys),
        "repeated_phase_key_count": len(repeated_phase),
        "maximum_phase_key_multiplicity": max(phase_keys.values()) if phase_keys else 0,
        "group_summaries": group_summaries,
        "carrier_records": carrier_rows,
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
                    "obstruction_record_count",
                    "obstruction_unique_state_count",
                    "state_classification_counts",
                    "f_obstruction_record_count",
                    "f_obstruction_unique_state_count",
                    "fourier_status_counts",
                    "active_support_counts",
                    "carrier_row_count",
                    "carrier_tie_count",
                    "local_height_deficit_count",
                    "repeated_phase_key_count",
                    "maximum_phase_key_multiplicity",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
