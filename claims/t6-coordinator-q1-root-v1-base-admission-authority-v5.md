---
kind: claim
claim_id: t6-coordinator-q1-root-v1-base-admission-authority-v5
title: q=1 root 的 V1 base admission exact-HEAD authority v5
statement: >-
  Subject to the reviewed repository-selected exact-commit trust condition,
  V5 is an exact-HEAD, no-queue authority for one actual ordinary q=1 G root
  after a V3 registered-prefix MISS and independently replayed V4 owner and
  scope evidence. It grants only Q1_ROOT_V1_BASE_MATERIALIZER and
  INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER. The materialized V1 state
  and semantic-origin preimage exclude every V4 E1/candidate field. A final
  receipt may set persistent_admission and v1_base_owner authority true, but
  queue/enqueue, successor, producer, E1-E5, T5, global and terminal-leaf
  authority remain false.
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - v1-base-admission
  - exact-head
  - proof-boundary
sources:
  - data: data/t6-wave1/t6-coordinator-role-registry-v5.json
    role: V5 exact-HEAD grants and no-queue denials
  - source: schemas/t6-coordinator-role-registry-v5.schema.json
    role: V5 registry source schema
  - source: schemas/t6-q-one-root-v1-base-admission-v1.schema.json
    role: normative V1 base receipt wire schema
  - source: scripts/t6_q_one_root_v1_base_materializer_v1.py
    role: canonical non-admitting V1 root materializer
  - source: scripts/t6_q_one_root_v1_base_admission_verifier_v1.py
    role: independent V1 gate and owner-reanchor verifier
  - reproduction: scripts/t6_coordinator_role_registry_v5.py
    role: exact-HEAD registry and V3/V4 cross binding
  - reproduction: scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py
    role: controlled exact-HEAD assembly
  - reproduction: scripts/t6_q_one_root_v1_base_admission_receipt_verifier_v1.py
    role: independent exact-HEAD wire replay
  - reproduction: tests/test_t6_q_one_root_v1_base_admission_roles_v1.py
    role: role-level semantic and coherent-reseal controls
  - reproduction: tests/test_t6_coordinator_role_registry_v5.py
    role: registry pin, trust-before-exec and fail-closed controls
  - reproduction: tests/test_t6_q_one_root_v1_base_admission_orchestrator_v1.py
    role: exact-HEAD integration and Git-environment controls
  - review: docs/audits/T6_Q1_ROOT_V1_BASE_ADMISSION_CONDITIONAL_REVIEW_2026-08-27.md
    role: conditional authority review and external commit-trust boundary
visibility: public
last_checked: '2026-08-27'
---

# V5 Boundary

V5 does not consume a V4 consumer/E1 receipt. It independently reconstructs
only the V4 owner and registered-prefix scope receipts from the same exact-HEAD
raw source and V3 production MISS. The materializer therefore creates a V1
`ROOT_INITIALIZER_OUTPUT` state from base source and terminal data alone.

The final V5 admission receipt may establish the narrow V1 base owner and
`persistent_admission=true`; it is not a queue operation. Its exact denials are:

```text
queue / enqueue / successor             = false
producer / continuation / branch         = false
E1 / E2 / E3 / E4 / E5 / T5             = false
global exhaustion / terminal leaf        = false
```

The V5 orchestrator derives V5 and V4 grants from exact-HEAD registry manifests.
Caller-supplied grants, owner/scope receipts, V4 E1 candidates, state wires,
queue tokens and authority booleans are not accepted. The independent replay
rebuilds the full expected wire without importing or invoking the orchestrator.

V5 binds execution to a reviewed, repository-selected full commit ID and rejects
worktree drift, Git replace objects, inherited Git routing variables, and pin
drift within that selected tree. It does not authenticate an arbitrary
caller-selected commit as an external trust root: a commit that changes both a
role artifact and its registry pins is a new authority policy and requires a
fresh review or an external immutable/signed anchor before use.

This does not close Gate 2 or Gate 4, produce a persistent queue entry, prove a
successor transition, establish E1-E5, or advance T6 beyond this single base
admission boundary. A new exact-HEAD/pin/resolver policy requires fresh review.
