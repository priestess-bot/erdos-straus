---
kind: claim
claim_id: type-I-f2-high-support-c1-r-three-anchor-no-reentry
title: High-support C=1 R=3 canonical anchor has no T5-admissible re-entry
statement: >-
  Let a core-prime high-support C=1 parent take its canonical R=3
  determinant dual into a target-local terminal miss, typed TYPEI/ABSORB
  state T3=(p,3,N;N), N=(3p+1)/4. Its universal-anchor complete-excess
  continuation is uniquely U=(p,3p+4,N(p+1);2N). U is TYPEI/CHARGED,
  so T3 to U is a protocol ascent in the fixed T5 potential. Nor can H to U
  be a macro ticket: 2N<Bp while the original high-support parent has
  floor(Bp/A)=0. Thus this canonical anchor route is not a recursive
  re-entry or paid macro. The result does not exclude non-anchor raw words,
  terminals, Type II routes, or another lower-protocol exit.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-c1-canonical-dual-absorb-handoff
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - F2
  - high-support
  - cofactor-one
  - R-three
  - absorb
  - re-entry
  - T5
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f2_high_support_anchor_and_saturation_boundaries.py
    role: canonical anchor and T5 boundary replay
visibility: public
last_checked: '2026-08-25'
---

# R=3 anchor no-reentry

Let \(p=24h+1\) be core and put

\[
N=\frac{3p+1}{4}=18h+1.
\tag{1}
\]

The C=1 determinant dual is \(T_3=(p,3,N;N)\). Since \(N\) is odd, its
universal anchor is \((1,2,1)\), and the unique complete-excess block is

\[
Q=2,\qquad \beta=1,\qquad M=\operatorname{lcm}(N,2)=2N.
\tag{2}
\]

The canonical rechart therefore is

\[
U=(p,3p+4,N(p+1);2N),
\tag{3}
\]

because \(p(3p+4)+1=4N(p+1)\). Its protocol is CHARGED and its local
charged data are

\[
\left(
\left\lfloor\frac{B_p}{2N}\right\rfloor,
\frac{p+1}{2},
\eta_p
\right).
\tag{4}
\]

The ABSORB source has local data \((3,1,1)\). Hence ABSORB to CHARGED is a
T5 protocol ascent and cannot be admitted.

It also cannot be hidden inside a macro beginning at a high C=1 parent:

\[
B_p-2N=\frac{p^2-8p-1}{4}>0
\qquad(p\ge73).
\tag{5}
\]

Thus the parent has first charged coordinate zero whereas (4) has a positive
one. No parent-to-\(U\) LOCAL_DROP exists. This only excludes the canonical
anchor continuation; every non-anchor and terminal route remains in the
residual.
