---
kind: claim
claim_id: type-I-f2-high-support-c1-direct-cofactor-return-v1
title: High-support C=1 direct-cofactor charts are exact same-chart returns
statement: >-
  Let p be a core prime, A>B_p=(p-1)^2/4, and let
  (p,R,K;A) be a canonical TYPEI/CHARGED high-support state with K=A and
  p<R<4A. For any direct-cofactor chart with 1<=r,C<p, positive target
  R_T, A_C=lcm(A,C), A_C|rC, and pR_T+1=4rC, the established three-phase
  identity gives h=(rC-A)/(pA) in {0,1,2}. A positive phase would force
  A<=(p-1)^2/(p+1)<p, contradicting A>B_p>p. Hence h=0, and the
  decomposition A=ga, C=gc, r=at with g=gcd(A,C) forces ct=1. Thus
  c=t=1, A_C=A, rC=A, and (R_T,rC;A_C)=(R,A;A): every admitted
  direct-cofactor action in this C=1 high-support subfamily is an exact
  arithmetic same-chart return. It cannot pay the frozen CHARGED E5 rank.
  The result excludes only this direct-cofactor action subfamily; it does
  not prove terminality, trace-unreachability, lower-protocol admission, or
  global C=1/F2/T6 closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-positive-phase-one-shot-token
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-high-support-empty-improvement-c1-local-minimum-boundary
topics:
  - type-I
  - F2
  - overflow
  - high-support
  - cofactor-one
  - direct-cofactor
  - same-chart-return
  - E5-boundary
sources:
  - claim: type-I-high-anchor-three-phase-nonreturn-window
    role: gate, phase identity, and target chart normal form
  - claim: type-I-high-anchor-positive-phase-one-shot-token
    role: positive-phase source barrier
  - claim: type-I-high-anchor-cofactor-outer-rank-composition
    role: C=1 decomposition and exact h=0 return identities
  - reproduction: reproductions/type_i_f2_high_support_c1_direct_cofactor_return.py
    role: independent algebraic replay and controls
visibility: public
last_checked: '2026-08-24'
---

# High-support C=1 direct-cofactor return

## Scope

Fix a core prime \(p\equiv1\pmod {24}\) and put

\[
B_p=\frac{(p-1)^2}{4}.
\]

The parent is a canonical charged chart

\[
pR+1=4K,\qquad K=A,\qquad A>B_p,
\qquad p<R<4A.
\]

Consider only a direct-cofactor candidate satisfying the established gate

\[
1\le r,C<p,
\qquad A_C=\operatorname{lcm}(A,C),
\qquad A_C\mid rC,
\]

and whose target chart is positive:

\[
pR_T+1=4rC,\qquad R_T>0.
\]

The candidate is assumed to have an actual source receipt when it is used as a
selector action. The arithmetic lemma below does not manufacture that receipt.

## Exact reduction

Let

\[
g=(A,C),\qquad A=ga,\qquad C=gc,
\qquad r=at,
\]

where the gate gives \(r=at\) and \(A_C=Ac\). The three-phase theorem for a
gated high-anchor cofactor chart gives

\[
h=\frac{rC-K}{pA}
 =\frac{rC-A}{pA}\in\{0,1,2\},
\qquad
R_T=R+4Ah.
\]

The positive-phase source barrier is

\[
h>0\quad\Longrightarrow\quad
A\le\frac{(p-1)^2}{p+1}<p.
\]

But (A>B_p), and (B_p>p) for every core prime (p\ge73). Therefore

\[
h>0
\quad\text{is impossible},
\qquad h=0.
\]

Now (rC=A), while the decomposition gives

\[
rC=(at)(gc)=A(ct).
\]

Consequently (ct=1), so (c=t=1). It follows that

\[
A_C=Ac=A,
\qquad r=a,
\qquad rC=A,
\qquad R_T=R.
\]

Thus the target is exactly

\[
\boxed{(p,R_T,rC;A_C)=(p,R,A;A).}
\]

No charged local coordinate decreases: the parent and target both have

\[
\Lambda_p^\sharp=(0,1),
\]

and the full T5 tuple is unchanged by the arithmetic chart return.

## Boundary

This is a subfamily result, not a C=1 closure theorem. A terminal-first hit or an
independent alternate action may still dispose of the parent. A same-chart
return can only be marked exhausted after its complete source/action/terminal
menu has been checked; a repeated arithmetic identity is not a recursive
successor. The following remain outside the claim:

- non-direct-cofactor producers, including joined reset and atomic H4 branches;
- lower-protocol or ABSORB transitions;
- outer-rank transitions;
- proof that every actual C=1 trace reaches a terminal or an alternate;
- global F2 or T6 closure.

The C1 residual therefore remains open, but its direct-cofactor branch is no
longer an unclassified paid-edge candidate.
