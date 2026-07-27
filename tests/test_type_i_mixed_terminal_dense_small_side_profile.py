import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mixed_terminal_dense_small_side_profile",
    ROOT / "reproductions" / "type_i_mixed_terminal_dense_small_side_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIMixedTerminalDenseSmallSideProfileTests(unittest.TestCase):
    def test_dense_500m_to_600m_profile_rebuilds_exactly(self):
        source = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-small-side-profile-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["type_i_terminal_bridge_count"], 247)
        self.assertEqual(actual["small_side_misses"], [])
        self.assertEqual(
            actual["selected_small_side_count"] + actual["alternative_small_side_captured_count"],
            actual["combined_small_side_closure_count"],
        )


if __name__ == "__main__":
    unittest.main()
