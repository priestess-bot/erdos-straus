import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_one_factor_prime_families",
    ROOT / "reproductions" / "h19_k23_global_one_factor_prime_families.py",
)
assert SPEC and SPEC.loader
families = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = families
SPEC.loader.exec_module(families)


class H19K23GlobalOneFactorPrimeFamiliesTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-one-factor-prime-families-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(families.run_audit(pressure), checked)

    def test_every_family_preserves_one_factor_and_all_base_only_misses(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-factor-prime-families-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["one_factor_prime_progression_count"], 22)
        self.assertEqual(result["distinct_new_prime_count"], 21)
        self.assertTrue(
            all(
                family["prime_progression_gcd"] == 1
                and family["unit_shift_one_factor_divisor"]
                == family["one_factor_divisor"]
                and family["unit_shift_base_only_miss_gaps"]
                == family["canonical_base_only_miss_gaps"]
                and family["source_denominator"]
                == family["tail_parameter"] + 1
                and family["unit_shift_source_denominator"]
                > family["source_denominator"]
                for family in result["families"]
            )
        )


if __name__ == "__main__":
    unittest.main()
