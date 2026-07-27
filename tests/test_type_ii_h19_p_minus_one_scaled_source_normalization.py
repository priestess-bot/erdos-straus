import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_p_minus_one_scaled_source_normalization",
    ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_normalization.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19PMinusOneScaledSourceNormalizationTests(unittest.TestCase):
    def test_all_stored_witnesses_have_the_exact_normal_form(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-p-minus-one-scaled-source-normalization-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["witness_count"], 15)
        self.assertTrue(result["all_target_first_denominators_divisible_by_prime"])
        self.assertTrue(result["all_shifts_recovered"])
        target = next(record for record in result["records"] if record["prime"] == 99_532_801)
        self.assertEqual(target["shift"], target["recovered_shift"])


if __name__ == "__main__":
    unittest.main()
