---
kind: claim
claim_id: type-I-linear-target-fiber-neighbor-profile-600m
title: 冻结线性完整谱的目标纤维近邻边界
statement: 在 200 个核心素数的完整线性谱中，1,018 个 hit 状态的目标纤维均可由 K^2 的目标除子精确重建；其中 792 个状态存在逐坐标预算内的目标表示近邻并通过 E=4K rho 产生偶终端，226 个状态没有该近邻。最小坐标预算超额分布为 -1:6、0:786、1:150、2:51、3:14、4:7、5:3、8:1。这是冻结有限谱的近邻分支边界，不是全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- target-fiber
- near-pair
- even-terminal
- finite-exponent
- complete-spectrum
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-spectrum-context
visibility: public
last_checked: '2026-07-29'
---

# 冻结线性完整谱的目标纤维近邻边界

## 审计对象

输入是 200 个一般 \(B\) 首次命中需要 \(B>1\) 的核心素数及其完整线性状态谱。
对每个分类为 hit 的状态 \((R,K)\)，逐一枚举

\[
d\mid K^2,\qquad d\equiv-K\pmod R,
\]

并将每个目标除子写成

\[
d=K\prod_iq_i^{z_i},
\qquad -\nu_i\le z_i\le\nu_i.
\]

对目标指数纤维中的每一对 \(z,w\)，定义坐标预算超额

\[
\operatorname{exc}(z,w)
=
\max_i\bigl(|z_i-w_i|-\nu_i\bigr).
\]

\(\operatorname{exc}(z,w)\le0\) 正是近邻终端引理所需的逐坐标条件。

## 冻结结果

完整谱共有 1,018 个 hit 状态。其中：

\[
\begin{array}{c|cc}
\text{类别}&\text{状态数}&\text{比例}\\ \hline
\text{存在近邻对}&792&77.7996\%\\
\text{不存在近邻对}&226&22.2004\%
\end{array}
\]

每个状态的最小超额分布为

\[
\begin{array}{c|rrrrrrrr}
\operatorname{exc}_{\min}&-1&0&1&2&3&4&5&8\\ \hline
\text{状态数}&6&786&150&51&14&7&3&1
\end{array}
\]

所有 792 个近邻状态都通过独立整数检查生成

\[
E=4K\prod_iq_i^{z_i-w_i},
\qquad
n=\frac{4K-E}{R},
\]

并验证 \(E\mid4K^2\)、\(E\equiv1\pmod R\)、\(E\le4K-4R\) 及
\(0<n<p\)。审计中生成的终端 \(n\) 范围为
\(67368\le n\le597694400\)。

## 研究含义

这项结果确认近邻分支不是稀有现象：在当前冻结 hit 压力谱中约四分之三的状态可由
目标表示重数直接闭合为偶终端。但 226 个状态的近邻缺失也排除了“所有 hit 自动有
近邻对”的状态内强命题；其中最近对的最大超额为 8，说明下一步应优先研究小超额
\(1\le\operatorname{exc}_{\min}\le8\) 的关系格或 \(2^j\) 传输，而不是把近邻引理误作
全称证明。

该审计只覆盖已命中的 200 点完整线性谱，不能推出每个普通 Type II 遗漏都存在目标
命中状态，也不能推出 226 个边界状态没有其他偶终端。

## 复现

~~~bash
python3 reproductions/type_i_linear_target_fiber_neighbor_profile_600m.py
~~~

结果文件：
[type-i-linear-target-fiber-neighbor-profile-600m-results.json](../reproductions/type-i-linear-target-fiber-neighbor-profile-600m-results.json)
