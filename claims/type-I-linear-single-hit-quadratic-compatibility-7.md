---
kind: claim
claim_id: type-I-linear-single-hit-quadratic-compatibility-7
title: 七个单命中压力点的二次 G 跨状态相容审计
statement: 在完整线性谱中仅有一个一般B目标命中的七个压力点上，恢复185个二次子群/角色G状态和1个纯高阶G状态；对二次G状态之间的K值共享奇素因子逐项验证q整除abs(R-R')/4且Jacobi符号(mm'/q)=1，共1397条关系、涉及1132对模数。结果确认相容律但未产生跨状态矛盾，因此二次G相容性本身不足以证明混合终端选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- quadratic-character
- cross-state
- shared-factors
- single-hit
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 七个单命中压力点的二次 (G) 跨状态相容审计

## 审计对象

从 200 点完整谱压力层中选出目标谱恰有一个命中的七个核心素数：

\[
67369,\ 878089,\ 13782409,\ 26034649,\ 57399241,\ 152498329,\ 283319689.
\]

对每个线性状态

\[
K_R=\frac{pR+1}{4},
\]

若 (-1\notin\langle q:q\mid K_R\rangle)，程序计算精确的单位群证书，并保留最小二次
分离导子 (m\mid R)，满足 (m\equiv3\pmod4)。纯高阶分离状态单独计数，不强行套用二次公式。

对于两个不同模数 (R,R') 的二次 (G) 状态，程序枚举

\[
q\mid\gcd(K_R,K_{R'}),\qquad q\text{ 为奇素数},
\]

并逐项验证既有相容律

\[
q\mid\frac{|R-R'|}{4},
\qquad
\left(\frac{mm'}q\right)=1.
\]

第一式来自跨模数公因子刚性，第二式来自两个二次分离角色在共享素因子上的平凡性。

## 结果

| (p) | 二次 (G) 状态 | 高阶 (G) 状态 | 二次状态对 | 有共享奇素因子的状态对 | 共享奇素因子关系 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 67,369 | 15 | 0 | 105 | 37 | 44 |
| 878,089 | 21 | 0 | 210 | 94 | 113 |
| 13,782,409 | 31 | 0 | 465 | 191 | 235 |
| 26,034,649 | 20 | 0 | 190 | 73 | 84 |
| 57,399,241 | 29 | 1 | 406 | 155 | 190 |
| 152,498,329 | 23 | 0 | 253 | 94 | 107 |
| 283,319,689 | 46 | 0 | 1,035 | 488 | 624 |
| **合计** | **185** | **1** | **2,664** | **1,132** | **1,397** |

1,397 条共享奇素因子关系全部满足上述两条算术约束。因而这些 (G) 状态并不是彼此
自动排斥的：相容关系可以在同一个素数的许多模数之间同时成立。

## 结论边界

该审计强化了二次互反拉回的可靠性，也给出了可用于筛法的碰撞限制；但它没有证明

\[
\text{“所有线性状态不能同时为 }G\text{”。}
\]

更重要的是，七个点的唯一命中仍要从大量 (G) 状态和 (F) 状态中被选出。二次相容律
不涉及 (F) 型有限指数盒，也不涉及高阶角色或私有指数层。因此下一阶段必须把共享碰撞
层与 (F\to\) 命中的反足点增长结合起来，或寻找一个能同时处理两类障碍的跨状态证书。

## 复现

```bash
python3 reproductions/type_i_linear_single_hit_quadratic_compatibility_7.py \
  --output reproductions/type-i-linear-single-hit-quadratic-compatibility-7-results.json
python3 -m unittest tests/test_type_i_linear_single_hit_quadratic_compatibility_7.py -q
```

结果文件：[type-i-linear-single-hit-quadratic-compatibility-7-results.json](../reproductions/type-i-linear-single-hit-quadratic-compatibility-7-results.json)
