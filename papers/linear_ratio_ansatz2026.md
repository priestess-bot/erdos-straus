---
kind: paper
citation_key: linear_ratio_ansatz2026
title: A Linear-Ratio Ansatz for Congruence Families in the Erdos-Straus Equation
authors:
- Idriss Olivier Bado
year: 2026
first_publication_date: '2026-05-22'
publication_status: preprint
assessment_status: verified_with_caveat
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://www.researchgate.net/publication/405169342_A_Linear-Ratio_Ansatz_for_Congruence_Families_in_the_Erdos-Straus_Equation
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-24'
topics:
- type-I
- congruence-family
- fixed-gap
- finite-cover-obstruction
- gray-literature
references:
- elsholtz_tao2013
- lopez2024
visibility: public
last_checked: '2026-07-24'
doi: 10.13140/RG.2.2.11677.06882
---

# A Linear-Ratio Ansatz for Congruence Families in the Erdos-Straus Equation

## 定位

Bado 的 2026 年 5 月 ResearchGate 预印本。它固定首分母

\[
X=\frac{p+a}{4},\qquad a\equiv3\pmod4,
\]

并规定其余两个分母满足线性比例 \(Z/Y=ps/r\)。每个固定原始三元组
\((a,r,s)\) 都给出一个有限模同余测试和若干无穷同余族；论文也证明有限多个此类三元组
不可能覆盖全部 Mordell 例外类中的素数。

## 已核对的数学内容

- Lemma 3.1 的公式
  \[
  Y=\frac{X(ps+r)}{as},\qquad
  Z=\frac{pX(ps+r)}{ar}
  \]
  在整数性条件下直接给出一组解；Corollary 3.2 将它准确化为模
  \(\operatorname{lcm}(24,4as,4ar)\) 的有限残数测试。
- 在 \(p\nmid ars\) 时，Proposition 4.1 正确说明该主族是 Elsholtz--Tao 的 Type I。
  本库的 linear-ratio-ansatz-type-I-translation 进一步把它精确译为 Bradford
  Type I 除子证书。
- Lemma 5.1 与 Theorem 5.2 的有限覆盖障碍成立：对每个固定原始三元组，残数
  \(1\bmod L(a,r,s)\) 不命中；取所有有限模数的最小公倍数并用 Dirichlet 定理，
  得到无穷多个同时逃过的核心素数。
- Proposition 7.1 和 7.3 的示例族（模 \(264\) 的 \(a=11,r=s=1\)，以及模
  \(1104\) 的 \(a=23,r=4,s=3\)）已由整数公式复核。

## 局限

这是一类固定缺口的 Type I 证书族，不是可从较小实例自动产生目标解的递降映射。
论文自己明确说明：有限模测试和有限计算表均不构成对例外类、更不构成对全部核心素数的
覆盖定理。Theorem 5.2 反而证明固定有限三元组的覆盖不可能性。

因此其实际价值是补充可检索的 Type I 同余族和一个清楚的有限覆盖边界；它不完成本项目
要求的“短证书或递降”全称引理。
