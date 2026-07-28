"""Regression checks for the exact fixed-s linear source factor-transfer profile."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_source_factor_transfer_profile_600m.py"
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-source-factor-transfer-profile-600m-results.json"
)


def load_module():
    spec = importlib.util.spec_from_file_location("linear_source_factor_transfer", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load factor-transfer profile")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile = load_module()


class LinearSourceFactorTransferProfileTests(unittest.TestCase):
    def test_frozen_artifact_reproduces_exactly(self):
        with ARTIFACT.open(encoding="utf-8") as handle:
            stored = json.load(handle)
        self.assertEqual(profile.run_audit(), stored)

    def test_every_profiled_transfer_preserves_source_and_realizes_its_k_factor(self):
        for source_profile in profile.run_audit()["profiles"]:
            prime = int(source_profile["prime"])
            states = profile.checked_states(prime)
            for state in states:
                a, s, _ = state
                for factor in profile.sources.divisors_from_factorization(
                    profile.sources.exact_factorization(a)
                ):
                    if factor <= 1 or (factor - 1) % s:
                        continue
                    target = profile.transfer_factor(prime, state, factor)
                    self.assertIn(target, states)
                    self.assertEqual(target[1], s)
                    self.assertLess(target[0], a)

    def test_s_isolated_failures_cannot_reach_a_target_hit_by_factor_transfer(self):
        input_profiles = json.loads(
            profile.INPUT.read_text(encoding="utf-8")
        )["profiles"]
        hits_by_prime = {
            int(source_profile["prime"]): {
                int(value) for value in source_profile["hit_R"]
            }
            for source_profile in input_profiles
        }
        for source_profile in profile.run_audit()["profiles"]:
            prime = int(source_profile["prime"])
            states = profile.checked_states(prime)
            hit_s = {
                state[1] for state in states if state[2] in hits_by_prime[prime]
            }
            isolated = {
                state
                for state in states
                if state[2] not in hits_by_prime[prime] and state[1] not in hit_s
            }
            self.assertEqual(
                len(isolated),
                int(source_profile["failed_state_s_isolated_from_target_hit_count"]),
            )
            self.assertTrue(isolated)
            for state in isolated:
                self.assertNotIn(state[1], hit_s)


if __name__ == "__main__":
    unittest.main()
