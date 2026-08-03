---
kind: paper
citation_key: girard_schmid2019_direct_zero_sum_rank_three
title: Direct zero-sum problems for certain groups of rank three
authors:
- Benjamin Girard
- Wolfgang A. Schmid
year: 2019
first_publication_date: '2018-06-20'
publication_status: preprint
assessment_status: verified
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://arxiv.org/abs/1806.07636
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-08-04'
topics:
- finite-abelian-groups
- davenport-constant
- rank-three-groups
- zero-sum-theory
- subsequence-products
references:
- schmid2011_c2_squared_c2n
visibility: public
last_checked: '2026-08-04'
arxiv: '1806.07636'
---

# Direct zero-sum problems for certain groups of rank three

## 本库使用的定理

论文第 2 节 Theorem 2.7 证明：对 \(m,n\ge1\)，

\[
D(C_2\oplus C_{2m}\oplus C_{2mn})=2m+2mn.
\]

这正是该不变因子族的精确 Davenport 阈值。把单位素因子残数看成该群中的有限序列，
长度达到该阈值时，必有非空子序列和为零；在乘法记号下就是非空子积等于单位元。

## Erdős--Straus 选择器中的作用

本库将它作为 Type II 共享除子选择器的秩三输入。当前 10M、\(m\le239\) profile 中，
所有秩三压力点都落在

\[
C_2\oplus C_2\oplus C_{30}
\quad\text{或}\quad
C_2\oplus C_4\oplus C_{12},
\]

对应阈值分别为 (32) 和 (16)。达到阈值才可以无条件构造共享除子；低于阈值的记录
只说明 Davenport 定理没有强制力，不说明没有更短的零积。

论文讨论的是一般有限阿贝尔群的零和常数，不是 Erdős--Straus 猜想；实际除子、
scaled-first marked lift 和范围核验均由本仓库独立实现。
