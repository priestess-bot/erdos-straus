---
kind: paper
citation_key: bradford_ionascu2015
title: A geometric reduction of the Erdos-Straus conjecture
authors:
- Kyle Bradford
- Eugen J. Ionascu
year: 2015
first_publication_date: '2015-01-01'
publication_status: peer_reviewed
assessment_status: verified_with_caveat
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://camo.ici.ro/journal/vol17/v17a3.pdf
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- geometric-reduction
- computation
- type-I
- conjectural-boundary
references:
- ionascu_wilson2010
- elsholtz_tao2013
visibility: public
last_checked: '2026-07-23'
arxiv: '1411.3403'
---

# A geometric reduction of the Erdos-Straus conjecture

## 定位

以同一目标 \(p\) 的 \((x,y)\) 格点边界定义 Type I(a)/I(b) 解；它是搜索空间的
几何重述，不是到较小分母实例的解提升。

## 主要贡献

- 定义边界型 Type I(a)/I(b) 解，并证明其 Proposition 2.2：Type I(a) 解也是 Type I(b) 解。
- 将 Ionascu--Wilson 的模 \(9240\) 覆盖结果所产生的解识别为 Type I(b)（Theorem 2.6）。
- 报告：在 \(p<10^8\) 的计算中，除 \(2,2521\) 外均发现满足其边界模式的解。
- 提出 Conjectures 2.8 和 2.10，猜想每个足够大素数都有这类边界点。

## 证据与核查

- 已核对期刊 PDF 的 Definitions 2.1、Proposition 2.2、Theorem 2.6、Conjectures 2.3、2.4、2.8、2.10 及第 3 节证明。
- 文中开头的“all primes except”表述在第 2 节被限定为 \(p<10^8\) 的计算观察；用于一般 \(p\) 的存在性随后明确标为 conjecture。
- 所有构造都围绕固定 \(p\) 选择 \(x,y\)；它们不产生 \(n<p\) 或 \(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 的映射。

## 局限与后续

该文可用作边界型短证书搜索的历史和参数化背景，但 Conjecture 2.10 正是未证明的全称
选择器，不能完成“短证书或递降”引理。
