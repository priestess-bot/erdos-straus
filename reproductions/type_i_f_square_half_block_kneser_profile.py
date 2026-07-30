#!/usr/bin/env python3
"""Profile the half-block Kneser defect on the frozen square-terminal states."""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-square-half-block-kneser-profile-results.json"
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"

SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"


def load_source():
    spec = importlib.util.spec_from_file_location("half_block_kneser_source", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def divisor_residues(value: int, modulus: int) -> frozenset[int]:
    factors = source.exact_factorization(value)
    residues = {1 % modulus}
    for prime, exponent in factors:
        residues = {
            residue * pow(prime, power, modulus) % modulus
            for residue in residues
            for power in range(exponent + 1)
        }
    return frozenset(residues)


def stabilizer(product_set: frozenset[int], modulus: int) -> frozenset[int]:
    # Since 1 is in every divisor spectrum, every stabilizer element is in product_set.
    return frozenset(
        candidate
        for candidate in product_set
        if {candidate * residue % modulus for residue in product_set}
        == set(product_set)
    )


def subgroup_certificate_order(certificate: dict[str, object]) -> int:
    component_orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    hnf = sympy.Matrix(certificate["column_lattice_hermite_normal_form"])
    index = abs(int(hnf.det()))
    full_order = math.prod(component_orders)
    if index < 1 or full_order % index:
        raise AssertionError("support lattice index does not divide unit-group order")
    return full_order // index


@lru_cache(maxsize=None)
def component_data(modulus: int) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    factors = source.exact_factorization(modulus)
    component_moduli = tuple(prime**exponent for prime, exponent in factors)
    orders = tuple(int(sympy.totient(value)) for value in component_moduli)
    roots = tuple(int(sympy.primitive_root(value)) for value in component_moduli)
    return component_moduli, orders, roots


@lru_cache(maxsize=None)
def generator_log(modulus: int, generator: int) -> tuple[int, ...]:
    component_moduli, _orders, roots = component_data(modulus)
    return tuple(
        int(sympy.discrete_log(component, generator % component, root))
        for component, root in zip(component_moduli, roots)
    )


def support_subgroup_order(modulus: int, generators: tuple[int, ...]) -> int:
    _component_moduli, orders, _roots = component_data(modulus)
    logs = [list(generator_log(modulus, generator)) for generator in generators]
    hnf = source.component_lattice_hnf(logs, list(orders))
    full_order = math.prod(orders)
    index = abs(int(hnf.det()))
    if index < 1 or full_order % index:
        raise AssertionError("support lattice index does not divide unit-group order")
    return full_order // index


def minimum_full_support(
    modulus: int, support_primes: tuple[int, ...], target_order: int
) -> tuple[int, tuple[int, ...]]:
    for rank in range(len(support_primes) + 1):
        for subset in itertools.combinations(support_primes, rank):
            if support_subgroup_order(modulus, (2, *subset)) == target_order:
                return rank, tuple(subset)
    raise AssertionError("the full support subgroup was not recovered")


def run(input_path: Path = INPUT) -> dict[str, object]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen square-terminal input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    candidates = [dict(row) for row in payload.get("candidates", [])]
    if len(candidates) != 253:
        raise AssertionError("expected the 253 frozen square-terminal candidates")

    records: list[dict[str, object]] = []
    two_power_membership: Counter[str] = Counter()
    stabilizer_sizes: Counter[int] = Counter()
    slack_counts: Counter[int] = Counter()
    quotient_order_counts: Counter[int] = Counter()
    full_support_rank_counts: Counter[int] = Counter()
    full_support_rank_by_two_power: dict[str, Counter[int]] = {
        "minus_one_in_<2>": Counter(),
        "two_adic_escape": Counter(),
    }
    R_counts: Counter[int] = Counter()
    all_f = True
    all_kneser_valid = True
    all_stabilizers_valid = True
    for row in sorted(
        candidates,
        key=lambda item: (
            int(item["prime"]),
            int(item["R"]),
            int(item["source"]),
            int(item["E"]),
        ),
    ):
        prime = int(row["prime"])
        R = int(row["R"])
        a = int(row["a"])
        s = int(row["s"])
        if prime != a + s + a * s * R or prime % 24 != 1:
            raise AssertionError("candidate is not a core linear source")
        if R % 8 != 3 or a % 4 != 3 or s % 4 != 3:
            raise AssertionError("square-terminal parity profile changed")
        G = (a * R + 1) // 2
        H_block = (s * R + 1) // 2
        K = G * H_block
        if 4 * K != prime * R + 1:
            raise AssertionError("half-block product does not reconstruct K")
        X = divisor_residues(G, R)
        Y = divisor_residues(H_block, R)
        product_set = frozenset((x * y) % R for x in X for y in Y)
        if product_set != divisor_residues(K, R):
            raise AssertionError("half-block divisor spectrum factorization failed")
        factors = source.exact_factorization(K)
        certificate = source.unit_group_subgroup_certificate(factors, R)
        H_order = subgroup_certificate_order(certificate)
        if not certificate["target_in_generated_subgroup"]:
            all_f = False
        if product_set & frozenset({(-value) % R for value in product_set}):
            raise AssertionError("a frozen candidate unexpectedly hits -1")
        T = stabilizer(product_set, R)
        if not T or 1 not in T:
            raise AssertionError("stabilizer lost the identity")
        if any((x * y) % R not in T for x in T for y in T):
            all_stabilizers_valid = False
        XT = frozenset((x * t) % R for x in X for t in T)
        YT = frozenset((y * t) % R for y in Y for t in T)
        lhs = len(XT) + len(YT) - len(T)
        if H_order % 2:
            raise AssertionError("F-state support subgroup must have even order")
        half_order = H_order // 2
        slack = half_order - lhs
        if slack < 0:
            all_kneser_valid = False
        if len(product_set) * 2 > H_order:
            raise AssertionError("F antipodal density boundary failed")
        two_order = int(sympy.n_order(2, R))
        minus_one_in_two = two_order % 2 == 0 and pow(2, two_order // 2, R) == R - 1
        two_power_membership["minus_one_in_<2>" if minus_one_in_two else "two_adic_escape"] += 1
        stabilizer_sizes[len(T)] += 1
        slack_counts[slack] += 1
        quotient_order = H_order // len(T)
        quotient_order_counts[quotient_order] += 1
        support_primes = tuple(sorted(prime for prime, _exponent in factors))
        full_rank, full_support = minimum_full_support(R, support_primes, H_order)
        full_support_rank_counts[full_rank] += 1
        branch = "minus_one_in_<2>" if minus_one_in_two else "two_adic_escape"
        full_support_rank_by_two_power[branch][full_rank] += 1
        R_counts[R] += 1
        records.append(
            {
                "prime": prime,
                "R": R,
                "a": a,
                "s": s,
                "K": K,
                "G": G,
                "H": H_block,
                "G_factorization": [[int(q), int(e)] for q, e in source.exact_factorization(G)],
                "H_factorization": [[int(q), int(e)] for q, e in source.exact_factorization(H_block)],
                "X_size": len(X),
                "Y_size": len(Y),
                "product_set_size": len(product_set),
                "generated_subgroup_order": H_order,
                "target_in_generated_subgroup": bool(certificate["target_in_generated_subgroup"]),
                "minus_one_in_two_power_subgroup": minus_one_in_two,
                "order_of_two_mod_R": two_order,
                "stabilizer": sorted(T),
                "stabilizer_size": len(T),
                "quotient_order": quotient_order,
                "full_support_rank_with_two": full_rank,
                "full_support_primes": list(full_support),
                "kneser_lhs": lhs,
                "half_order": half_order,
                "kneser_slack": slack,
                "strict_kneser_violation": slack < 0,
            }
        )

    equality = sum(int(row["kneser_slack"]) == 0 for row in records)
    two_power_rows = [row for row in records if row["minus_one_in_two_power_subgroup"]]
    escape_rows = [row for row in records if not row["minus_one_in_two_power_subgroup"]]
    return {
        "arithmetic": (
            "For every frozen square-terminal candidate, factor the two half-blocks, compute "
            "the exact divisor product set and its multiplicative stabilizer, and measure the "
            "two-block Kneser half-density defect in H_R(K)."
        ),
        "scope_note": (
            "Finite structural profile only. These 253 states are all F-type square-terminal "
            "witnesses from the frozen overflow audit; the profile does not prove that every "
            "linear state has this parity, nor that Kneser equality yields a cross-state descent."
        ),
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "candidate_count": len(records),
        "unique_R_count": len(R_counts),
        "all_target_in_generated_subgroup": all_f,
        "all_kneser_inequalities_valid": all_kneser_valid,
        "all_stabilizers_closed": all_stabilizers_valid,
        "two_power_split": dict(sorted(two_power_membership.items())),
        "two_power_rows": len(two_power_rows),
        "two_adic_escape_rows": len(escape_rows),
        "kneser_equality_count": equality,
        "kneser_strict_slack_count": len(records) - equality,
        "stabilizer_size_histogram": {str(k): int(v) for k, v in sorted(stabilizer_sizes.items())},
        "kneser_slack_histogram": {str(k): int(v) for k, v in sorted(slack_counts.items())},
        "quotient_order_histogram": {str(k): int(v) for k, v in sorted(quotient_order_counts.items())},
        "full_support_rank_with_two_histogram": {
            str(k): int(v) for k, v in sorted(full_support_rank_counts.items())
        },
        "full_support_rank_with_two_by_two_power": {
            branch: {str(k): int(v) for k, v in sorted(counter.items())}
            for branch, counter in full_support_rank_by_two_power.items()
        },
        "records": records,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        key: result[key]
        for key in (
            "candidate_count",
            "unique_R_count",
            "all_target_in_generated_subgroup",
            "all_kneser_inequalities_valid",
            "two_power_split",
            "kneser_equality_count",
            "stabilizer_size_histogram",
            "kneser_slack_histogram",
            "full_support_rank_with_two_histogram",
            "full_support_rank_with_two_by_two_power",
        )
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
