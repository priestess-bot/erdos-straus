from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_high_endpoint_root_lift_saturation.py"


def load_module():
    spec = importlib.util.spec_from_file_location("high_endpoint_root_lift_saturation", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SATURATION = load_module()


class HighEndpointRootLiftSaturationTests(unittest.TestCase):
    def test_core_curve_shadow_satisfies_periodic_gate_family(self) -> None:
        SATURATION.check_core_curve_shadow_saturation()

    def test_crt_constructs_an_odd_primitive_capacity_lift(self) -> None:
        SATURATION.check_crt_primitive_lift()

    def test_high_vieta_map_leaves_the_parameter_slice(self) -> None:
        SATURATION.check_high_vieta_noninvariance()


if __name__ == "__main__":
    unittest.main()
