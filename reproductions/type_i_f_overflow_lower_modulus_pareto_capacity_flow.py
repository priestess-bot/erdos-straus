#!/usr/bin/env python3
"""Solve a finite Pareto-demand / optimistic q-adic-capacity integer flow.

The demand columns are exact unit-weight minimizers of the lower-modulus target
fibres.  They are therefore Pareto minimal.  The resource side is deliberately
optimistic: block, modulus-difference, and label-difference heights are pooled
over a factor-support window and may be used independently.  Feasibility of
this ledger is only a finite counterexample to an automatic overload argument;
it is not an arithmetic map from overflow to carrier consumption.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PARETO_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-pareto-overflow-results.json"
)
UPPER_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-shortest-relation-results.json"
)
SOURCE_SCRIPT = (
    ROOT
    / "reproductions"
    / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-pareto-capacity-flow-results.json"
)

EXPECTED_PARETO_SHA256 = "8fd82842893674641cf15928cf436d872e450b5fd175d47f8a825fad5603c6fe"
EXPECTED_UPPER_SHA256 = "077f565596f9f06e30aca5c7c6c6de487b455581f9e28801b84950531032ad42"
EXPECTED_SOURCE_SHA256 = "96ee0c6711a4995fe387686a4915b41f1fcefa70cd4fe808c05a4092bf05e07d"
CHANNELS = ("block", "modulus_difference", "label_difference")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source():
    spec = importlib.util.spec_from_file_location(
        "pareto_capacity_linear_source", SOURCE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("q-adic height of zero is not a finite resource")
    value = abs(value)
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def state_key(profile: dict[str, object]) -> tuple[int, str, int, int, int]:
    return (
        int(profile["prime"]),
        str(profile["orientation"]),
        int(profile["original_R"]),
        int(profile["gap"]),
        int(profile["lower_modulus"]),
    )


def exact_overflow_vectors(bounds: tuple[int, ...], cost: int):
    """Yield every exponent vector with the prescribed scalar overflow."""
    vector = [0] * len(bounds)

    def visit(index: int, remaining: int):
        if index == len(bounds):
            if remaining == 0:
                yield tuple(vector)
            return
        bound = bounds[index]
        for exponent in range(-bound, bound + 1):
            vector[index] = exponent
            yield from visit(index + 1, remaining)
        for excess in range(1, remaining + 1):
            for exponent in (bound + excess, -bound - excess):
                vector[index] = exponent
                yield from visit(index + 1, remaining - excess)
        vector[index] = 0

    yield from visit(0, cost)


def weak_compositions(total: int, length: int):
    """Yield every nonnegative length-tuple with the prescribed sum."""
    vector = [0] * length

    def visit(index: int, remaining: int):
        if index == length - 1:
            vector[index] = remaining
            yield tuple(vector)
            return
        for value in range(remaining + 1):
            vector[index] = value
            yield from visit(index + 1, remaining - value)

    if length <= 0:
        if total == 0:
            yield ()
        return
    yield from visit(0, total)


def exponent_options(
    q: int, bound: int, overflow: int, modulus: int
) -> list[tuple[int, int]]:
    """Return exponent/residue choices with one exact overflow coordinate."""
    if overflow == 0:
        exponents = range(-bound, bound + 1)
    else:
        magnitude = bound + overflow
        exponents = (-magnitude, magnitude)
    return [
        (
            exponent,
            pow(
                q if exponent >= 0 else pow(q, -1, modulus),
                abs(exponent),
                modulus,
            ),
        )
        for exponent in exponents
    ]


def target_fiber_profile(
    coordinate_options: list[list[tuple[int, int]]], modulus: int
) -> tuple[int, tuple[int, ...] | None]:
    """Count target representations and keep a lexicographic witness."""
    states: dict[int, tuple[int, tuple[int, ...]]] = {1 % modulus: (1, ())}
    for options in coordinate_options:
        next_states: dict[int, tuple[int, tuple[int, ...]]] = {}
        for residue, (count, prefix) in states.items():
            for exponent, coordinate_residue in options:
                new_residue = residue * coordinate_residue % modulus
                witness = prefix + (exponent,)
                if new_residue not in next_states:
                    next_states[new_residue] = (count, witness)
                else:
                    old_count, old_witness = next_states[new_residue]
                    next_states[new_residue] = (
                        old_count + count,
                        min(old_witness, witness),
                    )
        states = next_states
    return states.get(modulus - 1, (0, None))


def overflow_vector(
    exponents: tuple[int, ...], bounds: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        max(abs(exponent) - bound, 0)
        for exponent, bound in zip(exponents, bounds)
    )


def relation_residue(
    factors: tuple[int, ...], modulus: int, exponents: tuple[int, ...]
) -> int:
    result = 1 % modulus
    for q, exponent in zip(factors, exponents):
        base = q if exponent >= 0 else pow(q, -1, modulus)
        result = result * pow(base, abs(exponent), modulus) % modulus
    return result


def side_minima(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    upper_bound: int,
) -> dict[int, tuple[int, dict[tuple[int, ...], tuple[int, ...]]]]:
    """For each residue retain every minimum-cost overflow pattern."""
    minima: dict[int, tuple[int, dict[tuple[int, ...], tuple[int, ...]]]] = {}
    for cost in range(upper_bound + 1):
        for exponents in exact_overflow_vectors(bounds, cost):
            residue = relation_residue(factors, modulus, exponents)
            overflow = overflow_vector(exponents, bounds)
            prior = minima.get(residue)
            if prior is None or cost < prior[0]:
                minima[residue] = (cost, {overflow: exponents})
            elif cost == prior[0]:
                previous = prior[1].get(overflow)
                if previous is None or exponents < previous:
                    prior[1][overflow] = exponents
    return minima


def complete_unit_optimal_options(
    profile: dict[str, object], upper_bound: int
) -> tuple[int, list[dict[str, object]], dict[str, int]]:
    """Close the exact unit-cost optimum by a meet-in-the-middle audit."""
    factorization = tuple(
        (int(q), int(exponent)) for q, exponent in profile["factorization"]
    )
    factors = tuple(q for q, _exponent in factorization)
    bounds = tuple(exponent for _q, exponent in factorization)
    modulus = int(profile["lower_modulus"])
    split = len(factors) // 2
    left = side_minima(
        factors[:split], bounds[:split], modulus, upper_bound
    )
    right = side_minima(
        factors[split:], bounds[split:], modulus, upper_bound
    )

    best_cost = upper_bound + 1
    options: dict[tuple[int, ...], tuple[int, ...]] = {}
    target = modulus - 1
    for residue, (left_cost, left_options) in left.items():
        needed = target * pow(residue, -1, modulus) % modulus
        if needed not in right:
            continue
        right_cost, right_options = right[needed]
        cost = left_cost + right_cost
        if cost > best_cost:
            continue
        if cost < best_cost:
            best_cost = cost
            options.clear()
        for left_overflow, left_exponents in left_options.items():
            for right_overflow, right_exponents in right_options.items():
                overflow = left_overflow + right_overflow
                exponents = left_exponents + right_exponents
                previous = options.get(overflow)
                if previous is None or exponents < previous:
                    options[overflow] = exponents

    if best_cost > upper_bound or not options:
        raise AssertionError("a valid upper-bound relation did not close Omega_1")
    result = []
    for overflow, exponents in sorted(options.items()):
        if sum(overflow) != best_cost:
            raise AssertionError("a minimum option has the wrong scalar cost")
        if relation_residue(factors, modulus, exponents) != modulus - 1:
            raise AssertionError("a minimum option lost the target residue")
        result.append(
            {
                "overflow_vector": list(overflow),
                "unit_cost": best_cost,
                "lexicographic_witness": list(exponents),
            }
        )
    return best_cost, result, {
        "left_residue_count": len(left),
        "right_residue_count": len(right),
    }


def exact_demand_sets() -> tuple[list[dict[str, object]], dict[str, object]]:
    pareto_payload = json.loads(PARETO_INPUT.read_text(encoding="utf-8"))
    upper_payload = json.loads(UPPER_INPUT.read_text(encoding="utf-8"))
    upper_by_key = {state_key(profile): profile for profile in upper_payload["profiles"]}
    profiles: list[dict[str, object]] = []
    inherited_count = 0
    completed_count = 0

    for profile in pareto_payload["profiles"]:
        key = state_key(profile)
        if key not in upper_by_key:
            raise AssertionError("a Pareto state lacks its valid upper-bound relation")
        upper = upper_by_key[key]
        factorization = [
            [int(q), int(exponent)] for q, exponent in profile["factorization"]
        ]
        if factorization != [
            [int(q), int(exponent)] for q, exponent in upper["factorization"]
        ]:
            raise AssertionError("the Pareto and upper-bound factorizations differ")

        discovered = list(profile["pareto_vectors_through_cap"])
        unit_omega = profile["unit_omega"]
        if unit_omega is not None:
            omega = int(unit_omega)
            options = [
                {
                    "overflow_vector": [
                        int(value) for value in record["overflow_vector"]
                    ],
                    "unit_cost": omega,
                    "lexicographic_witness": [
                        int(value) for value in record["lexicographic_witness"]
                    ],
                }
                for record in discovered
                if int(record["unit_cost"]) == omega
            ]
            if not options:
                raise AssertionError("a finite unit minimum has no option")
            method = "complete_cap_shell"
            audit = {
                "unit_overflow_cap": int(profile["unit_overflow_cap"]),
                "target_option_count_at_minimum": len(options),
            }
            inherited_count += 1
        else:
            upper_bound = int(upper["overflow_layers"])
            omega, options, split_audit = complete_unit_optimal_options(
                profile, upper_bound
            )
            method = "meet_in_the_middle_to_valid_upper_bound"
            audit = {
                "valid_upper_bound": upper_bound,
                "target_option_count_at_minimum": len(options),
                **split_audit,
            }
            completed_count += 1

        factors = tuple(q for q, _exponent in factorization)
        modulus = int(profile["lower_modulus"])
        for option in options:
            exponents = tuple(int(value) for value in option["lexicographic_witness"])
            if relation_residue(factors, modulus, exponents) != modulus - 1:
                raise AssertionError("a selected demand column is not in the target fibre")
        profiles.append(
            {
                "prime": int(profile["prime"]),
                "orientation": str(profile["orientation"]),
                "original_R": int(profile["original_R"]),
                "gap": int(profile["gap"]),
                "lower_modulus": modulus,
                "factorization": factorization,
                "unit_omega": omega,
                "unit_optimal_option_count": len(options),
                "completion_method": method,
                "completion_audit": audit,
                "unit_optimal_pareto_options": sorted(
                    options,
                    key=lambda record: (
                        record["overflow_vector"], record["lexicographic_witness"]
                    ),
                ),
            }
        )

    if len(profiles) != 42 or completed_count != 6:
        raise AssertionError("the frozen 42-state demand split changed")
    return profiles, {
        "cap_shell_completed_state_count": inherited_count,
        "meet_in_the_middle_completed_state_count": completed_count,
        "unit_omega_histogram": {
            str(value): count
            for value, count in sorted(
                Counter(int(profile["unit_omega"]) for profile in profiles).items()
            )
        },
        "total_unit_demand": sum(int(profile["unit_omega"]) for profile in profiles),
        "total_unit_optimal_option_count": sum(
            int(profile["unit_optimal_option_count"]) for profile in profiles
        ),
    }


def resource_capacities(
    profiles: list[dict[str, object]],
) -> tuple[dict[tuple[int, int], dict[str, object]], dict[int, dict[int, list[tuple[int, int]]]]]:
    support_windows: dict[tuple[int, int], list[int]] = defaultdict(list)
    for profile in profiles:
        for q, _exponent in profile["factorization"]:
            support_windows[(int(profile["prime"]), int(q))].append(
                int(profile["original_R"])
            )

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    source_context: dict[int, tuple[list[int], list[int]]] = {}
    resources: dict[tuple[int, int], dict[str, object]] = {}
    for prime, q in sorted(support_windows):
        if prime not in source_cache:
            _bound, states_by_R = source.enumerate_linear_source_states(prime)
            source_cache[prime] = states_by_R
            source_context[prime] = (
                sorted(states_by_R),
                sorted(
                    {
                        label
                        for states in states_by_R.values()
                        for a, s in states
                        for label in (a, s)
                    }
                ),
            )
        states_by_R = source_cache[prime]
        all_moduli, all_labels = source_context[prime]
        window = support_windows[(prime, q)]
        low = min(window)
        high = max(window)
        channel_capacity = {channel: 0 for channel in CHANNELS}
        global_channel_capacity = {channel: 0 for channel in CHANNELS}
        independent_max_capacity = 0
        global_independent_max_capacity = 0
        source_state_count = 0
        global_source_state_count = 0
        for modulus, states in states_by_R.items():
            modulus_height = max(
                (
                    valuation((modulus - other) // 4, q)
                    for other in all_moduli
                    if other != modulus
                ),
                default=0,
            )
            for a, s in states:
                block_height = max(
                    valuation(a * modulus + 1, q),
                    valuation(s * modulus + 1, q),
                )
                label_height = max(
                    (
                        valuation(label - other, q)
                        for label in (a, s)
                        for other in all_labels
                        if other != label
                    ),
                    default=0,
                )
                heights = {
                    "block": block_height,
                    "modulus_difference": modulus_height,
                    "label_difference": label_height,
                }
                for channel in CHANNELS:
                    global_channel_capacity[channel] += heights[channel]
                global_independent_max_capacity += max(heights.values())
                global_source_state_count += 1
                if low <= modulus <= high:
                    for channel in CHANNELS:
                        channel_capacity[channel] += heights[channel]
                    independent_max_capacity += max(heights.values())
                    source_state_count += 1
        if not source_state_count:
            raise AssertionError("a factor-support window contains no source state")
        resources[(prime, q)] = {
            "prime": prime,
            "q": q,
            "support_state_count": len(window),
            "R_min": low,
            "R_max": high,
            "ordered_source_state_count": source_state_count,
            "global_ordered_source_state_count": global_source_state_count,
            "channel_capacity": channel_capacity,
            "global_channel_capacity": global_channel_capacity,
            "block_capacity": channel_capacity["block"],
            "independent_max_capacity": independent_max_capacity,
            "additive_three_channel_capacity": sum(channel_capacity.values()),
            "global_block_capacity": global_channel_capacity["block"],
            "global_independent_max_capacity": global_independent_max_capacity,
            "global_additive_three_channel_capacity": sum(
                global_channel_capacity.values()
            ),
        }
    return resources, source_cache


def option_usage(
    profile: dict[str, object], option: dict[str, object]
) -> dict[int, int]:
    return {
        int(q): int(excess)
        for (q, _exponent), excess in zip(
            profile["factorization"], option["overflow_vector"]
        )
        if int(excess) > 0
    }


def attach_resource_feasible_options(
    profiles: list[dict[str, object]],
    resources: dict[tuple[int, int], dict[str, object]],
    capacity_field: str,
    option_field: str,
) -> dict[str, object]:
    """Find the first exact target shell inside each resource box."""
    total_vectors_examined = 0
    increased_cost_states = 0
    maximum_cost_increase = 0
    for profile in profiles:
        prime = int(profile["prime"])
        factorization = tuple(
            (int(q), int(exponent)) for q, exponent in profile["factorization"]
        )
        factors = tuple(q for q, _bound in factorization)
        caps = tuple(
            int(resources[(prime, q)][capacity_field]) for q in factors
        )
        modulus = int(profile["lower_modulus"])
        omega = int(profile["unit_omega"])
        options: dict[tuple[int, ...], tuple[int, ...]] = {}
        selected_cost = None
        # Any feasible vector has scalar cost at most sum(caps), so this is an
        # exact finite decision.  The frozen data find a target long before the
        # formal upper endpoint of this range.
        for cost in range(omega, sum(caps) + 1):
            for overflow in weak_compositions(cost, len(factors)):
                if any(excess > cap for excess, cap in zip(overflow, caps)):
                    continue
                total_vectors_examined += 1
                count, witness = target_fiber_profile(
                    [
                        exponent_options(q, bound, excess, modulus)
                        for (q, bound), excess in zip(factorization, overflow)
                    ],
                    modulus,
                )
                if not count:
                    continue
                if witness is None:
                    raise AssertionError("a positive target count has no witness")
                options[overflow] = witness
            if options:
                selected_cost = cost
                break

        profile[option_field] = [
            {
                "overflow_vector": list(overflow),
                "unit_cost": selected_cost,
                "lexicographic_witness": list(witness),
            }
            for overflow, witness in sorted(options.items())
        ]
        profile[f"{option_field}_minimum_unit_cost"] = selected_cost
        profile[f"{option_field}_capacity_vector"] = list(caps)
        if selected_cost is not None and selected_cost > omega:
            increased_cost_states += 1
            maximum_cost_increase = max(maximum_cost_increase, selected_cost - omega)

    return {
        "capacity_field": capacity_field,
        "state_count": len(profiles),
        "state_with_feasible_option_count": sum(
            bool(profile[option_field]) for profile in profiles
        ),
        "increased_cost_state_count": increased_cost_states,
        "maximum_cost_increase": maximum_cost_increase,
        "overflow_vectors_examined": total_vectors_examined,
    }


def solve_choice_model(
    profiles: list[dict[str, object]],
    resources: dict[tuple[int, int], dict[str, object]],
    capacity_field: str,
    option_field: str = "unit_optimal_pareto_options",
) -> dict[str, object]:
    by_prime: dict[int, list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        by_prime[int(profile["prime"])].append(profile)

    selected: dict[tuple[int, str, int, int, int], dict[str, object]] = {}
    prime_audits = []
    failed_primes = []
    for prime, states in sorted(by_prime.items()):
        states = sorted(states, key=state_key)
        option_lists = [state[option_field] for state in states]
        if any(not options for options in option_lists):
            failed_primes.append(prime)
            prime_audits.append(
                {
                    "prime": prime,
                    "state_count": len(states),
                    "combination_count_tested": 0,
                    "feasible_combination_count": 0,
                    "integer_feasible": False,
                    "reason": "a state has no target relation inside its coordinate capacities",
                }
            )
            continue
        tested = 0
        feasible = 0
        best_score = None
        best_combination = None
        best_usage = None
        for combination in itertools.product(*option_lists):
            tested += 1
            usage: dict[int, int] = defaultdict(int)
            for state, option in zip(states, combination):
                for q, amount in option_usage(state, option).items():
                    usage[q] += amount
            if any(
                amount > int(resources[(prime, q)][capacity_field])
                for q, amount in usage.items()
            ):
                continue
            feasible += 1
            maximum_ratio = max(
                (
                    Fraction(amount, int(resources[(prime, q)][capacity_field]))
                    for q, amount in usage.items()
                ),
                default=Fraction(0, 1),
            )
            score = (
                maximum_ratio,
                tuple(tuple(option["overflow_vector"]) for option in combination),
                tuple(tuple(option["lexicographic_witness"]) for option in combination),
            )
            if best_score is None or score < best_score:
                best_score = score
                best_combination = combination
                best_usage = dict(usage)
        if best_combination is None:
            failed_primes.append(prime)
            prime_audits.append(
                {
                    "prime": prime,
                    "state_count": len(states),
                    "combination_count_tested": tested,
                    "feasible_combination_count": 0,
                    "integer_feasible": False,
                }
            )
            continue
        for state, option in zip(states, best_combination):
            selected[state_key(state)] = option
        prime_audits.append(
            {
                "prime": prime,
                "state_count": len(states),
                "combination_count_tested": tested,
                "feasible_combination_count": feasible,
                "integer_feasible": True,
                "selected_maximum_resource_ratio": {
                    "numerator": best_score[0].numerator,
                    "denominator": best_score[0].denominator,
                    "decimal": float(best_score[0]),
                },
                "selected_usage": {
                    str(q): amount for q, amount in sorted(best_usage.items())
                },
            }
        )

    if failed_primes:
        return {
            "capacity_field": capacity_field,
            "option_field": option_field,
            "integer_feasible": False,
            "prime_count": len(by_prime),
            "failed_prime_count": len(failed_primes),
            "failed_primes": failed_primes,
            "selected_state_count_before_failures": len(selected),
            "prime_audits": prime_audits,
        }

    total_usage: dict[tuple[int, int], int] = defaultdict(int)
    selections = []
    for state in sorted(profiles, key=state_key):
        option = selected[state_key(state)]
        usage = option_usage(state, option)
        for q, amount in usage.items():
            total_usage[(int(state["prime"]), q)] += amount
        selections.append(
            {
                "prime": int(state["prime"]),
                "orientation": state["orientation"],
                "original_R": int(state["original_R"]),
                "gap": int(state["gap"]),
                "lower_modulus": int(state["lower_modulus"]),
                "unit_omega": int(state["unit_omega"]),
                "selected_unit_cost": sum(
                    int(value) for value in option["overflow_vector"]
                ),
                "overflow_vector": list(option["overflow_vector"]),
                "exponent_witness": list(option["lexicographic_witness"]),
                "coordinate_demand": {
                    str(q): amount for q, amount in sorted(usage.items())
                },
            }
        )
    used_resources = []
    for key, demand in sorted(total_usage.items()):
        capacity = int(resources[key][capacity_field])
        if demand > capacity:
            raise AssertionError("the reported integer choice exceeds capacity")
        used_resources.append(
            {
                "prime": key[0],
                "q": key[1],
                "demand": demand,
                "capacity": capacity,
                "slack": capacity - demand,
            }
        )
    return {
        "capacity_field": capacity_field,
        "option_field": option_field,
        "integer_feasible": True,
        "state_count": len(selections),
        "prime_count": len(by_prime),
        "total_demand": sum(row["demand"] for row in used_resources),
        "used_resource_count": len(used_resources),
        "maximum_used_resource_ratio": max(
            (row["demand"] / row["capacity"] for row in used_resources),
            default=0,
        ),
        "saturated_resource_count": sum(
            row["demand"] == row["capacity"] for row in used_resources
        ),
        "prime_audits": prime_audits,
        "selections": selections,
        "used_resources": used_resources,
    }


def attach_additive_channel_flow(
    model: dict[str, object],
    resources: dict[tuple[int, int], dict[str, object]],
    channel_capacity_field: str,
) -> None:
    remaining = {
        key: {
            channel: int(resource[channel_capacity_field][channel])
            for channel in CHANNELS
        }
        for key, resource in resources.items()
    }
    aggregate_flow: dict[tuple[int, int], dict[str, int]] = defaultdict(
        lambda: {channel: 0 for channel in CHANNELS}
    )
    for selection in model["selections"]:
        flow: dict[str, dict[str, int]] = {}
        prime = int(selection["prime"])
        for q_text, amount_value in sorted(
            selection["coordinate_demand"].items(), key=lambda item: int(item[0])
        ):
            q = int(q_text)
            amount = int(amount_value)
            coordinate_flow = {channel: 0 for channel in CHANNELS}
            for channel in CHANNELS:
                allocated = min(amount, remaining[(prime, q)][channel])
                coordinate_flow[channel] = allocated
                remaining[(prime, q)][channel] -= allocated
                aggregate_flow[(prime, q)][channel] += allocated
                amount -= allocated
            if amount:
                raise AssertionError("the additive model has no channel flow")
            flow[q_text] = coordinate_flow
        selection["channel_flow"] = flow

    model["aggregate_channel_flow"] = [
        {
            "prime": prime,
            "q": q,
            "flow": aggregate_flow[(prime, q)],
            "capacity": resources[(prime, q)][channel_capacity_field],
        }
        for prime, q in sorted(aggregate_flow)
    ]


def compact_model(model: dict[str, object]) -> dict[str, object]:
    return {
        key: model[key]
        for key in (
            "capacity_field",
            "option_field",
            "integer_feasible",
            "state_count",
            "prime_count",
            "total_demand",
            "used_resource_count",
            "maximum_used_resource_ratio",
            "saturated_resource_count",
            "failed_prime_count",
            "failed_primes",
        )
        if key in model
    }


def singleton_full_fiber_price_certificate(
    profile: dict[str, object],
    resources: dict[tuple[int, int], dict[str, object]],
    capacity_field: str,
) -> dict[str, object]:
    """Find a positive integer price separating one full target fibre."""
    prime = int(profile["prime"])
    factorization = tuple(
        (int(q), int(exponent)) for q, exponent in profile["factorization"]
    )
    factors = tuple(q for q, _exponent in factorization)
    capacities = tuple(
        int(resources[(prime, q)][capacity_field]) for q in factors
    )
    omega = int(profile["unit_omega"])
    unit_options = [
        tuple(int(value) for value in option["overflow_vector"])
        for option in profile["unit_optimal_pareto_options"]
    ]
    best = None
    for weights in itertools.product(range(1, 13), repeat=len(factors)):
        capacity_price = sum(
            weight * capacity for weight, capacity in zip(weights, capacities)
        )
        unit_minimum_price = min(
            sum(weight * excess for weight, excess in zip(weights, option))
            for option in unit_options
        )
        nonminimum_lower_bound = (omega + 1) * min(weights)
        full_fiber_lower_bound = min(
            unit_minimum_price, nonminimum_lower_bound
        )
        if full_fiber_lower_bound <= capacity_price:
            continue
        score = (max(weights), sum(weights), weights)
        if best is None or score < best[0]:
            best = (
                score,
                weights,
                capacity_price,
                unit_minimum_price,
                nonminimum_lower_bound,
                full_fiber_lower_bound,
            )
    if best is None:
        raise AssertionError("the expected singleton price certificate disappeared")
    (
        _score,
        weights,
        capacity_price,
        unit_minimum_price,
        nonminimum_lower_bound,
        full_fiber_lower_bound,
    ) = best
    return {
        "prime": prime,
        "orientation": profile["orientation"],
        "original_R": int(profile["original_R"]),
        "gap": int(profile["gap"]),
        "lower_modulus": int(profile["lower_modulus"]),
        "capacity_field": capacity_field,
        "q_coordinates": list(factors),
        "capacities": list(capacities),
        "positive_integer_prices": list(weights),
        "unit_omega": omega,
        "unit_optimal_options": [list(option) for option in unit_options],
        "capacity_price": capacity_price,
        "unit_minimum_price": unit_minimum_price,
        "nonminimum_price_lower_bound": nonminimum_lower_bound,
        "full_fiber_price_lower_bound": full_fiber_lower_bound,
        "strict_margin": full_fiber_lower_bound - capacity_price,
        "proof": (
            "Every target demand has scalar cost Omega_1 or at least Omega_1+1. "
            "The first class is exhausted by unit_optimal_options; the second has "
            "price at least (Omega_1+1)*min(price)."
        ),
    }


def run() -> dict[str, object]:
    for path, expected, label in (
        (PARETO_INPUT, EXPECTED_PARETO_SHA256, "truncated Pareto frontier"),
        (UPPER_INPUT, EXPECTED_UPPER_SHA256, "valid relation upper bounds"),
        (SOURCE_SCRIPT, EXPECTED_SOURCE_SHA256, "linear source enumerator"),
    ):
        if sha256(path) != expected:
            raise AssertionError(f"the frozen {label} input changed")

    profiles, demand_audit = exact_demand_sets()
    resources, source_cache = resource_capacities(profiles)
    global_feasible_audit = attach_resource_feasible_options(
        profiles,
        resources,
        "global_additive_three_channel_capacity",
        "global_additive_feasible_pareto_options",
    )
    block = solve_choice_model(profiles, resources, "block_capacity")
    independent_max = solve_choice_model(
        profiles, resources, "independent_max_capacity"
    )
    additive = solve_choice_model(
        profiles, resources, "additive_three_channel_capacity"
    )
    global_block = solve_choice_model(
        profiles, resources, "global_block_capacity"
    )
    global_independent_max = solve_choice_model(
        profiles, resources, "global_independent_max_capacity"
    )
    global_additive = solve_choice_model(
        profiles, resources, "global_additive_three_channel_capacity"
    )
    global_additive_full = solve_choice_model(
        profiles,
        resources,
        "global_additive_three_channel_capacity",
        "global_additive_feasible_pareto_options",
    )
    obstruction_profile = next(
        profile for profile in profiles if int(profile["prime"]) == 62704849
    )
    support_window_price_certificate = singleton_full_fiber_price_certificate(
        obstruction_profile,
        resources,
        "additive_three_channel_capacity",
    )
    if additive["integer_feasible"]:
        attach_additive_channel_flow(additive, resources, "channel_capacity")
    if global_additive["integer_feasible"]:
        attach_additive_channel_flow(
            global_additive, resources, "global_channel_capacity"
        )
    if global_additive_full["integer_feasible"]:
        attach_additive_channel_flow(
            global_additive_full, resources, "global_channel_capacity"
        )

    resource_rows = [resources[key] for key in sorted(resources)]
    return {
        "arithmetic": (
            "Close every exact unit-cost optimum and its complete minimizing demand set. "
            "Then solve both a factor-support-window ledger and a full-spectrum ledger. "
            "For the latter, continue exact target-shell search when a nonminimum Pareto "
            "vector is needed to fit the coordinate capacities."
        ),
        "conditional_resource_map": (
            "The finite demand sets and q-adic height counts are exact. The implication "
            "that one overflow layer consumes one block, modulus-difference, or "
            "label-difference unit is NOT proved. The additive model also treats the "
            "three channels as independent and may double-count one arithmetic source."
        ),
        "interpretation": (
            "The support-window ledger has a strict full-fibre price obstruction, while "
            "the still more optimistic full-spectrum ledger has an explicit integral "
            "flow. Neither statement is a Type-I/II certificate, descent, or proof that "
            "overflow is arithmetically forced to use the displayed resources."
        ),
        "integer_model": {
            "choice": "sum_{e in D_s} x_{s,e}=1, x_{s,e} in {0,1}",
            "demand": "d_{p,q}=sum_{s:p_s=p} sum_e e_q x_{s,e}",
            "capacity": "d_{p,q}<=C_{p,q}",
            "flow": (
                "for additive channels, sum_c y_{s,q,c}=sum_e e_q x_{s,e}; "
                "sum_s y_{s,q,c}<=C_{p,q,c}, y integral"
            ),
            "demand_set": (
                "The unit-optimal audit uses D_s=E_s^(1). The full-spectrum flow uses "
                "the first exact target shell inside its coordinate-capacity box; every "
                "listed column is globally Pareto minimal."
            ),
        },
        "pareto_input": PARETO_INPUT.name,
        "pareto_input_sha256": sha256(PARETO_INPUT),
        "upper_bound_input": UPPER_INPUT.name,
        "upper_bound_input_sha256": sha256(UPPER_INPUT),
        "source_script": SOURCE_SCRIPT.name,
        "source_script_sha256": sha256(SOURCE_SCRIPT),
        "state_count": len(profiles),
        "prime_count": len(source_cache),
        "resource_count": len(resources),
        "demand_audit": demand_audit,
        "resource_aggregate": {
            "block_capacity": sum(int(row["block_capacity"]) for row in resource_rows),
            "independent_max_capacity": sum(
                int(row["independent_max_capacity"]) for row in resource_rows
            ),
            "additive_three_channel_capacity": sum(
                int(row["additive_three_channel_capacity"]) for row in resource_rows
            ),
            "global_block_capacity": sum(
                int(row["global_block_capacity"]) for row in resource_rows
            ),
            "global_independent_max_capacity": sum(
                int(row["global_independent_max_capacity"]) for row in resource_rows
            ),
            "global_additive_three_channel_capacity": sum(
                int(row["global_additive_three_channel_capacity"])
                for row in resource_rows
            ),
        },
        "model_summary": {
            "block_only": compact_model(block),
            "independent_max": compact_model(independent_max),
            "additive_three_channel": compact_model(additive),
            "global_block_only": compact_model(global_block),
            "global_independent_max": compact_model(global_independent_max),
            "global_additive_three_channel": compact_model(global_additive),
            "global_additive_full_pareto": compact_model(global_additive_full),
        },
        "demand_profiles": profiles,
        "global_resource_feasible_audit": global_feasible_audit,
        "support_window_full_fiber_price_certificate": (
            support_window_price_certificate
        ),
        "resources": resource_rows,
        "models": {
            "block_only": block,
            "independent_max": independent_max,
            "additive_three_channel": additive,
            "global_block_only": global_block,
            "global_independent_max": global_independent_max,
            "global_additive_three_channel": global_additive,
            "global_additive_full_pareto": global_additive_full,
        },
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": result["state_count"],
                "prime_count": result["prime_count"],
                "resource_count": result["resource_count"],
                "demand_audit": result["demand_audit"],
                "resource_aggregate": result["resource_aggregate"],
                "model_summary": result["model_summary"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
