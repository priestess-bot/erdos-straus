---
kind: paper
citation_key: bello2012
title: On Egyptian Fractions
authors:
- Manuel Bello-Hernandez
- Manuel Benito
- Emilio Fernandez
year: 2012
first_publication_date: '2010-10-11'
publication_status: preprint
assessment_status: computationally_reported
corpus_tier: A
reading_status: studied
language: en
source_pointer: https://arxiv.org/abs/1010.2035
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- polynomial-family
- algorithm
- computation
references:
- yamamoto1965
- swett1999
visibility: public
last_checked: '2026-07-23'
arxiv: '1010.2035'
---

# On Egyptian Fractions

## 定位

构造三变量多项式可解族，证明存在任意长连续可解区间，给出贪心型算法并报告验证到 2*10^14。

## 主要贡献

- Theorem 1 证明存在任意长的连续可解整数序列。
- 多项式 p(alpha,beta,gamma) 的值自动给出分解，但 Lemma 7 表明它不覆盖完全平方数。
- 结合算法与多项式族报告 2<=n<=2*10^14 全部可解。

## 证据与核查

- 已核对 arXiv v2 摘要、公式 (2)-(3)、Theorem 1 和 Lemma 1。
- 2*10^14 属作者计算报告，本库未完整复现。

## 局限与后续

作者关于特定素数族被多项式覆盖的陈述含计算验证与 conjecture，不能写作全称定理。
