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
  high k=1 or odd-k stutter curve. An explicit subprogression also preserves
  the canonical maximal-receipt divisor and the root-bottom terminal miss.
  A valid exclusion must instead use a full valuation predicate proved
  nonrecurrent, a complete terminal-first schedule, or actual
  source/admission data. This is a boundary theorem, not an actual-state
  existence or T6 closure claim.
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

This proves a first precise limitation: a proof that only adds consequences
of \(D\mid ph+1\), \(D\mid K\), and the stutter congruence cannot obtain a
global bound on \(r\), nor prove either residual family empty.

### 3.1 Canonical receipt saturation

The preceding lift can be refined; canonical maximality by itself is not a
periodicity breaker. Suppose the initial chart has its canonical
complete-excess normalization

\[
z_0=R_0-h=E_0D,
\qquad Q_0>1,
\tag{14}
\]

where the same \(D\) in (2) is the actual canonical divisor. Set

\[
\mathcal A_j=\frac{K_j}{p-1},
\qquad H=ph+1,
\qquad L=(\mathcal A_0K_0z_0H)^2,
\tag{15}
\]

and replace (12) by the subprogression

\[
\omega_j=\omega_0+2D_KvLj.
\tag{16}
\]

It remains odd and primitive modulo \(v\), while direct substitution in
(5) gives

\[
\begin{aligned}
r_j-r_0&=MD_KLj,\\
\mathcal A_j-\mathcal A_0
 &=\frac{M(p+1)p^2D_K}{2}Lj,\\
K_j-K_0
 &=\frac{M(p^2-1)p^2D_K}{2}Lj,\\
z_j-z_0&=2Mp(p^2-1)D_KLj.
\end{aligned}
\tag{17}
\]

Consequently, for every prime \(q\mid H\), the three valuations

\[
v_q(\mathcal A_j),\qquad v_q(K_j),\qquad v_q(z_j)
\tag{18}
\]

equal their values at \(j=0\). Indeed, the square in (15) makes every
increment in (17) divisible by a strictly higher \(q\)-power than the
corresponding nonzero base value, and by \(q\) when the base value is a
unit.

For any canonical complete-excess divisor \(D_j\), its receipt formula
gives \(D_j\mid K_j\) and \(D_j\mid z_j\). Since

\[
pz_j=4K_j-H,
\tag{19}
\]

we have \(D_j\mid H\). The prime-by-prime normalization formula for
\(D_j\) depends only on the three valuations in (18), so (18)--(19) imply

\[
\boxed{D_j=D\quad(j\ge0).}
\tag{20}
\]

Thus the canonical stutter cofactor remains \(p-1\), and all normal-form
data determined by \((p,h,D)\), including the \(k=1\) versus odd
\(k\ge3\) split, are unchanged. The root-bottom terminal miss is also
preserved: if a lifted chart had \(Q_j=1\), then its canonical divisor would
be \(D_j=z_j\), contradicting (14), (17), and (20).

This does not preserve the complete terminal-first schedule or the complete
factorizations of \(Q_j,\beta_j,E_j\). It also does not make the lifted
charts actual persistent states. It only rules out the weaker inference that
canonical \(D\), its consequences, and the root-bottom terminal check must
eventually break the root-lift periodicity.

## 4. Why the low k=1 Vieta descent does not transfer

The high \(k=1\) parameter surface has

\[
y^2+xy-x^2=c(dxy-1),\qquad d\equiv2\pmod3,
\quad c\equiv1\pmod3,\quad 3\mid y,\quad3\nmid x.
\tag{21}
\]

As a quadratic in \(y\), its other root is

\[
y^\sharp=(cd-1)x-y.
\tag{22}
\]

Modulo \(3\), (22) is \(y^\sharp\equiv x\not\equiv0\). It therefore
does not preserve the high parameter domain. As a quadratic in \(x\), the
other root is \(-(cd-1)y-x<0\). This gives a direct structural reason that
the low-height \(k=1\) Vieta descent cannot simply be reused in the high
slice.

## 5. Fixed core control

The high \(k=1\) curve control

\[
(d,x,y)=(11,101,1020)
\tag{23}
\]

has

\[
\begin{aligned}
p&=115815206209,& h&=1169617882071,\\
D&=1207185892628946440,& v&=11467986421,\\
D_K&=30179647315723661,& \omega&=3161408027583.
\end{aligned}
\tag{24}
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
