---
kind: claim
claim_id: type-I-linear-block-square-terminal-boundary
title: 双向未决线性状态的较小块平方终端边界
statement: 对线性状态 U=sR+1、V=aR+1、UV=4K 且 U 为偶数，令 X=min(U,V)。若 U≠V 且不是 U<V、V 奇数的混合奇偶障碍，则 E=X^2 满足 E|4K^2、E≡1 modR，并给出严格更小源；源偶时为偶终端，源奇时为带标记奇源递降。对 11673 个双向二进未决状态，4186 个为偶终端、2963 个为奇标记下降、4524 个为精确平方整除障碍。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-normal-ratio-two-nondegenerate-terminal-or-descent
  - type-I-linear-block-imbalance-bidirectional-dyadic
topics:
- type-I
- linear-source
- block-square
- even-terminal
- marked-descent
- parity
- finite-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 双向未决线性状态的较小块平方终端边界

## 算术分流

在线性状态中

\[
U=sR+1,\qquad V=aR+1,\qquad UV=4K,
\]

有 \(U\) 偶数且 \(U\equiv V\equiv1\pmod R\)。设 \(U\ne V\)，并令

\[
X=\min(U,V),\qquad Y=\max(U,V),\qquad E=X^2.
\]

因为

\[
4K^2=\frac{U^2V^2}{4},
\]

若 \(X=V<U\)，则 \(E\mid4K^2\) 自动成立，因为 \(U\) 偶；若
\(X=U<V\)，则 \(E\mid4K^2\) 当且仅当 \(V\) 为偶数。因此该平方机制的唯一失败情形是

\[
U<V\quad\text{且}\quad V\ \text{为奇数}. \tag{1}
\]

在非失败情形中，

\[
E\equiv1\pmod R,\qquad
n=\frac{4K-E}{R}=\frac{UV-X^2}{R}
\]

是正整数。由于 \(E>1\) 且 \(4K=pR+1\)，有 \(n<p\)。又 \(E\mid4K^2\)、
\((E,R)=1\)，从

\[
nR=4K-E
\]

可得 \(E\mid nK\)。最后

\[
n\equiv E\pmod2
\]

因为 \(R\) 为奇数。因此：

- \(E\) 偶时，\(n\) 是严格更小的偶终端；
- \(E\) 奇时，\((n,E)\) 是严格更小的奇源带标记递降边，适用[非退化终端或标记下降二分](type-I-normal-ratio-two-nondegenerate-terminal-or-descent.md)；
- 条件 (1) 只说明这个“较小块平方”机制失败，不排除其它 \(2^J\)、关系格或 Type I/II 证书。

## 双向未决分支审计

复现脚本：

~~~text
python3 reproductions/type_i_linear_block_square_boundary.py
~~~

输入为双向二进审计结果，哈希锁定为
\`83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f\`。对全部 11673 个双向未决状态得到：

~~~text
record_count: 11673
even_terminal: 4186
odd_marked_descent: 2963
mixed_parity_square_obstruction: 4524
~~~

三类各自都覆盖 200 个冻结样本素数。这里的“奇源标记下降”保留了线性状态的提升标记，
不是普通 Erdős–Straus 归纳假设下的无标记解提升。

## 研究含义

双向 \(2^J\) 传输和较小块平方分流后，线性完整谱的局部缺口可压缩为：

\[
\text{目标命中/Type II}
\quad\lor\quad
\text{偶终端}
\quad\lor\quad
\text{标记奇源}
\quad\lor\quad
\text{混合奇偶平方障碍}.
\]

线性源已有平凡终端 \(E=U=sR+1\)，因此这里的较小块平方分流不是终端存在性的首次证明；
它的价值在于把双向 \(2^J\) 未决状态按可复用的非平凡终端形状和精确平方障碍分组。
下一步若要形成全称选择器，应优先研究 4524 个平方障碍状态的共同标签/模数差和
Fourier 载体；继续枚举同一较小块平方不会再提供新信息。
