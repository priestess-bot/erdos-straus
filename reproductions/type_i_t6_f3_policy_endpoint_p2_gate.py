#!/usr/bin/env python3
"""Verify focused identities for the T6-F3 policy-endpoint p^2 gate.

The universal statements are proved in the accompanying claim.  This program
checks exact complete-excess recomputation on three fixed controls and validates
the machine-readable proof boundary.  It performs no parameter or prime scan.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import gcd, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "t6-f3-policy-endpoint-p2-residual-v1.json"


@dataclass(frozen=True)
class SideFactor:
    value: int
    block: int
    beta: int
    support_gcd: int
    excess_multiplier: int
    charged_residual: int


@dataclass(frozen=True)
class EndpointFactorization:
    prime: int
    support: int
    capacity: int
    residual: int
    left: SideFactor
    right: SideFactor
    joined_support: int
    multiplier: int
    target_cofactor: int


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return the unique full over-capacity block and its residual."""
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def chart(prime: int, parameter: int) -> dict[str, int]:
    """Build the standard a=1,d=1 high-support chart."""
    g = (prime + 1) // 2
    b = 2 * prime * parameter - 1
    n = (prime + 1) * b - 1
    adjustable = prime * prime * parameter - g
    support = g * adjustable
    capacity = support * (prime - 1)
    residual = (prime - 1) * n - 1
    if not (
        support == (prime * n - 1) // 4
        and 4 * capacity == prime * residual + 1
    ):
        raise AssertionError("a=1,d=1 chart identity changed")
    return {
        "support": support,
        "capacity": capacity,
        "residual": residual,
    }


def side_factor(value: int, support: int, capacity: int) -> SideFactor:
    block, beta = complete_excess(value, capacity)
    support_gcd = gcd(support, block)
    return SideFactor(
        value=value,
        block=block,
        beta=beta,
        support_gcd=support_gcd,
        excess_multiplier=block // support_gcd,
        charged_residual=beta * support_gcd,
    )


def factor_endpoint(
    prime: int,
    support: int,
    capacity: int,
    left: int,
    right: int,
) -> EndpointFactorization:
    residual = left + right
    if not (
        left > 0
        and right > 0
        and gcd(left, right) == 1
        and prime * residual + 1 == 4 * capacity
        and capacity == support * (prime - 1)
        and left % prime
        and right % prime
    ):
        raise AssertionError("endpoint is not a primitive p-free chart node")

    left_factor = side_factor(left, support, capacity)
    right_factor = side_factor(right, support, capacity)
    d_left = left_factor.charged_residual
    d_right = right_factor.charged_residual
    e_left = left_factor.excess_multiplier
    e_right = right_factor.excess_multiplier

    joined_support = lcm(
        support,
        left_factor.block,
        right_factor.block,
    )
    multiplier = joined_support // support
    target_cofactor = pow(4 * joined_support, -1, prime)

    if not (
        left == e_left * d_left
        and right == e_right * d_right
        and capacity % d_left == 0
        and capacity % d_right == 0
        and gcd(d_left, d_right) == 1
        and capacity % (d_left * d_right) == 0
        and (prime * e_right * d_right + 1) % d_left == 0
        and (prime * e_left * d_left + 1) % d_right == 0
        and multiplier == e_left * e_right
    ):
        raise AssertionError("two-sided divisor-source normal form changed")

    return EndpointFactorization(
        prime=prime,
        support=support,
        capacity=capacity,
        residual=residual,
        left=left_factor,
        right=right_factor,
        joined_support=joined_support,
        multiplier=multiplier,
        target_cofactor=target_cofactor,
    )


def verify_p2_identity(data: EndpointFactorization) -> int:
    prime = data.prime
    if (data.multiplier - 1) % (prime * prime):
        raise AssertionError("control is not in the p^2 multiplier class")
    chi = (data.multiplier - 1) // (prime * prime)
    if chi <= 0:
        raise AssertionError("p^2 hard multiplier must be nontrivial")
    e_u = data.left.excess_multiplier
    d_u = data.left.charged_residual
    d_v = data.right.charged_residual
    if (
        e_u * data.residual - e_u * e_u * d_u - d_v
        != prime * prime * chi * d_v
    ):
        raise AssertionError("two-sided p^2 lifted identity changed")
    return chi


def verify_two_sided_control() -> dict[str, int]:
    prime = 73
    source = chart(prime, 57)
    anchor = prime + 1
    departure = source["residual"] - anchor
    if departure % prime:
        raise AssertionError("fixed split departure changed")
    right = departure // prime
    left = source["residual"] - right
    data = factor_endpoint(
        prime,
        source["support"],
        source["capacity"],
        left,
        right,
    )
    chi = verify_p2_identity(data)
    if not (
        data.left.excess_multiplier > 1
        and data.right.excess_multiplier > 1
        and data.target_cofactor == prime - 1
    ):
        raise AssertionError("fixed two-sided p^2 control changed")
    return {
        "prime": prime,
        "multiplier": data.multiplier,
        "chi": chi,
        "left_E": data.left.excess_multiplier,
        "right_E": data.right.excess_multiplier,
    }


def verify_full_capacity_one_sided_control() -> dict[str, int]:
    prime = 97
    source = chart(prime, 66_988_440)
    u = 58
    v = source["residual"] - u
    data = factor_endpoint(
        prime,
        source["support"],
        source["capacity"],
        u,
        v,
    )
    chi = verify_p2_identity(data)
    if data.left.excess_multiplier != 1:
        raise AssertionError("one-sided endpoint no longer divides K")

    d = data.right.charged_residual
    tau = (data.residual - 1) // prime
    m_num = d + u - 1
    c_num = prime * u + 1
    if m_num % prime or c_num % d or source["capacity"] % (u * d):
        raise AssertionError("one-sided factor-pair integrality changed")
    m = m_num // prime
    c = c_num // d
    w = source["capacity"] // (u * d)

    if not (
        data.right.excess_multiplier == 1 + prime * prime * chi
        and tau == m + prime * chi * d
        and 4 * u * w == c + prime + prime**3 * chi
        and w == (c + prime + prime**3 * chi) // (4 * u)
        and d * (prime + c) == m * prime * prime + prime + 1
        and u * (prime + c) == m * prime * c + c - 1
        and (m * c * c - c + 1) % (prime + c) == 0
        and d <= (tau - 1) // prime
        and u * u >= prime
        and (m, c, d, chi) == (4, 17, 331, 39_257_934)
    ):
        raise AssertionError("full-capacity one-sided p^2 gate changed")
    return {
        "prime": prime,
        "u": u,
        "d": d,
        "m": m,
        "c": c,
        "w": w,
        "chi": chi,
        "tau": tau,
    }


def verify_recanonicalization_noninvariance_control() -> dict[str, int]:
    """Show the multiplier congruence is not a chart-wide invariant.

    The two nodes are fixed arithmetic controls in one chart.  They are not
    asserted to be consecutive nodes of ``omega_pf``; the absence of an
    L1-to-L_omega bridge is a proof-boundary statement, not a path result
    manufactured by this control.
    """
    prime = 73
    source = chart(prime, 57)
    anchor = prime + 1
    departure = source["residual"] - anchor
    right = departure // prime
    left = source["residual"] - right
    first = factor_endpoint(
        prime,
        source["support"],
        source["capacity"],
        left,
        right,
    )
    endpoint = factor_endpoint(
        prime,
        source["support"],
        source["capacity"],
        3,
        source["residual"] - 3,
    )
    if not (
        first.multiplier % (prime * prime) == 1
        and endpoint.multiplier % prime != 1
        and endpoint.target_cofactor == 2
    ):
        raise AssertionError("L1/L_omega object-separation control changed")
    return {
        "prime": prime,
        "first_multiplier_mod_p2": first.multiplier % (prime * prime),
        "endpoint_multiplier_mod_p": endpoint.multiplier % prime,
        "endpoint_target_cofactor": endpoint.target_cofactor,
    }


def verify_two_sided_canonical_rechart_boundary() -> dict[str, int]:
    """Show a genuine p^2 target is a larger root-chart reparameterization."""

    prime, parameter = 73, 57
    source = chart(prime, parameter)
    anchor = prime + 1
    departure = source["residual"] - anchor
    right = departure // prime
    left = source["residual"] - right
    endpoint = factor_endpoint(
        prime,
        source["support"],
        source["capacity"],
        left,
        right,
    )
    chi = verify_p2_identity(endpoint)
    multiplier = endpoint.multiplier
    g = (prime + 1) // 2
    T = prime * prime * parameter - g
    parameter_prime = parameter + chi * T
    T_prime = prime * prime * parameter_prime - g
    if not (
        multiplier == 1 + prime * prime * chi
        and endpoint.target_cofactor == prime - 1
        and T_prime == multiplier * T
        and g * T_prime == source["support"] * multiplier
        and source["capacity"] * multiplier
        == g * T_prime * (prime - 1)
        and parameter_prime > parameter
    ):
        raise AssertionError("two-sided p^2 canonical rechart boundary changed")
    return {
        "prime": prime,
        "parameter": parameter,
        "parameter_prime": parameter_prime,
        "multiplier": multiplier,
        "chi": chi,
        "cofactor": endpoint.target_cofactor,
    }


def verify_manifest() -> dict[str, object]:
    with DATA_PATH.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not (
        payload["schema_version"] == "t6-f3-policy-endpoint-p2-residual/v1"
        and payload["normal_form_status"] == "ESTABLISHED"
        and payload["b5_status"] == "OPEN_MINIMAL_RESIDUAL"
        and payload["f3_status"] == "OPEN"
        and payload["object_separation"]["mapping_status"]
        == "NOT_ESTABLISHED_NO_CANONICAL_BRIDGE"
        and "B5=CLOSED" in payload["forbidden_conclusions"]
        and payload["admission_boundary"]["E5"]
        == "OPEN_ON_L_OMEGA_CONGRUENT_1_MOD_P2"
    ):
        raise AssertionError("p^2 residual manifest boundary changed")
    return payload


def run_verifier() -> dict[str, object]:
    manifest = verify_manifest()
    return {
        "schema_version": manifest["schema_version"],
        "normal_form_status": manifest["normal_form_status"],
        "b5_status": manifest["b5_status"],
        "f3_status": manifest["f3_status"],
        "two_sided_control": verify_two_sided_control(),
        "one_sided_control": verify_full_capacity_one_sided_control(),
        "recanonicalization_noninvariance_control": (
            verify_recanonicalization_noninvariance_control()
        ),
        "two_sided_canonical_rechart_boundary": (
            verify_two_sided_canonical_rechart_boundary()
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(run_verifier(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
