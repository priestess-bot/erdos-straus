import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profile_module = load_module(
    "type_i_tail_reverse_single_surplus_profile",
    "type_i_tail_reverse_single_surplus_profile.py",
)
boundary_module = load_module(
    "type_i_tail_reverse_single_surplus_boundary",
    "type_i_tail_reverse_single_surplus_boundary.py",
)


class TypeITailReverseSingleSurplusProfileTests(unittest.TestCase):
    def test_at_most_one_prime_profile_and_its_exhaustive_boundary(self):
        tail = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected_profile = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual_profile = profile_module.run_audit(tail)
        self.assertEqual(actual_profile, expected_profile)
        self.assertEqual(
            (actual_profile["single_surplus_captured_count"], len(actual_profile["single_surplus_misses"])),
            (1_683, 34),
        )
        self.assertEqual(actual_profile["selected_surplus_exponent_histogram"]["0"], 243)

        expected_boundary = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-boundary-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual_boundary = boundary_module.run_audit(actual_profile)
        self.assertEqual(actual_boundary, expected_boundary)
        self.assertEqual(actual_boundary["least_surplus_support_histogram"], {"2": 28, "3": 6})
        self.assertEqual(
            (actual_boundary["unresolved_core_source_count"], actual_boundary["maximum_selected_terminal_prime"]),
            (0, 107),
        )


if __name__ == "__main__":
    unittest.main()
