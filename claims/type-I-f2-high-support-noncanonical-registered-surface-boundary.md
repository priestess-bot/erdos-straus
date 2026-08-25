---
kind: claim
claim_id: type-I-f2-high-support-noncanonical-registered-surface-boundary
title: F2 noncanonical high-support headers are preempted on the bound-receipt and registered surfaces
statement: >-
  Let S=(p,R,K;A) be a TYPEI/CHARGED overflow with A>B_p and C=K/A>=p+1.
  If S has a source-bound determinant receipt (M,d,n) with pn=4Md+1,
  R=4M-n, K=M(p-d), M=Ab and 1<=d<p, then b>=2 and the same-chart
  support-promotion target (p,R,K;M) has canonical cofactor p-d in [1,p-1]
  and a strict local charged-rank drop.  Separately, every currently known
  determinant-style arithmetic target constructor has target cofactor in
  [1,p-1] or is not an overflow target.  These are surface-bounded statements;
  they do not prove that all semantic producers or future unregistered sources
  avoid F2-05a.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-canonicality-total-cofactor-boundary
  - type-I-f2-overflow-determinant-prepartition
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
topics:
  - type-I
  - F2
  - high-support
  - noncanonical
  - determinant
  - source-bound
  - proof-boundary
sources:
  - claim: type-I-f2-high-support-canonicality-total-cofactor-boundary
    role: canonical/noncanonical chart split
  - claim: type-I-f2-overflow-determinant-prepartition
    role: source-bound determinant dichotomy
  - reproduction: scripts/t6_q_one_full_carrier_runtime_slice_v1.py
    role: active runtime target surface
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: known determinant constructor image surface
visibility: public
last_checked: '2026-08-25'
---

# F2 noncanonical high-support boundary

The noncanonical branch \(C=K/A\ge p+1\) is a real chart-level possibility,
but it is not an independent obstruction whenever a bound determinant receipt
is already present.

## Bound-receipt lemma

Assume

\[
pn=4Md+1,
\quad R=4M-n,\quad K=M(p-d),\quad M=Ab,\quad 1\le d<p.
\tag{1}
\]

Since \(C=K/A\),

\[
C=b(p-d).
\tag{2}
\]

If \(C\ge p+1\), then \(b\ge2\), because \(p-d\le p-1\). The ordered
determinant prepartition therefore places this source in the earlier
same-chart support-promotion branch. Its target support is \(M\), and

\[
C_T=K/M=p-d\in\{1,\ldots,p-1\}.
\tag{3}
\]

The identity (pn=4Md+1) gives

\[
p(4M-n)+1=4M(p-d)=4K,
\]

so the target chart is canonical. Because \(M=bA>A>B_p\), both parent and
target have first local charged coordinate zero, while (3) strictly lowers
the second coordinate:

\[
(0,p-d)<(0,C).
\tag{4}
\]

Equation (4) is the arithmetic E5 comparison. It becomes a verified edge only
when the determinant receipt, common projector, admission and re-entry are
actually supplied.

## Exact divisor-image split

There is a sharper purely arithmetic statement for a fixed noncanonical chart.
Assume \(pR+1=4K\), \(K=AC\), \(R>p\), and \(C=K/A\ge p+1\).
A proper determinant decomposition with \(M=Ab<K\)
is equivalent to a divisor

\[
c\mid C,\qquad 2\le c<p.
\tag{5}
\]

Indeed, a decomposition (1) has \(c=p-d\), so \(C=bc\), \(M=Ab\), and
\(M<K\) is equivalent to \(b<C\), hence to \(c>1\). Conversely, from a
divisor in (5), define

\[
b=C/c,\qquad M=Ab,\qquad d=p-c,\qquad n=4M-R.
\tag{6}
\]

Using \(K=Mc=M(p-d)\) and \(pR+1=4K\),
\[
pn=p(4M-R)=4pM-(4K-1)=4Md+1>0.
\tag{7}
\]

Thus (6) is an exact arithmetic determinant decomposition and its same-chart
target has cofactor \(C_T=c\). Removing the forbidden post-hoc case
\(c=1,\ M=K,\ d=p-1\), a proper decomposition exists if and only if the
small-divisor set in (5) is nonempty.

This equivalence is deliberately not E1: choosing a divisor \(c\) reconstructs
an arithmetic decomposition, but it does not create an actual raw occurrence,
parent receipt or admission. It splits F2-05a into the two exact residual
forms: a small divisor with no source-bound occurrence/admitted same-chart
owner, or no small divisor \(2\le c<p\) of \(C\) at all.

## Known constructor image

On the current registered arithmetic surface, the determinant-style builders
use one of the following target forms:

\[
K_T=L(p-d),\quad K_T=L(p-r),\quad K_T=L(p-S/L),
\tag{8}
\]

with the corresponding positivity guards \(1\le d,r,S/L<p\). Same-chart
promotion has the same \(K_T=M(p-d)\) form. The q=1 runtime root starts with
\(A=1\); its contraction targets use (5), and its optional third-anchor target
has fixed cofactor \(C_T=9\), with \(9<p\) on the declared branch. The q=1
relay targets have cofactor at most (p-1) (or (p-2) before regeneration).
Thus the image of the currently executable runtime contains no state with

\[
A>B_p,\ C\ge p+1.
\tag{6}
\]

This is an induction over that concrete runtime queue, not over the semantic
state space. The constructor inventory still records unregistered source
signals and missing shared serializers, so (6) cannot be promoted to a global
unreachability theorem.

## Exact residual wording

The remaining F2-05a quantifier should therefore be read as

```text
actual persistent noncanonical overflow
with either a proper small divisor but no source-bound occurrence/admitted
same-chart owner, or no small divisor 2<=c<p of C.
```

It is not legitimate to count a source that already has (1) as a separate
noncanonical-normalizer gap while simultaneously ignoring the earlier
same-chart branch. Conversely, the current runtime result does not close the
semantic F2 family, because F1 producer coverage is not complete.
