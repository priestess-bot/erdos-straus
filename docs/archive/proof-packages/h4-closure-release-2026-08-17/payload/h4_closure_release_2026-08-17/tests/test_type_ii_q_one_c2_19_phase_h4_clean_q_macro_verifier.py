import importlib.util
import pathlib
import sys
import unittest

MODULE_PATH = pathlib.Path(__file__).parents[1] / "reproductions" / "type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py"
spec = importlib.util.spec_from_file_location("h4verifier", MODULE_PATH)
h4 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = h4
assert spec.loader is not None
spec.loader.exec_module(h4)


class H4CleanQMacroVerifierTests(unittest.TestCase):
    def test_existing_control_fixtures_pass_e1_e5(self):
        results = h4.verify_controls()
        self.assertEqual({r["name"] for r in results}, {"p73", "p241"})
        for r in results:
            self.assertEqual(r["branch"], "atomic_split")
            self.assertEqual(r["e1_e5"], {"E1": True, "E2": True, "E3": True, "E4": True, "E5": True})

    def test_corrected_single_side_formula_absorbs_y_block(self):
        m4, qx, qy = 35, 1, 11
        old_formula = __import__("math").lcm(m4, qx)
        corrected = h4.corrected_target_support(m4, qx, qy)
        self.assertEqual(old_formula, 35)
        self.assertEqual(corrected, 385)
        self.assertGreater(corrected, old_formula)

    def test_control_multiplier_matches_existing_known_values(self):
        # The pre-existing clean-q reproduction stores these as the support
        # multipliers L_target=M_target/M4, not as M_target itself.
        expected = {"p73": 793858499, "p241": 212593597025}
        for f in h4.CONTROL_FIXTURES:
            receipt = h4.verify_h4_macro(h4.make_control_input(**f))
            self.assertEqual(receipt["corrected_support"]["L_target"], expected[f["name"]])
            self.assertEqual(
                receipt["corrected_support"]["M_target"],
                receipt["h4"]["M4"] * expected[f["name"]],
            )

    def test_priority_miss_is_a_real_premise(self):
        inp = h4.make_control_input(**h4.CONTROL_FIXTURES[0])
        bad = h4.H4Input(
            p=inp.p, r4=inp.r4, k4=inp.k4, m4=inp.m4, c4=inp.c4,
            persistent_parent=inp.persistent_parent,
            priority_prefix={**inp.priority_prefix, "status": "hit"},
            upstream_h4=inp.upstream_h4,
        )
        with self.assertRaises(h4.VerificationError):
            h4.verify_h4_macro(bad)

    def test_target_type_label_is_not_inherited(self):
        receipt = h4.verify_h4_macro(h4.make_control_input(**h4.CONTROL_FIXTURES[0]))
        self.assertEqual(receipt["target"]["dispatch_status"], "pending_dispatch")
        self.assertFalse(receipt["target"]["inherited_type_label"])
        self.assertFalse(receipt["typed_reclassification"]["inherited_label"])

    def test_receipt_is_deterministic(self):
        inp = h4.make_control_input(**h4.CONTROL_FIXTURES[1])
        a = h4.verify_h4_macro(inp)
        b = h4.verify_h4_macro(inp)
        self.assertEqual(a["target"]["state_id"], b["target"]["state_id"])
        self.assertEqual(a["edge_id"], b["edge_id"])


if __name__ == "__main__":
    unittest.main()
