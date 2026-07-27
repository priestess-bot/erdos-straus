import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b1_terminal_overlap_profile",
    ROOT / "reproductions" / "type_i_b1_terminal_overlap_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIBOneTerminalOverlapProfileTests(unittest.TestCase):
    def test_checked_profile_rebuilds(self):
        tail = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json").read_text(
                encoding="utf-8"
            )
        )
        b1 = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-b1-terminal-overlap-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(profile.run_profile(tail, b1), expected)
        self.assertEqual(
            expected["counts"],
            {"other_even_source": 313, "p_minus_one_q_not_divide_r": 1400},
        )
        self.assertEqual(expected["examples"]["p_minus_one_q_not_divide_r"]["prime"], 67369)


if __name__ == "__main__":
    unittest.main()
