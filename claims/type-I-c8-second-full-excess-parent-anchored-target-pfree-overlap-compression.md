---
kind: claim
claim_id: type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression
title: c8 second-full-excess parent target 的 p-free 与小 overlap 压缩
statement: >-
  在 c8 second-full-excess parent-anchored macro 的既有算术域
  p=48s+1>=4129 内，令 final chart 为
  A_T=M Q, K_T=A_T c_T, pR_T+1=4K_T，并令 75c_T=64+lambda p。
  则 lambda 属于 [2,74]、lambda=2 mod 3、5 not divide lambda；此外
  p not divide R_T(R_T-1)，且 gcd(K_T,R_T-1)=gcd(K_T,p+1)<=124。
  因而 target 的 canonical p-source 在整数层 primitive，anchor
  R_T-1 的 maximal complete-excess block 非平凡且 p-free。此结论只压缩
  后继 high-support arithmetic；它不证明该 source 已 actual、target 已 admitted，
  也不从小 overlap 推出下一 canonical capacity 严格下降或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-c8-second-full-excess-parent-anchored-universal-fallback
  - type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
topics:
  - type-I
  - f2
  - c-eight
  - complete-excess
  - high-support
  - p-free
  - overlap
  - proof-boundary
sources:
  - claim: type-I-c8-second-full-excess-parent-anchored-universal-fallback
    role: parent-to-final target, 9<=c_T<=p-2, and relative macro scope
  - claim: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: c8 normal form, M/Q identities, and 8Q-75 formula
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: c8 g=1 support separation and primitive-source terminology
visibility: public
last_checked: '2026-08-27'
---

# c8 second-full-excess parent target 的 p-free 与小 overlap 压缩

## 1. Scope and notation

Work only in the arithmetic domain of
`type-I-c8-second-full-excess-parent-anchored-universal-fallback`. Thus

\[
p=48s+1\ge4129,\qquad pR_0+1=32M,\qquad R_0=2Q+1,
\tag{1}
\]

and the parent-anchored final chart is

\[
A_T=MQ,\qquad K_T=A_Tc_T,\qquad pR_T+1=4K_T.
\tag{2}
\]

The established parent macro gives

\[
9\le c_T\le p-2,\qquad 75c_T\equiv64\pmod p,
\tag{3}

\]

while the c8 carry calculation gives

\[
8Q-75=pD,\qquad
D=278784s^2-1584s-83=121p^2-275p+71.
\tag{4}

\]

The words "source" and "complete-excess" below are integer/chart statements.
They do not supply an actual source-path receipt or a selector admission.

## 2. The bounded lambda parameter

Define the integer \(\lambda\) by

\[
75c_T=64+\lambda p.
\tag{5}
\]

The bounds in (3) give \(0<\lambda<75\). Reducing (5) modulo \(3\) and
\(5\), using \(p\equiv1\pmod3\) and \(p\ne5\), gives

\[
\lambda\equiv2\pmod3,\qquad \lambda p\equiv1\pmod5.
\tag{6}
\]

Hence

\[
\boxed{
2\le\lambda\le74,\qquad
\lambda\equiv2\pmod3,\qquad
5\nmid\lambda.}
\tag{7}
\]

These restrictions will make the two apparent p-primary failures finite and
incompatible with the c8 residue class.

## 3. Both p-primary failures are excluded

From (1), (4), and (5),

\[
4800(pR_T+1)
=(pR_0+1)(pD+75)(p\lambda+64).
\tag{8}
\]

Modulo \(p^2\), (4) and \(R_0=(pD+79)/4\) give

\[
4800R_T\equiv99344+75\lambda\pmod p,
\tag{9}
\]

\[
4800(R_T-1)\equiv94544+75\lambda\pmod p.
\tag{10}
\]

Since \(p\nmid4800\), either \(p\mid R_T\) or \(p\mid R_T-1\) would give

\[
p\mid a+75\lambda,\qquad a\in\{99344,94544\}.
\tag{11}
\]

Put \(k=(a+75\lambda)/p\). Its displayed range and \(p\ge4129\) give
\(1\le k\le25\). By (5), \(p\lambda\equiv11\pmod{75}\), while
\(a\equiv44\pmod{75}\). Thus

\[
k\equiv4\lambda\pmod{75}.
\tag{12}
\]

The restrictions (7) leave only the following possibilities:

\[
(\lambda,k)\in
\{(2,8),(23,17),(38,2),(41,14),(59,11),(62,23)\}.
\tag{13}
\]

Direct division in (11) has a zero remainder only in the third row:

\[
\begin{array}{c|c|c|c}
\lambda&k&(99344+75\lambda)\bmod k&(94544+75\lambda)\bmod k\\
\hline
2&8&6&6\\
23&17&4&15\\
38&2&0&0\\
41&14&9&11\\
59&11&6&2\\
62&23&11&18
\end{array}
\]

That row gives \(p=51097\) or \(p=48697\), both \(25\pmod {48}\),
contradicting \(p=48s+1\). Therefore

\[
\boxed{p\nmid R_T(R_T-1).}
\tag{14}
\]

Also \(p\nmid M\) by (1), \(p\nmid Q\) by \(8Q\equiv75\pmod p\), and
\(p\nmid c_T\) by (3). Thus the target support and carrier are p-free.

## 4. Exact overlap identity and uniform bound

For every chart in (2), subtraction of \(p(R_T-1)\) from
\(pR_T+1=4K_T\), and the reverse implication modulo a common divisor, give

\[
\gcd(K_T,R_T-1)=\gcd(K_T,p+1).
\tag{15}
\]

Let \(X=(p+1)/2=24s+1\). The earlier c8 \(g=1\) calculation gives
\((M,X)=1\). Reducing (1) modulo \(X\) gives

\[
Q\equiv-16M\pmod X,
\]

so \((MQ,X)=1\). Consequently,

\[
\gcd(K_T,p+1)\le2\gcd(c_T,X).
\tag{16}
\]

Because \(p\equiv-1\pmod X\), (5) yields

\[
75c_T\equiv64-\lambda\pmod X.
\]

Hence \(\gcd(c_T,X)\mid(\lambda-64)\). The value \(\lambda=64\) is
excluded by (7), and \(|\lambda-64|\le62\), so (15)--(16) give

\[
\boxed{
\gcd(K_T,R_T-1)=\gcd(K_T,p+1)
\le2|\lambda-64|\le124.}
\tag{17}
\]

## 5. The real residual after the compression

Let

\[
Q_T^+=\prod_{v_q(R_T-1)>v_q(K_T)}q^{v_q(R_T-1)}.
\tag{18}
\]

Writing \(\beta=\gcd(K_T,R_T-1)\), this is exactly
\(Q_T^+=(R_T-1)/\beta\). By (14), it is p-free. Also
\(A_T\mid K_T\), so (15) and \((A_T,X)=1\) give
\((A_T,R_T-1)\mid(A_T,2X)\mid2\). The inherited chart parity is
\(R_T\equiv3\pmod4\): if \(A_T\) is even, the sole factor \(2\) is already
in \(\beta\), and if \(A_T\) is odd it is coprime to \(A_T\). Hence

\[
\gcd(A_T,Q_T^+)=1,
\qquad
A_+=\operatorname{lcm}(A_T,Q_T^+)=A_TQ_T^+.
\tag{19}
\]

By (17) and \(R_T>p\ge4129\), this block is nontrivial: otherwise
\(R_T-1\mid K_T\), contrary to \(\gcd(K_T,R_T-1)\le124<R_T-1\). Equation
(14) also makes the canonical integer p-source

\[
\bigl(p,\ R_T(p-1)-p,\ p-1\bigr)
\tag{20}
\]

primitive, since its three pairwise gcds reduce to \((p,R_T)\) or \(1\).

This is not a strict-successor theorem. If a future actual replay reaches
(19), let

\[
L_T=Q_T^+.
\]

The next canonical capacity, when its rechart is otherwise legitimate, is only

\[
c_{\mathrm{next}}=\langle c_TL_T^{-1}\rangle_p.
\tag{21}
\]

The bound (17) does not determine the residue of \(L_T\), and does not imply
\(c_{\mathrm{next}}<c_T\). This is a real arithmetic limitation, not only a
missing interface: at \(s=20892\),

\[
p=1002817\ \text{is prime},\qquad6s-1=103\cdot1217,
\]

so the c8 polynomial and the \(q_\star=103\) roughness formula apply. Direct
integer evaluation gives

\[
c_T=106968,\qquad\lambda=8,\qquad\beta=2,
\]

\[
Q_T^+=3110876803809441894703303491236110076677343,
\]

\[
c_{\mathrm{next}}=483069>c_T.
\]

This is an arithmetic control only: it is not claimed to be terminal-first
surviving, actual, or admitted. It rules out the unsupported inference
"small overlap implies strict capacity drop." Actual source/path,
terminal-first priority, target classification, E3 admission, re-entry, and
a paid strict inequality are all separate obligations.
