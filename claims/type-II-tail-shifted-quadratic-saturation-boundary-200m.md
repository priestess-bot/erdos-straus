---
kind: claim
claim_id: type-II-tail-shifted-quadratic-saturation-boundary-200m
title: 两亿平移平方尾的饱和素因子子群边界
statement: 对两亿范围65条最小偏移平移平方尾射线，若只用满足2a>=ord_t(q)-1的素因子q^a|L所生成的完全饱和循环子群来保证-L属于Pi_t(L^2)，则仅命中1511449与168478249两条，且25条平方必要射线全部遗漏。因此该简单饱和子群选择器不足。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- divisor-residues
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两亿平移平方尾的饱和素因子子群边界

在正规形 $-L\in\Pi_t(L^2)$ 中，若 $q^a\mid L$ 且

$$
2a\ge\operatorname{ord}_t(q)-1, \tag{1}
$$

则 $q$ 的可用指数 $0,\ldots,2a$ 已覆盖其模 $t$ 生成的整个循环子群。将所有满足式 (1)
的素因子子群相乘，得到一个显式、可证明包含于 $\Pi_t(L^2)$ 的饱和子群 $H$；若
$-L\in H$，便无需枚举未饱和指数。

对两亿压力集的 65 个最小偏移状态，完整枚举每个偏移下所有兼容 $k$ 后，该充分条件仅命中

$$
1{,}511{,}449,\qquad168{,}478{,}249. \tag{2}
$$

因此

$$
65=2_{\text{饱和子群命中}}+63_{\text{饱和子群遗漏}},
$$

且 25 条必须平方尾的状态无一命中。该结论不否定完整平方因子尾，因为未饱和指数的有限
组合仍可命中；它准确否定的是“只要某些素因子自身达到阶饱和，就足以解释内层选择”的
简化路线。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_saturation_profile.py \
  --input reproductions/type-ii-tail-shifted-quadratic-square-necessity-200m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-saturation-profile-200m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_saturation_profile_200m.py -q
~~~
