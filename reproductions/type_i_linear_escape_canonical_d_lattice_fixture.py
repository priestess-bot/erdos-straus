#!/usr/bin/env python3
"""Fixed-D canonical-source residual certificate for one linear escape state.

The fixture is constant-size.  It proves only that the original D=41 source
layer has trivial image in a chosen C2 quotient, while the next D'=1 layer can
introduce a new nontrivial source.  It is not a recursive completeness test.
"""

from __future__ import annotations

import argparse
import json


def legendre_symbol(value: int, prime: int) -> int:
    """Return the Legendre symbol for a nonzero residue modulo an odd prime."""
    residue = value % prime
    if residue == 0:
        return 0
    return -1 if pow(residue, (prime - 1) // 2, prime) == prime - 1 else 1


def has_order_58(value: int) -> bool:
    """Check the exact order in the cyclic group F_59^*."""
    return pow(value, 58, 59) == 1 and pow(value, 29, 59) == 58


def run_fixture() -> dict[str, object]:
    """Verify the fixed-D residual and the lower-layer scope guard."""
    prime = 57_399_241
    modulus = 59
    source_a = 956_654
    d_value = 41

    u_odd = 15
    v_odd = 2_693 * 20_959
    k_value = 3 * 5 * 2_693 * 20_959
    assert source_a + 1 + source_a * modulus == prime
    assert (prime * modulus + 1) // 4 == k_value
    assert source_a * modulus + 1 == v_odd
    assert pow(u_odd, 29, modulus) == 1 and u_odd != 1
    assert legendre_symbol(u_odd, modulus) == 1
    assert legendre_symbol(2_693, modulus) == -1
    assert legendre_symbol(20_959, modulus) == -1
    assert has_order_58(2_693)
    assert has_order_58(20_959)

    source_values = {
        1: (3, 5, 7, 546_661),
        d_value: (5, 2_861, 4_013),
    }
    expected_values = {
        1: 57_399_405,
        d_value: 57_405_965,
    }
    fixed_d_rows: list[dict[str, int]] = []
    for source_parameter, factors in source_values.items():
        value = prime + 4 * d_value * source_parameter
        product = 1
        for factor in factors:
            product *= factor
            assert value % factor == 0
            assert legendre_symbol(factor, modulus) == 1
            fixed_d_rows.append(
                {
                    "a": source_parameter,
                    "q": factor,
                    "residue_mod_59": factor % modulus,
                    "legendre": legendre_symbol(factor, modulus),
                }
            )
        assert value == expected_values[source_parameter] == product

    demand_representative = 2_693 % modulus
    assert demand_representative == 38
    assert legendre_symbol(demand_representative, modulus) == -1
    assert all(row["legendre"] == 1 for row in fixed_d_rows)

    lower_value = prime + 4
    lower_factor = 11_479_849
    assert lower_value == 5 * lower_factor
    assert lower_factor % modulus == 42
    assert legendre_symbol(lower_factor, modulus) == -1
    assert has_order_58(lower_factor)

    return {
        "scope_note": (
            "The fixed original D layer cannot pay the declared nontrivial C2 "
            "demand. A fresh lower-layer source exists, so this is not a "
            "recursive D-lattice or global no-go result."
        ),
        "state": {
            "p": prime,
            "R": modulus,
            "a": source_a,
            "s": 1,
            "K": k_value,
            "U_odd": u_odd,
            "V_odd": v_odd,
        },
        "fixed_D": d_value,
        "block_subgroup_order": 29,
        "escape_quotient": "C2",
        "demand_representative_mod_59": demand_representative,
        "fixed_D_source_rows": fixed_d_rows,
        "fixed_D_image_rank": 0,
        "demand_rank": 1,
        "lower_layer_scope_guard": {
            "D_prime": 1,
            "N": lower_value,
            "nonresidue_factor": lower_factor,
            "residue_mod_59": lower_factor % modulus,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(run_fixture(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
