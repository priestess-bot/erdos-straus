"""Regression checks for the exact combined linear source transfer closure."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_source_shift_transfer_closure_profile_600m.py"
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-source-shift-transfer-closure-profile-600m-results.json"
)


def load_module():
    spec = importlib.util.spec_from_file_location("linear_source_shift_transfer", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load shift-transfer profile")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile = load_module()


class LinearSourceShiftTransferClosureProfileTests(unittest.TestCase):
    def test_frozen_artifact_reproduces_exactly(self):
        with ARTIFACT.open(encoding="utf-8") as handle:
            stored = json.load(handle)
        self.assertEqual(profile.run_audit(), stored)

    def test_every_admissible_shift_transfer_preserves_the_linear_source(self):
        for source_profile in profile.run_audit()["profiles"]:
            prime = int(source_profile["prime"])
            states = profile.fixed.checked_states(prime)
            for state in states:
                for factor in profile.raw_shift_candidates(state):
                    target = profile.shift_transfer(prime, state, factor)
                    if target is None:
                        continue
                    self.assertIn(target, states)
                    self.assertEqual(target[0], state[0])
                    self.assertLess(target[1], state[1])

    def test_combined_closure_retains_the_two_isolated_to_hit_examples(self):
        actual = profile.run_audit()
        examples = [
            example
            for source_profile in actual["profiles"]
            for example in source_profile["shift_transfer_to_target_examples"]
        ]
        self.assertEqual(
            examples,
            [
                {"from": [1, 276321, 7], "to": [1, 92107, 23]},
                {"from": [1, 67118061, 7], "to": [1, 22372687, 23]},
            ],
        )

    def test_reversible_checked_edge_components_leave_every_pressure_point_with_a_target_free_part(self):
        for source_profile in profile.run_audit()["profiles"]:
            self.assertGreater(
                int(source_profile["target_free_component_count"]),
                0,
            )
            self.assertGreater(
                int(source_profile["states_in_target_free_components"]),
                0,
            )


if __name__ == "__main__":
    unittest.main()
