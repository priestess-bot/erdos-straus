---
kind: claim
claim_id: type-II-shared-bounded-support-selection-boundary
title: 共享 Type II 选择器的两素与三素支撑边界
statement: 在 p<=10^7 的 84 个四自动缺口后且无 k=1 选择器的核心素数中，完整扫描所有 m<=239、m=3 mod4 的 Type II 缺口和 p+m 的全部共享除子。每点可用共享除子的最小不同素因子数分布为 1:10、2:54、3:18、4:2。故固定为至多两个或至多三个不同素因子的共享选择规则均不能覆盖该有限压力集；p=967129 与 p=5596369 在所审计范围均至少需四素支撑。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- factorization
- divisor-residues
- product-sets
- computation
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器的两素与三素支撑边界

## 最小支撑审计

沿用四自动缺口后的 84 个无 \(k=1\) 压力点。对每个合法缺口

\[
3\le m\le239,\qquad m\equiv3\pmod4,
\]

先要求 \(x=(p+m)/4\) 有 Type II 除子证书；再枚举 \(p+m\) 的每个非平凡除子

\[
D\mid p+m,\qquad D\equiv1\pmod m. \tag{1}
\]

对每个 (1) 重建缩放首分母表示，并计算

\[
\omega(D)=\#\{q:q\mid D,\ q\text{ 为素数}\}. \tag{2}
\]

记录的是一个核心素数在所有通过审计的缺口与共享证书中的最小 \(\omega(D)\)，
不是脚本按缺口顺序最先遇到的证书。

## 精确结果

千万范围的最小支撑直方图为：

| 最小 \(\omega(D)\) | 核心素数点数 |
|---:|---:|
| 1 | 10 |
| 2 | 54 |
| 3 | 18 |
| 4 | 2 |

所有 84 点均在 \(m\le239\) 内有共享 Type II 证书，故本审计没有未命中点。
在单素数幂边界留下的 74 点中，54 点可由双素支撑处理，但另有 18 点至少需
三个不同素因子，且两个点至少需四个：

\[
\begin{aligned}
p&=967129,&m&=47,&D&=16968=2^3\cdot3\cdot7\cdot101,\\
p&=5596369,&m&=31,&D&=5596400=2^4\cdot5^2\cdot17\cdot823.
\end{aligned} \tag{3}
\]

对 (3) 中每个 \(p\)，所有 \(m\le239\) 的同缺口共享证书都满足
\(\omega(D)\ge4\)。

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 10000000 --gap-cap 239 --support-profile \
      --output reproductions/type-ii-automatic-residual-multi-prime-support-profile-10m-results.json

会重建直方图、每个点的最小支撑见证和 (3)。

## 正确结论

这个结果严格排除了两种有限范围强化：

1. 总能用至多两个不同素因子的 \(D\)；
2. 总能用至多三个不同素因子的 \(D\)。

它不排除存在一个更大的统一支撑界，也不构成对 Erdős--Straus 猜想的反例。
但它说明任何正向选择器定理必须处理真正的多重子集积残数，而不能简化为双素因子
配对或固定三因子模板。

因此最有价值的下一命题是一个有条件的积集命中引理：由 \(p+m\) 的素因子残数
生成的带重数子集积集，何时能在同一个有 Type II 证书的缺口达到 \(1\pmod m\)；
其证明必须允许支撑大小随局部因子结构变化。
