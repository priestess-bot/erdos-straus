---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-d-one-xside-reentry-source-d-gate-closure
title: H4 q0=1 d=1 x-side 第二 re-entry 的 source D-gate 全称排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter 中，设 d4=gcd((p+1)/2,M4)=1、a2=1、
  rho||q、qhat=q/rho>1，并定义 D=gcd(M4,Q_x2) beta_x2，其中
  x2=Q_x2 beta_x2 是 maximal complete-excess 分解。则 actual double-q raw
  identity、R4=1 (mod p) 和 D|K4 强制
  D=20 (mod p) 且 D divides q^2-4q+1。不存在满足这两个条件的核心素数
  p=1 (mod24)：写 D=20+pv，先由 q^2-4q+1=2 (mod4) 排除 v=0；令
  q^2-4q+1=D ell，则 1<=ell<p、80ell+3=kp、kv<20，并由 p=1 (mod24)
  得 v(k-3)=4(k-1) (mod24)。有限有界菜单唯一留下 (k,v)=(1,12)，但随后强制
  p=13。故 actual d4=1 second-stutter 不可能有 qhat>1 的 x-side raw re-entry；
  a2=1 时只剩 qhat=1 的第三 q-carrier 几何。该结论在 terminal/typed/payload
  guards 之前关闭 raw branch；它不处理 third carrier 或一般 G/Type I selector。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
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
  - source-provenance
  - divisor-gate
  - unitary-divisor
  - carrier-d
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: unitary-carrier-split-and-x-side-raw-reentry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: double-q-raw-endpoint-and-q-squared-identity
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: actual-H4-top-capacity-and-R4-mod-p-contract
  - concept: denominator-escape-state-contract
    role: raw-path-versus-admitted-edge-boundary
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_d_one_xside_d_gate.py
    role: finite-source-D-gate-elimination-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) \(d_4=1\) x-side second re-entry 的 source \(D\)-gate

## 1. 范围与归一化小除子

保留 actual H4 \(q_0=1\) double-\(q\) bridge 的 second-stutter \(a_2=1\)
分派。令

\[
w=\frac{p+1}{2},\qquad
d_4=(w,M_4)=1,\qquad
q=w,\qquad
p=2q-1,\qquad
h=2.
\tag{1}
\]

如已有 unitary-carrier transduction，若

\[
\rho\parallel q,\qquad
\widehat q=\frac q\rho>1,\qquad
E_{x,2}=\widehat qF,\qquad F=q\rho+pt,
\tag{2}
\]

则同一 actual H4 prefix 有 x-side raw re-entry

\[
\xi=\frac{x_2}{\widehat q}=FD,\qquad
\zeta=R_4-\xi.
\tag{3}
\]

这里把 selected complete-excess block 写为

\[
x_2=Q_{x,2}\beta_{x,2},\qquad
g=(M_4,Q_{x,2}),\qquad
D=g\beta_{x,2}.
\tag{4}
\]

因为 \(g\mid M_4\mid K_4\)、\(\beta_{x,2}\mid K_4\) 且
\((g,\beta_{x,2})=1\)，有

\[
\boxed{D\mid K_4.}
\tag{5}
\]

本卡只排除 (3) 的 actual raw occurrence，不要求它先通过 terminal、typed、single-side
或 atomic payload guards。

## 2. 两个无条件 source \(D\)-gate

double-\(q\) endpoint 满足

\[
q^2y_2=R_4-h,\qquad
x_2+y_2=R_4,\qquad
x_2=\widehat q\xi.
\tag{6}
\]

消去 \(x_2,y_2\) 得 exact raw identity

\[
\boxed{
(q^2-1)R_4=q^2\widehat q\,\xi-h
=q^2\widehat q FD-2.
}
\tag{7}
\]

actual H4 receipt 还给 \(R_4\equiv1\pmod p\)。又由 (2) 有

\[
\widehat qF\equiv q^2\pmod p,
\qquad
q^2\equiv\frac14\pmod p.
\tag{8}
\]

将 (7) 模 \(p\) 约化，得到

\[
q^4D\equiv q^2+1\pmod p,
\]

从而

\[
\boxed{D\equiv20\pmod p.}
\tag{9}
\]

这不是 p-primary endpoint 的条件，而是 every actual x-side re-entry 的 source
congruence。

另一方面，将 \(pR_4+1=4K_4\) 代入 (7)，并使用 (5)，得到

\[
\begin{aligned}
4(q^2-1)K_4-pq^2\widehat q FD
&=q^2-1-2p,\\
\boxed{D\mid q^2-1-2p}
&=\boxed{q^2-4q+1}.
\end{aligned}
\tag{10}
\]

记

\[
A=q^2-4q+1.
\tag{11}
\]

式 (9)--(10) 是本卡的完整 source \(D\)-gate。

## 3. 核心域中的有限整数矛盾

核心条件给 \(p\ge73\)、\(q\equiv1\pmod4\)，所以

\[
A>0,\qquad A\equiv2\pmod4,
\qquad 4A=p^2-6p-3.
\tag{12}
\]

由 (9) 写

\[
D=20+pv.
\tag{13}
\]

正性给 \(v\ge0\)。若 \(v=0\)，则 \(20\mid A\)，这与 (12) 的
\(v_2(A)=1\) 矛盾。因此

\[
v\ge1,\qquad D\ge p+20.
\tag{14}
\]

由 (10) 置 \(A=D\ell\)。又

\[
p(p+20)-A=\frac{3p^2+86p+3}{4}>0,
\tag{15}
\]

故

\[
1\le\ell<p.
\tag{16}
\]

将 \(4A=p^2-6p-3\) 模 \(p\) 约化，并使用 (13)，得到正整数 \(k\)：

\[
80\ell+3=kp,\qquad 1\le k\le80.
\tag{17}
\]

把 (13)、(17) 代回 \(4A=4D\ell\)，消去 \(\ell\)，得到

\[
\boxed{
v(kp-3)=20(p-k-6).
}
\tag{18}
\]

右端为正，且

\[
kv=\frac{20k(p-k-6)}{kp-3}<20.
\tag{19}
\]

于是 \(1\le k\le19\)。把 (18) 改写为

\[
p(20-kv)=20k+120-3v.
\tag{20}
\]

利用 \(p\equiv1\pmod{24}\)，有必要同余

\[
\boxed{
v(k-3)\equiv4(k-1)\pmod{24}.
}
\tag{21}
\]

在 \(1\le k\le19\)、\(1\le v\le\lfloor19/k\rfloor\) 的严格有限范围中，先用
\((k-3,24)\mid4(k-1)\) 删除不可能的 \(k\)，再解 (21)，得到：

\[
\begin{array}{c|ccccccccccccc}
k&1&2&4&5&7&8&10&11&13&14&16&17&19\\ \hline
v\text{ satisfying (19),(21)}
&12&\varnothing&\varnothing&\varnothing&\varnothing&\varnothing&
\varnothing&\varnothing&\varnothing&\varnothing&\varnothing&
\varnothing&\varnothing
\end{array}
\tag{22}
\]

所有未列 \(k\) 已被前述 gcd 整除条件排除。唯一余下的
\((k,v)=(1,12)\) 代入 (20) 给

\[
8p=104,\qquad p=13,
\tag{23}
\]

与核心域矛盾。因此 (9)--(10) 没有解。

\[
\boxed{
d_4=1,\ \widehat q>1
\quad\Longrightarrow\quad
\text{不存在 actual H4 }q_0=1\text{ x-side second re-entry}.
}
\tag{24}
\]

结合 unitary transduction，在 \(d_4=1\) 的 actual \(a_2=1\) second-stutter 中，
唯一仍可能的 raw carrier 几何是

\[
\boxed{\widehat q=1,\qquad\rho=q,}
\tag{25}
\]

即既有的第三 y-side \(q\)-carrier。该分支的 p-primary 已被独立排除，但其 p-free
payload/capacity 仍须单独处理。

## 4. 定向回执

    python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_d_one_xside_d_gate.py --verify

回执只枚举 (19)、(21) 强制的有限 \((k,v)\) 菜单，并在 \(p=73\) 控制上重算
\(A\) 的所有除子均不属于 \(20\pmod{73}\)。它不扫描素数、分母、H4 predecessor
或 Reach history。
