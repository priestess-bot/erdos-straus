---
kind: claim
claim_id: t6-coordinator-q1-root-source-scoped-e1-rebind-v1
title: q=1 root source-scoped E1 从 V2 occurrence 到 V5 V1 base source 的严格 rebind
statement: >-
  Subject to independently replayed V4 and V5 receipts at the same reviewed
  exact HEAD, a V4 ROOT_SOURCE_SCOPED_E1 occurrence for a registered-prefix
  MISS can be deterministically rebound to the newly content-addressed V5
  ROOT_INITIALIZER_OUTPUT source.  The rebind recomputes the V1 state owner,
  owner digest and source potential, carries the phase-root arithmetic only as
  an external candidate witness, and grants no generic/successor E1,
  producer, admission, E2-E5, T5, queue, re-entry or global authority.
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - source-rebind
  - scoped-e1
  - exact-head
  - proof-boundary
sources:
  - source: scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py
    role: independent V2/V4/V5 source-chain replay and namespaced rebind receipt
  - source: schemas/t6-q-one-root-source-scoped-e1-rebind-v1.schema.json
    role: normative rebind receipt wire and authority constants
  - reproduction: tests/test_t6_q_one_root_source_scoped_e1_rebind_v1.py
    role: positive controls, preemption and coherent-reseal mutation controls
  - claim: t6-coordinator-q1-root-prefix-scoped-e1-authority-v4
    role: V4 root-source-scoped E1 input contract
  - claim: t6-coordinator-q1-root-v1-base-admission-authority-v5
    role: V5 V1 base-source and owner reanchor input contract
  - concept: t6-persistent-selector-state-v1
    role: frozen V1 extractor, classifier and owner digest contract
  - source: scripts/t6_structured_transition_receipts_v1.py
    role: explicit non-reuse boundary; its generic E1 requires MISS_COMPLETE
visibility: public
last_checked: '2026-08-27'
---

# Rebind boundary

Let (E_4) be a valid V4 consumer receipt and (B_5) a valid V5 base-admission
receipt at one exact HEAD (H).  The rebind premise requires the complete V2
source chain in both receipts to agree byte-for-byte:

```text
raw q=1 G integers
CanonicalQOneGSourceBodyV2
RootInitializerAnchorV2
RawRootSourceStateV2 (state_id, digest)
root actualness (HEAD/tree and digest)
V3 registered-prefix MISS
V4 owner and scope receipts
```

The V5 receipt must additionally replay a new V1
`ROOT_INITIALIZER_OUTPUT` state with `persistent_admission=true`,
`parent_state_id=null`, and the frozen owner
`type_ii_relation_g_endpoint`.  This is a base-admission fact only; V5 still
does not enqueue the state or prove runtime queue membership.

The output is a separate
`Q1_ROOT_SOURCE_SCOPED_E1_REBIND_RECEIPT_V1`.  Its map is

```text
V2 RawRootSourceStateV2 state_id/digest
        -> V5 V1 state_id and V1 state-wire digest
```

The V1 state is copied only after independent replay and remains exactly the
V5 state.  Its state ID and semantic-origin preimage do not contain the V4
consumer receipt, candidate, math replay, or rebind map.

The receipt and its derived witness are explicitly namespaced
`Q1_ROOT_SOURCE_SCOPED_E1_REBIND_V1` with
`path_semantics=DERIVED_WITNESS_NOT_V1_STATE_PATH` and `not_transition=true`.
The V1 state-ID suffix and the full V1 state-wire digest have separate declared
domains; neither is a generic structured-E1 source-payload digest.  The owner
inside the derived witness is explicitly a V1 source owner, never a target
owner.  These fields prevent an adapter from silently treating this sidecar as
an ordinary V1 state path or transition.

# Recomputed versus carried data

The following arithmetic is replayed from the raw (p) and may be carried as
an external candidate witness:



\[
t=(p-1)/24,\qquad X=(p+3)/4,\qquad R=16t+3,\qquad K=X(16t+1),
\]

\[
(p,R(p-1)-p,p-1)\longrightarrow(1,R-1,1),
\qquad 4K=pR+1.
\]

The low-chart uniqueness, gcd and p-edge identities, ROOT_SOL mark equality,
and the registered scope ([3,7,11]) are checked again.  The V4 candidate and
math-replay digests are recorded as lineage pins, but are never copied into
the V1 state.

The rebind must recompute, rather than copy:

- the V2 and V1 source IDs and all source-chain digests;
- the V1 header, facts validation, fifteen-family predicate results,
  precedence index and `owner_digest_v1`;
- the V3 MISS and V5 terminal projection binding, including
  `next_unchecked_gap=15` and `global_exhaustion=false`;
- the V1 source potential receipt
  ((p,3,0,0,0,0,0)), bound to the new V1 state ID;
- the rebind candidate digest and the explicit old-to-new source map.

No target state ID, producer ID, branch ID, target owner, target terminal
result, E2/E3/E4/E5 receipt or T5 ticket is inferred by this operation.

# Quantified theorem

The machine-checkable theorem is conditional and pointwise, not a claim for
every \(p\equiv1\pmod {24}\):

\[
\forall(H,p,E_4,B_5),
\qquad
\operatorname{Valid}_{H}(E_4)
\land\operatorname{Valid}_{H}(B_5)
\land\operatorname{SameV2Root}(E_4,B_5)
\land\operatorname{V1BaseAdmitted}(B_5)
\Longrightarrow
\exists!\,R_6=\operatorname{Rebind}(E_4,B_5).
\]

The unique receipt is deterministic under the fixed canonical JSON encoding.
It has `v1_source_state_id = B5.v1_state_id`, a recomputed V1 owner digest,
and a fresh source-bound candidate witness.  The only authority bits set true
are:

```text
v4_root_source_scoped_e1 = true       # inherited evidence marker
root_source_scoped_e1_rebound = true
source_rebind_authority = true
```

`e1_authority`, `generic_e1`, `successor_e1`, producer/branch, admission,
queue/enqueue, E2--E5, T5, re-entry, terminal-leaf and global-exhaustion bits
are all false.

# Why this is not generic E1

The current structured receipt layer requires `source_terminal_result=MISS_COMPLETE`
for `E1OccurrenceReceiptV1`.  V4 and V5 only establish
`MISS_REGISTERED_PRIORITY_COMPLETE` for the declared finite prefix, with
`next_unchecked_gap=15`.  The rebind therefore uses a new namespace and keeps
`e1_authority=false`; it must not be passed to
`make_verified_transition_bundle_v1` as a successor E1.  A later producer edge
needs its own target terminal scope and independent E1--E5 receipts.

# Controls and limits

The focused controls include:

- (p=1201,2521): V3 prefix MISS, V4 scoped occurrence and V5 base source
  rebind;
- (p=73,193,241441): production terminal HIT preempts before V4/V5/rebind;
- cross-source and cross-HEAD swaps;
- V4/V5 registry-grant changes, receipt and candidate coherent reseals,
  authority flips, source-state/owner swaps and boolean/float injection;
- the (p=1201), gap-23 Type-I (d=34) certificate remains outside the
  registered scope and cannot become global exhaustion.

This claim does not establish a generic or successor E1, a producer or branch,
target E2--E5, common target admission, queue mutation, runtime queue
membership, Gate 2, Gate 4, F1/F2/F3, T6 totality or the Erdős--Straus
conjecture.  The V4/V5 selected-commit trust condition remains in force; the
pure role's local grant is not an external Git trust anchor.
