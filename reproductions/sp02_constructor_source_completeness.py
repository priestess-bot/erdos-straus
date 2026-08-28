#!/usr/bin/env python3
"""Independent finite-model verifier for the SP-02 conditional theorem.

The model uses canonical post-tie-break output relations.  It checks the
explicit state-change registry, the stated well-formedness assumptions,
computes the least reachable fixed point, classifies constructors, and runs
the seven negative controls described in the SP-02 dossier.

This is deliberately an abstract finite-model tool.  It does not inspect the
repository constructor census and cannot prove that a concrete implementation
has supplied a complete model.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import json
from typing import Iterable, Mapping


ACTIVE_PRODUCER = "ACTIVE_PRODUCER"
TERMINAL_ONLY = "TERMINAL_ONLY"
NONRUNTIME_CONTROL = "NONRUNTIME_CONTROL"
OBSOLETE_OR_UNREACHABLE = "OBSOLETE_OR_UNREACHABLE"
UNKNOWN = "UNKNOWN"

TerminalRecord = tuple[str, str, str]
SuccessorRecord = tuple[str, str, str]
InvokeRecord = tuple[str, str]
StateChangeRecord = tuple[str, str, str, str]


class SP02ModelError(ValueError):
    """A finite model violates one of the explicit SP-02 assumptions."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class FiniteModel:
    states: frozenset[str]
    constructors: frozenset[str]
    witnesses: frozenset[str]
    solutions: frozenset[str]
    roots: frozenset[str]
    legal: frozenset[str]
    verify_sol: frozenset[tuple[str, str]]
    selectors: frozenset[str]
    invokes: Mapping[str, frozenset[InvokeRecord]]
    terminals: Mapping[str, frozenset[TerminalRecord]]
    successors: Mapping[str, frozenset[SuccessorRecord]]
    state_change_registry: frozenset[StateChangeRecord]

    @property
    def controls(self) -> frozenset[str]:
        return self.constructors - self.selectors

    def validate(self) -> None:
        """Check the finite well-formedness contract before classification."""

        if not self.roots <= self.states:
            raise SP02ModelError("DOMAIN", "roots contain an unknown state")
        if not self.legal <= self.states:
            raise SP02ModelError("DOMAIN", "legal contains an unknown state")
        if not self.selectors <= self.constructors:
            raise SP02ModelError("DOMAIN", "selectors contain an unknown constructor")
        if set(self.invokes) != set(self.constructors):
            raise SP02ModelError("RELATION_KEYS", "invoke keys do not equal constructors")
        if set(self.terminals) != set(self.constructors):
            raise SP02ModelError("RELATION_KEYS", "terminal keys do not equal constructors")
        if set(self.successors) != set(self.constructors):
            raise SP02ModelError("RELATION_KEYS", "successor keys do not equal constructors")

        for source, solution in self.verify_sol:
            if source not in self.states or solution not in self.solutions:
                raise SP02ModelError("VERIFY_DOMAIN", "VerifySol contains an out-of-domain pair")

        terminal_by_call: set[tuple[str, str, str]] = set()
        successor_by_call: set[tuple[str, str, str]] = set()
        all_successors: set[StateChangeRecord] = set()

        for constructor in self.constructors:
            for source, witness in self.invokes[constructor]:
                if source not in self.states or witness not in self.witnesses:
                    raise SP02ModelError("INVOKE_DOMAIN", f"{constructor} has an out-of-domain invocation")

            for source, witness, solution in self.terminals[constructor]:
                if source not in self.states or witness not in self.witnesses or solution not in self.solutions:
                    raise SP02ModelError("TERMINAL_DOMAIN", f"{constructor} has an out-of-domain terminal")
                if (source, witness) not in self.invokes[constructor] or source not in self.legal:
                    raise SP02ModelError("OUTPUT_BINDING", f"{constructor} terminal is not bound to a legal invocation")
                if (source, solution) not in self.verify_sol:
                    raise SP02ModelError("TERMINAL_UNVERIFIED", f"{constructor} terminal is not in VerifySol")
                terminal_by_call.add((constructor, source, witness))

            for source, witness, target in self.successors[constructor]:
                if source not in self.states or target not in self.states or witness not in self.witnesses:
                    raise SP02ModelError("SUCCESSOR_DOMAIN", f"{constructor} has an out-of-domain successor")
                if (source, witness) not in self.invokes[constructor] or source not in self.legal:
                    raise SP02ModelError("OUTPUT_BINDING", f"{constructor} successor is not bound to a legal invocation")
                if target not in self.legal:
                    raise SP02ModelError("TARGET_ILLEGAL", f"{constructor} successor target is not legal")
                successor_by_call.add((constructor, source, witness))
                all_successors.add((constructor, source, witness, target))

        if terminal_by_call & successor_by_call:
            raise SP02ModelError("TERMINAL_SUCCESSOR_CONFLICT", "one canonical invocation has both output kinds")

        if self.state_change_registry != frozenset(all_successors):
            raise SP02ModelError(
                "STATE_CHANGE_REGISTRY",
                "explicit StateChangeRegistry does not equal the complete successor table",
            )

        for constructor in self.controls:
            if self.successors[constructor]:
                raise SP02ModelError("CONTROL_SUCCESSOR", f"control {constructor} has a successor")

        reachable = self.reach()
        self._validate_selector_totality(reachable)
        self._validate_constructor_owner_uniqueness(reachable)

    def reach(self) -> frozenset[str]:
        """Compute the least fixed point of the selector successor operator."""

        reached = set(self.roots & self.legal)
        changed = True
        while changed:
            changed = False
            for constructor in self.selectors:
                for source, _witness, target in self.successors[constructor]:
                    if source in reached and target in self.legal and target not in reached:
                        reached.add(target)
                        changed = True
        return frozenset(reached)

    def live_domain(self, constructor: str, reachable: Iterable[str] | None = None) -> frozenset[str]:
        reached = self.reach() if reachable is None else frozenset(reachable)
        return frozenset(
            source
            for source, _witness in self.invokes[constructor]
            if source in reached
        )

    def classify(self) -> dict[str, str]:
        self.validate()
        reachable = self.reach()
        labels: dict[str, str] = {}
        for constructor in sorted(self.constructors):
            live = self.live_domain(constructor, reachable)
            has_successor = any(
                source in live
                for source, _witness, _target in self.successors[constructor]
            )
            has_terminal = any(
                source in live
                for source, _witness, _solution in self.terminals[constructor]
            )
            if not live:
                labels[constructor] = OBSOLETE_OR_UNREACHABLE
            elif has_successor:
                labels[constructor] = ACTIVE_PRODUCER
            elif has_terminal:
                labels[constructor] = TERMINAL_ONLY
            elif constructor in self.controls:
                labels[constructor] = NONRUNTIME_CONTROL
            else:
                labels[constructor] = UNKNOWN
        return labels

    def _validate_selector_totality(self, reachable: frozenset[str]) -> None:
        for constructor in self.selectors:
            for source, witness in self.invokes[constructor]:
                if source not in reachable:
                    continue
                output_count = sum(
                    1
                    for terminal_source, terminal_witness, _solution in self.terminals[constructor]
                    if (terminal_source, terminal_witness) == (source, witness)
                )
                output_count += sum(
                    1
                    for successor_source, successor_witness, _target in self.successors[constructor]
                    if (successor_source, successor_witness) == (source, witness)
                )
                if output_count != 1:
                    raise SP02ModelError(
                        "SELECTOR_NOT_TOTAL",
                        f"{constructor} invocation ({source}, {witness}) has {output_count} canonical outputs",
                    )

    def _validate_constructor_owner_uniqueness(self, reachable: frozenset[str]) -> None:
        owners: dict[tuple[str, str], str] = {}
        for constructor in self.constructors:
            for source, _witness, target in self.successors[constructor]:
                if source not in reachable:
                    continue
                key = (source, target)
                previous = owners.setdefault(key, constructor)
                if previous != constructor:
                    raise SP02ModelError(
                        "SUCCESSOR_OWNER_CONFLICT",
                        f"{key} is emitted by both {previous} and {constructor}",
                    )

    def report(self) -> dict[str, object]:
        labels = self.classify()
        reachable = sorted(self.reach())
        unknown = sorted(
            constructor
            for constructor, label in labels.items()
            if label == UNKNOWN
        )
        return {
            "states": len(self.states),
            "constructors": len(self.constructors),
            "reachable": reachable,
            "labels": labels,
            "unknown_constructors": unknown,
            "unknown_count": len(unknown),
            "state_change_records": len(self.state_change_registry),
            "status": "PASS" if not unknown else "UNKNOWN_PRESENT",
        }


def _replace(
    model: FiniteModel,
    *,
    invokes: Mapping[str, frozenset[InvokeRecord]] | None = None,
    terminals: Mapping[str, frozenset[TerminalRecord]] | None = None,
    successors: Mapping[str, frozenset[SuccessorRecord]] | None = None,
    verify_sol: frozenset[tuple[str, str]] | None = None,
    state_change_registry: frozenset[StateChangeRecord] | None = None,
) -> FiniteModel:
    return replace(
        model,
        invokes=model.invokes if invokes is None else invokes,
        terminals=model.terminals if terminals is None else terminals,
        successors=model.successors if successors is None else successors,
        verify_sol=model.verify_sol if verify_sol is None else verify_sol,
        state_change_registry=(
            model.state_change_registry
            if state_change_registry is None
            else state_change_registry
        ),
    )


def good_model() -> FiniteModel:
    states = frozenset({"r", "a", "z", "b"})
    constructors = frozenset({"p", "t", "k", "u"})
    invokes = {
        "p": frozenset({("r", "w_p")}),
        "t": frozenset({("a", "w_t")}),
        "k": frozenset({("r", "w_k")}),
        "u": frozenset({("z", "w_u")}),
    }
    terminals = {
        "p": frozenset(),
        "t": frozenset({("a", "w_t", "s_star")}),
        "k": frozenset(),
        "u": frozenset(),
    }
    successors = {
        "p": frozenset({("r", "w_p", "a")}),
        "t": frozenset(),
        "k": frozenset(),
        "u": frozenset({("z", "w_u", "z")}),
    }
    registry = frozenset(
        {
            ("p", "r", "w_p", "a"),
            ("u", "z", "w_u", "z"),
        }
    )
    return FiniteModel(
        states=states,
        constructors=constructors,
        witnesses=frozenset({"w_p", "w_t", "w_k", "w_u"}),
        solutions=frozenset({"s_star"}),
        roots=frozenset({"r"}),
        legal=frozenset({"r", "a", "z"}),
        verify_sol=frozenset({("a", "s_star")}),
        selectors=frozenset({"p", "t", "u"}),
        invokes=invokes,
        terminals=terminals,
        successors=successors,
        state_change_registry=registry,
    )


def _expect_reject(model: FiniteModel, expected_code: str) -> None:
    try:
        model.validate()
    except SP02ModelError as error:
        if error.code != expected_code:
            raise AssertionError(
                f"expected {expected_code}, got {error.code}: {error.detail}"
            ) from error
        return
    raise AssertionError(f"model unexpectedly accepted; expected {expected_code}")


def verify_controls() -> dict[str, object]:
    model = good_model()
    report = model.report()
    expected_labels = {
        "p": ACTIVE_PRODUCER,
        "t": TERMINAL_ONLY,
        "k": NONRUNTIME_CONTROL,
        "u": OBSOLETE_OR_UNREACHABLE,
    }
    if report["labels"] != expected_labels or report["reachable"] != ["a", "r"]:
        raise AssertionError(f"good model report mismatch: {report}")
    if report["unknown_count"] != 0:
        raise AssertionError("good model has an UNKNOWN classification")

    controls: dict[str, tuple[FiniteModel, str]] = {}
    rogue_registry = model.state_change_registry | {("p", "a", "w_p", "z")}
    controls["NC-1"] = (_replace(model, state_change_registry=rogue_registry), "STATE_CHANGE_REGISTRY")

    terminals = dict(model.terminals)
    successors = dict(model.successors)
    successors["t"] = frozenset({("a", "w_t", "r")})
    successors["p"] = successors["p"]
    controls["NC-2"] = (
        _replace(
            model,
            terminals=terminals,
            successors=successors,
            state_change_registry=frozenset(
                {("p", "r", "w_p", "a"), ("t", "a", "w_t", "r"), ("u", "z", "w_u", "z")}
            ),
        ),
        "TERMINAL_SUCCESSOR_CONFLICT",
    )

    successors = dict(model.successors)
    successors["u"] = frozenset({("z", "w_u", "z"), ("r", "w_u", "a")})
    invokes = dict(model.invokes)
    invokes["u"] = invokes["u"] | {("r", "w_u")}
    controls["NC-3"] = (
        _replace(
            model,
            invokes=invokes,
            successors=successors,
            state_change_registry=frozenset(
                {
                    ("p", "r", "w_p", "a"),
                    ("u", "z", "w_u", "z"),
                    ("u", "r", "w_u", "a"),
                }
            ),
        ),
        "SUCCESSOR_OWNER_CONFLICT",
    )

    successors = dict(model.successors)
    successors["k"] = frozenset({("r", "w_k", "a")})
    controls["NC-4"] = (
        _replace(
            model,
            successors=successors,
            state_change_registry=frozenset(
                {
                    ("p", "r", "w_p", "a"),
                    ("k", "r", "w_k", "a"),
                    ("u", "z", "w_u", "z"),
                }
            ),
        ),
        "CONTROL_SUCCESSOR",
    )

    invokes = dict(model.invokes)
    invokes["u"] = invokes["u"] | {("r", "w_u")}
    controls["NC-5"] = (_replace(model, invokes=invokes), "SELECTOR_NOT_TOTAL")

    terminals = dict(model.terminals)
    terminals["k"] = frozenset({("r", "w_k", "s_star")})
    controls["NC-6"] = (_replace(model, terminals=terminals), "TERMINAL_UNVERIFIED")

    successors = dict(model.successors)
    successors["p"] = frozenset({("r", "w_p", "b")})
    controls["NC-7"] = (
        _replace(
            model,
            successors=successors,
            state_change_registry=frozenset(
                {("p", "r", "w_p", "b"), ("u", "z", "w_u", "z")}
            ),
        ),
        "TARGET_ILLEGAL",
    )

    negative_results: dict[str, str] = {}
    for control_id, (negative_model, expected_code) in controls.items():
        _expect_reject(negative_model, expected_code)
        negative_results[control_id] = expected_code

    return {
        "good_model": report,
        "negative_controls": negative_results,
        "negative_control_count": len(negative_results),
        "status": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the good model and all negative controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify_controls(), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
