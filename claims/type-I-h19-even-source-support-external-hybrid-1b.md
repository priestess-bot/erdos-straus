---
kind: claim
claim_id: type-I-h19-even-source-support-external-hybrid-1b
title: H19十亿偶桥支撑三或零偏移外源的混合闭合
statement: H19十亿664个源自由残余中，663个有m<=215且桥因子E至多含三个不同素因子的偶源Type I反向边；唯一四支撑点p=48605881有零偏移二次外源偶数源n=42530146。故664=663+1且无遗漏，四素因子内部桥并非该有限终止菜单的必要基本分支。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- even-source
- external-source
- hybrid-closure
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-and-lift-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# H19十亿偶桥支撑三或零偏移外源的混合闭合

[H19 十亿偶桥支撑边界](type-I-h19-even-source-support-boundary-1b.md)中，唯一最小四支撑内部桥是

$$
p=48{,}605{,}881.
$$

固定零偏移的平移二次外源参数化，对 $k\mid(p-1)/4$ 穷尽所有兼容候选。第一个外源证书的源
为奇数，不能接到 $n=2$ 终止基底；继续同一完整候选枚举，第二个兼容候选给出

$$
n=42{,}530{,}146<p,\qquad k=2,\qquad q=7,\qquad s=1,
$$

并由因子 $1{,}412$ 产生严格外源证书。这里 $n$ 为偶数，故可直接按比例缩放至 $n=2$ 的
已知终止解。于是有限闭合精确分成

$$
664=663_{\#\operatorname{supp}E\le3\text{ 的内部偶源反向边}}
+1_{\text{零偏移外源偶源}},
\qquad\text{遗漏}=\varnothing.
$$

该结论不声称零偏移外源总能替代高支撑桥，也不把 H19 残余视为全体十亿核心素数。它只表明，
这个新四支撑反例同样可以从有限终止菜单中移除；应将内部积集复杂度和可终止分支复杂度分开
研究。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_even_source_support_external_hybrid.py
python3 -m unittest tests/test_type_i_h19_even_source_support_external_hybrid.py -q
~~~
