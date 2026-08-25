# F1 Admission Runtime Boundary v1

Date: 2026-08-25  
Base: `332c0f7ed48d453ca76d35639a618659d9b559ca`  
Track: `F1-ADMISSION`

## Result

The current `PersistentSelectorRuntimeV1` cannot ingest an existing F2/F3
arithmetic scheduler output directly. The safe result is a small adapter
boundary, not a second queue path and not a relaxation of E1--E5.

The proposed machine-readable contract is
[`f1-admission-target-shape-proposal-v1.json`](../data/interface-requests/f1-admission-target-shape-proposal-v1.json).
The source census and its exact 18-row disposition matrix are
[`f1-admission-scope-freeze-v1.json`](../data/t6-wave1/f1-admission-scope-freeze-v1.json)
and
[`f1-admission-source-signal-residual-matrix-v1.json`](../data/t6-wave1/f1-admission-source-signal-residual-matrix-v1.json).

## What The Runtime Actually Requires

The runtime path is already strict:

1. `bootstrap_nonterminal_v1()` or an admitted queue item supplies a
   `RuntimeQueueItemV1`.
2. `verify_source_state_v1()` recomputes the header, owner digest and T5
   potential from canonical state fields.
3. A registered branch runs its source terminal schedule first.
4. The executor returns a runtime-issued `ProducedCandidateV1`; the runtime
   rejects a candidate that was not issued exactly once by that executor.
5. The projector creates `TargetProjectionV1`; caller-supplied owner, family,
   recursive flags and queue flags are forbidden.
6. The target terminal schedule runs before persistence.
7. An independent `TransitionValidationV1` must bind source, branch and
   projection and prove E1--E4.
8. The runtime recomputes the target owner, target state ID and fixed T5 N7
   ticket, then calls the sole `_enqueue_admitted_target_v1()` mutation.

These requirements are implemented in
[`scripts/t6_persistent_selector_runtime_v1.py`](../scripts/t6_persistent_selector_runtime_v1.py)
and the state-level extractor in
[`scripts/t6_persistent_selector_state_v1.py`](../scripts/t6_persistent_selector_state_v1.py).

## Why The Existing Arithmetic Outputs Cannot Pass Through

The representation-dual builders return legacy dictionaries whose
`source_state` and `successor_state` contain only arithmetic descriptors such as
`equation_target`, `R`, `K`, `absorbed_support` and sometimes `state_class`.
They do not contain the v1 top-level state envelope, `producer_id`, `branch_id`,
`queue_gate`, `parent_state_id`, mark receipt, terminal-first receipt, source
receipt or canonical `facts` map. Running those descriptors through
`extract_verified_selector_header_v1()` therefore stops at the missing-state
schema boundary before owner classification.

The total-cofactor adapter has a different but related problem: its
`registration(..., persistent_queue=True)` copies a boolean supplied by its
caller. Its `verify()` method passes fixed fixture sources and synthetic
`contract-fixture-*` digests. That is a relative arithmetic adapter, not a
runtime-issued source receipt. The boolean cannot become a queue right.

The H4 and c8 controls are safer by construction: H4 keeps
`recursive_edge_eligible=False` even when external premises are labelled
actual, and c8's fallback proposal is explicitly non-active. They remain
analysis evidence until an admitted parent/path, complete terminal-first miss,
target serializer and common re-entry are supplied.

## Minimal Safe Bridge

An arithmetic scheduler may be adapted only as a registered branch with this
shape:

```text
SourceExecutionContextV1
  -> branch-specific scheduler
  -> TerminalDraftV1 | GuardMissV1 | CandidateTransitionV1
  -> registered ProjectorV1
  -> registered target terminal schedule
  -> independent TransitionValidatorV1 (E1--E4)
  -> common owner extraction and T5 ticket check
  -> sole queue mutation
```

The scheduler may place an occurrence, divisor, path digest and deterministic
tie-break in `witness_payload`. It may not place `owner`, `family`,
`recursive_edge_eligible`, `persistent_queue`, cached `normal_form`, or a
precomputed owner digest there. The projector must reconstruct canonical target
integers and facts; the validator must bind the source state ID and projection
digest; the runtime must perform terminal precedence, E5 and re-entry.

## Strict Blockers

The following are independent blockers, not merely missing implementation
polish:

- no source `PersistentSelectorStateV1` receipt for the legacy arithmetic rows;
- no registered source/target terminal schedule for those rows;
- no independent E1--E4 validator binding the arithmetic receipt;
- no canonical target facts suitable for the shared extractor;
- no `T5StateDescriptorV1` whose potential can be recomputed from target facts;
- no runtime-issued `ProducedCandidateV1` envelope;
- no proof that target owner is in the producer's declared target set;
- no recursive re-entry path after target admission.

Consequently, replacing a legacy dictionary's `recursive_edge_eligible=True`
with a queue append would be unsound. The correct interim disposition is either
`NONRECURSIVE_CONTROL` (when the function is only a fixture/result builder) or
`REGISTERED_PRIMARY` with an explicit open E3/runtime blocker (when it is part of
the frozen producer surface).

## Verification Commands

The following focused checks were run against the stated base:

```bash
python3 -m json.tool data/t6-wave1/f1-admission-scope-freeze-v1.json
python3 -m json.tool data/t6-wave1/f1-admission-source-signal-residual-matrix-v1.json
python3 -m json.tool data/interface-requests/f1-admission-target-shape-proposal-v1.json
python3 scripts/audit_t6_constructor_inventory_v1.py
```

The source census and matrix both contain 18 unique anchors. The structural
inventory audit remains `PASS` with `closure_ready=false`; no F1/F2/F3/T6
status is upgraded by this report.
