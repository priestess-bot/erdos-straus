#!/usr/bin/env python3
"""Audit standard-even and E-split lifts for every frozen Psi_0=1 predecessor."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)
DYADIC_SCRIPT = (
    ROOT
    / "reproductions"
    / "type_i_linear_target_fiber_dyadic_non_near_profile_600m.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-standard-even-lift-audit-results.json"
)

EXPECTED_INPUT_SHA256 = "eb0ef6c4fe5103d907916ebb4d2fc0bc97913344d3cb143e1f17cb582fa0adc2"
EXPECTED_DYADIC_SHA256 = "0cacaa41ac65a59da52c897deae10ccd7eb90ed7ce5e7ff279590ab043390323"
EXPECTED_SUMMARY = {
    "source_state_count": 483,
    "raw_dyadic_candidate_count": 3_976,
    "unique_predecessor_count": 1_385,
    "raw_E_lt_2K_count": 3_896,
    "raw_2K_lt_E_lt_3K_count": 30,
    "raw_E_gt_3K_count": 50,
    "unique_E_lt_2K_count": 1_351,
    "unique_2K_lt_E_lt_3K_count": 17,
    "unique_E_gt_3K_count": 17,
    "half_positive_state_count": 483,
    "half_positive_candidate_count": 1_351,
    "half_base_square_divisor_count": 1_021_941,
    "half_unordered_factor_pair_count": 1_533_587,
    "half_natural_E_eligible_count": 915,
    "half_hit_count": 0,
    "half_hit_state_count": 0,
    "full_positive_candidate_count": 1_368,
    "full_base_square_divisor_count": 1_505_216,
    "full_unordered_factor_pair_count": 2_258_508,
    "full_natural_E_eligible_count": 1_368,
    "full_hit_count": 0,
    "full_hit_state_count": 0,
    "total_unordered_factor_pair_count": 3_792_095,
    "E_split_source_count": 1_385,
    "E_split_even_H_count": 1_385,
    "E_split_channel_count": 2_770,
    "E_split_positive_D_count": 2_557,
    "E_split_nonpositive_D_count": 213,
    "E_split_hit_count": 0,
    "E_split_hit_state_count": 0,
}
STATE_LOCAL_RESIDUALS = {
    (37_793_809, 35),
    (78_268_369, 8_895),
    (174_600_409, 20_631),
    (278_505_049, 231),
}
COMPLETE_REACH_FINAL_RESIDUALS = {
    (78_268_369, 8_895),
    (278_505_049, 231),
}
EXPECTED_RESIDUAL_SUMMARIES = {
    "state_local_four": {
        "state_count": 4,
        "raw_candidate_count": 88,
        "unique_predecessor_count": 12,
        "half_positive_candidate_count": 11,
        "half_unordered_factor_pair_count": 4_762,
        "full_positive_candidate_count": 12,
        "full_unordered_factor_pair_count": 7_512,
        "E_split_channel_count": 24,
        "E_split_positive_D_count": 21,
        "E_split_hit_count": 0,
    },
    "complete_reach_final_two": {
        "state_count": 2,
        "raw_candidate_count": 25,
        "unique_predecessor_count": 7,
        "half_positive_candidate_count": 6,
        "half_unordered_factor_pair_count": 2_244,
        "full_positive_candidate_count": 7,
        "full_unordered_factor_pair_count": 3_581,
        "E_split_channel_count": 14,
        "E_split_positive_D_count": 12,
        "E_split_hit_count": 0,
    },
}

_SQUARE_DIVISOR_CACHE: dict[int, tuple[int, ...]] = {}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


dyadic = load_module("standard_even_lift_dyadic", DYADIC_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def square_divisors(value: int) -> tuple[int, ...]:
    if value not in _SQUARE_DIVISOR_CACHE:
        factors = {int(q): int(e) for q, e in sympy.factorint(value).items()}
        if math.prod(q**e for q, e in factors.items()) != value:
            raise AssertionError("factorization did not reconstruct its input")
        divisors = [1]
        for q, exponent in sorted(factors.items()):
            divisors = [
                divisor * q**power
                for divisor in divisors
                for power in range(2 * exponent + 1)
            ]
        _SQUARE_DIVISOR_CACHE[value] = tuple(sorted(divisors))
    return _SQUARE_DIVISOR_CACHE[value]


def verify_solution(prime: int, solution: tuple[int, int, int]) -> None:
    if min(solution) <= 0 or sum((Fraction(1, value) for value in solution), Fraction()) != Fraction(4, prime):
        raise AssertionError("lift did not reconstruct the target unit-fraction identity")


def one_tail_audit(prime: int, coordinate: int) -> dict[str, object]:
    """Enumerate every unordered factor pair for a retained coordinate c<p."""
    if not 0 < coordinate < prime:
        raise AssertionError("the standard retained coordinate left 0<c<p")
    modulus = 4 * coordinate - prime
    if modulus <= 0:
        return {
            "positive_remainder": False,
            "base_square_divisor_count": 0,
            "unordered_factor_pair_count": 0,
            "hit_count": 0,
            "first_hit": None,
        }

    scale = prime * coordinate
    base_divisors = square_divisors(coordinate)
    factor_pair_count = 0
    hits = []
    for divisor in base_divisors:
        candidates = [(divisor, "Type_I")]
        if divisor <= coordinate:
            candidates.append((prime * divisor, "Type_II"))
        for factor, certificate_type in candidates:
            factor_pair_count += 1
            if (scale + factor) % modulus:
                continue
            complement = scale * scale // factor
            if (scale + complement) % modulus:
                raise AssertionError("the paired factor congruence was not automatic")
            solution = (
                coordinate,
                (scale + factor) // modulus,
                (scale + complement) // modulus,
            )
            verify_solution(prime, solution)
            hits.append(
                {
                    "factor": factor,
                    "base_divisor": divisor,
                    "type": certificate_type,
                    "solution": list(solution),
                }
            )
    expected_pair_count = (3 * len(base_divisors) + 1) // 2
    if factor_pair_count != expected_pair_count:
        raise AssertionError("unordered factor-pair count changed")
    first_hit = min(hits, key=lambda row: int(row["factor"])) if hits else None
    return {
        "positive_remainder": True,
        "gap": modulus,
        "base_square_divisor_count": len(base_divisors),
        "unordered_factor_pair_count": factor_pair_count,
        "hit_count": len(hits),
        "first_hit": first_hit,
    }


def natural_factor_status(
    prime: int, coordinate: int, E: int, audit: dict[str, object]
) -> dict[str, object]:
    eligible = bool(audit["positive_remainder"]) and coordinate * coordinate % E == 0
    hit = False
    if eligible:
        modulus = 4 * coordinate - prime
        scale = prime * coordinate
        complement = scale * scale // E
        hit = (scale + E) % modulus == 0 and (scale + complement) % modulus == 0
    return {"eligible": eligible, "hit": hit}


def E_split_audit(prime: int, n: int, E: int) -> dict[str, object]:
    if n * n % E:
        raise AssertionError("E did not divide n^2")
    H = n * n // E
    if n % 2 or E % 2 or H % 2:
        raise AssertionError("the E-split source was not integral")
    half = n // 2
    source = (half, (n + E) // 2, (n + H) // 2)
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(4, n):
        raise AssertionError("the E-split source identity failed")

    channels = []
    for label, tail, other in (("E", E, H), ("H", H, E)):
        replaced = (n + tail) // 2
        retained_tail = (n + other) // 2
        D = n * prime - 4 * (prime - n) * replaced
        hit = D > 0 and n * prime * replaced % D == 0
        row: dict[str, object] = {
            "tail": label,
            "D": D,
            "positive_D": D > 0,
            "hit": hit,
        }
        if hit:
            replacement = n * prime * replaced // D
            solution = (half, retained_tail, replacement)
            verify_solution(prime, solution)
            modulus = 4 * half - prime
            scale = prime * half
            factors = [
                modulus * retained_tail - scale,
                modulus * replacement - scale,
            ]
            if min(factors) <= 0 or factors[0] * factors[1] != scale * scale:
                raise AssertionError("E-split hit did not embed in the retained-half factor space")
            row.update(
                {
                    "replacement": replacement,
                    "solution": list(solution),
                    "retained_half_factor": min(factors),
                }
            )
        channels.append(row)
    return {"H": H, "source": list(source), "channels": channels}


def interval_name(E: int, K: int) -> str:
    if E < 2 * K:
        return "E_lt_2K"
    if 2 * K < E < 3 * K:
        return "2K_lt_E_lt_3K"
    if E > 3 * K:
        return "E_gt_3K"
    raise AssertionError("the forbidden E=2K or E=3K boundary occurred")


def predecessor_groups(source: dict[str, object]) -> list[dict[str, object]]:
    groups = []
    for record in source["records"]:
        prime = int(record["prime"])
        R = int(record["R"])
        K = int(record["K"])
        terminals = dyadic.legal_terminals(R, K)
        if len(terminals) != int(record["dyadic"]["candidate_count"]):
            raise AssertionError("dyadic raw multiplicity changed")
        by_predecessor: dict[tuple[int, int], list[dict[str, object]]] = defaultdict(list)
        for terminal in terminals:
            E = int(terminal["E"])
            n = int(terminal["n"])
            if not (0 < n < prime and n % 2 == 0 and E % R == 1 and E < 4 * K):
                raise AssertionError("a frozen dyadic predecessor lost its arithmetic contract")
            by_predecessor[(E, n)].append(terminal)
        if len(by_predecessor) != int(record["dyadic"]["distinct_n_count"]):
            raise AssertionError("per-state predecessor deduplication changed")
        for (E, n), raw in sorted(by_predecessor.items()):
            groups.append(
                {
                    "prime": prime,
                    "R": R,
                    "K": K,
                    "E": E,
                    "n": n,
                    "raw_multiplicity": len(raw),
                    "j_values": sorted({int(row["j"]) for row in raw}),
                    "interval": interval_name(E, K),
                }
            )
    return groups


def audit_predecessor(group: dict[str, object]) -> dict[str, object]:
    prime = int(group["prime"])
    E = int(group["E"])
    n = int(group["n"])
    half = one_tail_audit(prime, n // 2)
    full = one_tail_audit(prime, n)
    half["natural_E"] = natural_factor_status(prime, n // 2, E, half)
    full["natural_E"] = natural_factor_status(prime, n, E, full)
    half["semantics"] = "direct_gap_2n_minus_p" if half["positive_remainder"] else "nonpositive"
    if not full["positive_remainder"]:
        full["semantics"] = "nonpositive"
    elif 2 * n < prime:
        full["semantics"] = "direct_gap_4n_minus_p"
    else:
        full["semantics"] = "direct_Type_I_rechart_if_hit"
    return {
        **group,
        "standard_even_source": [n // 2, n, n],
        "retain_n_over_2": half,
        "retain_n": full,
        "E_split": E_split_audit(prime, n, E),
    }


def subset_summary(
    records: list[dict[str, object]], state_keys: set[tuple[int, int]]
) -> dict[str, int]:
    subset = [row for row in records if (int(row["prime"]), int(row["R"])) in state_keys]
    channels = [channel for row in subset for channel in row["E_split"]["channels"]]
    return {
        "state_count": len({(int(row["prime"]), int(row["R"])) for row in subset}),
        "raw_candidate_count": sum(int(row["raw_multiplicity"]) for row in subset),
        "unique_predecessor_count": len(subset),
        "half_positive_candidate_count": sum(bool(row["retain_n_over_2"]["positive_remainder"]) for row in subset),
        "half_unordered_factor_pair_count": sum(int(row["retain_n_over_2"]["unordered_factor_pair_count"]) for row in subset),
        "full_positive_candidate_count": sum(bool(row["retain_n"]["positive_remainder"]) for row in subset),
        "full_unordered_factor_pair_count": sum(int(row["retain_n"]["unordered_factor_pair_count"]) for row in subset),
        "E_split_channel_count": len(channels),
        "E_split_positive_D_count": sum(bool(channel["positive_D"]) for channel in channels),
        "E_split_hit_count": sum(bool(channel["hit"]) for channel in channels),
    }


def sensitivity_checks() -> dict[str, object]:
    failure_half = one_tail_audit(73, 36)
    failure_full = one_tail_audit(73, 72)
    if failure_half["hit_count"] or failure_full["hit_count"]:
        raise AssertionError("the p=73 standard-even counterexample changed")

    positive = audit_predecessor(
        {
            "prime": 97,
            "R": 15,
            "K": 364,
            "E": 676,
            "n": 52,
            "raw_multiplicity": 1,
            "j_values": [1],
            "interval": interval_name(676, 364),
        }
    )
    split_hits = [row for row in positive["E_split"]["channels"] if row["hit"]]
    if not positive["retain_n_over_2"]["hit_count"] or len(split_hits) != 1:
        raise AssertionError("the positive lift sensitivity check stopped detecting hits")
    return {
        "standard_even_failure": {
            "prime": 73,
            "R": 47,
            "K": 858,
            "E": 48,
            "n": 72,
            "half_factor_pairs": failure_half["unordered_factor_pair_count"],
            "full_factor_pairs": failure_full["unordered_factor_pair_count"],
        },
        "positive_E_split": {
            "prime": 97,
            "R": 15,
            "K": 364,
            "E": 676,
            "n": 52,
            "one_tail_first_hit": positive["retain_n_over_2"]["first_hit"],
            "E_split_hit": split_hits[0],
        },
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum terminal audit changed")
    if sha256(DYADIC_SCRIPT) != EXPECTED_DYADIC_SHA256:
        raise AssertionError("the generalized-dyadic enumerator changed")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    groups = predecessor_groups(source)
    records = [audit_predecessor(group) for group in groups]
    all_channels = [channel for row in records for channel in row["E_split"]["channels"]]

    raw_intervals = defaultdict(int)
    unique_intervals = defaultdict(int)
    for row in records:
        unique_intervals[str(row["interval"])] += 1
        raw_intervals[str(row["interval"])] += int(row["raw_multiplicity"])
    half_hit_states = {
        (int(row["prime"]), int(row["R"]))
        for row in records
        if row["retain_n_over_2"]["hit_count"]
    }
    full_hit_states = {
        (int(row["prime"]), int(row["R"]))
        for row in records
        if row["retain_n"]["hit_count"]
    }
    split_hit_states = {
        (int(row["prime"]), int(row["R"]))
        for row in records
        if any(channel["hit"] for channel in row["E_split"]["channels"])
    }
    summary = {
        "source_state_count": len(source["records"]),
        "raw_dyadic_candidate_count": sum(int(row["raw_multiplicity"]) for row in records),
        "unique_predecessor_count": len(records),
        "raw_E_lt_2K_count": raw_intervals["E_lt_2K"],
        "raw_2K_lt_E_lt_3K_count": raw_intervals["2K_lt_E_lt_3K"],
        "raw_E_gt_3K_count": raw_intervals["E_gt_3K"],
        "unique_E_lt_2K_count": unique_intervals["E_lt_2K"],
        "unique_2K_lt_E_lt_3K_count": unique_intervals["2K_lt_E_lt_3K"],
        "unique_E_gt_3K_count": unique_intervals["E_gt_3K"],
        "half_positive_state_count": len({
            (int(row["prime"]), int(row["R"]))
            for row in records
            if row["retain_n_over_2"]["positive_remainder"]
        }),
        "half_positive_candidate_count": sum(bool(row["retain_n_over_2"]["positive_remainder"]) for row in records),
        "half_base_square_divisor_count": sum(int(row["retain_n_over_2"]["base_square_divisor_count"]) for row in records),
        "half_unordered_factor_pair_count": sum(int(row["retain_n_over_2"]["unordered_factor_pair_count"]) for row in records),
        "half_natural_E_eligible_count": sum(bool(row["retain_n_over_2"]["natural_E"]["eligible"]) for row in records),
        "half_hit_count": sum(int(row["retain_n_over_2"]["hit_count"]) for row in records),
        "half_hit_state_count": len(half_hit_states),
        "full_positive_candidate_count": sum(bool(row["retain_n"]["positive_remainder"]) for row in records),
        "full_base_square_divisor_count": sum(int(row["retain_n"]["base_square_divisor_count"]) for row in records),
        "full_unordered_factor_pair_count": sum(int(row["retain_n"]["unordered_factor_pair_count"]) for row in records),
        "full_natural_E_eligible_count": sum(bool(row["retain_n"]["natural_E"]["eligible"]) for row in records),
        "full_hit_count": sum(int(row["retain_n"]["hit_count"]) for row in records),
        "full_hit_state_count": len(full_hit_states),
        "total_unordered_factor_pair_count": sum(
            int(row["retain_n_over_2"]["unordered_factor_pair_count"])
            + int(row["retain_n"]["unordered_factor_pair_count"])
            for row in records
        ),
        "E_split_source_count": len(records),
        "E_split_even_H_count": sum(int(row["E_split"]["H"]) % 2 == 0 for row in records),
        "E_split_channel_count": len(all_channels),
        "E_split_positive_D_count": sum(bool(row["positive_D"]) for row in all_channels),
        "E_split_nonpositive_D_count": sum(not bool(row["positive_D"]) for row in all_channels),
        "E_split_hit_count": sum(bool(row["hit"]) for row in all_channels),
        "E_split_hit_state_count": len(split_hit_states),
    }
    if summary != EXPECTED_SUMMARY:
        raise AssertionError(f"standard-even lift summary changed: {summary}")

    residual_summaries = {
        "state_local_four": subset_summary(records, STATE_LOCAL_RESIDUALS),
        "complete_reach_final_two": subset_summary(records, COMPLETE_REACH_FINAL_RESIDUALS),
    }
    if residual_summaries != EXPECTED_RESIDUAL_SUMMARIES:
        raise AssertionError(f"residual lift summaries changed: {residual_summaries}")

    first = records[0]
    first_counterexample: dict[str, object] = {
        "prime": first["prime"],
        "R": first["R"],
        "K": first["K"],
        "E": first["E"],
        "n": first["n"],
        "half_factor_pairs": first["retain_n_over_2"]["unordered_factor_pair_count"],
        "full_factor_pairs": first["retain_n"]["unordered_factor_pair_count"],
        "E_split_source": first["E_split"]["source"],
    }
    first_counterexample["E_split_remainders"] = [
        (
            int(first["n"])
            * int(first["prime"])
            * ((int(first["n"]) + tail) // 2)
        )
        % int(channel["D"])
        for tail, channel in zip(
            (int(first["E"]), int(first["E_split"]["H"])),
            first["E_split"]["channels"],
        )
        if int(channel["D"]) > 0
    ]

    return {
        "schema_version": "psi-one-full-spectrum-standard-even-lift-audit/v1",
        "scope_note": (
            "This is a complete finite audit of 1,385 distinct generalized-dyadic predecessors "
            "from 483 frozen F states. Zero hits do not imply a universal obstruction. Every "
            "one-retained-coordinate success is a direct Type I/II terminal or rechart, not an "
            "independent E4 descent edge."
        ),
        "inputs": {
            "terminal_audit": {"path": INPUT.name, "sha256": sha256(INPUT)},
            "dyadic_enumerator": {"path": DYADIC_SCRIPT.name, "sha256": sha256(DYADIC_SCRIPT)},
        },
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "residual_summaries": residual_summaries,
        "first_counterexample": first_counterexample,
        "sensitivity_checks": sensitivity_checks(),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
