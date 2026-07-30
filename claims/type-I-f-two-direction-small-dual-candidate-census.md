---
kind: claim
claim_id: type-I-f-two-direction-small-dual-candidate-census
title: F 型小对偶双方向需求的跨状态容量边界
statement: 在冻结的 45 个 F 型关系格状态上穷举所有 {-1,0,1}^r 对偶系数，保留目标相位非整数且至少两个活跃坐标的前两方向，并按核心素数、方向对、载体颜色和目标相位需求分组。共 15876 个候选、195 个需求键，只有两键跨两个状态重复；其精确双载体除子容量分别为 2 和 16，均不小于重复需求 2。因此该冻结样本不支持仅靠小对偶二维相位键产生容量超载；这是一条排除性有限边界，不是全称负面定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- finite-fourier
- two-active
- small-dual
- colored-capacity
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# F 型小对偶双方向需求的跨状态容量边界

## 审计规则

对每个冻结 F 状态，取关系格 \(\Lambda\) 的对偶向量

\[
y=\Lambda^{-*}c,
\qquad c\in\{-1,0,1\}^r,
\]

保留目标相位 \(\langle y,z_0\rangle\notin\mathbb Z\) 且活跃支撑至少为二的候选。对前两个活跃素数
\(q_1,q_2\)，分别在 \(U=sR+1,V=aR+1\) 中选择 \(q_i\)-进高度较大的载体块，平手时取
\(s\) 块。需求键规范化为

\[
\bigl(p,q_1,q_2,(t_1,t_2),\tau_I\bigr),
\]

其中 \((t_1,t_2)\) 是颜色对，\(\tau_I\) 是目标相位投影的二维需求残值。固定键后，使用
精确除子集合

\[
q_1q_2d\mid p-t,
\qquad
q_1q_2d=tR+1
\]

枚举全部可行 \(R\)，作为该键的载体容量；不使用独立颜色容量相乘的粗估计。

## 冻结结果

四个对抗核心的 45 个 F 状态共产生

\[
15{,}876\text{ 个小对偶候选},
\qquad
195\text{ 个精确需求键}.
\]

跨不同状态重复的需求键只有两组：

\[
\begin{array}{c|c|c|c|c|c}
p&(q_1,q_2)&(t_1,t_2)&\tau_I&\text{状态数}&\text{容量}\\
\hline
26034649&(379,941)&(a,a)&1/2&2&2\\
57399241&(5,71)&(s,s)&1/2&2&16
\end{array}
\]

两组的高度优先联合需求均为 2，分别达到容量 2 和容量 16；没有一组发生超载。完整
候选计数、重复状态和精确 \(R\) 容量见
`reproductions/type-i-f-two-direction-small-dual-candidate-census-results.json`。

## 研究含义

这排除了一个过于直接的方案：先从每个 F 状态任取小 HNF 对偶向量，再只按二维方向、
颜色和目标相位做 \(q\)-进装箱，就期待自动得到跨状态矛盾。当前样本中重复需求太少，且
容量仍有余量。

下一步必须至少加入一种额外载荷：

1. Fourier 幅度或固定层谱余量，把同一需求键的状态赋予不同的相位质量；
2. 目标纤维稀疏度/投影空缺，把非空键也转成严格需求；
3. 源距离、模数窗口或可提升终端的良基势函数；
4. 多方向联合相位，而不是只取前两个坐标。

本页不声称小对偶候选的所有选择都已统一规范化，也不声称容量未超载可以推广到所有
核心素数；它只是当前冻结样本上的负面边界。

## 复现

~~~bash
python3 reproductions/type_i_f_two_direction_small_dual_candidate_census.py
~~~
