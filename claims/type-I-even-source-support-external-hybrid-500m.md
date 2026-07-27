---
kind: claim
claim_id: type-I-even-source-support-external-hybrid-500m
title: 五亿偶桥支撑三或平移外源的终止混合闭合
statement: 五亿普通Type II尾遗漏中，1,715个有m<=215且桥因子E至多含三个不同素因子的偶源Type I反向边；唯一两个最小支撑为4的点42622969与357834409，分别由偏移s=5与s=9的平移平方外源偶源严格递降闭合。故1717=1715+2且无遗漏；四素因子桥并非该有限终止闭合的必要基本分支。
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

# 五亿偶桥支撑三或平移外源的终止混合闭合

[偶桥因子支撑边界](type-I-tail-reverse-even-source-support-boundary-500m.md)表明，完整
$m\le215$ 盒中有两个点的最小偶桥因子 $E$ 含四种不同素因子。它们并不强迫在终止菜单中
保留四素因子桥：读取独立平移平方外源审计并重建其首个兼容因子射线，得到

$$
1{,}717
=1{,}715_{\#\operatorname{supp}E\le3\text{ 的偶源反向边}}
+2_{\text{平移平方外源偶源边}}. \tag{1}
$$

两个外源替代为

| (p) | 偏移 (s) | 源分母 |
|---:|---:|---:|
| 42,622,969 | 5 | 42,620,000 |
| 357,834,409 | 9 | 356,817,834 |

两条源均为偶数，所以同样直接缩放至 $n=2$ 的终止解。

该分区的意义是有限且策略性的：它把“高因子支撑”从一个必须解释的终止障碍变成可切换至
另一已知构造的两点边界。它不证明 $s\le9$ 或桥支撑三在更大范围内有效，也不提供全局的
源侧选择器。

可复现命令：

~~~bash
python3 reproductions/type_i_even_source_support_external_hybrid.py
python3 -m unittest tests/test_type_i_even_source_support_external_hybrid.py -q
~~~
