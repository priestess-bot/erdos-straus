from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_q_one_phase_root_independent_math_replay_v1 as replay  # noqa: E402


def valid_bundle_73() -> dict[str, object]:
    return {
        "source": {
            "schema_version": 1,
            "root_context": 73,
            "equation_rank": 73,
            "equation_numerator": 4,
            "equation_denominator": 73,
            "q": 1,
            "gap": 3,
            "u": 18,
            "x": 19,
            "endpoint_fiber_code": 2,
            "major_phase_code": 3,
            "provenance_code": 1,
            "mark_kind_code": 1,
            "mark_root_context": 73,
            "mark_equation_rank": 73,
            "declared_branch_type_code": 1,
            "factorization": [[19, 1]],
        },
        "candidate": {
            "schema_version": 1,
            "root_context": 73,
            "t": 3,
            "x": 19,
            "chart_r": 51,
            "chart_k": 931,
            "support_a": 1,
            "source_u": 73,
            "source_v": 3599,
            "source_m": 72,
            "edge_prime": 73,
            "edge_shift": 1,
            "gcd_reduction": 1,
            "anchor_u": 1,
            "anchor_v": 50,
            "anchor_m": 1,
        },
        "projection": {
            "schema_version": 1,
            "root_context": 73,
            "equation_rank": 73,
            "equation_numerator": 4,
            "equation_denominator": 73,
            "mark_kind_code": 1,
            "mark_root_context": 73,
            "mark_equation_rank": 73,
            "major_phase_code": 2,
            "type_i_protocol_code": 4,
            "provenance_code": 2,
            "full_carrier_scope_code": 1,
            "support_a": 1,
            "chart_r": 51,
            "chart_k": 931,
            "declared_branch_type_code": 2,
            "ticket_code": 2,
            "source_t5_coordinates": [73, 3, 0, 0, 0, 0, 0],
            "target_t5_coordinates": [73, 2, 4, 1296, 931, 0, 0],
        },
    }


def valid_bundle_76129() -> dict[str, object]:
    bundle = valid_bundle_73()
    bundle["source"] = {
        "schema_version": 1,
        "root_context": 76129,
        "equation_rank": 76129,
        "equation_numerator": 4,
        "equation_denominator": 76129,
        "q": 1,
        "gap": 3,
        "u": 19032,
        "x": 19033,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "mark_root_context": 76129,
        "mark_equation_rank": 76129,
        "declared_branch_type_code": 1,
        "factorization": [[7, 1], [2719, 1]],
    }
    bundle["candidate"] = {
        "schema_version": 1,
        "root_context": 76129,
        "t": 3172,
        "x": 19033,
        "chart_r": 50755,
        "chart_k": 965981849,
        "support_a": 1,
        "source_u": 76129,
        "source_v": 3863800511,
        "source_m": 76128,
        "edge_prime": 76129,
        "edge_shift": 1,
        "gcd_reduction": 1,
        "anchor_u": 1,
        "anchor_v": 50754,
        "anchor_m": 1,
    }
    bundle["projection"] = {
        "schema_version": 1,
        "root_context": 76129,
        "equation_rank": 76129,
        "equation_numerator": 4,
        "equation_denominator": 76129,
        "mark_kind_code": 1,
        "mark_root_context": 76129,
        "mark_equation_rank": 76129,
        "major_phase_code": 2,
        "type_i_protocol_code": 4,
        "provenance_code": 2,
        "full_carrier_scope_code": 1,
        "support_a": 1,
        "chart_r": 50755,
        "chart_k": 965981849,
        "declared_branch_type_code": 2,
        "ticket_code": 2,
        "source_t5_coordinates": [76129, 3, 0, 0, 0, 0, 0],
        "target_t5_coordinates": [
            76129,
            2,
            4,
            1448868096,
            965981849,
            0,
            0,
        ],
    }
    return bundle


def forge_exact(value: object, **changes: object) -> object:
    forged = object.__new__(type(value))
    for field in fields(type(value)):
        object.__setattr__(
            forged,
            field.name,
            changes.get(field.name, getattr(value, field.name)),
        )
    return forged


def reseal_exact(
    receipt: replay.QOnePhaseRootMathReplayV1, **changes: object
) -> replay.QOnePhaseRootMathReplayV1:
    provisional = forge_exact(receipt, digest="0" * 64, **changes)
    payload = replay._jsonable(provisional)
    payload.pop("digest")
    return forge_exact(
        provisional, digest=replay.canonical_digest_v1(payload)
    )


class SpoofedBlockedAuthority(str):
    def __new__(cls) -> SpoofedBlockedAuthority:
        return str.__new__(cls, "GRANTED")

    def __eq__(self, other: object) -> bool:
        return other == "BLOCKED"


class SpoofedExpectedText(str):
    def __new__(cls, raw: str, expected: str) -> SpoofedExpectedText:
        value = str.__new__(cls, raw)
        value.expected = expected
        return value

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class SpoofedExpectedInt(int):
    def __new__(cls, raw: int, expected: int) -> SpoofedExpectedInt:
        value = int.__new__(cls, raw)
        value.expected = expected
        return value

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class SpoofedExpectedKey(str):
    def __new__(cls, raw: str, expected: str) -> SpoofedExpectedKey:
        value = str.__new__(cls, raw)
        value.expected = expected
        return value

    def __hash__(self) -> int:
        return hash(self.expected)

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class IndependentQOnePhaseRootReplayTests(unittest.TestCase):
    def assert_reject(
        self,
        code: replay.MathReplayRejectCode,
        bundle: dict[str, object],
    ) -> None:
        with self.assertRaises(replay.MathReplayError) as caught:
            replay.replay_q_one_phase_root_math_v1(
                bundle["source"], bundle["candidate"], bundle["projection"]
            )
        self.assertEqual(caught.exception.code, code)

    def test_hard_coded_single_and_multifactor_g_controls_replay(self):
        for bundle, expected in (
            (valid_bundle_73(), (73, 3, 19, 51, 931)),
            (valid_bundle_76129(), (76129, 3172, 19033, 50755, 965981849)),
        ):
            with self.subTest(prime=expected[0]):
                receipt = replay.replay_q_one_phase_root_math_v1(
                    bundle["source"], bundle["candidate"], bundle["projection"]
                )
                self.assertEqual(
                    (
                        receipt.core_g.prime,
                        receipt.core_g.t,
                        receipt.core_g.x,
                        receipt.full_carrier_root.chart_r,
                        receipt.full_carrier_root.chart_k,
                    ),
                    expected,
                )
                self.assertEqual(receipt.status, "EVIDENCE_ONLY_MATH_REPLAY")
                self.assertEqual(receipt.terminal_authority, "BLOCKED")
                self.assertEqual(receipt.role_authority, "BLOCKED")
                self.assertFalse(receipt.issuance_allowed)
                self.assertFalse(receipt.t5_phase_drop.admission_ticket_issued)

    def test_receipt_is_slotted_frozen_sealed_and_json_round_trips(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        self.assertFalse(hasattr(receipt, "__dict__"))
        with self.assertRaises(FrozenInstanceError):
            receipt.status = "AUTHORIZED"
        mapping = replay.receipt_to_mapping_v1(receipt)
        encoded = json.dumps(bundle, sort_keys=True)
        replayed = replay.replay_bundle_json_v1(encoded)
        self.assertEqual(replayed.digest, receipt.digest)
        self.assertEqual(mapping["digest"], receipt.digest)

    def test_resealed_exact_dataclass_authority_flips_are_rejected(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        for changes in (
            {"terminal_authority": "GRANTED"},
            {"role_authority": "GRANTED"},
            {"issuance_allowed": True},
        ):
            forged = reseal_exact(receipt, **changes)
            with self.subTest(changes=changes), self.assertRaises(
                replay.MathReplayError
            ) as caught:
                replay.receipt_to_mapping_v1(forged)
            self.assertEqual(
                caught.exception.code,
                replay.MathReplayRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            )

        forged_phase = forge_exact(
            receipt.t5_phase_drop, admission_ticket_issued=True
        )
        forged = reseal_exact(receipt, t5_phase_drop=forged_phase)
        with self.assertRaises(replay.MathReplayError) as caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            caught.exception.code,
            replay.MathReplayRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
        )

    def test_resealed_string_subclass_authority_spoof_is_rejected(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        spoof = SpoofedBlockedAuthority()
        self.assertEqual(spoof, "BLOCKED")
        self.assertEqual(str(spoof), "GRANTED")
        forged = reseal_exact(receipt, terminal_authority=spoof)
        with self.assertRaises(replay.MathReplayError) as caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            caught.exception.code,
            replay.MathReplayRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
        )

    def test_resealed_string_subclass_status_and_nested_spoofs_are_rejected(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        status_spoof = SpoofedExpectedText(
            "AUTHORIZED", "EVIDENCE_ONLY_MATH_REPLAY"
        )
        forged = reseal_exact(receipt, status=status_spoof)
        with self.assertRaises(replay.MathReplayError) as status_caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            status_caught.exception.code,
            replay.MathReplayRejectCode.MALFORMED_RECEIPT,
        )

        phase_spoof = SpoofedExpectedText("GENERIC_MARKED", "TYPEI")
        forged_projection = forge_exact(
            receipt.canonical_projection,
            target_phase=phase_spoof,
        )
        forged = reseal_exact(receipt, canonical_projection=forged_projection)
        with self.assertRaises(replay.MathReplayError) as nested_caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            nested_caught.exception.code,
            replay.MathReplayRejectCode.PROJECTION_MISMATCH,
        )

    def test_resealed_int_subclass_projection_tuple_spoofs_are_rejected(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        forged_values = (
            {
                "equation_target": (
                    SpoofedExpectedInt(5, 4),
                    73,
                )
            },
            {
                "target_chart": (
                    SpoofedExpectedInt(999, 51),
                    931,
                )
            },
        )
        for changes in forged_values:
            forged_projection = forge_exact(
                receipt.canonical_projection,
                **changes,
            )
            forged = reseal_exact(
                receipt,
                canonical_projection=forged_projection,
            )
            with self.subTest(changes=changes), self.assertRaises(
                replay.MathReplayError
            ) as caught:
                replay.receipt_to_mapping_v1(forged)
            self.assertEqual(
                caught.exception.code,
                replay.MathReplayRejectCode.PROJECTION_MISMATCH,
            )

    def test_resealed_exact_dataclass_math_and_type_flips_are_rejected(self):
        bundle = valid_bundle_73()
        receipt = replay.replay_q_one_phase_root_math_v1(
            bundle["source"], bundle["candidate"], bundle["projection"]
        )
        forged_root = forge_exact(receipt.full_carrier_root, chart_k=932)
        forged = reseal_exact(receipt, full_carrier_root=forged_root)
        with self.assertRaises(replay.MathReplayError) as math_caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            math_caught.exception.code,
            replay.MathReplayRejectCode.LOW_CHART_UNIQUENESS_MISMATCH,
        )

        forged_projection = forge_exact(
            receipt.canonical_projection,
            expected_branch_target_type="global_exclusive_owner",
        )
        forged = reseal_exact(receipt, canonical_projection=forged_projection)
        with self.assertRaises(replay.MathReplayError) as type_caught:
            replay.receipt_to_mapping_v1(forged)
        self.assertEqual(
            type_caught.exception.code,
            replay.MathReplayRejectCode.PROJECTION_MISMATCH,
        )

    def test_module_is_independent_of_runtime_and_historical_reproductions(self):
        module_path = SCRIPTS / "t6_q_one_phase_root_independent_math_replay_v1.py"
        tree = ast.parse(module_path.read_text(encoding="utf-8"))
        imported: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module)
        forbidden = {
            "t6_q_one_full_carrier_runtime_slice_v1",
            "type_ii_q_one_full_carrier_phase_root_entry",
            "type_ii_q_one_type_i_carrier_rail_dispatch",
            "t6_persistent_selector_runtime_v1",
            "t6_persistent_selector_state_v1",
        }
        self.assertTrue(imported.isdisjoint(forbidden))
        self.assertTrue(all(not name.startswith("reproductions") for name in imported))

    def test_p_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["candidate"]["root_context"] = 76129
        self.assert_reject(replay.MathReplayRejectCode.CROSS_ARTIFACT_MISMATCH, bundle)

    def test_g_factorization_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["source"]["factorization"] = [[7, 1], [2719, 1]]
        self.assert_reject(replay.MathReplayRejectCode.NOT_Q_ONE_G, bundle)

    def test_root_parameter_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["candidate"]["t"] = 4
        self.assert_reject(replay.MathReplayRejectCode.ROOT_FORMULA_MISMATCH, bundle)

    def test_valid_non_full_carrier_chart_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["candidate"]["chart_r"] = 3
        bundle["candidate"]["chart_k"] = 55
        bundle["projection"]["chart_r"] = 3
        bundle["projection"]["chart_k"] = 55
        self.assert_reject(replay.MathReplayRejectCode.CHART_IDENTITY_MISMATCH, bundle)

    def test_fresh_source_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["candidate"]["source_v"] = 3863800511
        self.assert_reject(replay.MathReplayRejectCode.FRESH_SOURCE_MISMATCH, bundle)

    def test_mark_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["projection"]["mark_equation_rank"] = 72
        self.assert_reject(replay.MathReplayRejectCode.MARK_MISMATCH, bundle)

    def test_potential_swap_is_rejected(self):
        bundle = valid_bundle_73()
        source_coordinates = bundle["projection"]["source_t5_coordinates"]
        bundle["projection"]["source_t5_coordinates"] = bundle["projection"][
            "target_t5_coordinates"
        ]
        bundle["projection"]["target_t5_coordinates"] = source_coordinates
        self.assert_reject(replay.MathReplayRejectCode.POTENTIAL_MISMATCH, bundle)

    def test_fake_g_label_with_2_mod_3_prime_factor_is_rejected(self):
        bundle = valid_bundle_73()
        source = bundle["source"]
        source.update(
            {
                "root_context": 97,
                "equation_rank": 97,
                "equation_denominator": 97,
                "u": 24,
                "x": 25,
                "mark_root_context": 97,
                "mark_equation_rank": 97,
                "factorization": [[5, 2]],
            }
        )
        bundle["candidate"].update(
            {
                "root_context": 97,
                "t": 4,
                "x": 25,
                "chart_r": 67,
                "chart_k": 1675,
                "support_a": 1,
                "source_u": 97,
                "source_v": 6335,
                "source_m": 96,
                "edge_prime": 97,
                "anchor_v": 66,
            }
        )
        bundle["projection"].update(
            {
                "root_context": 97,
                "equation_rank": 97,
                "equation_denominator": 97,
                "mark_root_context": 97,
                "mark_equation_rank": 97,
                "chart_r": 67,
                "chart_k": 1675,
                "source_t5_coordinates": [97, 3, 0, 0, 0, 0, 0],
                "target_t5_coordinates": [97, 2, 4, 2304, 1675, 0, 0],
            }
        )
        self.assert_reject(replay.MathReplayRejectCode.NOT_Q_ONE_G, bundle)

    def test_source_and_target_branch_type_swaps_are_rejected(self):
        for side in ("source", "projection"):
            bundle = valid_bundle_73()
            bundle[side]["declared_branch_type_code"] = 99
            with self.subTest(side=side):
                self.assert_reject(replay.MathReplayRejectCode.OWNER_MISMATCH, bundle)

    def test_projection_type_swap_is_rejected(self):
        bundle = valid_bundle_73()
        bundle["projection"]["type_i_protocol_code"] = 0
        self.assert_reject(replay.MathReplayRejectCode.PROJECTION_MISMATCH, bundle)

    def test_boolean_float_duplicate_and_authority_injections_fail_closed(self):
        for mutation, expected in (
            (("source", "q", True), replay.MathReplayRejectCode.MALFORMED_INTEGER),
            (("candidate", "t", 3.0), replay.MathReplayRejectCode.MALFORMED_INTEGER),
            (
                ("projection", "source_t5_coordinates", [73, True, 0, 0, 0, 0, 0]),
                replay.MathReplayRejectCode.POTENTIAL_MISMATCH,
            ),
        ):
            bundle = valid_bundle_73()
            section, key, value = mutation
            bundle[section][key] = value
            with self.subTest(section=section, key=key):
                self.assert_reject(expected, bundle)

        bundle = valid_bundle_73()
        bundle["projection"]["issuance_allowed"] = 1
        self.assert_reject(replay.MathReplayRejectCode.FIELD_SET_MISMATCH, bundle)

        with self.assertRaises(replay.MathReplayError) as duplicate:
            replay.replay_bundle_json_v1(
                '{"source":{},"source":{},"candidate":{},"projection":{}}'
            )
        self.assertEqual(
            duplicate.exception.code, replay.MathReplayRejectCode.FIELD_SET_MISMATCH
        )

    def test_direct_dict_string_subclass_key_spoof_is_rejected(self):
        bundle = valid_bundle_73()
        source = bundle["source"]
        q_value = source.pop("q")
        source[SpoofedExpectedKey("evil_q", "q")] = q_value
        self.assert_reject(replay.MathReplayRejectCode.FIELD_SET_MISMATCH, bundle)


if __name__ == "__main__":
    unittest.main()
