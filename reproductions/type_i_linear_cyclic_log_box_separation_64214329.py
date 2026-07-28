#!/usr/bin/env python3
"""Certify a cyclic-log finite-box obstruction at one F-state.

The state is an exact row of the seven-spectrum cross-source audit.  The
script recomputes its centered residue sets, then uses a primitive root of
U(359) to separate subgroup membership from the bounded exponent box.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-f-cross-source-pullback-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-cyclic-log-box-separation-64214329-359.json"
EXPECTED_INPUT_SHA256 = (
    "60a95000d81cdfee41f6b07b54b0f9e088bc56f71772ef296dec49b7c3020d05"
)

PRIME = 64_214_329
R = 359
A = 7_154
S = 25
EXPECTED_K = 5_763_236_028
EXPECTED_GAMMA = 2_244
EXPECTED_AFFINE = 2_568_287
EXPECTED_SHARED = 42_636


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> list[tuple[int, int]]:
    """Return an exact sorted prime factorization."""
    factors = sorted((int(q), int(e)) for q, e in sympy.factorint(value).items())
    if math.prod(q**e for q, e in factors) != value:
        raise AssertionError("factorization did not reconstruct its input")
    return factors


def centered_difference(value: int, modulus: int) -> set[int]:
    """Enumerate the centered prime-exponent difference box modulo 'modulus'."""
    residues = {1}
    for prime, exponent in factorization(value):
        powers = {pow(prime, z, modulus) for z in range(-exponent, exponent + 1)}
        residues = {left * right % modulus for left in residues for right in powers}
    return residues


def factor_payload(value: int) -> list[dict[str, int]]:
    return [{"prime": q, "exponent": e} for q, e in factorization(value)]


def load_frozen_row() -> dict[str, object]:
    """Load the row while checking that the frozen seven-spectrum input is unchanged."""
    if file_sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("seven-spectrum input artifact changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    for profile in payload["profiles"]:
        if int(profile["prime"]) != PRIME:
            continue
        for record in profile["records"]:
            if int(record["R"]) != R:
                continue
            orientations = record["orientations"]
            if len(orientations) != 1:
                raise AssertionError("the selected F-state must have one orientation")
            return {
                "K": record["K"],
                "shared_layer": record["shared_layer"],
                **orientations[0],
            }
    raise AssertionError("selected F-state row is missing")


def minimum_overflow(
    residue: int,
    modulus: int,
    factors: list[tuple[int, int]],
    max_overflow: int,
) -> tuple[int, tuple[int, ...]]:
    """Find the least common extra exponent budget representing 'residue'."""
    for overflow in range(max_overflow + 1):
        ranges = [
            range(-exponent - overflow, exponent + overflow + 1)
            for _, exponent in factors
        ]
        for vector in itertools.product(*ranges):
            value = 1
            for (prime, _), coordinate in zip(factors, vector):
                value = value * pow(prime, coordinate, modulus) % modulus
            if value == residue:
                if overflow == 0:
                    raise AssertionError("finite-box intersection was expected to be empty")
                return overflow, tuple(int(coordinate) for coordinate in vector)
    raise AssertionError("overflow exceeded the complete cyclic-group search bound")


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Recompute the exact cyclic-log separation certificate."""
    if input_path != INPUT:
        raise ValueError("this certificate is tied to the frozen seven-spectrum input")
    row = load_frozen_row()
    K = (PRIME * R + 1) // 4
    gamma = (S * R + 1) // 4
    affine = A * R + 1
    if (
        K != EXPECTED_K
        or gamma != EXPECTED_GAMMA
        or affine != EXPECTED_AFFINE
        or int(row["K"]) != K
        or int(row["gamma"]) != gamma
        or int(row["affine_block"]) != affine
        or int(row["shared_layer"]) != EXPECTED_SHARED
    ):
        raise AssertionError("frozen orientation parameters changed")
    if PRIME != A + S + A * S * R or 4 * K != PRIME * R + 1:
        raise AssertionError("source identities do not reconstruct")

    affine_factors = factorization(affine)
    gamma_difference = centered_difference(gamma, R)
    affine_difference = centered_difference(affine, R)
    shared_difference = centered_difference(EXPECTED_SHARED, R)
    target_pullback = {
        (-pow(residue, -1, R)) % R for residue in gamma_difference
    }
    raw = sorted(shared_difference & target_pullback)
    finite = sorted(affine_difference & target_pullback)

    primitive_root = int(sympy.primitive_root(R))
    group_order = R - 1
    affine_logs = {
        str(prime): int(sympy.discrete_log(R, prime % R, primitive_root))
        for prime, _ in affine_factors
    }
    if primitive_root != 7 or group_order != 358:
        raise AssertionError("unexpected unit-group generator")
    if affine_logs != {"19": 157, "135173": 201}:
        raise AssertionError("affine discrete-log coordinates changed")
    subgroup = {
        pow(primitive_root, exponent, R) for exponent in range(group_order)
    }
    subgroup_visible = sorted(residue for residue in raw if residue in subgroup)
    if set(subgroup_visible) != set(raw):
        raise AssertionError("the affine block does not generate the full unit group")

    overflow_rows = []
    for residue in subgroup_visible:
        log = int(sympy.discrete_log(R, residue, primitive_root))
        overflow, vector = minimum_overflow(
            residue, R, affine_factors, max_overflow=group_order
        )
        overflow_rows.append(
            {
                "residue": residue,
                "discrete_log": log,
                "minimum_extra_exponent": overflow,
                "witness_vector": list(vector),
            }
        )
    distribution = Counter(
        str(int(row_value["minimum_extra_exponent"])) for row_value in overflow_rows
    )
    if len(raw) != 60 or len(finite) != 0 or len(subgroup_visible) != 60:
        raise AssertionError("cyclic-log separation counts changed")
    if min(map(int, distribution)) != 12 or max(map(int, distribution)) != 77:
        raise AssertionError("cyclic-log overflow range changed")

    return {
        "arithmetic": (
            "exact centered prime-exponent boxes modulo R, a primitive-root discrete-log map, "
            "and exhaustive two-coordinate exponent boxes through the full group order"
        ),
        "scope_note": (
            "This is an exact boundary certificate for one F-state. It refutes the implication "
            "'shared pullback lies in the affine generated subgroup' => 'finite affine box aligns'; "
            "it neither refutes nor proves the universal mixed terminal selector."
        ),
        "prime": PRIME,
        "R": R,
        "source_state": {"a": A, "s": S},
        "K": K,
        "gamma": gamma,
        "affine_block": affine,
        "shared_layer": EXPECTED_SHARED,
        "gamma_factorization": factor_payload(gamma),
        "affine_factorization": factor_payload(affine),
        "shared_layer_factorization": factor_payload(EXPECTED_SHARED),
        "gamma_difference_count": len(gamma_difference),
        "target_pullback_count": len(target_pullback),
        "shared_difference_count": len(shared_difference),
        "raw_shared_pullback_count": len(raw),
        "subgroup_shared_pullback_count": len(subgroup_visible),
        "finite_shared_alignment_count": len(finite),
        "primitive_root": primitive_root,
        "unit_group_order": group_order,
        "affine_discrete_logs": affine_logs,
        "affine_finite_difference_residues": sorted(affine_difference),
        "raw_shared_pullback_residues": raw,
        "overflow_distribution": dict(
            sorted(distribution.items(), key=lambda item: int(item[0]))
        ),
        "minimum_overflow": min(distribution, key=int),
        "maximum_overflow": max(distribution, key=int),
        "overflow_rows": overflow_rows,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "overflow_rows"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
