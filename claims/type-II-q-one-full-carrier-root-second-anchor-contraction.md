---
kind: claim
claim_id: type-II-q-one-full-carrier-root-second-anchor-contraction
title: q=1 full-carrier root 到第二 anchor final target 的 checkpoint contraction
statement: >-
  Let an actual terminal-first-surviving ordinary q=1 G full-carrier root
  be followed through the forced first bundle and the existing second-anchor
  quotient-fold construction, while the first child and high determinant are
  retained as nonpersistent macro checkpoints. On the required intermediate
  and final terminal misses, the final target has a common v1 projection:
  it is TYPEI/CHARGED overflow when R_T>p and TYPEI/ABSORB MARKED_ABSORB
  with cursor (1,R_T-1,1) when R_T<p. Its N7 ticket computed directly from
  the root is LOCAL_DROP in the overflow case and PHASE_DROP in the low
  case. This removes the otherwise illegal persistent ABSORB-to-CHARGED
  re-entry through the old child-to-macro presentation. It remains a
  pre-admission macro interface: runtime parent binding, terminal schedules,
  T2 admission disposition, and final target re-entry are not established.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-first-child-absorb-entry
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-II-q-one-type-I-carrier-rail-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-II
  - q-one
  - full-carrier
  - macro
  - checkpoint
  - overflow
  - absorb
  - T5
  - terminal-first
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
    role: parity-specific quotient-fold final target
  - claim: type-II-q-one-full-carrier-first-child-absorb-entry
    role: low-child protocol boundary and cursor semantics
  - reproduction: reproductions/type_ii_q_one_full_carrier_root_second_anchor_contraction.py
    role: root-to-final N7 ticket and target owner controls
visibility: public
last_checked: '2026-08-25'
---

# q=1 root-to-second-anchor checkpoint contraction

## 1. Why a contraction is necessary

The first full-carrier child is low. Under the active Freeze-B grammar, a
target-terminal miss therefore projects it to `TYPEI/ABSORB`, with the
cursor established in
`type-II-q-one-full-carrier-first-child-absorb-entry`. The historical
second-anchor formula then produces a final target which is often a
`TYPEI/CHARGED` overflow. Persisting the child before running that formula
would consequently require an inadmissible same-rank

\[
\mathrm{ABSORB}\longrightarrow\mathrm{CHARGED}
\tag{1}
\]

return.

The correct object is instead a parent-to-final macro. Its forced first
child and its second-anchor high determinant are checkpoint data inside one
receipt; neither is put into the persistent queue. The root remains the
persistent source for the T5 comparison.

## 2. Input and macro path

Fix a terminal-first-surviving actual q=1 full-carrier root

\[
S_X=(p,R_X,K_X;1),\qquad p=24t+1,
\tag{2}
\]

with its unique complete-excess first block

\[
M=16t+2=R_X-1.
\tag{3}
\]

The first child is the deterministic parity chart from the carrier rail.
The existing second-anchor macro then performs:

\[
S_X
\longrightarrow H\;\text{(checkpoint)}
\longrightarrow\text{high determinant (checkpoint)}
\longrightarrow T.
\tag{4}
\]

For odd \(t\), the final carrier is

\[
L=2(10t+1).
\tag{5}
\]

For even \(t=2s\), it is

\[
L=9s q_*,
\tag{6}
\]

where \(q_*\) is the canonical least forced second-anchor excess prime
dividing \(6s-1\). In both cases the existing quotient-fold theorem gives

\[
T=(p,R_T,K_T;L),\qquad 4K_T=pR_T+1,\qquad L\mid K_T,\qquad L>1.
\tag{7}
\]

The macro must run the declared terminal priority at the root, before its
child checkpoint, and at its final target. A hit at any of these stages is a
terminal leaf. The remaining discussion is conditional on all relevant
registered terminal schedules returning MISS.

## 3. Final target type without an upward protocol return

There are two cases, decided from the final chart rather than from an
intermediate label.

### 3.1 High final target

If \(R_T>p\), set

```text
major_phase       = TYPEI
type_i_protocol   = CHARGED
provenance_kind   = OVERFLOW
is_overflow       = true
support_A          = L
```

This is an existing ordinary overflow shape. Because \(L>1\), its T5
potential compares directly with the root:

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{1}\right\rfloor=B_p.
\tag{8}
\]

Thus root-to-final admission has the direct ticket

\[
\boxed{\mathrm{LOCAL\_DROP}.}
\tag{9}
\]

No potential of the nonpersistent child is used in (8).

### 3.2 Low final target

If \(R_T<p\), the universal p-source gives the final anchor

\[
(1,R_T-1,1).
\tag{10}
\]

As in the first-child entry, choose `min`, so

\[
\texttt{absorb_m}=1,\qquad
\texttt{absorb_r_epsilon}=1.
\tag{11}
\]

The final projection is `TYPEI/ABSORB + MARKED_ABSORB`, and the root-to-final
tuple is

\[
\Pi(S_X)=\left(p,2,4,B_p,K_X,0,0\right)
>
\left(p,2,2,R_T,1,1,0\right)=\Pi(T).
\tag{12}
\]

Hence this case has the direct ticket

\[
\boxed{\mathrm{PHASE\_DROP}.}
\tag{13}
\]

Again, it never needs a persistent intermediate ABSORB state.

## 4. Contract status

| Item | Status | Scope |
|---|---|---|
| E1 | relative | Concatenate the actual root receipt, forced first bundle, second-anchor path and quotient-fold data; common runtime parent/digest binding remains absent. |
| E2 | established | (5)--(7) and the least-prime tie break determine one final chart. |
| E3 | established pre-admission | (7), then the high/low split and (10)--(11), select existing v1 final owners. |
| E4 | established | All macro stages retain \(\operatorname{Sol}(p)\), so the parent-to-final lift is the identity. |
| E5 | established pre-admission | (8)--(9) or (12)--(13) compares the true persistent root with the final target. |

The distinction from the old child-to-final formulation is essential: that
form compared T5 ranks against a child now typed ABSORB, while the present
macro compares the root and final target only.

## 5. Boundary

This is not an active atomic arm or a registered runtime producer. Before it
can enter the queue, the project still needs to prove and bind all of:

1. actual parent `state_id` and source/path receipt through (4);
2. the three ordered terminal schedule outcomes;
3. the appropriate T2/admission disposition for this checkpointed macro;
4. the final target's recursive runtime route.

The contraction removes a protocol inconsistency; it does not close the
post-G selector, F2, T6, or the conjecture.
