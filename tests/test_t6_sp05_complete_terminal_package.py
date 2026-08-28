from __future__ import annotations

import json
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "reproductions" / "sp05_complete_terminal_decision"


class SP05CompleteTerminalPackageTests(unittest.TestCase):
    def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args,
            cwd=PACKAGE,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_integrated_manifest_is_stable_before_and_after_replay(self) -> None:
        self.assertTrue((PACKAGE / "INTEGRATION-NOTE.md").is_file())
        self.assertTrue((PACKAGE / "SOURCE-MANIFEST.sha256").is_file())
        self.assertEqual(list(PACKAGE.glob("*.zip")), [])
        self._run("sha256sum", "-c", "MANIFEST.sha256")
        self._run("bash", "run_all.sh")
        self._run("sha256sum", "-c", "MANIFEST.sha256")

    def test_p21169_complete_schedule_preempts_registered_prefix_miss(self) -> None:
        replay = json.loads(
            (PACKAGE / "evidence" / "p21169-terminal-replay.json").read_text(
                encoding="utf-8"
            )
        )
        decision = replay["source_terminal_decision"]
        self.assertEqual(
            decision["prefix_result"]["outcome"],
            "MISS_REGISTERED_PRIORITY_COMPLETE",
        )
        self.assertEqual(decision["outcome"], "HIT")
        self.assertEqual(
            decision["certificate"]["denominators"],
            [5300, 3619899, 19185464700],
        )
        self.assertEqual(replay["conclusion"], "TERMINAL_PREEMPTS_SUCCESSOR")

    def test_status_preserves_open_actual_edge_boundary(self) -> None:
        status = json.loads(
            (PACKAGE / "evidence" / "status-boundary.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            status["status"],
            "OPEN_PROPOSITION_FOR_FIRST_ACTUAL_NONTERMINAL_EDGE",
        )
        self.assertIn("concrete nonterminal edge witness", status["not_issued"])
        self.assertIn(
            "nonterminal-edge/counterexample equivalence", status["proved"]
        )


if __name__ == "__main__":
    unittest.main()
