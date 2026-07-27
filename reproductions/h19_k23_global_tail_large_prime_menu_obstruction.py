#!/usr/bin/env python3
"""Avoid a finite large variable-prime menu across every H19-k23 global tail."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-tail-large-prime-menu-obstruction-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
BASE_OBSTRUCTION = ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_large_menu_global_closure", GLOBAL_CLOSURE)
base_obstruction = load_module(
    "h19_k23_large_menu_base_obstruction", BASE_OBSTRUCTION
)


def crt_pair(
    residue: int, modulus: int, other_residue: int, other_modulus: int
) -> tuple[int, int]:
    """Combine two coprime congruences."""
    if math.gcd(modulus, other_modulus) != 1:
        raise ValueError("CRT moduli must be coprime")
    multiplier = (
        (other_residue - residue) * pow(modulus, -1, other_modulus)
    ) % other_modulus
    combined = modulus * other_modulus
    return (residue + modulus * multiplier) % combined, combined


def default_menu(coefficient: int, period: int) -> tuple[int, ...]:
    """Choose reproducible large primes unramified in the seed progression."""
    result = []
    for prime in sympy.primerange(74, 10_000):
        if math.gcd(int(prime), coefficient * period) == 1:
            result.append(int(prime))
        if len(result) == 7:
            return tuple(result)
    raise AssertionError("could not find the default large-prime menu")


def choose_local_residue(
    prime: int,
    offset: int,
    coefficient: int,
    period: int,
    gaps: list[int],
) -> tuple[int, int]:
    """Avoid prime divisibility in p and every global variable tail factor."""
    forbidden = {
        (-offset * pow(coefficient * period, -1, prime)) % prime
    }
    for gap in gaps:
        slope = coefficient // (gap + 1)
        u_offset = (offset + gap) // (gap + 1)
        forbidden.add((-u_offset * pow(slope * period, -1, prime)) % prime)
    residue = next(candidate for candidate in range(prime) if candidate not in forbidden)
    return residue, len(forbidden)


def run_audit(
    payload: dict[str, object], menu: tuple[int, ...] | None = None
) -> dict[str, object]:
    """Build a primitive prime progression avoiding a finite large menu globally."""
    _, bases = global_closure.global_tail_bases()
    gaps = sorted(bases)
    seed = payload["families"][0]
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in base_obstruction.boundary.remaining_branches()
    }
    coefficient, constant = forms[int(seed["branch_v_mod_29"])]
    parameter = int(seed["parameter_seed"])
    period = int(seed["parameter_period"])
    offset = coefficient * parameter + constant
    if offset != int(seed["prime_progression_offset"]):
        raise AssertionError("prime-obstruction seed does not match its branch")
    primes = menu if menu is not None else default_menu(coefficient, period)
    if not primes:
        raise ValueError("variable-prime menu must not be empty")
    outer_residue, outer_modulus = 0, 1
    local_rows = []
    for prime in primes:
        if prime <= len(gaps) + 1 or not sympy.isprime(prime):
            raise ValueError("menu primes must exceed the global-tail root bound")
        if math.gcd(prime, coefficient * period) != 1:
            raise ValueError("menu primes must be unramified in the seed progression")
        local_residue, root_count = choose_local_residue(
            prime, offset, coefficient, period, gaps
        )
        outer_residue, outer_modulus = crt_pair(
            outer_residue, outer_modulus, local_residue, prime
        )
        local_rows.append(
            {
                "prime": prime,
                "avoiding_outer_residue": local_residue,
                "forbidden_root_count": root_count,
            }
        )
    selected_parameter = parameter + period * outer_residue
    selected_prime = coefficient * selected_parameter + constant
    progression_step = coefficient * period * outer_modulus
    if math.gcd(progression_step, selected_prime) != 1:
        raise AssertionError("large-menu progression is not primitive")
    if selected_prime % 24 != 1 or progression_step % 24:
        raise AssertionError("large-menu progression left the core-prime class")
    if any(
        selected_prime % prime == 0
        or any(
            ((selected_prime + gap) // (gap + 1)) % prime == 0
            for gap in gaps
        )
        for prime in primes
    ):
        raise AssertionError("CRT selection did not avoid the global variable menu")
    if any(
        base_obstruction.base_only_residue_divisor(
            selected_prime, gap, bases[gap], False
        )
        is not None
        for gap in gaps
    ):
        raise AssertionError("large-menu progression lost its all-tail base obstruction")
    return {
        "arithmetic": (
            "on t=t0+M*n, each unramified menu prime ell has at most one root for "
            "ell|p and at most one root for ell|u_m for each of the 72 global tails. "
            "Thus at most 73 residues modulo ell are forbidden; ell>73 supplies an "
            "avoiding class, and CRT combines every finite menu. The inherited all-tail "
            "base-only miss and primitivity give infinitely many core primes by Dirichlet"
        ),
        "scope_note": (
            "An infinite obstruction to finite variable-prime menus whose entries exceed "
            "the 73-root bound and are unramified in the chosen pressure progression. "
            "It does not yet exclude finite menus containing the finitely many small or "
            "ramified primes, nor adaptive factors outside a fixed menu."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "global_tail_count": len(gaps),
        "menu_primes": list(primes),
        "outer_parameter_residue": outer_residue,
        "outer_parameter_modulus": outer_modulus,
        "local_avoidance": local_rows,
        "prime_progression_offset": selected_prime,
        "prime_progression_step": progression_step,
        "prime_progression_gcd": math.gcd(progression_step, selected_prime),
        "core_prime_residue_mod_24": selected_prime % 24,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prime", type=int, action="append")
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    menu = tuple(args.prime) if args.prime else None
    result = run_audit(payload, menu)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
