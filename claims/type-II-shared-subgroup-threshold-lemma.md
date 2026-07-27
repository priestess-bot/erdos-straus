---
kind: claim
claim_id: type-II-shared-subgroup-threshold-lemma
title: 共享 Type II 选择器的生成子群阈值引理及零覆盖边界
statement: 设 p=1 mod24，m=3 mod4 为一个已有 Type II 证书的合法缺口；令 H 为 p+m 中所有与 m 互素的素因子残数生成的 U(m) 子群，按重数记这些素因子为 t 个。若 t>=|H|，则存在非平凡 D|p+m 且 D=1 modm，故该缺口满足共享 Type II 选择器条件。这是 phi(m) 阈值的强化。对 p<=10^7 的 84 个四自动缺口后且无 k=1 选择器的压力点，完整 m<=239 扫描中该强化条件仍命中为零。
claim_status: established
topics:
- type-II
- shared-divisor
- factorization
- finite-abelian-groups
- subgroup-structure
- divisor-residues
- product-sets
- computation
- obstruction
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework"
  role: finite-group-product-set-context
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器的生成子群阈值引理及零覆盖边界

## 命题

在一个已有 Type II 证书的合法缺口 \(m\) 上，取 \(p+m\) 中所有与 \(m\) 互素的
素因子并按重数列为 \(q_1,\ldots,q_t\)。令

\[
H=\langle q_1\bmod m,\ldots,q_t\bmod m\rangle
\le(\mathbb Z/m\mathbb Z)^\times. \tag{1}
\]

若

\[
t\ge |H|, \tag{2}
\]

则存在非平凡除子

\[
D\mid p+m,\qquad D\equiv1\pmod m. \tag{3}
\]

配合该缺口的 Type II 证书，(3) 满足
`type-II-shared-residue-selector-conjecture` 的共享因子条件。

## 证明

全部前缀积

\[
P_0=1,\qquad P_j=q_1\cdots q_j\bmod m\quad(1\le j\le t)
\]

都位于 \(H\)。由 (2)，这 \(t+1\) 个前缀多于 \(H\) 的元素数；故有
\(P_i=P_j\)（\(i<j\)）。子积

\[
D=q_{i+1}\cdots q_j
\]

非平凡、整除 \(p+m\)，且 \(D\equiv P_jP_i^{-1}\equiv1\pmod m\)。证毕。

因为 \(|H|\le\varphi(m)\)，它严格强化
`type-II-shared-totient-threshold-lemma` 的阈值。它仍只是充分条件：短零积可能在
\(t<|H|\) 时已经出现。

## 精确边界

对四自动缺口后的 84 个无 \(k=1\) 压力点，脚本扫描全部有 Type II 证书的

\[
3\le m\le239,\qquad m\equiv3\pmod4,
\]

计算 (1)，再检验 (2) 并重建相应 \(D\)。结果是

\[
\#\{\text{生成子群阈值命中}\}=0,\qquad
\#\{\text{未命中压力点}\}=84. \tag{4}
\]

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 10000000 --gap-cap 239 --subgroup-threshold-profile \
      --output reproductions/type-ii-automatic-residual-subgroup-threshold-profile-10m-results.json

会重建 (4)。

## 对下一步的约束

(4) 排除了“单位因子数大于其实际生成子群规模”这一自然的稳定子群型充分条件。
但实际共享证书常由远短于 \(|H|\) 的零积子序列给出。故下一步不能再只比较长度和
群阶，而应研究短零积的逆结构，或用多个可选缺口 \(p+m\) 的固定差值关系排除这些
短零积避靶状态的共同实现。
