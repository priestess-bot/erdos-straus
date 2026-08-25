---
kind: claim
claim_id: type-I-h4-atomic-capacity-one-source-gate-exclusion
title: H4 clean q 原子目标容量一的负 D 残数全称 source-gate 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a=1 clean-q
  bridge 中，令 w=(p+1)/2=qd、d=gcd(w,M4)、p=2dq-1，且原 q-word 的
  x-side full-excess multiplier 为 E_x。若 atomic target canonical capacity c_q=1，
  则 E_x=-q (mod p)，并强制 D=(M4,Q_x)beta_x 同时满足
  D=-delta_d (mod p)、D|(2d-1)((2d+1)q-1)、0<D<2dp，其中
  delta_d=2d(4d^2-2d+1)。叠加 31 个 actual phase progression 与
  d|abs(1536-a(p)) 后，p<=delta_d 的 2,204 个 q 值、524 个 phase prime 和
  1,054,140 个 D 候选全部不整除；p>delta_d 时，k=1 的固定常数因子参数化无
  phase prime，k>=2 的有限 (d,ell) 参数化只剩唯一算术行
  (u,a,d,q,p,D,ell,k)=(117,2046,85,48842701,8303259169,
  141150521603,10,17)。对该 p 重建 actual H3->H4 maximal carrier 得
  gcd((p+1)/2,M4)=1，而非必要的 85，故最后一行也不在 actual source 域。
  因此 H4 clean-q atomic target 的 C=1 actual family 为空。本结论不单独证明其它
  H4 分支、未来 producer 或全局 high-support C=1 trace 均不可达，F2/T6 仍开放。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-I-high-support-empty-improvement-c1-local-minimum-boundary
topics:
  - type-I
  - type-II
  - H4
  - atomic-split
  - high-support
  - capacity-one
  - source-provenance
  - finite-parameterization
  - family-empty
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual q-word and E_x/D source identity
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: 31-phase selector and exact H3-to-H4 carrier reconstruction
  - reproduction: reproductions/type_i_h4_atomic_capacity_one_source_gate_exclusion.py
    role: exact low/high parameter menus and sole-survivor carrier replay
visibility: public
last_checked: '2026-08-24'
---

# H4 clean-(q) atomic target 的 (C=1) 排除

## 1. Actual source 与负号容量门

保持 actual H4 proper-overlap top-capacity (a_{\mathrm{alt}}=1) clean-(q) bridge 的记号：

\[
w=\frac{p+1}{2}=qd,
\qquad
d=(w,M_4),
\qquad
p=2dq-1,
\tag{1}
\]

\[
x_q=Q_x\beta_x=E_xD,
\qquad
E_x=\frac{Q_x}{(M_4,Q_x)},
\qquad
D=(M_4,Q_x)\beta_x\mid K_4.
\tag{2}
\]

同一 actual raw word 给出

\[
q x_q=(q-1)R_4+2d,
\qquad
R_4\equiv1\pmod p.
\tag{3}
\]

原子 target 的 canonical capacity 满足

\[
c_q\equiv-qE_x^{-1}\pmod p.
\tag{4}
\]

所以本卡研究的唯一假设是

\[
\boxed{c_q=1\iff E_x\equiv-q\pmod p.}
\tag{5}
\]

既有 stutter theorem 排除的是 (E_x\equiv q\pmod p)，不能用于 (5)。我们重新从
source identity 推导负号门。

将 (2)--(3) 模 (p) 约化，并使用 (q^{-1}\equiv2d\pmod p)，得到

\[
q^2D\equiv q+2d-1\pmod p.
\tag{6}
\]

在 (5) 下，等价地

\[
\boxed{
D\equiv-\delta_d\pmod p,
\qquad
\delta_d:=2d(4d^2-2d+1).
}
\tag{7}
\]

而 source divisibility 与正负号无关，仍给出

\[
\boxed{
D\mid A_d:=(2d-1)((2d+1)q-1),
\qquad 0<D<2dp.
}
\tag{8}
\]

actual 19-phase 还要求

\[
p\equiv p_u:=912u+769\pmod {108528},
\qquad
u\in\mathcal U_{31},
\tag{9}
\]

\[
d\mid|1536-a(u)|,
\qquad d\text{ 为奇数}.
\tag{10}
\]

31 个 (u) 类与 (10) 共有 109 个 ((u,a,d)) 对。

## 2. 低区间 (p\le\delta_d) 全空

由 (1)，(p\le\delta_d) 等价于

\[
2\le q\le S_d:=4d^2-2d+1.
\tag{11}
\]

把 (p=2dq-1) 代入 (9)，对每个固定 ((u,d)) 得到一个 (q) 的一次同余类。
在 (11) 内总计只有 2,204 个 (q) 值；其中 524 个产生满足 phase progression 的素数
(p)。对每个这样的 (p)，(7)--(8) 令

\[
D=r^-_{p,d}+jp,
\qquad 0\le j<2d,
\tag{12}
\]

其中 (r^-_{p,d}) 是 (-\delta_d) 的正剩余。精确菜单含 1,054,140 个 (D)；没有
一项整除 (A_d)。所以

\[
\boxed{p\le\delta_d\Longrightarrow\text{无 actual C=1 source}.}
\tag{13}
\]

这里枚举的是由 (7)--(12) 证明完整的有限整数菜单，不是素数区间扫描。

## 3. 高区间的有限参数化

现在设 (p>\delta_d)。由 (7)--(8)，唯一写成

\[
D=kp-\delta_d,
\qquad
A_d=\ell D,
\qquad
k,\ell\ge1.
\tag{14}
\]

把 (q=(p+1)/(2d)) 代入，得到

\[
\boxed{
p\bigl(2dk\ell-(4d^2-1)\bigr)
=2d\ell\delta_d+(2d-1).
}
\tag{15}
\]

正性与 (D<2dp) 给出

\[
k\ell\ge2d,
\qquad
\ell(k-1)\le2d-1.
\tag{16}
\]

### 3.1 (k=1)

令

\[
C_d:=\delta_d(4d^2-1)+(2d-1).
\tag{17}
\]

从 (15) 可改写为

\[
p=\delta_d+\frac{C_d}{m},
\qquad
m=2d\ell-(4d^2-1),
\qquad
m\mid C_d,\qquad m\equiv1\pmod {2d}.
\tag{18}
\]

所以每个候选由固定常数 (C_d) 的一个因子唯一决定。109 个 phase-carrier pair 共产生
255 个因子参数、98 个素数值，但没有一个位于相应 actual phase progression。

### 3.2 (k\ge2)

由 (16)，对每个 (1\le\ell<2d)，若存在 (k)，则最小且唯一可能值为

\[
k=\left\lceil\frac{2d}{\ell}\right\rceil.
\tag{19}
\]

因为再增加一会使 (ell(k-1)>2d-1)。故 (15) 在 32,853 个 ((d,\ell)) 参数上
直接给定 (p)。其中 422 个为整数、108 个为素数，只有一行位于 actual phase progression：

\[
\boxed{
(u,a,d,q,p,D,\ell,k)
=(117,2046,85,48842701,8303259169,141150521603,10,17).
}
\tag{20}
\]

## 4. 唯一行违反 actual carrier equality

式 (20) 到目前为止只使用 phase progression、selector (a)、source 的负 (D)-gate 与
整除式。Actual H3→H4 receipt 还要求

\[
\boxed{d=\gcd\left(\frac{p+1}{2},M_4\right),}
\tag{21}
\]

其中 (M_4) 必须从 H3 的真正 maximal complete-excess block 重建，而不是由 (20)
反向指定。

对 (p=8303259169)，exact H3 reconstruction 给

\[
u=117,\qquad a=2046,\qquad
\beta_4=10,\quad(M_3,Q_4^*)=1,\quad\lambda=5,
\tag{22}
\]

并且

\[
\boxed{
\gcd\left(\frac{p+1}{2},M_4\right)=1\ne85.
}
\tag{23}
\]

所以 (20) 不是 actual H4 source。结合 (13)、(18)--(23)，负号 source menu 全空：

\[
\boxed{
\text{actual H4 clean-}q\text{ atomic target cannot have }c_q=1.
}
\tag{24}
\]

## 5. 边界与跨 track 后果

本定理只排除 actual `H4_A1` clean-(q) atomic producer 的 capacity-one target。
已有 c8 second-full-excess fallback 由 (75c\equiv64\pmod p) 排除 (c=1)。两者结合
显著减少 high-support C=1 的可能 producer，但还不能在 coordinator 完成全部 producer
target-set freeze 以前宣称全局 trace-unreachable。

尤其，本卡不证明：

- H4 非 atomic 分支全部关闭；
- 未来新 producer 不能产生 C=1；
- 当前抽象 high-support C=1 family 已 EMPTY；
- F2 或 T6 已闭合。

聚焦复现：

```bash
python3 reproductions/type_i_h4_atomic_capacity_one_source_gate_exclusion.py --verify
python3 -m unittest tests.test_type_i_h4_atomic_capacity_one_source_gate_exclusion -v
```
