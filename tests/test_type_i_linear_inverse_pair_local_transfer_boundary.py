"""Regression checks for the inverse-pair local-transfer boundary."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_inverse_pair_local_transfer_boundary.py"
ARTIFACT = ROOT / "reproductions" / "type-i-linear-inverse-pair-local-transfer-boundary-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("inverse_pair_local_boundary", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load inverse-pair local-transfer boundary")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile = load_module()


class InversePairLocalTransferBoundaryTests(unittest.TestCase):
    def test_frozen_artifact_reproduces_exactly(self):
        with ARTIFACT.open(encoding="utf-8") as handle:
            stored = json.load(handle)
        self.assertEqual(profile.run_audit(), stored)

    def test_affine_block_divisors_cannot_be_local_transfer_factors(self):
        for row in profile.run_audit()["profiles"]:
            counts = row["affine_divisor_counts"]
            self.assertEqual(counts["fixed_s_admissible_count"], 0)
            self.assertEqual(counts["shift_s_admissible_count"], 0)
            self.assertEqual(row["gcd_a_L"], 1)
            self.assertEqual(row["gcd_s_L"], 1)

    def test_forward_closures_are_target_free(self):
        actual = profile.run_audit()
        self.assertEqual(actual["inverse_pair_candidate_count"], 2)
        for row in actual["profiles"]:
            self.assertEqual(row["forward_local_closure_hit_R"], [])
            self.assertEqual(row["forward_local_closure_hit_state_count"], 0)
        by_key = {(row["prime"], row["R"]): row for row in actual["profiles"]}
        self.assertEqual(by_key[(64_214_329, 359)]["forward_local_closure_state_count"], 1)
        self.assertEqual(by_key[(105_295_129, 839)]["forward_local_closure_state_count"], 7)

    def test_source_edges_preserve_strict_linear_source_identities(self):
        for row in profile.run_audit()["profiles"]:
            prime = int(row["prime"])
            for edge in row["forward_local_closure_edges"]:
                source = tuple(int(value) for value in edge["from"])
                target = tuple(int(value) for value in edge["to"])
                profile.state_valid(prime, source)
                profile.state_valid(prime, target)
                if edge["kind"] == "fixed_s":
                    self.assertEqual(source[1], target[1])
                    self.assertLess(target[0], source[0])
                elif edge["kind"] == "shift_s":
                    self.assertEqual(source[0], target[0])
                    self.assertLess(target[1], source[1])
                else:
                    self.assertEqual(source[2], target[2])


if __name__ == "__main__":
    unittest.main()
