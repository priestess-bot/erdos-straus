# T6 F2/F3 Wave1 Gate 2 Grammar Decision

> Integration branch: `integration/t6-f2-f3-wave1`
>
> Integration baseline: `9215f8c92c53c0eb1081849b0a03e5cb922facad`
>
> Freeze status: `FROZEN_E3_TYPE_SPACE_PRODUCERS_NOT_YET_ADMITTED`
>
> Grammar hash: `d073a68dfd7c109f2f71fe0533d5084e78ef8fca870d229a0ea98e85c0ce02e1`

## 1. Decision Scope

This is Gate 2 of `T6_F2_F3_HIGH_CONCURRENCY_EXECUTION_PLAN.md`. It freezes the
shared E3 type space after all seven tracks supplied scope freezes, residual matrices,
and target-shape proposals. It does not freeze producers, prove source reachability, or
upgrade any F1/F2/F3/T6 theorem.

The executable source is:

```text
data/t6-wave1/family-grammar-freeze-v1.json
scripts/t6_persistent_selector_state_v1.py
scripts/t6_persistent_selector_runtime_v1.py
```

## 2. Accepted Type Refinements

### 2.1 High proper-factor root

`proper_root_high_endpoint` is a persistent owner only for the exact semantic guard:

\[
\operatorname{ROOT\_SOL}\land\operatorname{TYPEI/CHARGED}
\land\operatorname{PROPER\_ROOT}\land
M=(p^2+p+1)/3\land u=(2r+1,M)\land0<u<M\land h=3u>p\land k=\varnothing.
\]

It exists solely to preserve the F3 high endpoint quantifier. A high endpoint cannot be
forced to fill low-height fields such as (k) or (D_*). Its strict rebase target, when
proved and admitted, is an existing `TYPEI/CHARGED` overflow owner; its high stutter
leaf remains open.

### 2.2 Ordinary marked absorb

`type_i_absorb_marked_residual` is the only new ordinary Type-I family. Its exact guard is:

\[
\operatorname{ROOT\_SOL}\land\operatorname{TYPEI/ABSORB}
\land\operatorname{MARKED\_ABSORB}\land R<p\land A\mid K
\land\operatorname{terminal\_first\ miss}.
\]

It exists for a genuine semantic protocol transition, not for a support-size threshold.
If a source is `CHARGED` and a non-hit target has (R<p), the branch must still prove
E1--E4 and then use `PHASE_DROP` into ABSORB. Conversely, a target with (R>p) is
CHARGED overflow even when its support is at most (B_p), and must prove its own
`LOCAL_DROP` or `OUTER_RANK_DROP`.

### 2.3 Atomic payloads

`AtomicPendingTargetV1` is an edge-receipt occurrence envelope, not a persistent family.
The old `t2_v1_atomic_pending_target` remains historical T2 vocabulary in the frozen
pre-T6 frontier, but `PersistentSelectorStateV1` rejects `ATOMIC_PENDING` with
`PENDING_OUTPUT_NOT_PERSISTENT`.

The only retained atomic arms are `H4_A1` and `C8_DOUBLE_LOW`, each stored in the
producer receipt. Before queue admission, their final target must be recomputed as:

```text
terminal
or TYPEI/CHARGED overflow
or TYPEI/ABSORB marked-absorb
```

Typed F/G fields are certificate context, not owner authority.

## 3. Rejected Requests

- No generic F2 explicit-residual family.
- No generic QC1 family before a theorem converts (q\mid k) into a source-bound integer
  occurrence with conserved charge and E1 path.
- No standalone p-adic, (L_1), (L_\omega), raw-policy, atomic or second-child checkpoint state.
- No C=1 family merely encoding a local no-go.
- No reuse of H4/c8 arms for m=3 q=5 two-sided occurrence payloads.
- No later ordered total-cofactor producer: the current determinant prepartition makes it
  preempted or a stutter.

## 4. Independent Findings Incorporated

The freeze incorporates early cross-review corrections:

1. A target with (R_T<p) and (M\mid K_T) cannot have (M>B_p); the former target is
   semantic ABSORB only after a full protocol transition, not a CHARGED local drop.
2. The m=3 q=5 domain includes a nonminimal (v_5(T)\ge2) branch and an odd first-child
   strict branch. Neither can be silently moved into the minimal (L_\omega) theorem.
3. A quotient ideal factor is not a physical QC1 occurrence. Self-authenticated
   `ACTUAL_PERSISTENT`, producer, terminal miss, E1--E5 or mark records are rejected.
4. c8 OTHER excludes C=1 on its own universal fallback, while H4 C=1 required and now has
   a separate source-gate analysis; these conclusions cannot be generalized to future producers.

## 5. What Gate 2 Does Not Establish

```text
producer registry hash              NOT FROZEN
F1 source-signal count = 0          NOT ESTABLISHED
all queue writes use runtime        NOT ESTABLISHED
F2 residual leaves = 0              FALSE
F3 residual leaves = 0              FALSE
any new candidate is verified edge  FALSE
```

Gate 3 requires each remaining producer to have a symbolic guard partition, a shared
projector and source/target terminal schedules, independent E1--E4 validator, target
owner set, strict semantic N7 ticket, and actual re-entry through the runtime.
