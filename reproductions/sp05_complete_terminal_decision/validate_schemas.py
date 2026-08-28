#!/usr/bin/env python3
"""Validate the standalone SP-05 evidence against closed JSON schemas."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(instance, schema_path: Path) -> None:
    schema = load(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(instance)


def main() -> None:
    terminal_schema = ROOT / "schemas" / "sp05-complete-terminal-decision-v1.schema.json"
    status_schema = ROOT / "schemas" / "sp05-status-boundary-v1.schema.json"
    replay = load(ROOT / "evidence" / "p21169-terminal-replay.json")
    validate(replay["source_terminal_decision"], terminal_schema)
    validate(replay["target_terminal_decision"], terminal_schema)
    validate(load(ROOT / "evidence" / "status-boundary.json"), status_schema)
    print("schema validation passed")


if __name__ == "__main__":
    main()
