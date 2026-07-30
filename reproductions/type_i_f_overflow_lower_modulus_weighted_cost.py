#!/usr/bin/env python3
"""Compute a finite unit-weight overflow-cost profile for lower-modulus F misses.

The search is deliberately shell based: every integer exponent vector with exact
overflow cost L is visited once.  Values found inside the cap are exact minima;
an unresolved state is reported only with the corresponding finite-search lower
bound.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-weighted-cost-results.json"

EXPECTED_INPUT_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"
PRIMARY_MAX_OVERFLOW = 6
SECONDARY_MAX_OVERFLOW = 9


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_overflow_vectors(nu: list[int], cost: int):
    """Yield each z with sum(max(abs(z_i)-nu_i, 0)) == cost exactly once."""
    vector = [0] * len(nu)

    def visit(index: int, remaining: int):
        if index == len(nu):
            if remaining == 0:
                yield tuple(vector)
            return

        bound = nu[index]
        # Values inside the box have zero cost and can be chosen freely.
        for exponent in range(-bound, bound + 1):
            vector[index] = exponent
            yield from visit(index + 1, remaining)

        # Outside the box, the two signs are the only choices for each excess.
        for excess in range(1, remaining + 1):
            for exponent in (bound + excess, -bound - excess):
                vector[index] = exponent
                yield from visit(index + 1, remaining - excess)
        vector[index] = 0

    yield from visit(0, cost)


def relation_residue(factors: list[int], modulus: int, vector: tuple[int, ...]) -> int:
    residue = 1 % modulus
    for q, exponent in zip(factors, vector):
        if math.gcd(q, modulus) != 1:
            raise AssertionError("a factor is not a unit modulo the lower modulus")
        if exponent >= 0:
            residue = residue * pow(q, exponent, modulus) % modulus
        else:
            residue = residue * pow(pow(q, -1, modulus), -exponent, modulus) % modulus
    return residue


def search_cost(
    factors: list[int], nu: list[int], modulus: int, maximum_cost: int
) -> dict[str, object]:
    """Search complete overflow shells through maximum_cost."""
    if modulus <= 1:
        raise AssertionError("the F relation requires a nontrivial lower modulus")
    if modulus % 4 != 1:
        raise AssertionError("the lower modulus must be 1 mod 4")

    checked = 0
    shell_counts: dict[str, int] = {}
    target = modulus - 1
    for cost in range(maximum_cost + 1):
        shell_count = 0
        best: tuple[int, ...] | None = None
        for vector in exact_overflow_vectors(nu, cost):
            shell_count += 1
            if relation_residue(factors, modulus, vector) != target:
                continue
            # The minimum cost is already fixed; this tie-break only makes the
            # representative reproducible and does not enter the scalar claim.
            if best is None or vector < best:
                best = vector
        checked += shell_count
        shell_counts[str(cost)] = shell_count
        if best is not None:
            return {
                "omega": cost,
                "vector": list(best),
                "vectors_checked": checked,
                "shell_vectors_checked": shell_counts,
                "exact_within_cap": True,
            }
    return {
        "omega": None,
        "vector": None,
        "vectors_checked": checked,
        "shell_vectors_checked": shell_counts,
        "exact_within_cap": False,
        "lower_bound": maximum_cost + 1,
    }


def histogram(rows: list[dict[str, object]], field: str) -> dict[str, int]:
    return {
        str(value): count
        for value, count in sorted(
            Counter(
                int(row[field])
                for row in rows
                if row[field] is not None
            ).items()
        )
    }


def run() -> dict[str, object]:
    input_hash = sha256(INPUT)
    source_hash = sha256(SOURCE_INPUT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError("the lower-modulus split input changed")
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")

    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): dict(row)
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }

    profiles: list[dict[str, object]] = []
    for row in payload["records"]:
        key = (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"]))
        if key not in source_rows:
            raise AssertionError("a split row is missing its frozen factorization")
        source_row = source_rows[key]
        for candidate in row.get("candidates", []):
            if candidate.get("lower_modulus_classification") != "F_box_miss":
                continue
            factors_with_multiplicity = [
                (int(q), int(nu)) for q, nu in source_row["factorization"]
            ]
            factors = [q for q, _nu in factors_with_multiplicity]
            nu = [exponent for _q, exponent in factors_with_multiplicity]
            modulus = int(candidate["balanced_t"])
            box_size = math.prod(2 * exponent + 1 for exponent in nu)

            primary = search_cost(factors, nu, modulus, PRIMARY_MAX_OVERFLOW)
            if primary["omega"] == 0:
                raise AssertionError("an F-box miss unexpectedly hit at cost zero")
            if primary["omega"] is not None:
                secondary = primary
            else:
                secondary = search_cost(factors, nu, modulus, SECONDARY_MAX_OVERFLOW)

            profiles.append(
                {
                    "prime": int(row["prime"]),
                    "orientation": row["orientation"],
                    "original_R": int(row["R"]),
                    "gap": int(candidate["gap"]),
                    "lower_modulus": modulus,
                    "factorization": [[q, exponent] for q, exponent in factors_with_multiplicity],
                    "box_size": box_size,
                    "primary_max_overflow": PRIMARY_MAX_OVERFLOW,
                    "omega_primary": primary["omega"],
                    "omega_primary_vector": primary["vector"],
                    "primary_exact_within_cap": primary["exact_within_cap"],
                    "primary_lower_bound": primary.get("lower_bound"),
                    "primary_vectors_checked": primary["vectors_checked"],
                    "primary_shell_vectors_checked": primary["shell_vectors_checked"],
                    "secondary_max_overflow": SECONDARY_MAX_OVERFLOW,
                    "omega_secondary": secondary["omega"],
                    "omega_secondary_vector": secondary["vector"],
                    "secondary_exact_within_cap": secondary["exact_within_cap"],
                    "secondary_lower_bound": secondary.get("lower_bound"),
                    "secondary_vectors_checked": secondary["vectors_checked"],
                    "secondary_shell_vectors_checked": secondary["shell_vectors_checked"],
                }
            )

    if len(profiles) != 42:
        raise AssertionError(f"unexpected lower-modulus F-box miss count: {len(profiles)}")

    by_orientation = {
        orientation: [row for row in profiles if row["orientation"] == orientation]
        for orientation in ("forward", "reverse")
    }
    return {
        "arithmetic": (
            "For each frozen lower-modulus F-box miss, enumerate the integer exponent "
            "fiber prod(q_i^z_i)=-1 by exact overflow-cost shells."
        ),
        "scope_note": (
            "Unit weights w_i=1 and finite caps only. A value found by a complete shell "
            "search through L is an exact Omega_1 minimum; an unresolved state is only "
            "known to have Omega_1 greater than the cap. This profile is not a q-height "
            "theorem, a capacity contradiction, or a descent proof."
        ),
        "input": INPUT.name,
        "input_sha256": input_hash,
        "factorization_input": SOURCE_INPUT.name,
        "factorization_input_sha256": source_hash,
        "state_count": len(profiles),
        "primary_max_overflow": PRIMARY_MAX_OVERFLOW,
        "primary_exact_count": sum(row["omega_primary"] is not None for row in profiles),
        "primary_unresolved_count": sum(row["omega_primary"] is None for row in profiles),
        "primary_histogram": histogram(profiles, "omega_primary"),
        "secondary_max_overflow": SECONDARY_MAX_OVERFLOW,
        "secondary_exact_count": sum(row["omega_secondary"] is not None for row in profiles),
        "secondary_unresolved_count": sum(row["omega_secondary"] is None for row in profiles),
        "secondary_histogram": histogram(profiles, "omega_secondary"),
        "primary_max_box_size": max(int(row["box_size"]) for row in profiles),
        "secondary_unresolved_states": [
            {
                "prime": row["prime"],
                "lower_modulus": row["lower_modulus"],
                "orientation": row["orientation"],
                "omega_secondary_lower_bound": row["secondary_lower_bound"],
            }
            for row in profiles
            if row["omega_secondary"] is None
        ],
        "profiles_by_orientation": {
            orientation: {
                "state_count": len(rows),
                "primary_exact_count": sum(row["omega_primary"] is not None for row in rows),
                "primary_histogram": histogram(rows, "omega_primary"),
                "secondary_exact_count": sum(
                    row["omega_secondary"] is not None for row in rows
                ),
                "secondary_histogram": histogram(rows, "omega_secondary"),
            }
            for orientation, rows in by_orientation.items()
        },
        "profiles": profiles,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "state_count",
                    "primary_exact_count",
                    "primary_unresolved_count",
                    "primary_histogram",
                    "secondary_exact_count",
                    "secondary_unresolved_count",
                    "secondary_histogram",
                    "secondary_unresolved_states",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
