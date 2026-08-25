---
kind: claim
claim_id: type-II-q-one-default-tree-third-full-product-high-root-obstruction
title: The q=1 default tree cannot reach its canonical high root by a third full-product fold
statement: >-
  For the receipt-bound q=1 default-tree high-root subdomain with t>=8, and
  for its separately replayed p=73 control, the canonical first bundle and
  second primitive have carrier below 4p^2. Every exact full-product predecessor
  of the canonical root has carrier above 4p^2, so the third primitive cannot
  be a full-product fold into that root. Fixed-n, r-chart and RESET third
  primitives are likewise too small. The result leaves single-side and atomic
  complete-excess third steps open and does not create an actual fresh source,
  E1 receipt, producer or re-entry.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-canonical-root-default-entry-capacity-gap
  - type-II-q-one-canonical-root-full-product-predecessor-rigidity
  - type-II-q-one-p73-three-bundle-path-anchored-capacity-no-go
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-a-one-dual-outer-rank-reset
topics:
  - type-II
  - q-one
  - fresh-root
  - F3
  - high-endpoint
  - full-product
  - capacity-gap
  - proof-boundary
sources:
  - claim: type-II-q-one-canonical-root-default-entry-capacity-gap
    role: canonical first-two-step carrier bound
  - claim: type-II-q-one-canonical-root-full-product-predecessor-rigidity
    role: exact inverse full-product classification
  - claim: type-II-q-one-p73-three-bundle-path-anchored-capacity-no-go
    role: exceptional small-prime control
visibility: public
last_checked: '2026-08-25'
---

# Default-tree third full-product obstruction for the canonical high root

## 1. Capacity separation

Let \(p=24t+1\) be a core prime in the q=1 default-entry domain. For the
canonical root parameter \(r=t\), write

\[
g=\frac{p+1}{2},\qquad T=p^2t-g,\qquad A_\star=gT.
\tag{1}
\]

The receipt-bound default tree has, after its canonical first bundle and any
listed second primitive, a carrier

\[
M_2=A_2<4p^2.
\tag{2}
\]

An exact full-product fold into the root (1) has the rigid inverse form

\[
d\mid A_\star,\qquad 1\le d<p,\qquad
M_d=\frac{A_\star}{d}.
\tag{3}
\]

For \(t\ge8\),

\[
\frac{A_\star}{p-1}
>
\frac{p^2(pt-1)}{2(p-1)}
>4p^2.
\tag{4}
\]

Thus every carrier in (3) exceeds \(4p^2\), contradicting (2). Consequently

\[
\boxed{
\text{third canonical full-product fold to the q=1 canonical root is impossible.}
}
\tag{5}
\]

The separately replayed small control is \(p=73\). Its default first bundle
has \(A_1=50\), and the second old primitive has carrier at most \(3600\).
Here \(A_\star=590150\), whose largest divisor below \(73\) is \(58\), so
every inverse full-product predecessor has carrier at least \(10175\). Hence
(5) also holds there. This claim makes no assertion outside the stated
\(t\ge8\) subdomain and the \(p=73\) control.

## 2. Other old third primitives

The same comparison excludes the other currently named third primitives from
landing at \(A_\star\): bounded fixed-\(n\) targets satisfy \(L\le B_p<A_\star\),
r-chart admission has support at most \(B_p\), and the \(A=1\) RESET target has
both support and residual below \(p\). Atomic pending objects are not persistent
grammar arms.

This is a narrow obstruction for the existing receipt-bound menu. It does not
exclude a single-side or atomic complete-excess step with

\[
A_s\mid A_\star,\qquad
\operatorname{lcm}(A_s,Q)=A_\star,
\tag{6}
\]

nor does it turn a static inverse chart into an E1 source. Such a route must
still supply a maximal-excess occurrence, terminal prefix, fresh scope,
root-chart validator, common admission and re-entry.
