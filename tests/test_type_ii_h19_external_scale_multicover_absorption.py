import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_external_scale_multicover_absorption",
    ROOT / "reproductions" / "type_ii_h19_external_scale_multicover_absorption.py",
)
assert SPEC and SPEC.loader
absorption = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = absorption
SPEC.loader.exec_module(absorption)


class TypeIIH19ExternalScaleMulticoverAbsorptionTests(unittest.TestCase):
    def test_mod_seven_split_has_no_immediate_exit(self):
        result = absorption.run_audit()
        self.assertEqual(result["path"]["stationary_scale_count"], 144)
        self.assertEqual(
            result["parent"]["covering_primes"], [7, 37, 53, 61, 73]
        )
        self.assertEqual(result["immediate_exit_count"], 0)
        self.assertEqual(len(result["children"]), 7)
        self.assertEqual(
            [child["w_mod_7"] for child in result["children"]], list(range(7))
        )
        for child in result["children"]:
            self.assertEqual(child["combined_form_count"], 164)
            self.assertEqual(child["covering_primes"], [37, 53, 61, 73])
            self.assertEqual(child["h19_ray_hits"], [])
            self.assertEqual(child["source_hits"], [])

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-external-scale-multicover-absorption.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["immediate_exit_count"], 0)
        self.assertEqual(len(result["children"]), 7)


if __name__ == "__main__":
    unittest.main()
