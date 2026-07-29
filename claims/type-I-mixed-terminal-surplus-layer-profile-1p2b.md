---
kind: claim
claim_id: type-I-mixed-terminal-surplus-layer-profile-1p2b
title: 五亿至十二亿首选偶桥的平方剩余层边界
statement: 在500000000<p<=1200000000的七段连续审计中，1649条已存首个偶源 Type I 最大尾桥按 S=E/gcd(E,4K) 分类：63条S=1，359条为单素数幂，1227条含至少两个不同素因子；支持数分布为0:63、1:359、2:614、3:444、4:149、5:19、6:1。该结果否定把E|4K或单素数幂剩余作为全称充分机制，但因为每点只保留首个桥，不排除同一素数存在更简单的未选桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- terminal-bridge
- square-budget
- surplus-layer
- factorization
- mixed-selector
- finite-audit
- counterexample-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-bridge-context
visibility: public
last_checked: '2026-07-29'
---

# 五亿至十二亿首选偶桥的平方剩余层边界

## 定义

对每条已验证的 Type I 最大尾偶源桥，设其正规形参数为

\[
p=4ABC-m,\qquad mR=4B^2C+1,\qquad K=BC(AR-B),
\]

桥因子满足 \(E\mid4K^2\)。定义平方预算之外的剩余层

\[
S=\frac{E}{\gcd(E,4K)}.
\]

\(S=1\) 正好是较强的线性条件 \(E\mid4K\)；\(S=q^r\) 表示只需要一个素数的额外
平方指数；多个不同素因子则表示真正的多素因子平方预算。

## 七段连续数据

对 (500\text{M}<p\le1.2\text{B}) 的七个已归档区间，程序读取每点保存的首个偶桥，
重新计算 \(R,K,E,S\)，并逐条验证桥的同余、偶性和平方整除条件。总计 1,649 条记录：

\[
\begin{array}{c|r}
\text{剩余层类型}&\text{数量}\\ \hline
S=1&63\\
\text{单素数幂}&359\\
\text{至少两个不同素因子}&1{,}227\\ \hline
\text{合计}&1{,}649
\end{array}
\]

按不同素因子个数的完整分布为

\[
\begin{array}{c|rrrrrrr}
\#\operatorname{supp}(S)&0&1&2&3&4&5&6\\
\hline
\text{数量}&63&359&614&444&149&19&1
\end{array}
\]

在 359 条单素数幂记录中，指数分布为

\[
1:319,\qquad 2:35,\qquad 3:4,\qquad 6:1.
\]

## 研究含义

这个边界排除了两条看似自然但过强的证明路线：

1. 试图把所有终端桥压到 \(E\mid4K\)；
2. 只允许在线性层之外增加一个素数幂。

在当前首选记录中，约 74.4% 的桥需要至少两个不同素因子的额外指数层。因此后续理论
必须处理 \(L=2K\) 的普通除子比值积集，或处理多素因子平方层的联合残数增长；只研究单一
素数的补偿无法覆盖现有数据。

## 证据边界

程序只读取每个素数的**首个**偶桥。一个素数可能还有未被首选策略保存的更简单桥，故该
剖面是证明路线的负边界而不是“所有桥都复杂”的定理。它也不产生混合终端选择引理的
反例，因为所有 1,649 个点仍已在有限 (m\le215) 盒内闭合。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_surplus_layer_profile_1p2b.py
python3 -m unittest tests/test_type_i_mixed_terminal_surplus_layer_profile_1p2b.py -q
~~~

结果文件：
[type-i-mixed-terminal-surplus-layer-profile-1p2b-results.json](../reproductions/type-i-mixed-terminal-surplus-layer-profile-1p2b-results.json)
