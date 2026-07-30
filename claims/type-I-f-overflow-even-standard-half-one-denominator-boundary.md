---
kind: claim
claim_id: type-I-f-overflow-even-standard-half-one-denominator-boundary
title: 多支持较小块平方终端的标准偶源 n 除以 2 一项保留边界
statement: 对 253 个去重较小块平方终端中的 241 个上半区源，标准偶源 4/n=1/(n/2)+1/n+1/n 保留坐标 n/2，完整枚举 e|(p(n/2))^2、e<=p(n/2) 且 (2n-p)|(p(n/2)+e)，共检查 221723 个因子，没有同余候选、目标候选或自然范围命中。该结果只排除标准偶源的 n/2 一项保留族。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-square-terminal-lift-boundary
  - even-standard-two-tail-descent
  - one-denominator-lift-factor-criterion
topics:
- type-I
- F-state
- overflow-radius
- block-square
- even-terminal
- standard-even-source
- one-denominator-lift
- descent
- negative-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: one-denominator-lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的标准偶源 \(n/2\) 一项保留边界

## 审计范围

对 253 个平方终端源 \(n\)，241 个满足 \(p/2<n<p\)。标准偶源为

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\]

本审计保留另一个未覆盖的坐标 \(c=n/2\)，令

\[
R=4c-p=2n-p,\qquad S=pc.
\]

完整枚举

\[
e\mid S^2,\qquad e\le S,\qquad R\mid S+e,
\]

并复核互补同余、目标单位分数恒等式和自然首分母范围。

## 结果

```text
candidate_count: 253
upper_half_count: 241
lower_half_count: 12
divisors_checked: 221723
congruence_candidate_count: 0
target_candidate_count: 0
natural_candidate_count: 0
target_hit_prime_count: 0
natural_hit_prime_count: 0
```

241 个上半区源没有一个通过 \(n/2\) 一项保留判据；12 个下半区源不满足
\(R=2n-p>0\) 的正距离前提。

## 逻辑边界

这与保留 \(n\) 的审计合并后，完整覆盖标准偶源的两个不同坐标。它不排除非标准源、
下半区的其它源解、同时重组两个或三个坐标，或一般 Type I/II 证书。

## 复现

```bash
python3 reproductions/type_i_f_overflow_even_standard_half_one_denominator_lift.py
```

结果文件：

`reproductions/type-i-f-overflow-even-standard-half-one-denominator-lift-results.json`

结果文件 SHA-256：

`fc22b53d7c6508e8177107dcb7897bd1d14a61cd174cadc47efa44ee1e2d64b3`

