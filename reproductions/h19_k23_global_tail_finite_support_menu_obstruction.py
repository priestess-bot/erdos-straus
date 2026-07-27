#!/usr/bin/env python3
"""Exclude every fixed finite nonbase-prime support menu on one H19-k23 ray."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-tail-finite-support-menu-obstruction-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
BASE_OBSTRUCTION = ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py"
DEFAULT_MENU = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 79,
    97, 101, 103, 87_060_409_452_631,
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_finite_support_global_closure", GLOBAL_CLOSURE)
base_obstruction = load_module(
    "h19_k23_finite_support_base_obstruction", BASE_OBSTRUCTION
)


def crt_pair(
    residue: int, modulus: int, other_residue: int, other_modulus: int
) -> tuple[int, int]:
    """Combine two congruences with coprime moduli."""
    if math.gcd(modulus, other_modulus) != 1:
        raise ValueError("CRT moduli must be coprime")
    multiplier = (
        (other_residue - residue) * pow(modulus, -1, other_modulus)
    ) % other_modulus
    combined = modulus * other_modulus
    return (residue + modulus * multiplier) % combined, combined


def support_residue_divisor(
    prime: int, gap: int, support_primes: set[int], require_size_bound: bool
) -> int | None:
    """Return a target-residue divisor of x^2 supported on support_primes."""
    q = (gap + 1) // 4
    u = (prime + gap) // (gap + 1)
    x = q * u
    values = [1]
    for factor in sorted(support_primes):
        exponent = base_obstruction.valuation(x, factor)
        if exponent:
            values = [
                value * factor**power
                for value in values
                for power in range(2 * exponent + 1)
            ]
    candidates = [value for value in values if value % gap == (-x) % gap]
    if require_size_bound:
        candidates = [value for value in candidates if value <= x]
    return min(candidates) if candidates else None


def frozen_local_primes(
    coefficient: int, period: int, gaps: list[int]
) -> set[int]:
    """Include all ramified and all fixed q=(m+1)/4 primes."""
    frozen = set(sympy.factorint(coefficient * period))
    frozen.update(sympy.primerange(2, len(gaps) + 2))
    frozen.update(
        factor
        for gap in gaps
        for factor in sympy.factorint((gap + 1) // 4)
    )
    return frozen


def choose_seed(
    payload: dict[str, object],
    forms: dict[int, tuple[int, int]],
    bases: dict[int, set[int]],
) -> tuple[dict[str, object], int, int, int, set[int]]:
    """Choose a pressure seed with no raw target residue in its local support."""
    gaps = sorted(bases)
    for family in payload["families"]:
        coefficient, constant = forms[int(family["branch_v_mod_29"])]
        prime = int(family["prime_seed"])
        period = int(family["parameter_period"])
        frozen = frozen_local_primes(coefficient, period, gaps)
        if any(
            support_residue_divisor(
                prime, gap, bases[gap] | frozen, require_size_bound=False
            )
            is not None
            for gap in gaps
        ):
            continue
        return family, coefficient, constant, period, frozen
    raise AssertionError("no pressure seed avoids the finite local support")


def freeze_local_primes(
    prime: int, period: int, bases: dict[int, set[int]], frozen: set[int]
) -> int:
    """Extend a period so every frozen prime has fixed valuation at every tail."""
    result = period
    for gap in bases:
        u = (prime + gap) // (gap + 1)
        for factor in frozen:
            result = math.lcm(
                result, factor ** (base_obstruction.valuation(u, factor) + 1)
            )
    return result


def choose_outer_residue(
    prime: int, coefficient: int, period: int, gaps: list[int], selected_prime: int
) -> tuple[int, int]:
    """Avoid a prime in p and every u_m along the refined progression."""
    forbidden = {
        (-prime * pow(coefficient * period, -1, selected_prime)) % selected_prime
    }
    for gap in gaps:
        slope = coefficient // (gap + 1)
        u = (prime + gap) // (gap + 1)
        forbidden.add(
            (-u * pow(slope * period, -1, selected_prime)) % selected_prime
        )
    residue = next(
        candidate for candidate in range(selected_prime) if candidate not in forbidden
    )
    return residue, len(forbidden)


def run_audit(
    payload: dict[str, object], menu: tuple[int, ...] = DEFAULT_MENU
) -> dict[str, object]:
    """Build one primitive prime progression avoiding a fixed finite support menu."""
    if not menu:
        raise ValueError("nonbase support menu must not be empty")
    if len(set(menu)) != len(menu) or not all(sympy.isprime(prime) for prime in menu):
        raise ValueError("nonbase support menu must contain distinct primes")
    _, bases = global_closure.global_tail_bases()
    gaps = sorted(bases)
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in base_obstruction.boundary.remaining_branches()
    }
    family, coefficient, constant, base_period, frozen = choose_seed(
        payload, forms, bases
    )
    prime = int(family["prime_seed"])
    parameter = int(family["parameter_seed"])
    if coefficient * parameter + constant != prime:
        raise AssertionError("selected pressure seed does not match its branch")
    period = freeze_local_primes(prime, base_period, bases, frozen)
    for gap in gaps:
        if period % gap:
            raise AssertionError("refined period changed a global target residue")
        slope = coefficient // (gap + 1)
        original_u = (prime + gap) // (gap + 1)
        shifted_u = original_u + slope * period
        for factor in frozen:
            exponent = base_obstruction.valuation(original_u, factor)
            if (slope * period) % factor ** (exponent + 1):
                raise AssertionError("refined period did not freeze a local valuation")
            if base_obstruction.valuation(shifted_u, factor) != exponent:
                raise AssertionError("local valuation changed under the refined period")
        if support_residue_divisor(
            prime, gap, bases[gap] | frozen, require_size_bound=False
        ) is not None:
            raise AssertionError("frozen support unexpectedly has a raw witness")
        if support_residue_divisor(
            shifted_u * (gap + 1) - gap,
            gap,
            bases[gap] | frozen,
            require_size_bound=False,
        ) is not None:
            raise AssertionError("frozen support changed under the refined period")

    outer_residue, outer_modulus = 0, 1
    local_rows = []
    for selected_prime in menu:
        if selected_prime in frozen:
            local_rows.append({"prime": selected_prime, "mode": "frozen-support"})
            continue
        if selected_prime <= len(gaps) + 1:
            raise AssertionError("unfrozen menu prime is below the root bound")
        if math.gcd(selected_prime, coefficient * period) != 1:
            raise AssertionError("unfrozen menu prime is unexpectedly ramified")
        local_residue, root_count = choose_outer_residue(
            prime, coefficient, period, gaps, selected_prime
        )
        outer_residue, outer_modulus = crt_pair(
            outer_residue, outer_modulus, local_residue, selected_prime
        )
        local_rows.append(
            {
                "prime": selected_prime,
                "mode": "crt-avoided",
                "avoiding_outer_residue": local_residue,
                "forbidden_root_count": root_count,
            }
        )
    selected_parameter = parameter + period * outer_residue
    selected_target = coefficient * selected_parameter + constant
    progression_step = coefficient * period * outer_modulus
    if math.gcd(progression_step, selected_target) != 1:
        raise AssertionError("finite-support progression is not primitive")
    if selected_target % 24 != 1 or progression_step % 24:
        raise AssertionError("finite-support progression left the core-prime class")
    for gap in gaps:
        if support_residue_divisor(
            selected_target, gap, bases[gap] | set(menu), require_size_bound=False
        ) is not None:
            raise AssertionError("finite support menu supplied a raw witness")
    return {
        "arithmetic": (
            "a pressure seed whose every 72-tail target residue is absent from the full "
            "divisor set supported on its finite local prime set is selected, without "
            "using d<=x. That set contains all ramified primes, every prime at most 73, "
            "and every fixed q=(m+1)/4 prime. Refining the period freezes its local "
            "valuations. Every other menu prime is larger than the 73-root bound and "
            "unramified, so CRT avoids it in p and every u_m. The primitive resulting "
            "progression has infinitely many core-prime terms by Dirichlet"
        ),
        "scope_note": (
            "An infinite obstruction to every fixed finite nonbase-prime support menu "
            "within the canonical 72-tail Type II framework. It does not exclude an "
            "unbounded adaptive factor choice or a different descent state."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "global_tail_count": len(gaps),
        "seed_prime": prime,
        "seed_branch_v_mod_29": int(family["branch_v_mod_29"]),
        "frozen_local_primes": sorted(frozen),
        "menu_primes": list(menu),
        "outer_parameter_residue": outer_residue,
        "outer_parameter_modulus": outer_modulus,
        "local_avoidance": local_rows,
        "prime_progression_offset": selected_target,
        "prime_progression_step": progression_step,
        "prime_progression_gcd": math.gcd(progression_step, selected_target),
        "core_prime_residue_mod_24": selected_target % 24,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prime", type=int, action="append")
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    menu = tuple(args.prime) if args.prime else DEFAULT_MENU
    result = run_audit(payload, menu)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
