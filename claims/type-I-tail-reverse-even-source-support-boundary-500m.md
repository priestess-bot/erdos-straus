---
kind: claim
claim_id: type-I-tail-reverse-even-source-support-boundary-500m
title: 五亿偶源反向选择器的桥因子支撑边界
statement: 对五亿普通Type II尾遗漏的1,717个点，完整枚举m<=215的所有偶源Type I最大尾反向边，并最小化桥因子E的不同素因子数，精确分布为1:1061、2:621、3:33、4:2。故至多三个不同素因子的偶桥规则不能覆盖该完整有限盒；两个最小支撑为4的点是p=42622969与p=357834409。
claim_status: computationally_reproduced
topics:
- type-I
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

# 五亿偶源反向选择器的桥因子支撑边界

在[偶源反向选择器](type-I-normal-even-source-selector.md)中，偶源由目标端因子

$$
E\mid4K^2,\qquad E\equiv4K\pmod R,\qquad2\mid E
$$

确定。对 $1{,}717$ 个普通 Type II $p-1$ 尾遗漏，完整枚举 $m\le215$ 的全部 Type I
正规形和全部严格偶源边，并对每个 $p$ 按

$$
(\#\operatorname{supp}E,\ \Omega(E),\ E,\ B,\ m,\ n)
$$

取最小桥因子。共穷尽 $78{,}215$ 个正规形及 $166{,}089$ 条严格边，结果为

| 最小不同素因子数 (#operatorname{supp}E) | 点数 |
|---:|---:|
| 1 | 1,061 |
| 2 | 621 |
| 3 | 33 |
| 4 | 2 |

因此支撑至多三的偶桥选择器在该完整盒内恰遗漏

$$
42{,}622{,}969,\qquad357{,}834{,}409. \tag{1}
$$

两个最小桥因子分别为

$$
\begin{aligned}
42{,}622{,}969:&\quad E=2\cdot3\cdot31\cdot131^2,\qquad m=47,\\
357{,}834{,}409:&\quad E=2^2\cdot59^2\cdot137^2\cdot233^2,\qquad m=95.
\end{aligned} \tag{2}
$$

二者都仍有偶源严格边；(1) 只否定把目标端因子选择预设为至多三个不同素因子的证明策略。
特别是，偶源终止本身已经在同一盒中全覆盖，困难在于从 $K$ 的因子结构中构造满足指定
模 $R$ 同余的乘积，而不是终止基底。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_support_minimization.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_support_minimization.py -q
~~~
