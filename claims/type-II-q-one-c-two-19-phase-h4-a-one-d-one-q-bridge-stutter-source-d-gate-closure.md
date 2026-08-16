---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-d-one-q-bridge-stutter-source-d-gate-closure
title: H4 d4=1 clean q-bridge 容量 stutter 的 source D-gate 全称排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 中，若 d4=gcd((p+1)/2,M4)=1，则 actual H4 carry 强制 h=2、
  q=(p+1)/2、p=2q-1。原 q-word 的唯一 arithmetic capacity stutter 是
  E_x=q (mod p)。令 x_q=Q_x beta_x、E_x=Q_x/gcd(M4,Q_x)、
  D=gcd(M4,Q_x) beta_x，则 raw identity q x_q=(q-1)R4+2、R4=1 (mod p)
  与 D|K4 强制 D=6 (mod p) 且 D divides 3q-1=(3p+1)/2. 因 0<D<2p，
  D 只可能为 6 或 p+6；前者不整除 3q-1，后者严格介于其一半与其本身之间而不能整除。
  故 d4=1 不存在 actual clean q-bridge capacity stutter。特别地，d4=1 的 q0=1
  double-q/third-q carrier 与 q0>1 re-entry 都没有 actual parent；非 stutter 的
  terminal、p-free strict-capacity 或 guarded payload 分派不受此结论替代。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - d-one
  - fresh-carrier
  - raw-path
  - complete-excess-bundle
  - residual-capacity
  - source-provenance
  - divisor-gate
  - q0-one
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: unique-original-q-bridge-stutter-E-x-congruent-q
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-complete-excess-decomposition
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-H4-carry-shape
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-carry-provenance-and-d4-overlap
  - concept: denominator-escape-state-contract
    role: distinction-between-arithmetic-closure-and-admitted-payload
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_d_one_q_bridge_stutter_source_d_gate.py
    role: focused-source-D-gate-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(d_4=1\) clean \(q\)-bridge stutter 的 source \(D\)-gate

## 1. 实际 \(d_4=1\) 的 carry 归一化

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) 的 clean
\(q\)-bridge。写

\[
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad q=\frac w{d_4},
\qquad h=(R_4-1,K_4).
\tag{1}
\]

actual H4 carry 可写 \(h=2e\)，并有 \(M_4=M_3L\)、\((w,M_3)=1\) 和

\[
Lc_4=c_3+ps_4.
\tag{2}
\]

令 \(e=(w,c_3-s_4)\)。因为 \(p\equiv-1\pmod w\)，(2) 给
\(d_4=(w,L)\mid e\)。另一方面 \(h\mid K_4\) 与 clean \(q\) 条件给
\((e,q)=1\)；由 \(w=qd_4\) 得 \(e\mid d_4\)。所以

\[
\boxed{h=2d_4.}
\tag{3}
\]

本卡只取 \(d_4=1\)。于是

\[
\boxed{h=2,\qquad q=w=\frac{p+1}{2},\qquad p=2q-1.}
\tag{4}
\]

## 2. 原始 q-word 的小除子

令 original clean \(q\)-word 的端点为

\[
x_q=R_4-\frac zq,\qquad y_q=\frac zq,
\qquad z=R_4-h.
\tag{5}
\]

把 \(x_q\) 的 maximal complete-excess 分解写成

\[
x_q=Q_x\beta_x,\qquad
g=(M_4,Q_x),\qquad
E_x=\frac{Q_x}{g},\qquad D=g\beta_x.
\tag{6}

\]

其中 \(g\) 与 \(\beta_x\) 是 \(K_4\) 的互素因子，故

\[
\boxed{x_q=E_xD,\qquad D\mid K_4.}
\tag{7}
\]

original q-word identity 是

\[
qx_q=(q-1)R_4+h=(q-1)R_4+2.
\tag{8}
\]

已有 complete-excess stutter reduction 说明，所有 nonterminal p-free endpoint
的唯一非严格 arithmetic capacity 情形是

\[
E_x\equiv q\pmod p.
\tag{9}
\]

在 actual H4 receipt \(R_4\equiv1\pmod p\) 中，将 (7)--(9) 代入 (8)，有

\[
qE_xD\equiv q+1\pmod p,
\qquad
\boxed{D\equiv6\pmod p.}
\tag{10}
\]

再把 \(pR_4+1=4K_4\) 代入 (8)：

\[
4(q-1)K_4-pqE_xD=q-1-2p=1-3q.
\tag{11}
\]

由 (7) 得第二个 source gate

\[
\boxed{D\mid3q-1=\frac{3p+1}{2}.}
\tag{12}
\]

## 3. 两项有限菜单的矛盾

记

\[
A=3q-1=\frac{3p+1}{2}.
\tag{13}
\]

核心域 \(p\ge73\) 给 \(0<A<2p\)。由 (10)、正性与 (12)，\(D\) 只能是

\[
D=6\quad\text{或}\quad D=p+6.
\tag{14}
\]

若 \(D=6\)，写 \(p=24t+1\)，则 \(q=12t+1\)，从而

\[
A=36t+2\not\equiv0\pmod3,
\tag{15}
\]

不可能被 \(6\) 整除。

若 \(D=p+6\)，则

\[
D<A<2D
\tag{16}

\]

（左边由 \(A-D=(p-11)/2>0\)，右边由 \(2D-A=(p+23)/2>0\)）。
故 \(D\mid A\) 将强制 \(D=A\)，即 \(p=11\)，与核心域矛盾。

因此 (9) 不可能：

\[
\boxed{
d_4=1
\quad\Longrightarrow\quad
\text{original clean }q\text{-bridge 没有 actual capacity stutter}.
}
\tag{17}
\]

## 4. 对后继 raw 分支的影响

\(q_0=1\) 的 double-\(q\) bridge、其 second stutter 以及 third \(q\)-carrier，
都以原 q-word 的 (9) 为入口；\(q_0>1\) re-entry 也同样以该 stutter target 为入口。
所以 (17) 给出 source-level 的更早排除：在 actual \(d_4=1\) H4 域内，它们没有
parent raw occurrence。

这不替代原 q-word 的 non-stutter 分派：terminal-first、p-free strict capacity、
single-side 与 atomic payload 仍须分别满足既有 contracts。也不改变 \(d_4>1\) 的
q-bridge 分支。

## 5. 定向回执

    python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_d_one_q_bridge_stutter_source_d_gate.py --verify

回执只核对 (10)--(16) 的两项整数菜单和 \(p=73\) divisor control；它不搜索素数、
分母、H4 predecessor 或 Reach history。
