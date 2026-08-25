#!/usr/bin/env python3
"""Audit the T6 constructor inventory from active source and active data.

This audit deliberately has two independent inputs:

* active Python syntax supplies a conservative census of code that can mark a
  recursive edge eligible or manufacture/accept a persistent-queue flag;
* the T6 frontier and obligation ledger supply the frozen registered surface.

Agreement between the two data registries is not treated as proof that source
discovery is complete.  Unknown syntax signals, archive references, missing
symbols, and unregistered mappings fail closed.  A structurally honest
inventory may pass while ``closure_ready`` remains false.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence


DEFAULT_INVENTORY = Path("data/t6-constructor-inventory-v1.json")
FRONTIER_PATH = Path("data/t6-proof-frontier-v2.json")
LEDGER_PATH = Path("data/t6-selector-obligation-ledger-v1.json")
KERNEL_PATH = Path("data/pre-t6-contract-kernel-v1.json")
AUDIT_TOOL_PATH = Path("scripts/audit_t6_constructor_inventory_v1.py")

REGISTERED_DISPOSITIONS = {
    "INITIALIZER_PRIMARY",
    "REGISTERED_PRIMARY",
    "REGISTERED_ALIAS",
}


@dataclass(frozen=True)
class AuditResult:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    source_signals: tuple[str, ...]
    queue_api_signals: tuple[str, ...]
    closure_ready: bool

    @property
    def ok(self) -> bool:
        return not self.errors

    def payload(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "closure_ready": self.closure_ready,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "source_signals": list(self.source_signals),
            "queue_api_signals": list(self.queue_api_signals),
        }


def _load_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON file {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"top-level JSON must be an object: {path}")
    return value


def _active_python_files(root: Path, active_roots: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for relative in active_roots:
        base = root / relative
        if not base.is_dir():
            continue
        for path in base.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue
            if path.relative_to(root) == AUDIT_TOOL_PATH:
                continue
            files.append(path)
    return sorted(set(files))


def _function_owner(node: ast.AST, parents: Mapping[ast.AST, ast.AST]) -> str:
    current = node
    while current in parents:
        current = parents[current]
        if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return current.name
    return "<module>"


def _class_owner(node: ast.AST, parents: Mapping[ast.AST, ast.AST]) -> str:
    current = node
    while current in parents:
        current = parents[current]
        if isinstance(current, ast.ClassDef):
            return current.name
    return "<module>"


def _is_persistent_runtime_queue_append(
    node: ast.Call, parents: Mapping[ast.AST, ast.AST], relative: str
) -> bool:
    """Recognize the one concrete queue mutation in the shared runtime.

    Generic list.append calls in reproductions are often search/BFS
    bookkeeping. This deliberately recognizes only the internal queue owned
    by PersistentSelectorRuntimeV1.
    """
    if relative != "scripts/t6_persistent_selector_runtime_v1.py":
        return False
    if not (
        isinstance(node.func, ast.Attribute)
        and node.func.attr == "append"
        and isinstance(node.func.value, ast.Attribute)
        and node.func.value.attr == "_queue"
        and isinstance(node.func.value.value, ast.Name)
        and node.func.value.value.id == "self"
    ):
        return False
    return (
        _class_owner(node, parents) == "PersistentSelectorRuntimeV1"
        and _function_owner(node, parents) == "_enqueue_admitted_target_v1"
    )


def _is_literal_false(node: ast.AST | None) -> bool:
    return isinstance(node, ast.Constant) and node.value is False


def discover_source_signals(root: Path, active_roots: Iterable[str]) -> tuple[str, ...]:
    """Return conservative constructor/queue signals from active Python only."""
    signals: set[str] = set()
    for path in _active_python_files(root, active_roots):
        relative = path.relative_to(root).as_posix()
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        except (OSError, SyntaxError, UnicodeError) as exc:
            signals.add(f"{relative}:<parse-error>:{type(exc).__name__}")
            continue
        parents: dict[ast.AST, ast.AST] = {}
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                parents[child] = node

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                arguments = [
                    *node.args.posonlyargs,
                    *node.args.args,
                    *node.args.kwonlyargs,
                ]
                if any(argument.arg == "persistent_queue" for argument in arguments):
                    signals.add(
                        f"{relative}:{node.name}:persistent_queue_parameter"
                    )

            if isinstance(node, ast.Dict):
                for key, value in zip(node.keys, node.values, strict=True):
                    if (
                        isinstance(key, ast.Constant)
                        and key.value == "recursive_edge_eligible"
                        and not _is_literal_false(value)
                    ):
                        owner = _function_owner(node, parents)
                        signals.add(
                            f"{relative}:{owner}:recursive_edge_eligible_nonfalse"
                        )

            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if (
                        isinstance(target, ast.Subscript)
                        and isinstance(target.slice, ast.Constant)
                        and target.slice.value == "recursive_edge_eligible"
                        and not _is_literal_false(node.value)
                    ):
                        owner = _function_owner(node, parents)
                        signals.add(
                            f"{relative}:{owner}:recursive_edge_eligible_nonfalse"
                        )

            if isinstance(node, ast.Call):
                for keyword in node.keywords:
                    if (
                        keyword.arg == "persistent_queue"
                        and not _is_literal_false(keyword.value)
                    ):
                        owner = _function_owner(node, parents)
                        signals.add(
                            f"{relative}:{owner}:persistent_queue_nonfalse_call"
                        )
    return tuple(sorted(signals))


def discover_queue_api_signals(root: Path, active_roots: Iterable[str]) -> tuple[str, ...]:
    """Find concrete queue mutation calls, not receipt flags or prose labels."""
    signals: set[str] = set()
    for path in _active_python_files(root, active_roots):
        relative = path.relative_to(root).as_posix()
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        except (OSError, SyntaxError, UnicodeError):
            continue
        parents: dict[ast.AST, ast.AST] = {}
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                parents[child] = node
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if _is_persistent_runtime_queue_append(node, parents, relative):
                signals.add(
                    f"{relative}:PersistentSelectorRuntimeV1."
                    "_enqueue_admitted_target_v1:self._queue.append"
                )
                continue
            call_name = ""
            if isinstance(node.func, ast.Name):
                call_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                call_name = node.func.attr
            if call_name not in {"enqueue", "put", "put_nowait"}:
                continue
            owner = _function_owner(node, parents)
            signals.add(f"{relative}:{owner}:{call_name}")
    return tuple(sorted(signals))


def _top_level_symbols(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }


def _as_object_list(value: object, *, name: str, errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append(f"{name} must be a list")
        return []
    result: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            errors.append(f"{name}[{index}] must be an object")
            continue
        result.append(item)
    return result


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _validate_evidence_path(root: Path, reference: str) -> bool:
    if reference.startswith("archive/") or reference.startswith("docs/archive/"):
        return False
    return (root / reference).is_file()


def audit_inventory(
    root: Path,
    inventory_path: Path | None = None,
    *,
    source_signals: Sequence[str] | None = None,
    queue_api_signals: Sequence[str] | None = None,
) -> AuditResult:
    """Audit one inventory against a repository root.

    ``source_signals`` and ``queue_api_signals`` are injectable so mutation
    tests can reuse a real scan or supply a temporary active tree.  Production
    CLI use leaves both unset and always scans the requested root.
    """
    errors: list[str] = []
    warnings: list[str] = []
    inventory_file = inventory_path or root / DEFAULT_INVENTORY
    if not inventory_file.is_absolute():
        inventory_file = root / inventory_file

    try:
        inventory = _load_object(inventory_file)
        frontier = _load_object(root / FRONTIER_PATH)
        ledger = _load_object(root / LEDGER_PATH)
        kernel = _load_object(root / KERNEL_PATH)
    except ValueError as exc:
        return AuditResult((str(exc),), (), (), (), False)

    scope = inventory.get("scope")
    if not isinstance(scope, dict):
        errors.append("scope must be an object")
        scope = {}
    active_roots = scope.get("active_source_roots")
    if not isinstance(active_roots, list) or not all(
        isinstance(item, str) and item for item in active_roots
    ):
        errors.append("scope.active_source_roots must be a nonempty string list")
        active_roots = ["reproductions", "scripts"]
    if any(item.startswith("archive") or item.startswith("docs/archive") for item in active_roots):
        errors.append("ARCHIVE_POLLUTION: archive cannot be an active source root")

    discovered = tuple(source_signals) if source_signals is not None else discover_source_signals(root, active_roots)
    queue_discovered = tuple(queue_api_signals) if queue_api_signals is not None else discover_queue_api_signals(root, active_roots)

    entries = _as_object_list(inventory.get("entries"), name="entries", errors=errors)
    entry_ids = [str(item.get("id", "")) for item in entries]
    if "" in entry_ids:
        errors.append("every inventory entry requires a stable nonempty id")
    for duplicate in sorted(_duplicates(entry_ids)):
        errors.append(f"duplicate inventory entry id: {duplicate}")

    registered_entries: dict[str, dict[str, Any]] = {}
    initializer_entries: dict[str, dict[str, Any]] = {}
    for entry in entries:
        entry_id = str(entry.get("id", "<missing>"))
        implementation = entry.get("implementation")
        if not isinstance(implementation, dict):
            errors.append(f"{entry_id}: implementation must be an object")
            continue
        file_name = implementation.get("file")
        symbols = implementation.get("symbols")
        if not isinstance(file_name, str) or not file_name:
            errors.append(f"{entry_id}: implementation.file is missing")
            continue
        if file_name.startswith("archive/") or file_name.startswith("docs/archive/"):
            errors.append(f"ARCHIVE_POLLUTION: {entry_id} implementation uses {file_name}")
            continue
        source_file = root / file_name
        if not source_file.is_file():
            errors.append(f"{entry_id}: missing implementation file {file_name}")
            continue
        if not isinstance(symbols, list) or not symbols or not all(
            isinstance(symbol, str) and symbol for symbol in symbols
        ):
            errors.append(f"{entry_id}: implementation.symbols must be nonempty")
        else:
            try:
                defined = _top_level_symbols(source_file)
            except (OSError, SyntaxError, UnicodeError) as exc:
                errors.append(f"{entry_id}: cannot parse {file_name}: {exc}")
                defined = set()
            for symbol in symbols:
                if symbol not in defined:
                    errors.append(f"{entry_id}: missing symbol {file_name}:{symbol}")

        correspondence = entry.get("registry_correspondence")
        if not isinstance(correspondence, dict):
            errors.append(f"{entry_id}: registry_correspondence must be an object")
        else:
            kind = correspondence.get("kind")
            registry_id = correspondence.get("id")
            if not isinstance(registry_id, str) or not registry_id:
                errors.append(f"{entry_id}: registry id is missing")
            elif kind == "registered_edge":
                registered_entries[registry_id] = entry
            elif kind == "initializer":
                initializer_entries[registry_id] = entry
            else:
                errors.append(f"{entry_id}: unknown registry kind {kind!r}")

        for key in ("source_state_kind", "terminal_first_branch", "nonterminal_target_schema", "owner"):
            if not isinstance(entry.get(key), str) or not entry[key]:
                errors.append(f"{entry_id}: required field {key} is missing")
        source_families = entry.get("source_family_ids")
        if not isinstance(source_families, list) or not source_families:
            errors.append(f"{entry_id}: source_family_ids must be nonempty")

        serializer = entry.get("serializer")
        if not isinstance(serializer, dict):
            errors.append(f"{entry_id}: serializer must be an object")
        else:
            for required in ("receipt_builder", "admission_serializer", "enqueue_gate"):
                if not isinstance(serializer.get(required), str) or not serializer[required]:
                    errors.append(f"{entry_id}: serializer.{required} is missing")
            if queue_discovered:
                if serializer.get("enqueue_gate") == "UNASSIGNED":
                    warnings.append(f"{entry_id}: queue API exists but this entry has no enqueue gate")
            elif serializer.get("enqueue_gate") != "UNASSIGNED":
                errors.append(f"{entry_id}: claims enqueue gate although no active queue mutation API was found")

        persistent = entry.get("persistent_queue")
        if not isinstance(persistent, dict) or not isinstance(
            persistent.get("observed_enqueue_call"), bool
        ):
            errors.append(f"{entry_id}: persistent_queue observation is malformed")
        elif persistent.get("observed_enqueue_call") and not queue_discovered:
            errors.append(f"{entry_id}: observed_enqueue_call=true without a queue API signal")

        t2_t3 = entry.get("t2_t3_coverage")
        if not isinstance(t2_t3, dict) or not all(
            isinstance(t2_t3.get(name), str) and t2_t3[name]
            for name in ("T2", "T3")
        ):
            errors.append(f"{entry_id}: T2/T3 coverage is incomplete")

        evidence = entry.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{entry_id}: evidence must be nonempty")
        else:
            for reference in evidence:
                if not isinstance(reference, str) or not _validate_evidence_path(root, reference):
                    errors.append(f"{entry_id}: invalid or archive-only evidence {reference!r}")

    frontier_edges = {
        str(item.get("id")): item
        for item in _as_object_list(
            frontier.get("registered_edges"), name="frontier.registered_edges", errors=errors
        )
    }
    ledger_edges = {
        str(item.get("id")): item
        for item in _as_object_list(
            ledger.get("concrete_edge_families"),
            name="ledger.concrete_edge_families",
            errors=errors,
        )
    }
    registry_ids = set(registered_entries)
    for name, values in (("frontier", set(frontier_edges)), ("ledger", set(ledger_edges))):
        missing = sorted(values - registry_ids)
        extra = sorted(registry_ids - values)
        if missing:
            errors.append(f"REGISTRY_MISSING_IN_INVENTORY[{name}]: {missing}")
        if extra:
            errors.append(f"INVENTORY_EDGE_NOT_IN_REGISTRY[{name}]: {extra}")
    if set(frontier_edges) != set(ledger_edges):
        errors.append("frontier and ledger registered edge id sets differ")

    family_owners = frontier.get("family_frontier_ownership")
    if not isinstance(family_owners, dict):
        errors.append("frontier family_frontier_ownership is missing")
        family_owners = {}
    for registry_id in sorted(set(frontier_edges) & set(ledger_edges) & registry_ids):
        entry = registered_entries[registry_id]
        entry_id = str(entry.get("id"))
        frontier_edge = frontier_edges[registry_id]
        ledger_edge = ledger_edges[registry_id]
        for field in ("source_family_ids", "target_family_ids", "guard_class"):
            if frontier_edge.get(field) != ledger_edge.get(field):
                errors.append(f"{registry_id}: frontier/ledger disagree on {field}")
        if entry.get("source_family_ids") != frontier_edge.get("source_family_ids"):
            errors.append(f"{entry_id}: source families differ from active registry")
        correspondence = entry.get("registry_correspondence", {})
        if correspondence.get("guard_class") != frontier_edge.get("guard_class"):
            errors.append(f"{entry_id}: guard class differs from active registry")
        expected_owners = {
            family_owners.get(family)
            for family in frontier_edge.get("source_family_ids", [])
        }
        expected_owners.discard(None)
        if len(expected_owners) == 1 and entry.get("owner") not in expected_owners:
            errors.append(f"{entry_id}: owner differs from source-family owner")
        if "t2_v1_atomic_pending_target" in frontier_edge.get("target_family_ids", []):
            t2_value = entry.get("t2_t3_coverage", {}).get("T2")
            if not isinstance(t2_value, str) or not t2_value.startswith("T2v1_"):
                errors.append(f"{entry_id}: atomic target lacks T2v1 coverage")
        if "generic_nontrivial_marked_state" in frontier_edge.get("target_family_ids", []):
            t3_value = entry.get("t2_t3_coverage", {}).get("T3")
            if t3_value in {None, "UNASSIGNED", "T3v1_CURRENT_GRAPH"}:
                errors.append(f"{entry_id}: nontrivial marked target lacks a T3 extension")

    initialization = ledger.get("initialization")
    initializer_id = initialization.get("serializer_id") if isinstance(initialization, dict) else None
    if not isinstance(initializer_id, str):
        errors.append("ledger initialization.serializer_id is missing")
    elif set(initializer_entries) != {initializer_id}:
        errors.append(
            f"initializer inventory differs from ledger: inventory={sorted(initializer_entries)}, ledger={[initializer_id]}"
        )
    elif initializer_entries[initializer_id].get("owner") != family_owners.get("initial_core_root"):
        errors.append("initializer owner differs from active family owner")

    recorded_signal_rows = _as_object_list(
        inventory.get("source_signal_anchors"),
        name="source_signal_anchors",
        errors=errors,
    )
    recorded_signals = [str(row.get("anchor", "")) for row in recorded_signal_rows]
    if "" in recorded_signals:
        errors.append("every source signal requires a nonempty anchor")
    for duplicate in sorted(_duplicates(recorded_signals)):
        errors.append(f"duplicate source signal anchor: {duplicate}")
    missing_signals = sorted(set(discovered) - set(recorded_signals))
    stale_signals = sorted(set(recorded_signals) - set(discovered))
    if missing_signals:
        errors.append(f"SOURCE_SIGNAL_UNINVENTORIED: {missing_signals}")
    if stale_signals:
        errors.append(f"INVENTORY_SIGNAL_NOT_IN_SOURCE: {stale_signals}")

    known_mapping_ids = {*registry_ids, *initializer_entries}
    unresolved_signal_count = 0
    for row in recorded_signal_rows:
        anchor = row.get("anchor")
        disposition = row.get("disposition")
        mapping = row.get("maps_to")
        if not isinstance(disposition, str) or not disposition:
            errors.append(f"{anchor}: missing signal disposition")
            continue
        if disposition in REGISTERED_DISPOSITIONS:
            if mapping not in known_mapping_ids:
                errors.append(f"{anchor}: registered disposition maps to unknown id {mapping!r}")
        else:
            unresolved_signal_count += 1
            if mapping != "UNASSIGNED":
                errors.append(f"{anchor}: unresolved disposition must map to UNASSIGNED")

    unknown_items = _as_object_list(
        inventory.get("unknown_items"), name="unknown_items", errors=errors
    )
    unknown_ids = [str(item.get("id", "")) for item in unknown_items]
    if "" in unknown_ids:
        errors.append("every unknown item requires a stable id")
    for duplicate in sorted(_duplicates(unknown_ids)):
        errors.append(f"duplicate unknown item id: {duplicate}")
    open_unknowns = [item for item in unknown_items if item.get("status") == "OPEN"]
    if unresolved_signal_count and not any(
        item.get("kind") == "SOURCE_DRIFT" for item in open_unknowns
    ):
        errors.append("unresolved source signals lack an OPEN SOURCE_DRIFT item")

    kernel_scope = kernel.get("scope")
    if not isinstance(kernel_scope, dict):
        errors.append("kernel scope is missing")
    elif kernel_scope.get("semantic_reachable_state_exhaustion") is not False:
        errors.append("kernel must not claim semantic reachable-state exhaustion")

    runtime = inventory.get("runtime_surface")
    if not isinstance(runtime, dict):
        errors.append("runtime_surface must be an object")
        runtime = {}
    runtime_assigned = all(
        runtime.get(key) not in {None, "UNASSIGNED"}
        for key in (
            "selector_runtime",
            "canonical_reentry_extractor",
            "persistent_queue_implementation",
            "global_enqueue_gate",
            "constructor_registration_marker",
        )
    )
    queue_anchors = runtime.get("queue_api_anchors", [])
    if not isinstance(queue_anchors, list) or not all(
        isinstance(item, str) and item for item in queue_anchors
    ):
        errors.append("runtime_surface.queue_api_anchors must be a string list")
        queue_anchors = []
    missing_queue_anchors = sorted(set(queue_discovered) - set(queue_anchors))
    stale_queue_anchors = sorted(set(queue_anchors) - set(queue_discovered))
    if missing_queue_anchors:
        errors.append(f"QUEUE_API_UNINVENTORIED: {missing_queue_anchors}")
    if stale_queue_anchors:
        errors.append(f"INVENTORY_QUEUE_API_NOT_IN_SOURCE: {stale_queue_anchors}")

    local_protocols = runtime.get("local_protocols", [])
    if not isinstance(local_protocols, list):
        errors.append("runtime_surface.local_protocols must be a list")
        local_protocols = []
    local_protocol_ids: set[str] = set()
    for index, protocol in enumerate(local_protocols):
        if not isinstance(protocol, dict):
            errors.append(f"runtime_surface.local_protocols[{index}] must be an object")
            continue
        protocol_id = protocol.get("id")
        if not isinstance(protocol_id, str) or not protocol_id:
            errors.append(f"runtime_surface.local_protocols[{index}].id is missing")
            continue
        if protocol_id in local_protocol_ids:
            errors.append(f"duplicate local runtime protocol id: {protocol_id}")
        local_protocol_ids.add(protocol_id)
        for field in (
            "status",
            "implementation",
            "state_admission",
            "queue_mutation_anchor",
            "registration_protocol",
            "global_coverage",
        ):
            if field not in protocol:
                errors.append(f"local runtime protocol {protocol_id} missing {field}")
        anchor = protocol.get("queue_mutation_anchor")
        if isinstance(anchor, str) and anchor not in queue_anchors:
            errors.append(
                f"local runtime protocol {protocol_id} uses unregistered queue anchor"
            )

    all_entry_gates_assigned = all(
        isinstance(entry.get("serializer"), dict)
        and entry["serializer"].get("admission_serializer") != "UNASSIGNED"
        and entry["serializer"].get("enqueue_gate") != "UNASSIGNED"
        for entry in entries
    )
    closure_ready = bool(
        not errors
        and not open_unknowns
        and unresolved_signal_count == 0
        and runtime_assigned
        and all_entry_gates_assigned
        and queue_discovered
    )
    assessment = inventory.get("closure_assessment")
    if not isinstance(assessment, dict):
        errors.append("closure_assessment must be an object")
    else:
        if assessment.get("unknown_item_count") != len(unknown_items):
            errors.append("closure_assessment.unknown_item_count is stale")
        if assessment.get("F1_reachable_state_exhaustion") != "OPEN" and not closure_ready:
            errors.append("inventory upgrades F1 despite unresolved constructor surface")
        if assessment.get("T6_global_selector_totality") != "OPEN":
            errors.append("A0 inventory must not upgrade T6")

    if open_unknowns:
        warnings.append(f"F1 remains OPEN: {len(open_unknowns)} explicit unknown items")
    if unresolved_signal_count:
        warnings.append(
            f"F1 remains OPEN: {unresolved_signal_count} source signals are not registered constructors"
        )
    if not queue_discovered:
        warnings.append("F1 remains OPEN: no concrete enqueue/queue mutation API was found")
    elif not runtime_assigned:
        warnings.append(
            "F1 remains OPEN: local queue runtime exists, but global constructor "
            "routing/reentry coverage is unproved"
        )
    if not runtime_assigned:
        warnings.append("F1 remains OPEN: selector runtime/extractor/queue contracts are unassigned")

    return AuditResult(
        tuple(errors),
        tuple(dict.fromkeys(warnings)),
        tuple(discovered),
        tuple(queue_discovered),
        closure_ready,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--inventory", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="emit a machine-readable report")
    parser.add_argument(
        "--require-closure-ready",
        action="store_true",
        help="also fail when the honest inventory still exposes F1 gaps",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    result = audit_inventory(root, args.inventory)
    if args.json:
        print(json.dumps(result.payload(), ensure_ascii=True, indent=2, sort_keys=True))
    else:
        status = "PASS" if result.ok else "FAIL"
        print(f"T6 constructor inventory structural audit: {status}")
        print(f"closure_ready={str(result.closure_ready).lower()}")
        print(f"source_signals={len(result.source_signals)}")
        print(f"queue_api_signals={len(result.queue_api_signals)}")
        for error in result.errors:
            print(f"ERROR: {error}")
        for warning in result.warnings:
            print(f"WARNING: {warning}")
    if not result.ok:
        return 1
    if args.require_closure_ready and not result.closure_ready:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
