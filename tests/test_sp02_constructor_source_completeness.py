from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reproductions"))

import sp02_constructor_source_completeness as sp02  # noqa: E402


class SP02ConstructorSourceCompletenessTests(unittest.TestCase):
    def test_good_finite_model_reaches_fixed_point_and_has_four_labels(self) -> None:
        model = sp02.good_model()
        self.assertEqual(model.reach(), frozenset({"r", "a"}))
        report = model.report()
        self.assertEqual(report["unknown_count"], 0)
        self.assertEqual(
            report["labels"],
            {
                "p": sp02.ACTIVE_PRODUCER,
                "t": sp02.TERMINAL_ONLY,
                "k": sp02.NONRUNTIME_CONTROL,
                "u": sp02.OBSOLETE_OR_UNREACHABLE,
            },
        )

    def test_all_seven_negative_controls_fail_closed(self) -> None:
        result = sp02.verify_controls()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["negative_control_count"], 7)

    def test_selector_without_output_is_not_silently_classified(self) -> None:
        model = sp02.good_model()
        invokes = copy.deepcopy(model.invokes)
        invokes["u"] = invokes["u"] | {("r", "w_u")}
        malformed = sp02.FiniteModel(
            states=model.states,
            constructors=model.constructors,
            witnesses=model.witnesses,
            solutions=model.solutions,
            roots=model.roots,
            legal=model.legal,
            verify_sol=model.verify_sol,
            selectors=model.selectors,
            invokes=invokes,
            terminals=model.terminals,
            successors=model.successors,
            state_change_registry=model.state_change_registry,
        )
        with self.assertRaises(sp02.SP02ModelError) as raised:
            malformed.validate()
        self.assertEqual(raised.exception.code, "SELECTOR_NOT_TOTAL")

    def test_registry_is_explicit_and_not_inferred_from_successors(self) -> None:
        model = sp02.good_model()
        malformed = sp02.FiniteModel(
            states=model.states,
            constructors=model.constructors,
            witnesses=model.witnesses,
            solutions=model.solutions,
            roots=model.roots,
            legal=model.legal,
            verify_sol=model.verify_sol,
            selectors=model.selectors,
            invokes=model.invokes,
            terminals=model.terminals,
            successors=model.successors,
            state_change_registry=frozenset(),
        )
        with self.assertRaises(sp02.SP02ModelError) as raised:
            malformed.validate()
        self.assertEqual(raised.exception.code, "STATE_CHANGE_REGISTRY")


if __name__ == "__main__":
    unittest.main()
