---
kind: claim
claim_id: t6-coordinator-q1-root-prefix-scoped-e1-authority-v4
title: q=1 root registered-prefix MISS 的 scope-aware common-owner 与 source-scoped E1 authority v4
statement: >-
  Coordinator registry v4 is a separate exact-HEAD extension of the frozen V3
  registry.  With every artifact independently pinned, it authorizes exactly
  three loader-free roles:
  COMMON_ROOT_OWNER_CLASSIFIER, INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR and
  REGISTERED_PREFIX_E1_CONSUMER.  The extension is restricted to the ordinary
  parentless q=1 G root after the V3 registered gaps [3,7,11] MISS.  Its only
  authorized E1 result is a ROOT_SOURCE_SCOPED_E1 receipt; it cannot create a
  generic or successor E1, global miss, producer branch, E2-E5 edge, T5 ticket,
  persistent admission, re-entry or queue mutation.  Any placeholder state
  remains fail-closed and cannot produce a V4 role manifest.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
  - T6
  - q-one
  - scope-aware-e1
  - common-owner
  - exact-head
  - proof-boundary
sources:
  - data: data/t6-wave1/t6-coordinator-role-registry-v4.json
    role: HEAD-free V4 source registry and active exact-HEAD authority policy
  - source: schemas/t6-coordinator-role-registry-v4.schema.json
    role: exact V4 source, artifact, receipt and denial schema
  - reproduction: scripts/t6_coordinator_role_registry_v4.py
    role: exact-HEAD V3 cross-binding and fail-closed V4 resolver
  - source: scripts/t6_q_one_root_owner_classifier_v2.py
    role: loader-free common owner classifier
  - source: scripts/t6_q_one_scope_aware_e1_validator_v2.py
    role: loader-free scope-aware E1 validator
  - source: scripts/t6_q_one_registered_prefix_e1_consumer_v2.py
    role: loader-free source-scoped E1 consumer
  - reproduction: scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py
    role: exact-HEAD controlled role orchestration
  - reproduction: scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py
    role: issuer-independent post-issuance wire replay
  - source: schemas/t6-q-one-root-prefix-scoped-e1-v2.schema.json
    role: normative V4 role-receipt schema
  - reproduction: tests/test_t6_coordinator_role_registry_v4.py
    role: registry, pin, authority-matrix and controlled-loader controls
  - reproduction: tests/test_t6_q_one_root_prefix_scoped_e1_roles_v2.py
    role: pure-role mathematical and authority-boundary controls
  - reproduction: tests/test_t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py
    role: exact-HEAD positive and adversarial integration controls
  - review: docs/audits/T6_Q1_ROOT_PREFIX_SCOPED_E1_FINAL_INDEPENDENT_REVIEW_2026-08-26.md
    role: final independent review and explicit proof boundary
visibility: public
last_checked: '2026-08-26'
---

# V4 scope boundary

V4 does not modify or supersede V3.  It consumes only a V3 production receipt
whose exact HEAD, root actualness, schedule and independent replay all match the
same requested commit.  A V3 `ROOT_TERMINAL_HIT` is terminal-first and cannot
enter this extension.  Only `MISS_REGISTERED_PRIORITY_COMPLETE` may reach the
V4 scope, and that result remains:

The active resolved capability count is seven only in the bookkeeping
sense of four inherited V3 roles plus three new V4 roles; it does not create
seven new roles or broaden the V3 terminal authority.

```text
ordered_gaps       = [3, 7, 11]
next_unchecked_gap  = 15
global_exhaustion   = false
```

The owner classifier is deliberately independent of the terminal result.  It
rebuilds the root source chain and classifies the exact normalized owner
`type_ii_relation_g_endpoint`; it cannot infer a terminal miss or issue E1.
Its `owner_digest` must be the bare SHA-256 of the frozen V1
`owner_digest_v1` preimage and `owner_id` must equal `owner:` plus that digest;
the normalized header must pass the actual pinned V1 facts validator and
classifier, not a copied predicate-only approximation.
The scope-aware validator consumes that owner receipt plus the exact V3 MISS and
checks source actualness and scope, but its receipt carries no common-owner
authority.  The consumer combines both independent receipts and is the only
role that may issue the narrow source-scoped E1 result; it cannot obtain that
authority from the validator receipt alone.

All three role modules are loader-free and receive an exact eight-field grant
wire.  The grant digest is recomputed locally; the module itself cannot assert
HEAD authority.  The exact-HEAD orchestrator projects grants from the V4
resolved manifest and the independent post-issuance replayer reconstructs the
complete expected wire.  Local serializers do not authenticate a repository or
cross-chain digest preimage.

The V4 authority matrix keeps every recursive or global capability false:

```text
common_owner_authority      = true       # owner receipt and final composition
registered_prefix_miss      = true       # validator/final composition only
scope_validation_authority  = true       # validator/final composition only
root_source_scoped_e1       = true       # consumer receipt only
scope_aware_consumer        = true       # consumer receipt only
root_source_occurrence      = true       # consumer receipt only
terminal_receipt_continuation = false
generic_e1 / successor_e1   = false
e1_authority                = false     # generic E1 remains denied
global_miss / exhaustion    = false
producer / branch           = false
E2 / E3 / E4 / E5 / T5      = false
persistent / re-entry / queue = false
```

The active registry requires all three roles, the orchestrator, the
post-issuance replayer, the V3 dependencies and the normative receipt schema to
be present and transitively pinned.  Any placeholder or zero pin is not
evidence of authority and must fail before any V4 manifest is returned.

This claim does not close the full E1-E5 transition contract, common producer
admission, Gate 2, Gate 4, T6 or the Erdős-Straus conjecture.  Any future change
to the resolver, loader policy, role bytes or explicit pins is a new authority
policy and requires a fresh proof and review.
