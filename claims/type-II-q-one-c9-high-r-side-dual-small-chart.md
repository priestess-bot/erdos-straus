---
kind: claim
claim_id: type-II-q-one-c9-high-r-side-dual-small-chart
title: q=1 C=9 high target 的确定性 r-side dual 至 R=11/23/35
statement: >-
  For the q=1 odd low-final third-anchor C=9 high target at p=336k+25,
  let r be its support modulo p, equivalently the inverse of 36 modulo p.
  The canonical r-side determinant dual is the strictly smaller of the two
  symmetric dual charts and is one of (R,K;A)=(23,(23p+1)/4,(23p+1)/36),
  (35,(35p+1)/4,(35p+1)/36), or
  (11,(11p+1)/4,(11p+1)/36) as k is 0, 1, or 2 modulo 3. On a terminal
  miss it has a TYPEI/ABSORB projection with cursor (1,R-1,1) and a
  CHARGED-to-ABSORB PHASE_DROP. This is a relative source-preserving
  contraction of the q=1 C=9 macro, not a proof that these R=11/23/35
  states have total successors.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-odd-low-final-third-anchor-contraction
  - type-I-f2-high-support-determinant-dual-absorb-handoff
  - type-I-universal-p-source-capacity-anchor-orbit
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-II
  - q-one
  - cofactor-nine
  - determinant-dual
  - R-eleven
  - R-twenty-three
  - R-thirty-five
  - absorb
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_q_one_c9_high_r_side_dual_small_chart.py
    role: exact r-side dual and protocol-ticket controls
visibility: public
last_checked: '2026-08-25'
---

# q=1 C=9 high r-side dual

## 1. C=9 source

On the remaining odd q=1 class \(p=336k+25\), the third-anchor contraction
has the high chart

\[
H_9=(p,R_9,K_9;M),
\qquad
R_9=1200k+95,
\qquad
K_9=9M,
\tag{1}
\]

with

\[
M=2(140k+11)(40k+3),
\qquad 36M-1=pR_9.
\tag{2}
\]

Thus the support residue is the inverse of \(36\) modulo \(p\):

\[
r:=M\bmod p,\qquad 36r\equiv1\pmod p.
\tag{3}
\]

The high cofactor is \(C=9\), so the determinant dual has

\[
d=p-9,\qquad K_r=r(p-d)=9r.
\tag{4}
\]

## 2. Fixed small r-side chart

Write \(R_r=(36r-1)/p\). Since

\[
4K_r=36r=pR_r+1,
\tag{5}
\]

it is the r-side canonical dual chart. The residue of \(p\) modulo \(36\)
is determined by \(k\bmod3\), giving

\[
\begin{array}{c|c|c|c}
k\bmod3&p\bmod36&R_r&r\\ \hline
0&25&23&(23p+1)/36\\
1&1&35&(35p+1)/36\\
2&13&11&(11p+1)/36.
\end{array}
\tag{6}
\]

All three charts are low. To see that this is the canonical selected side,
let \(R_d\) be the d-side dual. The symmetric-dual identities give

\[
R_d-R_r=4(d-r).
\tag{7}
\]

For \(R_r\in\{11,23\}\), equation (6) gives \(r<d\) immediately for
every core prime. In the \(R_r=35\) case,

\[
d-r=\frac{p-325}{36}>0.
\tag{8}
\]

Here \(k\equiv1\pmod3\) gives \(p\equiv361\pmod {1008}\); the only
smaller positive representative \(361=19^2\) is not prime. Thus every core
prime in this row has \(p>325\). Equations (7)--(8) show that the r-side
chart is strictly smaller than the d-side chart.

## 3. Protocol projection

Each row of (6) satisfies \(3\le R_r<p\), \(r\mid K_r\), and has the
universal target-side raw source ending at

\[
(1,R_r-1,1).
\tag{9}
\]

On a target-local terminal MISS, set

\[
\texttt{absorb_m}=1,
\qquad
\texttt{absorb_r_epsilon}=1
\tag{10}
\]

with the `min` direction. The target is therefore a semantic
`TYPEI/ABSORB + MARKED_ABSORB` state, not a low CHARGED state.

The C=9 source is `TYPEI/CHARGED`, so after all E1--E4 receipt fields are
bound, the N7 ticket is automatically

\[
\boxed{\mathrm{PHASE\_DROP}.}
\tag{11}
\]

The q=1 root, its third-anchor C=9 chart, and this r-side chart can be kept
as a parent-to-final checkpoint macro, avoiding any persistent high-to-low
intermediate state whose source provenance is not yet registered.

## 4. Boundary

This result makes the C=9 output a finite low-chart problem with
\(R\in\{11,23,35\}\). Existing fixed-\(R\) terminal and descent families
may be applied only after their own guards are rechecked. They do not cover
all three rows automatically. In particular, this card does not prove a
terminal, an ABSORB re-entry, a shared runtime producer, F2 totality, T6
totality, or the conjecture.
