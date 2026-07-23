---
kind: paper
citation_key: mihnea_dumitru2025
title: Further verification and empirical evidence for the Erdos-Straus conjecture
authors:
- Spiridon Mihnea
- Bogdan C. Dumitru
year: 2025
first_publication_date: '2025-08-29'
publication_status: preprint
assessment_status: computationally_reported
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://arxiv.org/abs/2509.00128
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- computation
- modular-sieve
- solution-counting
- reproducibility
references:
- salez2014
- elsholtz_tao2013
- bradford2024
visibility: public
last_checked: '2026-07-23'
arxiv: '2509.00128'
---

# Further verification and empirical evidence for the Erdos-Straus conjecture

## 定位

扩展 Salez 的模过滤器，报告验证到 10^18，并公开 Python/C++/GMP 代码；同时采样解计数函数。

## 主要贡献

- 加入 S29 得到 G8=25878772920 与 |R8|=2101514。
- 把搜索拆成至 k=38641709 的批次，并报告约两周运行。
- 公开代码与候选处理说明。

## 证据与核查

- 已核对 arXiv 原文 Section 2、参数、边界和实现说明。
- Pomerance–Weingartner 期刊论文提及该计算，但这不是独立重跑。

## 局限与后续

本库未完成 10^18 全量复现；最高上界必须写作公开报告。
