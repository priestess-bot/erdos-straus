from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_full_carrier_root_second_anchor_contraction.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_root_second_anchor_contraction", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONTRACTION = load_module()


def load_state_fixtures():
    path = ROOT / "tests" / "test_t6_persistent_selector_state_v1.py"
    spec = importlib.util.spec_from_file_location("q_one_contraction_state_fixtures", path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


FIX = load_state_fixtures()


class QOneRootSecondAnchorContractionTests(unittest.TestCase):
    def test_root_to_final_tickets_cover_both_final_protocols(self) -> None:
        CONTRACTION.verify()

    def test_final_targets_match_common_owner_grammar(self) -> None:
        for prime, expected_owner in (
            (73, "type_i_a_gt_one_overflow_residual"),
            (601, "type_i_absorb_marked_residual"),
        ):
            receipt = CONTRACTION.root_second_anchor_contraction(prime)
            target = receipt["final_target"]
            facts = FIX.facts(
                major_phase=target["facts"]["major_phase"],
                type_i_protocol=target["facts"]["type_i_protocol"],
                provenance_kind=target["facts"]["provenance_kind"],
                full_carrier_scope=True,
                is_overflow=target["facts"]["is_overflow"],
                support_A=target["support"],
                chart_R=target["R"],
                chart_K=target["K"],
                t5_eta_p=target["facts"].get("t5_eta_p", 0),
            )
            if target["facts"]["type_i_protocol"] == "ABSORB":
                facts.update(
                    absorb_m=target["facts"]["absorb_m"],
                    absorb_r_epsilon=target["facts"]["absorb_r_epsilon"],
                )
            raw = FIX.make_state(
                facts,
                producer=FIX.INITIALIZER,
                branch="root_nonterminal",
                root_context=prime,
                equation_rank=prime,
            )
            header = FIX.extract(raw)
            owner = FIX.CONTRACT.classify_selector_owner_v1(header)
            self.assertEqual(owner.owner, expected_owner)


if __name__ == "__main__":
    unittest.main()
