---
kind: claim
claim_id: type-I-t6-f3-r6-dyadic-companion-full-capacity-pfree
title: R6 dyadic atomic companion has a p-free full-capacity raw continuation
statement: >-
  In an actual source-bound low R6 dyadic-fresh endpoint with 2<=h<p and
  R congruent to 1 modulo p, after the first q=2 child is p-free and the
  initial child and every internal W_y prefix all return terminal-first MISS,
  suppose the opposite side has Q_y>1 and
  F_y=W_y*J_y is congruent to 2^mu modulo p. With the same K=A(p-1),
  dyadic valuation shape forces W_y != delta=(h+1)/2. Therefore the complete
  W_y raw word reaches Y_K=(y,K) with a p-free primitive endpoint; its
  arithmetic classification is terminal when the complement divides K or
  single-side complete-excess otherwise, never a genuine atomic endpoint.
  This is a conditional source-bound raw/E2 reduction only: canonical
  companion support, E3/E4/E5, admission and re-entry remain open.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-tr1-fresh-dstar-endpoint-split
  - type-I-t6-f3-qc1-endpoint-excess-deflation
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
topics:
  - type-I
  - F3
  - R6
  - TR1
  - dyadic
  - atomic
  - complete-excess
  - p-free
  - proof-boundary
sources:
  - claim: type-I-t6-f3-tr1-fresh-dstar-endpoint-split
    role: source-bound fresh-factor and primitive-child hypotheses
  - reproduction: reproductions/type_i_f3_r6_dyadic_companion_boundary.py
    role: fixed arithmetic identities and scope controls
visibility: public
last_checked: '2026-08-25'
---

# R6 dyadic companion full-capacity continuation

Assume the actual source-bound low R6 hypotheses, including
\(2\le h<p\), \(m>3\), \(R\equiv1\pmod p\), and a p-free dyadic
fresh first child:

\[
x=z/2,\qquad y=R-x,
\tag{1}
\]

The initial child and every internal prefix of the fixed occurrence-ordered
\(W_y\) word have terminal-first MISS receipts. Let \(K=A(p-1)\), write
\(\lambda=v_2(p-1)\), and suppose the opposite side has

\[
Q_y>1,\qquad
F_y=\frac{Q_y}{(A,Q_y)}\equiv2^\mu\pmod p,
\tag{2}
\]

where \(\mu=1\) or \(\lambda+1\) is the dyadic capacity exponent. Define

\[
W_y=\prod_{v_q(y)>v_q(K)}q^{v_q(y)-v_q(K)},
\qquad
J_y=(Q_y,p-1),
\qquad F_y=W_yJ_y.
\tag{3}
\]

The dyadic shape gives

\[
v_2(h-1)=1,\qquad v_2(h+1)=\lambda,\qquad
h+1=2^\lambda H,\quad H\text{ odd}.
\tag{4}
\]

Since \(y\) and \(Q_y,J_y,W_y\) are odd, \(J_y\mid n\) where
\(p-1=2^\lambda n\), \(n\) is odd. Write \(n=J_yL\). Also
\(H\le J_yL\) because \(h<p\).

Put \(\delta=(h+1)/2=2^{\lambda-1}H\). If \(W_y\equiv\delta\pmod p\),
then (2) gives \(J_y\delta\equiv2^\mu\pmod p\). Multiplication by \(2L\)
and \(2^\lambda J_yL=p-1\equiv-1\pmod p\) yields

\[
p\mid H+2^{\mu+1}L.
\tag{5}
\]

For \(\mu=1\), \(H+4L\le(J_y+4)L<p\), since
\((2^\lambda-1)J_y>4\). For \(\mu=\lambda+1\), (5) becomes
\(p\mid H+4\cdot2^\lambda L\). If \(J_y\ge5\), the same size bound follows
from \((2^\lambda-1)J_y-4\cdot2^\lambda\ge3\). If \(J_y=1\), writing
\(H=(t-4)2^\lambda L+t\) gives either \(H<0\), even \(H=4\), or
\(H>L\). If \(J_y=3\), writing
\(H=(3t-4)2^\lambda L+t\) gives either \(H<0\) or \(H>3L\). All cases
contradict \(0<H\le J_yL\) and oddness. Hence

\[
\boxed{W_y\not\equiv\delta\pmod p.}
\tag{6}
\]

Along the fixed nondecreasing occurrence order, run terminal-first at every
internal prefix. If any prefix is a terminal HIT, return that terminal
immediately. If all prefixes MISS, the deterministic full-capacity raw word
strips all \(W_y\) and reaches

\[
Y_K=(y,K),
\tag{7}
\]

Since \(x=(R-h)/2\) and \(R\equiv1\pmod p\), the opposite child satisfies
\(y=R-x\equiv(h+1)/2=\delta\pmod p\). Therefore
\(p\mid R-Y_K\) is equivalent to \(W_y\equiv\delta\pmod p\), excluded by
(6), so the complement \(R-Y_K\) is \(p\)-free. Since \(Y_K\mid K\), its
canonical excess block is empty. The endpoint is therefore either a direct
Type-I terminal (if the complement also divides \(K\)) or a one-sided
complete-excess endpoint. It is never a genuine two-sided atomic endpoint
after this full word.

The raw word is source-bound and primitive under the assumed path receipt.
The fixed occurrence order makes the word deterministic; an internal terminal
would preempt the next occurrence by hypothesis. Its canonical support/rank
still requires capacity-aware recomputation; no
claim here supplies a persistent target, common E3 admission, universal E4,
parent-to-final E5 or recursive re-entry.
