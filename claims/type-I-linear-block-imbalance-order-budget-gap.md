---
kind: claim
claim_id: type-I-linear-block-imbalance-order-budget-gap
title: 双向未决二进状态的阶—预算缺口
statement: 在冻结 200 个核心素数完整线性谱的 11673 个双向广义二进未决状态中，全部满足 ord_R(2)>v_2(2K)；其中 7433 个没有任何预算内正向/反向同余类，4186 个只有正向同余类但高度失败，54 个只有反向同余类但高度失败。该缺口是二进传输族的有限结构证书，不是目标平方除子不存在性定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-linear-block-imbalance-bidirectional-dyadic
  - type-I-general-dyadic-terminal-transfer
topics:
- type-I
- linear-source
- block-imbalance
- dyadic
- multiplicative-order
- budget-gap
- fourier
- capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 双向未决二进状态的阶—预算缺口

## 诊断量

对二进不平衡状态，记

\[
o_R(2)=\operatorname{ord}_R(2),\qquad
J_{\max}=v_2(2K)=v_2(K)+1,\qquad
j_0=|\lambda_2|.
\]

正向传输只能使用

\[
J\equiv j_0\pmod{o_R(2)},\qquad 1\le J\le J_{\max},
\]

反向传输只能使用

\[
J\equiv-j_0\pmod{o_R(2)},\qquad 1\le J\le J_{\max}.
\]

若任一方向同时满足高度不等式，就得到双向广义二进终端。对双向未决状态，下面的
有限审计显示一个共同的必要缺口：

\[
o_R(2)>J_{\max}.
\]

这并不意味着没有预算内同余类：当 \(|\lambda_2|\) 在阶 \(o_R(2)\) 下有小的剩余时，
仍可能有一个 \(J\le J_{\max}\)，但其对应的高度方向不等式失败。

## 精确冻结结果

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_order_budget.py
~~~

输入哈希锁定为
\`83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f\`。结果：

~~~text
record_count: 11673
order_budget_gap_count: 11673
minimum_order: 2
maximum_order: 295249762
minimum_budget: 1
maximum_budget: 13
residue_window_counts:
  none: 7433
  forward_only: 4186
  reverse_only: 54
~~~

与较小块平方分流交叉后：

\[
\begin{array}{c|r}
\text{分支}&\text{状态数}\\ \hline
\text{偶终端}&4186\\
\text{奇源标记下降}&2963\\
\text{混合奇偶平方障碍}&4524
\end{array}
\]

其中 4186 个正向同余窗口全部因方向不等式失败，54 个反向窗口全部因方向不等式失败；
7433 个状态在预算区间内没有任何方向的同余窗口。

## 对统一选择器的意义

这个结果把剩余二进分支从“某个 \(J\) 还没试到”改写为一个可计算的阶—预算缺口。
在循环商上，\(\operatorname{ord}_R(2)\) 给出规范角色阶，而 \(J_{\max}\) 给出有限
指数盒的二进预算；因此它可以直接作为 Fourier/关系格证书的输入，并与跨状态
\(q\)-进容量比较。

边界仍然明确：阶—预算缺口只排除当前二进传输族，不能推出
\(-1\notin\mathcal C_R(K)\)，也不能替代目标平方除子、普通 Type II 或跨状态下降。
