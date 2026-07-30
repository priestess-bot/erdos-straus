---
kind: claim
claim_id: type-I-f-overflow-even-standard-one-denominator-boundary
title: 多支持较小块平方终端的偶标准源一项保留提升边界
statement: 对多支持溢出分支的 253 个去重较小块平方终端，241 个源满足 p/2<n<p；从标准偶源 4/n=1/(n/2)+1/n+1/n 出发，完整枚举 e|(np)^2、e<=np 且 (4n-p)|(np+e)，共检查 581931 个因子，没有一个目标候选、自然范围候选或素数命中。其余 12 个源在 n<=p/2，不属于该一项保留定理的正距离域。该结果只排除当前标准偶源一项保留、两尾重组族。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-square-terminal-lift-boundary
  - even-standard-two-tail-descent
topics:
- type-I
- F-state
- overflow-radius
- block-square
- even-terminal
- one-denominator-lift
- two-tail-recombination
- descent
- negative-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的偶标准源一项保留提升边界

## 审计范围

对 253 个去重平方终端源 \(n\) 和目标素数 \(p\)，先按
\(p/2<n<p\) 分流。对上半区 241 个源，使用标准偶数恒等式

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\]

保留一个分母 \(n\)，并令

\[
R=4n-p,\qquad S=np.
\]

依据[偶数标准源保留一项并重组两尾的完整递降族](even-standard-two-tail-descent.md)，完整枚举

\[
e\mid S^2,\qquad e\le S,\qquad R\mid S+e,
\]

随后由

\[
u=\frac{S+e}{R},\qquad
v=\frac{S+S^2/e}{R}
\]

恢复目标尾，并独立验证单位分数恒等式、排序和自然首分母范围。

## 结果

```text
candidate_count: 253
upper_half_count: 241
lower_half_count: 12
divisors_checked: 581931
congruence_candidate_count: 0
target_candidate_count: 0
natural_candidate_count: 0
target_hit_prime_count: 0
natural_hit_prime_count: 0
```

上半区源没有一个满足一项保留判据。下半区 12 个源的 \(R=4n-p\le0\)，不属于该定理
的正距离域，不能据此宣称失败。

## 逻辑边界

1. 该审计完整覆盖 241 个上半区源的标准偶源一项保留族和全部 \(e\mid(np)^2\)；
2. 它不覆盖下半区源的其它正参数化，也不覆盖非标准偶数源、只保留其它分母、同时重组
   两个或三个坐标、一般 Type I/II 证书；
3. 因而它把剩余缺口进一步收窄为“需要非标准源或真正多坐标耦合”，但不是全称递降证明。

## 复现

```bash
python3 reproductions/type_i_f_overflow_even_standard_one_denominator_lift.py
```

结果文件：

`reproductions/type-i-f-overflow-even-standard-one-denominator-lift-results.json`

结果文件 SHA-256：

`5f45f4ec0e7b117517c271af7ea8f6ddee6545347878caa2499cd8385d3df478`
