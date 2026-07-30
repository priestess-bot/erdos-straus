---
kind: claim
claim_id: type-I-f-overflow-four-divisible-nonstandard-one-denominator-boundary
title: 多支持较小块平方终端的四倍源非标准平方尾一项提升边界
statement: 对 253 个去重较小块平方终端源，使用 4|n 的非标准平方尾恒等式并逐坐标应用完整一项保留提升判据；759 个坐标中 506 个满足 4c-p>0，共检查 19961548 个 e|(pc)^2、e<=pc 的因子，没有一个通过双同余、目标恒等式或自然范围，目标素数命中为 0。该结果只排除当前 4|n 非标准源的一项保留族。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-square-terminal-lift-boundary
  - four-divisible-nonstandard-source-lift-obstruction
  - one-denominator-lift-factor-criterion
topics:
- type-I
- F-state
- overflow-radius
- block-square
- even-terminal
- nonstandard-source
- one-denominator-lift
- descent
- negative-boundary
sources:
- paper: subramanian2026
  locator: Equation (2.1)
  role: nonstandard-source-identity
- paper: bradford2024
  locator: Propositions 1--4
  role: one-denominator-lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的四倍源非标准平方尾一项提升边界

## 审计范围

253 个平方终端源都满足 \(4\mid n\)。写 \(n=4t\)，使用非标准源解

\[
\frac4n
=\frac1{t+1}+\frac1{(t+1)^2}+\frac1{t(t+1)^2}.
\]

对三个坐标 \(c\) 分别令

\[
R=4c-p,\qquad S=pc.
\]

对所有 \(R>0\) 的坐标，完整枚举

\[
e\mid S^2,\qquad e\le S,\qquad
R\mid S+e,\qquad R\mid S+\frac{S^2}{e},
\]

并重建两个目标尾，独立验证目标单位分数恒等式和自然首分母范围。

## 结果

```text
candidate_count: 253
coordinate_count: 759
positive_coordinate_count: 506
divisors_checked: 19961548
congruence_candidate_count: 0
target_candidate_count: 0
natural_candidate_count: 0
target_hit_prime_count: 0
natural_hit_prime_count: 0
coordinate_domain_histogram: {"positive": 506, "nonpositive": 253}
```

506 个正距离坐标没有一个通过一项保留判据；253 个首坐标的
\(4(t+1)-p\le0\)，不在该族的正距离域。

## 逻辑边界

1. 该审计完整覆盖 253 个保存源的这一个非标准恒等式、全部三个坐标和全部
   \(e\mid(pc)^2\) 因子；
2. 它不覆盖 \(4\mid n\) 的其它源解、下半区的其它参数化、同时重组两个或三个坐标、
   一般 Type I/II 证书；
3. 因而它只说明当前非标准平方尾的一项保留机制不能承接这些终端，剩余正向空间是
   非标准源重组或跨状态多坐标下降。

## 复现

```bash
python3 reproductions/type_i_f_overflow_four_divisible_nonstandard_one_denominator_lift.py
```

结果文件：

`reproductions/type-i-f-overflow-four-divisible-nonstandard-one-denominator-lift-results.json`

结果文件 SHA-256：

`0e6153dc7f01ca68f8e15089bdbee3365c9d9bdf1e723da4511bb25dc9adfb60`

