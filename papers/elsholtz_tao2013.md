---
kind: paper
citation_key: elsholtz_tao2013
title: Counting the number of solutions to the Erdos-Straus equation on unit fractions
authors:
- Christian Elsholtz
- Terence Tao
year: 2013
first_publication_date: '2011-07-06'
publication_status: peer_reviewed
assessment_status: verified
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://doi.org/10.1017/S1446788712000468
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- type-I-II
- solution-counting
- parametrization
- algorithms
references:
- erdos1950
- bernstein1962
- jia2012
- jollensten1976
- li1981
- rosati1954
- sander1991
- sander1994
- schinzel1956
- schinzel2000
- swett1999
- terzi1971
- vaughan1970
- webb1970
- yamamoto1965
- yang1982
- bello2012
visibility: public
last_checked: '2026-07-23'
doi: 10.1017/S1446788712000468
arxiv: '1107.1010'
---

# Counting the number of solutions to the Erdos-Straus equation on unit fractions

## 定位

现代核心论文：对素数分母的解作 Type I/II 参数化，证明平均解数上下界，给出逐点上界和枚举复杂度，并系统整理历史计算与多项式可解性。

## 主要贡献

- 证明 N(log N)^2 << sum_{p<=N} f(p) << N(log N)^2 log log N。
- 把素数解分为 Type I 与 Type II，并建立完整参数化。
- 给出枚举 Type I/II 解的期望时间 n^(3/5+o(1)) 与 n^(2/5+o(1))。
- 证明原始剩余类模 840 的非平方类可多项式求解，而平方类不能由该固定多项式机制覆盖。

## 证据与核查

- 已取得 arXiv 全文与 Cambridge 出版 PDF，核对主定理、参数化章节、算法结论和 89 条参考文献。
- 平均值丰富不蕴含每个 p 都有解；知识库单独记录这一逻辑边界。

## 局限与后续

论文不证明猜想；若把平均阶误读为逐点非零，会造成核心逻辑错误。
