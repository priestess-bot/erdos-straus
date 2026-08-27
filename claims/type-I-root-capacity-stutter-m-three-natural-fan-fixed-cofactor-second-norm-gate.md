---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
title: proper-root m=3 natural-fan fixed-cofactor fiber 的 second-norm divisor gate
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 core 中，令 fixed-C fiber 的
  F=156C-8-3u=D、H=p+e、S=A^2+A rho+rho^2。则
  AF=3u^2-u+1，且 13u divides S 当且仅当 u divides
  7rho^2+4rho+1，当且仅当 u divides F^2+F+7。等价地每个 fixed-C
  divisor candidate 必满足 156C-8-F divides 3(F^2+F+7)。所以 second
  norm 在 fiber 上是一条 exact finite sieve；其 13 部分不是独立 residual。
  结论不排空一般 fan-miss C，也不提供 terminal、E1--E5 或 T6 closure。
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
  - fixed-cofactor
  - divisor-gate
  - norm
  - diophantine-reduction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
    role: fixed-C factor fiber and actual core normal form
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: second norm and primitive-kernel definitions
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan fixed-cofactor fiber 的 second-norm divisor gate

## 1. Scope and fixed fiber

Remain in the actual `m=3`, \(d=13\), \(s_d=3\) core. Let

\[
p=52C-3,\qquad h=3u,\qquad
S=A^2+A\rho+\rho^2.
\]

For the fixed-\(C\) factor fiber, write

\[
F=156C-8-3u,\qquad H=A+p+u.
\tag{1}
\]

The earlier bridge identifies these quantities intrinsically:

\[
\boxed{F=3p+1-h=D,\qquad H=p+e,\qquad FH=3p^2+p+1.}
\tag{2}
\]

The same bridge gives

\[
\boxed{AF=3u^2-u+1.}
\tag{3}
\]

In particular \((F,u)=1\), because \(AF\equiv1\pmod u\).

## 2. The second norm becomes an exact divisor gate

The actual double-norm identities include

\[
4S=(2A-\rho-1)u+(7\rho^2+4\rho+1).
\tag{4}
\]

Thus, since \(u\) is odd,

\[
u\mid S
\Longleftrightarrow
u\mid7\rho^2+4\rho+1.
\tag{5}
\]

On the other hand, \(3\rho=u-2A-1\), so direct reduction of \(9S\) modulo
\(u\) gives

\[
9S\equiv7A^2+A+1\pmod u.
\tag{6}
\]

Multiplying by \(F^2\) and using (3) yields

\[
9F^2S\equiv F^2+F+7\pmod u.
\tag{7}
\]

Because \(3F\) is a unit modulo \(u\), (5)--(7) give the exact equivalence

\[
\boxed{
u\mid7\rho^2+4\rho+1
\Longleftrightarrow
u\mid S
\Longleftrightarrow
u\mid F^2+F+7.}
\tag{8}
\]

Since \(3u=156C-8-F\), every fixed-\(C\) divisor candidate must therefore
satisfy the integer filter

\[
\boxed{156C-8-F\mid3(F^2+F+7).}
\tag{9}
\]

This is an exact synchronized sieve on the finite divisor list \(F\mid
3p^2+p+1\); it is not a search over arbitrary raw words.

## 3. The 13-part is automatic in the full core

The `m=3`, \(s_d=3\) parameterization has

\[
A\equiv-1,\qquad \rho\equiv4,\qquad u\equiv11\pmod{13}.
\tag{10}
\]

Hence \(13\mid S\) and \((13,u)=1\). Combining this with (5) gives

\[
\boxed{
13u\mid S
\Longleftrightarrow
u\mid7\rho^2+4\rho+1.}
\tag{11}
\]

Thus the factor \(13\) in the previously displayed second-norm quotient is
not an independent unresolved gate. The only independent second-norm test on
the fixed fiber is (9).

For consistency, reducing the full fiber modulo \(13\) forces

\[
F\equiv11,\qquad H\equiv7,\qquad u\equiv11,\qquad
A\equiv-1,\qquad\rho\equiv4,\qquad\lambda\equiv4\pmod{13}.
\tag{12}
\]

These are necessary congruences, not an existence theorem.

## 4. Boundary

The divisor gate (9) does not prove that every fan-miss cofactor is empty.
It does not reconstruct a maximal receipt, establish a terminal, or supply
source provenance, E1--E5, common admission, re-entry, or a global T6
conclusion. It identifies the remaining independent second-norm obstruction
that must be applied to every fixed-\(C\) fiber.
