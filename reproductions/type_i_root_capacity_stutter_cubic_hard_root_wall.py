#!/usr/bin/env python3
"""Verify exact algebraic controls for the root-stutter cubic height wall."""

from __future__ import annotations

import argparse


def envelope(m_value: int, a_value: int) -> tuple[int, int, int]:
    if m_value < 3 or a_value < 3:
        raise AssertionError("cubic envelope requires m >= 3 and a >= 3")

    layer = a_value * m_value
    shift = m_value - a_value
    bound = layer * layer + layer * shift + shift * shift
    first = layer + 3 * a_value - 3 * m_value
    second = 4 * layer - 3 * a_value + 3 * m_value

    if not (
        13 * layer * layer - 9 * bound == first * second
        and first == m_value * (a_value - 3) + 3 * a_value
        and second == a_value * (4 * m_value - 3) + 3 * m_value
        and first > 0
        and second > 0
        and 9 * bound < 13 * layer * layer
        and 3 * shift < layer
        and 3 * (a_value - 1) <= layer - 3
        and layer >= 9
    ):
        raise AssertionError("pair envelope certificate changed")
    return layer, shift, bound


def verify_envelope_extremes() -> None:
    # These fixed pairs exercise the m=3 edge, the a=3 edge, and a generic pair.
    for m_value, a_value in ((3, 3), (6, 3), (13, 209)):
        envelope(m_value, a_value)


def verify_parity_implication() -> None:
    # Odd m gives odd D and Da; even m gives a + 3u even for u odd.
    for a_mod_two in (0, 1):
        if ((a_mod_two * 1) % 2 == 1) != (a_mod_two == 1):
            raise AssertionError("odd-m parity implication changed")
        if ((a_mod_two + 3) % 2 == 0) != (a_mod_two == 1):
            raise AssertionError("even-m parity implication changed")


def verify_shadow_gate_scale() -> None:
    # This is the existing core-congruent composite shadow. It checks the
    # algebraic gate only; it is deliberately not claimed to be an actual receipt.
    p_value, u_value, m_value, a_value, e_value = 54_481, 4_021, 13, 209, 944
    layer, shift, bound = envelope(m_value, a_value)
    h_value = 3 * u_value
    numerator = 9 * u_value * u_value + 3 * (a_value - 1) * u_value + shift

    if not (
        layer * p_value == numerator
        and bound % u_value == 0
        and (a_value + 3 * u_value) % m_value == 0
        and (a_value + 3 * u_value) // m_value == e_value
        and p_value < 19 * layer**3
        and 3 * h_value * h_value > 2 * layer * p_value
        and 513 * h_value**6 > 8 * p_value**4
    ):
        raise AssertionError("cubic height wall algebra changed")


def verify() -> None:
    verify_envelope_extremes()
    verify_parity_implication()
    verify_shadow_gate_scale()
    print("verified root-stutter cubic envelope and hard-root wall controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
