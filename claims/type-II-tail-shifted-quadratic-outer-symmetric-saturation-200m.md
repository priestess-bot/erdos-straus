---
kind: claim
claim_id: type-II-tail-shifted-quadratic-outer-symmetric-saturation-200m
title: 两亿平移平方尾的外层对称饱和逃逸
statement: 两亿最小偏移中未达到对称盒子群饱和的17条射线，改在更大偏移上逐个精确扫描后，s<=202521已有11条达到饱和；扩大探索盒至s<=1000001时达到14条，仅26034649、168434809、171292489仍未达到该充分条件。每个命中均重新构造并验证严格递降证书。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- divisor-residues
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两亿平移平方尾的外层对称饱和逃逸

令 $\Delta_t(L)$ 为[反向普通除子对判据](shifted-quadratic-tail-opposite-divisor-pair.md)
中的有符号指数盒。若 $\Delta_t(L)$ 填满由 $L$ 的素因子生成的单位子群，且该子群含有
$-1$，则该射线自动有完整平方尾。

最小偏移审计中有17条射线没有达到这一充分条件。对每条射线从其已知最小偏移之后开始，
逐个枚举所有 $s\equiv1\pmod4$ 和所有兼容

$$
k\mid\frac{p-s}{4},\qquad s\mid4k-1.
$$

每次对子群饱和命中都再次构造实际的平方尾因子并检验严格递降。结果为

$$
17=11_{s\le202{,}521}+6_{\rm miss},
$$

而将同一探索盒扩大到 $s\le1{,}000{,}001$ 后为

$$
17=14_{s\le1{,}000{,}001}+3_{\rm miss}. \tag{1}
$$

百万盒内仍未饱和的三条为

$$
26{,}034{,}649,\qquad168{,}434{,}809,\qquad171{,}292{,}489. \tag{2}
$$

例如最难的六坐标最小射线 $p=6{,}294{,}649$ 在其最小 $s=25$ 上没有饱和，
但在

$$
s=33{,}305,\quad k=391{,}334,\quad t=47
$$

首次达到 $|\Delta_t(L)|=|H_t(L)|=46$，并给出源距离4的已验证递降。另一个偏移较大的
新命中是 $p=185{,}772{,}409$：其最小偏移为13，而首次饱和偏移为651,833，源距离4。

这说明“最小偏移上低密度或未饱和”并非稳定障碍：外层偏移可有选择地改变 $t,L$ 的因子
残数结构，并把多数压力点送入可由群论充分条件解释的区域。结论严格限于上述有限偏移盒，
不声称三条遗漏点没有其他平移平方尾，也不预言统一偏移上界。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_outer_saturation_profile.py
python3 reproductions/type_ii_tail_shifted_quadratic_outer_saturation_profile.py \
  --offset-bound 1000001 \
  --output reproductions/type-ii-tail-shifted-quadratic-outer-saturation-profile-200m-1m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_outer_saturation_profile_200m.py -q
~~~
