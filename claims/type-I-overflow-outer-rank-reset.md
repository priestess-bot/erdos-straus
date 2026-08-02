---
kind: claim
claim_id: type-I-overflow-outer-rank-reset
title: overflow RESET 的 joined-support 外层秩递降
statement: 设 overflow 满足 pn=4Md+1，并携带旧 charged support A|M，且 1≤A≤B_p=(p-1)^2/4。对对称双载体 t∈{d,M mod p}，令 A'=lcm(A,t)，并取 t 的规范图表 (R_t,K_t)。若 A'>A、A'|K_t 且 floor(((p-1)^2/4)/A')<floor(((p-1)^2/4)/A)，则 (p,R_t,K_t;A') 是带恒等解提升和完整 E1--E5 的 overflow_outer_rank_reset_v1 边；R_t<p 时目标是 marked absorb，R_t>p 时目标仍是 overflow 但 absorbed-support 外层秩严格下降。若任一条件失败，旧支撑不能被该 RESET 丢弃，回执只能保留为 analysis_evidence。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-support-preserving-dual-criterion
  - type-I-marked-support-accumulation-rechart-saturation
  - type-I-overflow-phase-reset-cycle-boundary
topics:
- type-I
- overflow
- phase-reset
- charged-support
- outer-rank
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: joined-support RESET verifier and E1--E5 receipts
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 24-channel classification
visibility: public
last_checked: '2026-08-03'
---

# overflow RESET 的 joined-support 外层秩递降

## 1. 精确规则

设一个已有来源回执的 overflow 状态满足

\[
pn=4Md+1,\qquad K_M=M C,\qquad R_M=4M-n>p,
\]

并携带此前已经承诺保留的支撑 \(A\mid M\)。对对称双通道取

\[
t\in\{d,r\},\qquad r=M\bmod p,
\]

并令 \((R_t,K_t)\) 为载体 \(t\) 的规范图表。RESET 不得把 \(t\) 直接写成新的
charged support；必须先加入旧承诺：

\[
 A'=\operatorname{lcm}(A,t).
\]

如果 \(A'\mid K_t\)，则目标状态可以携带 \(A'\)，并由图表无关的标记集
\(\operatorname{Sol}(p)\) 采用恒等提升。外层秩定义为

\[
 B_p=\frac{(p-1)^2}{4},\qquad
 \Pi_A(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

该分支先要求 \(1\le A\le B_p\)。由于 \(A'/A\) 是大于 \(1\) 的整数，且
\(A'\) 还要通过显式的势值比较，才可写成

\[
 \Pi_A(A')<\Pi_A(A).
\]

实现仍显式重算这个不等式，而不把“支撑变大”当作隐含证明。

## 2. E1--E5 边界

当

\[
A'>A,\qquad A'\mid K_t,
\qquad \Pi_A(A')<\Pi_A(A),
\]

对称双图表给出合法的 `overflow_outer_rank_reset_v1`：

- E1：目标方程仍为 \(4/p\)，且 \(4K_t=pR_t+1\)；
- E2：\(A'\mid K_t\)，目标状态的 charged support 合法；
- E3：来源、双载体和 \(A'\) 均由 overflow determinant 回执重算；
- E4：标记集取图表无关的 \(\operatorname{Sol}(p)\)，恒等映射提升全部成员；
- E5：\(\Pi_A(A')<\Pi_A(A)\) 是预先定义且不可由该边重置的外层秩下降。
若源 \(A>B_p\)，当前 \(\Pi_A=0\)，本分支拒绝该 RESET，必须改用另一个外层秩。

若 \(R_t<p\)，目标属于普通 `marked_absorb`；若 \(R_t>p\)，目标仍是
`overflow`，但这是一个可以继续交给 overflow 选择器的严格递降状态。后一类不能
伪装成直接 Type I 终端，却不需要等待 \(R_t<p\) 才能支付 E5。

若 \(A'=A\)，或者 \(A'\nmid K_t\)，则该通道不能丢弃旧支撑；回执只记录
`analysis_evidence`，并列出 `strict_support_gain` 或
`joined_support_divisibility` 缺失。这样旧的 \(p=73\) 载体循环不能通过把
\(t<M\) 误写成全局秩来闭合。

## 3. 聚焦复现

统一 selector 对现有 12 个 overflow、24 个双通道逐项重算：

| 分类 | 数量 |
|---|---:|
| 对称双通道 | 24 |
| joined-support 外层秩 verified edge | 8 |
| 其中 \(R_t<p\) 的吸收目标 | 3 |
| 其中仍为 overflow 的秩递降目标 | 5 |
| 被拒绝的通道 | 16 |

新增的 overflow 目标包括：\(p=409\) 的同图表支撑增强、\(p=241\) 的
\(A=38\to190\) 支撑增强，以及 \(p=73\) 可达冲突行的
\(A=19\to38\) 支撑增强。它们的图表 \(R\) 可以保持不变或仍大于 \(p\)，但
\(A\) 已写入状态并严格支付外层秩。

这不等于旧 RESET 局部载体边全部合法。以 \(p=73,M=38,A=19\) 为例，小图表
载体 \(t=12\) 的 \(K_t=420\) 不吸收
\(\operatorname{lcm}(19,12)=228\)，因此该方向仍被拒绝；可用的是另一条支撑保持
通道 \(t=38\)，它把同一图表状态的支撑从 \(19\) 提升到 \(38\)。这一区分正是
`carrier-size` 局部下降与不可重置外层秩的差异。

## 4. 逻辑边界

该规则把“RESET 后不得丢弃旧支撑”变成可核验的 E2/E5 条件，并为仍然 overflow 的
目标提供一种严格递降类型。但它没有证明每个 \(A>1\) overflow 至少有一个满足三项
条件的 \(t\)。当前 16 个被拒绝通道仍需 alternate、直接终端、跨状态容量矛盾，或
另一种不可重置秩来处理；因此该主张是统一选择器的中间引理，不是 Erdős--Straus
猜想的全称证明。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于
`reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`overflow_outer_rank_reset`。
