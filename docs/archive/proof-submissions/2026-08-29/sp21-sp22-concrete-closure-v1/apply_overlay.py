#!/usr/bin/env python3
"""Apply and optionally verify the SP-21/SP-22 closure overlay."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import NoReturn

BASE_HEAD = "e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4"
PACKAGE_ROOT = Path(__file__).resolve().parent
OVERLAY = PACKAGE_ROOT / "repo-overlay"
PATCH_SPEC = OVERLAY / "patches/sp21-sp22-root-readme-v1.json"


def fail(message: str) -> NoReturn:
    raise SystemExit(f"apply_overlay: {message}")


def run(command: list[str], *, cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def current_head(repo: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def patch_root_readme(repo: Path) -> None:
    spec = json.loads(PATCH_SPEC.read_text(encoding="utf-8"))
    if spec["base_head_sha"] != BASE_HEAD or spec["target"] != "README.md":
        fail("invalid root README patch specification")
    path = repo / spec["target"]
    if not path.is_file():
        fail(f"missing {path}")
    text = path.read_text(encoding="utf-8")
    for index, row in enumerate(spec["replacements"]):
        old = row["old"]
        new = row["new"]
        old_count = text.count(old)
        new_count = text.count(new)
        if old_count == 1:
            text = text.replace(old, new, 1)
        elif old_count == 0 and new_count == 1:
            # Idempotent re-application.
            continue
        else:
            fail(
                f"README replacement {index} expected one old block or one already-applied new block; "
                f"found old={old_count}, new={new_count}"
            )
    path.write_text(text, encoding="utf-8")


def copy_overlay(repo: Path) -> int:
    copied = 0
    for source in sorted(OVERLAY.rglob("*")):
        if not source.is_file() or "__pycache__" in source.parts:
            continue
        relative = source.relative_to(OVERLAY)
        destination = repo / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied += 1
    return copied


def verify(repo: Path) -> None:
    reproduction = repo / "reproductions/sp21_q1_p21169_concrete_selector_v1"
    run(
        [
            sys.executable,
            "scripts/t6_sp21_q1_p21169_concrete_selector_v1.py",
            "--repo-root",
            ".",
            "--output",
            str(reproduction.relative_to(repo) / "evidence-v1.json"),
        ],
        cwd=repo,
    )
    run(
        [
            sys.executable,
            "scripts/t6_sp21_q1_p21169_independent_replayer_v1.py",
            "--repo-root",
            ".",
            "--evidence",
            str(reproduction.relative_to(repo) / "evidence-v1.json"),
            "--output",
            str(reproduction.relative_to(repo) / "independent-replay-v1.json"),
        ],
        cwd=repo,
    )
    run(
        [
            sys.executable,
            "-m",
            "unittest",
            "tests.test_t6_sp21_q1_p21169_concrete_selector_v1",
            "-v",
        ],
        cwd=repo,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path, help="local erdos-straus checkout")
    parser.add_argument(
        "--allow-head-mismatch",
        action="store_true",
        help="apply outside the signed base commit; authority verification will normally fail",
    )
    parser.add_argument("--no-verify", action="store_true")
    args = parser.parse_args()
    repo = args.repository.resolve()
    if not repo.is_dir():
        fail(f"not a directory: {repo}")
    head = current_head(repo)
    if not args.allow_head_mismatch:
        if head is None:
            fail("target is not a readable Git checkout; use --allow-head-mismatch only for inspection")
        if head != BASE_HEAD:
            fail(f"expected HEAD {BASE_HEAD}, got {head}")
    copied = copy_overlay(repo)
    patch_root_readme(repo)
    if not args.no_verify:
        verify(repo)
    print(
        json.dumps(
            {
                "base_head": head,
                "copied_files": copied,
                "root_readme_patched": True,
                "verification_run": not args.no_verify,
                "overlay_sha256": hashlib.sha256(
                    b"".join(
                        path.relative_to(OVERLAY).as_posix().encode("utf-8")
                        + b"\0"
                        + path.read_bytes()
                        for path in sorted(OVERLAY.rglob("*"))
                        if path.is_file() and "__pycache__" not in path.parts
                    )
                ).hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
