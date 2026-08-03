---
kind: paper
citation_key: zhong2025_davenport_rank_two
title: On the Inverse Problem of the k-th Davenport Constants for Groups of Rank 2
authors:
- Qinghai Zhong
year: 2025
first_publication_date: '2025-05-26'
publication_status: peer_reviewed
assessment_status: verified_with_caveat
corpus_tier: A
reading_status: metadata_verified
language: en
source_pointer: https://doi.org/10.1007/s00493-025-00153-3
source_acquired: false
source_verified_against_original: false
source_verification_method: none
description_source: publisher_abstract
description_last_audit: none
topics:
- finite-abelian-groups
- davenport-constant
- rank-two-groups
- zero-sum-theory
- subsequence-products
references: []
visibility: public
last_checked: '2026-08-04'
doi: 10.1007/s00493-025-00153-3
---

# On the Inverse Problem of the k-th Davenport Constants for Groups of Rank 2

## 定位

这篇论文研究有限阿贝尔群秩二时的第 \(k\) 个 Davenport 常数。其摘要明确使用已知
公式：若 \(G\simeq C_{n_1}\oplus C_{n_2}\)、\(n_1\mid n_2\)，则
\[
\mathsf D_k(G)=n_1+k n_2-1.
\]
取 \(k=1\) 即得到本库所需的
\[
\mathsf D(G)=n_1+n_2-1.
\]
循环群则有 \(\mathsf D(C_n)=n\)。

## 本库实际使用

本库将该 rank-at-most-two 公式应用到 Type II 缺口的单位素因子残数生成子群，
构造 \(D\equiv1\pmod m\) 的共享除子。群结构和算术提升由仓库脚本独立重算；论文
只作为 rank-2 Davenport 输入，不被归因于 Erdős--Straus 结论。

## 证据边界

本轮核对了 Springer 元数据、DOI、作者、发表日期和摘要；尚未取得可逐式复核的原文
PDF。因此文献卡保持 verified_with_caveat，具体应用仍只登记为内部证明和有限回放。
