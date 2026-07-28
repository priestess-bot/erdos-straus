---
kind: claim
claim_id: type-I-linear-general-b-obstruction-mixture-profile-600m
title: 七点全线性目标谱的角色与有限指数混合剖面
statement: 对七个补偿平方机制残余的全部278个线性源诱导模数，目标平方除子状态精确分为20个命中、190个子群角色障碍和68个有限指数障碍。每个素数同时存在命中及至少一种失败，且两类失败的比例跨素数显著变化。因此跨源一般B选择器不能只处理角色逃逸或只处理指数盒饱和，必须在同一论证中处理两类精确障碍。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- linear-source
- centered-spectrum
- subgroup-character
- finite-exponent
- target-square-divisor
- pressure-set
- computational-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 七点全线性目标谱的角色与有限指数混合剖面

对固定 \((R,K)\)，一般 \(B\) 目标条件等价于中心化平方除子谱包含 \(-1\)。
[中心化谱障碍二分](type-I-general-b-centered-square-spectrum.md)给出唯一的三分：

\[
\begin{array}{c|c}
\text{分类}&\text{精确条件}\\
\hline
\text{命中}&-1\in\mathcal C_R(K)\\
\text{有限指数}&-1\in\mathcal H_R(K)\setminus\mathcal C_R(K)\\
\text{子群角色}&-1\notin\mathcal H_R(K).
\end{array} \tag{1}
\]

这里 \(\mathcal C_R(K)\) 是 (K^2) 除子的中心化有限指数盒，
\(\mathcal H_R(K)\) 是 (K) 的素因子模 \(R\) 所生成的单位群子群。

输入为[七个补偿平方残余的全线性目标谱闭合](type-I-linear-general-b-spectrum-resolution-profile-600m.md)
所冻结的七个素数。对每个素数，重新穷尽全部线性源诱导的 \(R\)，直接枚举

\[
d\mid K^2,\qquad4d\equiv-1\pmod R,
\]

并在无命中时用单位群证书判定 \(-1\in\mathcal H_R(K)\) 与否。这个审计不从补偿因子
推断一般目标谱；两者是独立计算。

| \(p\) | 线性 \(R\) | 命中 | 有限指数 | 子群角色 |
| ---: | ---: | ---: | ---: | ---: |
| 214729 | 30 | 3 | 8 | 19 |
| 878089 | 24 | 1 | 2 | 21 |
| 2210569 | 28 | 3 | 4 | 21 |
| 13782409 | 41 | 1 | 9 | 31 |
| 64214329 | 47 | 4 | 18 | 25 |
| 105295129 | 55 | 4 | 10 | 41 |
| 536944489 | 53 | 4 | 17 | 32 |
| **合计** | **278** | **20** | **68** | **190** |

每一行都已有至少一个普通线性一般 \(B\) 证书，故此处的失败状态不是素数失败；它们是
同一素数的其它可达模数上的精确局部障碍。\(p=878089\) 的切片复现了既有单点剖面：唯一
命中为 \(R=59\)，两个有限指数模数为 \(279,503\)。

这给出下一阶段的实际约束。角色型障碍占多数，但有限指数型在每个点都存在，并在
\(p=64214329\) 与 \(p=536944489\) 中占到相当比例。因而下列任一路线都不足以单独完成
全称选择：

- 只证明某种跨 \(R\) 的分离角色不能持续存在；
- 只证明某个固定状态的指数盒最终饱和。

需要的命题必须比较同一素数不同源模数的素因子分布，并同时排除“所有状态皆为角色障碍”
与“剩余状态皆为有限指数障碍”两种可能。不同 \(R\) 的单位群没有天然公共坐标，因此本页
不把这个有限剖面误写为跨源角色不相容定理。

复现：

~~~bash
python3 reproductions/type_i_linear_general_b_obstruction_mixture_profile_600m.py
python3 -m unittest tests.test_type_i_linear_general_b_obstruction_mixture_profile_600m -q
~~~
