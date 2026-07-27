import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_canonical_tail_support_defect_audit",
    ROOT / "reproductions" / "h19_k23_canonical_tail_support_defect_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19K23CanonicalTailSupportDefectAuditTests(unittest.TestCase):
    def test_global_bases_and_nonuniform_fallback_are_explicit(self):
        bases = audit.canonical_bases()
        self.assertEqual(bases[31], ({2, 7, 19}, "maximal-global-affine"))
        self.assertEqual(bases[59], ({3, 5, 7}, "maximal-global-affine"))
        self.assertEqual(bases[63], ({2}, "q-only-nonuniform-tail"))
        self.assertEqual(bases[95], ({2, 3}, "maximal-global-affine"))

    def test_known_terminal_examples_have_their_exact_canonical_defects(self):
        m91 = audit.support_defect(1_431_455_361_734_959_201, 91, {23})
        m95 = audit.support_defect(1_396_789_353_309_110_401, 95, {2, 3})
        self.assertIsNotNone(m91)
        self.assertIsNotNone(m95)
        self.assertEqual(m91["defect"], 1)
        self.assertEqual(m95["defect"], 2)

    def test_checked_artifact_has_no_support_two_miss(self):
        with (
            ROOT / "reproductions" / "h19-k23-canonical-tail-support-defect-1048576.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 1_048_576)
        self.assertEqual(result["m27_alternative_record_count"], 5_081)
        self.assertEqual(result["canonical_support_defect_count"], 5_081)
        self.assertEqual(result["support_defect_misses"], [])
        self.assertEqual(
            result["support_defect_histogram_by_tail_gap"],
            {
                "31": {"0": 2287, "1": 1443},
                "35": {"1": 734, "2": 2},
                "39": {"1": 278, "2": 15},
                "47": {"0": 83, "1": 131, "2": 9},
                "59": {"0": 42, "1": 33, "2": 1},
                "63": {"1": 5, "2": 1},
                "71": {"0": 5, "1": 5, "2": 1},
                "79": {"0": 2, "1": 1, "2": 1},
                "91": {"1": 1},
                "95": {"2": 1},
            },
        )


if __name__ == "__main__":
    unittest.main()
