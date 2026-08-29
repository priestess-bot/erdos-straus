#!/usr/bin/env python3
"""Verify all files listed in MANIFEST.sha256."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
manifest = root / "MANIFEST.sha256"
failed = False
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    digest, relative = line.split("  ", 1)
    path = root / relative
    actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
    status = "OK" if actual == digest else "FAIL"
    print(f"{status}  {relative}")
    failed |= status != "OK"
raise SystemExit(1 if failed else 0)
