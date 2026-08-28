from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "reproductions" / "sp04_q1_m23"
ARCHIVE = (
    ROOT
    / "docs"
    / "archive"
    / "proof-packages"
    / "standalone-proof-propositions-2026-08-28"
    / "SP-04-complete-proof-package.zip"
)
EXPECTED_ARCHIVE_SHA256 = (
    "55219cd1f34a35046119573f7c90d2a24177565d340c860e77ae95abe257924c"
)


class SP04Q1M23PackageTests(unittest.TestCase):
    def test_archive_is_present_and_source_directory_has_no_zip(self) -> None:
        self.assertTrue(ARCHIVE.is_file())
        self.assertEqual(
            hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
            EXPECTED_ARCHIVE_SHA256,
        )
        self.assertEqual(list(EVIDENCE.glob("*.zip")), [])

    def test_constructor_and_independent_verifier_replay(self) -> None:
        constructor = subprocess.run(
            [sys.executable, "sp04_constructor.py"],
            cwd=EVIDENCE,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn('"registered_gap_records": 42', constructor.stdout)
        verifier = subprocess.run(
            [sys.executable, "sp04_verifier.py"],
            cwd=EVIDENCE,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SP-04 INDEPENDENT VERIFICATION: PASS", verifier.stdout)
        manifest_check = subprocess.run(
            ["sha256sum", "-c", "MANIFEST.sha256"],
            cwd=EVIDENCE,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(manifest_check.returncode, 0)

    def test_earliest_controls_and_registered_miss_boundary(self) -> None:
        outcomes = json.loads((EVIDENCE / "outcomes.json").read_text(encoding="utf-8"))
        expected = {
            73: (7, 1, "II"),
            241441: (11, 27, "II"),
            2689: (15, 26, "I"),
            12721: (19, 7, "II"),
            1201: (23, 34, "I"),
            2521: (23, 8, "II"),
        }
        for outcome in outcomes:
            prime = outcome["p"]
            if prime == 21169:
                self.assertEqual(outcome["status"], "MISS_REGISTERED_PRIORITY_COMPLETE")
                self.assertEqual(outcome["coverage"], "REGISTERED_PRIORITY_ONLY")
                self.assertEqual(outcome["next_unchecked_gap"], 27)
                self.assertFalse(outcome["global_exhaustion"])
            else:
                self.assertEqual(outcome["status"], "TERMINAL_HIT")
                earliest = outcome["earliest"]
                self.assertEqual(
                    (earliest["m"], earliest["d"], earliest["type"]),
                    expected[prime],
                )

        report = (EVIDENCE / "verification_report.txt").read_text(encoding="utf-8")
        self.assertIn("p=21169,m=31,d=1,Type-II verified", report)
        self.assertIn("global_exhaustion=false", report)


if __name__ == "__main__":
    unittest.main()
