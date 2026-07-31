---
kind: claim
claim_id: type-I-linear-block-imbalance-order-budget-gap
title: 双向广义二进终端的阶—预算二分
statement: 在线性块不平衡的奇除子归一化中，令 A≡2^j0 B (mod R)、o=ord_R(2)、J_max=v_2(2K)。若 o≤J_max，则正向或反向至少一个方向必满足一般二进传输的预算与严格高度条件，因而产生合法偶终端；所以任何双向未决状态必满足 o>J_max。冻结 200 个核心素数完整线性谱的 11673 个双向未决状态全部复现该必要缺口，其中 7433 个无预算内方向、4186 个只有正向方向但高度失败、54 个只有反向方向但高度失败。其逆命题不成立，且该缺口只排除本二进传输族。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-linear-block-imbalance-bidirectional-dyadic
  - type-I-general-bidirectional-dyadic-window-selector
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
- claim: type-I-general-bidirectional-dyadic-window-selector
  role: exact-two-window-selector
visibility: public
last_checked: '2026-07-31'
---

# 双向广义二进终端的阶—预算二分

## 全称二分定理

这是一般[双向二进窗口选择引理](type-I-general-bidirectional-dyadic-window-selector.md)
在 \(A,B\) 都为奇数时的直接推论。下面保留自包含证明，以固定线性块分支的作用域。

在线性块不平衡三分的奇除子归一化中，取互素奇除子

\[
A,B\mid 2K,
\qquad
A\equiv 2^{j_0}B\pmod R,
\qquad j_0\ge 1.
\]

记

\[
o=\operatorname{ord}_R(2),
\qquad
J_{\max}=v_2(2K).
\]

则有

\[
\boxed{
o\le J_{\max}
\quad\Longrightarrow\quad
\text{正向或反向至少存在一个合法广义二进偶终端}.}
\tag{1}
\]

等价地，任何双向未决状态都必满足

\[
\boxed{o>J_{\max}.}
\tag{2}
\]

### 证明

令 \(u\in\{1,\ldots,o\}\) 是 \(j_0\bmod o\) 的正代表；若余数为零则取
\(u=o\)。同样令 \(v\in\{1,\ldots,o\}\) 是 \(-j_0\bmod o\) 的正代表。于是

\[
A\equiv2^uB\pmod R,
\qquad
B\equiv2^vA\pmod R.
\tag{3}
\]

若 \(o\le J_{\max}\)，则 \(1\le u,v\le J_{\max}\)。因为 \(A,B\) 都是奇数，
[一般二进传输判据](type-I-general-dyadic-terminal-transfer.md)中的二进预算正好是
\(1\le J\le J_{\max}\)。因此正向只剩高度条件 \(A<2^uB\)，反向只剩高度条件
\(B<2^vA\)。

假设两者都失败，则

\[
A\ge2^uB,
\qquad
B\ge2^vA.
\]

相乘并消去正数 \(AB\)，得到 \(1\ge2^{u+v}>1\)，矛盾。故至少一个方向同时满足
同余、预算和严格高度条件，并由一般二进传输产生合法偶终端。这证明 (1)，取逆否命题
即得 (2)。证毕。

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

若任一方向同时满足高度不等式，就得到双向广义二进终端。上面的全称二分已经证明，
双向未决状态必有共同的必要缺口：

\[
o_R(2)>J_{\max}.
\]

这并不意味着没有预算内同余类：当 \(|\lambda_2|\) 在阶 \(o_R(2)\) 下有小的剩余时，
仍可能有一个 \(J\le J_{\max}\)，但其对应的高度方向不等式失败。

## 精确冻结复现

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_imbalance_order_budget.py
~~~

输入哈希锁定为
83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f。结果：

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

定理把剩余二进分支从“某个 \(J\) 还没试到”改写为一个可计算的阶—预算缺口；冻结
复现则记录这个缺口在当前完整线性谱中的实际分布。在循环商上，
\(\operatorname{ord}_R(2)\) 给出规范角色阶，而 \(J_{\max}\) 给出有限指数盒的二进
预算；因此它可以直接作为 Fourier/关系格证书的输入，并与跨状态 \(q\)-进容量比较。

边界仍然明确：式 (2) 只是双向未决的必要条件，不是充分条件；即使
\(o_R(2)>J_{\max}\)，某个方向仍可能有预算内代表并满足高度条件。阶—预算缺口只排除
当前二进传输族，不能推出 \(-1\notin\mathcal C_R(K)\)，也不能替代目标平方除子、
普通 Type II 或跨状态下降。
