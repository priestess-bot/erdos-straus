---
kind: claim
claim_id: type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
title: p=5281 的 Jacobi-odd 有限物理 source/transition 账本
statement: 对 p=5281 的 G-anchor 图表 R=5279、K=6969600、Q=2639，Jacobi-odd 完整 divisor 菜单恰为 {7,91,203,2639}。universal p-root 后的偶坐标优先表示重排显式标为非 raw；每个标签通过无损 (M,t) 编码给出真实 determinant 行，并且所有端点均留在该菜单内的 m=1 divisor-factor raw 边恰为 7->91 (q=13)、7->203 (q=29)、91->2639 (q=29)、203->2639 (q=13)。因此该声明的有限菜单拥有完整的 actual source/path 与 physical transition 账本；203 与 2639 共享未标记行 (M,C,d,n)=(2323200,3,5278,9287521) 但尾 t 分别为 1751、1759，故精确尾不可删除。该账本仍是 G/Jacobi 二次控制：它没有 F 型奇 q-primary 锚定、row-to-anchor 映射、共同仿射标签律、carry-lift、E4 或 E5，因而必须保持 ANCHORED_PHASE_MAP_UNCLOSED 和 analysis_evidence。p=5281 本身还有 gap-7 Type II terminal，terminal-first 不会进入该账本的递归分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-raw-fixed-chart-factor-projection
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-anchored-affine-phase-tree-capacity
topics:
  - type-I
  - G-state
  - G-anchor
  - physical-source-table
  - physical-transition
  - raw-path
  - Jacobi-symbol
  - marked-tail
  - source-completeness
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: finite-Jacobi-odd-source-menu
  - claim: type-I-g-anchor-raw-fixed-chart-factor-projection
    role: lossless-marked-row-embedding
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: raw-transition-and-tail-necessity
  - claim: type-I-anchored-affine-phase-tree-capacity
    role: AAL-gate-boundary
  - reproduction: reproductions/type_i_g_anchor_jacobi_p5281_physical_ledger.py
    role: fixed-ledger-verifier
visibility: public
last_checked: '2026-08-07'
---

# p=5281 的 Jacobi-odd 有限物理 source/transition 账本

## 1. 声明的有限宇宙

取 G-anchor 图表

\[
p=5281,
\qquad R=p-2=5279,
\qquad K=\frac{(p-1)^2}{4}=6969600,
\qquad Q=\frac{p-3}{2}=2639=7\cdot13\cdot29.
\tag{1}
\]

这里

\[
K=2^8\cdot3^2\cdot5^2\cdot11^2,
\qquad (Q,K)=1.
\tag{2}
\]

令 \(\chi_R\) 为 Jacobi 角色，并只声明下面这个有限 endpoint 菜单：

\[
\mathcal D^-=
\{\delta:\delta\mid Q,\ \chi_R(\delta)=-1\}
=\{7,91,203,2639\}.
\tag{3}
\]

`source_complete` 在本卡中只指 (3)：universal \(p\)-source 先实际到达
\((1,R-1,1)\)，再在同一无序节点中把包含 \(2Q\) 的坐标列为第一坐标；该重排明确
记录为 `coordinate_swap_not_a_raw_transition`。随后按 \(\delta\) 的规范素因子词实际到达
每一个 (3) 中的 endpoint。
它不声称覆盖完整 raw 图、所有 G source，或任何 F-state。

## 2. 无损物理行表

对每个 \(\delta\in\mathcal D^-\)，写

\[
x_\delta=\frac{2Q}{\delta},
\qquad y_\delta=R-x_\delta,
\qquad C_\delta=(y_\delta,K),
\qquad M_\delta=K/C_\delta,
\qquad t_\delta=y_\delta/C_\delta.
\tag{4}
\]

再令 \(d_\delta=p-C_\delta\)、\(n_\delta=4M_\delta-R\)。逐行有

\[
p n_\delta=4M_\delta d_\delta+1,
\qquad
M_\delta t_\delta^{-1}\equiv K\delta\pmod R.
\tag{5}
\]

实际账本为：

\[
\begin{array}{c|r|r|r|r|r}
\delta&M&C&t&d&n\\ \hline
7&278784&25&181&5256&1109857\\
91&6969600&1&5221&5280&27873121\\
203&2323200&3&1751&5278&9287521\\
2639&2323200&3&1759&5278&9287521
\end{array}
\tag{6}
\]

这是每一行的实际整数 \((M,C,t,d,n)\)，而不是只保留有限群角色值的表。

## 3. 完整的声明内 transition relation

为避免将 reverse peeling 误写成 actual raw 方向，令边方向为

\[
e\xrightarrow{q}qe.
\tag{7}
\]

这里每条边都在 \(m=1\) 层选取偶坐标 \(2Q/e\)，经过实际 raw step 后到达
\(2Q/(qe)\)。菜单内的全部此类边恰为

\[
7\xrightarrow{13}91,
\qquad
7\xrightarrow{29}203,
\qquad
91\xrightarrow{29}2639,
\qquad
203\xrightarrow{13}2639.
\tag{8}
\]

反向去皮才是 \(qe\to e\)。验证器逐边重算 selected coordinate、超容量、unit 条件、shift、
gcd reduction 与有序 destination；(8) 是所有满足

\[
e,qe\in\mathcal D^-,
\qquad q\mid Q,
\tag{9}
\]

的 divisor-factor raw 边，故 `physical_transition_complete=true` 也严格限于 (9)。
完整 raw 图并不闭合在这个菜单内：例如其中六条已验证的合法离开边为

\[
\begin{aligned}
(754,4525)&\xrightarrow{181}(25,5254), &
(58,5221)&\xrightarrow{23}(227,5052),\\
(58,5221)&\xrightarrow{227}(23,5256), &
(26,5253)&\xrightarrow{17}(309,4970),\\
(26,5253)&\xrightarrow{103}(51,5228), &
(2,5277)&\xrightarrow{1759}(3,5276).
\end{aligned}
\tag{10}
\]

因此 `full_raw_transition_complete=false`；这些 exit 也不能被静默丢弃或当成菜单内边。

## 4. 尾标记的必要性

标签 \(203\) 和 \(2639\) 在 (6) 中有同一个未标记 physical row：

\[
(M,C,d,n)=(2323200,3,5278,9287521),
\tag{11}
\]

但精确尾不同：

\[
t_{203}=1751,
\qquad t_{2639}=1759.
\tag{12}
\]

特别地，它们以同一个逆向标签 \(q=29\) 去皮时分别回到 \(7\) 和 \(91\)。所以
\((M,C,d,n)\)，甚至再加 \(q\)，都不能确定带标记 physical successor；尾 \(t\) 是该
source/transition 账本中不可删的字段。

## 5. AAL 边界和 terminal-first

本账本已完成两个有限物理前提：声明的 Jacobi-odd source 菜单完整，且其声明内 raw
transition relation 完整。但它没有以下 AAL 字段：

```text
F_q_primary_anchor         = not_available_in_this_G_Jacobi_C2_control
row_to_anchor_map          = not_available
common_affine_chart        = not_available
physical_label_interval    = not_available
physical_label_multiplicity = not_available
physical_carry_status      = not_evaluated_for_a_cofactor_lift
```

故状态必须为 `ANCHORED_PHASE_MAP_UNCLOSED`，不是锚定仿射容量实例，更不是 E1--E5
edge。它的作用是证明“有限、物理、带方向 source/transition table”本身可以严格建立，
并固定未来 F/奇 \(q\) 表还必须补上的字段。

此外 \(7\mid Q\)，有直接 Type II leaf

\[
\frac4{5281}
=\frac1{1322}+\frac1{998109}+\frac1{1319500098}.
\tag{13}
\]

所以 terminal-first selector 必先输出 (13)，不会把本控制用于递归。

窄复现：

~~~bash
python3 reproductions/type_i_g_anchor_jacobi_p5281_physical_ledger.py --verify
~~~
