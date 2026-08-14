---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-refined-affine-terminal-boundary
title: q=1 高 C=2 的 19 相位细分仿射终端边界
statement: >-
  在 q=1 high C=2 19 相位 63 类终端菜单留下的 33 个 u (mod 119) residue progression
  上，若固定 gap 且 Type I/II 的 square divisor 对整个整数参数 progression 是常数或
  非常数仿射函数，则完整有限枚举恰给出两条 Type II 终端：u=13 的
  (m,A,B,C(t))=(23,6,17,31+266t)，以及 u=20 的
  (31,14,17,20+114t)。所有 33 条 progression 的常数 Type II、常数 Type I 与
  非常数仿射 Type I 候选均为空。因此 direct terminal-first 菜单精确增加两类至 65 类，
  剩余 31 类；该边界仅限于对完整整数 progression 成立的仿射 square-divisor identity，
  不排除非线性或按单个素数选择的证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-affine-uniform-divisor-rigidity
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - affine-divisor
  - terminal-first
  - short-certificate
  - residue-dispatch
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-residue-terminal-dispatch
    role: 63-class-input-menu-and-33-class-domain
  - claim: type-II-affine-uniform-divisor-rigidity
    role: complete-nonconstant-affine-divisor-normal-form
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_refined_affine_terminal_boundary.py
    role: finite-residue-and-divisor-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的细分仿射终端边界

## 1. Refined input domain

The preceding affine terminal dispatch writes every residual progression as

\[
p(t)=P_u+Lt,
\qquad
P_u=912u+769,
\qquad
L=108528,
\qquad
t\ge0,
\tag{1}
\]

with

\[
u\in\mathcal U_{33}=
\{1,5,6,8,13,15,19,20,22,26,27,34,36,40,41,43,54,57,
62,68,69,75,78,83,85,90,92,96,99,103,104,111,117\}.
\tag{2}
\]

For a fixed legal gap \(m\), put

\[
x(t)=\frac{p(t)+m}{4}=St+T,
\qquad
S=27132,
\qquad
T=\frac{P_u+m}{4}.
\tag{3}
\]

This card examines only a certificate formula valid for every integer
\(t\ge0\) in (1). It is stronger than checking selected primes, but narrower
than a selector allowed to choose unrelated data at each prime.

## 2. Complete affine candidate normal forms

Let \(E=(S,T)\), \(N(t)=x(t)/E\), and suppose first that the square divisor
\(d(t)\) is nonconstant affine. The uniform affine-divisor rigidity lemma
gives

\[
d(t)=aN(t),
\qquad a\mid E^2.
\tag{4}
\]

For Type II, \(d(t)\le x(t)\) also gives \(a\le E\), while its congruence
is exactly

\[
m\mid x(t)+d(t)
\quad\Longleftrightarrow\quad
m\mid E+a.
\tag{5}
\]

Hence \(m\le2E\le2S\). The finite loop

\[
3\le m\le\min(P_u-2,2S),\quad m\equiv3\pmod4,
\quad E=(S,T),\quad a\mid E^2,\quad a\le E,\quad m\mid E+a
\tag{6}
\]

is exhaustive for all nonconstant uniform affine Type II divisors.

For Type I, write \(N(t)=qt+n\). Its congruence is equivalent to

\[
m\mid F(t):=p(t)x(t)+d(t)=N(t)\bigl(4E^2N(t)+a\bigr).
\tag{7}
\]

This is an integer quadratic. It holds for all \(t\ge0\) if and only if
\(m\) divides its three binomial coefficients

\[
\begin{aligned}
F(0)&=n(4E^2n+a),\\
\Delta F(0)&=q\bigl(4E^2(2n+q)+a\bigr),\\
\Delta^2F(0)&=8E^2q^2.
\end{aligned}
\tag{8}
\]

Together with \(3\le m\le P_u-2\) and \(a\mid E^2\), this is again a
complete finite enumeration, with no prime-range scan.

If \(d\) is constant, then \(d\mid E^2\). Type II additionally requires
\(m\mid S\) and \(m\mid T+d\). Type I instead uses the three differences
of \(4(St+T)^2+d\):

\[
4T^2+d,
\qquad 4S(2T+S),
\qquad 8S^2.
\tag{9}
\]

Thus constant affine divisors are included, rather than silently omitted.

## 3. Exact result on the 33 former residual classes

Applying (6)--(9) produces exactly two nonconstant Type II rows and no rows
in the other three families.

| \(u\) | \(P_u\) | \(m\) | \(E\) | \(a\) in (4) | \((A,B)\) | \(C(t)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 12625 | 23 | 102 | 36 | \((6,17)\) | \(31+266t\) |
| 20 | 19009 | 31 | 476 | 392 | \((14,17)\) | \(20+114t\) |

The first row has

\[
\frac{p(t)+23}{4}=6\cdot17(31+266t),
\qquad
d(t)=36(31+266t),
\tag{10}
\]

and \(23=6+17\). The second has

\[
\frac{p(t)+31}{4}=14\cdot17(20+114t),
\qquad
d(t)=392(10+57t),
\tag{11}
\]

and \(31=14+17\). Both are Type II normal forms on every member of their
respective progression.

For concrete phase-prime controls, \(u=13,t=2\) gives \(p=229681\) and

\[
\frac4{229681}
=\frac1{57426}+\frac1{775862418}+\frac1{2198276851},
\tag{12}
\]

while \(u=20,t=0\) gives \(p=19009\) and

\[
\frac4{19009}
=\frac1{4760}+\frac1{5322520}+\frac1{6463060}.
\tag{13}
\]

The finite receipt finds no constant Type II row, no constant Type I row,
and no nonconstant affine Type I row in any of the 33 original classes.

## 4. Updated boundary

The earlier menu had 60 fixed-raw Type II classes and 3 fixed Type I classes.
Equations (10)--(11) add two disjoint direct Type II terminal classes, so

\[
63\longrightarrow65,
\tag{14}
\]

and the exact remaining input for a genuinely non-uniform terminal or a
cross-chart descent is

\[
\mathcal U_{31}=
\{1,5,6,8,15,19,22,26,27,34,36,40,41,43,54,57,62,68,69,75,78,
83,85,90,92,96,99,103,104,111,117\}.
\tag{15}
\]

This is not a no-certificate result for \(\mathcal U_{31}\). It only rules
out the complete integer-progression-uniform constant/affine square-divisor
families described above; nonlinear divisors, per-prime selectors, and the
existing strict H3 relay all remain available.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_refined_affine_terminal_boundary.py --verify
```
