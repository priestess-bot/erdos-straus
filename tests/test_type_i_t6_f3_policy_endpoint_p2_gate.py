import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_t6_f3_policy_endpoint_p2_gate",
    ROOT / "reproductions" / "type_i_t6_f3_policy_endpoint_p2_gate.py",
)
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)


class TypeIT6F3PolicyEndpointP2GateTests(unittest.TestCase):
    def test_two_sided_normal_form(self):
        result = gate.verify_two_sided_control()
        self.assertEqual(result["prime"], 73)
        self.assertGreater(result["left_E"], 1)
        self.assertGreater(result["right_E"], 1)
        self.assertEqual(result["multiplier"] % (73 * 73), 1)

    def test_full_capacity_one_sided_factor_pair(self):
        result = gate.verify_full_capacity_one_sided_control()
        self.assertEqual((result["m"], result["c"], result["d"]), (4, 17, 331))
        self.assertEqual(result["chi"], 39_257_934)
        self.assertGreaterEqual(result["u"] * result["u"], result["prime"])

    def test_multiplier_congruence_is_not_a_chart_wide_invariant(self):
        result = gate.verify_recanonicalization_noninvariance_control()
        self.assertEqual(result["first_multiplier_mod_p2"], 1)
        self.assertNotEqual(result["endpoint_multiplier_mod_p"], 1)
        self.assertEqual(result["endpoint_target_cofactor"], 2)

    def test_manifest_keeps_b5_and_f3_open(self):
        result = gate.run_verifier()
        self.assertEqual(result["normal_form_status"], "ESTABLISHED")
        self.assertEqual(result["b5_status"], "OPEN_MINIMAL_RESIDUAL")
        self.assertEqual(result["f3_status"], "OPEN")

    def test_nonprimitive_endpoint_is_rejected(self):
        source = gate.chart(73, 57)
        with self.assertRaisesRegex(AssertionError, "primitive p-free"):
            gate.factor_endpoint(
                73,
                source["support"],
                source["capacity"],
                2,
                2,
            )


if __name__ == "__main__":
    unittest.main()
