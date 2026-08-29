from __future__ import annotations

import ast
import copy
import importlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

selector = importlib.import_module("t6_sp21_q1_p21169_concrete_selector_v1")
replayer = importlib.import_module("t6_sp21_q1_p21169_independent_replayer_v1")

DATA = ROOT / "data/t6-sp21-q1-p21169"
POLICY_PATH = DATA / "sp21-policy-registry-v1.json"
LOCK_PATH = DATA / "sp21-artifact-lock-v1.json"
AUTHORITY_PATH = DATA / "sp21-external-authority-anchor-v1.json"
EVIDENCE_PATH = ROOT / "reproductions/sp21_q1_p21169_concrete_selector_v1/evidence-v1.json"


class ConcreteSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.policy = selector.load_policy(POLICY_PATH)
        cls.lock = selector.load_artifact_lock(LOCK_PATH)
        cls.authority = selector.load_and_verify_authority(
            AUTHORITY_PATH, policy=cls.policy, artifact_lock=cls.lock
        )
        cls.evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    def _verify_tampered_evidence_fails(self, mutate) -> None:
        value = copy.deepcopy(self.evidence)
        mutate(value)
        value["evidence_id"] = replayer.digest_json(
            {key: child for key, child in value.items() if key != "evidence_id"}
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "tampered.json"
            path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")
            with self.assertRaises(replayer.ReplayFailure):
                replayer.verify_evidence(
                    repo_root=ROOT,
                    policy_path=POLICY_PATH,
                    lock_path=LOCK_PATH,
                    authority_path=AUTHORITY_PATH,
                    evidence_path=path,
                )

    def test_01_signed_policy_and_artifact_lock(self) -> None:
        receipt = selector.verify_artifact_lock(self.lock, ROOT)
        self.assertTrue(receipt["all_locked_artifacts_match"])
        self.assertEqual(
            self.authority.key_fingerprint, selector.TRUSTED_AUTHORITY_KEY_SHA256
        )
        self.assertFalse(
            self.policy.payload["authority_contract"]["producer_may_issue_or_mutate_policy"]
        )
        self.assertFalse(
            self.policy.payload["authority_contract"]["caller_boolean_is_authority"]
        )

    def test_02_policy_order_overlap_and_no_reject(self) -> None:
        receipt = selector.verify_policy_static(self.policy.payload)
        self.assertEqual(receipt["prior_terminal_indices"], [0, 1, 2, 3, 4, 5])
        self.assertEqual(receipt["later_terminal_indices"], [7])
        self.assertEqual(receipt["reject_action_count"], 0)
        self.assertTrue(receipt["overlap_partition_complete"])
        rows = self.policy.payload["priority_overlap_proof"]["rows"]
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(row["guard_overlap"] for row in rows))

    def test_03_universal_actual_source_local_totality(self) -> None:
        theorem = selector.prove_universal_local_totality(self.policy)
        self.assertTrue(theorem["every_valid_actual_source_decided"])
        self.assertEqual(
            theorem["domain_quantifier"],
            "FOR_EVERY_P_SATISFYING_SIGNED_DOMAIN_PREDICATE",
        )
        self.assertEqual(theorem["reject_result_count_on_valid_domain"], 0)
        self.assertEqual(theorem["fallthrough_result_count_on_valid_domain"], 0)
        self.assertTrue(all(theorem["checks"].values()))
        witnesses, results = selector.execute_regression_witnesses(
            self.policy, self.authority
        )
        self.assertTrue(witnesses["not_the_basis_of_universal_totality"])
        self.assertEqual(results[73]["selected_action_index"], 1)
        self.assertEqual(results[193]["selected_action_index"], 1)
        self.assertEqual(results[1201]["selected_action_index"], 5)
        self.assertEqual(results[2521]["selected_action_index"], 5)
        self.assertEqual(results[12721]["selected_action_index"], 4)
        self.assertEqual(results[21169]["selected_action_index"], 6)

    def test_04_terminal_preemption_controls(self) -> None:
        expected = {
            1201: (23, "TYPE_I", 34),
            2521: (23, "TYPE_II", 8),
            12721: (19, "TYPE_II", 7),
        }
        for p, (gap, family, d) in expected.items():
            result = selector.run_selector_for_p(
                policy=self.policy, authority=self.authority, p=p
            )
            self.assertEqual(result["result_kind"], "TERMINAL")
            certificate = result["terminal_certificate"]
            self.assertEqual(certificate["family"], family)
            self.assertEqual(certificate["d"], d)
            self.assertEqual(result["selector_trace"][-1]["output"]["gap"], gap)
            self.assertTrue(selector.verify_unit_fraction_certificate(p, certificate["triple"]))

    def test_05_p21169_complete_prior_clearance(self) -> None:
        execution = self.evidence["p21169_execution"]
        prior = execution["selector_trace"][:6]
        self.assertEqual([row["action_index"] for row in prior], list(range(6)))
        self.assertTrue(all(row["output"]["outcome"] == "MISS" for row in prior))
        clearance = execution["clearance_receipt"]
        self.assertEqual(
            clearance["semantic"], "MISS_HIGHER_PRIORITY_POLICY_COMPLETE"
        )
        self.assertEqual(clearance["coverage"], "REGISTERED_HIGHER_PRIORITY_ONLY")
        self.assertFalse(clearance["global_exhaustion"])
        self.assertEqual(clearance["covered_action_indices"], list(range(6)))

    def test_06_p21169_actual_source_and_e1_binding(self) -> None:
        execution = self.evidence["p21169_execution"]
        source = execution["actual_source_receipt"]
        e1 = execution["edge_bundle"]["E1"]
        self.assertTrue(source["source_actualness"])
        self.assertTrue(source["source_admitted"])
        self.assertTrue(source["domain_membership_verified"])
        self.assertEqual(
            source["root_admission_status"],
            "EXTERNAL_COORDINATOR_ROOT_ADMISSION_VERIFIED",
        )
        self.assertEqual(source["occurrence_path"], ["arithmetic", "q"])
        self.assertEqual(source["occurrence_value"], 1)
        self.assertEqual(e1["source_state_id"], source["source_state_id"])
        self.assertEqual(e1["actual_source_receipt_id"], source["receipt_id"])
        self.assertEqual(e1["policy_payload_sha256"], self.policy.payload_sha256)
        self.assertEqual(e1["selected_branch_index"], 6)
        self.assertEqual(e1["selected_branch_id"], "q1_phase_root_producer_v1")

    def test_07_projection_e2_and_phase_root_arithmetic(self) -> None:
        execution = self.evidence["p21169_execution"]
        projection = execution["projection"]
        e2 = execution["edge_bundle"]["E2"]
        self.assertEqual(projection["R"], 14115)
        self.assertEqual(projection["K"], 74700109)
        self.assertEqual(4 * projection["K"], 21169 * projection["R"] + 1)
        self.assertTrue(e2["projection_unique"])
        self.assertFalse(e2["caller_supplied_tie_break"])
        with self.assertRaises(TypeError):
            selector.project_phase_root(
                execution["actual_source_receipt"]["source_state_wire"], 17
            )

    def test_08_target_subject_replay_is_independent(self) -> None:
        execution = self.evidence["p21169_execution"]
        source_subject = execution["actual_source_receipt"]["source_state_id"]
        projection_subject = execution["projection"]["projection_id"]
        target_receipt = execution["target_terminal_receipt"]
        self.assertEqual(
            target_receipt["outcome"], "MISS_REGISTERED_TARGET_PRIORITY_COMPLETE"
        )
        self.assertFalse(target_receipt["global_exhaustion"])
        for row in target_receipt["records"]:
            self.assertEqual(row["subject_kind"], "TARGET_PROJECTION")
            self.assertEqual(row["subject_id"], projection_subject)
            self.assertNotEqual(row["subject_id"], source_subject)
        self.assertEqual(target_receipt["records"][-1]["output"]["gcd_R_minus_1_K"], 1)

    def test_09_e3_acyclic_prestate_and_owner(self) -> None:
        execution = self.evidence["p21169_execution"]
        prestate = execution["target_prestate"]
        for forbidden in (
            "owner",
            "owner_digest",
            "edge_bundle",
            "bundle_id",
            "admission",
            "admission_id",
        ):
            self.assertNotIn(forbidden, prestate)
        self.assertEqual(replayer.digest_json(prestate), execution["target_state_id"])
        owner = execution["owner_receipt"]
        self.assertEqual(owner["target_state_id"], execution["target_state_id"])
        self.assertEqual(owner["owner_id"], "type_i_full_carrier_post_g")
        self.assertTrue(owner["owner_recomputed_not_inherited"])

    def test_10_universal_e4_and_frozen_e5(self) -> None:
        execution = self.evidence["p21169_execution"]
        e4 = execution["edge_bundle"]["E4"]
        e5 = execution["edge_bundle"]["E5"]
        self.assertEqual(e4["source_equation"], e4["target_equation"])
        self.assertTrue(e4["universal_quantifier"])
        self.assertEqual(e4["lift_id"], "IDENTITY_ON_POSITIVE_INTEGER_TRIPLES_V1")
        self.assertEqual(e5["source_potential"], [21169, 3, 0, 0, 0, 0, 0])
        self.assertEqual(
            e5["target_potential"],
            [21169, 2, 4, 112021056, 74700109, 0, 0],
        )
        self.assertLess(tuple(e5["target_potential"]), tuple(e5["source_potential"]))
        self.assertEqual(e5["ticket_kind"], "PHASE_DROP")

    def test_11_common_admission_unique_ingress_and_reentry(self) -> None:
        execution = self.evidence["p21169_execution"]
        sidecar = execution["admission_sidecar"]
        reentry = execution["reentry_receipt"]
        trace = execution["runtime_trace"]
        self.assertTrue(sidecar["admitted"])
        self.assertEqual(
            sidecar["unique_queue_writer_id"],
            "unique_persistent_queue_ingress_sp21_v1",
        )
        self.assertEqual([row["event"] for row in trace], [
            "QUEUE_INGRESS_WRITE",
            "QUEUE_CONSUME_AND_REENTRY",
        ])
        self.assertEqual(reentry["result"], "ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY")
        self.assertFalse(reentry["self_edge_emitted"])
        self.assertFalse(reentry["queue_write_during_reentry"])
        self.assertTrue(execution["queue_empty_after_reentry"])
        self.assertTrue(self.evidence["queue_ingress_audit"]["audit_pass"])

    def test_12_gap31_later_negative_control(self) -> None:
        control = self.evidence["gap31_negative_control"]
        certificate = control["analysis_only_replay_record"]["output"][
            "selected_certificate"
        ]
        self.assertEqual(
            certificate,
            {
                "d": 1,
                "family": "TYPE_II",
                "triple": [5300, 3619899, 19185464700],
            },
        )
        self.assertFalse(control["later_terminal_executed_by_selector"])
        self.assertFalse(control["scope_clearance_global_exhaustion"])
        self.assertFalse(control["miss_complete_claim"])
        self.assertTrue(selector.verify_unit_fraction_certificate(21169, certificate["triple"]))

    def test_13_independent_end_to_end_replayer(self) -> None:
        receipt = replayer.verify_evidence(
            repo_root=ROOT,
            policy_path=POLICY_PATH,
            lock_path=LOCK_PATH,
            authority_path=AUTHORITY_PATH,
            evidence_path=EVIDENCE_PATH,
        )
        self.assertTrue(receipt["all_checks_pass"])
        self.assertFalse(receipt["global_exhaustion_asserted"])
        self.assertTrue(receipt["independent_boundary"]["independent_boundary_pass"])
        self.assertEqual(receipt["independent_boundary"]["repository_local_imports"], [])

    def test_14_policy_reorder_is_rejected(self) -> None:
        payload = copy.deepcopy(self.policy.payload)
        payload["source_policy"]["actions"][5], payload["source_policy"]["actions"][6] = (
            payload["source_policy"]["actions"][6],
            payload["source_policy"]["actions"][5],
        )
        payload["source_policy"]["actions"][5]["index"] = 5
        payload["source_policy"]["actions"][6]["index"] = 6
        with self.assertRaises(selector.ContractError) as caught:
            selector.verify_policy_static(payload)
        self.assertEqual(caught.exception.code, selector.RejectCode.POLICY_INVALID)

    def test_15_overlap_omission_is_rejected(self) -> None:
        payload = copy.deepcopy(self.policy.payload)
        payload["priority_overlap_proof"]["rows"].pop()
        with self.assertRaises(selector.ContractError) as caught:
            selector.verify_policy_static(payload)
        self.assertEqual(caught.exception.code, selector.RejectCode.PRIORITY_OVERLAP_GAP)

    def test_16_signed_authority_rejects_policy_mutation(self) -> None:
        document = copy.deepcopy(self.policy.document)
        document["payload"]["non_claims"] = document["payload"]["non_claims"] + [
            "MUTATED_BUT_STATICALLY_WELL_FORMED"
        ]
        document["payload_sha256"] = selector.digest_json(document["payload"])
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "policy.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            mutated = selector.load_policy(path)
            with self.assertRaises(selector.ContractError) as caught:
                selector.load_and_verify_authority(
                    AUTHORITY_PATH, policy=mutated, artifact_lock=self.lock
                )
            self.assertEqual(
                caught.exception.code, selector.RejectCode.AUTHORITY_SCOPE_MISMATCH
            )

    def test_17_artifact_mutation_breaks_lock(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for row in self.lock.payload["artifacts"]:
                destination = root / row["path"]
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / row["path"], destination)
            victim = root / self.lock.payload["artifacts"][0]["path"]
            victim.write_bytes(victim.read_bytes() + b"\n# mutation\n")
            with self.assertRaises(selector.ContractError) as caught:
                selector.verify_artifact_lock(self.lock, root)
            self.assertEqual(
                caught.exception.code, selector.RejectCode.ARTIFACT_LOCK_MISMATCH
            )

    def test_18_source_swap_is_rejected(self) -> None:
        other = selector.initialize_actual_source(self.policy, self.authority, 1201)
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["edge_bundle"]["E1"].__setitem__(
                "source_state_id", other["source_state_id"]
            )
        )

    def test_19_q_path_swap_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["edge_bundle"]["E1"].__setitem__(
                "occurrence_path", ["arithmetic", "p"]
            )
        )

    def test_20_branch_index_swap_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["edge_bundle"]["E1"].__setitem__(
                "selected_branch_index", 7
            )
        )

    def test_21_scope_miss_cannot_be_globalized(self) -> None:
        def mutate(value) -> None:
            value["p21169_execution"]["clearance_receipt"]["global_exhaustion"] = True
            value["p21169_execution"]["clearance_receipt"]["semantic"] = "MISS_COMPLETE"

        self._verify_tampered_evidence_fails(mutate)

    def test_22_owner_swap_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["owner_receipt"].__setitem__(
                "owner_id", "attacker_owner"
            )
        )

    def test_23_target_bundle_cycle_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["target_prestate"].__setitem__(
                "bundle_id", value["p21169_execution"]["edge_bundle"]["bundle_id"]
            )
        )

    def test_24_t5_drift_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["edge_bundle"]["E5"][
                "target_potential"
            ].__setitem__(1, 3)
        )

    def test_25_queue_bypass_and_duplicate_token_are_rejected(self) -> None:
        with self.assertRaises(selector.ContractError) as caught:
            selector.PersistentPilotRuntime(object(), self.policy, self.authority)
        self.assertEqual(caught.exception.code, selector.RejectCode.QUEUE_BYPASS)

        runtime = selector.PersistentPilotRuntime.open(self.policy, self.authority)
        envelope = {
            "target_state_id": "0" * 64,
            "admission_sidecar": {"queue_token": "1" * 64},
        }
        with self.assertRaises(selector.ContractError) as caught:
            runtime._unique_queue_write_v1(object(), envelope)
        self.assertEqual(caught.exception.code, selector.RejectCode.QUEUE_BYPASS)

        execution = self.evidence["p21169_execution"]
        runtime = selector.PersistentPilotRuntime.open(self.policy, self.authority)
        kwargs = {
            "target_prestate": execution["target_prestate"],
            "target_state_id": execution["target_state_id"],
            "owner": execution["owner_receipt"],
            "target_terminal": execution["target_terminal_receipt"],
            "bundle": execution["edge_bundle"],
        }
        selector.common_admit_v1(runtime, **kwargs)
        with self.assertRaises(selector.ContractError) as caught:
            selector.common_admit_v1(runtime, **kwargs)
        self.assertEqual(caught.exception.code, selector.RejectCode.DUPLICATE_QUEUE_TOKEN)

    def test_26_caller_authority_boolean_is_not_an_api(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            selector.run_selector_for_p(
                policy=self.policy, authority=True, p=21169  # type: ignore[arg-type]
            )

    def test_27_independent_replayer_has_no_local_import(self) -> None:
        path = SCRIPTS / "t6_sp21_q1_p21169_independent_replayer_v1.py"
        tree = ast.parse(path.read_text(encoding="utf-8"))
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names if alias.name.startswith("t6_"))
            elif isinstance(node, ast.ImportFrom) and node.module:
                if node.module.startswith("t6_"):
                    imports.append(node.module)
        self.assertEqual(imports, [])

    def test_28_predicate_domain_is_not_a_finite_fixture(self) -> None:
        domain = self.policy.payload["source_domain"]
        self.assertNotIn("members", domain)
        self.assertEqual(
            domain["closed_world_kind"], "DECIDABLE_PREDICATE_CLOSED_WORLD"
        )
        for p in (73, 21169, 61681, 99961):
            accepted, checks = selector.source_domain_membership(p)
            self.assertTrue(accepted, (p, checks))
        for p in (1, 25, 97, 1202):
            self.assertFalse(selector.source_domain_membership(p)[0])
            with self.assertRaises(selector.ContractError) as caught:
                selector.initialize_actual_source(self.policy, self.authority, p)
            self.assertEqual(caught.exception.code, selector.RejectCode.SOURCE_NOT_AUTHORIZED)

    def test_29_second_nonterminal_source_uses_same_verified_path(self) -> None:
        result = selector.run_selector_for_p(
            policy=self.policy, authority=self.authority, p=61681
        )
        self.assertEqual(result["result_kind"], "VERIFIED_SUCCESSOR")
        self.assertEqual(result["selected_action_index"], 6)
        self.assertTrue(result["edge_bundle"]["all_obligations_verified"])
        self.assertEqual(
            result["reentry_receipt"]["result"],
            "ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY",
        )
        self.assertFalse(result["clearance_receipt"]["global_exhaustion"])

    def test_30_authority_id_is_inside_signed_statement(self) -> None:
        anchor = json.loads(AUTHORITY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(anchor["authority_id"], anchor["statement"]["authority_id"])
        anchor["authority_id"] = "producer_self_declared_authority"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "authority.json"
            path.write_text(json.dumps(anchor), encoding="utf-8")
            with self.assertRaises(selector.ContractError) as caught:
                selector.load_and_verify_authority(
                    path, policy=self.policy, artifact_lock=self.lock
                )
            self.assertEqual(
                caught.exception.code, selector.RejectCode.AUTHORITY_SCOPE_MISMATCH
            )

    def test_31_exact_status_boundary(self) -> None:
        status = self.evidence["status"]
        self.assertEqual(status["SP21"], "ESTABLISHED_SIGNED_Q1_G_POLICY_DOMAIN")
        self.assertEqual(
            status["SP22"],
            "ESTABLISHED_FOR_EVERY_SIGNED_Q1_G_ACTUAL_SOURCE",
        )
        self.assertEqual(status["F1"], "UNCHANGED_OPEN")
        self.assertEqual(status["F2"], "UNCHANGED_OPEN")
        self.assertEqual(status["F3"], "UNCHANGED_OPEN")
        self.assertEqual(status["T6"], "UNCHANGED_OPEN")
        self.assertEqual(status["erdos_straus_conjecture"], "UNCHANGED_OPEN")


    def test_32_bounded_predicate_domain_audit_matches_expected_census(self) -> None:
        audit = selector.bounded_predicate_domain_audit(self.policy)
        self.assertEqual(audit["domain_source_count"], 606)
        self.assertEqual(
            audit["selected_action_counts"],
            {"0": 0, "1": 475, "2": 83, "3": 11, "4": 16, "5": 15, "6": 6},
        )
        self.assertEqual(
            audit["verified_successor_ps"],
            [21169, 61681, 67369, 87481, 94441, 99961],
        )
        self.assertTrue(audit["not_the_basis_of_universal_totality"])

    def test_33_generic_independent_prefix_replayer_never_calls_producer(self) -> None:
        anchor, statement_digest = replayer.verify_authority(
            AUTHORITY_PATH,
            policy_digest=self.policy.payload_sha256,
            lock_digest=self.lock.payload_sha256,
        )
        terminal = replayer.independent_source_prefix_decision(
            policy=self.policy.payload,
            policy_digest=self.policy.payload_sha256,
            authority=anchor,
            statement_digest=statement_digest,
            p=1201,
        )
        self.assertEqual(terminal["result_kind"], "TERMINAL")
        self.assertEqual(terminal["selected_action_index"], 5)
        self.assertFalse(terminal["selected_producer_or_edge_code_called"])
        successor_prefix = replayer.independent_source_prefix_decision(
            policy=self.policy.payload,
            policy_digest=self.policy.payload_sha256,
            authority=anchor,
            statement_digest=statement_digest,
            p=61681,
        )
        self.assertEqual(
            successor_prefix["result_kind"], "SELECTED_PRODUCER_GUARD_TRUE"
        )
        self.assertEqual(successor_prefix["selected_action_index"], 6)
        self.assertFalse(successor_prefix["clearance_receipt"]["global_exhaustion"])
        self.assertFalse(successor_prefix["selected_producer_or_edge_code_called"])

    def test_34_manifest_and_ledgers_use_exact_status_boundary(self) -> None:
        directory = ROOT / "docs/standalone-proof-propositions-2026-08-28"
        manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
        rows = {row["id"]: row for row in manifest["propositions"]}
        self.assertEqual(rows["SP-21"]["status"], "ESTABLISHED")
        self.assertEqual(rows["SP-22"]["status"], "ESTABLISHED")
        self.assertEqual(
            sum(row["status"] == "OPEN_PROPOSITION" for row in rows.values()), 18
        )
        readme = (directory / "README.md").read_text(encoding="utf-8")
        audit = (directory / "SELF-CONTAINED-AUDIT.md").read_text(encoding="utf-8")
        portfolio = (directory / "CURRENT-PROOF-PORTFOLIO-2026-08-29.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("其余 18 个", readme)
        self.assertIn("OPEN_PROPOSITION 总数 | 18", audit)
        self.assertIn("当前 18 个 `OPEN_PROPOSITION`", portfolio)
        for text in (readme, audit, portfolio):
            self.assertIn("T6", text)
            self.assertIn("OPEN", text)


    def test_35_source_target_transcript_subject_swap_is_rejected(self) -> None:
        def mutate(value) -> None:
            source_id = value["p21169_execution"]["actual_source_receipt"]["source_state_id"]
            value["p21169_execution"]["target_terminal_receipt"]["records"][0][
                "subject_id"
            ] = source_id

        self._verify_tampered_evidence_fails(mutate)

    def test_36_single_record_policy_digest_splice_is_rejected(self) -> None:
        self._verify_tampered_evidence_fails(
            lambda value: value["p21169_execution"]["selector_trace"][0].__setitem__(
                "policy_payload_sha256", "f" * 64
            )
        )

    def test_37_authority_public_key_replacement_is_rejected(self) -> None:
        anchor = json.loads(AUTHORITY_PATH.read_text(encoding="utf-8"))
        anchor["public_key"]["e"] = 3
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "authority.json"
            path.write_text(json.dumps(anchor), encoding="utf-8")
            with self.assertRaises(selector.ContractError) as caught:
                selector.load_and_verify_authority(
                    path, policy=self.policy, artifact_lock=self.lock
                )
            self.assertEqual(
                caught.exception.code, selector.RejectCode.AUTHORITY_KEY_MISMATCH
            )


if __name__ == "__main__":
    unittest.main()
