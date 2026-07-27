---
kind: claim
claim_id: type-I-dyadic-residual-low-b-complement-100k
title: 十万前缀二幂p减一残余的低B补集剖面
statement: 对完整二幂p减一桥子族在p不大于100009留下的94个核心素数，穷尽所有自然Type I缺口、B不大于4的正规形与最大尾严格偶源反向桥，全部获得边。按最小源距离选择，93个以源p-1、B属于{1,2}及E不大于136实现；唯一非p-1选择为p=20521，源为p-61，且E=3844=2^2乘31^2。按最小奇部桥选择，每条边的奇素数支撑至多一个、奇部指数和至多二。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- factorization
- dyadic
- finite-audit
- complement
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 十万前缀二幂 \(p-1\) 残余的低 \(B\) 补集剖面

从[完整二幂 \(p-1\) 桥剖面](type-I-dyadic-pminusone-profile-100k.md)的 94 个遗漏开始，对每个点完整枚举

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,
\]

的所有 Type I 正规形，并保留 \(B\le4\) 的最大尾两项保持反向边。每条保留边都用其记录的
\((m,A,B,C,R,K,E,n,a)\) 直接复核目标与源的三项分式恒等式；这里 \(n\) 是严格更小的偶源，
且 \(E\mid4K^2\)。

| 项目 | 数值 |
|---|---:|
| 二幂 \(p-1\) 残余 | 94 |
| \(B\le4\) 严格偶源边 | 5,010 |
| 最小源距离为 \(1\) | 93 |
| 最小源距离最大值 | 61 |
| 最小奇部桥为纯二幂 | 7 |
| 最小奇部桥的奇素数支撑为 1 | 87 |
| 最小奇部指数和最大值 | 2 |

更强的、但仍只限此有限补集的描述为：93 个点可取 \(n=p-1\)，其所选边的
\(B\) 分布为 \(B=1:81\)、\(B=2:12\)，且 \(E\le136\)。唯一按源距离最优的非 \(p-1\)
点为

\[
p=20521,\quad (m,A,B,C)=(331,1,1,5213),\quad R=63,\quad K=323206,
\]
\[
n=20460=p-61,\qquad E=3844=2^2\cdot31^2.
\]

这说明二幂 \(p-1\) 子族的遗漏不是随机逃逸：在本前缀中它们全部落入非常小的非二幂桥或极短的
源位移。然而这不是全称选择器，也不证明 \(B\)、\(E\) 或 \(p-n\) 在任意素数上有界；尤其不能从
该 94 点剖面推出所有将来的二幂残余都有同一性质。

可复现命令：

~~~bash
python3 reproductions/type_i_dyadic_residual_general_edge_profile_100k.py
python3 -m unittest tests/test_type_i_dyadic_residual_general_edge_profile_100k.py -q
~~~
