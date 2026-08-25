from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_t6_f3_proper_root_routing.py"
)


def load_module():
    name = "type_i_t6_f3_proper_root_routing"
    spec = importlib.util.spec_from_file_location(name, MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ROUTING = load_module()


class ProperRootDomainTests(unittest.TestCase):
    def test_high_arithmetic_control_is_retained_in_total_domain(self) -> None:
        self.assertTrue(ROUTING.proper_factor_root(313, 543))
        self.assertFalse(ROUTING.strict_proper_height(313, 543))
        header = ROUTING.fixture(
            p=313, r=90, h=543, m=None, k=None, d_star=None
        )
        result = ROUTING.route(header)
        self.assertEqual(result["route_code"], "HIGH_ENDPOINT_RESIDUAL")
        self.assertFalse(result["low_height_payload_consumed"])
        self.assertFalse(result["low_height_theorems_applicable"])

    def test_low_height_requires_the_low_arithmetic_payload(self) -> None:
        result = ROUTING.route(
            ROUTING.fixture(m=None, k=None, d_star=None)
        )
        self.assertEqual(result["outcome"], "OUTSIDE_DOMAIN")
        self.assertIn("LOW_HEIGHT_K_MISSING", result["errors"])

    def test_nonpersistent_and_analysis_headers_are_outside_domain(self) -> None:
        for source_class in (
            "CONDITIONAL_ADAPTER_CONTROL",
            "ANALYSIS_ONLY",
            "DEBUG_WORKFILE",
            "ARITHMETIC_RECEIPT_NOT_PERSISTENT",
        ):
            result = ROUTING.route(
                ROUTING.fixture(source_class=source_class)
            )
            self.assertEqual(result["outcome"], "OUTSIDE_DOMAIN")
            self.assertIn("SOURCE_NOT_ACTUAL_PERSISTENT", result["errors"])


class ProperRootRoutingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = ROUTING.load_spec()

    def test_seven_residuals_are_pairwise_selected(self) -> None:
        observed = ROUTING.verify_partition(self.spec)
        self.assertEqual(tuple(observed), ROUTING.RESIDUAL_CODES)
        self.assertEqual(set(observed.values()), {"OPEN_MINIMAL_GAP"})

    def test_terminal_first_preempts_every_carrier_route(self) -> None:
        header = ROUTING.fixture(
            p=313,
            r=90,
            h=543,
            m=None,
            k=None,
            d_star=None,
            terminal_first_status=ROUTING.TERMINAL_HIT,
            terminal_certificate_id="fixture-certificate",
            active_serializer_id="unregistered-and-not-read",
        )
        result = ROUTING.route(header, self.spec)
        self.assertEqual(result["outcome"], "TERMINAL")
        self.assertFalse(result["active_edge"])

    def test_k_one_is_covered_only_as_an_empty_actual_slice(self) -> None:
        result = ROUTING.route(ROUTING.fixture(k=1, d_star=7), self.spec)
        self.assertEqual(result["route_code"], "K_ONE_ACTUAL_EMPTY")
        self.assertFalse(result["actual_instance_consistent"])
        self.assertFalse(result["active_edge"])

    def test_high_preempts_low_k_and_serializer_fields(self) -> None:
        result = ROUTING.route(
            ROUTING.fixture(
                p=313,
                r=90,
                h=543,
                m=None,
                k=1,
                d_star=None,
                active_serializer_id="must-not-be-read",
            ),
            self.spec,
        )
        self.assertEqual(result["route_code"], "HIGH_ENDPOINT_RESIDUAL")
        self.assertFalse(result["low_height_payload_consumed"])
        self.assertFalse(result["active_edge"])

    def test_m3_q5_is_only_the_two_low_q5_residuals(self) -> None:
        unbound = ROUTING.route(ROUTING.fixture(), self.spec)
        bound = ROUTING.route(
            ROUTING.fixture(raw_path_bound=True), self.spec
        )
        self.assertEqual(unbound["route_code"], ROUTING.RESIDUAL_CODES[1])
        self.assertEqual(bound["route_code"], ROUTING.RESIDUAL_CODES[2])
        for result in (unbound, bound):
            self.assertTrue(result["m3_q5_slice"])
            self.assertEqual(result["p2_gate_status"], "OPEN")
            self.assertIsNone(result["active_serializer"])
            self.assertFalse(result["active_edge"])

    def test_no_active_qc1_or_tr1_serializer_exists(self) -> None:
        self.assertEqual(
            self.spec["active_physical_serializers"],
            {"QC1": [], "TR1": []},
        )
        with self.assertRaises(ROUTING.RoutingContractError):
            ROUTING.route(
                ROUTING.fixture(active_serializer_id="unregistered-qc1"),
                self.spec,
            )

    def test_full_focused_verifier_preserves_open_boundary(self) -> None:
        report = ROUTING.run()
        self.assertEqual(report["status"], "ESTABLISHED_DOMAIN_PARTITION")
        self.assertEqual(report["physicalization"], "OPEN_MINIMAL_GAPS")
        self.assertFalse(report["fixtures_are_actual_receipt_evidence"])
        self.assertEqual(
            report["active_physical_serializers"],
            {"QC1": [], "TR1": []},
        )


if __name__ == "__main__":
    unittest.main()
