---
kind: claim
claim_id: type-II-h19-p-minus-one-scaled-source-quadratic-boundary
title: 完整 p-1 缩放源不能闭合 H19 的四个二次递降漏点
statement: 对 H19 十亿范围中四个完整二次因子外部源递降漏点，p-1 的全部 b=1,2,4 缩放候选均无平方尾命中。因此完整 p-1 分支不能替代受控 r 偶源递降。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- scaled-source
- p-minus-one
- finite-audit
- boundary
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# \(p-1\) 缩放源不能闭合 H19 的四个二次递降漏点

对 H19 十亿范围中完整二次因子外部源递降留下的四个素数

\[
35\,840\,809,\quad132\,285\,169,\quad141\,326\,089,\quad640\,775\,689,
\]

固定 \(n=p-1\)，完整枚举所有由移位因子约化给出的 \(an\)、\(an/2\)、\(an/4\) 候选，
并对每个候选完整枚举强制倍数平方尾。118 个去重候选全数失败，故没有相应的 Type I
证书。其中 \(b=1\) 的 29 个候选正是旧 \(c=1\) 标准偶源；其余 89 个为非倍数候选。

这说明 \(p-1\) 缩放源虽可闭合固定 \(r\) 的 15 点边界，却不能取代四点上的受控
\(r\) 偶源递降。该结论只排除这一固定源的三种完整比例，不排除其它源、其它尾部公式或
已有的 \(r\)-偶源提升。

## 重建

~~~bash
python3 reproductions/type_ii_h19_p_minus_one_scaled_source_quadratic_boundary.py
python3 -m unittest tests/test_type_ii_h19_p_minus_one_scaled_source_quadratic_boundary.py -q
~~~
