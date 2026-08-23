---
kind: claim
claim_id: f2-post-g-h4-target-high-support-owner-v1
title: H4 clean-q final target 的高支撑 overflow 归属与 F/G owner 解耦
statement: >-
  在 actual q=1 high-C=2 19-phase H4 clean-q macro 的任一 nonterminal single-side
  或 atomic endpoint 上，canonical support M_T=lcm(M4,Q_x,Q_y) 满足
  M_T>M4>p^4/8>B_p，且既有 stutter closure 给 1<=c_T<=p-2。于是
  R_T=(4M_Tc_T-1)/p>p，A_T=M_T>1，A_T|K_T；target 必是 high-support
  Type-I overflow。target-local F/G classifier 只重算 certificate_context，不能改变
  persistent owner；若没有更窄的已登记 high-support predicate，它唯一进入现有
  type_i_a_gt_one_overflow_residual family。H4 source/path 与 atomic occurrence 保存在
  edge receipt，不需要新 H4-F/H4-G family。该归属证明 E3 的 family-shape 部分，但
  common serializer/admission、atomic arm 和该 overflow family 的 total successor 仍为
  外部依赖；因此不关闭 H4 descendant totality、F2 或 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - t6-persistent-selector-state-v1
topics:
  - F2
  - H4
  - clean-q
  - high-support
  - overflow
  - F-state
  - G-state
  - owner
  - re-entry
  - proof-boundary
sources:
  - data: data/t6-wave1/f2-post-g-h4-target-owner-v1.json
    role: machine-readable-target-shape-and-owner-request
  - reproduction: reproductions/f2_post_g_h4_target_owner.py
    role: focused-bound-and-family-predicate-replay
visibility: public
last_checked: '2026-08-24'
---

# H4 target 的 high-support owner

## 1. 输入

保留 actual H4 clean-q macro 的记号。其 persistent parent P 通过 H3=>H4 source/path、
terminal-first 和 clean-q guards；endpoint 的 unique complete-excess blocks 为 (Q_x,Q_y)，
且 canonical target 为

\[
M_T=\operatorname{lcm}(M_4,Q_x,Q_y),
\qquad
K_T=M_Tc_T,
\qquad
R_T=\frac{4K_T-1}{p}.
\tag{1}
\]

actual endpoint 已证明只有 (Q_x=1<Q_y) 或 (Q_x,Q_y>1)，并且

\[
1\le c_T\le p-2.
\tag{2}
\]

## 2. support 必为 high

H4 carrier bound 给出

\[
M_4>M_0=\frac{(p-1)(2p+1)(2p^2-3p-1)}8>\frac{p^4}{8}
\qquad(p\ge73).
\tag{3}
\]

target endpoint 至少有 (Q_y>1)，其完整超额指数超过 (K_4)，从而也超过
(M_4\mid K_4)。因此

\[
M_T>M_4>\frac{p^4}{8}.
\tag{4}
\]

另一方面 (B_p=(p-1)^2/4<p^2/4)，所以 (4) 强制

\[
\boxed{A_T=M_T>B_p.}
\tag{5}
\]

## 3. target 必为 overflow

由 (1)--(2)、(c_T\ge1) 与 (4)，

\[
R_T=\frac{4M_Tc_T-1}{p}
>\frac{p^4/2-1}{p}
>p.
\tag{6}
\]

并且 (A_T=M_T\mid K_T)、(A_T>1)。所以 target 的直接事实是：

```text
major_phase = TYPEI
provenance_kind = OVERFLOW
is_overflow = true
support_A = carrier_M = M_T > B_p
chart = (R_T,K_T), R_T>p
mark = ROOT_SOL
```

这些字段在调用 F/G classifier 以前就已确定。

## 4. F/G 是 certificate，不是 owner

target-local total rechart 对同一个 ((p,R_T,K_T,A_T)) 可能输出 F 或 G。它只改变
`target_fiber`、separator/witness 与 signed-defect fields；不改变 (5)--(6)、equation target、
mark、support 或 H4 edge provenance。

在现有 persistent family predicate 中：

- `type_i_a_one_overflow` 不命中，因为 (A_T>1)；
- `type_i_low_support_persistent_overflow` 不应凭 H4 edge 伪造
  `same_chart_promotion_receipt`；
- `type_i_high_support_sink` 只有在 target 另有实际 sink-SCC receipt 时才是更窄 owner；
- 否则 `type_i_a_gt_one_overflow_residual` 必命中。

因此无需创建 `H4_F_DESCENDANT` 或 `H4_G_DESCENDANT` persistent family。H4 source/path、
single-side/atomic occurrence 与 target-local F/G receipt保存在 edge payload；owner 由 target
直接 facts 决定。

## 5. E3 与总性边界

本定理建立：target normal-form 的 inequality/type facts 与 existing-family membership。
尚未建立：

1. shared `PersistentSelectorStateV1` serializer 和 common gate 的实际调用；
2. atomic output 的 Agent 3 arm/owner payload；
3. `type_i_a_gt_one_overflow_residual` 或 `type_i_high_support_sink` 的全称 outgoing exit。

所以准确组合接口是

```text
H4 final target
  -> terminal
   | admitted high-support overflow
       -> Agent 2 overflow/high-support totality theorem
```

若 Agent 2 的 totality 尚未建立，则 `H4_F_G_DESCENDANT_TOTALITY` 仍为 OPEN_EXTERNAL_DEPENDENCY。
