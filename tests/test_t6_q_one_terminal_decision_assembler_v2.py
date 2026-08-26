from __future__ import annotations

import ast
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ASSEMBLER_PATH = "scripts/t6_q_one_terminal_decision_assembler_v2.py"
ROOT_ENVELOPE_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v2.json"
REGISTRY_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v2.schema.json"
REGISTRY_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
SCHEDULER_PATH = "scripts/t6_q_one_priority_prefix_scheduler_v1.py"
COVERAGE_PATH = "scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py"

FIXTURE_PATHS = (
    ASSEMBLER_PATH,
    ROOT_ENVELOPE_PATH,
    REGISTRY_PATH,
    REGISTRY_SCHEMA_PATH,
    REGISTRY_RESOLVER_PATH,
    SCHEDULER_PATH,
    COVERAGE_PATH,
)


def raw_q_one_g(prime: int, factors: list[list[int]]) -> dict[str, object]:
    return {
        "schema_id": "q1_root_initializer_raw_v2",
        "schema_version": 2,
        "root_context": prime,
        "equation_rank": prime,
        "equation_numerator": 4,
        "equation_denominator": prime,
        "q": 1,
        "gap_three_x": (prime + 3) // 4,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "mark_root_context": prime,
        "mark_equation_rank": prime,
        "gap_three_factorization": factors,
    }


RAW_73 = raw_q_one_g(73, [[19, 1]])
RAW_193 = raw_q_one_g(193, [[7, 2]])
RAW_1201 = raw_q_one_g(1_201, [[7, 1], [43, 1]])
RAW_2521 = raw_q_one_g(2_521, [[631, 1]])


def run_git(root: Path, *args: str) -> str:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    return completed.stdout.strip()


class RepositoryFixture:
    def __init__(self, base: Path):
        self.base = base
        self.counter = 0

    def commit(
        self,
        *,
        overrides: dict[str, bytes] | None = None,
    ) -> tuple[Path, str]:
        self.counter += 1
        root = self.base / f"repo-{self.counter}"
        root.mkdir()
        overrides = overrides or {}
        for path in FIXTURE_PATHS:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(overrides.get(path, (ROOT / path).read_bytes()))
        run_git(root, "init", "-q")
        run_git(root, "add", ".")
        run_git(
            root,
            "-c",
            "user.name=Assembler Test",
            "-c",
            "user.email=assembler@example.invalid",
            "commit",
            "-q",
            "-m",
            "fixture",
        )
        return root, run_git(root, "rev-parse", "HEAD")

    @staticmethod
    def commit_current(root: Path, message: str) -> str:
        run_git(root, "add", ".")
        run_git(
            root,
            "-c",
            "user.name=Assembler Test",
            "-c",
            "user.email=assembler@example.invalid",
            "commit",
            "-q",
            "-m",
            message,
        )
        return run_git(root, "rev-parse", "HEAD")


SUBPROCESS_DRIVER = r"""
import json
from dataclasses import fields
from pathlib import Path
import sys

root = Path(sys.argv[1])
head = sys.argv[2]
action = sys.argv[3]
marker = root / "side-effect-marker.txt"
sys.path.insert(0, str(root / "scripts"))

stale_specs = {
    "stale_scheduler": (
        "t6_q_one_priority_prefix_scheduler_v1.py",
        b"    fields = frozenset(value)\n",
    ),
    "stale_coverage": (
        "t6_q_one_priority_prefix_coverage_verifier_v1.py",
        b"    domain = _require_exact_dict(value, _DOMAIN_FIELDS, \"raw_domain\")\n",
    ),
    "stale_root_envelope": (
        "t6_q_one_root_initializer_envelope_v2.py",
        b"    raw = _require_exact_mapping(value, RAW_FIELDS, \"raw q=1 G source\")\n",
    ),
}
stale_path = None
stale_bytes = None
if action in stale_specs:
    filename, needle = stale_specs[action]
    stale_path = root / "scripts" / filename
    stale_bytes = stale_path.read_bytes()
    replacement = (
        f"    __import__('pathlib').Path({str(marker)!r}).write_text('executed', encoding='utf-8'); "
    ).encode("utf-8") + needle.lstrip()
    if needle not in stale_bytes:
        raise RuntimeError(f"injection point changed for {filename}")
    stale_path.write_bytes(stale_bytes.replace(needle, replacement, 1))
import t6_q_one_terminal_decision_assembler_v2 as assembler
if stale_bytes is not None:
    stale_path.write_bytes(stale_bytes)

raw = json.loads(sys.stdin.read())
try:
    if action == "scheduler_swap":
        import t6_q_one_priority_prefix_scheduler_v1 as canonical_scheduler
        original = canonical_scheduler.replay_q_one_priority_prefix_v1
        def replacement(value):
            marker.write_text("executed", encoding="utf-8")
            return original(value)
        replacement.__name__ = original.__name__
        replacement.__module__ = original.__module__
        canonical_scheduler.replay_q_one_priority_prefix_v1 = replacement
    elif action == "resolver_self_restore":
        import t6_coordinator_role_registry_v2 as canonical_registry
        original = canonical_registry.resolve_registry_v2
        def replacement(*args, **kwargs):
            marker.write_text("executed", encoding="utf-8")
            canonical_registry.resolve_registry_v2 = original
            return original(*args, **kwargs)
        replacement.__name__ = original.__name__
        replacement.__module__ = original.__module__
        canonical_registry.resolve_registry_v2 = replacement
    elif action == "state_swap":
        import t6_q_one_root_initializer_envelope_v2 as canonical_root
        original = canonical_root.make_raw_root_source_state_v2
        def replacement(body, anchor):
            marker.write_text("executed", encoding="utf-8")
            return original(body, anchor)
        replacement.__name__ = original.__name__
        replacement.__module__ = original.__module__
        canonical_root.make_raw_root_source_state_v2 = replacement
    elif action == "module_swap":
        import t6_q_one_priority_prefix_coverage_verifier_v1 as canonical_coverage
        import t6_q_one_priority_prefix_scheduler_v1 as canonical_scheduler
        canonical_coverage.__file__ = canonical_scheduler.__file__

    decision = assembler.assemble_q_one_terminal_decision_v2(
        root=root,
        requested_head=head,
        raw_q_one_g=raw,
    )
    if action == "forge_authority":
        cls = type(decision)
        provisional = object.__new__(cls)
        for field in fields(cls):
            value = True if field.name == "issuer_authority" else getattr(decision, field.name)
            object.__setattr__(provisional, field.name, value)
        values = {field.name: getattr(provisional, field.name) for field in fields(cls)}
        digest = assembler.canonical_digest_v2(
            assembler._unsigned_decision_mapping_v2(cls, values)
        )
        object.__setattr__(provisional, "decision_id", cls.ID_PREFIX + digest)
        object.__setattr__(provisional, "digest", digest)
        assembler.terminal_decision_to_mapping_v2(provisional)
    mapping = assembler.terminal_decision_to_mapping_v2(decision)
    print(json.dumps({"ok": True, "mapping": mapping, "marker": marker.exists()}, sort_keys=True))
except assembler.TerminalDecisionAssemblerError as exc:
    print(json.dumps({"ok": False, "code": exc.code.value, "detail": exc.detail, "marker": marker.exists()}, sort_keys=True))
"""


def run_assembler(
    root: Path,
    head: str,
    raw: dict[str, object],
    *,
    action: str = "normal",
) -> dict[str, object]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, "-c", SUBPROCESS_DRIVER, str(root), head, action],
        cwd=root,
        input=json.dumps(raw),
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    return json.loads(completed.stdout)


class QOneTerminalDecisionAssemblerV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-terminal-assembler-v2-")
        self.fixture = RepositoryFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def assert_error(
        self,
        result: dict[str, object],
        code: str,
    ) -> None:
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["code"], code)

    def test_exact_head_hit_and_miss_controls_are_non_authorizing(self):
        root, head = self.fixture.commit()
        for raw, outcome, artifact_type in (
            (RAW_73, "ROOT_TERMINAL_HIT_EVIDENCE", "QOneRootTerminalHitEvidenceV2"),
            (RAW_193, "ROOT_TERMINAL_HIT_EVIDENCE", "QOneRootTerminalHitEvidenceV2"),
            (RAW_1201, "PREFIX_MISS_EVIDENCE", "QOneRegisteredPrefixMissEvidenceV2"),
            (RAW_2521, "PREFIX_MISS_EVIDENCE", "QOneRegisteredPrefixMissEvidenceV2"),
        ):
            with self.subTest(prime=raw["root_context"]):
                result = run_assembler(root, head, raw)
                self.assertTrue(result["ok"], result)
                mapping = result["mapping"]
                self.assertEqual(mapping["artifact_type"], artifact_type)
                self.assertEqual(mapping["outcome"], outcome)
                self.assertEqual(mapping["head_sha"], head)
                self.assertEqual(mapping["subject_kind"], "SOURCE_STATE")
                self.assertFalse(mapping["global_exhaustion"])
                self.assertEqual(mapping["next_unchecked_gap"], 15)
                self.assertEqual(len(mapping["scan_digests"]), 3)
                for name in (
                    "source_actualness",
                    "initializer_authority",
                    "issuer_authority",
                    "terminal_authority",
                    "e1_authority",
                    "queue_authority",
                    "producer_continuation_allowed",
                ):
                    self.assertFalse(mapping[name])
                self.assertNotEqual(mapping["decision_id"], mapping["state_id"])
                if raw["root_context"] == 193:
                    self.assertEqual(
                        (
                            mapping["selected_certificate"]["certificate_type"],
                            mapping["selected_certificate"]["gap"],
                            mapping["selected_certificate"]["divisor"],
                        ),
                        ("TYPE_I", 7, 10),
                    )

    def test_api_exposes_no_caller_domain_callable_or_authority(self):
        source = (ROOT / ASSEMBLER_PATH).read_text(encoding="utf-8")
        tree = ast.parse(source)
        function = next(
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "assemble_q_one_terminal_decision_v2"
        )
        self.assertEqual(function.args.args, [])
        self.assertIsNone(function.args.vararg)
        self.assertEqual(
            tuple(argument.arg for argument in function.args.kwonlyargs),
            ("root", "requested_head", "raw_q_one_g"),
        )
        self.assertIsNone(function.args.kwarg)
        imported_modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_modules.add(node.module)
        self.assertTrue(
            all(not name.startswith("t6_") for name in imported_modules),
            imported_modules,
        )
        for forbidden in (
            "issue_production_terminal_receipt_v2",
            "enqueue_v2",
            "authorize_e1_v2",
            "register_producer_v2",
        ):
            self.assertNotIn(forbidden, source)

    def test_caller_authority_legacy_state_and_domain_injections_are_rejected(self):
        root, head = self.fixture.commit()
        for field, value in (
            ("issuer_authority", True),
            ("queue_authority", True),
            ("scheduler_domain", {"q": 1}),
            ("terminal_first", {"outcome": "MISS"}),
            ("state_id", "legacy"),
            ("source_receipt", {"E1": True}),
        ):
            raw = copy.deepcopy(RAW_1201)
            raw[field] = value
            with self.subTest(field=field):
                self.assert_error(
                    run_assembler(root, head, raw),
                    "DOMAIN_ERROR",
                )

    def test_canonical_and_stale_dependency_swaps_cannot_affect_fresh_execution(self):
        for action in (
            "scheduler_swap",
            "state_swap",
            "module_swap",
            "resolver_self_restore",
            "stale_scheduler",
            "stale_coverage",
            "stale_root_envelope",
        ):
            root, head = self.fixture.commit()
            with self.subTest(action=action):
                result = run_assembler(root, head, RAW_1201, action=action)
                self.assertTrue(result["ok"], result)
                self.assertEqual(result["mapping"]["outcome"], "PREFIX_MISS_EVIDENCE")
                self.assertFalse(result["marker"], result)

    def test_grant_swap_is_rejected_by_resolved_registry(self):
        source = json.loads((ROOT / REGISTRY_PATH).read_text(encoding="ascii"))
        source["role_grants"][0]["artifact_id"], source["role_grants"][1]["artifact_id"] = (
            source["role_grants"][1]["artifact_id"],
            source["role_grants"][0]["artifact_id"],
        )
        overrides = {
            REGISTRY_PATH: (
                json.dumps(source, ensure_ascii=True, indent=2).encode("ascii") + b"\n"
            )
        }
        root, head = self.fixture.commit(overrides=overrides)
        self.assert_error(run_assembler(root, head, RAW_1201), "REGISTRY_ERROR")

    def test_symbolic_abbreviated_and_stale_heads_are_rejected(self):
        root, head = self.fixture.commit()
        self.assert_error(run_assembler(root, "HEAD", RAW_1201), "HEAD_BINDING_ERROR")
        self.assert_error(run_assembler(root, head[:12], RAW_1201), "HEAD_BINDING_ERROR")

        assembler_path = root / ASSEMBLER_PATH
        assembler_path.write_bytes(assembler_path.read_bytes() + b"\n# drift\n")
        self.fixture.commit_current(root, "drift assembler")
        self.assert_error(
            run_assembler(root, head, RAW_1201),
            "WORKTREE_BINDING_ERROR",
        )

    def test_required_worktree_module_drift_is_rejected(self):
        for path in (ROOT_ENVELOPE_PATH, SCHEDULER_PATH, COVERAGE_PATH):
            root, head = self.fixture.commit()
            target = root / path
            target.write_bytes(target.read_bytes() + b"\n# drift\n")
            with self.subTest(path=path):
                self.assert_error(
                    run_assembler(root, head, RAW_1201),
                    "WORKTREE_BINDING_ERROR",
                )

    def test_git_replace_does_not_change_requested_head(self):
        root, original_head = self.fixture.commit()
        note = root / "note.txt"
        note.write_text("replacement commit\n", encoding="utf-8")
        replacement_head = self.fixture.commit_current(root, "replacement")
        subprocess.run(
            ["git", "replace", original_head, replacement_head],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        result = run_assembler(root, original_head, RAW_1201)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["mapping"]["head_sha"], original_head)

    def test_authority_flip_after_object_reseal_is_rejected(self):
        root, head = self.fixture.commit()
        self.assert_error(
            run_assembler(root, head, RAW_73, action="forge_authority"),
            "AUTHORITY_ERROR",
        )


if __name__ == "__main__":
    unittest.main()
