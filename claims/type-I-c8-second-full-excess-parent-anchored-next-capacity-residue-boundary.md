---
kind: claim
claim_id: type-I-c8-second-full-excess-parent-anchored-next-capacity-residue-boundary
title: c8 second-full-excess parent target 的下一容量 residue 公式与 no-stutter 边界
statement: >-
  在 c8 second-full-excess parent target 的既有 arithmetic domain 内，令
  c=c_T、X=(p+1)/2、beta=gcd(K_T,R_T-1)、L=(R_T-1)/beta，
  并写 75c=64+lambda p。则
  beta=2^[2 divides s lambda] gcd(c,X)，并且下一 canonical capacity 为
  c_next=<4096 beta (94544+75lambda)^(-1)>_p。特别地 c_next is never c，
  而 L>c，故全整除的 easy carry gate L divides c 永远不可用。存在同一
  (lambda,beta)=(8,2) 的 arithmetic controls，分别给 c_next>c 与 c_next<c；
  因而 lambda/overlap 数据不能全称决定方向。结果不提供 actual source、terminal、
  E1--E5、admission 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression
  - type-I-c8-second-full-excess-parent-anchored-universal-fallback
  - type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
topics:
  - type-I
  - f2
  - c-eight
  - complete-excess
  - high-support
  - capacity
  - residue
  - no-stutter
  - proof-boundary
sources:
  - claim: type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression
    role: p-free target, overlap bound, and capacity-control setup
  - claim: type-I-c8-second-full-excess-parent-anchored-universal-fallback
    role: parent macro and final target arithmetic
  - claim: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: c8 polynomials and 75c=64 congruence
visibility: public
last_checked: '2026-08-27'
---

# c8 second-full-excess parent target 的下一容量 residue 公式与 no-stutter 边界

## 1. Arithmetic setup

Remain in the arithmetic domain of the parent-anchored c8 fallback. Write

\[
p=48s+1\ge4129,\qquad X=\frac{p+1}{2},
\]

\[
A_T=MQ_0,\qquad K_T=A_Tc,\qquad pR_T+1=4K_T,
\]

where \(Q_0=(R_0-1)/2\) is the first c8 complete-excess block and
\(c=c_T\) is the canonical final capacity. The established formulas give

\[
75c=64+\lambda p,\qquad
2\le\lambda\le74,\qquad
\lambda\equiv2\pmod3,\qquad5\nmid\lambda,
\tag{1}
\]

and \((A_T,X)=1\). Put

\[
\beta=\gcd(K_T,R_T-1),\qquad
L=\frac{R_T-1}{\beta},\qquad
D_\lambda=94544+75\lambda.
\tag{2}
\]

The previous target-overlap calculation proves \(p\nmid(R_T-1)\) and
\(\beta\le124\). Thus all inverses below are defined modulo \(p\).

## 2. The exact small overlap datum

The chart identity gives

\[
\beta=\gcd(A_Tc,R_T-1)=\gcd(A_Tc,2X).
\tag{3}
\]

The c8 normal form has \(Q_0\) odd and \(M\equiv s\pmod2\), while (1)
gives \(c\equiv\lambda\pmod2\). Since \((A_T,X)=1\) and \(X\) is odd,

\[
\boxed{
\beta=2^\varepsilon\gcd(c,X),
\qquad
\varepsilon=
\begin{cases}
1,&2\mid s\lambda,\\
0,&2\nmid s\lambda.
\end{cases}}
\tag{4}
\]

Moreover \(p=2X-1\) turns (1) into

\[
75c=2\lambda X+(64-\lambda),
\]

so

\[
\boxed{\beta\mid2|\lambda-64|.}
\tag{5}
\]

Thus \(\beta\) is determined by small gcd data; no factorization of the
very large integer \(R_T-1\) is needed to compute it.

## 3. Exact next-capacity formula

The c8 expansion already used in the p-free proof yields

\[
4800(R_T-1)\equiv D_\lambda\pmod p.
\tag{6}
\]

Substituting \(R_T-1=\beta L\) gives

\[
L^{-1}\equiv4800\beta D_\lambda^{-1}\pmod p.
\tag{7}
\]

For a legitimate next complete-excess rechart, its canonical capacity is
\(c_{\rm next}=\langle cL^{-1}\rangle_p\). Since
\(c\equiv64\cdot75^{-1}\pmod p\) and \(4800/75=64\), (7) becomes

\[
\boxed{
c_{\rm next}
=\left\langle4096\,\beta D_\lambda^{-1}\right\rangle_p.}
\tag{8}
\]

This is an exact arithmetic formula in \((p,\lambda,\beta)\). It is not a
source receipt and does not by itself make the rechart admissible.

For comparison with an integer carry, let \(h\) be the unique integer with
\(0\le h<L\) and \(c+ph\equiv0\pmod L\). Then

\[
c_{\rm next}=\frac{c+ph}{L},
\qquad
c_{\rm next}<c
\Longleftrightarrow
ph<c(L-1).
\tag{9}
\]

## 4. There is no full-excess capacity fixed point

Suppose \(c_{\rm next}=c\). Since \(c\) is a unit modulo \(p\), (8) gives
\(L\equiv1\pmod p\). By (6),

\[
p\mid N:=D_\lambda-4800\beta.
\tag{10}
\]

Write \(N=kp\). The bounds \(p\ge4129\), (1), and (5) give

\[
-121\le k\le23.
\tag{11}
\]

Modulo \(75\), (1) and (10) give \(k\equiv4\lambda\pmod{75}\). Since
\(p\equiv1\pmod{16}\), reducing (10) modulo \(16\) also gives
\(k\equiv11\lambda\pmod{16}\). Hence

\[
k\equiv379\lambda\pmod{1200}.
\tag{12}
\]

For the twenty allowed \(\lambda\) values in (1), the signed representatives
of \(379\lambda\pmod{1200}\) are

\[
\begin{array}{c|rrrrrrrrrr}
\lambda&2&8&11&14&17&23&26&29&32&38\\
\hline
k&-442&-568&569&506&443&317&254&191&128&2\\[2pt]
\lambda&41&44&47&53&56&59&62&68&71&74\\
\hline
k&-61&-124&-187&-313&-376&-439&-502&572&509&446
\end{array}
\]

Only \((\lambda,k)=(38,2)\) and \((41,-61)\) lie in (11). In the first
case,

\[
p=48697-2400\beta\equiv25\pmod{48},
\]

contrary to \(p\equiv1\pmod{48}\). In the second case,

\[
61p=4800\beta-97619.
\]

Modulo \(61\), this forces \(\beta\equiv60\pmod{61}\), whereas (5) gives
\(\beta\mid2|41-64|=46\). Both cases are impossible, so

\[
\boxed{c_{\rm next}\ne c.}
\tag{13}
\]

This is a finite congruence proof, not a parameter scan.

## 5. A useful easy-gate no-go

The c8 polynomial has

\[
Q_0=1672704s^3+25344s^2-696s-1>124
\]

for \(s\ge86\), while the parent macro gives \(M>B_p=(p-1)^2/4\). Thus
\(A_T=M Q_0>124B_p\). With \(c\ge9\),

\[
p(R_T-1)=4A_Tc-(p+1)>124pc.
\]

Together with \(\beta\le124\), this gives

\[
\boxed{L>c.}
\tag{14}
\]

Consequently the usual sufficient integer-carry gate \(L\mid c\), which
would make (9) strict with \(h=0\), is impossible on this deterministic
block. This does not rule out the general modular inequality in (9).

## 6. Why overlap data cannot decide the sign

The following two arithmetic controls both satisfy the c8 polynomial, the
\(q_\star=103\) roughness residual, and the necessary terminal-first
congruence residual \(s=86+103u\) with \(u\equiv1,6\pmod7\):

\[
\begin{array}{c|c|c|c|c|c|c}
u&s&p&\lambda&\beta&L\bmod p&c_{\rm next}\\
\hline
202&20892&1002817&8&2&811456&483069>106968\\
6077&626017&30048817&8&2&24314511&2683246<3205208
\end{array}
\]

Both displayed \(p\) are prime; their residual cofactors are respectively
\((6s-1)/103=1217\) and \(36467\), both prime and larger than \(103\).
They are formula controls only, not terminal-first surviving or admitted
states. They prove that even the exact pair \((\lambda,\beta)=(8,2)\) does
not determine the sign in (9): the remaining essential datum is the residue
in (8).

Thus a future actual replay landing in the strict half of (9) would have the
arithmetic part of a CHARGED E5 decrease, but still needs actual source/path,
target terminal/classifier, E2--E4, common E3 admission, and re-entry.
