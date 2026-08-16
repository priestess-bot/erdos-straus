---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-proper-unitary-reentry-p-primary-d-gate
title: H4 q0=1 proper-unitary 第二 re-entry 的 p-primary D-gate
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter 中，设 a2=1、rho||q 为 proper unitary divisor、
  qhat=q/rho>1，写 E_x2=qhat(q*rho+p*t)。令 x2=Q_x2 beta_x2、
  D=gcd(M4,Q_x2) beta_x2，则 D divides K4、gcd(D,qhat)=1，且 actual raw re-entry
  (xi,zeta)=(x2/qhat,R4-xi) 有 xi=(q*rho+p*t)D。其新的 p-primary gate 精确为
  p divides zeta iff q*rho*D=1 (mod p)，并且 D divides ph-q^2+1；因此也必有
  p divides q^2(qhat-1)-h+1。特别地，若 d=gcd((p+1)/2,M4)=1，则 h=2、
  p=2q-1 强制 qhat=5。此时 q=5rho、p=10rho-1，且所有 p-primary candidate 必满足
  D=20+p*v divides 25rho^2-20rho+1，其中 v>=1 为奇数且 5 does not divide v。
  静态 core row (p,q,rho,qhat)=(409,205,41,5) 满足 endpoint 必要同余，
  但没有 divisor D 通过此 D-gate，严格说明 endpoint congruence 本身不足以建立或
  排除 actual p-primary 分支。该结论不关闭 d>1 或 d=1 的全部 D-divisor menu，
  也不自动支付 terminal/typed/payload guards。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - q0-one
  - double-q-carrier
  - raw-path
  - p-primary
  - complete-excess-bundle
  - unitary-divisor
  - divisor-gate
  - capacity-map
  - strict-counterexample
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: proper-unitary-raw-reentry-and-signed-stutter-normal-form
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: actual-second-endpoint-p-free-and-q-squared-geometry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
    role: actual-H4-carry-h-equals-two-d-and-normalized-divisor-pattern
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-complete-excess-raw-word-convention
  - concept: denominator-escape-state-contract
    role: guarded-p-free-or-strict-dispatch-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py
    role: proper-unitary-D-gate-and-endpoint-only-boundary-control
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) proper-unitary 第二 re-entry 的 \(p\)-primary \(D\)-gate

## 1. 入口和 support-normalized re-entry

保留 actual H4 \(q_0=1\) second-stutter 的 \(a_2=1\) proper-unitary 分支。令

\[
\rho\parallel q,
\qquad
1<\widehat q=\frac q\rho,
\qquad
s=\widehat q t,
\tag{1}
\]

其中 \(\rho\parallel q\) 表示 \(\rho\mid q\) 且 \((\rho,\widehat q)=1\)。second
stutter 的 exact form 因而是

\[
E_{x,2}=q^2+p\widehat q t
=\widehat q F,
\qquad
F=q\rho+pt.
\tag{2}
\]

将 \(x_2\) 的 maximal complete-excess 分解写为

\[
x_2=Q_{x,2}\beta_{x,2},
\qquad
g=(M_4,Q_{x,2}),
\qquad
D=g\beta_{x,2}.
\tag{3}
\]

因为 \(Q_{x,2}=gE_{x,2}\)、\(\widehat q\) clean，且 \(g\) 与
\(\beta_{x,2}\) 分别是 \(K_4\) 的互素因子，有

\[
\boxed{D\mid K_4,\qquad (D,\widehat q)=1.}
\tag{4}
\]

实际 raw word 的 re-entry endpoint 是

\[
\boxed{
\xi=\frac{x_2}{\widehat q}=FD,
\qquad
\zeta=R_4-\xi.
}
\tag{5}
\]

这一步只规范化 actual complete-excess support，不把 (5) 自动视为已获 payload
admission 的 macro。

## 2. 精确 \(p\)-primary gate

原 double-\(q\) identity 和 (5) 给

\[
\boxed{(q^2-1)R_4=q^2\widehat q\,\xi-h.}
\tag{6}
\]

这里 \(p\nmid\xi\)：\(F\equiv q\rho\not\equiv0\pmod p\)，且
\(p\nmid D\mid K_4\)。所以唯一可能重新出现的 \(p\)-block 在 \(\zeta\) 一侧。
由 \(R_4\equiv1\pmod p\)，有

\[
\begin{aligned}
p\mid\zeta
&\Longleftrightarrow \xi\equiv1\pmod p\\
&\Longleftrightarrow \boxed{q\rho D\equiv1\pmod p}.
\end{aligned}
\tag{7}
\]

另一方面，对 (6) 乘以 \(p\) 并模 \(D\) 约化；使用 \(pR_4+1=4K_4\) 和 (4)，得到

\[
\boxed{D\mid ph-q^2+1.}
\tag{8}
\]

式 (7)--(8) 是 proper-unitary re-entry 的精确 support-normalized \(D\)-gate。它
比仅检查 endpoint 同余严格得多。

作为不含 \(D\) 的必要投影，若 \(p\mid\zeta\)，在 (6) 中令
\(R_4\equiv\xi\equiv1\pmod p\)，得到

\[
\boxed{p\mid q^2(\widehat q-1)-h+1.}
\tag{9}
\]

但 (9) 不能代替 (7)--(8)：它会遗漏 complete-excess overlap 和真实 H4 source
support 的限制。

## 3. \(d=1\) 的五分支正规形

现在额外设

\[
d=\left(\frac{p+1}{2},M_4\right)=1.
\tag{10}
\]

actual H4 carry 给 \(h=2\)，且 \(p=2q-1\)。把 (9) 乘以 \(4\)，利用
\(4q^2\equiv1\pmod p\)，有

\[
0\equiv4\bigl(q^2(\widehat q-1)-1\bigr)
\equiv\widehat q-5\pmod p.
\tag{11}
\]

由于 \(1<\widehat q\le q<p\)，唯一可能是

\[
\boxed{\widehat q=5.}
\tag{12}
\]

所以 \(q=5\rho\)、\(p=10\rho-1\)，且 \((5,\rho)=1\)。式 (7) 化成

\[
\rho D\equiv2\pmod p.
\tag{13}
\]

写 \(\rho D=2+pk\)。模 \(\rho\) 使用 \(p\equiv-1\pmod\rho\)，得到
\(k\equiv2\pmod\rho\)。由于 \(\rho>1\)，正性使

\[
k=2+\rho v,
\qquad v\ge0,
\qquad
\boxed{D=20+pv.}
\tag{14}
\]

再将 \(h=2\)、\(q=5\rho\) 代入 (8)，得到有限 divisor menu

\[
\boxed{20+pv\mid 25\rho^2-20\rho+1.}
\tag{15}
\]

右端为奇数且模 \(5\) 同余 \(1\)，故 (15) 进一步强制

\[
\boxed{v\ge1,\qquad v\equiv1\pmod2,\qquad 5\nmid v.}
\tag{16}
\]

式 (12)、(15)--(16) 把 \(d=1\) 的 proper-unitary \(p\)-primary 余项从无界
endpoint event 压成一条 \(\widehat q=5\) 的显式除子门。

## 4. endpoint-only 同余的严格边界

取静态 core arithmetic row

\[
(p,q,d,\rho,\widehat q)=(409,205,1,41,5).
\tag{17}
\]

它满足 \(p\equiv1\pmod{24}\)、\(p=2q-1\) 以及 endpoint-only 条件 (9)：

\[
q^2(\widehat q-1)-1=168099=411p.
\tag{18}
\]

但是 (8) 的右端为

\[
ph-q^2+1=-41206=-2\cdot11\cdot1873,
\tag{19}
\]

而 (13) 要求 \(D\equiv20\pmod{409}\)。(19) 的所有正除子均不在该剩余类，故
不存在 \(D\)。这个 row 不是 actual H4 predecessor，也不声称 actual stutter；它是
一个严格反例，说明 (9) 单独既不能建立 p-primary，也不能用来证明其不可能。

## 5. 边界和定向回执

本卡关闭了 \(\rho=1\) 外的一个常见错误推理，并将 proper-unitary 分支准确压缩为
\(D\)-gate。它尚未排除 (15) 的全部整数菜单，也没有处理 \(d>1\)、\(\widehat q=1\)
第三 carrier，或任何 terminal-first、typed、payload、serializer 和 persistent guards。

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py --verify
```

回执只检查 (11)、(14)--(15) 与 (17)--(19) 的固定整数控制；它不扫描素数范围、
denominator、H4 predecessor 或 Reach history。
