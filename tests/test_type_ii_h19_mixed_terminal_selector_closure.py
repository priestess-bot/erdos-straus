import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_mixed_terminal_selector_closure",
    ROOT / "reproductions" / "type_ii_h19_mixed_terminal_selector_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIIH19MixedTerminalSelectorClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (
            ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
        ).open(encoding="utf-8") as handle:
            cls.tail_payload = json.load(handle)
        with (
            ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
        ).open(encoding="utf-8") as handle:
            cls.external_payload = json.load(handle)

    def test_rebuilds_the_stored_mixed_terminal_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-h19-mixed-terminal-selector-closure-1b-results.json"
        ).open(encoding="utf-8") as handle:
            expected = json.load(handle)
        self.assertEqual(
            closure.run_audit(self.tail_payload, self.external_payload), expected
        )

    def test_every_h19_residual_has_the_requested_branch(self):
        result = closure.run_audit(self.tail_payload, self.external_payload)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["ordinary_type_ii_tail_certificate_count"], 662)
        self.assertEqual(result["type_i_even_terminal_bridge_count"], 2)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            result["type_i_even_terminal_bridge_records"],
            [
                {
                    "prime": 225_289,
                    "source_denominator": 197_128,
                    "k": 2,
                    "R": 7,
                    "K": 394_256,
                    "external_factor": 82,
                    "gap": 47,
                    "normal_form": [687, 1, 82],
                    "E": 197_128,
                    "source_first_denominator": 394_256,
                    "conditions": {
                        "divides_4K_squared": True,
                        "residue_one_mod_R": True,
                        "strict_source_lower_bound": True,
                        "source_is_even": True,
                    },
                },
                {
                    "prime": 2_707_609,
                    "source_denominator": 2_594_792,
                    "k": 6,
                    "R": 23,
                    "K": 15_568_752,
                    "external_factor": 86,
                    "gap": 15,
                    "normal_form": [7871, 1, 86],
                    "E": 2_594_792,
                    "source_first_denominator": 15_568_752,
                    "conditions": {
                        "divides_4K_squared": True,
                        "residue_one_mod_R": True,
                        "strict_source_lower_bound": True,
                        "source_is_even": True,
                    },
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
