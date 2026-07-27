import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_multisource_marked_state",
    ROOT / "reproductions" / "h19_k23_multisource_marked_state.py",
)
assert SPEC and SPEC.loader
state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = state
SPEC.loader.exec_module(state)


class H19K23MultisourceMarkedStateTests(unittest.TestCase):
    def test_post_affine_states_have_complete_source_and_collision_labels(self):
        result = state.run_audit()
        schema = result["state_schema"]
        self.assertEqual(schema["post_affine_residual_branch_count"], 14)
        self.assertEqual(schema["stationary_scale_count"], 37)
        self.assertEqual(schema["h19_shift_count"], 19)
        self.assertEqual(len(result["collision_label"]["source_collision_primes"]), 40)
        self.assertEqual(len(result["collision_label"]["joint_collision_primes"]), 368)
        self.assertTrue(
            all(
                not row["h19_ray_certificate"]
                and len(row["sources"]) == 37
                and all(not source["complete_square_tail_hit"] for source in row["sources"])
                for row in result["states"]
            )
        )

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "h19-k23-multisource-marked-state.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["state_schema"]["post_affine_residual_branch_count"], 14)
        self.assertEqual(len(result["states"]), 14)


if __name__ == "__main__":
    unittest.main()
