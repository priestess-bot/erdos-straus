import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_external_scale_k23_branching",
    ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py",
)
assert SPEC and SPEC.loader
branching = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = branching
SPEC.loader.exec_module(branching)


class TypeIIH19ExternalScaleK23BranchingTests(unittest.TestCase):
    def test_full_mod_twenty_nine_branch_partition(self):
        result = branching.run_audit()
        self.assertEqual(result["parent"]["covering_primes"], [29])
        self.assertEqual(len(result["covering_root_map_mod_29"]), 29)
        self.assertEqual(len(result["branches"]), 29)
        self.assertEqual(
            result["histogram"],
            {
                "nonprimitive": 1,
                "h19_ray_certificate": 5,
                "external_source_descent": 9,
                "admissible_escape": 18,
            },
        )
        self.assertEqual(result["resolved_branch_count"], 11)
        self.assertEqual(
            [branch["v_mod_29"] for branch in result["branches"]], list(range(29))
        )
        escapes = [
            branch for branch in result["branches"] if branch["admissible_escape"]
        ]
        self.assertEqual(len(escapes), 18)
        self.assertTrue(
            all(
                branch["combined_form_count"] == 57
                and branch["covering_primes"] == []
                and not branch["h19_ray_hits"]
                and not branch["source_hits"]
                for branch in escapes
            )
        )

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-external-scale-k23-branching.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["parent"]["covering_primes"], [29])
        self.assertEqual(result["resolved_branch_count"], 11)
        self.assertEqual(result["histogram"]["admissible_escape"], 18)


if __name__ == "__main__":
    unittest.main()
