---
kind: claim
claim_id: type-I-f-overflow-scaled-source-lift-boundary
title: 多支持较小块平方终端的 b 等于 1、2、4 缩放提升边界
statement: 对多支持溢出分支的 253 个去重较小块平方终端，完整枚举缩放刚性允许的 b∈{1,2,4} 及所有正互素 a，并检查 d=p-4a(p-n)/b>0、b|n、d|(an/b) 和全部平方尾条件；共执行 9871013 个 a 循环，仅 1 个 (a,b,d) 通过源参数条件，进一步检查 17731 个 e 因子后无一个通过双同余，得到 0 个 Type I 参数和 0 个目标素数命中。该结果只排除当前同尾缩放族在这批终端上的覆盖。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-square-terminal-lift-boundary
  - scaled-source-descent-rigidity
topics:
- type-I
- F-state
- overflow-radius
- block-square
- scaled-source
- descent
- lift
- negative-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的 \(b=1,2,4\) 缩放提升边界

## 审计范围

对[多支持较小块平方终端的移位外部源提升边界](type-I-f-overflow-shifted-external-lift-boundary.md)中的 253 个去重平方终端，记源为 \(n\)、目标素数为 \(p\)，并令 \(t=p-n\)。依据[缩放一坐标提升的四分母刚性与非倍数 Type I 递降](scaled-source-descent-rigidity.md)，只枚举

\[
b\in\{1,2,4\},\qquad \gcd(a,b)=1,\qquad d=p-\frac{4a t}{b}>0.
\]

随后要求 \(b\mid n\)、\(d\mid an/b\)，并对

\[
L=an,\qquad q=4a-b
\]

的全部 \(e\mid L^2\) 检查

\[
e\le L,\qquad bd\mid e,\qquad
q\mid L+e,\qquad q\mid L+\frac{L^2}{e},
\]

以及自然缺口 \(3\le m=(4e+bd)/q\le p-2\)。每个保留项都独立复核源/目标单位分数恒等式和 \(D=bd\,u^2/e\mid u^2\)。

## 结果

```text
candidate_count: 253
a_loop_count: 9871013
admissible_ab_count: 1
admissible_b_histogram: {"4": 1}
e_divisor_count: 17731
e_candidate_count: 0
parameter_count: 0
hit_prime_count: 0
```

唯一通过源参数条件的点是

\[
(p,n,b,a,d)=(168434809,168434560,4,676445,4).
\]

该点的 17,731 个 \(e\) 因子均未通过两条平方尾同余，因此没有进入 Type I 证书。

## 逻辑边界

这是一个定向有限负边界：

1. \(a\) 和 \(e\) 的枚举对保存的 253 个终端以及当前 \(b=1,2,4\) 同尾缩放公式是完整的；
2. 它不排除非同尾替换、一般 \(B\) 终端、Type II 或新的良基下降；
3. 它不说明这些源没有其它 Erdős--Straus 表示，也不构成全称选择器。

因此，现有两类平方终端到目标证书的缺口已经同时排除了奇数距离、移位外部源和 \(b=1,2,4\) 同尾缩放三条已知接口；后续应研究一般 \(B\) 的补偿平方桥或非同尾双分母递降。

## 复现

```bash
python3 reproductions/type_i_f_overflow_scaled_source_lift.py
```

结果文件：

`reproductions/type-i-f-overflow-scaled-source-lift-results.json`

结果文件 SHA-256：

`00f492e6290284a8bbf0bd3d15c8245d09c2108477006027344f8be6441dd1a5`

