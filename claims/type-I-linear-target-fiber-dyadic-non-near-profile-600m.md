---
kind: claim
claim_id: type-I-linear-target-fiber-dyadic-non-near-profile-600m
title: 非近邻目标纤维的比值二终端边界
statement: 在冻结的 1,018 个线性 hit 状态中，目标纤维审计得到的 226 个非近邻状态全部存在互素除子 a,b|2K，满足 a=2b (mod R)、a<2b，并由 E=2K a/b 产生合法偶终端；因此该有限边界的最小广义二进指数 j 全部为 1。这是有限证据，不是普适终端选择定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- target-fiber
- dyadic
- ratio-terminal
- non-near
- even-terminal
- finite-exponent
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 非近邻目标纤维的比值二终端边界

## 审计对象

目标纤维近邻审计中的 226 个非近邻 hit 状态满足
\(\operatorname{exc}_{\min}>0\)。对每个状态令 \(L=2K\)，穷举所有互素除子
\(a,b\mid L\) 及全部二进预算合法的 \(j\)，检查

\[
a\equiv2^j b\pmod R,
\qquad
a<2^j b.
\]

对每个通过同余和方向条件的候选，独立验证一般二进终端判据：

\[
E_j=2^{1-j}L\frac ab,
\qquad
E_j\mid L^2,
\qquad
E_j\equiv1\pmod R,
\qquad
n=\frac{2L-E_j}{R}\in2\mathbb Z,\quad 0<n<p.
\]

## 冻结结果

226 个非近邻状态全部找到合法终端，且最小 \(j\) 的分布为

\[
\begin{array}{c|c}
\text{最小 }j&\text{状态数}\\ \hline
1&226
\end{array}
\]

也就是说，在这组有限边界中，广义 \(2^j\) 搜索没有产生 \(j>1\) 的新增需求；
普通比值二已经足够，但这里的 \(a,b\) 不必来自同一目标纤维近邻对。

## 研究含义

该结果区分了两个不同的充分机制：

1. **目标纤维近邻机制**：两个目标表示之比产生终端，并把目标命中与终端绑定；
2. **独立比值二机制**：任意 \(a,b\mid2K\) 的有限群碰撞产生终端，不要求 \(a,b\)
   来自目标纤维。

因此 226 个非近邻状态不是终端反例，而是说明“目标纤维近邻”并非终端存在性的必要
条件。下一步真正需要证明的是：对每个普通 Type II 遗漏，能否找到某个合法状态使
目标命中，或直接产生这种独立比值碰撞；当前审计尚未提供从一个遗漏到该状态的全称
选择映射。

## 证据边界

该结果只覆盖冻结的 200 点完整线性谱中的 hit 状态，不能推出所有核心素数、所有
非线性 Type I 状态或所有 \(j>1\) 状态均有终端。

## 复现

~~~bash
python3 reproductions/type_i_linear_target_fiber_dyadic_non_near_profile_600m.py
~~~

结果文件：
[type-i-linear-target-fiber-dyadic-non-near-profile-600m-results.json](../reproductions/type-i-linear-target-fiber-dyadic-non-near-profile-600m-results.json)
