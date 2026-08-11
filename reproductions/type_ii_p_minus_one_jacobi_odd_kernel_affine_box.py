#!/usr/bin/env python3
"""Verify the Jacobi C2-to-odd-kernel affine-box reduction."""

from __future__ import annotations

import argparse
from itertools import product

import sympy

from type_ii_p_minus_one_jacobi_source_localization import derive_state


def state_data(prime: int, cofactor: int, generator: int) -> dict:
    state = derive_state(prime, cofactor)
    modulus = state.modulus
    order = int(sympy.n_order(generator, modulus))
    if order != int(sympy.totient(modulus)) or order % 2 != 0:
        raise AssertionError("generator is not cyclic of order 2s")
    s = order // 2
    factors = {
        int(value): int(exponent)
        for value, exponent in sympy.factorint(state.first_denominator).items()
    }
    logs = {
        prime_factor: int(sympy.discrete_log(modulus, prime_factor, generator))
        for prime_factor in factors
    }
    beta = {prime_factor: logs[prime_factor] % 2 for prime_factor in factors}
    negative = tuple(
        prime_factor for prime_factor in factors if beta[prime_factor] == 1
    )
    b_values = {
        prime_factor: (logs[prime_factor] - beta[prime_factor]) // 2
        for prime_factor in factors
    }
    return {
        "state": state,
        "s": s,
        "factors": factors,
        "logs": logs,
        "beta": beta,
        "negative": negative,
        "b": b_values,
    }


def direct_target(data: dict, vector: tuple[int, ...]) -> bool:
    residue = 1
    for prime_factor, exponent in zip(data["factors"], vector, strict=True):
        residue = (
            residue
            * pow(prime_factor, exponent, data["state"].modulus)
            % data["state"].modulus
        )
    return residue == data["state"].modulus - 1


def reduced_target(data: dict, vector: tuple[int, ...]) -> bool:
    negative = data["negative"]
    parity = sum(vector[data["factor_order"].index(prime_factor)] for prime_factor in negative)
    if parity % 2 != 1:
        return False
    s = data["s"]
    b_sum = sum(
        data["b"][prime_factor] * coordinate
        for prime_factor, coordinate in zip(
            data["factor_order"], vector, strict=True
        )
    )
    return (b_sum + (parity - 1) // 2) % s == (s - 1) // 2


def reduced_mode_solutions(data: dict) -> dict[tuple[int, ...], list[tuple[int, ...]]]:
    factors = data["factor_order"]
    negative = data["negative"]
    positive = tuple(prime_factor for prime_factor in factors if prime_factor not in negative)
    solutions: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for delta in product((0, 1), repeat=len(negative)):
        if sum(delta) % 2 != 1:
            continue
        negative_ranges = tuple(
            range(
                (-data["factors"][prime_factor] - bit + 1) // 2,
                (data["factors"][prime_factor] - bit) // 2 + 1,
            )
            for prime_factor, bit in zip(negative, delta, strict=True)
        )
        positive_ranges = tuple(
            range(
                -data["factors"][prime_factor],
                data["factors"][prime_factor] + 1,
            )
            for prime_factor in positive
        )
        rhs = (
            (data["s"] - 1) // 2
            - sum(
                data["b"][prime_factor] * bit
                for prime_factor, bit in zip(negative, delta, strict=True)
            )
            - (sum(delta) - 1) // 2
        ) % data["s"]
        rows = []
        for negative_values, positive_values in product(
            product(*negative_ranges),
            product(*positive_ranges) if positive_ranges else [()],
        ):
            lhs = (
                sum(
                    data["logs"][prime_factor] * value
                    for prime_factor, value in zip(
                        negative, negative_values, strict=True
                    )
                )
                + sum(
                    data["b"][prime_factor] * value
                    for prime_factor, value in zip(
                        positive, positive_values, strict=True
                    )
                )
            ) % data["s"]
            if lhs == rhs:
                rows.append(negative_values + positive_values)
        solutions[delta] = rows
    return solutions


def verify_fixture(
    prime: int,
    cofactor: int,
    generator: int,
    expected_nonempty: bool,
    expected_hit: tuple[int, ...] | None = None,
) -> None:
    data = state_data(prime, cofactor, generator)
    data["factor_order"] = tuple(data["factors"])
    solutions = reduced_mode_solutions(data)
    has_solution = any(solutions.values())
    if has_solution != expected_nonempty:
        raise AssertionError(
            f"reduced odd box status changed for p={prime}, q={cofactor}: "
            f"{solutions}"
        )

    ranges = tuple(
        range(-data["factors"][prime_factor], data["factors"][prime_factor] + 1)
        for prime_factor in data["factor_order"]
    )
    for vector in product(*ranges):
        if direct_target(data, vector) != reduced_target(data, vector):
            raise AssertionError(
                f"C2-to-odd reduction failed for p={prime}, q={cofactor}, "
                f"z={vector}"
            )

    if expected_hit is not None:
        if not direct_target(data, expected_hit):
            raise AssertionError("declared target vector is not a target hit")
        if not reduced_target(data, expected_hit):
            raise AssertionError("declared target vector missed reduced equation")


def verify() -> None:
    verify_fixture(73, 2, 3, True, expected_hit=(-2, -1))
    verify_fixture(337, 6, 5, True, expected_hit=(0, -2, -1))
    verify_fixture(67_369, 7, 2, False)
    verify_fixture(67_369, 21, 2, False)
    verify_fixture(67_369, 42, 5, False)

    data_q7 = state_data(67_369, 7, 2)
    data_q7["factor_order"] = tuple(data_q7["factors"])
    if set(reduced_mode_solutions(data_q7)) != {(0, 1), (1, 0)}:
        raise AssertionError("q=7 parity-mode decomposition changed")

    print("PASS: TYPE_II_P_MINUS_ONE_JACOBI_ODD_KERNEL_AFFINE_BOX")
    print("p73=odd_kernel_hit")
    print("p337=odd_kernel_hit_under_source_collision")
    print("p67369=q7_q21_q42=odd_kernel_box_empty")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
