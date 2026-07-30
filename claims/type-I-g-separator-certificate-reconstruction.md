---
kind: claim
claim_id: type-I-g-separator-certificate-reconstruction
title: 冻结 G 状态的规范有限群分离证书重建
statement: 对七个冻结线性目标谱中的 190 个 G 型状态，重建单位群支撑子群的 HNF 对偶格，并在规范系数盒 {-1,0,1}^d 中找到一个角色：它在 K 的每个素因子生成元上恒等、在 -1 上非恒等。逐项验证 CRT 分量阶、生成元相位和目标相位，故 190 个状态均有可独立复核的精确 G 证书；这是有限计算重建，不是跨状态容量矛盾或全称选择器定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- G-state
- finite-fourier
- subgroup-character
- separator
- hermite-normal-form
- certificate
- reproducibility
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 冻结 G 状态的规范有限群分离证书重建

## 证书定义

设

\[
G=(\mathbb Z/R\mathbb Z)^\times,
\qquad
H=\langle q:q\mid K\rangle,
\qquad
-1\notin H.
\]

按 CRT 把 (G) 写成循环分量，令第 (j) 个分量的阶为 (n_j)，并用该分量的原根
记录每个 (q\mid K) 的离散对数向量 (g_q)。把所有 (g_q) 与阶向量
(n_je_j) 生成的整数格写成列 HNF 矩阵 (M)。若

\[
y=M^{-T}c,
\qquad c\in\mathbb Z^d,
\]

并且 (n_jy_j\in\mathbb Z)，则 (y) 定义一个 (G) 上的角色

\[
\chi_y(x)=\exp\left(2\pi i\sum_jy_j\ell_j(x)\right),
\]

其中 (ell_j(x)) 是 (x) 在第 (j) 个 CRT 分量的离散对数。若对所有生成元有

\[
\sum_jy_j\ell_j(q)\in\mathbb Z,
\]

而

\[
\sum_jy_j\ell_j(-1)\notin\mathbb Z,
\]

则 (chi_y) 是精确的 G 型支撑外分离证书。

脚本按

\[
c\in\{-1,0,1\}^d
\]

枚举，并按 ((\|c\|_1,\lvert\operatorname{supp}c\rvert,c)) 选择规范的最小候选；所有相位条件使用有理数精确验证。

## 冻结重建结果

输入是七个冻结线性目标谱中的 190 个 G 型状态。每个状态重新计算
(K=(pR+1)/4)、素因子分解、CRT 离散对数和支撑格 HNF，再验证角色在所有生成元上恒等而在
(-1) 上非恒等。190 个状态全部在 ({-1,0,1}^d) 盒内找到证书。

规范候选的角色阶分布为：

\[
\begin{array}{c|rrr}
\text{角色阶}&2&4&6\\ \hline
\text{状态数}&185&2&3
\end{array}
\]

非平凡 CRT 分量数分布为

\[
\begin{array}{c|rrrrr}
\text{活跃分量数}&1&2&3&4&5\\ \hline
\text{状态数}&89&75&24&1&1.
\end{array}
\]

角色阶这里指规范 HNF 对偶候选的实际阶，不是此前“最小二幂分离角色阶”普查中的指标；因此
出现阶 (6) 不与高阶 G 型普查的二幂阶 (2,4,8) 分类矛盾。完整证书载荷和输入哈希见
`reproductions/type-i-g-separator-certificate-results.json`。

## 逻辑边界

有限阿贝尔群对偶性本身保证 G 型存在某个分离角色；本页新增的是在冻结输入上把该角色
规范化为小 HNF 对偶系数并逐项重建。它没有证明：

- 所有核心素数的 G 状态都存在同样有界的对偶系数；
- 不同状态的角色具有共同素因子、颜色或可比较相位支撑；
- 190 张证书的 (q)-进需求超过标签差/模数差容量；
- 因而它尚未给出跨状态容量矛盾或 Type I/II 全称选择器。

## 复现

~~~bash
python3 reproductions/type_i_g_separator_certificate.py
~~~
