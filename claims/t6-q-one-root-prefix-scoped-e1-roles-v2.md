---
kind: claim
claim_id: t6-q-one-root-prefix-scoped-e1-roles-v2
title: q=1 root registered-prefix 的 common-owner 与 source-scoped E1 roles v2
statement: >-
  For an actual parentless ordinary q=1 G root at one exact HEAD, if the V3
  production terminal receipt is an independently verified registered-prefix
  MISS for gaps [3,7,11], the V4 role chain reconstructs the unique frozen V1
  common source owner and issues only a ROOT_SOURCE_SCOPED_E1 occurrence for
  the deterministic full-carrier phase root.  It issues no generic/successor
  E1, producer continuation, persistent admission, queue, E2-E5, T5, global
  exhaustion, or root-terminal authority.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
  - T6
  - q-one
  - common-owner
  - registered-prefix
  - source-scoped-e1
  - exact-head
sources:
  - data: data/t6-wave1/t6-coordinator-role-registry-v4.json
    role: active exact-HEAD role grants and denial matrix
  - source: scripts/t6_q_one_root_owner_classifier_v2.py
    role: loader-free exact V1 owner replay
  - source: scripts/t6_q_one_scope_aware_e1_validator_v2.py
    role: independent registered-prefix scope replay
  - source: scripts/t6_q_one_registered_prefix_e1_consumer_v2.py
    role: root-source-scoped E1 consumer
  - reproduction: scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py
    role: exact-HEAD controlled orchestration
  - reproduction: scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py
    role: post-issuance independent wire replay
  - source: schemas/t6-q-one-root-prefix-scoped-e1-v2.schema.json
    role: normative receipt wire schema
  - reproduction: tests/test_t6_q_one_root_prefix_scoped_e1_roles_v2.py
    role: pure-role positive, boundary and mutation controls
  - reproduction: tests/test_t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py
    role: exact-HEAD orchestration and independent replay controls
  - review: docs/audits/T6_Q1_ROOT_PREFIX_SCOPED_E1_FINAL_INDEPENDENT_REVIEW_2026-08-26.md
    role: final independent review and non-claim audit
visibility: public
last_checked: '2026-08-26'
---

# V4 q=1 Root Prefix-Scoped E1 Roles (v2)

## Claim Status

`established / independent review / exact-HEAD V4 scope only`

This claim records a deliberately narrow role layer.  It does **not** claim a
complete terminal schedule, a global selector, or a proof of the
Erdos--Straus conjecture.

## Frozen DAG

```text
raw q=1 G integers
  -> canonical source body -> root initializer anchor -> raw source state
  -> terminal-issuer actualness sidecar
  -> common root-owner receipt
  -> registered-prefix scope-validation receipt
  -> root-source-scoped E1 receipt
```

The three role modules are loader-free and import no project runtime,
scheduler, producer, subprocess, or repository API.  They accept explicit
plain mappings and exact role-grant preimages.  Exact-HEAD provenance and grant
authentication are supplied by the V4 controlled orchestrator and checked by a
separate post-issuance replayer; a pure role's local grant digest is not itself
a provenance authority.

## Common Owner

`classify_q_one_root_owner_v2` independently replays the raw source as an
exact prime (p\equiv1\pmod {24}), (q=1), ordinary G endpoint, with

\[
X=(p+3)/4
\]

and the complete ordered factorization of (X) into primes congruent to one
modulo three.  It rebuilds the body, anchor, state, and issuer actualness
preimages, then constructs the common selector header.  All fifteen frozen
family predicates are evaluated in `FAMILY_PRECEDENCE_V1` order.  For this
root domain the only true predicate is
`type_ii_relation_g_endpoint` (zero-based precedence index 2).

The normalized facts are not merely predicate-shaped.  They satisfy the exact
frozen V1 grammar, including `type_i_protocol=null` outside Type I and
`proper_root_height_class=NONE`.  The owner preimage is exactly

```text
contract_id=t6_persistent_selector_state_v1
schema_version=1
state_id, facts_digest, owner, matched_families, precedence_index
```

so `owner_id=owner:<bare-sha256>` agrees byte-for-byte with V1
`owner_digest_v1`, while the receipt's `owner_digest` stores its bare suffix.
The focused suite imports the pinned V1 reference only as an independent test,
passes `_validate_facts`, rebuilds `VerifiedSelectorHeaderV1`, and compares the
full classifier result and owner ID.

The owner scope is exactly `ROOT_SOURCE_DISPATCH_ONLY`; it is not persistent
queue admission.  The receipt has `common_owner_authority=true`, while
terminal dependency, prefix-MISS authority, E1, producer continuation,
admission, queue, and E2--E5 flags are false.  The receipt embeds complete
source preimages so its serializer can replay source semantics rather than
only checking an opaque ID and digest.  It has no terminal-result input and is
therefore independent of a later HIT or MISS.

## Scope Validation

`validate_q_one_registered_prefix_e1_scope_v2` repeats the source, actualness,
and owner replay without importing the owner role.  It independently factors

\[
x_m=(p+m)/4
\]

for (m=3,7,11), enumerates every (d\mid x_m^2), and checks both Bradford
Type-I and Type-II formulae in the deterministic order
`gap ascending, divisor ascending, Type-I before Type-II`.  A valid production
receipt must be exactly `ProductionQOneRegisteredPrefixMissReceiptV1` with
`MISS_REGISTERED_PRIORITY_COMPLETE`, gaps `[3,7,11]`, `next_unchecked_gap=15`,
and `global_exhaustion=false`.  Any root-terminal HIT is rejected before a
scope result is produced.

Gap 23 is recorded only as an outside-scope control.  For (p=1201), for
example, it contains the Type-I certificate (d=34), so a prefix MISS cannot
be relabeled global exhaustion.  The validator's own authority is limited to
`registered_prefix_miss_authority` and `scope_validation_authority`; it sets
`common_owner_authority=false`, `root_source_scoped_e1=false`, and all generic
or successor E1 and recursive permissions false.

## Root-Source E1

`consume_q_one_registered_prefix_miss_for_e1_v2` independently checks the
same source chain, common owner, production MISS, and scope-validation scans.
Only then does it derive the deterministic phase-root witness

\[
t=(p-1)/24,\qquad X=(p+3)/4,\qquad
R=16t+3,\qquad K=X(16t+1).
\]

It verifies (4K=pR+1), the fresh source

\[
(p,R(p-1)-p,p-1)\longrightarrow(1,R-1,1),
\]

the raw (p)-edge divisibility and gcd identities, and the target's
`TYPEI/CHARGED/FULL_CARRIER_POST_G` shape.  The resulting receipt is
`ROOT_SOURCE_SCOPED_E1_ISSUED` and sets `root_source_scoped_e1=true` plus
`scope_aware_consumer_authority=true` and
`scope_validation_authority=true`.  It explicitly keeps
`e1_authority=false`: this is a source-scoped occurrence witness, not generic
transition E1 or queue admission.  `terminal_receipt_direct_continuation_authority`
is false; the new scope-aware consumer authority comes only from the verified
combination of the three receipts.

## Controls

The focused role suite covers:

- (p=1201) and (p=2521): owner, scope validation, and root-source E1;
- (p=73,193,241441): production terminal HIT rejected by the E1 path;
- raw/body/anchor/state/actualness/owner/grant/scope swaps;
- gap-23 (p=1201,d=34) outside-scope evidence;
- schema ID/prefix and authority mutations;
- `object.__new__` forged receipts before and after digest resealing.

The local serializers and schema enforce shape and fixed authority constants,
but exact-HEAD artifact provenance is not inferred from a role-supplied digest.
That boundary is checked only by the V4 orchestrator/replayer.

## Explicit Non-Claims

This layer does not establish target-state E2, common target ownership, E3
normal form, identity-lift E4, T5/E5 potential payment, a persistent admission
ticket, producer or branch authority, queue mutation, complete terminal
coverage, `MISS_COMPLETE`, global exhaustion, Gate 2, Gate 4 completion, T6
totality, or the Erdos--Straus conjecture.

Focused verification:

```bash
python3 -m unittest tests.test_t6_q_one_root_prefix_scoped_e1_roles_v2 -v
ruff check scripts/t6_q_one_root_owner_classifier_v2.py \
  scripts/t6_q_one_scope_aware_e1_validator_v2.py \
  scripts/t6_q_one_registered_prefix_e1_consumer_v2.py \
  tests/test_t6_q_one_root_prefix_scoped_e1_roles_v2.py
```
