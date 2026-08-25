---
kind: claim
claim_id: type-I-f2-high-support-canonicality-total-cofactor-boundary
title: High-support canonicality split and noncanonical total-cofactor normalization
statement: >-
  For any Type-I/CHARGED overflow chart with K=A*C, the canonical cofactor
  c=< (4A)^(-1) >_p gives C=c+p*t. Thus R<4A exactly when 1<=C<p, while
  R>4A exactly when C>=p+1. A noncanonical high-support chart t>0 has a
  deterministic canonical total-cofactor projection with the same support and
  a strict charged local rank drop. This proves E2, identity E4 and E5 only:
  a bare chart can be reparameterized after the fact as a determinant receipt,
  so no E1/E3 producer follows without independent raw provenance and common
  admission. The F2 C=1/C>1 determinant-dual split applies only after the
  canonicality branch has been discharged.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-determinant-dual-absorb-handoff
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - t6-persistent-selector-state-v1
topics:
  - type-I
  - F2
  - high-support
  - canonical-chart
  - total-cofactor
  - well-foundedness
  - E1-E5
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f2_high_support_canonicality_normalizer.py
    role: canonical and noncanonical exact chart controls
  - claim: type-I-f2-high-support-determinant-dual-absorb-handoff
    role: determinant-dual canonical-domain boundary
visibility: public
last_checked: '2026-08-25'
---

# High-support canonicality split

Let

\[
4K=pR+1,\qquad K=AC,\qquad A>B_p:=\frac{(p-1)^2}{4},
\tag{1}
\]

be a TYPEI/CHARGED overflow chart. Define the unique canonical cofactor

\[
c=\left\langle(4A)^{-1}\right\rangle_p\in\{1,\ldots,p-1\}.
\tag{2}
\]

Since \(4AC\equiv1\pmod p\), there is a unique \(t\ge0\) such that

\[
\boxed{C=c+pt.}
\tag{3}
\]

Using \(pR+1=4AC\) gives

\[
R=4A\frac Cp-\frac1p.
\tag{4}
\]

The two excluded equalities \(C=p\) and \(R=4A\) would make
\(4AC\equiv0\pmod p\) or \(pR+1=4Ap+1\), respectively. Hence

\[
\boxed{
\begin{aligned}
R<4A&\Longleftrightarrow 1\le C\le p-1,\\
R>4A&\Longleftrightarrow C\ge p+1.
\end{aligned}}
\tag{5}
\]

The first line is the canonical domain on which the existing \(C=1\),
\(2\le C<p\), and \(d=p-C\) determinant-dual theorems are stated. It is not
an invariant of every high-support header.

## Noncanonical normalizer

When \(t>0\), define

\[
R^\circ=R-4At,\qquad K^\circ=Ac.
\tag{6}
\]

Then

\[
pR^\circ+1=4K^\circ,\qquad p<R^\circ<4A,
\tag{7}
\]

where \(R^\circ>p\) follows because \(K^\circ\ge A>B_p\), whereas a chart
with \(R^\circ<p\) would have \(K^\circ\le B_p\). The chart in (6) is the
unique canonical support-\(A\) projection and its charged rank strictly drops:

\[
(0,C,\ldots)>(0,c,\ldots).
\tag{8}
\]

Thus a real source-bound normalizer would have deterministic E2, identity E4
and E5. It remains nonrecursive until a producer supplies E1, target
terminal-first is replayed, and the common gate supplies E3/re-entry.

## Why determinant arithmetic is not E1

Every bare \(C>1\) chart in (1) admits the formal rewrite

\[
M=K,\qquad d=p-1,\qquad n=4K-R,
\tag{9}
\]

which satisfies \(pn=4Md+1\). Treating (9) as a determinant/source receipt
would manufacture a strict same-chart support update \(A\to K\) for every
such chart. This is precisely the forbidden target-derived E1 inference.
An admitted F2 producer must bind its determinant to an independently replayed
raw or complete-excess occurrence; (9) alone is an E1 negative control.

For example,

\[
(p,R,K;A)=(73,5551,101306;1369)
\tag{10}
\]

satisfies every public chart condition and \(A>B_{73}=1296\), but has
\(C=74\), \(R=4A+75\). Its canonical projection is
\((73,75,1369;1369)\) with cofactor \(1\). This is a formal control, not an
actual source or selector edge.
