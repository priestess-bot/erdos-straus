# T6 F2/F3 Wave1 Gate 2 Grammar Decision

> Integration branch: `integration/t6-f2-f3-wave1`
>
> Integration baseline: `9215f8c92c53c0eb1081849b0a03e5cb922facad`
>
> Freeze status: `FROZEN_E3_TYPE_SPACE_PRODUCERS_NOT_YET_ADMITTED`
>
> Grammar hash: `ffba0a082073127ba1090eb02fd666aa7621fd55ef0045061d549a3e2defb00a`

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
\begin{gathered}
g=(p+1)/2,\quad A=g(p^2r-g),\quad K=A(p-1),\\
R=2p^3r-p^2-2pr-p+1,\quad \texttt{is\_overflow}=\mathrm{true},\\
M=(p^2+p+1)/3\land u=(2r+1,M)\land0<u<M\land h=3u>p\land k=\varnothing.
\end{gathered}
\]

It exists solely to preserve the F3 high endpoint quantifier. A high endpoint cannot be
forced to fill low-height fields such as (k) or (D_*). Its strict rebase target, when
proved and admitted, is an existing `TYPEI/CHARGED` overflow owner; its high stutter
leaf remains open.

### 2.2 Lineage and overflow are independent axes

`C8_PARENT` and `PROPER_ROOT` name a source lineage; `is_overflow` names the
chart geometry. For `TYPEI/CHARGED`, the contract now requires
`is_overflow` exactly when (R>p). Generic `OVERFLOW` remains a provenance value
for a chart with no finer lineage, but it is no longer forced onto a genuine C8 or
proper-root source.

The freeze permits only the explicit overlaps in the machine-readable grammar:
C8 may refine an overflow owner, and each coupled proper-root owner may refine the
high-support sink or the (A>1) overflow residual. Existing precedence retains the
lineage owner. This is a type correction only: C8 relay proof, fresh source scope,
actual E1, common admission and re-entry are still absent.

### 2.3 Ordinary marked absorb

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

### 2.4 Atomic payloads

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
4. c8 OTHER excludes C=1 on its own universal fallback. The later source-gate theorem
   establishes that H4_A1 actual clean-q atomic C=1 is empty. It does not establish
   that non-atomic H4, future producers, or global high-support C=1 are empty.
5. A header-local root chart is now tied to its proper-root parameter. The shared v1
   receipt still lacks `source_tree_scope`, `state_origin`, raw transcript and
   per-prefix terminal receipts, so this correction does not turn a type-space root
   into an actual fresh-lineage source.

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
