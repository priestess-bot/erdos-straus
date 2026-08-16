---
kind: claim
claim_id: type-II-q-one-c3-source-lineage-phase-root-entry
title: q=1 G 到 c=3 source-lineage 根及 R=11 RESET 的单向 phase relay
statement: >-
  对任一核心素数 p=24h+1，若它既是 ordinary q=1 Type II G endpoint，又具有一份从预先声明的
  c=3 universal p-source 到 N_R(p-3) 的有效 source-lineage raw receipt，则可在 terminal-first
  前提下把该 endpoint 以 Sol(p) 恒等映射单向重索引为 fresh_source_tree_only 的 c=3 根，继而以
  d=3 dual RESET 到 R=11、A=3。root receipt 的 E1--E3 由 source、逐边 raw 重放、lineage mark 和
  typed fiber 给出；endpoint-to-root 与 root-to-R=11 两条边各自满足 E1--E5，势按 phase 2 -> 1，
  再按 A:1 -> 3 严格下降。该定理以 raw receipt 的存在为条件，不证明每个 q=1 G endpoint 都有此
  receipt，不给出 R=11 后的全称 selector，也不证明全局 G/Type I exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-g-anchor-c3-root-to-r11-reset-terminal-bridge
  - type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - G-state
  - type-I
  - c3
  - source-lineage
  - root-entry
  - phase-reindexing
  - R11
  - identity-lift
  - well-founded-potential
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: q-one-G-endpoint-and-one-way-phase-policy
  - claim: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
    role: c3-chart-and-root-receipt-boundary
  - claim: type-I-g-anchor-c3-root-to-r11-reset-terminal-bridge
    role: d3-reset-and-terminal-first-contract
  - claim: type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt
    role: non-p-first-source-lineage-control
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: reverse-parent-no-go-for-E1
  - concept: denominator-escape-state-contract
    role: E1-to-E5-and-global-phase-contract
  - reproduction: reproductions/type_ii_q_one_c3_source_lineage_phase_root_entry.py
    role: replayable-controls-and-relay-verifier
visibility: public
last_checked: '2026-08-16'
---

# \(q=1\) G 到 \(c=3\) source-lineage 根的单向 relay

## 1. 精确的条件性输入

固定核心素数

\[
p=24h+1,
\qquad
R=104h-9,
\qquad
M=26h+1,
\qquad
x=p-3,
\qquad
K=Mx.
\tag{1}
\]

本卡只在下列两个彼此独立的输入同时成立时适用。

1. \(p\) 是 ordinary `q=1` Type II G endpoint，且标记解集为
   \(\operatorname{Sol}(p)\)；
2. 有一份 c=3 source-lineage receipt：它从闭式预先声明的 source
   \[
   \mathsf S_p=\bigl(p,R(p-1)-p,p-1\bigr)
   \tag{2}
   \]
   出发，逐边回放到 \(N_R(x)\)。每条 raw 边保存有序 source、所选坐标、标签 \(q_i\)、
   gcd reduction \(g_i\) 和有序 destination。唯一允许的非 raw 操作是 canonical
   \(p\)-edge 后 \((1,R-1,1)\mapsto(R-1,1,1)\) 的一次坐标元数据交换。

第二项不是“存在某个 \(p\)-parent”的改写。其左端恰为 (2)，完全由 \(p\) 的 c=3
闭式图表决定；任何从 seed 反向制造的 predecessor 即使能逐边回放，也不能满足本卡的 E1。

还要求

\[
h\ge3,
\qquad h\not\equiv2\pmod3,
\qquad h\not\equiv12\pmod{13},
\tag{3}
\]

从而 (1) 满足

\[
pR+1=4K,
\qquad R=4M-13,
\qquad 13p=12M+1.
\tag{4}
\]

source chart 和 \(R=11\) chart 的 F/G/hit 分类都必须独立重算；它们不是 Type II G
标签的传播。

## 2. 来源线尾标记引理

令 \(z_i\) 是 (2) 的首坐标在第 \(i\) 条 raw 边后的有序后代，令

\[
E_i=\prod_{j\le i}q_jg_j,
\qquad
\sigma=-p^{-1}\pmod R,
\qquad
\Theta_i=\sigma E_i\pmod R.
\tag{5}
\]

逐边 raw 公式给出

\[
q_i g_i z_i\equiv z_{i-1}\pmod R,
\qquad
E_i z_i\equiv p\pmod R,
\qquad
\Theta_i z_i\equiv-1\pmod R.
\tag{6}
\]

receipt 的末三条标签必须为 \(13,2,2\)，并且其 physical rows 分别是

\[
N_R(4x),\qquad N_R(2x),\qquad N_R(x).
\tag{7}
\]

若同一来源坐标在三点都落在 \(\epsilon tx\) 一侧，其中
\(\epsilon\in\{+1,-1\}\)、\(t=4,2,1\)，由 \(4Mx\equiv1\pmod R\) 得

\[
\boxed{
\Theta_4=-\epsilon M,
\qquad
\Theta_2=-2\epsilon M,
\qquad
\Theta_1=-13\epsilon
\pmod R.}
\tag{8}
\]

因此相位不是 endpoint 倒推时可自由指定的 multiplier。它由 source、raw labels 和
gcd reductions 唯一运输而来；orientation 也必须进入 receipt identity。

## 3. c=3 根的准入

在 (1)--(8) 和一份重新验证的 source-chart typed fiber 下，创建

```text
adapter             = c3_source_lineage_even_tail_root_receipt_v1
state_origin        = c3_source_lineage_even_tail_root_receipt_v1
source_tree_scope   = fresh_source_tree_only
normal_form         = c3_source_lineage_even_tail_overflow_seed_v1
phase               = type_i_c3_source_lineage_tree
equation_target     = (4, p)
marked_solution_set = Sol(p)
chart               = (R, K)
absorbed_support    = 1
state_id            = hash(chart, fiber, raw digest, lineage digest, orientation, scope)
```

这给出 root receipt 的 E1--E3：E1 是 (2) 的实际 source 和整条 raw replay，E2 是
(4) 及 \((d,n)=(3,13)\)，E3 是 typed fiber、尾标记和内容寻址 state identity。单独
调用这份 receipt 仍只是分析证据；它只能作为本卡指定 phase edge 的 target，不能从
`charged_history_only` 或 formal \(p\)-parent 直接初始化。

## 4. 两条 E1--E5 边

令 \(S\) 是输入的 `q=1 G` endpoint，\(T\) 是第 3 节的 c=3 根。定义

\[
R_{11}=11,
\qquad
K_{11}=\frac{11p+1}{4}=3(22h+1),
\tag{9}
\]

并令 \(U=(p,11,K_{11};A=3)\)。在 terminal-first 已由外层 dispatcher 满足时，
本卡登记

\[
S\longrightarrow T\longrightarrow U.
\tag{10}
\]

| 边 | E1 | E2--E3 | E4 | E5 |
|---|---|---|---|---|
| \(S\to T\) | q=1 G endpoint 与第 3 节 source receipt | c=3 closed chart、typed fiber、state digest | \(\operatorname{id}:\operatorname{Sol}(p)\to\operatorname{Sol}(p)\) | phase \(2\to1\) |
| \(T\to U\) | 已验证 fresh root | (9) 与独立的 \(R=11\) typed fiber | 同一恒等映射 | \(A:1\to3\) |

全局 phase policy 只允许非终端转移

\[
\text{Type II q=1 G}\to\text{c=3 tree},
\qquad
\text{c=3 tree}\to\text{c=3 tree},
\qquad
\text{c=3 tree}\to(n<p),
\tag{11}
\]

禁止 c=3 tree 非终端返回 Type II；其后的 Type II 结果只能是 terminal leaf。取

\[
B_p=\frac{(p-1)^2}{4},
\qquad
\Pi(S)=[2,1,0],
\qquad
\Pi(T)=[1,B_p,K],
\qquad
\Pi(U)=[1,B_p/3,K_{11}/3].
\tag{12}
\]

按字典序有 \(\Pi(S)>\Pi(T)>\Pi(U)\)。第一项由 (11) 支付，第二项由
\(B_p>B_p/3\) 支付。raw word 的中间点不承担 E5。

## 5. 控制与边界

`type_ii_q_one_c3_source_lineage_phase_root_entry.py --verify` 从整数重新回放

\[
p=73,\quad1033,\quad3313
\tag{13}
\]

三份 p-first c=3 receipt；它们均是 q=1 G endpoint，尾 orientation 为 \(-1\)，并通过
(10) 的两套 E1--E5。它也回放 \(p=1009\) 的 `349,41,1013,13,2,2` non-p-first bypass，
得到 orientation \(+1\) 与 (8) 的正向控制；但 \(p=1009\) 不是 q=1 G endpoint，故它不是
(10) 的 control。

本卡没有证明：

1. 每个核心素数、或每个 q=1 G endpoint，存在 c=3 source-lineage receipt；
2. \(R=11\) 后的 selector 在所有未命中 terminal 的状态上有出口；
3. 任何全局 G/Type I exit、递降或 Erdős--Straus 猜想。

所以它把一个原先仅有 E1--E3 的 c=3 raw receipt 接成**条件性**的两边 macro，
而不把有限 controls 误升格为全称结论。

复现：

    python3 reproductions/type_ii_q_one_c3_source_lineage_phase_root_entry.py --verify
