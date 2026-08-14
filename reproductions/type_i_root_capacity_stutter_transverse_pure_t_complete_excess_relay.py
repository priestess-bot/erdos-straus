#!/usr/bin/env python3
"""Verify fixed pure-T q-primary normalization and checkpoint relay controls."""

from __future__ import annotations

import argparse
from math import gcd


LOW_GAPS = (3, 7, 11, 23)
LOW_GAP_ROOT_BOX_FACTORS = {
    3: (7,),
    7: (43,),
    11: (3, 37),
    23: (3, 13, 13),
}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise AssertionError("valuation control unexpectedly vanished")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_negative_root_shape(
    p: int, q: int, gap: int, height: int, m_value: int
) -> int:
    """Check the shared q-local L>1 negative-root data, not an actual receipt."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and gap in LOW_GAPS):
        raise AssertionError("control did not retain a core prime and low-gap carrier")
    if q % (2 * gap) != 2 * gap - 1:
        raise AssertionError("control lost the even-K negative-root residue")
    k_value, remainder = divmod(q + 1, gap)
    if remainder or k_value % 2:
        raise AssertionError("control lost the even negative-root K")
    l_value = k_value - 1
    local_d = m_value * p + 1 - height
    if not (
        l_value > 1
        and local_d > 0
        and local_d % q == 0
        and (p * height + 1) % q == 0
        and (gap * (height - 1) + 1) % q == 0
        and (l_value * p - 1) % q == 0
        and height % q == (-l_value) % q
        and m_value % q == (-l_value * (l_value + 1)) % q
        and (height * height - 1) % q != 0
        and (p * p - 1) % q != 0
        and (2 * p + 1) % q != 0
        and m_value % q != 0
        and (m_value + 2) % q != 0
        and (m_value - 1) % q != 0
    ):
        raise AssertionError("control left the pure-T negative-root branch")
    return l_value


def verify_actual_stutter_cross_mod_control() -> None:
    """Check the full actual stutter identities behind the cross-mod map."""
    p, r_value, height, m_value = 97, 6618, 58, 4
    d_value, receipt_quotient, sigma = 331, 17, 376206
    if not (is_prime(p) and p % 24 == 1 and 2 <= height < p):
        raise AssertionError("control did not retain a proper core-prime stutter shape")
    t_value = p * p * r_value - (p + 1) // 2
    k_value = (p * p - 1) // 2 * t_value
    r_polynomial = 2 * p**3 * r_value - p * p - 2 * p * r_value - p + 1
    e_multiplier = 1 + p * sigma
    m_plus_two_r = m_value + 2 * r_value
    if not (
        d_value == m_value * p + 1 - height
        and receipt_quotient * d_value == p * height + 1
        and r_polynomial - height == e_multiplier * d_value
        and k_value % (height * d_value) == 0
        and gcd(height, r_polynomial - height) == 1
        and sigma * d_value == 2 * t_value - m_plus_two_r
        and (p + receipt_quotient + sigma) * d_value
        == (p * p - 1) * m_plus_two_r
        and (sigma * (1 - height) + m_plus_two_r + 1) % p == 0
    ):
        raise AssertionError("actual stutter cross-mod identities changed")


def verify_actual_p_free_pblock_digit_control() -> None:
    """Check the actual p-adic digit required before a p-block q-entry can occur."""
    p, height, m_value, d_value, receipt_quotient = 97, 58, 4, 331, 17
    r_zero = 66_988_440
    r_step = 4_243_815_461_730_835_674_059_638_914_706_837_844_637
    e_zero = 369_377_901_007
    e_step = 23_400_629_237_489_299_674_263_740_436_419_983_401_253_504
    family_index = 79
    r_value = r_zero + family_index * r_step
    e_multiplier = e_zero + family_index * e_step
    t_value = (e_multiplier - 1) // (p * p)
    sigma = p * t_value
    t_capacity = p * p * r_value - (p + 1) // 2
    k_value = (p * p - 1) // 2 * t_capacity
    r_polynomial = 2 * p**3 * r_value - p * p - 2 * p * r_value - p + 1
    r_one = r_value + t_value * t_capacity
    f_one = 2 * (p - 1) * r_one - 1
    if not (
        is_prime(p)
        and p % 24 == 1
        and 2 <= height < p
        and e_multiplier == 1 + p * sigma
        and d_value == m_value * p + 1 - height
        and receipt_quotient * d_value == p * height + 1
        and r_polynomial - height == e_multiplier * d_value
        and k_value % (height * d_value) == 0
        and gcd(height, r_polynomial - height) == 1
        and sigma * d_value == 2 * t_capacity - (m_value + 2 * r_value)
        and (m_value + 2 * r_value + 1) % p == 0
        and f_one % p == (t_value + m_value) % p
        and valuation(f_one, p) == 1
        and (e_multiplier - (1 - p * p * m_value)) % (p**3) == 0
    ):
        raise AssertionError("actual p-free p-block digit gate changed")


def verify_low_gap_root_box_exclusion() -> None:
    """Check the finite obstruction to a negative-root carrier dividing p^2+p+1."""
    for gap, factors in LOW_GAP_ROOT_BOX_FACTORS.items():
        root_box_constant = gap * gap - gap + 1
        factor_product = 1
        for factor in factors:
            if not is_prime(factor):
                raise AssertionError("low-gap root-box table lost a prime factor")
            factor_product *= factor
            if factor % (2 * gap) == 2 * gap - 1:
                raise AssertionError("root-box factor entered the negative-root residue")
        if factor_product != root_box_constant:
            raise AssertionError("low-gap root-box factorization changed")


def verify_p_free_root_expulsion_control() -> None:
    """Check q remains in K_1 but not in the p-free return's root capacity."""
    p, q, r_value, t_value = 313, 17, 15, 9
    if verify_negative_root_shape(p, q, 3, 12, 4) != 5:
        raise AssertionError("p-free control lost its low-gap negative-root carrier")
    if (4 + 2 * r_value) % q:
        raise AssertionError("p-free control lost the pure-T synchronized q-layer")
    sigma = p * t_value
    e_multiplier = 1 + p * sigma
    t_capacity = p * p * r_value - (p + 1) // 2
    c_value = (p * p - 1) // 2
    k_value = c_value * t_capacity
    b_zero = 2 * p * r_value - 1
    n_zero = (p + 1) * b_zero - 1
    b_one = e_multiplier * b_zero - sigma
    n_one = e_multiplier * n_zero - sigma
    r_one = r_value + t_value * t_capacity
    t_one = p * p * r_one - (p + 1) // 2
    k_one = e_multiplier * k_value
    r_polynomial_one = (p - 1) * n_one - 1
    root_box = p * p + p + 1
    root_capacity = gcd(r_polynomial_one - (p + 1), k_one)
    if not (is_prime(p) and p % 24 == 1 and is_prime(q)):
        raise AssertionError("p-free q-primary control lost its core-prime shape")
    if not (
        e_multiplier % (p * p) == 1
        and valuation(e_multiplier, q) == 1
        and valuation(t_capacity, q) == 1
        and valuation(k_value, q) == 1
        and valuation(k_one, q) == 2
        and b_one == 2 * p * r_one - 1
        and n_one == (p + 1) * b_one - 1
        and t_one == e_multiplier * t_capacity
        and k_one == e_multiplier * k_value
        and root_box % q != 0
        and (p + 1) % q != 0
        and (p * (r_polynomial_one - (p + 1)) + root_box) % q == 0
        and (r_polynomial_one - (p + 1)) % q != 0
        and root_box % root_capacity == 0
        and root_capacity % q != 0
    ):
        raise AssertionError("p-free return no longer expels q from the root capacity")


def verify_p_free_pblock_reentry_control(
    *,
    label: str,
    p: int,
    q: int,
    gap: int,
    height: int,
    m_value: int,
    r_value: int,
    t_value: int,
    expected_p_height: int,
    expected_x_q_height: int,
) -> None:
    """Check the discrete-log q-entry gate in one p-free p-block control."""
    l_value = verify_negative_root_shape(p, q, gap, height, m_value)
    if (m_value + 2 * r_value) % q:
        raise AssertionError("p-block control lost the pure-T synchronized q-layer")
    sigma = p * t_value
    e_multiplier = 1 + p * sigma
    t_capacity = p * p * r_value - (p + 1) // 2
    c_value = (p * p - 1) // 2
    k_value = c_value * t_capacity
    b_zero = 2 * p * r_value - 1
    n_zero = (p + 1) * b_zero - 1
    b_one = e_multiplier * b_zero - sigma
    n_one = e_multiplier * n_zero - sigma
    r_one = r_value + t_value * t_capacity
    t_one = p * p * r_one - (p + 1) // 2
    k_one = e_multiplier * k_value
    f_one = 2 * (p - 1) * r_one - 1
    p_height = valuation(f_one, p)
    u_value = f_one // (p**p_height)
    y_value = (p + 1) * u_value
    x_value = 1 + (p ** (p_height + 1) - 1) * y_value
    r_polynomial_one = (p - 1) * n_one - 1
    gate_hit = pow(l_value, p_height, q) == gap % q
    q_capacity_height = valuation(k_one, q)
    q_x_height = valuation(x_value, q)
    if not (
        is_prime(p)
        and p % 24 == 1
        and valuation(t_capacity, q) == 1
        and valuation(e_multiplier, q) == 1
        and valuation(k_value, q) == 1
        and q_capacity_height == 2
        and b_one == 2 * p * r_one - 1
        and n_one == (p + 1) * b_one - 1
        and t_one == e_multiplier * t_capacity
        and k_one == e_multiplier * k_value
        and r_polynomial_one == x_value + y_value
        and 4 * k_one == p * r_polynomial_one + 1
        and p_height == expected_p_height
        and f_one % q == (-l_value * l_value) % q
        and y_value % q != 0
        and (x_value % q == 0) == gate_hit
        and q_x_height == expected_x_q_height
        and q_x_height <= q_capacity_height
    ):
        raise AssertionError(f"{label} p-free p-block reentry gate changed")


def verify_control(
    *,
    label: str,
    p: int,
    q: int,
    gap: int,
    height: int,
    m_value: int,
    r_value: int,
    sigma: int,
    d_value: int,
    expected_valuations: tuple[int, int, int, int, int, int],
    expected_checkpoint_suffix: int | None = None,
) -> None:
    """Check one synthetic q-primary maximal-normalization control."""
    l_value = verify_negative_root_shape(p, q, gap, height, m_value)
    if (d_value + height - 1) % p == 0:
        raise AssertionError("synthetic D accidentally became an actual stutter divisor")
    if (m_value + 2 * r_value) % q:
        raise AssertionError("control lost the forced pure-T synchronized q-layer")

    t_value = p * p * r_value - (p + 1) // 2
    a_value = (p + 1) // 2 * t_value
    k_value = (p * p - 1) // 2 * t_value
    e_multiplier = 1 + p * sigma
    z_value = e_multiplier * d_value
    if 4 * k_value % d_value:
        raise AssertionError("synthetic D did not divide the capacity product")
    receipt_quotient = 4 * k_value // d_value - p * e_multiplier
    if d_value * (p * e_multiplier + receipt_quotient) != 4 * k_value:
        raise AssertionError("receipt-quotient bridge changed")

    tau = valuation(t_value, q)
    delta = valuation(d_value, q)
    epsilon = valuation(e_multiplier, q)
    zeta = valuation(z_value, q)
    quotient_valuation = valuation(p * e_multiplier + receipt_quotient, q)
    actual_tuple = (
        tau,
        delta,
        epsilon,
        zeta,
        valuation(receipt_quotient, q),
        quotient_valuation,
    )
    if actual_tuple != expected_valuations:
        raise AssertionError(f"{label} valuation control changed: {actual_tuple}")
    if valuation(a_value, q) != tau or valuation(k_value, q) != tau:
        raise AssertionError("pure-T capacity did not remain entirely in T")

    if zeta <= tau:
        expected_delta, expected_epsilon = zeta, 0
    else:
        expected_delta, expected_epsilon = tau, zeta - tau
    if (delta, epsilon) != (expected_delta, expected_epsilon):
        raise AssertionError("maximal complete-excess q-primary split changed")
    if quotient_valuation != tau - delta:
        raise AssertionError("exact pE+e valuation bridge changed")

    b_zero = 2 * p * r_value - 1
    b_one = b_zero * e_multiplier - sigma
    e_one = (p - 1) * b_one - 1
    if expected_checkpoint_suffix is not None and not (
        sigma % p == expected_checkpoint_suffix % p
        and e_one % p == expected_checkpoint_suffix % p
    ):
        raise AssertionError("q-primary control lost its prescribed checkpoint suffix")
    if not (
        p * b_zero - 1 == 2 * t_value
        and p * b_one - 1 == e_multiplier * (p * b_zero - 1)
        and p * e_one + 1 == 2 * (p - 1) * e_multiplier * t_value
    ):
        raise AssertionError("checkpoint factorization changed")
    checkpoint_valuation = valuation(p * e_one + 1, q)
    if checkpoint_valuation != epsilon + tau:
        raise AssertionError("checkpoint q-primary factor inheritance changed")
    if epsilon:
        if not (
            tau == delta
            and receipt_quotient % q != 0
            and sigma % q == (-l_value) % q
            and b_zero % q == l_value
            and b_one % q == l_value
            and e_one % q == (-l_value) % q
            and (p * e_one + 1) % (q**epsilon) == 0
            and checkpoint_valuation == zeta
        ):
            raise AssertionError("complete-excess checkpoint relay changed")
    else:
        if not (
            tau > delta
            and e_multiplier % q != 0
            and receipt_quotient % q != 0
            and (p * e_multiplier + receipt_quotient) % (q ** (tau - delta)) == 0
        ):
            raise AssertionError("T-slack receipt-quotient branch changed")


def verify() -> None:
    # Both are q-primary normalization controls, not complete actual root receipts.
    verify_actual_stutter_cross_mod_control()
    verify_actual_p_free_pblock_digit_control()
    verify_low_gap_root_box_exclusion()
    verify_p_free_root_expulsion_control()
    verify_p_free_pblock_reentry_control(
        label="p-block q-entry gate miss",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        t_value=9,
        expected_p_height=0,
        expected_x_q_height=0,
    )
    verify_p_free_pblock_reentry_control(
        label="p-block q-entry gate hit below capacity",
        p=433,
        q=11,
        gap=3,
        height=30,
        m_value=10,
        r_value=6,
        t_value=13,
        expected_p_height=1,
        expected_x_q_height=1,
    )
    verify_control(
        label="high-excess E",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        sigma=12,
        d_value=17,
        expected_valuations=(1, 1, 2, 3, 0, 0),
    )
    # CRT keeps the same exact q-primary excess compatible with every p-suffix.
    verify_control(
        label="p-free E-excess",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        sigma=2817,
        d_value=17,
        expected_valuations=(1, 1, 1, 2, 0, 0),
        expected_checkpoint_suffix=0,
    )
    verify_control(
        label="regeneration E-excess",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        sigma=1253,
        d_value=17,
        expected_valuations=(1, 1, 1, 2, 0, 0),
        expected_checkpoint_suffix=1,
    )
    verify_control(
        label="raw-source E-excess",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        sigma=4381,
        d_value=17,
        expected_valuations=(1, 1, 1, 2, 0, 0),
        expected_checkpoint_suffix=-1,
    )
    verify_control(
        label="strict-carry E-excess",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=15,
        sigma=29,
        d_value=17,
        expected_valuations=(1, 1, 1, 2, 0, 0),
        expected_checkpoint_suffix=29,
    )
    verify_control(
        label="T-slack",
        p=313,
        q=17,
        gap=3,
        height=12,
        m_value=4,
        r_value=66,
        sigma=1,
        d_value=17,
        expected_valuations=(2, 1, 0, 1, 0, 1),
    )
    print(
        "verified pure-T cross-mod map, complete-excess relay, "
        "factor inheritance, CRT suffix boundary, p-free root expulsion, "
        "the actual p-adic digit gate, and the p-block q-entry gate"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
