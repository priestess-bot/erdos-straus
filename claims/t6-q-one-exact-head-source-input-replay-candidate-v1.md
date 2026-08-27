---
kind: claim
claim_id: t6-q-one-exact-head-source-input-replay-candidate-v1
title: q=1 source-input 的 exact-HEAD replay candidate V1
statement: >-
  For a reviewed repository-selected exact HEAD and raw ordinary q=1 G input
  whose V3 outcome is the registered-prefix MISS, the V6 candidate pipeline
  fresh-replays V3, V4, V5, and V6, constructs an exact source-input replay
  candidate and its non-E1 V2 external-binding projection, and an independent
  replayer reconstructs identical wires. Every serializable marker for source
  actualness, V1 base-admission evidence, V6 rebind evidence, generic or
  successor E1, producer, admission, queue, E2--E5, T5, re-entry, and global
  exhaustion is false. The runtime result authority_verified=true only reports
  successful independent replay; it is not a serialized grant.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - t6-coordinator-q1-root-v1-base-admission-authority-v5
  - t6-coordinator-q1-root-source-scoped-e1-rebind-v1
  - t6-q-one-phase-root-prestate-v2-nonauthorizing-construction
topics:
  - T6
  - q-one
  - exact-head
  - source-replay
  - replay-candidate
  - proof-boundary
sources:
  - source: data/t6-wave1/t6-coordinator-role-registry-v6.json
    role: candidate-only role policy and authority denials
  - source: schemas/t6-q-one-exact-head-source-input-v1.schema.json
    role: closed-world candidate wire schema
  - source: scripts/t6_coordinator_role_registry_v6.py
    role: exact-tree registry resolver
  - source: scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py
    role: controlled exact-HEAD candidate construction
  - source: scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py
    role: independent exact-HEAD wire reconstruction
  - reproduction: tests/test_t6_q_one_exact_head_source_input_v1.py
    role: isolated positive and negative replay controls
visibility: public
last_checked: '2026-08-27'
---

# q=1 Exact-HEAD Source Replay Candidate

## Candidate Pipeline

For a raw ordinary q=1 G input, the controlled exact-HEAD path performs

~~~text
V3 prefix-MISS replay
-> V4 scoped source occurrence replay
-> V5 V1 base-admission replay
-> V6 source-rebind replay
-> source-input replay candidate
-> non-E1 ExternalQOneSourceBindingV2 projection.
~~~

The V6 resolver reads the requested Git tree, binds every role artifact to its
tracked blob and matching worktree bytes, checks V3/V4/V5 cross-registry
digests, and rejects worktree drift. The independent replayer uses separately
fresh-loaded modules and does not import or invoke the controlled orchestrator
or V3 issuer.

The positive isolated control is \(p=1201\), where the replayer reconstructs
the same candidate and V2 binding wire. A V3 terminal HIT at \(p=73\)
preempts the chain before V4/V5/V6 construction.

## Non-Authority Invariant

Every serialized candidate, including a locally self-resealed one, has:

~~~text
source_actualness_input=false
v1_base_admission_evidence=false
v6_rebind_evidence=false
generic_e1=false
successor_e1=false
e1_authority=false
producer/admission/queue=false
E2/E3/E4/E5/T5/re-entry/global_exhaustion=false.
~~~

The schema is closed-world and the public parser and public V2 projection
reject candidate wires. The independent replayer may return
authority_verified=true as a runtime result after completing its own
exact-HEAD reconstruction. That result is not a serializable capability, so a
future consumer must invoke the replayer itself rather than trust any wire
field.

## Boundary

This claim establishes reproducible candidate evidence only. It does not
authenticate a source for downstream use, establish actual E1, issue a
producer or branch, admit a state, mutate a queue, prove E2--E5, or change
F1/F2/F3/T6 status. The selected-commit external trust condition for V5/V6
also remains separate from this replay result.
