---
kind: claim
claim_id: type-II-tail-shifted-quadratic-offset-boundary-500m
title: 五亿平移平方外源的五百万偏移边界
statement: 对p<=500000000的124条零偏移平方外源遗漏，123条在s<=202521有平移平方外源严格递降；唯一477015289未命中。对该点单独完整枚举所有s<=5000001及每个s的兼容k后仍无命中，实际兼容射线数为50。该点有独立gap=27的Type I直接证书，且其两张非最短gap-27证书可分别严格递降到偶数源32897608和475989640；故此边界只否定当前平移外源递降族，不是否定Erdos--Straus猜想。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- external-source
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿平移平方外源的五百万偏移边界

五亿完整审计中，普通 Type II 双尾遗漏有1,717条；其中1,593条已有零偏移完整平方外源
递降，留下124条平移压力点。固定偏移完整枚举给出

$$
124=123_{s\le202{,}521}+1_{\rm miss}. \tag{1}
$$

唯一遗漏为

$$
p=477{,}015{,}289. \tag{2}
$$

这首次打破了两亿至四亿均保持的 $s\le202{,}521$ 经验盒。为排除它只是小幅越界，对该点
从 $s=1$ 起逐个枚举所有 $s\equiv1\pmod4$ 至

$$
s\le5{,}000{,}001,
$$

并在每个 $s$ 上完整枚举

$$
k\mid\frac{p-s}{4},\qquad s\mid4k-1.
$$

结果仍无平移平方外源证书；整个五百万盒中只有50条兼容 $(s,k)$ 射线。这是当前该外源
递降族的精确有限失败边界，而不是仅对 $k$ 截断的失败。

该点不是 Erdős--Straus 猜想的数值反例。完整短证书搜索给出 Type I 缺口

$$
m=27,\qquad x=119{,}253{,}829,\qquad d=7{,}986{,}977,
$$

其中

$$
x=29\cdot433\cdot9497,\qquad d=29^2\cdot9497.
$$

故它显示的是“当前平移平方外源选择器未命中”，而不是方程无解。小奇距离
$c<100$ 的完整偶源扇，以及 $(3p+1)/4$ 源递降，在该点也未命中。随后对 gap-27
目标证书的二分母保留反向枚举发现两条不同形状的严格边，分别降到偶数源
$32{,}897{,}608$ 和 $475{,}989{,}640$，见
[gap-27 的二分母保留严格递降](boundary-gap-27-reverse-two-tail-bridge.md)。这说明新的
研究任务不是证明该点完全无递降，而是从目标因子状态直接构造这种可递归维护的反向边。
更进一步，对五亿范围全部124个平移外源压力点的同类短缺口反向枚举已全部命中，最大选中
缺口仅为111，见 [五亿压力集的反向二尾全闭合](type-II-tail-pressure-reverse-two-tail-closure-500m.md)。
因此本卡保留的是平移平方外源族的真实有限边界，而不再是这124点上的一般严格递降边界。
该124点只是五亿普通尾遗漏1,717点的最难外源子集；完整遗漏集也已在最大缺口127的同类
目标侧反向审计中全闭合，见 [五亿普通尾遗漏的反向二尾全闭合](type-II-tail-reverse-two-tail-closure-500m.md)。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-500m-results.json \
  --offset-bound 202521 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-500m-results.json
python3 reproductions/type_ii_tail_shifted_quadratic_single_offset_search.py \
  --prime 477015289 \
  --offset-bound 5000001 \
  --output reproductions/type-ii-tail-shifted-quadratic-single-offset-search-477015289-5m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_offset_boundary_500m.py -q
~~~
