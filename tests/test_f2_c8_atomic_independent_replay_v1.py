from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "reproductions" / "f2_c8_atomic_independent_replay_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "f2_c8_atomic_independent_replay_v1", PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {PATH}")
REPLAY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = REPLAY
SPEC.loader.exec_module(REPLAY)


class IndependentReplayTests(unittest.TestCase):
    def test_independent_replay(self) -> None:
        REPLAY.verify()

    def test_parent_stutter_and_low_capacities_are_not_in_the_congruence(self) -> None:
        prime = 157_393
        for capacity in (*range(1, 9), prime - 1):
            with self.subTest(capacity=capacity):
                with self.assertRaises(AssertionError):
                    REPLAY.verify_capacity_interval(prime, capacity)


if __name__ == "__main__":
    unittest.main()
