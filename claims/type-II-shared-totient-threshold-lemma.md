---
kind: claim
claim_id: type-II-shared-totient-threshold-lemma
title: 共享 Type II 选择器的单位因子总数充分引理及零覆盖边界
statement: 设 p=1 mod24，m=3 mod4 为一个已有 Type II 证书的合法缺口。若 p+m 中与 m 互素的素因子按重数至少有 phi(m) 个，则存在非平凡 D|p+m 且 D=1 modm，故该缺口满足共享 Type II 选择器条件。这由单位群中的前缀积抽屉原理给出。对 p<=10^7 的 84 个四自动缺口后且无 k=1 选择器的压力点，完整 m<=239 扫描中该充分条件命中数为零。
claim_status: established
topics:
- type-II
- shared-divisor
- factorization
- finite-abelian-groups
- divisor-residues
- product-sets
- computation
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器的单位因子总数充分引理及零覆盖边界

## 命题

设 \(p\equiv1\pmod {24}\)，并令

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,\qquad x=\frac{p+m}{4}.
\]

假设该 \(m\) 已满足 Type II 除子条件

\[
-x\in\Pi_m(x^2). \tag{1}
\]

把 \(p+m\) 中所有不整除 \(m\) 的素因子按重数列成

\[
q_1,\ldots,q_t,\qquad \gcd(q_i,m)=1.
\]

若

\[
t\ge\varphi(m), \tag{2}
\]

则存在 \(D>1\) 满足

\[
D\mid p+m,\qquad D\equiv1\pmod m. \tag{3}
\]

因而 (1) 与 (3) 同时成立，该缺口满足
`type-II-shared-residue-selector-conjecture` 的两项条件。

## 证明

在有限群 \(G=(\mathbb Z/m\mathbb Z)^\times\) 中考虑前缀积

\[
P_0=1,\qquad P_j=q_1\cdots q_j\bmod m\quad(1\le j\le t).
\]

群的大小为 \(\varphi(m)\)。由 (2)，有 \(t+1>\lvert G\rvert\)，所以两个前缀
\(P_i,P_j\)（\(0\le i<j\le t\)）相同。于是

\[
D=q_{i+1}\cdots q_j>1
\]

是 \(p+m\) 的除子且 \(D\equiv P_jP_i^{-1}\equiv1\pmod m\)。这给出 (3)。
(1) 已给出 Type II 证书，证毕。

注意这个引理只使用一个足够强的全局计数阈值；实际的子积集可能在远少于
\(\varphi(m)\) 个因子时已达到 \(1\)，所以 (2) 并非必要条件。

## 精确适用边界

脚本逐个扫描四自动缺口后的 84 个非 \(k=1\) 压力点、每个

\[
3\le m\le239,\qquad m\equiv3\pmod4,
\]

以及有 Type II 证书的缺口。每次先删去与 \(m\) 不互素的素因子，再检验 (2)，
并用前缀碰撞直接重建 (3)。

结果为：

\[
\#\{\text{满足 (1) 且 (2) 的压力点}\}=0,\qquad
\#\{\text{未由该阈值命中的压力点}\}=84. \tag{4}
\]

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 10000000 --gap-cap 239 --totient-threshold-profile \
      --output reproductions/type-ii-automatic-residual-totient-threshold-profile-10m-results.json

会重建 (4)。

## 含义

这个引理提供了一个完全无条件、可构造的共享因子充分条件，但 (4) 表明最粗的
因子总数阈值不足以处理当前最小压力集。正向工作不能仅证明
\(\Omega_{\mathrm{unit}}(p+m)\) 大；必须利用实际素因子残数的子集积增长、稳定子群
结构，或不同缺口 \(p+m\) 之间的关联。

它不构成 Erdős--Straus 猜想的证明，也不把共享标记表示当作无标记递降。
