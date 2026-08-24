---
kind: claim
claim_id: type-I-f2-high-support-determinant-dual-absorb-handoff
title: Canonical high-support determinant dual gives a deterministic low-chart handoff
statement: >-
  Let H=(p,R,AC;A) be an actual terminal-first-surviving canonical
  TYPEI/CHARGED high-support overflow, where p is a core prime,
  A>B_p=(p-1)^2/4, 1<=C<p, and p<R<4A. Put d=p-C, n=4A-R,
  r=A mod p, k=(A-r)/p, and s=n-4kd. Then pn=4Ad+1 and
  ps=4rd+1. The two symmetric determinant duals are
  (R_d,K_d)=(4d-s,d(p-r)) and
  (R_r,K_r)=(4r-s,r(p-d)); both are positive canonical charts and
  min(R_d,R_r)<p. Selecting the smaller R with d-side tie break gives a
  target-independent deterministic low chart. A new producer that binds an
  actual parent, runs target terminal-first, constructs an E3 state with a
  valid lower-protocol cursor, and chooses semantic TYPEI/ABSORB on a miss
  would have identity Sol(4,p) lift and a CHARGED-to-ABSORB phase drop.
  This is a conditional target-shape handoff only: source-event provenance,
  E3, target typing, and ABSORB re-entry remain open.
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-outer-rank-reset
  - type-I-t5-full-contract-level-global-well-foundedness
  - t6-persistent-selector-state-v1
topics:
  - type-I
  - F2
  - overflow
  - high-support
  - determinant-dual
  - low-chart
  - absorb
  - phase-drop
  - proof-boundary
sources:
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: determinant-dual identities and low-chart existence
  - concept: t5-global-well-foundedness-contract-v2
    role: CHARGED-to-ABSORB phase order
  - reproduction: reproductions/type_i_f2_high_support_determinant_dual_absorb_handoff.py
    role: independent exact dual reconstruction
visibility: public
last_checked: '2026-08-24'
---

# High-support determinant dual handoff

## Exact Domain

Fix a core prime \(p\equiv1\pmod {24}\), and let

\[
H=(p,R,K;A,\sigma),
\qquad
K=AC,
\qquad
A>B_p:=\frac{(p-1)^2}{4},
\qquad
1\le C<p,
\tag{1}
\]

be a canonical high-support overflow chart:

\[
p<R<4A,
\qquad
pR+1=4AC.
\tag{2}
\]

The parent must be actual and terminal-first surviving if this construction is
ever used as a producer. The lemma proves only the deterministic arithmetic
target generated from its chart facts.

Put

\[
d=p-C,
\qquad
n=4A-R.
\tag{3}
\]

Then

\[
\boxed{pn=4Ad+1.}
\tag{4}
\]

Write \(A=kp+r\) with \(1\le r<p\). The strict lower bound on \(r\) follows
from \(4AC\equiv1\pmod p\). Define

\[
s=n-4kd.
\tag{5}
\]

Substitution in (4) gives

\[
\boxed{ps=4rd+1.}
\tag{6}
\]

In particular \(s>0\), \(s<4d\), and \(s<4r\).

## Deterministic Low Chart

The symmetric duals from (6) are

\[
\begin{aligned}
R_d&=4d-s,& K_d&=d(p-r),\\
R_r&=4r-s,& K_r&=r(p-d).
\end{aligned}
\tag{7}
\]

They satisfy

\[
pR_d+1=4K_d,
\qquad
pR_r+1=4K_r,
\qquad
d\mid K_d,
\qquad
r\mid K_r.
\tag{8}
\]

Both coordinates are positive and congruent to \(3\pmod4\). At least one is
strictly below \(p\). If both exceeded \(p\), then (8) would imply

\[
4d(p-r)>p^2,
\qquad
4r(p-d)>p^2.
\]

After multiplication this gives

\[
16\frac dp\left(1-\frac dp\right)
\frac rp\left(1-\frac rp\right)>1,
\]

which is impossible because each factor \(x(1-x)\) is at most \(1/4\).
Equality with \(p\) is excluded by \(R_t\equiv3\pmod4\) and
\(p\equiv1\pmod4\).

Define the canonical side without a factor choice:

\[
t=
\begin{cases}
d,&R_d\le R_r,\\
r,&R_r<R_d,
\end{cases}
\qquad
(R_\star,K_\star)=
\begin{cases}
(R_d,K_d),&t=d,\\
(R_r,K_r),&t=r.
\end{cases}
\tag{9}
\]

Then

\[
\boxed{
3\le R_\star\le p-2,
\qquad
pR_\star+1=4K_\star,
\qquad
t\mid K_\star.
}
\tag{10}
\]

Thus (9) is a target-independent low-chart constructor on the declared
arithmetic domain.

## Conditional Lower-Protocol Handoff

The target must first run target-local terminal-first rules. On a target
terminal it returns a direct terminal. On a target miss, the proposed
recursive interpretation is

\[
\mathrm{TYPEI/CHARGED}
\longrightarrow
\mathrm{TYPEI/ABSORB}.
\tag{11}
\]

This would use the identity map on \(\operatorname{Sol}(4,p)\) and the frozen
protocol drop for E5. It is not an active edge because the following remain
unproved:

1. a producer-specific E1 source event which turns the chart-derived
   determinant into an authorized successor construction;
2. target-local terminal/F/G typing and a generic ordinary E3 owner;
3. a replayable ABSORB cursor \((m,r_\varepsilon)\), not merely \(R_\star<p\);
4. an ABSORB re-entry theorem which never returns upward at the same equation
   rank.

The special \(C=1\) case has \(r=(3p+1)/4\), and (9) selects
\(R_\star=3\), so the C=1 handoff is a specialization.

## Boundary

This result does not assert that every high-support F/G source carries an
admitted determinant-dual producer, that a low dual is terminal, or that the
low chart has a current selector family. It supplies a deterministic target
and isolates the remaining E1/E3/re-entry work; it does not close C=1, C>1,
F2, T6, or the conjecture.
