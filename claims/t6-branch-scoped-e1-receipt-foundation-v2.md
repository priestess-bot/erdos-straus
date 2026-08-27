---
kind: claim
claim_id: t6-branch-scoped-e1-receipt-foundation-v2
title: T6 branch-scoped E1 V2 zero-authority receipt foundation
statement: >-
  The V2 branch-scoped receipt module provides three factory-only immutable
  wire types for structural branch-selection replay, explicit integer
  occurrence replay from a supplied source-state wire at the path pinned by
  the selected producer action, and independent PASS evidence binding. Its
  parsers reconstruct every receipt from the embedded inputs and reject
  incomplete or reordered policy prefixes, duplicate producer action keys,
  cross-source or cross-policy substitutions, occurrence-path substitutions,
  V1 casts, global-miss relabeling, non-integer occurrences, replayer identity
  reuse, resealing with authority, and extra authority fields. This establishes
  only a zero-authority serialization and replay foundation. It does not
  authenticate the supplied route policy, external authority policy, source,
  issuer or verifier; does not issue actual E1; does not satisfy Goal Gate 2;
  and does not replace the complete terminal schedule and preemption required
  by Goal Gates 4 and 5. F1, F2, F3 and T6 remain OPEN.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - t6-branch-scoped-priority-clearance-soundness-v2
  - t6-terminal-miss-scope-taxonomy-v2
  - denominator-escape-state-contract
topics:
  - T6
  - E1
  - branch-selection
  - receipt-foundation
  - zero-authority
  - proof-boundary
sources:
  - reproduction: scripts/t6_branch_scoped_e1_receipts_v2.py
    role: factory-only V2 receipt construction, canonical sealing and strict replay
  - reproduction: tests/test_t6_branch_scoped_e1_receipts_v2.py
    role: positive roundtrip and fail-closed binding/authority controls
  - data: schemas/t6-branch-scoped-e1-receipts-v2.schema.json
    role: exact external wire shape and zero-authority constants
  - claim: t6-branch-scoped-priority-clearance-soundness-v2
    role: policy-relative mathematical interpretation and remaining admission hypotheses
visibility: public
last_checked: '2026-08-27'
---

# T6 branch-scoped E1 V2 zero-authority receipt foundation

## 1. Established software theorem

The module exposes exactly three receipt classes:

```text
BranchSelectionReceiptV2
E1OccurrenceReceiptV2
E1IndependentReplayReceiptV2
```

All three are frozen, slotted and factory-only. Their public parsers do not
accept a receipt's terminal fields as sufficient evidence: they reconstruct
the expected receipt from its embedded policy, replay, source and lineage
inputs, then compare the complete wire including the content ID and digest.
Consequently, changing a derived field and merely recomputing the outer seal
does not preserve validity.

The branch-selection factory replays a finite ordered decision policy. If the
selected producer occupies index \(j\), the supplied prior-replay array must
have exactly \(j\) entries and bind policy decisions \(0,\ldots,j-1\) in that
order. A prior terminal must report `TERMINAL_MISS`; a prior producer must
report `GUARD_FALSE`; and the selected producer guard must report true. The
receipt therefore proves structural completeness only relative to the exact
submitted policy prefix.

The occurrence factory resolves `occurrence_path` directly against the exact
submitted `source_state_payload`. Its content-addressed `state_id` and full
wire digest must replay. The caller path and source-lineage path must both equal
the `expected_occurrence_path` pinned by the selected producer action in the
route policy, including its canonical digest. The resolved value must have
exact Python/JSON integer type: a boolean is not accepted as an integer. The
source lineage must also bind the same HEAD, source, owner/domain, route policy,
route, producer, branch and selected guard as the branch-selection receipt.

The lineage's `authority_policy_digest` is deliberately a separate slot from
the route-policy digest. It is inert external caller evidence in this
foundation, and equality with the route-policy digest is neither required nor
treated as authentication. The positive control uses distinct digests to keep
that separation executable.

The independent-replay factory binds both preceding receipt IDs and digests.
It accepts only PASS evidence and requires the replayer ID and digest to match
the independent-verifier pins in the lineage. It also rejects reuse of the
producer, issuer, lineage replayer or any branch-selection replayer identity or
digest. These are structural separation checks, not proof that the named
principal is independently controlled.

## 2. Frozen non-authority boundary

Every receipt fixes the following semantics:

```text
clearance_outcome       = MISS_HIGHER_PRIORITY_POLICY_COMPLETE
coverage_semantics      = REGISTERED_HIGHER_PRIORITY_ONLY
completeness_scope      = BEFORE_SELECTED_BRANCH_ONLY
terminal_universe_status = NOT_ASSERTED_NOT_REQUIRED
global_exhaustion       = false
```

It also fixes `authority`, `e1_authority`, `producer_authority`,
`admission_authority`, `persistent_admission`, `queue_authority`,
`enqueue_authority`, `goal_gate2_e1_authority`,
`complete_terminal_schedule_authority`, `goal_gate4_authority` and
`goal_gate5_authority` to false. V2 is explicitly incompatible with V1 and
cannot be downcast. In particular, neither a policy prefix nor its receipt may
be relabeled `MISS_COMPLETE`.

The source-lineage issuer, role grant, external trust anchor and independent
verifier fields, including the distinct external authority-policy digest, are
inert caller evidence in this foundation. There is no registered issuer,
coordinator runtime, producer, capability resolver, admission path or queue
mutation API. Thus a structurally valid V2 receipt is not an authoritative
statement that its source is actual reachable state, and its integer path
replay is not Goal Gate 2 E1. The `consumed_occurrence_*` fields repeat the
factory's structural source/path/value binding only; they are not independent
evidence that a producer consumed that value.

## 3. Focused controls

The focused test module checks all three positive wire/schema roundtrips and
the following fail-closed boundaries:

- direct construction outside the factories;
- V1 inputs and V1 compatibility/downcast claims;
- global miss or terminal-universe miss relabeling;
- prior-decision omission, reordering and kind/outcome mismatch;
- duplicate producer/branch/contract/occurrence action keys;
- route, producer, branch, source and policy substitution;
- caller occurrence-path and resealed lineage-path substitution;
- boolean and non-integer occurrence values;
- changing a sealed occurrence to a derived path or another value;
- independent replayer ID or digest reuse;
- resealing an authority bit and injecting an extra authority field.

These controls establish the public factory/parser behavior under the normal
trusted-process model. They do not claim a hostile Python process security
boundary against `object.__new__`, `object.__setattr__`, monkeypatching or
module replacement.

## 4. Remaining proof obligations

To become a Goal-compatible E1 input, this foundation still needs an
authenticated exact-HEAD coordinator policy and source lineage, active role
and issuer grants, an independently controlled verifier, and an actual-source
theorem covering the relevant reachable owner/domain. It must then be
cross-bound to deterministic E2, common legal E3, universal E4, strict E5,
common admission and recursive re-entry.

The current Goal additionally requires a complete terminal schedule and
terminal-over-producer preemption. This V2 prefix theorem does not replace
Goal Gates 4 or 5. It supplies no F1/F2/F3 residual-exhaustion theorem and no
selector totality theorem. F1, F2, F3 and T6 therefore remain OPEN.
