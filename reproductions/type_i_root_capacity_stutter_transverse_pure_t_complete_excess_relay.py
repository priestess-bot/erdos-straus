#!/usr/bin/env python3
"""Verify fixed pure-T q-primary normalization and checkpoint relay controls."""

from __future__ import annotations

import argparse


LOW_GAPS = (3, 7, 11, 23)


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
    verify_control(
        label="E-excess",
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
    print("verified pure-T complete-excess classification and checkpoint relay")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
