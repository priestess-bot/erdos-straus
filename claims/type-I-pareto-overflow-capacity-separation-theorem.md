---
kind: claim
claim_id: type-I-pareto-overflow-capacity-separation-theorem
title: Pareto 溢出需求的全局价格分离定理
statement: 对映入同一有限资源坐标系的一族有限 Pareto 需求集，存在总需求逐坐标不超过容量的凸组合选择，当且仅当每个共同非负价格向量下，各状态最低价格之和不超过容量价格。因而凸容量不可行当且仅当存在一个对所有状态统一的非负价格向量给出严格超载；逐状态另选权重不能构成容量证明。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-I-target-fiber-fourier-overflow-generating-function
  - type-I-cross-state-q-adic-capacity-bound
topics:
- type-I
- F-state
- Pareto
- overflow
- convex-duality
- capacity
- linear-programming
- proof-program
sources:
- claim: type-I-target-fiber-fourier-overflow-generating-function
  role: pareto-demand-interface
- claim: type-I-cross-state-q-adic-capacity-bound
  role: arithmetic-capacity-interface
visibility: public
last_checked: '2026-07-30'
---

# Pareto 溢出需求的全局价格分离定理

## 定理

设 \(\mathcal S\) 是有限非空状态集，\(Q\) 是有限的公共资源坐标集。对每个
\(s\in\mathcal S\)，令 \(D_s\subset\mathbb R_{\ge0}^{Q}\) 是非空有限需求集；在应用中，
\(D_s\) 应由该状态的局部需求经过一个**已经证明的共同资源映射**得到。若只映射原
盒外空间的 Pareto 极小点，还必须证明该映射保持逐坐标支配；否则应先映射全部可行
需求，再在资源空间重新取 Pareto 极小集。
给定容量 \(C\in\mathbb R_{\ge0}^{Q}\)，定义向上闭凸需求多面体

\[
P_s=\operatorname{conv}(D_s)+\mathbb R_{\ge0}^{Q}.
\tag{1}
\]

则下列两项等价：

1. 存在 \(x_s\in P_s\)，使 \(\sum_sx_s\le C\)（逐坐标）；
2. 对每个共同价格 \(w\in\mathbb R_{\ge0}^{Q}\)，都有

\[
\sum_{s\in\mathcal S}\min_{d\in D_s}w\mathbin{\cdot}d
\le w\mathbin{\cdot}C.
\tag{2}
\]

因此，凸容量模型不可行当且仅当存在一个非零
\(w\in\mathbb R_{\ge0}^{Q}\) 使

\[
\boxed{
\sum_{s\in\mathcal S}\min_{d\in D_s}w\mathbin{\cdot}d
>w\mathbin{\cdot}C.}
\tag{3}
\]

这个 \(w\) 是整个状态族共享的容量价格证书。

## 证明

令 \(P=\sum_{s\in\mathcal S}P_s\) 为 Minkowski 和。它是闭凸多面体，并满足
\(P+\mathbb R_{\ge0}^{Q}=P\)。若存在 \(x_s\in P_s\) 且
\(\sum_sx_s\le C\)，则

\[
C=\sum_sx_s+\left(C-\sum_sx_s\right)\in P.
\]

反之，\(C\in P\) 直接给出 \(C=\sum_sx_s\) 的可行分解。因此凸容量可行当且仅当
\(C\in P\)。

若 \(C\notin P\)，闭凸集的严格分离定理给出一个非零线性泛函 \(w\)，满足

\[
\inf_{x\in P}w\mathbin{\cdot}x>w\mathbin{\cdot}C.
\tag{4}
\]

因为 \(P\) 在每个正坐标方向上无界，(4) 中的 \(w\) 不可能有负坐标，否则左端为
\(-\infty\)。故 \(w\ge0\)。对非负 \(w\)，有

\[
\begin{aligned}
\inf_{x\in P}w\mathbin{\cdot}x
&=\sum_s\inf_{x_s\in P_s}w\mathbin{\cdot}x_s\\
&=\sum_s\min_{d\in D_s}w\mathbin{\cdot}d,
\end{aligned}
\]

于是 (4) 正是 (3)。反方向更直接：若存在可行的 \(x_s\)，则对任意 \(w\ge0\)，

\[
\sum_s\min_{d\in D_s}w\mathbin{\cdot}d
\le\sum_sw\mathbin{\cdot}x_s
\le w\mathbin{\cdot}C,
\]

排除 (3)。证毕。

## 不能逐状态选择价格

目标纤维生成函数允许对单个状态计算任意权下的
\(\Omega_w(s)=\min_{d\in D_s}w\cdot d\)。但容量矛盾要求 (3) 中同一个 \(w\) 同时为
所有状态和容量定价。若每个状态分别挑选最有利的 \(w_s\)，这些标量最低价一般不能
相加，也不是任何线性容量模型的对偶证书。

这给出了搜索策略的严格约束：应联合求解一个全局价格向量，或直接求解 (1) 的有限
线性规划；不应把各状态的单位权最小值或各自最优权简单求和。

## 整数边界与当前缺口

本定理精确刻画的是凸化后的选择问题。若每个状态必须选取 \(D_s\) 中一个整数需求，
则 (3) 仍是整数不可行的充分证书，但不存在这样的线性价格并不保证整数可行；剩余障碍
可能来自整数性或组合冲突，需要整数规划、流的全幺模结构或单独的舍入论证。

对当前 Erdos--Straus 统一选择器，还必须补上以下算术输入：

1. 把每个局部盒外向量映到同一组实际资源坐标，而不是给不同状态使用不同载体；
2. 证明该映射保持支配关系，或在映射全部需求后重新计算资源空间 Pareto 前沿；
3. 证明映射后的每一层确实消耗标签差、模数差或块因子的 \(q\)-进高度；
4. 从嵌套同余链等结构得到有效容量 \(C\)，并控制重复标签和多中心分组。

在这些输入建立后，(3) 才能把 Pareto 边界升级为全局超载证明；在此之前，它是精确的
对偶接口而不是猜想本身的容量结论。
