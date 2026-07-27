---
kind: claim
claim_id: type-I-moving-window-adaptive-conditional-escape
title: Type I 自适应一私有因子逃逸可达二十三窗口但在九十五缺口闭合
statement: 在 Dickson 素数元组猜想或相应 Schinzel 假设下，存在无穷多个核心素数 p，使其在前23个移动缺口 \(m=3,7,\ldots,91\) 都没有 Type I 证书。该条件逃逸由 seed 709921 的自适应一私有素因子状态精确构造；加入下一个缺口 m=95 后，全部95个新增残数类的完整模型平方除子积集均命中 \(-1/4\bmod95\)。逃逸和闭合均限于该状态模型，不是固定窗口的一般定理。
claim_status: conditional
topics:
- type-I
- moving-window
- conditional-escape
- adaptive-state
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 自适应一私有因子逃逸可达二十三窗口但在九十五缺口闭合

## 条件逃逸链

从 \(p=709921\) 的前八窗口失败残数出发，先构造局部可采纳的一私有素因子状态，再依次
加入

\[
m=35,39,43,\ldots,91. \tag{1}
\]

每步完整枚举新缺口的所有残数类，选择首个同时满足以下两项的分支：

\[
x_j(k)=E_jL_j(k),\qquad
-\frac14\notin\Pi_{4j-1}(E_j^2L_j(k)^2). \tag{2}
\]

并对全部 \(p,L_1,\ldots,L_j\) 的仿射形式做有限局部可采纳性检查。到第 23 个位置时，
共有 24 个两两不同、局部可采纳的原始仿射形式；所以在 Dickson 或 Schinzel 假设下，
无穷多个参数同时令这些形式为素数。对充分大的这些参数，所得核心素数在

\[
m=3,7,\ldots,91 \tag{3}
\]

全部没有 Type I 证书。

这说明“有限 Type I 移动窗口必覆盖”的论证不能只靠固定前八个缺口，也不能由小范围
计算的最大首缺口直接外推。

## 九十五缺口的状态闭合

对该第 23 窗口状态，逐一细分新缺口 \(m=95\) 的全部 95 个参数残数类。每一类都有

\[
E=1032=2^3\cdot3\cdot43,\qquad L\equiv77\pmod{95},\qquad
-\frac14\equiv71\pmod{95}. \tag{4}
\]

完整平方除子积集都命中目标；例如

\[
774\,L^2\equiv71\pmod{95},\qquad 774\mid E^2. \tag{5}
\]

因此 \(m=95\) 的全部 95 个分支都出现 Type I 证书。闭合并非单个固定除子造成，而是
固定碰撞因子 \(E\) 和新增私有素因子被强制的残数 \(L\bmod95\) 的联合结果。

## 意义

该链同时给出两条研究约束：

1. 固定有限窗口不能替代动态因子选择器，因为条件逃逸可以跨越至少 23 个位置。
2. 逃逸状态也不能被当作自由参数；增加新缺口会更新固定碰撞因子和私有残数，并可能像
   (5) 一样强制闭合。

因此更有希望的命题是对状态转换的分类或势函数：证明每个可采纳的一私有因子逃逸状态，
在有限但随状态可计算的窗口增长后都触发一个类似 (5) 的目标命中，或者证明任何无限
逃逸都必须引入超出一私有素因子模型的新因子复杂度。

## 边界

这是条件性模型结果，不是 Erdős--Straus 猜想的反例或证明。它没有排除其它残数起点、
多私有素因子状态、非仿射因子，或更大的窗口继续逃逸；也不能从一个状态在 \(m=95\)
闭合推出所有状态都在同一缺口闭合。

## 重建

    python3 reproductions/type_i_moving_window_adaptive_escape.py
    python3 -m unittest tests/test_type_i_moving_window_adaptive_escape.py -q
