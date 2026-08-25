from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_full_carrier_first_child_absorb_entry.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_first_child_absorb_entry", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ENTRY = load_module()


def load_state_fixtures():
    path = ROOT / "tests" / "test_t6_persistent_selector_state_v1.py"
    spec = importlib.util.spec_from_file_location("q_one_absorb_state_fixtures", path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


FIX = load_state_fixtures()


class QOneFirstChildAbsorbEntryTests(unittest.TestCase):
    def test_parity_controls_have_canonical_absorb_cursor(self) -> None:
        ENTRY.verify()

    def test_odd_and_even_targets_match_the_common_absorb_owner(self) -> None:
        for prime in (73, 241):
            entry = ENTRY.first_child_absorb_entry(prime)
            target = entry["target"]
            raw = FIX.make_state(
                FIX.facts(
                    type_i_protocol="ABSORB",
                    provenance_kind="MARKED_ABSORB",
                    full_carrier_scope=True,
                    support_A=target["support_A"],
                    chart_R=target["chart"]["R"],
                    chart_K=target["chart"]["K"],
                    absorb_m=target["absorb_m"],
                    absorb_r_epsilon=target["absorb_r_epsilon"],
                ),
                producer=FIX.INITIALIZER,
                branch="root_nonterminal",
                root_context=prime,
                equation_rank=prime,
            )
            header = FIX.extract(raw)
            owner = FIX.CONTRACT.classify_selector_owner_v1(header)
            self.assertEqual(owner.owner, "type_i_absorb_marked_residual")


if __name__ == "__main__":
    unittest.main()
