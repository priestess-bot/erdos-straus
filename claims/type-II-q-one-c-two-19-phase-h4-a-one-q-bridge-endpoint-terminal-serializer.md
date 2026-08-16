---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-endpoint-terminal-serializer
title: H4 clean q-bridge endpoint full-excess sink 的直接 Type I terminal 证书
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 的 clean
  q bridge 中，若 q endpoint 满足 Q_x=Q_y=1，则 x_q y_q divides K4。于是有唯一的
  canonical sorted denominator triple sort(K4/y_q,K4/x_q,p*K4)，并且其倒数和严格等于
  4/p。端点还满足 p not divides K4 x_q y_q，故这是直接可输出的 Type I terminal
  certificate，而不是等待 typed target、state serializer、solution lift 或 potential 的
  candidate。该结论只关闭 endpoint full-excess terminal 支，不处理 source-level priority
  prefix 或任一 nonterminal single-side/atomic-split 支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - terminal-certificate
  - complete-excess-bundle
  - direct-construction
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-q-endpoint-and-maximal-block-taxonomy
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
    role: endpoint-is-the-only-full-excess-terminal-location
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: p-free-endpoint-and-H4-K-context
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
    role: actual-high-H4-antecedent-exclusion
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: full-excess-sink-criterion
  - concept: denominator-escape-state-contract
    role: direct-terminal-leaves-do-not-require-E1-to-E5
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_endpoint_terminal_serializer.py
    role: focused-full-excess-sink-serialization-control
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge endpoint full-excess sink 的直接 Type I terminal 证书

## 1. 端点 sink 输入

保留 clean \(q\)-bridge 的 actual endpoint

\[
x_q+y_q=R_4,
\qquad
pR_4+1=4K_4.
\tag{1}
\]

若两个 maximal complete-excess block 都为空，

\[
Q_{K_4}(x_q)=Q_{K_4}(y_q)=1,
\tag{2}
\]

则定义本身给 \(x_q\mid K_4\)、\(y_q\mid K_4\)。primitive q-word 还给
\((x_q,y_q)=1\)，故

\[
\boxed{x_qy_q\mid K_4.}
\tag{3}
\]

这正是 full-excess sink，但下面不把它只作为一个需要外部实现的布尔标签。

## 2. 确定性的三分母 serializer

定义无序的三分母集合

\[
\boxed{
\mathcal D_q=
\left\{
\frac{K_4}{y_q},\
\frac{K_4}{x_q},\
pK_4
\right\},
}
\tag{4}
\]

并按非降序输出它。式 (3) 使前两个数均为正整数；取排序只消除 raw pair 的显示方向，
不改变证书。直接计算给

\[
\begin{aligned}
\sum_{d\in\mathcal D_q}\frac1d
&=\frac{y_q}{K_4}+\frac{x_q}{K_4}+\frac1{pK_4}\\
&=\frac{R_4}{K_4}+\frac1{pK_4}\\
&=\frac{pR_4+1}{pK_4}
=\frac4p.
\end{aligned}
\tag{5}
\]

actual H4 clean bridge 还满足 \(p\nmid K_4x_qy_q\)。所以 (4) 的前两个分母不被
\(p\) 整除，而第三个分母恰被 \(p\) 整除；这是直接的 Type I terminal certificate。

## 3. 对状态合同的影响

这个分支输出的是 `terminal_leaf`，不是新状态。因此不需要：

- target typed reclassification 或 target `state_id`；
- E4 的跨状态提升；
- E5 的严格势；
- single-side payload 或 atomic owner/ledger。

它仍服从较早的 state-level terminal/alternate priority：若 H4 source 已有更高优先级
输出，selector 返回该输出即可；若到达任意符合 (2) 的 endpoint，(4) 是无需额外
serializer 的确定性直接终端。对本卡的 actual high-H4 scope，后继
[\(y\)-block 非空引理](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty.md)
进一步证明 (2) 的 antecedent 为空。因此本卡保留正确的条件性 Type I serializer，
而 actual H4 nonterminal endpoint 仍须走 y-side single-side 或 atomic-split guarded macro。

## 4. 聚焦回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_endpoint_terminal_serializer.py --verify
```

回执只核对一个 \(p=73,R=23,K=420,\{x,y\}=\{2,21\}\) 的 full-excess sink：
它重建 (4) 为 \((20,210,30660)\) 并逐项核验 (5)。该控制不声称该点是 actual
19-phase H4 predecessor，也不扫描素数或分母范围。
