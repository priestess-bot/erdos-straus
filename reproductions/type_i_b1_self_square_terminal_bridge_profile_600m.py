#!/usr/bin/env python3
"""Profile the self-square terminal bridge on selected B=1 pressure targets."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_500 = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
UPPER_500 = ROOT / "reproductions" / "type-i-tail-upper-b1-completion-profile-500m-results.json"
DENSE_600 = ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
UPPER_600 = ROOT / "reproductions" / "type-i-mixed-terminal-dense-upper-b1-reselection-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b1-self-square-terminal-bridge-profile-600m-results.json"


def verify_target(prime: int, A: int, C: int, H: int, R: int, K: int) -> int:
    """Validate one B=1 target normal form and return its natural gap."""
    gap, remainder = divmod(4 * C + 1, R)
    if (
        remainder
        or prime % 24 != 1
        or gap < 3
        or gap % 4 != 3
        or R < 3
        or R % 4 != 3
        or H != A * R - 1
        or K != C * H
        or prime != 4 * A * C - gap
        or 4 * K != prime * R + 1
        or Fraction(4, prime) != Fraction(1, A * C) + Fraction(1, A * C * H) + Fraction(1, prime * K)
    ):
        raise AssertionError("stored B=1 target did not reconstruct")
    return gap


def self_square_witness(
    prime: int, A: int, C: int, H: int, R: int, K: int
) -> dict[str, int | bool] | None:
    """Use E=16*C^2 whenever the complementary B=1 factor is large and even."""
    gap = verify_target(prime, A, C, H, R, K)
    if H % 2 or H <= 4 * C:
        return None
    E = 16 * C * C
    numerator = 4 * K - E
    source, remainder = divmod(numerator, R)
    if remainder:
        raise AssertionError("self-square bridge lost its source integrality")
    source_term, remainder = divmod(source * K, E)
    if (
        remainder
        or E % 2
        or E % R != 1
        or (4 * K * K) % E
        or E > 4 * K - 2 * R
        or source % 2
        or not (2 <= source < prime)
        or Fraction(4, source) != Fraction(1, source_term) + Fraction(1, A * C) + Fraction(1, A * C * H)
    ):
        raise AssertionError("self-square bridge did not reconstruct")
    quotient = (H - 4 * C) // R
    if H - 4 * C != quotient * R or source != 4 * C * quotient or source_term != quotient * H // 4:
        raise AssertionError("self-square source formulas did not reconstruct")
    return {
        "A": A,
        "B": 1,
        "C": C,
        "H": H,
        "m": gap,
        "R": R,
        "K": K,
        "E": E,
        "source_denominator": source,
        "source_term": source_term,
        "quotient": quotient,
        "upper_half": 2 * source >= prime + 1,
    }


def append_target(
    targets: list[dict[str, int | str]],
    prime: int,
    normal: list[int],
    R: int,
    K: int,
    origin: str,
) -> None:
    """Store a target-only B=1 normal form after checking its normal data."""
    A, B, C = (int(value) for value in normal)
    if B != 1 or K % C:
        raise AssertionError("input did not supply a B=1 target form")
    H = K // C
    verify_target(prime, A, C, H, R, K)
    targets.append({"prime": prime, "A": A, "C": C, "H": H, "R": R, "K": K, "origin": origin})


def selected_targets(
    base: dict[str, object], upper_500: dict[str, object], dense: dict[str, object], upper_600: dict[str, object]
) -> list[dict[str, int | str]]:
    """Recover the exact 1,964 selected upper-source B=1 target forms."""
    targets: list[dict[str, int | str]] = []
    lower_500: list[int] = []
    records = base["records"]
    if not isinstance(records, list):
        raise TypeError("base 500M records are not a list")
    for row in records:
        prime = int(row["prime"])
        witness = row["minimum_b1_source_witness"]
        if not isinstance(witness, dict):
            raise TypeError("base witness is not an object")
        lift = witness["reverse_two_tail_lift"]
        if not isinstance(lift, dict):
            raise TypeError("base witness has no reverse lift")
        if 2 * int(lift["source_denominator"]) >= prime + 1:
            append_target(
                targets,
                prime,
                [int(value) for value in witness["normal_form"]],
                int(witness["R"]),
                int(witness["K"]),
                "500_direct_upper",
            )
        else:
            lower_500.append(prime)
    if len(targets) != 1709 or sorted(lower_500) != [629689, 58757449, 83445289, 218482009]:
        raise AssertionError("500M direct/lower source partition changed")

    for row in upper_500["lower_source_state_reselected_records"]:
        certificate = row["certificate"]
        append_target(
            targets,
            int(row["prime"]),
            [int(value) for value in certificate["normal_form"]],
            int(certificate["R"]),
            int(certificate["K"]),
            "500_reselected_upper",
        )
    row = upper_500["lower_source_state_direct_gap_extension_record"]
    certificate = row["certificate"]
    append_target(
        targets,
        int(row["prime"]),
        [int(value) for value in certificate["normal_form"]],
        int(certificate["R"]),
        int(certificate["K"]),
        "500_reselected_extension",
    )
    for row in upper_500["direct_B_eq_1_gap_extension_records"]:
        certificate = row["certificate"]
        append_target(
            targets,
            int(row["prime"]),
            [int(value) for value in certificate["normal_form"]],
            int(certificate["R"]),
            int(certificate["K"]),
            "500_direct_extension",
        )

    reselected_600 = {
        int(row["prime"]): row["selected_upper_B_one_state"]
        for row in upper_600["reselected_upper_B_eq_1_records"]
    }
    for row in dense["records"]:
        prime = int(row["prime"])
        lift = row["reverse_two_tail_lift"]
        source = int(lift["source_denominator"])
        E, remainder = divmod(int(lift["bridge_divisor"]), prime * prime)
        if remainder:
            raise AssertionError("dense bridge factor did not reconstruct")
        if 2 * source >= prime + 1:
            R, remainder = divmod(E - 1, prime - source)
            if remainder:
                raise AssertionError("dense direct bridge R did not reconstruct")
            append_target(
                targets,
                prime,
                [int(value) for value in row["normal_form"]],
                R,
                (prime * R + 1) // 4,
                "600_direct_upper",
            )
            continue
        state = reselected_600.get(prime)
        if not isinstance(state, dict):
            raise AssertionError("dense lower source has no stored upper re-selection")
        realization = state["B_one_realization"]
        append_target(
            targets,
            prime,
            [int(realization["A"]), 1, int(realization["C"])],
            int(realization["R"]),
            int(realization["K"]),
            "600_reselected_upper",
        )

    primes = {int(row["prime"]) for row in targets}
    if len(targets) != 1964 or len(primes) != len(targets):
        raise AssertionError("selected B=1 target assembly did not recover 1,964 distinct primes")
    return sorted(targets, key=lambda row: int(row["prime"]))


def run_audit(
    base_path: Path = BASE_500,
    upper_500_path: Path = UPPER_500,
    dense_path: Path = DENSE_600,
    upper_600_path: Path = UPPER_600,
) -> dict[str, object]:
    """Reconstruct the deterministic self-square bridge profile."""
    targets = selected_targets(
        json.loads(base_path.read_text(encoding="utf-8")),
        json.loads(upper_500_path.read_text(encoding="utf-8")),
        json.loads(dense_path.read_text(encoding="utf-8")),
        json.loads(upper_600_path.read_text(encoding="utf-8")),
    )
    records: list[dict[str, object]] = []
    parity_failures = 0
    small_complement_failures = 0
    for target in targets:
        H = int(target["H"])
        C = int(target["C"])
        if H % 2:
            parity_failures += 1
        if H <= 4 * C:
            small_complement_failures += 1
        witness = self_square_witness(
            int(target["prime"]),
            int(target["A"]),
            C,
            H,
            int(target["R"]),
            int(target["K"]),
        )
        if witness is not None:
            records.append({"prime": int(target["prime"]), "origin": target["origin"], "witness": witness})

    origin_counts = Counter(str(row["origin"]) for row in records)
    upper_count = sum(bool(row["witness"]["upper_half"]) for row in records)
    return {
        "arithmetic": (
            "recover the selected upper-source B=1 target normal forms on the frozen 600M ordinary-tail "
            "pressure set; whenever H is even and H>4C, set E=16C^2 and replay the resulting target and source identities"
        ),
        "scope_note": (
            "This is a finite profile of already selected B=1 target forms. The self-square condition is a "
            "general sufficient bridge theorem, but the profile does not assert that every core prime has such a form."
        ),
        "base_500_input": base_path.name,
        "upper_500_input": upper_500_path.name,
        "dense_600_input": dense_path.name,
        "upper_600_input": upper_600_path.name,
        "selected_B_one_target_count": len(targets),
        "self_square_bridge_count": len(records),
        "self_square_upper_half_count": upper_count,
        "parity_failure_count": parity_failures,
        "small_complement_failure_count": small_complement_failures,
        "self_square_origin_counts": dict(sorted(origin_counts.items())),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-500", type=Path, default=BASE_500)
    parser.add_argument("--upper-500", type=Path, default=UPPER_500)
    parser.add_argument("--dense-600", type=Path, default=DENSE_600)
    parser.add_argument("--upper-600", type=Path, default=UPPER_600)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.base_500, args.upper_500, args.dense_600, args.upper_600)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
