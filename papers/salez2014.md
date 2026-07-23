---
kind: paper
citation_key: salez2014
title: 'The Erdos-Straus conjecture: New modular equations and checking up to N = 10^17'
authors:
- Serge E. Salez
year: 2014
first_publication_date: '2014-06-24'
publication_status: preprint
assessment_status: computationally_reported
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://arxiv.org/abs/1406.6307
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- modular-equations
- modular-sieve
- computation
references:
- rosati1954
- yamamoto1965
- swett1999
visibility: public
last_checked: '2026-07-23'
arxiv: '1406.6307'
---

# The Erdos-Straus conjecture: New modular equations and checking up to N = 10^17

## 定位

证明一次素多项式范围内七条参考模方程的完备性，设计组合模筛，并报告计算验证到 10^17。

## 主要贡献

- 在四条既有参考方程上增加三条，共七条，而不是九条。
- 定义 S_m、缩短过滤器 S_m*、周期 G_i 与候选剩余集 R_i。
- 报告 G7=892371480、|R7|=147348、平均候选间隔 6056，并提供 C++ 程序附件。

## 证据与核查

- 已核对摘要、第 1 节约化、参考方程、筛法参数与 10^17 计算计数。
- 本知识库另有小尺度重实现，用精确有理数核对基础恒等式与过滤器定义；未重跑 10^17。

## 局限与后续

七式完备性只针对论文定义的线性素多项式模方程类别，不排除更广的参数化。计算上界仍是作者报告。
