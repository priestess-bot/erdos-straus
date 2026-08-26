# T6 q=1 Phase-Root E2 Preprojection Handoff

Date: 2026-08-27

## Established Mathematical Inputs

For an ordinary q=1 G root with

\[
p=24t+1,
\qquad X=6t+1,
\qquad R=16t+3,
\qquad K=X(16t+1),
\]

the target chart is uniquely determined among low full-carrier charts by

\[
4K=pR+1,
\qquad A=1,
\qquad X\mid K,
\qquad 3\le R\le p-2.
\]

The target facts are

```text
ROOT_SOL
TYPEI / CHARGED / FULL_CARRIER_POST_G
full_carrier_scope = true
support_A = 1
is_overflow = false
chart = (R,K)
```

The frozen V1 predicate vector has the unique match
`type_i_full_carrier_post_g` at precedence index 14. This fixes a target owner
label, but not an owner digest for a future V2 persistent state, because that
digest must depend on the eventual target state ID.

The target-local anchor-sink predicate is always false:

\[
\gcd(R-1,K)=1.
\]

The finite Bradford predicate at gaps `[3,7,11]` is p-only and therefore has
the same mathematical result at the q=1 source and the full-carrier target.
This transport must still be rebound to a target projection; it does not
convert a source-state terminal receipt into a target receipt.

## Required Object Order

Do not construct a persistent successor state before its target terminal scope is
frozen. The required acyclic order is:

```text
P: pure canonical target preprojection
  -> {C: target predicate preclassification,
      L: target-bound finite terminal result,
      D: target T5 coordinate draft}
  -> A: edge anchor
  -> Q: non-authorizing V2 target prestate and state ID
  -> O: final owner classification and future V2 owner digest
  -> B: E1--E5 bundle
  -> admission sidecar
```

`P` is p-only and contains no source state, terminal, owner, potential, target
state, edge, transition or admission ID. `C`, `L` and `D` are independent
siblings of one pure projection. `L` binds `SOURCE_STATE` and
`TARGET_PROJECTION`, but not `target_state_id`. Apart from its own V2 prestate
fields, the only allowed upstream edge/transition reference in `Q` is `A`; it
must not contain a final owner, final E1--E5 receipt, transition ID or admission
result. `O` is necessarily post-state-ID and must not be written back into `Q`.

The existing `t6_acyclic_transition_bundle_v2` is a structural template for
this order only. It has no E2, terminal issuance, producer, admission or queue
authority.

## Target Terminal Scopes

Two future policies must never be conflated:

```text
SELECTED_GAPS_3_7_11_23_PLUS_ANCHOR
NATURAL_PREFIX_3_7_11_15_19_23_PLUS_ANCHOR
```

Neither is a complete terminal universe. Both must carry their exact family
list, ordering, projection binding and `global_exhaustion=false`.

The current V3 receipt provides only `[3,7,11]`, with
`next_unchecked_gap=15`. A target schedule can transport that p-only finite
predicate only after independently replaying it under the target projection.

## Controls

`p=1201` and `p=2521` remain valid for the current `[3,7,11]` source scope,
but both have a gap-23 terminal. They must terminal-first preempt under either
future policy that includes 23:

```text
p=1201: Type I, m=23, d=34
p=2521: Type II, m=23, d=8
```

`p=12721` is a q=1 G control that misses `3,7,11,23` and has an anchor-sink
MISS, but has a gap-19 Type II terminal. It is suitable only for the explicit
non-contiguous selected-gap policy, not for the continuous prefix through 23.

p=21169 is a stronger q=1 G control for the natural six-gap prefix. It has
\(X=5293=67\cdot79\), misses the complete Bradford Type-I/II screens at
gaps 3,7,11,15,19,23, and also has the anchor-sink MISS. This only says that
the named finite schedule has no hit at that input; it does not rule out an
unregistered terminal family. The exact gap-23 classification and this
control are recorded in
[type-I-type-II-gap-23-two-box-classification](../../claims/type-I-type-II-gap-23-two-box-classification.md).
Thus no finite prefix through 23 can be called a complete terminal universe.

Before any E2 implementation, the planned Q object must be a non-authorizing
V2 prestate rather than a PersistentSelectorStateV1 successor. In the V1
schema, the successor source receipt containing E1--E5=true is part of the
state-ID preimage, whereas the independently replayable E1--E5 bundle must be
constructed only after the target state ID and owner digest. A boolean
placeholder would either assert an unproved edge or create a content-ID cycle.
The exact dependency proof and proposed V2 boundary are in
[T6_Q1_PHASE_ROOT_PRESTATE_V2_BOUNDARY_2026-08-27.md](T6_Q1_PHASE_ROOT_PRESTATE_V2_BOUNDARY_2026-08-27.md).

## Non-Claims

This handoff does not authorize E2, target terminal issuance, E3, E4, E5,
producer/branch, queue, re-entry or a verified successor. The V6 pure rebind
remains `DERIVED_WITNESS_NOT_V1_STATE_PATH`, not generic E1.
