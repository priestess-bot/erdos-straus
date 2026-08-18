#!/usr/bin/env python3
"""Verify the T6 obligation ledger without treating it as a closure proof.

The ledger records exactly which current edge claims have complete E1--E5
receipts under their written guards, and separates that from unresolved
universal selector obligations.  Passing this program therefore confirms the
inventory's internal consistency; it cannot establish T6 totality.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "data" / "t6-selector-obligation-ledger-v1.json"
TAXONOMY_PATH = ROOT / "data" / "t5-full-transition-taxonomy-v2.json"

CLAIM_STATUSES = {"established", "computationally_reproduced"}
RECEIPT_COMPONENT = "established_under_written_claim_guard"
FAMILY_COVERAGE = {
    "CLOSED_BY_EMPTY_PROOF",
    "CLOSED_BY_UNIVERSAL_SUCCESSOR",
    "TERMINAL",
    "LOCAL_EDGE_ONLY",
    "RELATIVE_EDGE_ONLY",
    "OPEN",
    "UNREACHABLE_IN_CURRENT_NAMED_GRAPH",
}
ALLOWED_GAP_CLOSURES = {
    "family_empty_proof",
    "universal_terminal",
    "universal_verified_successor",
}
REQUIRED_GAP_IDS = {
    "GAP-O1-INITIAL-ROOT",
    "GAP-O1-GLOBAL-EXHAUSTION",
    "GAP-O1-H4-OTHER-BRANCHES",
    "GAP-O1-POST-G-TYPE-I",
    "GAP-O1-A-GT-ONE-OVERFLOW",
    "GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY",
    "GAP-O1-ATOMIC-TARGET-CLOSURE",
    "GAP-O2-PROPER-ROOT-K-GT-ONE",
    "GAP-O3-C8-OUTGOING",
    "GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY",
}
REQUIRED_OBLIGATION_IDS = {
    "O1-INITIAL-ROOT",
    "O1-GLOBAL-EXHAUSTION",
    "O1-H4-OTHER-BRANCHES",
    "O1-POST-G-TYPE-I",
    "O1-A-GT-ONE-OVERFLOW",
    "O1-HIGH-SUPPORT-ROOT-CAPACITY",
    "O1-ATOMIC-TARGET-CLOSURE",
    "O2-PROPER-ROOT-PHYSICALIZATION",
    "O3-C8-OUTGOING",
    "O4-NEW-ATOMIC-OR-MARKED-FAMILY",
}


def read_json(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def claim_status(claim_id: str) -> str:
    path = ROOT / "claims" / f"{claim_id}.md"
    if not path.is_file():
        raise AssertionError(f"missing claim card: {claim_id}")
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"^claim_status:\s*([^\n]+)$", text, flags=re.MULTILINE
    )
    if match is None:
        raise AssertionError(f"claim status missing: {claim_id}")
    return match.group(1).strip(" '\"")


def require_unique(rows: list[dict[str, object]], key: str, label: str) -> set[str]:
    values = [str(row[key]) for row in rows]
    if len(values) != len(set(values)):
        raise AssertionError(f"duplicate {label}")
    return set(values)


def run_ledger() -> dict[str, object]:
    ledger = read_json(LEDGER_PATH)
    taxonomy = read_json(TAXONOMY_PATH)

    if ledger["ledger_id"] != "t6_global_selector_obligation_ledger_v1":
        raise AssertionError("unexpected T6 ledger identifier")
    current_status = ledger["current_status"]
    if not isinstance(current_status, dict):
        raise AssertionError("ledger current status must be an object")
    if current_status["t6_global_selector_totality"] != "OPEN":
        raise AssertionError("a ledger with open acceptance gates cannot claim T6")

    scope = ledger["scope"]
    if not isinstance(scope, dict):
        raise AssertionError("ledger scope must be an object")
    if set(scope["closure_modes"]) != ALLOWED_GAP_CLOSURES:
        raise AssertionError("selector closure modes changed")

    initialization = ledger["initialization"]
    if not isinstance(initialization, dict):
        raise AssertionError("initialization row must be an object")
    if initialization["family_id"] != "initial_core_root":
        raise AssertionError("initial root family cannot be omitted")
    if initialization["coverage_status"] != "OPEN":
        raise AssertionError("initial serializer was promoted without its total proof")

    families = ledger["state_families"]
    if not isinstance(families, list):
        raise AssertionError("state families must be a list")
    family_ids = require_unique(families, "id", "state-family id")
    if "initial_core_root" not in family_ids or "direct_terminal_leaf" not in family_ids:
        raise AssertionError("state-family boundary lost root or terminal")
    for row in families:
        if row["coverage_status"] not in FAMILY_COVERAGE:
            raise AssertionError(f"unknown family coverage: {row['id']}")
        if not row["guard"] or not row["terminal_exit"] or not row["successor_exit"]:
            raise AssertionError(f"family lacks a selector boundary: {row['id']}")
        if not isinstance(row["minimal_gap_ids"], list):
            raise AssertionError(f"family gap list malformed: {row['id']}")

    taxonomy_rows = taxonomy["current_verified_edge_families"]
    generic_reference = ledger["taxonomy_cross_check"]["generic_contract_reference"]
    taxonomy_references = {str(row["reference"]) for row in taxonomy_rows}
    expected_claim_references = taxonomy_references - {str(generic_reference)}

    edge_rows = ledger["concrete_edge_families"]
    if not isinstance(edge_rows, list):
        raise AssertionError("concrete edge families must be a list")
    require_unique(edge_rows, "id", "edge-family id")
    ledger_claim_references = {str(row["claim_reference"]) for row in edge_rows}
    if ledger_claim_references != expected_claim_references:
        missing = sorted(expected_claim_references - ledger_claim_references)
        extra = sorted(ledger_claim_references - expected_claim_references)
        raise AssertionError(f"edge ledger drifted from T5 taxonomy: missing={missing}, extra={extra}")

    for row in edge_rows:
        source_ids = set(row["source_family_ids"])
        target_ids = set(row["target_family_ids"])
        if not source_ids or not target_ids:
            raise AssertionError(f"edge has no source or target family: {row['id']}")
        if not source_ids <= family_ids or not target_ids <= family_ids:
            raise AssertionError(f"edge names an unknown state family: {row['id']}")
        if row["guard_class"] not in set(ledger["status_vocabulary"]["controls"]):
            raise AssertionError(f"edge has invalid control class: {row['id']}")
        receipt = row["receipt"]
        if not isinstance(receipt, dict):
            raise AssertionError(f"edge receipt malformed: {row['id']}")
        for component in ("E1", "E2", "E3", "E4"):
            if receipt.get(component) != RECEIPT_COMPONENT:
                raise AssertionError(f"{row['id']} lost guarded {component}")
        if not receipt.get("E5_ticket"):
            raise AssertionError(f"{row['id']} lost its T5 ticket")
        if claim_status(str(row["claim_reference"])) not in CLAIM_STATUSES:
            raise AssertionError(f"unaccepted claim status: {row['claim_reference']}")
        if not (ROOT / str(row["verifier"])).is_file():
            raise AssertionError(f"missing focused verifier: {row['verifier']}")

    obligations = ledger["obligations"]
    if not isinstance(obligations, list):
        raise AssertionError("obligations must be a list")
    obligation_ids = require_unique(obligations, "id", "obligation id")
    if obligation_ids != REQUIRED_OBLIGATION_IDS:
        missing = sorted(REQUIRED_OBLIGATION_IDS - obligation_ids)
        extra = sorted(obligation_ids - REQUIRED_OBLIGATION_IDS)
        raise AssertionError(f"obligation surface changed: missing={missing}, extra={extra}")
    for row in obligations:
        if row["status"] != "OPEN":
            raise AssertionError(f"open obligation incorrectly promoted: {row['id']}")
        if not set(row["family_ids"]) <= family_ids:
            raise AssertionError(f"obligation names unknown family: {row['id']}")

    gaps = ledger["minimal_selector_gaps"]
    if not isinstance(gaps, list):
        raise AssertionError("minimal gaps must be a list")
    gap_ids = require_unique(gaps, "id", "minimal-gap id")
    if gap_ids != REQUIRED_GAP_IDS:
        missing = sorted(REQUIRED_GAP_IDS - gap_ids)
        extra = sorted(gap_ids - REQUIRED_GAP_IDS)
        raise AssertionError(f"minimal-gap surface changed: missing={missing}, extra={extra}")
    gap_families: set[str] = set()
    for row in gaps:
        if row["status"] != "OPEN":
            raise AssertionError(f"minimal selector gap incorrectly closed: {row['id']}")
        if set(row["allowed_closure_modes"]) != ALLOWED_GAP_CLOSURES:
            raise AssertionError(f"minimal gap has an invalid closure rule: {row['id']}")
        if not set(row["family_ids"]) <= family_ids:
            raise AssertionError(f"minimal gap names unknown family: {row['id']}")
        gap_families.update(row["family_ids"])
    open_family_ids = {
        str(row["id"])
        for row in families
        if row["coverage_status"] == "OPEN"
    }
    if not open_family_ids <= gap_families:
        raise AssertionError("an open state family has no minimal selector gap")

    gates = ledger["acceptance_gates"]
    if not isinstance(gates, list):
        raise AssertionError("acceptance gates must be a list")
    require_unique(gates, "id", "acceptance-gate id")
    if not any(row["status"] != "ESTABLISHED" for row in gates):
        raise AssertionError("all gates established but T6 remains OPEN")

    current_atomic = set(ledger["taxonomy_cross_check"]["current_atomic_claim_references"])
    taxonomy_atomic = {
        str(row["reference"])
        for row in taxonomy_rows
        if str(row["family"]).startswith("T2 ")
    }
    if current_atomic != taxonomy_atomic:
        raise AssertionError("current named atomic surface drifted")

    return {
        "ledger_id": ledger["ledger_id"],
        "t6_global_selector_totality": current_status["t6_global_selector_totality"],
        "concrete_edge_family_count": len(edge_rows),
        "state_family_count": len(families),
        "open_state_family_ids": sorted(open_family_ids),
        "minimal_selector_gap_ids": sorted(gap_ids),
        "acceptance_gate_count": len(gates),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run_ledger()
    if args.verify:
        print("T6 selector obligation ledger verification passed; T6 remains OPEN")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
