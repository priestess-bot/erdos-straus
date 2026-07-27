import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_release_boundary",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_release_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19FourthEvenSourceReleaseBoundaryTests(unittest.TestCase):
    def test_checked_artifact_records_the_first_release(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-release-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["scanned_odd_distances_through"], 34_091)
        first = result["first_strict_descent"]
        self.assertIsNotNone(first)
        assert first is not None
        self.assertEqual(first["distance"], 34_091)
        self.assertEqual(first["source_denominator"], 640_741_598)
        self.assertEqual((first["k"], first["q"], first["factor"]), (4699, 18_795, 1_761_718))
        self.assertEqual(first["certificate"]["gap"], 375)

    def test_even_caps_are_rejected(self):
        with self.assertRaises(ValueError):
            audit.run_audit(34_090)


if __name__ == "__main__":
    unittest.main()
