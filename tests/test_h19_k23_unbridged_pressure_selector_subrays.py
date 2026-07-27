import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_unbridged_pressure_selector_subrays",
    ROOT / "reproductions" / "h19_k23_unbridged_pressure_selector_subrays.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class H19K23UnbridgedPressureSelectorSubraysTests(unittest.TestCase):
    def test_checked_artifact_is_a_fresh_exact_rerun(self):
        with selector.DEFAULT_INPUT.open(encoding="utf-8") as handle:
            source = json.load(handle)
        with selector.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(selector.run_audit(source), checked)

    def test_both_unbridged_rays_have_infinite_low_defect_subrays(self):
        with selector.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["selector_subray_count"], 2)
        self.assertTrue(result["all_subrays_primitive"])
        self.assertTrue(result["all_support_defects_at_most_two"])
        by_seed = {row["prime_seed"]: row for row in result["subrays"]}
        self.assertEqual(
            by_seed[2_220_549_727_681_245_601]["new_support"], [29]
        )
        self.assertEqual(
            by_seed[748_375_048_866_405_601]["new_support"], [19, 2089]
        )
        self.assertEqual(
            sorted(row["support_defect"] for row in by_seed.values()), [1, 2]
        )

    def test_refinement_multipliers_match_original_pressure_steps(self):
        bridge_path = (
            ROOT
            / "reproductions"
            / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        )
        with bridge_path.open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with selector.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            result = json.load(handle)
        original_steps = {
            int(row["prime_seed"]): int(row["pressure_prime_coefficient"])
            for row in bridge["rows"]
        }
        refined_steps = {
            int(row["prime_seed"]): int(row["prime_step"])
            for row in result["subrays"]
        }
        self.assertEqual(
            refined_steps[2_220_549_727_681_245_601]
            // original_steps[2_220_549_727_681_245_601],
            29,
        )
        self.assertEqual(
            refined_steps[748_375_048_866_405_601]
            // original_steps[748_375_048_866_405_601],
            2_089**2,
        )


if __name__ == "__main__":
    unittest.main()
