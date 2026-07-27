import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_even_external_source_normal_bridge",
    ROOT / "reproductions" / "type_i_even_external_source_normal_bridge.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIEvenExternalSourceNormalBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            cls.payload = json.load(handle)
        cls.witnesses = {
            int(record["prime"]): record["quadratic_factor_external_source_descent"]
            for record in cls.payload["records"]
        }

    def test_even_external_witness_is_the_target_normal_terminal_bridge(self):
        expected = {
            225_289: (197_128, 2, 7, 394_256, [687, 1, 82]),
            2_707_609: (2_594_792, 6, 23, 15_568_752, [7871, 1, 86]),
        }
        for prime, (source, k, r, normal_k, normal_form) in expected.items():
            bridge = audit.bridge_from_quadratic_external_witness(
                prime, self.witnesses[prime]
            )
            self.assertEqual(bridge["source_denominator"], source)
            self.assertEqual(bridge["k"], k)
            self.assertEqual(bridge["R"], r)
            self.assertEqual(bridge["K"], normal_k)
            self.assertEqual(bridge["normal_form"], normal_form)
            self.assertEqual(bridge["E"], source)
            self.assertTrue(all(bridge["conditions"].values()))
            a, b, _ = normal_form
            normal_tail = audit.short_certificate.type_i_normal_tail_deflation_witness(
                prime, bridge["gap"], a, b
            )
            self.assertIsNotNone(normal_tail)
            assert normal_tail is not None
            self.assertEqual(normal_tail.source_denominator, source)
            self.assertEqual(
                normal_tail.source_solution[2], bridge["source_first_denominator"]
            )
            self.assertEqual(
                normal_tail.target_solution[2],
                prime * bridge["source_first_denominator"],
            )

    def test_odd_external_witness_has_the_same_bridge_without_terminal_parity(self):
        bridge = audit.bridge_from_quadratic_external_witness(3361, self.witnesses[3361])
        self.assertEqual(bridge["source_denominator"], 2941)
        self.assertEqual(bridge["R"], 7)
        self.assertEqual(bridge["K"], 5882)
        self.assertEqual(bridge["normal_form"], [25, 2, 17])
        self.assertFalse(bridge["conditions"]["source_is_even"])
        a, b, _ = bridge["normal_form"]
        normal_tail = audit.short_certificate.type_i_normal_tail_deflation_witness(
            3361, bridge["gap"], a, b
        )
        self.assertIsNotNone(normal_tail)
        assert normal_tail is not None
        self.assertEqual(normal_tail.source_denominator, 2941)
        self.assertTrue(
            all(
                bridge["conditions"][name]
                for name in (
                    "divides_4K_squared",
                    "residue_one_mod_R",
                    "strict_source_lower_bound",
                )
            )
        )

    def test_one_billion_h19_audit_splits_terminal_and_marked_sources(self):
        result = audit.run_audit(self.payload)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_external_hit_count"], 660)
        self.assertEqual(result["quadratic_external_miss_count"], 4)
        self.assertEqual(result["normal_bridge_count"], 660)
        self.assertEqual(result["terminal_even_bridge_count"], 120)
        self.assertEqual(result["odd_source_bridge_count"], 540)
        self.assertEqual(
            result["quadratic_external_misses"],
            [35_840_809, 132_285_169, 141_326_089, 640_775_689],
        )


if __name__ == "__main__":
    unittest.main()
