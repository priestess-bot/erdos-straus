---
kind: claim
claim_id: type-I-f2-high-support-c1-r-three-terminal-g-split
title: High-support C=1 R=3 dual terminal-or-G split
statement: >-
  Let a core prime p occur in an actual terminal-first-surviving high-support
  C=1 parent. Its deterministic low dual is the R=3 chart with
  N=(3p+1)/4. If N has a prime q congruent to 2 modulo 3, the
  three-p-plus-one construction yields an explicit direct Type I certificate
  for 4/p, so this is a terminal branch before any ABSORB admission. If every
  prime divisor of N is congruent to 1 modulo 3, the R=3 chart is G and the
  corresponding N-marked two-denominator source is empty. The latter is only
  an R=3-G residual, not a proof that p has no other terminal or successor.
  Thus the C=1 dual handoff is partitioned into a direct terminal branch and
  the precise R=3-G lower-protocol residual.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-c1-canonical-dual-absorb-handoff
  - three-p-plus-one-descent-certificate
  - type-I-type-II-mod-three-double-g-exit-obstruction
topics:
  - type-I
  - F2
  - high-support
  - cofactor-one
  - R-three
  - terminal-first
  - G-state
  - factorization
  - proof-boundary
sources:
  - claim: three-p-plus-one-descent-certificate
    role: direct Type I terminal from a 2 modulo 3 factor of N
  - claim: type-I-type-II-mod-three-double-g-exit-obstruction
    role: exact R=3 G equivalence and residual boundary
  - reproduction: reproductions/type_i_f2_high_support_c1_r_three_terminal_split.py
    role: focused certificate and G controls
visibility: public
last_checked: '2026-08-24'
---

# High-support C=1 R=3 terminal-or-G split

## R=3 Dual

For a high-support C=1 parent, the canonical dual handoff constructs

\[
(R_3,K_3)=\left(3,N\right),
\qquad
N=\frac{3p+1}{4}.
\tag{1}
\]

This target is independent of the parent support. It must be terminal-first
classified before any lower-protocol target is considered.

## Direct Terminal Branch

Suppose a prime \(q\) satisfies

\[
q\mid N,
\qquad
q\equiv2\pmod3.
\tag{2}
\]

Since \(N\equiv1\pmod3\), the least such \(q\) has \(q^2\le N\). Put

\[
r=\frac{N/q+1}{3},
\qquad
m=\frac{4q+1}{3},
\qquad
x=qr,
\qquad
d=qr^2.
\tag{3}
\]

Then \(m\equiv3\pmod4\), \(3\le m\le p-2\), \(d\mid x^2\), and

\[
m\mid px+d.
\tag{4}
\]

Therefore

\[
y=\frac{px+d}{m},
\qquad
z=\frac{p(x+px^2/d)}{m}
\tag{5}
\]

are positive integers and give the direct Type I terminal

\[
\boxed{\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{6}
\]

This terminal concerns the original equation \(4/p\); no recursive
transition, owner, or ABSORB state is needed.

## R=3 G Residual

If (2) fails for every prime factor of \(N\), every prime divisor of \(N\) is
\(1\pmod3\). The \(R=3\) chart is then G, equivalently the marked
two-denominator source at denominator \(N\) is empty. Hence the exact
target-local split is

\[
\boxed{
\begin{array}{ccl}
\exists q\mid N,\ q\equiv2\pmod3
&\Longrightarrow& \mathrm{TERMINAL},\\
\forall q\mid N,\ q\equiv1\pmod3
&\Longrightarrow& \mathrm{R3\_G\_RESIDUAL}.
\end{array}}
\tag{7}
\]

The second line is not a global no-solution statement. For example,
\(p=241\) has \(N=181\) and is R=3 G, but it has an independent gap-7
Type II terminal. It only says that the particular \(N\)-source/Type-I-R=3
handoff has not terminated.

## Boundary

This claim strengthens the C=1 handoff by making one target-terminal branch
explicit. It does not create the generic ABSORB owner, resolve the R=3-G
residual, prove target re-entry, or close C=1/F2/T6.
