from __future__ import annotations

import ast
import copy
from dataclasses import replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_q_one_priority_prefix_coverage_verifier_v1 as coverage  # noqa: E402
import t6_q_one_priority_prefix_scheduler_v1 as scheduler  # noqa: E402


def raw_domain(prime: int, factors: list[list[int]]) -> dict[str, object]:
    return {
        "schema_id": "q1_priority_prefix_domain_v1",
        "schema_version": 1,
        "root_context": prime,
        "equation_rank": prime,
        "equation_numerator": 4,
        "equation_denominator": prime,
        "q": 1,
        "gap_three_x": (prime + 3) // 4,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "mark_root_context": prime,
        "mark_equation_rank": prime,
        "gap_three_factorization": factors,
    }


DOMAINS = {
    73: raw_domain(73, [[19, 1]]),
    1_201: raw_domain(1_201, [[7, 1], [43, 1]]),
    2_521: raw_domain(2_521, [[631, 1]]),
    241_441: raw_domain(241_441, [[7, 1], [8_623, 1]]),
}


def digest(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def reseal_scan(scan: dict[str, object]) -> None:
    unsigned = {key: value for key, value in scan.items() if key != "scan_digest"}
    scan["scan_digest"] = digest(unsigned)


def reseal_outer(evidence: dict[str, object]) -> None:
    unsigned = {key: value for key, value in evidence.items() if key != "digest"}
    evidence["digest"] = digest(unsigned)


def evidence_mapping(prime: int) -> dict[str, object]:
    evidence = scheduler.replay_q_one_priority_prefix_v1(
        copy.deepcopy(DOMAINS[prime])
    )
    return scheduler.evidence_to_mapping_v1(evidence)


class QOnePriorityPrefixIndependentEvidenceTests(unittest.TestCase):
    def assert_verifier_rejects(
        self,
        domain: dict[str, object],
        evidence: dict[str, object],
        code: coverage.PrefixCoverageRejectCode,
    ) -> None:
        with self.assertRaises(coverage.PrefixCoverageVerificationError) as caught:
            coverage.verify_q_one_priority_prefix_coverage_v1(domain, evidence)
        self.assertEqual(caught.exception.code, code)

    def test_hit_and_miss_controls_cross_independent_boundary(self):
        expected = {
            73: scheduler.ROOT_TERMINAL_HIT,
            1_201: scheduler.PREFIX_MISS_EVIDENCE_ONLY,
            2_521: scheduler.PREFIX_MISS_EVIDENCE_ONLY,
            241_441: scheduler.ROOT_TERMINAL_HIT,
        }
        for prime, status in expected.items():
            with self.subTest(prime=prime):
                mapping = evidence_mapping(prime)
                result = coverage.verify_q_one_priority_prefix_coverage_v1(
                    copy.deepcopy(DOMAINS[prime]), mapping
                )
                self.assertEqual(mapping["status"], status)
                self.assertEqual(result.outcome, status)
                self.assertFalse(result.global_exhaustion)
                self.assertEqual(result.terminal_authority, "BLOCKED")
                self.assertEqual(result.role_authority, "BLOCKED")
                self.assertFalse(result.issuance_allowed)

    def test_p73_selects_gap_seven_type_ii_d_one(self):
        mapping = evidence_mapping(73)
        self.assertEqual(
            mapping["selected_terminal"],
            {
                "certificate_type": "TYPE_II",
                "gap": 7,
                "x": 20,
                "divisor": 1,
                "y": 219,
                "z": 4_380,
                "candidate_index": 1,
            },
        )

    def test_p241441_natural_selection_and_historical_d1083_both_replay(self):
        mapping = evidence_mapping(241_441)
        selected = mapping["selected_terminal"]
        self.assertEqual(
            (selected["gap"], selected["certificate_type"], selected["divisor"]),
            (11, "TYPE_II", 27),
        )
        gap_eleven = mapping["gap_scans"][2]
        matches = {
            (item["certificate_type"], item["divisor"])
            for item in gap_eleven["matching_certificates"]
        }
        self.assertIn(("TYPE_II", 1_083), matches)
        historical = next(
            item
            for item in gap_eleven["matching_certificates"]
            if item["certificate_type"] == "TYPE_II"
            and item["divisor"] == 1_083
        )
        self.assertEqual(
            Fraction(1, historical["x"])
            + Fraction(1, historical["y"])
            + Fraction(1, historical["z"]),
            Fraction(4, 241_441),
        )

    def test_p1201_prefix_miss_has_explicit_global_gap23_boundary(self):
        mapping = evidence_mapping(1_201)
        self.assertEqual(mapping["status"], "PREFIX_MISS_EVIDENCE_ONLY")
        self.assertTrue(
            all(scan["scan_status"] == "GAP_PREFIX_MISS" for scan in mapping["gap_scans"])
        )

        prime, gap, x, divisor = 1_201, 23, 306, 34
        self.assertEqual(x * x % divisor, 0)
        self.assertEqual((prime * x + divisor) % gap, 0)
        y = (prime * x + divisor) // gap
        z = prime * (x + prime * x * x // divisor) // gap
        self.assertEqual((y, z), (15_980, 172_727_820))
        self.assertEqual(
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z),
            Fraction(4, prime),
        )
        self.assertFalse(mapping["global_exhaustion"])
        self.assertEqual(mapping["next_unchecked_gap"], 15)

    def test_scheduler_and_verifier_do_not_import_each_other_or_old_engines(self):
        paths = (
            SCRIPTS / "t6_q_one_priority_prefix_scheduler_v1.py",
            SCRIPTS / "t6_q_one_priority_prefix_coverage_verifier_v1.py",
        )
        imported_by_file: list[set[str]] = []
        for path in paths:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            imported: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.update(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported.add(node.module)
            imported_by_file.append(imported)
            self.assertTrue(
                all(
                    "runtime" not in name and not name.startswith("reproductions")
                    for name in imported
                )
            )
        self.assertNotIn(
            "t6_q_one_priority_prefix_coverage_verifier_v1",
            imported_by_file[0],
        )
        self.assertNotIn(
            "t6_q_one_priority_prefix_scheduler_v1",
            imported_by_file[1],
        )

    def test_gap_and_candidate_order_swaps_are_rejected_after_reseal(self):
        for field, value, code in (
            (
                "ordered_gaps",
                [3, 11, 7],
                coverage.PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
            ),
            (
                "candidate_order",
                "gap_ascending_type_II_before_I",
                coverage.PrefixCoverageRejectCode.CANDIDATE_ORDER_MISMATCH,
            ),
        ):
            evidence = evidence_mapping(1_201)
            evidence[field] = value
            reseal_outer(evidence)
            with self.subTest(field=field):
                self.assert_verifier_rejects(DOMAINS[1_201], evidence, code)

        evidence = evidence_mapping(1_201)
        scan = evidence["gap_scans"][0]
        scan["gap"] = 7
        reseal_scan(scan)
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
        )

    def test_divisor_and_factorization_swaps_are_rejected_after_reseal(self):
        evidence = evidence_mapping(1_201)
        scan = evidence["gap_scans"][1]
        scan["divisor_universe"][0] = 2
        reseal_scan(scan)
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.DIVISOR_UNIVERSE_MISMATCH,
        )

        evidence = evidence_mapping(1_201)
        scan = evidence["gap_scans"][2]
        scan["factorization"] = [[3, 1], [101, 2]]
        reseal_scan(scan)
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.FACTORIZATION_MISMATCH,
        )

    def test_domain_scope_and_global_flag_swaps_are_rejected_after_reseal(self):
        evidence = evidence_mapping(1_201)
        self.assert_verifier_rejects(
            DOMAINS[2_521],
            evidence,
            coverage.PrefixCoverageRejectCode.DOMAIN_BINDING_MISMATCH,
        )

        evidence = evidence_mapping(1_201)
        evidence["coverage_scope"] = "TERMINAL_UNIVERSE_COMPLETE"
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.SCHEDULE_SCOPE_MISMATCH,
        )

        evidence = evidence_mapping(1_201)
        evidence["global_exhaustion"] = True
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.GLOBAL_EXHAUSTION_FORBIDDEN,
        )

    def test_selected_divisor_and_scan_order_swaps_are_rejected(self):
        evidence = evidence_mapping(73)
        evidence["selected_terminal"]["divisor"] = 2
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[73],
            evidence,
            coverage.PrefixCoverageRejectCode.SELECTED_TERMINAL_MISMATCH,
        )

        evidence = evidence_mapping(1_201)
        evidence["gap_scans"][1], evidence["gap_scans"][2] = (
            evidence["gap_scans"][2],
            evidence["gap_scans"][1],
        )
        reseal_outer(evidence)
        self.assert_verifier_rejects(
            DOMAINS[1_201],
            evidence,
            coverage.PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
        )

    def test_raw_domain_factor_and_schedule_miss_injection_are_rejected(self):
        domain = copy.deepcopy(DOMAINS[73])
        domain["gap_three_factorization"] = [[7, 1], [2_719, 1]]
        with self.assertRaises(scheduler.PriorityPrefixError):
            scheduler.replay_q_one_priority_prefix_v1(domain)

        domain = copy.deepcopy(DOMAINS[73])
        domain["schedule_miss"] = 1
        with self.assertRaises(scheduler.PriorityPrefixError) as caught:
            scheduler.replay_q_one_priority_prefix_v1(domain)
        self.assertEqual(
            caught.exception.code,
            scheduler.PriorityPrefixRejectCode.FIELD_SET_MISMATCH,
        )

        valid = scheduler.replay_q_one_priority_prefix_v1(
            copy.deepcopy(DOMAINS[73])
        )
        with self.assertRaises(scheduler.PriorityPrefixError):
            scheduler.evidence_to_mapping_v1(replace(valid, schema_version=True))


if __name__ == "__main__":
    unittest.main()
