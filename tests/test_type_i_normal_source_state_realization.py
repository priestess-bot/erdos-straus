import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_normal_source_state_realization",
    ROOT / "reproductions" / "type_i_normal_source_state_realization.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeINormalSourceStateRealizationTests(unittest.TestCase):
    def test_source_state_divisor_pairs_recover_all_stored_normal_forms(self):
        profile = json.loads(
            (ROOT / "reproductions" / "type-i-h19-p25-residue-boundary-source-profile-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-normal-source-state-realization-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(profile)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["input_source_state_count"], 28)
        self.assertTrue(actual["all_stored_normal_forms_recovered"])
        self.assertTrue(actual["all_source_states_have_B_eq_1_realization"])
        self.assertTrue(all(record["compatible_normal_form_count"] >= 2 for record in actual["records"]))
        self.assertTrue(all(record["B_eq_1_form_count"] >= 1 for record in actual["records"]))


if __name__ == "__main__":
    unittest.main()
