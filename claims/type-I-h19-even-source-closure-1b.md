---
kind: claim
claim_id: type-I-h19-even-source-closure-1b
title: H19 十亿源自由残余的偶源反向二尾闭合
statement: 对p<=10^9的664个H19源自由残余，完整枚举m<=215的Type I正规形和严格最大尾反向边，全部664个有偶数源。首个偶源边最大缺口仅91，唯一达到该值的是p=433984321；故同一偶源终止机制在独立的十亿压力子集上给出664=664的有限闭合。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- even-source
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

# H19 十亿源自由残余的偶源反向二尾闭合

H19 十亿剖面中的 $664$ 个源自由残余来自一个与五亿普通 $p-1$ 尾遗漏不同的压力筛选。
对每个目标完整枚举

$$
3\le m\le215,\qquad m\equiv3\pmod4
$$

内的 Type I 正规形及严格最大尾反向边，得到

$$
664=664_{\text{偶源反向边}},\qquad\text{遗漏}=\varnothing. \tag{1}
$$

每条源分母均为偶数，因此可由 $n=2$ 的解按比例缩放终止。虽然审计允许 $m$ 到 $215$，
首个偶源边的实际最大缺口只有

$$
p=433{,}984{,}321,\qquad m=91,\qquad n=431{,}872{,}848. \tag{2}
$$

按缺口递增枚举意味着该点在同一选择器的 $m\le87$ 盒中没有偶源边；故 $91$ 是这个 H19
有限样本的精确首缺口边界。

此结果是对偶源反向机制的独立规模检验，不应被误读为“所有十亿核心素数”都已由该规则
闭合。H19 只是特定 Type II 扇留下的源自由残余；全局难点仍是为任意核心素数选择正规形和
偶桥因子。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_even_source_closure.py
python3 -m unittest tests/test_type_i_h19_even_source_closure.py -q
~~~
