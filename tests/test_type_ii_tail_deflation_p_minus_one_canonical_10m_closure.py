import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_canonical_10m_closure",
    ROOT
    / "reproductions"
    / "type_ii_tail_deflation_p_minus_one_canonical_10m_closure.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOneCanonical10mClosureTests(unittest.TestCase):
    def test_small_canonical_fan_closes_the_strict_descent_boundary(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-canonical-10m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["canonical_shift_cap"], 2)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["strict_descent_count"], 82_880)
        self.assertEqual(result["canonical_short_certificate_count"], 7)
        self.assertEqual(result["unclosed_count"], 0)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            [(record["prime"], record["witness"]["first_shift"]) for record in result["records"]],
            [
                (214_729, 2),
                (297_049, 1),
                (878_089, 1),
                (1_511_449, 1),
                (3_942_409, 2),
                (5_478_169, 1),
                (6_294_649, 2),
            ],
        )

    def test_same_three_layer_closure_through_twenty_million(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-canonical-20m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 20_000_000)
        self.assertEqual(result["canonical_shift_cap"], 2)
        self.assertEqual(result["core_prime_count"], 158_595)
        self.assertEqual(result["strict_descent_count"], 158_584)
        self.assertEqual(result["canonical_short_certificate_count"], 11)
        self.assertEqual(result["unclosed_count"], 0)
        self.assertEqual(
            [(record["prime"], record["witness"]["first_shift"]) for record in result["records"][-4:]],
            [
                (10_170_169, 2),
                (13_782_409, 1),
                (16_152_889, 1),
                (16_267_729, 1),
            ],
        )

    def test_fifty_million_requires_shifts_three_through_five(self):
        boundary_path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-canonical-50m-s2-boundary.json"
        )
        closure_path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-canonical-50m-results.json"
        )
        with boundary_path.open(encoding="utf-8") as handle:
            boundary = json.load(handle)
        with closure_path.open(encoding="utf-8") as handle:
            closure = json.load(handle)
        self.assertEqual(boundary["canonical_shift_cap"], 2)
        self.assertEqual(boundary["unclosed_count"], 4)
        self.assertEqual(
            boundary["unclosed_primes"],
            [25_073_689, 33_011_449, 42_622_969, 48_825_529],
        )
        self.assertEqual(closure["canonical_shift_cap"], 5)
        self.assertEqual(closure["core_prime_count"], 374_902)
        self.assertEqual(closure["strict_descent_count"], 374_882)
        self.assertEqual(closure["canonical_short_certificate_count"], 20)
        self.assertEqual(closure["unclosed_count"], 0)
        self.assertEqual(
            [
                (record["prime"], record["witness"]["first_shift"])
                for record in closure["records"]
                if record["prime"] in boundary["unclosed_primes"]
            ],
            [
                (25_073_689, 3),
                (33_011_449, 3),
                (42_622_969, 4),
                (48_825_529, 5),
            ],
        )


if __name__ == "__main__":
    unittest.main()
