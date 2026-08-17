#!/usr/bin/env python3
"""Verify the ordinary positive-q G -> full-carrier Type-I root adapter.

The theorem verified here is conditional on an *actual*, terminal-first,
ordinary Type-II G endpoint.  The focused controls rebuild the endpoint
arithmetic and an exact finite-abelian separating character, then replay the
same p-only root/source and first strict Type-I step used by the established
q=1 adapter.  Finite controls are not used as an existence proof for source
states.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from math import gcd, lcm

import type_ii_q_one_full_carrier_phase_root_entry as q_one
import type_ii_q_one_type_i_carrier_rail_dispatch as rail
from type_ii_odd_kernel_overflow_natural_tail_relation_graph import factorization
from type_ii_relation_scc_proper_endpoint_descent import signed_box_profile

ADAPTER = "positive_q_g_full_carrier_phase_root_entry_v1"
Q_ONE_ADAPTER = "q_one_full_carrier_phase_root_entry_v1"
FIRST_LOCAL_ADAPTER = "full_carrier_first_local_dispatch_origin_normalized_v1"
ALLOWED_ROOT_ORIGINS = (Q_ONE_ADAPTER, ADAPTER)
SOURCE_PHASE = "TYPEII_G_HANDOFF"
TARGET_PHASE = "TYPEI"
TARGET_PROTOCOL = "CHARGED"
SOURCE_SCOPE = "type_ii_endpoint_only"
TARGET_SCOPE = "fresh_source_tree_only"


def digest(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "ascii"
    )
    return hashlib.sha256(encoded).hexdigest()


def semantic_root_projection(root_state: dict[str, object]) -> dict[str, object]:
    """Project away the handoff origin while retaining every local-edge guard."""
    return {
        "source_tree_scope": root_state["source_tree_scope"],
        "normal_form": root_state["normal_form"],
        "equation_target": root_state["equation_target"],
        "marked_solution_set": root_state["marked_solution_set"],
        "chart": root_state["chart"],
        "absorbed_support": root_state["absorbed_support"],
        "carrier": root_state["carrier"],
        "raw_source_digest": root_state["raw_source_digest"],
    }


def first_local_edge_receipt(
    prime: int,
    root_state: dict[str, object],
    raw_source: dict[str, object],
    dispatch: dict[str, object],
) -> dict[str, object]:
    """Normalize either G-handoff origin into the first strict Type-I edge.

    The focused positive-q controls do not supply an actual parent receipt.  The
    function therefore verifies the complete arithmetic/serialization schema
    and records actual-parent replay as the theorem hypothesis rather than
    manufacturing recursive eligibility.
    """
    origin = str(root_state["state_origin"])
    if origin not in ALLOWED_ROOT_ORIGINS:
        raise AssertionError("full-carrier local dispatch received an unknown origin")

    t = (prime - 1) // 24
    B_p = (prime - 1) ** 2 // 4
    root_chart = dict(root_state["chart"])
    root_R, root_K = int(root_chart["R"]), int(root_chart["K"])
    bundle = int(dispatch["full_external_bundle"])
    target_chart = dict(dispatch["dispatch"])
    target_R = int(target_chart["R"])
    target_K = int(target_chart["K"])
    support = int(target_chart["support"])
    kind = str(target_chart["kind"])

    target_state: dict[str, object] = {
        "adapter": FIRST_LOCAL_ADAPTER,
        "state_origin": FIRST_LOCAL_ADAPTER,
        "parent_state_id": root_state["state_id"],
        "parent_origin": origin,
        "parent_semantic_digest": digest(semantic_root_projection(root_state)),
        "source_tree_scope": TARGET_SCOPE,
        "normal_form": (
            "type_i_full_carrier_first_marked_absorb_v1"
            if kind == "marked_absorb"
            else "type_i_full_carrier_first_fixed_n_identity_lift_v1"
        ),
        "major_phase": TARGET_PHASE,
        "protocol": TARGET_PROTOCOL,
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "chart": {"R": target_R, "K": target_K},
        "absorbed_support": support,
        "dispatch_kind": kind,
    }
    if "overflow" in dispatch:
        target_state["overflow_receipt"] = dispatch["overflow"]
    target_state["state_id"] = "state:" + digest(target_state)

    source_potential = [prime, 2, 4, B_p, root_K, 0, 0]
    target_potential = [prime, 2, 4, B_p // support, target_K // support, 0, 0]
    e1_arithmetic = bool(
        raw_source["destination"] == [1, root_R - 1, 1]
        and bundle == root_R - 1
        and bundle > 1
        and root_state["source_tree_scope"] == TARGET_SCOPE
        and root_state["normal_form"] == "type_i_full_carrier_low_root_v1"
    )
    if t % 2:
        e2 = bool(
            kind == "marked_absorb"
            and target_R == 20 * t + 3
            and target_K == (8 * t + 1) * (15 * t + 1)
            and support == 16 * t + 2
        )
    else:
        overflow = dict(dispatch["overflow"])
        e2 = bool(
            kind == "fixed_n_edge"
            and overflow
            == {
                "R": 52 * t + 7,
                "K": (16 * t + 2) * ((39 * t + 2) // 2),
                "n": 12 * t + 1,
                "d": 9 * t // 2,
            }
            and target_R == 6 * t - 1
            and target_K == (9 * t // 2) * (8 * t - 1)
            and support == 9 * t // 2
        )
    e3 = bool(
        3 <= target_R <= prime - 2
        and prime * target_R + 1 == 4 * target_K
        and target_K % support == 0
        and support > 1
        and target_state["parent_origin"] in ALLOWED_ROOT_ORIGINS
    )
    e4 = bool(
        root_state["equation_target"]
        == target_state["equation_target"]
        == [4, prime]
        and root_state["marked_solution_set"]
        == target_state["marked_solution_set"]
        == "Sol(p)"
    )
    e5 = bool(source_potential > target_potential and B_p // support < B_p)
    if not all((e1_arithmetic, e2, e3, e4, e5)):
        raise AssertionError("origin-normalized first local edge did not replay")

    return {
        "adapter": FIRST_LOCAL_ADAPTER,
        "accepted_parent_origins": list(ALLOWED_ROOT_ORIGINS),
        "parent_origin": origin,
        "parent_semantic_projection": semantic_root_projection(root_state),
        "target": target_state,
        "contract_replay": {
            "E1": {
                "root_source_and_bundle_arithmetic": e1_arithmetic,
                "actual_parent_state_receipt": False,
                "complete": False,
                "completion_rule": (
                    "complete for every actual root emitted by either registered "
                    "handoff origin"
                ),
            },
            "E2": e2,
            "E3": e3,
            "E4": e4,
            "E5": e5,
        },
        "solution_lift": "identity: Sol(p) -> Sol(p)",
        "T5_ticket": "LOCAL_DROP",
        "potentials": {"source": source_potential, "target": target_potential},
        "selector_status": "conditional_origin_migration_control",
        "recursive_edge_eligible": False,
    }


def phi(prime_power: int) -> int:
    factors = factorization(prime_power)
    if len(factors) != 1:
        raise AssertionError("phi helper expects a prime power")
    prime, exponent = next(iter(factors.items()))
    return (prime - 1) * prime ** (exponent - 1)


def prime_power_components(modulus: int) -> tuple[int, ...]:
    return tuple(
        prime**exponent for prime, exponent in factorization(modulus).items()
    )


def primitive_root_odd_prime_power(prime_power: int) -> int:
    order = phi(prime_power)
    order_primes = tuple(factorization(order))
    for candidate in range(2, prime_power):
        if gcd(candidate, prime_power) != 1:
            continue
        if all(
            pow(candidate, order // divisor, prime_power) != 1
            for divisor in order_primes
        ):
            return candidate
    raise AssertionError("odd prime-power unit group lost a primitive root")


def cyclic_log(value: int, modulus: int, generator: int, order: int) -> int:
    current = 1
    for exponent in range(order):
        if current == value % modulus:
            return exponent
        current = current * generator % modulus
    raise AssertionError("unit is outside the declared cyclic component")


def unit_coordinate_system(modulus: int) -> dict[str, object]:
    """Return deterministic coordinates for U(modulus).

    Odd prime-power components use their least primitive root.  The 2-primary
    component uses the standard (-1,5) decomposition when its exponent is at
    least three.  This is only a focused verifier implementation; the proof
    uses the standard finite-abelian character-separation lemma.
    """
    components: list[dict[str, int | str]] = []
    for prime_power in prime_power_components(modulus):
        prime, exponent = next(iter(factorization(prime_power).items()))
        if prime != 2:
            components.append(
                {
                    "kind": "cyclic",
                    "modulus": prime_power,
                    "generator": primitive_root_odd_prime_power(prime_power),
                    "order": phi(prime_power),
                }
            )
        elif exponent == 1:
            continue
        elif exponent == 2:
            components.append(
                {
                    "kind": "cyclic",
                    "modulus": prime_power,
                    "generator": 3,
                    "order": 2,
                }
            )
        else:
            components.extend(
                [
                    {
                        "kind": "sign",
                        "modulus": prime_power,
                        "generator": prime_power - 1,
                        "order": 2,
                    },
                    {
                        "kind": "five",
                        "modulus": prime_power,
                        "generator": 5,
                        "order": 2 ** (exponent - 2),
                    },
                ]
            )

    def coordinates(value: int) -> tuple[int, ...]:
        if gcd(value, modulus) != 1:
            raise AssertionError("character coordinate requested for a nonunit")
        answer: list[int] = []
        offset = 0
        while offset < len(components):
            component = components[offset]
            local_modulus = int(component["modulus"])
            local_value = value % local_modulus
            if component["kind"] != "sign":
                answer.append(
                    cyclic_log(
                        local_value,
                        local_modulus,
                        int(component["generator"]),
                        int(component["order"]),
                    )
                )
                offset += 1
                continue

            sign = 0 if local_value % 4 == 1 else 1
            positive_value = local_value if sign == 0 else -local_value % local_modulus
            five_component = components[offset + 1]
            answer.extend(
                [
                    sign,
                    cyclic_log(
                        positive_value,
                        local_modulus,
                        5,
                        int(five_component["order"]),
                    ),
                ]
            )
            offset += 2
        return tuple(answer)

    units = tuple(value for value in range(1, modulus) if gcd(value, modulus) == 1)
    table = {value: coordinates(value) for value in units}
    orders = tuple(int(component["order"]) for component in components)
    if len(set(table.values())) != len(units):
        raise AssertionError("unit coordinate map is not injective")
    if len(units) != (1 if not orders else _product(orders)):
        raise AssertionError("unit coordinate orders do not reconstruct phi(m)")
    for left in units:
        for right in units:
            expected = tuple(
                (a + b) % order
                for a, b, order in zip(
                    table[left], table[right], orders, strict=True
                )
            )
            if table[left * right % modulus] != expected:
                raise AssertionError("unit coordinate map is not a homomorphism")
    return {"components": components, "orders": orders, "coordinates": table}


def _product(values: tuple[int, ...]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def canonical_g_separator(modulus: int, source_generators: tuple[int, ...]) -> dict[str, object]:
    """Construct the lexicographically first exact character separating -1.

    Character values are represented by exponents modulo the lcm of the
    invariant cyclic-component orders, so no floating-point roots of unity
    occur in the receipt.
    """
    system = unit_coordinate_system(modulus)
    orders = tuple(system["orders"])
    coordinate_table = dict(system["coordinates"])
    common_order = lcm(*orders) if orders else 1

    def phase(weights: tuple[int, ...], residue: int) -> int:
        return sum(
            weight * coordinate * (common_order // order)
            for weight, coordinate, order in zip(
                weights, coordinate_table[residue % modulus], orders, strict=True
            )
        ) % common_order

    for weights in product(*(range(order) for order in orders)):
        if all(weight == 0 for weight in weights):
            continue
        if any(phase(weights, generator) != 0 for generator in source_generators):
            continue
        target_phase = phase(weights, modulus - 1)
        if target_phase == 0:
            continue
        return {
            "modulus": modulus,
            "component_orders": list(orders),
            "character_weights": list(weights),
            "root_of_unity_order": common_order,
            "source_generator_phases": {
                generator: phase(weights, generator) for generator in source_generators
            },
            "target_residue": modulus - 1,
            "target_phase": target_phase,
            "coordinate_system": system["components"],
        }
    raise AssertionError("G nonmembership was not separated by the finite dual")


def positive_q_g_endpoint(prime: int, cofactor: int) -> dict[str, object]:
    """Rebuild the p,q arithmetic and canonical ordinary G source guard.

    This function deliberately does not manufacture an actual-reachability or
    terminal-first receipt.  Those are hypotheses of the relative theorem and
    must be supplied by the persistent source state in a real invocation.
    """
    if cofactor <= 1:
        raise AssertionError("positive-q adapter is reserved for q > 1")
    profile = signed_box_profile(prime, cofactor)
    if profile["classification"] != "G":
        raise AssertionError("source endpoint is not G")
    modulus = int(profile["gap"])
    source_generators = tuple(sorted(int(value) for value in profile["factors"]))
    separator = canonical_g_separator(modulus, source_generators)
    if not (
        all(value == 0 for value in separator["source_generator_phases"].values())
        and int(separator["target_phase"]) != 0
        and not bool(profile["target_in_source_subgroup"])
    ):
        raise AssertionError("canonical G separator did not replay")
    endpoint_downset_receipt = {
        "base_U": int(profile["U"]),
        "source_cofactor": cofactor,
        "source_rank": int(profile["rank"]),
        "endpoint_bound": int(profile["endpoint_bound"]),
        "cofactor_divides_U": int(profile["U"]) % cofactor == 0,
        "within_endpoint_bound": cofactor <= int(profile["endpoint_bound"]),
    }
    endpoint_downset_receipt["receipt_digest"] = digest(endpoint_downset_receipt)
    endpoint = {
        "phase": SOURCE_PHASE,
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "ordinary_mark": True,
        "endpoint": {
            "q": cofactor,
            "gap": modulus,
            "first_denominator": int(profile["x"]),
            "U": int(profile["U"]),
            "rank": int(profile["rank"]),
            "endpoint_bound": int(profile["endpoint_bound"]),
        },
        "source_factorization": [
            [factor, exponent] for factor, exponent in profile["factors"].items()
        ],
        "target_fiber": {
            "status": "empty",
            "emptiness_certificate": separator,
        },
        "signed_defect": {
            "status": "not_applicable",
            "reason": "G_empty_target_fiber",
        },
        "endpoint_downset_receipt": endpoint_downset_receipt,
        "source_tree_scope": SOURCE_SCOPE,
        "actual_source_receipt": {
            "status": "hypothesis_not_supplied_by_focused_control",
            "required_fields": [
                "source_state_id",
                "source_provenance_digest",
                "terminal_first_receipt_digest",
            ],
        },
    }
    endpoint["arithmetic_guard_digest"] = "guard:" + digest(endpoint)
    return endpoint


def phase_root_entry(prime: int, cofactor: int) -> dict[str, object]:
    """Build the conditional positive-q G -> p-only root control receipt."""
    endpoint = positive_q_g_endpoint(prime, cofactor)
    t = (prime - 1) // 24
    X = (prime + 3) // 4
    carrier = rail.carrier_chart(prime, X)
    R, K = int(carrier["R"]), int(carrier["K"])
    raw_source = q_one.universal_root_source(prime, R, K)
    dispatch = rail.full_carrier_dispatch(prime)
    if carrier != dispatch["root"]:
        raise AssertionError("p-only root and first dispatch disagree")

    root_state = {
        "adapter": ADAPTER,
        "state_origin": ADAPTER,
        "source_tree_scope": TARGET_SCOPE,
        "normal_form": "type_i_full_carrier_low_root_v1",
        "major_phase": TARGET_PHASE,
        "protocol": TARGET_PROTOCOL,
        "equation_target": [4, prime],
        "marked_solution_set": "Sol(p)",
        "chart": {"R": R, "K": K},
        "absorbed_support": 1,
        "carrier": X,
        "raw_source_digest": digest(raw_source),
    }
    root_state["state_id"] = "state:" + digest(root_state)

    B_p = (prime - 1) ** 2 // 4
    source_potential = [prime, 3, 0, 0, 0, 0, 0]
    root_potential = [prime, 2, 4, B_p, K, 0, 0]
    first_target = dispatch["dispatch"]
    support = int(first_target["support"])
    target_K = int(first_target["K"])
    first_target_potential = [
        prime,
        2,
        4,
        B_p // support,
        target_K // support,
        0,
        0,
    ]

    e1_arithmetic = bool(
            endpoint["endpoint"]["q"] == cofactor
            and endpoint["target_fiber"]["status"] == "empty"
            and endpoint["signed_defect"]["status"] == "not_applicable"
            and endpoint["endpoint_downset_receipt"]["cofactor_divides_U"]
            and endpoint["endpoint_downset_receipt"]["within_endpoint_bound"]
            and raw_source["destination"] == [1, R - 1, 1]
        )
    e2_e5 = {
        "E2": bool(
            R == 16 * t + 3
            and K == X * (16 * t + 1)
            and root_state["state_origin"] == ADAPTER
            and "q" not in root_state
        ),
        "E3": bool(
            3 <= R <= prime - 2
            and 4 * K == prime * R + 1
            and gcd(X, K) == X
            and root_state["source_tree_scope"] == TARGET_SCOPE
            and root_state["absorbed_support"] == 1
        ),
        "E4": bool(
            endpoint["equation_target"] == root_state["equation_target"]
            and endpoint["marked_solution_set"]
            == root_state["marked_solution_set"]
            == "Sol(p)"
        ),
        "E5": bool(
            source_potential > root_potential
            and source_potential[1:3] == [3, 0]
            and root_potential[1:3] == [2, 4]
        ),
    }
    if not e1_arithmetic or not all(e2_e5.values()):
        failed = [name for name, passed in e2_e5.items() if not passed]
        if not e1_arithmetic:
            failed.insert(0, "E1_arithmetic")
        raise AssertionError(f"positive-q phase-root entry failed: {failed}")
    if not root_potential > first_target_potential:
        raise AssertionError("root's first Type-I segment is not a local drop")
    first_local_edge = first_local_edge_receipt(
        prime, root_state, raw_source, dispatch
    )

    return {
        "adapter": ADAPTER,
        "endpoint": endpoint,
        "root": root_state,
        "root_source": raw_source,
        "contract_replay": {
            "E1": {
                "endpoint_and_target_source_arithmetic": e1_arithmetic,
                "actual_source_state_receipt": False,
                "terminal_first_receipt": False,
                "complete": False,
                "completion_rule": (
                    "becomes complete only when the theorem's actual persistent "
                    "source receipt and terminal-first digest are supplied"
                ),
            },
            **e2_e5,
        },
        "solution_lift": "identity: Sol(p) -> Sol(p)",
        "T5_ticket": "PHASE_DROP",
        "selector_status": "conditional_adapter_control",
        "recursive_edge_eligible": False,
        "potentials": {
            "endpoint": source_potential,
            "root": root_potential,
            "first_type_i_target": first_target_potential,
        },
        "first_type_i_step": first_target,
        "first_local_edge": first_local_edge,
        "scope": {
            "actual_terminal_first_source": (
                "theorem hypothesis; not supplied or asserted by focused controls"
            ),
            "nontrivial_mark": "excluded",
            "later_type_i_totality": "not proved",
        },
    }


def verify() -> dict[str, object]:
    controls_by_pair = {
        (97, 3): phase_root_entry(97, 3),
        (241, 4): phase_root_entry(241, 4),
        (577, 8): phase_root_entry(577, 8),
        (937, 13): phase_root_entry(937, 13),
    }
    expected = {
        (97, 3): {"gap": 11, "x": 27},
        (241, 4): {"gap": 15, "x": 64},
        (577, 8): {"gap": 31, "x": 152},
        (937, 13): {"gap": 51, "x": 247},
    }
    for key, receipt in controls_by_pair.items():
        prime, cofactor = key
        endpoint = receipt["endpoint"]["endpoint"]
        if not (
            endpoint["gap"] == expected[key]["gap"]
            and endpoint["first_denominator"] == expected[key]["x"]
            and endpoint["q"] == cofactor
            and receipt["contract_replay"]["E1"][
                "endpoint_and_target_source_arithmetic"
            ]
            and not receipt["contract_replay"]["E1"]["complete"]
            and all(receipt["contract_replay"][name] for name in ("E2", "E3", "E4", "E5"))
            and receipt["T5_ticket"] == "PHASE_DROP"
            and receipt["selector_status"] == "conditional_adapter_control"
            and not receipt["recursive_edge_eligible"]
            and receipt["potentials"]["endpoint"] > receipt["potentials"]["root"]
            and receipt["potentials"]["root"]
            > receipt["potentials"]["first_type_i_target"]
            and receipt["first_local_edge"]["parent_origin"] == ADAPTER
            and receipt["first_local_edge"]["T5_ticket"] == "LOCAL_DROP"
            and receipt["first_local_edge"]["potentials"]["source"]
            > receipt["first_local_edge"]["potentials"]["target"]
            and receipt["first_local_edge"]["contract_replay"]["E1"][
                "root_source_and_bundle_arithmetic"
            ]
            and not receipt["first_local_edge"]["contract_replay"]["E1"][
                "complete"
            ]
            and all(
                receipt["first_local_edge"]["contract_replay"][name]
                for name in ("E2", "E3", "E4", "E5")
            )
        ):
            raise AssertionError(f"positive-q control changed for p={prime}, q={cofactor}")

    # For a fixed p the target serialization is q-independent.  p=1009 has
    # several positive-q G endpoints and gives a direct confluence control.
    same_prime = {
        q: phase_root_entry(1009, q) for q in (2, 4, 7, 9, 18)
    }
    if len({receipt["root"]["state_id"] for receipt in same_prime.values()}) != 1:
        raise AssertionError("p-only target serialization inherited source q")

    q_one_root = q_one.phase_root_entry(241)["root"]
    positive_root = controls_by_pair[(241, 4)]["root"]
    if semantic_root_projection(q_one_root) != semantic_root_projection(positive_root):
        raise AssertionError("q=1 and positive-q roots differ beyond their origin")
    migrated_q_one = first_local_edge_receipt(
        241,
        q_one_root,
        controls_by_pair[(241, 4)]["root_source"],
        rail.full_carrier_dispatch(241),
    )
    if not (
        migrated_q_one["parent_origin"] == Q_ONE_ADAPTER
        and migrated_q_one["target"]["chart"]
        == controls_by_pair[(241, 4)]["first_local_edge"]["target"]["chart"]
        and migrated_q_one["target"]["absorbed_support"]
        == controls_by_pair[(241, 4)]["first_local_edge"]["target"][
            "absorbed_support"
        ]
    ):
        raise AssertionError("origin normalization changed the first local edge")

    return {
        "status": "verified_conditional_adapter_arithmetic",
        "controls": {
            f"p={prime},q={cofactor}": receipt
            for (prime, cofactor), receipt in controls_by_pair.items()
        },
        "same_prime_target_independence": {
            "prime": 1009,
            "source_cofactors": sorted(same_prime),
            "unique_root_state_id": next(
                iter({receipt["root"]["state_id"] for receipt in same_prime.values()})
            ),
        },
        "q_one_positive_q_first_local_origin_confluence": {
            "prime": 241,
            "semantic_root_digest": digest(semantic_root_projection(q_one_root)),
            "accepted_parent_origins": list(ALLOWED_ROOT_ORIGINS),
            "target_chart": migrated_q_one["target"]["chart"],
            "target_support": migrated_q_one["target"]["absorbed_support"],
        },
        "scope": (
            "Handoff E1 endpoint/target-source arithmetic plus E2-E5 and the "
            "origin-normalized first local edge schema are replayed. Controls do "
            "not supply an actual persistent source receipt or a terminal-first "
            "digest and therefore are not recursive edges."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
