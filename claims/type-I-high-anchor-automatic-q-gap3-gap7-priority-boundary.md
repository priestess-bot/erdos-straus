---
kind: claim
claim_id: type-I-high-anchor-automatic-q-gap3-gap7-priority-boundary
title: automatic-q 高锚来源的 gap-3/gap-7 terminal-priority 边界
statement: >-
  p=34897 与 p=68713 都是实际的 beta_0=2 fresh-root complete-excess
  automatic-q=2 高锚来源：各自有可重放的 charged same-chart parent、第二
  full-excess Q_1=R-1，以及 C=2A 的 automatic cofactor gate 和 h=1。
  p=34897 完整避开 gap-7，却有 gap-3 Type I 证书 d=5，故只含 gap-7 的
  terminal-first prefix 会在 H 和 transient S 上错误返回 no_output。p=68713 有
  gap-3 Type I d=41 和 gap-7 Type I d=5，验证有序的 gap-3、gap-7 前缀须先选
  gap-3 terminal。该结果关闭两个宏候选，不提供 nonterminal macro 或全局覆盖结论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-automatic-q-source-template
  - type-I-high-anchor-cofactor-terminal-guarded-adapter
  - short-certificate-equivalence
topics:
  - Erdos-Straus
  - type-I
  - high-anchor
  - automatic-q
  - complete-excess
  - terminal-first
  - priority-guard
  - gap-three
  - gap-seven
  - proof-boundary
sources:
  - claim: type-I-high-anchor-automatic-q-source-template
    role: fresh-root-and-automatic-gate-normal-form
  - claim: type-I-high-anchor-cofactor-terminal-guarded-adapter
    role: source-and-transient-priority-requirement
  - reproduction: reproductions/type_i_high_anchor_automatic_q_priority_guard.py
    role: exact-parent-gate-and-priority-prefix-replay
visibility: public
last_checked: '2026-08-16'
---

# automatic-q 高锚来源的 gap-3/gap-7 terminal-priority 边界

## 1. 问题

automatic C=qA 高锚构造已有两个正的 source/path 控制，但二者恰好都被
gap 7 截断。不能因此把“未命中 gap 7”解释成一个可入队的宏。这里给出两个
更严格的控制：它们都有真实的 fresh-root parent；其中 p=34897 完整避开 gap 7，
却被 gap 3 直接终止，另一行则检查当两个 gap 都命中时的优先级顺序。

这使 terminal-first 的要求可检验地落在 persistent 高锚 H 和 bundle 内部的
transient overflow S 两个位置，而不是只在一个控制例的末尾附一条 terminal 注记。

## 2. 两个实际 automatic-q 来源

下表中 R_0=2A+1 是 core root，第一次 complete-excess rechart 的 bundle 为

\[
Q_0=A,\qquad \beta_0=2,
\]

并产生 canonical 高锚 H=(p,R,K;A)。其 charged parent 是同图表的
support-promotion receipt，因而不是 p=409 那种缺少 charged parent 的临时算术行。
第二 bundle 满足

\[
Q_1=R-1,\qquad \beta_1=1,
\]

并给出 M=A(R-1)、C=2A。所以 a=A/(A,C)=1，cofactor gate 自动通过；
两个控制都处于 h=1 的最小正相位。

| p | A | R_0 | H=(R,K) | M | C | h |
|---:|---:|---:|---|---:|---:|---:|
| 34897 | 13635 | 27271 | (39827,347460705) | 543027510 | 27270 | 1 |
| 68713 | 31143 | 62287 | (103067,1770510693) | 3209784438 | 62286 | 1 |

对第一行，parent 的中心纤维有一个可复放的 F witness；对第二行，模
R=103067 的 Legendre character 给出 G separator。因而二者的 parent receipt
均实际结束于所列 H，并带图表无关的 Sol(p) 恒等 lift。

## 3. gap-7-only 前缀为何不足

令原始的弱 prefix 只有一项 `direct_bradford_gap_7`。对 p=34897，完整的
gap 7 Type I/II 除子检查返回 `no_output`；因此若该 prefix 被错误地当作全部
优先菜单，它会允许 H 到 T 的宏继续构造。

但两数都满足 gap 3 的完整 Type I 条件：

\[
\begin{aligned}
\frac4{34897}
 &=\frac1{8725}+\frac1{101492110}+\frac1{6180388933859150},
 &&(m,d)=(3,5),\\
\frac4{68713}
 &=\frac1{17179}+\frac1{393473556}+\frac1{11328397601986332},
 &&(m,d)=(3,41).
\end{aligned}
\]

每个恒等式均由完整 Bradford Type I 除子判据重建并以整数等式验证；这不是从有限
factor menu 取到的近似命中。第二行还存在一个较晚的 gap 7 Type I certificate
(m,d)=(7,5)，所以它不用于证明 gap-7-only 的空性；它用于确认有序菜单不会跳过
更早的 gap 3 leaf。

## 4. 正确的有限 priority 回执

在当前明确声明的前缀中取有序列表

```text
1. direct_bradford_gap_3 / short_certificate/v1
2. direct_bradford_gap_7 / short_certificate/v1
```

每次回放都绑定输入 `state_id`、有序列表及其 digest。对上述两个 p，在 H 和
S 上都在第 1 项返回同一个 `terminal_leaf`；第 2 项不会被当作可以跳过的唯一检查。
特别地，p=34897 说明第二项单独运行并不能替代第一项。因此它们不能生成
`pending_dispatch`，更不能被登记为 `verified_edge`。

这正是 guarded-adapter 合同所需的局部结论：`no_output` 只能相对于一个明确、版本绑定的
前缀解释。这里并未把 (3,7) 声称为所有 terminal 的完备菜单。

## 5. 边界和下一接口

本卡的正面推进是找到两条带真实 charged parent 的 automatic-q source，并证明它们都被
有序前缀正确抢占。p=34897 否定的是下列错误推断：

\[
\text{automatic-q source} + \text{gap-7 miss}
\Longrightarrow \text{可递归宏}.
\]

它不构造 terminal-first unresolved source，也没有完成 source/target 的完整 typed macro
E4 或全局 E5 调度。后续来源搜索必须至少同时避开这个已编码的 gap-3/gap-7 前缀；即便如此，
仍须通过更高优先 terminal/alternate 菜单、typed lift 和全局良基势。

## 聚焦验证

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_priority_guard.py --verify
```
