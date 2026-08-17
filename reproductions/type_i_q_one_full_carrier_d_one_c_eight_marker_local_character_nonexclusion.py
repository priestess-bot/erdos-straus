#!/usr/bin/env python3
"""Verify arithmetic certificates for the c=8 marker local no-go theorem.

The accompanying claim uses the standard Chebotarev density theorem for its
infinite-prime conclusion.  This script verifies only the exact, finite
arithmetic inputs: the P/G transport identity, discriminants, Frobenius-cycle
certificates modulo 3 and 19, and the two marker residue rows.  It performs no
search over source parameters, primes, or certificates.
"""

from __future__ import annotations

import argparse


# Coefficients are in descending degree order.
P = (121, -396, 346, 4, -79)
G = (1, -4, -27_334, 2_471_436, -59_657_719)

DISC_P = -(2**12) * 5**3 * 11**3 * 23 * 163
DISC_G = DISC_P * 79**6


def bareiss_determinant(matrix: list[list[int]]) -> int:
    """Return an exact determinant using fraction-free elimination."""
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            for replacement in range(pivot_index + 1, size):
                if work[replacement][pivot_index] != 0:
                    work[pivot_index], work[replacement] = (
                        work[replacement],
                        work[pivot_index],
                    )
                    sign *= -1
                    break
            else:
                return 0
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise AssertionError("Bareiss division was not exact")
                work[row][column] = quotient
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def polynomial_discriminant(coefficients: tuple[int, ...]) -> int:
    """Compute a polynomial discriminant from its Sylvester determinant."""
    degree = len(coefficients) - 1
    derivative = tuple(
        coefficients[index] * (degree - index) for index in range(degree)
    )
    derivative_degree = degree - 1
    width = degree + derivative_degree
    matrix: list[list[int]] = []
    for shift in range(derivative_degree):
        matrix.append([0] * shift + list(coefficients) + [0] * (width - shift - len(coefficients)))
    for shift in range(degree):
        matrix.append([0] * shift + list(derivative) + [0] * (width - shift - len(derivative)))
    resultant = bareiss_determinant(matrix)
    sign = (-1) ** (degree * (degree - 1) // 2)
    value, remainder = divmod(sign * resultant, coefficients[0])
    if remainder:
        raise AssertionError("resultant did not divide by the leading coefficient")
    return value


def trim(poly: list[int]) -> list[int]:
    """Remove high zero coefficients from an ascending coefficient vector."""
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def polynomial_mod(poly: list[int], modulus_poly: list[int], prime: int) -> list[int]:
    """Reduce an ascending polynomial vector modulo a monic polynomial."""
    result = [coefficient % prime for coefficient in poly]
    modulus_poly = trim([coefficient % prime for coefficient in modulus_poly])
    inverse = pow(modulus_poly[-1], -1, prime)
    while result != [0] and len(result) >= len(modulus_poly):
        scale = result[-1] * inverse % prime
        offset = len(result) - len(modulus_poly)
        for index, coefficient in enumerate(modulus_poly):
            result[index + offset] = (result[index + offset] - scale * coefficient) % prime
        trim(result)
    return result


def multiply_mod(
    left: list[int], right: list[int], modulus_poly: list[int], prime: int
) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            product[left_index + right_index] = (
                product[left_index + right_index] + left_coefficient * right_coefficient
            ) % prime
    return polynomial_mod(product, modulus_poly, prime)


def power_mod(
    base: list[int], exponent: int, modulus_poly: list[int], prime: int
) -> list[int]:
    value = [1]
    base = polynomial_mod(base, modulus_poly, prime)
    while exponent:
        if exponent & 1:
            value = multiply_mod(value, base, modulus_poly, prime)
        base = multiply_mod(base, base, modulus_poly, prime)
        exponent //= 2
    return value


def polynomial_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    """Return a monic gcd for ascending vectors over F_prime."""
    left = trim([coefficient % prime for coefficient in left])
    right = trim([coefficient % prime for coefficient in right])
    while right != [0]:
        left, right = right, polynomial_mod(left, right, prime)
    inverse = pow(left[-1], -1, prime)
    return [(coefficient * inverse) % prime for coefficient in left]


def evaluate(coefficients: tuple[int, ...], value: int, prime: int) -> int:
    """Evaluate descending coefficients in F_prime."""
    result = 0
    for coefficient in coefficients:
        result = (result * value + coefficient) % prime
    return result


def multiply_descending(
    left: tuple[int, ...], right: tuple[int, ...], prime: int
) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_coefficient * right_coefficient
            ) % prime
    return tuple(result)


def verify_transport_and_discriminants() -> None:
    """Check that P and G have the same splitting field and discriminant class."""
    transported = (-79, 4 * 79, 346 * 79**2, -396 * 79**3, 121 * 79**4)
    if transported != tuple(-79 * coefficient for coefficient in G):
        raise AssertionError("lambda^4 P(79/lambda) = -79 G(lambda) changed")
    if not (
        polynomial_discriminant(P) == DISC_P
        and polynomial_discriminant(G) == DISC_G
        and DISC_G == DISC_P * 79**6
    ):
        raise AssertionError("quartic discriminant certificates changed")


def verify_s4_cycle_certificates() -> None:
    """Certify a 4-cycle mod 19 and a 3-cycle mod 3 for P."""
    prime = 19
    normalized_p = tuple(
        coefficient * pow(P[0], -1, prime) % prime for coefficient in P
    )
    normalized_g = tuple(coefficient % prime for coefficient in G)
    if normalized_p != (1, 14, 6, 6, 5):
        raise AssertionError("P's monic reduction modulo 19 changed")
    if normalized_g != (1, 15, 7, 11, 1):
        raise AssertionError("G's reduction modulo 19 changed")

    # Rabin's degree-four irreducibility criterion over F_19.
    for polynomial in (normalized_p, normalized_g):
        ascending = list(reversed(polynomial))
        x = [0, 1]
        x_q2 = power_mod(x, prime**2, ascending, prime)
        x_q4 = power_mod(x, prime**4, ascending, prime)
        difference = x_q2[:]
        difference[1] = (difference[1] - 1) % prime
        if not (x_q4 == x and polynomial_gcd(ascending, difference, prime) == [1]):
            raise AssertionError("mod-19 quartic is no longer irreducible")

    p_mod_3 = tuple(coefficient % 3 for coefficient in P)
    g_mod_3 = tuple(coefficient % 3 for coefficient in G)
    p_cubic = (1, 2, 2, 2)  # X^3-X^2-X-1
    g_cubic = (1, 1, 1, 2)  # X^3+X^2+X-1
    if not (
        p_mod_3 == multiply_descending((1, 1), p_cubic, 3)
        and g_mod_3 == multiply_descending((1, 1), g_cubic, 3)
        and all(evaluate(p_cubic, value, 3) for value in range(3))
        and all(evaluate(g_cubic, value, 3) for value in range(3))
    ):
        raise AssertionError("mod-3 one-plus-three cycle certificate changed")


def crt(left: int, left_modulus: int, right: int, right_modulus: int) -> int:
    """Return the least nonnegative solution of two coprime congruences."""
    return (
        left
        + left_modulus
        * ((right - left) * pow(left_modulus, -1, right_modulus) % right_modulus)
    ) % (left_modulus * right_modulus)


def verify_marker_residue_rows() -> None:
    """Recover the two q/lambda congruence rows forced by g_b=47."""
    if pow(41, 23, 47) != 46:
        raise AssertionError("41 should remain a quadratic nonresidue modulo 47")
    source_roots = tuple(
        s
        for s in range(47)
        if (9 * s * (176 * s + 5) * (3168 * s * s + 24 * s - 1)) % 47 == 0
    )
    if source_roots != (0, 20):
        raise AssertionError("47-support roots of M changed")

    rows = []
    for source_parameter in source_roots:
        prime = (48 * source_parameter + 1) % 47
        raw_prime = (prime * prime + prime - 1) % 47
        carry = ((32 * raw_prime + 79) * pow(prime, -1, 47)) % 47
        carry_mod_752 = crt(15, 16, carry, 47)
        rows.append((source_parameter, prime, raw_prime, carry, carry_mod_752))
    if tuple(rows) != ((0, 1, 1, 17, 111), (20, 21, 38, 46, 751)):
        raise AssertionError("c=8 marker q/lambda residue table changed")


def verify() -> None:
    verify_transport_and_discriminants()
    verify_s4_cycle_certificates()
    verify_marker_residue_rows()
    print(
        "verified c=8 marker local-character nonexclusion inputs: "
        "shared S4 quartic field, discriminant class, and two mod-47/mod-752 rows"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
