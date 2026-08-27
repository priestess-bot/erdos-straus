---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
title: proper-root m=3 natural-fan cofactor 的 double-norm support 分离
statement: >-
  在 actual proper-root m=3, d>1, natural gap s_d=3 的 double-norm core 中，
  d=13、p+3=52C、h=3u、C=1 mod 6。若 A=52t-1、
  u=2A+3rho+1 且 A lambda=9rho^2+5rho+1，则有 exact bridge
  156AC-8A-1=u(3A+3u-1)。此外 gcd(C,u) divides 7，
  gcd(C,Phi_6(p))=gcd(C,13)，且 u 的每个素因子均为 1 mod 3。
  因而 natural fan 所需的 C 中 2 mod 3 素因子不能从现有 height carrier u、
  whole-d Phi_6 carrier 或已知 primitive quotient carrier 传递得到；
  剩余耦合变量是 -11 gate quotient lambda。本结论只给 Diophantine support
  boundary，不证明 fan hit、terminal、actual successor 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
  - type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - natural-fan
  - eisenstein-norm
  - support-separation
  - diophantine-reduction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: actual s_d=3 double-norm core and primitive quotient facts
  - claim: type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
    role: exact natural Type-II fan criterion
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan cofactor 的 double-norm support 分离

## 1. Exact scope

Work only in the actual `m=3`, \(d>1\), natural-gap \(s_d=3\) core of
`type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction`. Its
established normal form has

\[
d=13,\qquad h=3u,\qquad p+3=52C,\qquad C\equiv1\pmod6,
\tag{1}
\]

and, with \(A=52t-1\),

\[
u=2A+3\rho+1,
\qquad
A\lambda=9\rho^2+5\rho+1,
\tag{2}
\]

\[
52C=6A+15\rho+7+\lambda
=3u+6\rho+4+\lambda.
\tag{3}
\]

This is a necessary arithmetic core of an actual receipt. It does not assert
that every integer solution of (1)--(3) reconstructs a maximal receipt.

## 2. An exact cofactor bridge

The equations in (2)--(3) give a direct relation between the natural-fan
cofactor and the two norm coordinates:

\[
\boxed{
156AC-8A-1=u(3A+3u-1).}
\tag{4}
\]

Indeed, multiplying (3) by \(3A\), substituting \(3A\lambda\) from
(2), and collecting terms gives

\[
156AC-8A-1
=18A^2+45A\rho+13A+27\rho^2+15\rho+2.
\]

On the other hand, substituting \(u=2A+3\rho+1\) gives exactly the same
right-hand side for \(u(3A+3u-1)\). Thus (4) is an identity, rather than a
congruence derived from a selected factor.

It follows that the previously separate natural-fan cofactor is genuinely
coupled to the double-norm coordinates. The identity alone does not, however,
transfer a prime factor from \(u\) to \(C\).

## 3. Two cyclotomic support barriers

The first support barrier follows directly from \(p=52C-3\):

\[
\Phi_3(p)=p^2+p+1
=2704C^2-260C+7\equiv7\pmod C.
\tag{5}
\]

Since \(3u=h\mid\Phi_3(p)\) and \((C,3)=1\),

\[
\boxed{\gcd(C,u)\mid7.}
\tag{6}
\]

The independent \(\Phi_6\) calculation is equally sharp:

\[
\Phi_6(p)=p^2-p+1
=2704C^2-364C+13\equiv13\pmod C,
\]

so

\[
\boxed{\gcd(C,\Phi_6(p))=\gcd(C,13).}
\tag{7}
\]

Thus every prime factor of \(C\) outside \(\{7,13\}\) is disjoint from
both the root-height carrier and the whole-\(d\) \(\Phi_6\) carrier.

There is a compatible internal proof of (6). The second norm gate gives

\[
u\mid g(\rho):=7\rho^2+4\rho+1,
\]

while direct substitution of (2)--(3) gives the second exact linear identity

\[
52AC+4\rho+1=(3A+3\rho+2)u.
\]

Thus a common divisor of \(C\) and \(u\) divides \(4\rho+1\). The identity

\[
16g(\rho)=7(4\rho+1)^2+2(4\rho+1)+7
\]

again forces that common divisor to divide \(7\). This second derivation is
useful because it exposes the precise point at which the two norm gates fail
to transfer general support to \(C\).

## 4. Residue direction and the remaining variable

Every prime \(r\mid u\) is \(1\pmod3\). To see this, \(p\equiv1\pmod3\)
gives

\[
v_3\bigl(\Phi_3(p)\bigr)=1,
\]

so \(3\nmid u\). Since \(r\le u<h<p\), \(p\) is a unit modulo \(r\).
If \(r\mid u\) and \(p\equiv1\pmod r\), then
\(r\mid\Phi_3(p)\) would force \(r=3\), impossible. Hence the order of
\(p\) modulo \(r\) is exactly three, and

\[
\boxed{r\mid u\Longrightarrow r\equiv1\pmod3.}
\tag{8}
\]

The established primitive quotient calculation in the same core gives the
same \(1\pmod3\) direction for every prime factor of its quotient \(q\), and
\(d=13\equiv1\pmod3\). Meanwhile the natural fan has

\[
x=dC=13C,
\]

and it hits exactly when some divisor of \(x\) is \(-1\pmod3\). Therefore

\[
\operatorname{Fan}(3,13C)\text{ misses}
\Longleftrightarrow
\text{every prime factor of }C\text{ is }1\pmod3.
\tag{9}
\]

Equations (6)--(9) show that neither the height carrier \(u\), the
whole-\(d\) carrier, nor the known primitive quotient can supply the required
\(2\pmod3\) factor of \(C\) by support transfer. The exceptional overlap
primes \(7\) and \(13\) are themselves \(1\pmod3\).

Thus the only displayed direct connection to the fan cofactor that remains is
the \(-11\) quotient \(\lambda\) in (3), or equivalently the exact bridge
(4). A proof that the fan always hits must add a genuinely new constraint
linking that quotient or the full receipt to the factorization of \(C\).

## 5. Fixed-C finite fiber

The bridge also turns every fixed cofactor \(C\) into a finite divisor
problem before the remaining \(K,\tau,q\) gates are imposed. Put

\[
Y=6u+3A-1.
\]

Using (4) to eliminate the quadratic terms in \(u\) gives

\[
Y^2=9A^2+(1872C-102)A-11.
\tag{10}
\]

Completing the square in (10), equivalently expanding and then using (4),
gives the exact factorization

\[
\boxed{
(156C-8-3u)(3A+156C-9+3u)
=3(8112C^2-884C+25).}
\tag{11}
\]

Both factors on the left are positive. For the first, \(3u=h<p=52C-3\)
gives \(156C-8-3u>104C-5>0\); the second is manifestly positive. Thus, for
each fixed \(C\), every integer core packet gives a positive divisor pair of
the fixed integer on the right. Conversely, such a pair fixes

\[
3u=156C-8-F,
\qquad
3A=G-156C+9-3u,
\]

before the residual integrality, primitive-kernel, and actual-receipt gates
are checked. This is a genuine finite Diophantine reduction for fixed \(C\),
not a scan over primes.

Under the fan-miss-compatible congruence \(C\equiv1\pmod3\), the first
factor in (11) is \(1\pmod3\), while

\[
8112C^2-884C+25\equiv2\pmod3.
\]

Hence the second factor has exactly one factor of \(3\). This direction is
consistent with the support separation above; it does not force a
\(2\pmod3\) prime in \(C\).

## 6. Boundary

This is a support-separation and Diophantine-reduction theorem. It does not
prove that (9) is impossible, does not build a Type II certificate, and does
not provide source provenance, E1--E5, common admission, re-entry, or any
global T6 conclusion.
