#!/usr/bin/env python3
"""Focused checks for prime-matched owner carriers and their descent boundary."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, lcm

from type_i_core_jacobi_punctured_kernel_primary_selector import (
    factorint,
    is_prime,
)
from type_i_odd_owner_scale_dichotomy_small_cofactor_terminal import divisors


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def radical(value: int) -> int:
    result = 1
    for prime, _ in factorint(value):
        result *= prime
    return result


def is_squarefree(value: int) -> bool:
    return all(exponent == 1 for _, exponent in factorint(value))


def euler_phi(value: int) -> int:
    result = value
    for prime, _ in factorint(value):
        result = result // prime * (prime - 1)
    return result


def multiplicative_order(value: int, modulus: int) -> int:
    assert gcd(value, modulus) == 1
    order = euler_phi(modulus)
    for prime, _ in factorint(order):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    assert pow(value, order, modulus) == 1
    return order


def beta(p: int, modulus: int) -> int:
    return (-p * pow(4, -1, modulus)) % modulus


def allowed_residues(q: int, j: int) -> tuple[int, ...]:
    modulus = q ** (j + 1)
    return tuple(
        residue
        for residue in range(1, modulus)
        if gcd(residue, q) == 1 and (q != 3 or residue % 3 == 2)
    )


def verify_cyclotomic_prime(q: int, r: int) -> None:
    cyclotomic_value = sum(q**exponent for exponent in range(q))
    assert is_prime(q) and q % 2 == 1
    assert is_prime(r) and cyclotomic_value % r == 0
    assert multiplicative_order(q, r) == q
    assert (r - 1) % q == 0 and (r - 1) % (q * q) != 0
    quotient = (r - 1) // q
    eta_q = pow(q, quotient, r)
    assert multiplicative_order(eta_q, r) == q
    assert pow(r - 1, quotient, r) == 1


def verify_fixed_template(
    *, q: int, j: int, r: int, u: int, v: int, lam: int, p: int
) -> dict[str, int | tuple[int, ...]]:
    modulus = q ** (j + 1)
    b = beta(p, modulus)
    assert b in allowed_residues(q, j)
    assert all(is_prime(value) for value in (p, r, u, v, lam))
    assert p % 24 == 1
    assert u % modulus == (1 + q**j) % modulus
    assert v % modulus == (1 - q**j) % modulus
    assert lam % modulus == b * pow(r, -1, modulus) % modulus
    assert len({r, u, v, lam}) == 4

    d_star = x = r * lam
    d0 = x * u * v
    endpoints = (d0, d0 * u)
    assert is_squarefree(d0)
    assert is_squarefree(d0 // u)
    assert d_star < d0 and 4 * endpoints[1] < p
    assert endpoints[0] % modulus == x % modulus == b
    assert endpoints[1] % modulus == b * (1 + q**j) % modulus

    heights = tuple(valuation(p + 4 * value, q) for value in endpoints)
    target_height = valuation(p + 4 * x, q)
    assert heights[0] >= j + 1 and heights[1] == j
    assert target_height >= j + 1
    assert ((endpoints[1] - endpoints[0]) // q**j) % q
    assert multiplicative_order(q, 4 * d_star) % q == 0
    return {
        "p": p,
        "b": b,
        "target": x,
        "d0": d0,
        "endpoints": endpoints,
        "heights": heights + (target_height,),
    }


def bezout_vector(values: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    current = 0
    coefficients: list[int] = []
    for value in values:
        old_current = current
        old_coefficients = coefficients
        a, b = old_current, value
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        while b:
            quotient, remainder = divmod(a, b)
            a, b = b, remainder
            x0, x1 = x1, x0 - quotient * x1
            y0, y1 = y1, y0 - quotient * y1
        current = abs(a)
        sign = 1 if a >= 0 else -1
        coefficients = [sign * x0 * item for item in old_coefficients]
        coefficients.append(sign * y0)
    assert sum(coefficient * value for coefficient, value in zip(coefficients, values)) == current
    return current, tuple(coefficients)


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    assert len(left) == len(right)
    return sum(a * b for a, b in zip(left, right))


def gamma_compatible_bezout(
    delta: tuple[int, ...], role: tuple[int, ...], q: int
) -> tuple[int, tuple[int, ...]]:
    content, _ = bezout_vector(delta)
    assert content > 0 and content % q
    primitive_delta = tuple(value // content for value in delta)
    primitive_content, primitive_bezout = bezout_vector(primitive_delta)
    assert primitive_content == 1
    role_value = dot(role, primitive_delta) % q
    assert role_value
    scalar = pow(role_value, -1, q)
    correction_target = (1 - scalar * dot(role, primitive_delta)) // q
    correction = tuple(correction_target * value for value in primitive_bezout)
    result = tuple(
        scalar * role_value_i + q * correction_i
        for role_value_i, correction_i in zip(role, correction)
    )
    assert dot(result, primitive_delta) == 1
    assert all((result_i - scalar * role_i) % q == 0 for result_i, role_i in zip(result, role))
    return content, result


def primitive_root(prime: int) -> int:
    assert is_prime(prime)
    factors = tuple(factor for factor, _ in factorint(prime - 1))
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("prime has no primitive root")


def discrete_log(base: int, value: int, prime: int) -> int:
    current = 1
    for exponent in range(prime - 1):
        if current == value % prime:
            return exponent
        current = current * base % prime
    raise AssertionError("value is not in the generated unit group")


def verify_adaptive_content_carrier() -> dict[str, int | tuple[int, ...]]:
    q, j, r, u = 3, 1, 13, 31
    source_difference = (4,)
    source_role = (1,)
    content, compatible_bezout = gamma_compatible_bezout(
        source_difference, source_role, q
    )
    assert content == 4 and dot(source_role, source_difference) % q

    modulus = q ** (j + 1)
    h = lcm(content, r, u)
    a0 = h // radical(h)
    assert h == 1612 and a0 == 2
    v, lam = 19, 37
    p = 281_043_793
    assert all(is_prime(value) for value in (p, r, u, v, lam))
    assert p % 24 == 1
    b = beta(p, modulus)
    assert b == 2
    assert v % modulus == 1 and gcd(v, h) == 1
    assert lam % modulus == b * pow(a0 * h, -1, modulus) % modulus
    assert gcd(lam, h * v) == 1

    d_star = h * lam
    target_a = a0
    target_c = radical(h) * lam
    x = target_a * d_star
    d0 = d_star * v
    source_as = (a0, a0 * u)
    endpoints = tuple(d0 * source_a for source_a in source_as)

    assert target_c == d_star // target_a and is_squarefree(target_c)
    assert all(d0 % source_a == 0 for source_a in source_as)
    assert all(is_squarefree(d0 // source_a) for source_a in source_as)
    assert d_star < d0 and 4 * endpoints[1] < p
    assert endpoints == (x * v, x * u * v)
    assert endpoints[0] % modulus == x % modulus == b
    assert endpoints[1] % modulus == b * (1 + q**j) % modulus
    heights = tuple(valuation(p + 4 * value, q) for value in endpoints)
    assert heights[0] >= 2 and heights[1] == 1
    assert valuation(p + 4 * x, q) >= 2
    assert ((endpoints[1] - endpoints[0]) // q**j) % q

    endpoint_delta = endpoints[1] - endpoints[0]
    assert endpoint_delta % content == 0
    affine_slope = endpoint_delta // content * compatible_bezout[0]
    assert endpoints[0] + affine_slope * source_difference[0] == endpoints[1]
    normalized_owner_form = tuple(
        endpoint_delta // (content * q**j) * value % q
        for value in compatible_bezout
    )
    pivot = next(index for index, value in enumerate(source_role) if value % q)
    owner_scalar = normalized_owner_form[pivot] * pow(source_role[pivot], -1, q) % q
    assert owner_scalar
    assert all(
        form_i == owner_scalar * role_i % q
        for form_i, role_i in zip(normalized_owner_form, source_role)
    )

    source_modulus = 4 * d0
    target_modulus = 4 * d_star
    assert source_modulus == target_modulus * v
    assert multiplicative_order(q, source_modulus) % q == 0
    assert pow(q, 2, source_modulus) != 1
    physical_block = {1, q % source_modulus}
    assert {q * value % source_modulus for value in physical_block} != physical_block

    kernel_size = v - 1
    assert len(physical_block) < kernel_size
    binary_slots_needed = (kernel_size - 1).bit_length()
    assert binary_slots_needed == 5

    generator = primitive_root(v)
    crt_step = (generator - 1) * pow(target_modulus, -1, v) % v
    kernel_element = 1 + target_modulus * crt_step
    assert kernel_element % target_modulus == 1
    assert kernel_element % v == generator
    assert gcd(kernel_element, source_modulus) == 1
    assert kernel_element != 1

    psi_q_exponent = discrete_log(generator, q, v)
    chosen_twist = None
    chosen_phase = None
    for twist in range(q):
        phase = (Fraction(psi_q_exponent, v - 1) + Fraction(twist, q)) % 1
        if phase != Fraction(1, 2):
            chosen_twist = twist
            chosen_phase = phase
            break
    assert chosen_twist is not None and chosen_phase != Fraction(1, 2)
    # eta is trivial on the reduction kernel because r divides D_*.
    assert kernel_element % r == 1
    assert pow(q, (r - 1) // q, r) != 1

    return {
        "p": p,
        "content": content,
        "h": h,
        "target": x,
        "d_star": d_star,
        "d0": d0,
        "endpoints": endpoints,
        "kernel_size": kernel_size,
        "binary_slots_needed": binary_slots_needed,
        "fourier_twist": chosen_twist,
    }


def verify_source_role_boundaries() -> None:
    q = 3
    delta = (1, 2)
    role = (0, 1)
    content, generic_bezout = bezout_vector(delta)
    assert content == 1 and generic_bezout == (1, 0)
    assert dot(generic_bezout, (1, 0)) % q
    assert dot(role, (1, 0)) % q == 0

    compatible_content, compatible = gamma_compatible_bezout(delta, role, q)
    assert compatible_content == 1 and dot(compatible, delta) == 1
    scalar = compatible[1] % q
    assert scalar
    assert all(
        compatible_i % q == scalar * role_i % q
        for compatible_i, role_i in zip(compatible, role)
    )

    # A nonzero character on the abstract sublattice 3Z need not extend to Z.
    naked_delta = (3,)
    naked_content, _ = bezout_vector(naked_delta)
    assert naked_content % q == 0
    assert all(coefficient * naked_delta[0] % q == 0 for coefficient in range(q))


def verify_prescribed_label_twist_obstruction() -> None:
    q = 3
    u = (1, 0)
    c = (0, 1)
    anchor = (4, 0)

    def psi_phase(value: tuple[int, int]) -> Fraction:
        return Fraction((value[0] + value[1]) % 2, 2)

    def eta_phase(value: tuple[int, int]) -> Fraction:
        return Fraction(value[0] % q, q)

    def chi_phase(value: tuple[int, int], twist: int) -> Fraction:
        return (psi_phase(value) + twist * eta_phase(value)) % 1

    assert psi_phase(c) == Fraction(1, 2)
    allowed_twists = tuple(
        twist for twist in range(q) if chi_phase(anchor, twist) == 0
    )
    assert allowed_twists == (0,)
    assert chi_phase(u, 0) == Fraction(1, 2)
    assert all(chi_phase(u, twist) != Fraction(1, 2) for twist in (1, 2))


def reduction_kernel(source_modulus: int, target_modulus: int) -> tuple[int, ...]:
    assert source_modulus % target_modulus == 0
    return tuple(
        residue
        for residue in range(1, source_modulus)
        if gcd(residue, source_modulus) == 1 and residue % target_modulus == 1
    )


def stabilizer(modulus: int, subset: set[int]) -> tuple[int, ...]:
    return tuple(
        unit
        for unit in range(1, modulus)
        if gcd(unit, modulus) == 1
        and {unit * value % modulus for value in subset} == subset
    )


def verify_old_kernel_controls() -> tuple[dict[str, object], ...]:
    controls = (
        (280, 56, (1, 57, 113, 169), (1, 169)),
        (520, 260, (1, 261), (1,)),
    )
    receipts = []
    for source_modulus, target_modulus, expected_kernel, expected_intersection in controls:
        kernel = reduction_kernel(source_modulus, target_modulus)
        assert kernel == expected_kernel
        order = multiplicative_order(3, source_modulus)
        q_cycle = {pow(3, exponent, source_modulus) for exponent in range(order)}
        intersection = tuple(sorted(set(kernel) & q_cycle))
        assert intersection == expected_intersection
        assert not set(kernel) <= q_cycle
        assert stabilizer(source_modulus, {1, 3}) == (1,)
        receipts.append(
            {
                "source_modulus": source_modulus,
                "target_modulus": target_modulus,
                "kernel": kernel,
                "q_cycle_intersection": intersection,
            }
        )
    return tuple(receipts)


def marked_tail_solutions(n: int, a: int) -> tuple[tuple[int, int], ...]:
    coefficient = 4 * a - n
    product_root = n * a
    assert coefficient > 0
    solutions = []
    for factor in divisors(product_root * product_root):
        complement = product_root * product_root // factor
        if (product_root + factor) % coefficient:
            continue
        if (product_root + complement) % coefficient:
            continue
        b = (product_root + factor) // coefficient
        c = (product_root + complement) // coefficient
        if b <= c:
            assert Fraction(4, n) == Fraction(1, a) + Fraction(1, b) + Fraction(1, c)
            solutions.append((b, c))
    return tuple(solutions)


def verify_natural_marked_lift_no_go() -> dict[str, object]:
    p, q, j, x = 2113, 3, 1, 14
    n = (p + 4 * x) // q ** (j + 1)
    assert n == 241 and n < p
    expected = {
        62: ((2139, 1_030_998), (2169, 134_478)),
        63: ((1386, 334_026), (1446, 30_366)),
        66: ((693, 334_026), (723, 15_906)),
    }
    nonempty = {}
    divisibility_receipts = {}
    for a in range(61, 69):
        solutions = marked_tail_solutions(n, a)
        if solutions:
            nonempty[a] = solutions
        delta = n * p - 4 * (p - n) * a
        assert delta > 0
        divisibility_receipts[a] = (delta, n * p * a % delta)
        assert not (solutions and n * p * a % delta == 0)
    assert nonempty == expected
    assert {a: divisibility_receipts[a] for a in expected} == {
        62: (44_977, 43_569),
        63: (37_489, 28_584),
        66: (15_025, 13_478),
    }
    return {
        "p": p,
        "n": n,
        "source_coordinates_with_tails": tuple(nonempty),
        "marked_fiber_empty": True,
    }


def verify() -> None:
    verify_cyclotomic_prime(3, 13)
    verify_cyclotomic_prime(5, 11)
    assert allowed_residues(3, 1) == (2, 5, 8)
    assert len(allowed_residues(5, 1)) == 20
    assert gcd(3, 4 * 39) != 1  # r=13 divides D=39, but [3] is not a unit.

    fixed_q3 = (
        verify_fixed_template(q=3, j=1, r=13, u=31, v=7, lam=5, p=5_946_697),
        verify_fixed_template(q=3, j=1, r=13, u=31, v=7, lam=17, p=5_946_793),
        verify_fixed_template(q=3, j=1, r=13, u=31, v=7, lam=2, p=5_947_177),
    )
    assert tuple(receipt["b"] for receipt in fixed_q3) == (2, 5, 8)
    fixed_q5 = verify_fixed_template(
        q=5, j=1, r=11, u=31, v=71, lam=41, p=123_092_521
    )
    assert fixed_q5["heights"] == (4, 1, 2)
    assert all(
        multiplicative_order(3, modulus) % prime
        for modulus in (56, 260)
        for prime in (5, 7, 11)
    )

    # The fixed q=3 rows cannot admit a content-11 affine source pair.
    assert 210 % 11 and 390 % 11
    verify_source_role_boundaries()
    adaptive = verify_adaptive_content_carrier()
    verify_prescribed_label_twist_obstruction()
    kernels = verify_old_kernel_controls()
    marked = verify_natural_marked_lift_no_go()

    print(
        "verified: residue counts and fixed-template controls",
        {"q3_residues": (2, 5, 8), "q5_menu_size": 20},
    )
    print("verified: content-adaptive affine carrier", adaptive)
    print("verified: strict-kernel stabilizer/Fourier boundary", kernels)
    print("verified: natural marked-lift no-go", marked)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
