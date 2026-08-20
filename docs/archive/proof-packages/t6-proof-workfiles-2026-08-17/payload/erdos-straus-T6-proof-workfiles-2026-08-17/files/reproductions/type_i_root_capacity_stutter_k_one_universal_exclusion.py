#!/usr/bin/env python3
"""Verify symbolic identities in the proper-root k=1 infinite descent.

This verifier deliberately performs no bounded search.  The universal order
arguments and the well-founded descent are proved in the accompanying claim;
the script checks their exact polynomial identities over the integers.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

VARIABLES = ("A", "B", "c", "d", "e", "g", "x", "y")
ZERO_EXPONENTS = (0,) * len(VARIABLES)


@dataclass(frozen=True)
class Polynomial:
    """A minimal exact multivariate polynomial over the integers."""

    terms: dict[tuple[int, ...], int]

    def __post_init__(self) -> None:
        normalized = {
            powers: coefficient
            for powers, coefficient in self.terms.items()
            if coefficient != 0
        }
        object.__setattr__(self, "terms", normalized)

    @classmethod
    def constant(cls, value: int) -> Polynomial:
        return cls({ZERO_EXPONENTS: value})

    @classmethod
    def variable(cls, name: str) -> Polynomial:
        powers = [0] * len(VARIABLES)
        powers[VARIABLES.index(name)] = 1
        return cls({tuple(powers): 1})

    @staticmethod
    def coerce(value: int | Polynomial) -> Polynomial:
        if isinstance(value, Polynomial):
            return value
        return Polynomial.constant(value)

    def __add__(self, other: int | Polynomial) -> Polynomial:
        result = dict(self.terms)
        for powers, coefficient in self.coerce(other).terms.items():
            result[powers] = result.get(powers, 0) + coefficient
        return Polynomial(result)

    def __radd__(self, other: int | Polynomial) -> Polynomial:
        return self + other

    def __neg__(self) -> Polynomial:
        return Polynomial(
            {powers: -coefficient for powers, coefficient in self.terms.items()}
        )

    def __sub__(self, other: int | Polynomial) -> Polynomial:
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Polynomial) -> Polynomial:
        return self.coerce(other) - self

    def __mul__(self, other: int | Polynomial) -> Polynomial:
        result: dict[tuple[int, ...], int] = {}
        for left_powers, left_coefficient in self.terms.items():
            for right_powers, right_coefficient in self.coerce(other).terms.items():
                powers = tuple(
                    left + right
                    for left, right in zip(left_powers, right_powers, strict=True)
                )
                result[powers] = (
                    result.get(powers, 0) + left_coefficient * right_coefficient
                )
        return Polynomial(result)

    def __rmul__(self, other: int | Polynomial) -> Polynomial:
        return self * other

    def __pow__(self, exponent: int) -> Polynomial:
        if exponent < 0:
            raise ValueError("polynomial exponent must be nonnegative")
        result = Polynomial.constant(1)
        base = self
        power = exponent
        while power:
            if power % 2:
                result *= base
            base *= base
            power //= 2
        return result


def assert_zero(polynomial: Polynomial, label: str) -> None:
    if polynomial.terms:
        raise AssertionError(f"{label} failed: {polynomial.terms}")


def verify_root_gcd_identity() -> None:
    a_cap = Polynomial.variable("A")
    b_cap = Polynomial.variable("B")
    e_var = Polynomial.variable("e")
    g_var = Polynomial.variable("g")
    h_cap = a_cap**2 - a_cap * b_cap + b_cap**2
    p_times_a = e_var * g_var * h_cap - b_cap

    left = p_times_a**2 + a_cap * p_times_a + a_cap**2
    bracket = (
        e_var**2 * g_var**2 * h_cap
        + e_var * g_var * (a_cap - 2 * b_cap)
        + 1
    )
    assert_zero(left - h_cap * bracket, "actual-root common-divisor identity")


def verify_parameterization_and_integrality() -> None:
    d_var = Polynomial.variable("d")
    x_var = Polynomial.variable("x")
    y_var = Polynomial.variable("y")

    e_var = d_var * x_var**2
    a_var = d_var * x_var * y_var - 1
    b_var = e_var - 1
    q_form = x_var**2 - x_var * y_var + y_var**2
    m_var = d_var * q_form - 1
    h_var = e_var * m_var - a_var
    norm = a_var**2 - a_var * b_var + b_var**2
    h_closed = d_var**2 * x_var**2 * q_form - d_var * x_var * (x_var + y_var) + 1

    assert_zero(norm - h_var, "k=1 norm parameterization")
    assert_zero(h_var - h_closed, "closed formula for h")

    numerator = e_var * (h_var - 1) + 1
    cubic = (x_var - y_var) * (x_var**2 - x_var * y_var - y_var**2)
    quotient = x_var**2 * (
        d_var**2 * x_var**3 * y_var**2
        - d_var**2 * x_var**2 * y_var**3
        + d_var**2 * x_var * y_var**4
        + d_var * x_var**2 * y_var
        - 2 * d_var * x_var * y_var**2
        + x_var
        - 2 * y_var
    )
    assert_zero(
        y_var**3 * numerator - cubic - a_var * quotient,
        "p-integrality cubic remainder",
    )

    assert_zero(
        x_var * a_var - y_var * b_var - (y_var - x_var),
        "linear gcd identity",
    )
    assert_zero(b_var - a_var - d_var * x_var * (x_var - y_var), "gcd bridge")


def verify_descent_invariant() -> None:
    c_var = Polynomial.variable("c")
    d_var = Polynomial.variable("d")
    x_var = Polynomial.variable("x")
    y_var = Polynomial.variable("y")
    ell = d_var * c_var + 1

    a_var = d_var * x_var * y_var - 1
    p_two = x_var**2 - x_var * y_var - y_var**2
    positive_decomposition = (
        (d_var - 1) * x_var**2 * y_var
        + (y_var - 1) * (x_var**2 + x_var)
        + y_var**2
    )
    assert_zero(x_var * a_var - p_two - positive_decomposition, "c<x identity")

    def equation(first: Polynomial, second: Polynomial) -> Polynomial:
        return first**2 - ell * first * second - second**2 + c_var

    q_var = x_var - ell * y_var
    r_var = y_var - ell * q_var
    assert_zero(equation(q_var, r_var) - equation(x_var, y_var), "Vieta invariant")

    assert_zero(
        equation(x_var, y_var)
        - (x_var * q_var - (y_var**2 - c_var)),
        "first Vieta quotient identity",
    )
    assert_zero(
        equation(x_var, y_var)
        - (q_var**2 + c_var - y_var * r_var),
        "second Vieta quotient identity",
    )


def verify() -> None:
    verify_root_gcd_identity()
    verify_parameterization_and_integrality()
    verify_descent_invariant()
    print("verified proper-root k=1 symbolic identities and Vieta descent invariant")
    print("no bounded scan is used; order and well-foundedness are proved in the claim")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
