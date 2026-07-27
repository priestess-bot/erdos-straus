---
kind: claim
claim_id: type-II-moving-window-finite-collision-reduction
title: 直接 Type II 移动窗口的有限碰撞状态分解
statement: 对固定窗口 j=1,...,J 和核心素数 p>4J，令 x_j=(p+4j-1)/4。任意 j!=k 有 gcd(x_j,x_k)|j-k；删去所有整除某个窗口差 j-k 的有限素数后，x_j 的私有余因子两两互素。每个 x_j^2 的 Type II 除子残数集精确分解为碰撞部分与私有部分的乘积集，且窗口失败当且仅当私有残数集避开碰撞部分诱导的有限目标集。对 p=153633769、J=31 的实际共同失败窗口逐项验证了该分解。
claim_status: established
topics:
- type-II
- moving-window
- multishift
- divisor-residues
- factorization
- finite-abelian-groups
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework; Theorem C"
  role: product-set-language
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 直接 Type II 移动窗口的有限碰撞状态分解

## 连续首分母参数

固定 \(J\ge2\)，取核心素数 \(p>4J\)，并令

\[
m_j=4j-1,\qquad x_j=\frac{p+m_j}{4}\qquad(1\le j\le J). \tag{1}
\]

因为 \(p\equiv1\pmod {24}\)，这些 \(x_j\) 是连续整数：

\[
x_j-x_k=j-k. \tag{2}
\]

因此

\[
\gcd(x_j,x_k)\mid j-k\qquad(j\ne k). \tag{3}
\]

令 \(\mathcal P_J\) 为所有 \(1\le |j-k|<J\) 的素因子集合。把 \(x_j\) 的
\(\mathcal P_J\)-部分记为 \(E_j\)，其余部分记为 \(R_j\)。由 (3)，

\[
\gcd(R_j,R_k)=1\qquad(j\ne k). \tag{4}
\]

又因 \(m_j<p\)，若素数同时整除 \(x_j\) 与 \(m_j\)，它整除
\(4x_j-m_j=p\)，矛盾；故 \(x_j\) 的全部素因子都是
\((\mathbb Z/m_j\mathbb Z)^\times\) 的单位。

## 残数状态分解

记 \(\Pi_m(n)\) 为 \(n\) 的全部除子模 \(m\) 的残数集。由因子分解，

\[
\Pi_{m_j}(x_j^2)=
\Pi_{m_j}(E_j^2)\,\Pi_{m_j}(R_j^2). \tag{5}
\]

Type II 在位置 \(j\) 失败当且仅当

\[
-x_j\notin\Pi_{m_j}(x_j^2). \tag{6}
\]

因此 (5)--(6) 等价于：对每个
\(e\in\Pi_{m_j}(E_j^2)\)，私有残数集避开有限目标

\[
-x_j e^{-1}\pmod {m_j}. \tag{7}
\]

碰撞部分 \(E_j\) 的素因子和指数状态只涉及有限集 \(\mathcal P_J\)，故对固定
窗口它是有限状态；(4) 则将所有未受控因子压为跨位置两两互素的私有余因子。

## 记录失败点的审计

移动窗口 \(J=27\) 在 \(p\le2\cdot10^8\) 的唯一遗漏为

\[
p=153633769.
\]

该点在 \(j=1,\ldots,31\) 全部失败，首个命中在 \(j=32\)。对前 31 个位置，

\[
\mathcal P_{31}=\{2,3,5,7,11,13,17,19,23,29\}.
\]

脚本逐项验证 (5)、(7) 和 (4)：31 个私有余因子两两互素，且没有一个私有残数集
触及相应的碰撞诱导目标。

运行：

    python3 reproductions/type_ii_moving_window_collision.py \
      --prime 153633769 --window 31 \
      --output reproductions/type-ii-moving-window-collision-p153633769-j31-results.json

会重建这个有限状态审计。

## 含义

这一定理不证明某个窗口位置必成功。它排除的是一个不精确的逃逸想象：
共同失败不能依赖无限复杂的跨窗口公共大因子。尚未解决的是，为什么这些由同一
\(p\) 产生、但两两互素的私有残数积集不能在每个位置持续避开 (7)。

因此下一步应研究 (7) 的跨模数兼容性、连续 \(x_j\) 的逐素因子分布，或能从某个
共同失败状态构造更小直接 Type II 实例的可提升约化。
