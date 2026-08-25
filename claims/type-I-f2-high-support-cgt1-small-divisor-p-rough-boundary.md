---
kind: claim
claim_id: type-I-f2-high-support-cgt1-small-divisor-p-rough-boundary
title: F2 C>=p+1 noncanonical overflow splits into small-divisor image and p-rough residual
statement: >-
  For a high-support noncanonical chart pR+1=4K, K=AC, R>p and C>=p+1,
  a proper determinant decomposition with M=Ab<K, K=M(p-d), 1<=d<p and
  n=4M-R>0 exists exactly when C has a divisor c with 2<=c<p. The
  resulting same-chart target has cofactor c and strict arithmetic charged
  descent. If no such divisor exists, the proper determinant image is empty;
  however formal p-rough charts exist for every core p, so this arithmetic
  fact proves neither TERMINAL nor FAMILY_EMPTY for the actual persistent
  source domain. E1, E3 and recursive re-entry remain open for both branches.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-noncanonical-registered-surface-boundary
  - type-I-f2-high-support-canonicality-total-cofactor-boundary
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
topics:
  - type-I
  - F2
  - high-support
  - noncanonical
  - cofactor
  - divisor-image
  - p-rough
  - source-provenance
  - terminal-boundary
  - proof-boundary
sources:
  - claim: type-I-f2-high-support-noncanonical-registered-surface-boundary
    role: bound-receipt canonicalizing image and current runtime boundary
  - claim: type-I-f2-high-support-canonicality-total-cofactor-boundary
    role: canonical/noncanonical chart identity
  - reproduction: reproductions/type_i_f2_high_support_canonicality_normalizer.py
    role: noncanonical E1-negative control
visibility: public
last_checked: '2026-08-25'
---

# Scope

Fix a core prime \(p\equiv1\pmod{24}\) and a positive chart

\[
pR+1=4K,\qquad K=AC,\qquad A>B_p:=\frac{(p-1)^2}{4},\qquad R>p,\qquad C\ge p+1.
\tag{1}
\]

This is the arithmetic domain of the F2-05a noncanonical high-support residual.
The statement below is deliberately independent of any claimed source path. It
does not turn a chart into an actual persistent state.

## Exact Proper-Image Equivalence

Call a tuple \((b,c,M,d,n)\) a **proper determinant image** of (1) when

\[
b\in\mathbb N,\quad M=Ab<K,\quad 2\le c<p,\quad d=p-c,\quad n=4M-R>0,
\tag{2}
\]

and

\[
K=Mc=M(p-d),\qquad pn=4Md+1.
\tag{3}
\]

Then a proper determinant image exists if and only if

\[
\boxed{\mathcal D(C):=\{c\in\mathbb Z:2\le c<p,\ c\mid C\}\ne\varnothing.}
\tag{4}
\]

### Forward direction

Given (2)--(3), \(C=K/A=(M/A)c=bc\), so \(c\mid C\). Since
\(M<K\), \(Ab<Abc\), hence \(c>1\); the defining range gives
\(2\le c<p\).

### Reverse direction

Take \(c\in\mathcal D(C)\), set

\[
b=\frac Cc,\qquad M=Ab,\qquad d=p-c,\qquad n=4M-R.
\tag{5}
\]

Because \(C\ge p+1>c\), \(b\ge2\), so \(M>A\) and \(M<K\). Also
\(K=AC=Mc=M(p-d)\). Using (1),

\[
\begin{aligned}
pn
 &=p(4M-R)\\
 &=4pM-(4K-1)\\
 &=4pM-4Mc+1\\
 &=4M(p-c)+1\\
 &=4Md+1>0.
\end{aligned}
\tag{6}
\]

Thus \(n\) is a positive integer and (3) holds. Since \(R>p>0\), also
\(n<4M\). The target chart is canonical because
\(4Mc=4K\equiv1\pmod p\) and \(1\le c<p\). If the determinant schema
requires a p-free carrier, the same congruence gives \(p\nmid M\).

The arithmetic charged rank therefore drops as

\[
\left(0,\frac KA\right)=(0,C)\quad\longrightarrow\quad
\left(0,\frac KM\right)=(0,c),\qquad c<C.
\tag{7}
\]

This is an E5 arithmetic comparison only. It becomes a persistent successor
only after an independently replayed source occurrence, terminal-first receipt,
projector, owner/admission record and recursive re-entry are supplied.

The excluded \(c=1\) case is exactly \(M=K,d=p-1\); its algebraic identity is
the repository's post-hoc E1 negative control.

## The p-Rough Subdomain Is Not Arithmetically Empty

The condition \(\mathcal D(C)=\varnothing\) removes all proper determinant images,
but it does not make the chart domain empty. For every core prime \(p\), choose
any prime \(q>p\), let

\[
a_0=\left\langle(4q)^{-1}\right\rangle_p\in\{1,\ldots,p-1\},\qquad
A=a_0+up>B_p
\tag{8}
\]

for a sufficiently large integer \(u\), and define

\[
C=q,\qquad K=Aq,\qquad R=\frac{4Aq-1}{p}.
\tag{9}
\]

Then \(R\) is integral, \(pR+1=4K\), and

\[
R-4A=\frac{4A(q-p)-1}{p}>0.
\tag{10}
\]

Consequently \(R>4A>p\), \(A>B_p\), \(C=q\ge p+1\), and
\(\mathcal D(C)=\varnothing\) because \(q\) is prime. For example,

\[
(p,q,A,C,K,R)=(73,151,1325,151,200075,10963)
\tag{11}
\]

is a formal p-rough chart control. It is not asserted to be an actual source,
and no terminal-first MISS is inferred from it.

Therefore the current arithmetic results cannot label the p-rough actual-source
subdomain TERMINAL or FAMILY_EMPTY. A valid closure would still require one
of:

1. a complete terminal certificate and terminal-first proof;
2. a family-empty theorem over the actual persistent source/path domain; or
3. a different source-bound producer satisfying E1--E5 and re-entry.

## Boundary

The small-divisor equivalence narrows the F2-05a problem but does not close it:

    small divisor + actual occurrence/admission: conditional same-chart route;
    small divisor without occurrence: E1 residual;
    p-rough/no small divisor: proper determinant image empty, terminal/EMPTY open.

No claim is made about F1, global producer exhaustion, F2 totality or T6.
