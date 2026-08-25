---
kind: claim
claim_id: type-II-q-one-full-carrier-first-child-absorb-entry
title: q=1 full-carrier first child 的语义 ABSORB entry
statement: >-
  Let an actual terminal-first-surviving ordinary q=1 G full-carrier root
  for p=24t+1 be consumed by its forced complete-excess bundle. On a
  target-local terminal miss, the parity-determined first child has a
  source-preserving TYPEI/ABSORB projection with provenance MARKED_ABSORB,
  support equal to 16t+2 for odd t or 9t/2 for even t, and canonical cursor
  (1,R_T-1,1) with epsilon=min, hence absorb_m=absorb_r_epsilon=1. It
  satisfies the common E3 type predicate, has the identity Sol(p) lift, and
  pays the frozen N7 CHARGED-to-ABSORB PHASE_DROP. Its E1 remains relative
  to an admitted parent root, consumed bundle and target terminal miss; this
  does not register a runtime producer or prove ABSORB re-entry.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-type-I-carrier-rail-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - absorb
  - protocol
  - terminal-first
  - E3
  - T5
  - proof-boundary
sources:
  - claim: type-II-q-one-type-I-carrier-rail-dispatch
    role: forced full bundle and parity child formulas
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: target universal p-source and anchor cursor
  - concept: t6-persistent-selector-state-v1
    role: ordinary marked-absorb type predicate
  - reproduction: reproductions/type_ii_q_one_full_carrier_first_child_absorb_entry.py
    role: parity formulas, cursor and N7 ticket controls
visibility: public
last_checked: '2026-08-25'
---

# q=1 full-carrier first-child ABSORB entry

## 1. Exact conditional input

Fix an ordinary \(q=1\) G full-carrier root which has already been admitted
from its actual phase-root predecessor and has survived its declared
root-local terminal schedule. Write

\[
p=24t+1,\qquad X=6t+1,\qquad
(R_X,K_X)=(16t+3,X(16t+1)).
\tag{1}
\]

At the universal anchor \((1,R_X-1,1)\), the complete-excess block is
forced:

\[
M=R_X-1=16t+2,\qquad (M,K_X)=1.
\tag{2}
\]

The parent is therefore a genuine path-anchored bundle input, not a chart
reconstructed from a bare prime. This card only describes the nonterminal
child **after its own target-local terminal schedule returns MISS**. A hit
remains a terminal leaf and never enters the ABSORB state space.

## 2. The two first-child charts are always low

The carrier-rail dispatch gives the following complete parity split.

For odd \(t\),

\[
R_T=20t+3,\qquad
K_T=(8t+1)(15t+1)=M\frac{15t+1}{2},\qquad
A_T=M.
\tag{3}
\]

For even \(t\), the intermediate complete-excess chart is an internal
overflow checkpoint; the actual first persistent child is the fixed-\(n\)
fold

\[
R_T=6t-1,\qquad
K_T=\frac{9t}{2}(8t-1),\qquad
A_T=\frac{9t}{2}.
\tag{4}
\]

In either case

\[
4K_T=pR_T+1,\qquad A_T\mid K_T,\qquad 3\le R_T<p.
\tag{5}
\]

For (3), the final inequality follows from
\(p-R_T=4t-2>0\). For (4), it follows from
\(p-R_T=18t+2>0\). Thus the even branch must not persist its transient
\(R>p\) checkpoint; its final chart is low just as in the odd branch.

## 3. Canonical ABSORB cursor

Apply the universal p-source theorem to the target chart (5). It gives the
actual target-side raw path

\[
\bigl(p,R_T(p-1)-p,p-1\bigr)
\longmapsto
\bigl(1,R_T-1,1\bigr).
\tag{6}
\]

The right-hand side is the formal cursor

\[
(A,B,m)=(1,R_T-1,1).
\tag{7}
\]

Because \(R_T>3\) in the q=1 G domain, the deterministic `min` direction
has

\[
\varepsilon=\min,\qquad r_\varepsilon=1.
\tag{8}
\]

Consequently the common state projection on a target terminal miss is

```text
major_phase       = TYPEI
type_i_protocol   = ABSORB
provenance_kind   = MARKED_ABSORB
is_overflow       = false
chart             = (p, R_T, K_T)
support_A          = A_T
absorb_m           = 1
absorb_r_epsilon   = 1
fresh scope        = propagated from the parent
```

By (5), (7), and (8), this passes the `TYPEI/ABSORB + MARKED_ABSORB +
R<p` grammar guard and is classified as
`type_i_absorb_marked_residual`. This is a semantic protocol conclusion;
it is not inferred merely from \(A_T\le B_p\).

## 4. E1--E5 status

Conditional on the actual admitted root, the consumed bundle in (2), and a
target terminal MISS, the entry has the following precise contract.

| Item | Status | Reason |
|---|---|---|
| E1 | relative | The root's actual path/bundle receipt is consumed; (6) supplies the target-side universal raw source. Runtime parent binding and the target terminal receipt are still required. |
| E2 | established | The parity formulas (3)--(4) determine exactly one final chart and support. |
| E3 | established pre-admission | Equations (5)--(8) give the ordinary ABSORB grammar fields and canonical cursor. |
| E4 | established | Both endpoints carry \(\operatorname{Sol}(p)\); the lift is the identity. |
| E5 | established relative to E1--E4 | The frozen N7 tuple makes `TYPEI/CHARGED -> TYPEI/ABSORB` a `PHASE_DROP`. |

For example, the parent and target tuples have the form

\[
\begin{aligned}
\Pi(S_X)&=\left(p,2,4,\left\lfloor B_p/1\right\rfloor,K_X,0,0\right),\\
\Pi(T)&=(p,2,2,R_T,1,1,0),
\end{aligned}
\tag{9}
\]

so the third coordinate strictly drops, independently of the old local
support calculation.

## 5. Boundary

The cursor \(m=1,r_{\min}=1\) does not itself supply an ABSORB successor:
the formal \(m=1\) system has a known self-loop unless a direction and a
separately valid target/rechart are supplied. Therefore this card does not
prove ABSORB re-entry, a complete target terminal schedule, an active runtime
producer, the full post-G continuation, F2/T6 totality, or the conjecture.

It resolves only the prior type mismatch: the old `CHARGED/LOCAL_DROP`
notation for the first low child is not the active Freeze-B semantic form.
On a genuine terminal miss, the correct v1 projection is the explicit
`MARKED_ABSORB` entry above.
