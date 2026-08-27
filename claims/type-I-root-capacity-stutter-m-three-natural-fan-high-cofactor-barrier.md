---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
title: proper-root m=3 natural-fan fan-miss 的 high-cofactor 与高端差 barrier
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 natural-fan miss core 中，定义
  w=(p-h-1)/3。则 gcd(u,D(p+e))=1，且 exact high-end gates 为
  u divides 3w^2+3w+1、D=6u+9w+4 divides 9w^2+10w+4、
  52 divides 3u+3w+4。它们给 104C<=9w^2+7w+8。既有 primitive
  scale bounds further force C>=1993、w>=152、p-h>=457；在 even-z
  subbranch C>=11824、w>=370、p-h>=1111。结论显著缩小 actual
  Diophantine residual，但不证明 high-C core 为空、fan hit、terminal、E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
  - type-I-root-capacity-stutter-m-three-natural-fan-small-cofactor-clearance
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - natural-fan
  - high-cofactor
  - divisor-gate
  - scale-barrier
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
    role: fixed fiber, second norm, and F/H identities
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-small-cofactor-clearance
    role: initial C>=223 clearance
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: primitive sigma, tau, theta, and z-parity scale bounds
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan fan-miss 的 high-cofactor 与高端差 barrier

## 1. Coprime factor carriers

Use the actual `m=3`, \(d=13\), \(s_d=3\) core. Put

\[
T=26C,
\qquad
N=3p^2+p+1=12T^2-34T+25,
\]

\[
P_0=\Phi_3(p)=p^2+p+1=4T^2-10T+7.
\]

The two exact identities

\[
N-3P_0=4(1-T),
\qquad
P_0-(T-1)(4T-6)=1
\tag{1}
\]

give \(\gcd(N,P_0)\mid4\). Both integers are odd, hence

\[
\boxed{\gcd(N,P_0)=1.}
\tag{2}
\]

The fixed fiber has \(F H=N\), while \(h=3u\mid P_0\). Therefore

\[
\boxed{\gcd(u,FH)=1.}
\tag{3}
\]

This is an arithmetic support separation: the height carrier cannot share a
prime with either fixed-fiber factor \(F=D\) or \(H=p+e\).

## 2. High-end difference normal form

Define

\[
w=\frac{p-h-1}{3}.
\tag{4}
\]

It is a positive integer. Indeed, \(w=0\) would make \(h=p-1\), but then
\(p-1\mid p^2+p+1\) would force \(p-1\mid3\), impossible for a core prime.
The defining identities become

\[
p=3u+3w+1,
\qquad
C=\frac{3u+3w+4}{52},
\tag{5}
\]

\[
F=D=6u+9w+4.
\tag{6}

\]

The second-norm gate has a high-end identity

\[
3P_0
=(52C-4-3w)(156C+9w-3)
+9(3w^2+3w+1).
\tag{7}
\]

Since \(52C-4-3w=3u\) and \((u,3)=1\), the fixed-fiber second norm is
equivalent to

\[
\boxed{u\mid R_w:=3w^2+3w+1.}
\tag{8}

\]

The first-norm identity \(AF=3u^2-u+1\) likewise gives

\[
12(3u^2-u+1)
=9(9w^2+10w+4)+F(104C-15w-14).
\tag{9}
\]

Here \(F\) is odd and \(F\equiv1\pmod3\), hence it is coprime to \(12\).
The first norm is therefore equivalently

\[
\boxed{F=6u+9w+4\mid S_w:=9w^2+10w+4.}
\tag{10}

\]

Thus the high-cofactor residual has the fully explicit necessary kernel

\[
u\mid R_w,
\qquad
6u+9w+4\mid S_w,
\qquad
52\mid3u+3w+4,
\tag{11}

\]

together with primality, fan-miss support, and the remaining primitive and
actual-receipt gates. The converse is not claimed.

## 3. A quantitative high-end barrier

From (10),

\[
6u+9w+4\le9w^2+10w+4,
\]

so (5) gives

\[
\boxed{104C\le9w^2+7w+8.}
\tag{12}

\]

Equivalently,

\[
w\ge
\left\lceil\frac{\sqrt{3744C-239}-7}{18}\right\rceil.
\tag{13}

\]

There is an independent stronger cofactor scale bound from the actual
primitive core. Write

\[
A=52t-1,\qquad
\sigma=37+54z,\qquad
\lambda=39\tau+\theta.
\]

The established bounds are

\[
t\ge13,\qquad \tau\ge\sigma+6,
\]

\[
\begin{array}{c|c|c}
z\bmod2&\sigma&\theta\\
\hline
1&\sigma\ge955&\theta\ge30\\
0&\sigma\ge5869&\theta\ge186
\end{array}
\tag{14}
\]

and the exact cofactor identity is

\[
52C=6A+65\sigma+2+\lambda.
\tag{15}
\]

Substitution of the lower bounds in (14)--(15) gives

\[
\boxed{z\text{ odd}\Longrightarrow C\ge1993,}
\tag{16}

\]

\[
\boxed{z\text{ even}\Longrightarrow C\ge11824.}
\tag{17}

\]

In particular every actual fan-miss core has \(C\ge1993\). Combining
(13) with (16)--(17) gives

\[
\boxed{
\begin{array}{c|c|c}
\text{branch}&w&p-h=3w+1\\
\hline
\text{all}&w\ge152&p-h\ge457\\
z\text{ even}&w\ge370&p-h\ge1111
\end{array}}
\tag{18}
\]

Thus the apparent short-distance high-end fan-miss region is family-empty.

## 4. Boundary

This is a necessary-core high-cofactor barrier. It does not prove that a
packet satisfying (11) exists, that all high fibers are empty, or that the
natural fan hits. It supplies no terminal, source path, E1--E5 bundle,
admission, re-entry, or global T6 conclusion.
