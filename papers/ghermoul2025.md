---
kind: paper
citation_key: ghermoul2025
title: Exact Polynomial Families Solving the Erdos-Straus Equation
authors:
- Bilal Ghermoul
year: 2025
first_publication_date: '2025-08-10'
publication_status: preprint
assessment_status: computationally_reported
corpus_tier: A
reading_status: studied
language: en
source_pointer: https://arxiv.org/abs/2508.07383
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-28'
topics:
- polynomial-family
- computation
- conjectural-cover
references:
- bello2012
- salez2014
visibility: public
last_checked: '2026-07-23'
arxiv: '2508.07383'
---

# Exact Polynomial Families Solving the Erdos-Straus Equation

## 定位

构造四个多变量多项式族；前三族的每个输出有显式分解，但四族合并覆盖所有 1 mod4 整数仍是猜想。

## 主要贡献

- 证明前三个族输出的分解恒等式。
- 报告 q<=10^9 的联合覆盖和单个族对素数到至少 1.2*10^10 的覆盖。
- 附 Mathematica 实现。
- 其显式已证覆盖正好处理 \(q\not\equiv0\pmod6\)；未证的 \(q=6c\) 对应
  本库的核心 \(p=24c+1\) 分支。

## 证据与核查

- 已核对 arXiv 摘要、公式 (4)-(7)、(14)-(17) 与多项式构造章节。
- 论文引言把若干历史归属写得过于宽泛；本库不沿用其 Tao entropy 等表述。

## 局限与后续

联合覆盖是计算支持的 conjecture；其中 \(q\equiv0\pmod6\) 的覆盖没有全称证明，且
计算尚未独立全量复现。详见[其核心残余归约](../claims/ghermoul-2025-core-residual-reduction.md)
和[第二族的 \(B=1\) 正规形等价](../claims/ghermoul-2025-p2-b1-normal-form-equivalence.md)。
