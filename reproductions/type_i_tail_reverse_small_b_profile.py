#!/usr/bin/env python3
"""Profile bounded-B Type I normal reverse tails on 500M tail misses."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 127
DEFAULT_B_CAP = 5
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-small-b5-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("tail_reverse_small_b_landscape", LANDSCAPE)
bridge = load_module("tail_reverse_small_b_bridge", BRIDGE)


def first_small_b_edge(
    prime: int, gap_cap: int, b_cap: int, even_source_only: bool = False
) -> tuple[dict[str, object] | None, int]:
    """Return the first verified Type I maximum-tail edge with B<=b_cap."""
    checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = entry["normal_form"]
            if B > b_cap:
                continue
            checked += 1
            certificate = bridge.short_certificate.type_i_normal_form_certificate(
                prime, gap, A, B
            )
            if certificate is None:
                raise AssertionError("stored normal form did not rebuild")
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                if even_source_only and int(lift["source_denominator"]) % 2:
                    continue
                if even_source_only:
                    bridge_divisor = int(lift["bridge_divisor"])
                    if bridge_divisor % (prime * prime):
                        raise AssertionError("bridge divisor did not reconstruct E")
                    E = bridge_divisor // (prime * prime)
                    R = (4 * B * B * C + 1) // gap
                    K = (prime * R + 1) // 4
                    if (
                        E % 2
                        or E % R != 1
                        or E > 4 * K - 2 * R
                        or (4 * K * K) % E
                    ):
                        raise AssertionError(
                            "even-source lift did not satisfy the bridge criterion"
                        )
                target = (certificate.x, certificate.y, certificate.z)
                source = (lift["source_term"], certificate.x, certificate.y)
                if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
                    raise AssertionError("target identity did not verify")
                if Fraction(4, lift["source_denominator"]) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("source identity did not verify")
                return (
                    {
                        "gap": gap,
                        "divisor": entry["divisor"],
                        "normal_form": [A, B, C],
                        "target_solution": list(target),
                        "reverse_two_tail_lift": lift,
                        "source_solution": list(source),
                    },
                    checked,
                )
    return None, checked


def run_profile(
    tail: dict[str, object],
    gap_cap: int = DEFAULT_GAP_CAP,
    b_cap: int = DEFAULT_B_CAP,
    even_source_only: bool = False,
) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    checked = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        edge, local_checked = first_small_b_edge(
            prime, gap_cap, b_cap, even_source_only
        )
        checked += local_checked
        if edge is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, **edge})
    b_counts: dict[str, int] = {}
    for record in records:
        B = int(record["normal_form"][1])
        b_counts[str(B)] = b_counts.get(str(B), 0) + 1
    result = {
        "arithmetic": (
            "for each stored ordinary-tail miss, enumerate every Type I normal "
            "certificate with m=3 (mod 4) through gap_cap and B<=b_cap; apply "
            "the complete E|4K^2 maximum-tail selector and verify source and target identities"
        ),
        "scope_note": (
            "Finite bounded-B profile. It tests target-side Type I normal forms and "
            "does not supply a source-side selector beyond the stated range."
        ),
        "input_prime_limit": tail["prime_limit"],
        "tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "b_cap": b_cap,
        "captured_count": len(records),
        "misses": misses,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "total_small_b_normal_forms_checked_until_first_edge_or_cap": checked,
        "first_hit_b_counts": dict(sorted(b_counts.items(), key=lambda item: int(item[0]))),
        "records": records,
    }
    if even_source_only:
        result["source_parity_filter"] = "even"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--even-source-only", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.tail.read_text(encoding="utf-8")),
        args.gap_cap,
        args.b_cap,
        args.even_source_only,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
