#!/usr/bin/env python3
"""Verify the v=5 centered mixed-source-fiber obstruction in one cyclic factor."""

from __future__ import annotations

import argparse
import json
from itertools import product

import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_high_r_chart_two_anchor as shared


COMPONENT = 171_566_399
GENERATOR = 7
ORDER = COMPONENT - 1
SUPPORT_LOGS = (34_001_298, 46_258_077, 7_372_596, 134_674_827, 6_933_472, 171_198_251)
DELTA_LOG = 119_416_350


def verify_cyclic_component() -> dict[str, object]:
    """Check an exact cyclic-component witness for delta outside the difference box."""
    factors = tuple(v5.K_FACTORS)
    support = tuple(prime for prime, _exponent in factors)
    if not (
        shared.is_prime(COMPONENT)
        and v5.R % COMPONENT == 0
        and pow(GENERATOR, ORDER, COMPONENT) == 1
        and all(
            pow(GENERATOR, ORDER // prime, COMPONENT) != 1
            for prime, _exponent in shared.factorization(ORDER)
        )
        and support == (2, 19, 193, 5351, 66383, 31641497801)
        and len(SUPPORT_LOGS) == len(factors)
    ):
        raise AssertionError("centered-fiber cyclic component changed")

    phi0 = pow(v5.C0, -1, v5.R)
    phi1 = (-pow(v5.C1, -1, v5.R)) % v5.R
    delta = phi1 * pow(phi0, -1, v5.R) % v5.R
    if not (
        phi0 == 13
        and phi1 == 4_387_621_028_405
        and delta == 5_147_016_975_629
        and delta == (-v5.C0 * pow(v5.C1, -1, v5.R)) % v5.R
        and all(
            pow(GENERATOR, logarithm, COMPONENT) == prime % COMPONENT
            for prime, logarithm in zip(support, SUPPORT_LOGS)
        )
        and pow(GENERATOR, DELTA_LOG, COMPONENT) == delta % COMPONENT
    ):
        raise AssertionError("centered-fiber discrete-log receipt changed")

    ranges = [range(-2 * exponent, 2 * exponent + 1) for _prime, exponent in factors]
    difference_logs = {
        sum(coefficient * logarithm for coefficient, logarithm in zip(vector, SUPPORT_LOGS))
        % ORDER
        for vector in product(*ranges)
    }
    if not (
        len(tuple(product(*ranges))) == 28_125
        and len(difference_logs) == 24_541
        and DELTA_LOG not in difference_logs
    ):
        raise AssertionError("delta entered the centered support difference box")
    return {
        "component": COMPONENT,
        "generator": GENERATOR,
        "order": ORDER,
        "support_logs": list(SUPPORT_LOGS),
        "delta": delta,
        "delta_log": DELTA_LOG,
        "difference_box_cardinality": 28_125,
        "distinct_difference_logs": len(difference_logs),
        "delta_in_difference_box": False,
    }


def verify_relative_q19_phase() -> dict[str, object]:
    """Record the relative q=19 direction without registering a capacity edge."""
    conductor, zeta = 191, 150
    phase_table = {pow(zeta, exponent, conductor): exponent for exponent in range(19)}

    def phase(value: int) -> int:
        return phase_table[pow(value, 10, conductor)]

    phi0 = pow(v5.C0, -1, v5.R)
    phi1 = (-pow(v5.C1, -1, v5.R)) % v5.R
    delta = phi1 * pow(phi0, -1, v5.R) % v5.R
    if not (
        pow(-1, 10, conductor) == 1
        and phase(v5.C0) == 3
        and phase(v5.C1) == 11
        and phase(delta) == 11
    ):
        raise AssertionError("relative q=19 phase changed")
    return {
        "conductor": conductor,
        "zeta": zeta,
        "relative_phase": 11,
        "status": "observed_only; no native centered source fiber exists",
    }


def build_result() -> dict[str, object]:
    """Build an exact no-go receipt, not a capacity or selector receipt."""
    return {
        "certificate_type": "c3_core19_v5_centered_mixed_source_fiber_no_go_v1",
        "cyclic_component": verify_cyclic_component(),
        "relative_q19": verify_relative_q19_phase(),
        "native_adapter_status": "impossible_for_every_centered_C_R(N)_with_N_dividing_K",
        "remaining_boundaries": [
            "provided_unbounded_F_witness_is_not_canonical_fourier_input",
            "terminal_first_m3_d11_preempts_the_v5_control",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 centered mixed-source-fiber no-go")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
