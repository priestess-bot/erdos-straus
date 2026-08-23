from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_high_endpoint_normal_form.py"


def load_module():
    spec = importlib.util.spec_from_file_location("high_endpoint_normal_form", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ROOT / "reproductions"))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


NORMAL_FORM = load_module()


class HighEndpointNormalFormTests(unittest.TestCase):
    def test_strict_actual_control_is_overflow(self) -> None:
        NORMAL_FORM.check_strict_actual_control()

    def test_stutter_shadow_is_explicitly_noncore(self) -> None:
        NORMAL_FORM.check_high_stutter_shadow()

    def test_high_stutter_identities_do_not_require_h_less_than_p(self) -> None:
        NORMAL_FORM.check_high_stutter_symbolic_identities()


if __name__ == "__main__":
    unittest.main()
