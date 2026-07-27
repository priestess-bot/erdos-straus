---
kind: claim
claim_id: type-I-h19-even-source-support-boundary-1b
title: H19十亿源自由残余的偶桥支撑边界
statement: 对p<=10^9的664个H19源自由残余，完整枚举m<=215的所有偶源Type I最大尾反向边，并最小化桥因子E的不同素因子数，分布为1:474、2:188、3:1、4:1。唯一最小支撑为4的点是p=48605881，故内部偶桥支撑至多三不能覆盖该独立有限盒。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- even-source
- factorization
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# H19十亿源自由残余的偶桥支撑边界

对 H19 十亿源自由残余的全部 $664$ 个目标，穷尽

$$
3\le m\le215,\qquad m\equiv3\pmod4
$$

中的 Type I 正规形和严格最大尾反向边，只保留偶数源，并按

$$
(\#\operatorname{supp}E,\ \Omega(E),\ E,\ B,\ m,\ n)
$$

最小化偶桥因子。总共检查 $42{,}602$ 个正规形和 $56{,}595$ 条严格边，得到

| 最小不同素因子数 ($\#\operatorname{supp}E$) | 点数 |
|---:|---:|
| 1 | 474 |
| 2 | 188 |
| 3 | 1 |
| 4 | 1 |

因此这组独立的十亿压力残余中也不能将内部偶桥预设为至多三个不同素因子。唯一边界点为

$$
\begin{aligned}
p&=48{,}605{,}881,\\
m&=11,\qquad R=6{,}527,\\
E&=2^4\cdot3^2\cdot31^2\cdot193^2
=5{,}154{,}665{,}616.
\end{aligned}
$$

另一个最小支撑至少三的点是 $p=707{,}590{,}321$，其最小桥为

$$
E=2^2\cdot107^2\cdot70{,}351^2.
$$

这与五亿普通尾遗漏中出现的两个四支撑边界相互独立，因而否定了把“至多三素因子内部偶桥”
作为跨残余族的全称选择规则。它不否定偶源终止，也不提供全局支撑界；困难仍是从正规形的
因子中命中模 $R$ 的比二积集。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_even_source_support_minimization.py
python3 -m unittest tests/test_type_i_h19_even_source_support_minimization.py -q
~~~
