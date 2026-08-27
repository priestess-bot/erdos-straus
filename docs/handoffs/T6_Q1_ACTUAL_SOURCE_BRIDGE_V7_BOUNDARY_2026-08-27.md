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

Only after a coordinator-owned complete source terminal schedule exists may a
second, branch-scoped issuer be considered:

```text
AuthenticatedQ1RootSourcePrefixV1
  -> complete source terminal replayer
       -> HIT: Terminal
       -> MISS_COMPLETE: Q1_PHASE_ROOT_BRANCH_SCOPED_E1_ISSUER
```

The branch-scoped issuer must independently:

1. Invoke the V6 replayer itself.
2. Replay the complete terminal schedule.
3. Terminal-preempt every hit.
4. Bind an explicit `facts.relation_q=1` integer occurrence path.
5. Obtain all policy pins from its coordinator registry.
6. Use an independent E1 verifier that does not reuse the producer result.

It must still not be promoted to generic E1 without a separate scope and
coverage proof.

## Downstream DAG

```text
authenticated V1 source + COMPLETE source MISS
  -> branch-scoped E1
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
