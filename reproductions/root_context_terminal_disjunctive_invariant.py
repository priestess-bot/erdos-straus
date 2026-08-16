#!/usr/bin/env python3
"""Check the root-certificate / marked-fiber outcome distinction.

This is a fixed p=73 type control.  It does not assert reachability of the
illustrative mark, search prime ranges, or provide a global selector.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable

from type_i_atomic_split_total_typed_rechart import (
    direct_certificate_denominators,
)


Triple = tuple[int, int, int]
Mark = Callable[[Triple], bool]


@dataclass(frozen=True)
class RootContextState:
    """A state keeps its root prime even when its local equation changes."""

    root_prime: int
    equation_target: tuple[int, int]
    mark_name: str
    mark: Mark


@dataclass(frozen=True)
class RootCertificate:
    """A verified Type I/II receipt for the immutable root equation."""

    root_prime: int
    receipt_kind: str
    gap: int
    divisor: int
    denominators: Triple


@dataclass(frozen=True)
class RootTerminalOutcome:
    certificate: RootCertificate


@dataclass(frozen=True)
class MarkedTerminalOutcome:
    solution: Triple


Outcome = RootTerminalOutcome | MarkedTerminalOutcome


def solves_root_equation(prime: int, triple: Triple) -> bool:
    """Use the cleared-denominator identity for 4/prime."""
    x, y, z = triple
    return (
        prime > 1
        and x > 0
        and y > 0
        and z > 0
        and 4 * x * y * z == prime * (x * y + x * z + y * z)
    )


def direct_root_certificate(
    prime: int, kind: str, gap: int, divisor: int
) -> RootCertificate:
    """Materialize an already registered direct Type I/II receipt."""
    triple = direct_certificate_denominators(prime, kind, gap, divisor)
    certificate = RootCertificate(prime, kind, gap, divisor, triple)
    if not verifies_registered_direct_receipt(certificate):
        raise AssertionError("direct receipt did not solve its root equation")
    return certificate


def verifies_registered_direct_receipt(certificate: RootCertificate) -> bool:
    """Rebuild the named Type I/II receipt rather than trust its payload."""
    try:
        expected = direct_certificate_denominators(
            certificate.root_prime,
            certificate.receipt_kind,
            certificate.gap,
            certificate.divisor,
        )
    except (AssertionError, ValueError):
        return False
    return (
        expected == certificate.denominators
        and solves_root_equation(certificate.root_prime, certificate.denominators)
    )


def admit_root_terminal(
    state: RootContextState, certificate: RootCertificate
) -> RootTerminalOutcome:
    """Admit only a certificate for the immutable root, never for a local target."""
    if state.root_prime != certificate.root_prime:
        raise ValueError("certificate root does not match state root context")
    if not verifies_registered_direct_receipt(certificate):
        raise ValueError("certificate is not its registered direct root receipt")
    return RootTerminalOutcome(certificate)


def admit_marked_terminal(
    state: RootContextState, certificate: RootCertificate
) -> MarkedTerminalOutcome:
    """The marked-terminal path still requires literal mark membership."""
    if state.root_prime != certificate.root_prime:
        raise ValueError("certificate root does not match marked state")
    if not verifies_registered_direct_receipt(certificate):
        raise ValueError("candidate is not its registered direct root receipt")
    if not state.mark(certificate.denominators):
        raise ValueError("candidate is not in the current marked solution set")
    return MarkedTerminalOutcome(certificate.denominators)


def lift_outcome(
    outcome: Outcome, marked_lift: Callable[[Triple], Triple]
) -> Outcome:
    """Extend a verified marked lift by identity on root certificates."""
    if isinstance(outcome, RootTerminalOutcome):
        return outcome
    return MarkedTerminalOutcome(marked_lift(outcome.solution))


def type_ii_mark(prime: int) -> Mark:
    """Use a nonempty familiar mark: the second and third tails carry p."""

    def belongs(triple: Triple) -> bool:
        _, y, z = triple
        return y % prime == 0 and z % prime == 0

    return belongs


def verify() -> None:
    """Show both summands and reject a certificate tied to another root."""
    prime = 73
    state = RootContextState(
        root_prime=prime,
        equation_target=(4, prime),
        mark_name="two_p_tails",
        mark=type_ii_mark(prime),
    )
    type_i = direct_root_certificate(prime, "I", 7, 10)
    type_ii = direct_root_certificate(prime, "II", 7, 1)

    assert type_i.denominators == (20, 210, 30_660)
    assert type_ii.denominators == (20, 219, 4_380)
    assert not state.mark(type_i.denominators)
    assert state.mark(type_ii.denominators)

    root_outcome = admit_root_terminal(state, type_i)
    assert isinstance(root_outcome, RootTerminalOutcome)
    assert lift_outcome(root_outcome, lambda triple: triple) == root_outcome

    marked_outcome = admit_marked_terminal(state, type_ii)
    assert isinstance(marked_outcome, MarkedTerminalOutcome)
    assert lift_outcome(marked_outcome, lambda triple: triple) == marked_outcome

    # A direct root certificate closes the same root even from another local target.
    changed_target = RootContextState(
        root_prime=prime,
        equation_target=(3, 7),
        mark_name="unrelated_local_mark",
        mark=lambda triple: False,
    )
    assert admit_root_terminal(changed_target, type_i) == root_outcome

    wrong_root = RootContextState(
        root_prime=241,
        equation_target=(4, 241),
        mark_name="two_p_tails",
        mark=type_ii_mark(241),
    )
    try:
        admit_root_terminal(wrong_root, type_i)
    except ValueError as error:
        assert "root context" in str(error)
    else:
        raise AssertionError("a certificate for p=73 entered a p=241 root context")

    try:
        admit_marked_terminal(state, type_i)
    except ValueError as error:
        assert "marked solution set" in str(error)
    else:
        raise AssertionError("a root terminal was silently promoted to marked")

    forged = RootCertificate(prime, "I", 7, 10, (1, 1, 1))
    try:
        admit_root_terminal(state, forged)
    except ValueError as error:
        assert "registered direct root receipt" in str(error)
    else:
        raise AssertionError("a forged root-certificate payload was accepted")

    print(
        "verified root-certificate disjunction: same-root direct certificates "
        "survive lifts, marks remain strict, and cross-root reuse is rejected"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
