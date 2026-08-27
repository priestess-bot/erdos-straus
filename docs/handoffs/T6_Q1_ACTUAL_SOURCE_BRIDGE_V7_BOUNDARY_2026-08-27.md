# T6 q=1 Actual Source Bridge V7 Boundary (2026-08-27)

## Finding

The current q=1 chain cannot issue a Gate-2 `E1OccurrenceReceiptV1`.

The exact-HEAD V6 replayer can reconstruct the V3/V4/V5/V6 candidate chain,
but the only source terminal result is
`MISS_REGISTERED_PRIORITY_COMPLETE` for gaps `[3,7,11]`. The structured E1
verifier requires `MISS_COMPLETE`, while the complete terminal registry has
no registered complete schedules. Therefore a V6 candidate is not a source
authentication grant and cannot be relabeled as E1.

This is a structural contract boundary, not a test gap:

```text
registered prefix MISS != complete terminal MISS
candidate replay != serialized source authority
```

## V7 Pre-E1 Layer

The next safe layer is coordinator-owned `AuthenticatedQ1RootSourcePrefixV1`.
It is deliberately prefix-only and remains non-E1.

```text
raw q=1 G input + V3 result + untrusted candidate
  -> external commit/trust-anchor verification
  -> consumer-owned V6 independent replayer invocation
  -> fresh V3/V4/V5/V6 reconstructed source context
  -> AuthenticatedQ1RootSourcePrefixV1
```

The consumer must not accept caller-provided V4/V5/V6 receipts, state wires,
role grants, artifact manifests, or `authority_verified` fields. It must
fresh-load and invoke the independent replayer itself.

Positive facts allowed on this object:

```text
exact_head_tree_matched
external_commit_anchor_verified
v3_v4_v5_v6_independently_replayed
v1_source_state_reconstructed
parent_kind = ROOT_INITIALIZER
terminal_scope = REGISTERED_PRIORITY_ONLY
```

All of the following remain false:

```text
source_terminal_complete
generic_e1 / successor_e1 / e1_authority
producer / branch / projector
E2 / E3 / E4 / E5 / T5
admission / queue / enqueue / reentry / global_exhaustion
```

The external trust anchor must be outside the mutable repository content and
bind at least the exact head, tree, and reviewed policy/manifest digest. A
commit that simultaneously changes resolver code and its pins cannot serve as
its own trust root.

## First E1 Prerequisites

V1 remains blocked by its global `MISS_COMPLETE` constant. A separate,
zero-authority V2 foundation can study policy-relative branch clearance after
the coordinator freezes a total decision order and independently clears every
action before the selected phase-root branch:

```text
AuthenticatedQ1RootSourcePrefixV1
  -> coordinator prior-decision replayer
       -> prior HIT: Terminal
       -> prior producer selected: follow that branch
       -> ALL_PRIOR_ROUTES_MISS:
            Q1_PHASE_ROOT_BRANCH_SCOPED_E1_ISSUER_V2
```

The branch-scoped issuer must independently:

1. Invoke the V6 replayer itself.
2. Replay the complete ordered list of terminal and producer actions before
   the selected branch.
3. Terminal-preempt every prior hit and honor every prior matching producer.
4. Bind an explicit `facts.relation_q=1` integer occurrence path.
5. Obtain all policy pins and the branch index from its coordinator registry.
6. Use an independent E1 verifier that does not reuse the producer result.

It emits `MISS_HIGHER_PRIORITY_POLICY_COMPLETE` with
`global_exhaustion=false`; it must not be promoted to generic E1 or a terminal
universe miss. This does not amend the current Goal: Gate 4/5 still require
terminal-over-producer preemption and a complete source terminal schedule. A
Goal-compatible activation must place every overlapping registered terminal
before the producer, or prove its guard disjoint, and then replay that complete
schedule. See `t6-branch-scoped-priority-clearance-soundness-v2`.

## Downstream DAG

```text
authenticated V1 source + Goal-compatible complete terminal clearance
  -> branch-scoped E1 candidate
  -> P -> {C, L, D} -> A -> Q
  -> persistent target V2 state
  -> final owner / common E3
  -> E2, E4, E5 receipts
  -> final bundle -> admission sidecar -> re-entry
```

`Q` remains a nonpersistent prestate. It must not be relabeled as a V1
successor merely to bypass the state-ID/owner/bundle dependency cycle.

## Related F3/C8 Terminal Work

F3 and C8 short certificates can be installed only as hit-only terminal
guards on an already admitted source. A positive terminal certificate needs
only the source state identity, the shared root `p`, and its verified integer
witness. A guard miss cannot be treated as an exhaustive miss without the
registered complete factor/divisor coverage.

This leaves T6, F1, F2, and F3 `OPEN`.
