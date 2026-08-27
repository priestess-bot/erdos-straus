---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-cofactor-lambda-adic-gates
title: proper-root m=3 natural-fan cofactor 的 -11 quotient r-adic gates
statement: >-
  在 actual proper-root m=3, d=13, s_d=3 double-norm core 内，令
  A=52t-1、lambda=(9rho^2+5rho+1)/A、p+3=52C。则
  X=18rho+15A+5 与 Delta_A=9A^2-102A-11 满足
  X^2-Delta_A=1872AC。故任意 r|C 且 r not divide 78 都使
  Delta_A 成为模 r^(v_r(A)+v_r(C)) 的平方。另有
  gcd(C,lambda) divides 108A^2+102A+47；在 fan-miss 子域，任何
  r|gcd(C,lambda) 必位于 1,4,16,25,31 mod 33。该门是 lambda 到 C 的
  具体 Diophantine 接口，但不强制 C 含 2 mod3 素因子、fan hit、terminal 或
  T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - natural-fan
  - lambda
  - p-adic
  - quadratic-residue
  - diophantine-reduction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
    role: actual s_d=3 normal form and fixed-C cofactor bridge
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: -11 norm quotient and fan-miss criterion
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan cofactor 的 -11 quotient r-adic gates

## 1. Scope

Use the actual `m=3`, \(d=13\), \(s_d=3\) necessary core. Keep the
notation

\[
A=52t-1,\qquad
A\lambda=9\rho^2+5\rho+1,
\]

\[
p+3=52C=6A+15\rho+7+\lambda.
\tag{1}
\]

The cofactor \(C\) is the one appearing in the natural fan
\(x=13C\). None of the following congruences supplies a terminal or an
actual transition; they are necessary arithmetic gates on that core.

## 2. The r-adic square gate

Define

\[
X=18\rho+15A+5,
\qquad
\Delta_A=9A^2-102A-11.
\]

Direct completion of the square using (1) gives

\[
\boxed{X^2-\Delta_A=1872AC.}
\tag{2}
\]

Indeed, after substituting \(52C\) from (1), the left side is exactly

\[
-36\bigl(A\lambda-9\rho^2-5\rho-1\bigr).
\]

Writing \(A=52t-1\) makes the discriminant form explicit:

\[
\Delta_A=4D_t,
\qquad
D_t=6084t^2-1560t+25=(78t-10)^2-75.
\tag{3}
\]

Let \(r\mid C\) be prime with \(r\nmid78\). Equation (2) implies the
high-power square condition

\[
\boxed{
\Delta_A\equiv X^2
\pmod {r^{v_r(A)+v_r(C)}}.}
\tag{4}
\]

In particular, if \(r\nmid\Delta_A\), then

\[
\left(\frac{D_t}{r}\right)=1.
\tag{5}
\]

The ramified alternative is explicit rather than ignorable: if
\(r\mid\Delta_A\), then \(r\mid X\). The identity

\[
5X=312C+(39A-6\lambda-17)
\tag{6}
\]

then gives

\[
\boxed{r\mid39A-6\lambda-17.}
\tag{7}
\]

Thus every cofactor prime is either in the r-adic square branch (4) or in
the concrete ramified branch (7); neither branch may be discarded in a
future fan proof.

## 3. Common support with the -11 quotient

Put

\[
H=6A+15\rho+7=52C-\lambda,
\qquad
E_A=108A^2+102A+47.
\]

The \(-11\) norm identity gives the exact relation

\[
E_A=75(A\lambda)+36AH-3H^2+17H.
\tag{8}
\]

If a prime divides both \(C\) and \(\lambda\), then \(H\equiv0\) in
(8), hence

\[
\boxed{\gcd(C,\lambda)\mid E_A.}
\tag{9}
\]

On the natural-fan miss subdomain, every prime \(r\mid C\) is
\(1\pmod3\). For a prime \(r\mid\gcd(C,\lambda)\), the identity

\[
36A\lambda=(18\rho+5)^2+11
\tag{10}
\]

shows \(\left(\frac{-11}{r}\right)=1\). (The exceptional prime \(11\) is
not \(1\pmod3\).) Combining the two residue conditions gives

\[
\boxed{
r\mid\gcd(C,\lambda)
\Longrightarrow
r\equiv1,4,16,25,31\pmod{33}.}
\tag{11}
\]

Consequently, common \(C\)--\(\lambda\) support lies in a sharply defined
split subset and must also divide the explicit polynomial \(E_A\). This is
the first direct factor-level bridge from the \(-11\) quotient to \(C\).

## 4. A necessary no-go for the simplest reciprocity argument

It is tempting to combine the fan-miss condition with \(p=52C-3\) using
quadratic reciprocity. That yields no new contradiction. Indeed, for every
prime \(r\mid C\) in the fan-miss subdomain,

\[
\left(\frac pr\right)=\left(\frac{-3}{r}\right)=1.
\]

Thus \(\left(\frac Cp\right)=1\). But this is automatic on the other side:

\[
52C\equiv3\pmod p,
\qquad
\left(\frac Cp\right)
=\left(\frac3p\right)\left(\frac{52}p\right)
=\left(\frac{13}p\right)
=\left(\frac{10}{13}\right)=1.
\tag{12}
\]

Hence a proof must use the stronger r-adic square gate or the common-support
gate, not only the elementary \(-3\) reciprocity calculation.

## 5. Boundary

The gates (4), (7), and (11) do not prove that \(C\) has a
\(2\pmod3\) prime factor. They do not exclude the fan-miss cofactor, build a
Type II certificate, or provide E1--E5, common admission, re-entry, or any
global T6 conclusion. They specify the remaining number-theoretic interface
that a successful proof or countercontrol must address.
