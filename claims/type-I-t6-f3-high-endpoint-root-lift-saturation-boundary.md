---
kind: claim
claim_id: type-I-t6-f3-high-endpoint-root-lift-saturation-boundary
title: F3 high stutter root-lift saturation and divisor-gate boundary
statement: >-
  Let a core high-stutter static datum satisfy M=(p^2+p+1)/3=uv,
  h=3u>p, gcd(D,M)=1, D divides ph+1, and D is congruent to 1-h
  modulo p. Put A_0=u(p^2-1)/4 and D_K=D/gcd(D,A_0). Then the
  condition D divides K for a root parameter omega is exactly
  omega = 3v(p^2)^(-1) modulo D_K. There are infinitely many positive
  odd omega with gcd(omega,v)=1 in that class. Each gives a root r,
  a formal chart with D dividing K and R-h, and the same root/capacity
  divisor gates. Therefore those gates alone cannot bound or empty a
  high k=1 or odd-k stutter curve; canonical maximal-receipt valuations,
  terminal-first, or actual source/admission data must add a nonperiodic
  condition. This is a boundary theorem, not an actual-state existence or
  T6 closure claim.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-high-endpoint-stutter-divisor-gates-v1
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-t6-f3-high-endpoint-k-one-pell-residual-v1
topics:
  - type-I
  - root-capacity
  - f3
  - high-endpoint
  - stutter
  - divisor-gate
  - CRT
  - periodicity
  - proof-boundary
sources:
  - claim: type-I-t6-f3-high-endpoint-stutter-divisor-gates-v1
    role: high-domain root and capacity gate identities
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual receipt gives gcd(D,M)=1
  - reproduction: reproductions/type_i_t6_f3_high_endpoint_root_lift_saturation.py
    role: exact root-lift and periodicity controls
visibility: public
last_checked: '2026-08-25'
---

# F3 high stutter root-lift saturation

## 1. Scope

This is a negative structural result about the arithmetic data used by the
two high-stutter divisor gates. It deliberately retains the distinction
between a static root chart and an actual persistent state.

Let

\[
p\equiv1\pmod {24},\qquad
M=\frac{p^2+p+1}{3}=uv,\qquad h=3u>p,
\tag{1}
\]

and fix a positive integer \(D\) satisfying

\[
(D,M)=1,\qquad D\mid ph+1,\qquad D\equiv1-h\pmod p.
\tag{2}
\]

Every actual high stutter receipt supplies (1)--(2): the first condition in
(2) is the cyclotomic exclusion for the actual normalized \(D\). The
argument below does **not** reverse that implication. In particular it does
not prove that an arbitrary datum satisfying (1)--(2) is canonical,
terminal-first surviving, persistent, or reachable.

Write

\[
A_0=\frac{u(p^2-1)}4,\qquad
D_K=\frac{D}{(D,A_0)}.
\tag{3}
\]

Since \((D,u)=1\), this is equivalently

\[
D_K=\frac{D}{\left(D,(p^2-1)/4\right)}.
\tag{4}
\]

## 2. Exact root-lift congruence

For any positive odd \(\omega\) with \((\omega,v)=1\), set

\[
r=\frac{u\omega-1}{2},\qquad
K=A_0\bigl(p^2\omega-3v\bigr),\qquad
R=\frac{4K-1}{p}.
\tag{5}
\]

The last expression is integral: modulo \(p\),

\[
4K\equiv(-1)u(-3v)=3uv=p^2+p+1\equiv1.
\tag{6}
\]

Moreover

\[
(2r+1,M)=(u\omega,uv)=u.
\tag{7}
\]

These are the standard root-chart formulas: substituting the displayed
\(r\) into the root-capacity source expression gives

\[
R=2p^3r-p^2-2pr-p+1,
\qquad R\equiv1\pmod p.
\tag{7a}
\]

The capacity condition is exactly one congruence:

\[
\begin{aligned}
D\mid K
&\Longleftrightarrow D_K\mid p^2\omega-3v\\
&\Longleftrightarrow
\boxed{\omega\equiv3v(p^2)^{-1}\pmod {D_K}}.
\end{aligned}
\tag{8}
\]

Indeed, after dividing \(D\mid A_0(p^2\omega-3v)\) by
\((D,A_0)\), the remaining modulus is coprime to the remaining coefficient.
Also \((p,D_K)=1\), because \(D\mid ph+1\), and \((v,D_K)=1\), because
\((D,M)=1\).

Let \(\bar\omega\) be the residue in (8). The simultaneous conditions

\[
\omega\equiv\bar\omega\pmod {D_K},\qquad
\omega\equiv1\pmod {2v}
\tag{9}
\]

are compatible. Their moduli have greatest common divisor at most \(2\);
if it is \(2\), then \(\bar\omega\) is odd because \(p\) and \(v\) are
odd. The Chinese remainder theorem therefore gives a positive odd solution
with \((\omega,v)=1\).

For such a solution, (5) gives \(D\mid K\). Since

\[
p(R-h)=4K-(ph+1),
\tag{10}
\]

it also gives \(D\mid R-h\). The stutter congruence and (7a) give

\[
R-h\equiv D\equiv1-h\pmod p,\qquad
\frac{R-h}{D}\equiv1\pmod p.
\tag{11}
\]

Equation (11) is only a formal raw quotient. It does not assert that this
quotient is the actual maximal complete-excess \(E\).

## 3. Infinite periodic family

If \(\omega\) is any solution of (8)--(9), then for every \(t\ge0\),

\[
\omega_t=\omega+2D_Kvt
\tag{12}
\]

is again positive and odd, satisfies \((\omega_t,v)=1\), and has the same
residue modulo \(D_K\). Hence all corresponding root parameters \(r_t\)
satisfy

\[
(2r_t+1,M)=u,\qquad D\mid K_t,\qquad D\mid R_t-h.
\tag{13}
\]

The root-quotient divisor gate depends only on \((p,h,D,m)\), while the
capacity gate follows from (13). Thus both high divisor gates persist along
the infinite family. So do all high normal-form quantities determined only
by \((p,h,D,m,e,a,k)\), including the split into the \(k=1\) Pell and odd
\(k\ge3\) residuals.

This proves a precise limitation: a proof that only adds consequences of
\(D\mid ph+1\), \(D\mid K\), and the stutter congruence cannot obtain a
global bound on \(r\), nor prove either residual family empty. A valid next
argument must use information not invariant under (12), such as the
prime-by-prime canonical maximal-receipt valuation, terminal-first, or a
source/path/admission restriction.

## 4. Why the low k=1 Vieta descent does not transfer

The high \(k=1\) parameter surface has

\[
y^2+xy-x^2=c(dxy-1),\qquad d\equiv2\pmod3,
\quad c\equiv1\pmod3,\quad 3\mid y,\quad3\nmid x.
\tag{14}
\]

As a quadratic in \(y\), its other root is

\[
y^\sharp=(cd-1)x-y.
\tag{15}
\]

Modulo \(3\), (15) is \(y^\sharp\equiv x\not\equiv0\). It therefore
does not preserve the high parameter domain. As a quadratic in \(x\), the
other root is \(-(cd-1)y-x<0\). This gives a direct structural reason that
the low-height \(k=1\) Vieta descent cannot simply be reused in the high
slice.

## 5. Fixed core control

The high \(k=1\) curve control

\[
(d,x,y)=(11,101,1020)
\tag{16}
\]

has

\[
\begin{aligned}
p&=115815206209,& h&=1169617882071,\\
D&=1207185892628946440,& v&=11467986421,\\
D_K&=30179647315723661,& \omega&=3161408027583.
\end{aligned}
\tag{17}
\]

It satisfies all static root, stutter, and two-gate identities above, and
(12) supplies further lifts. It remains outside the actual residual
quantifier: its \(D\) is not established as the canonical maximal receipt,
and the root is preempted by the gap-3 terminal factor \(8363\). The
control therefore tests the boundary rather than witnessing an actual
terminal-first survivor.

## Boundary

This claim does not construct an E1--E5 edge, prove an actual high stutter
state exists, close \(k=1\), close odd \(k\), or change F3/T6 from `OPEN`.
It rules out only a narrower strategy: treating more static divisor-gate
manipulation as a family-empty proof.
