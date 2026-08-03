---
kind: paper
citation_key: olson1969_davenport_p_groups
title: A combinatorial problem on finite Abelian groups, I
authors:
- John E. Olson
year: 1969
first_publication_date: '1969-01-01'
publication_status: peer_reviewed
assessment_status: verified_with_caveat
corpus_tier: A
reading_status: metadata_verified
language: en
source_pointer: https://doi.org/10.1016/0022-314X(69)90021-3
source_acquired: false
source_verified_against_original: false
source_verification_method: none
description_source: publisher_abstract
description_last_audit: none
topics:
- finite-abelian-groups
- davenport-constant
- p-groups
- zero-sum-theory
- subsequence-products
references: []
visibility: public
last_checked: '2026-08-04'
doi: 10.1016/0022-314X(69)90021-3
---

# A combinatorial problem on finite Abelian groups, I

## 定位

Olson 的这篇早期论文研究有限阿贝尔群中“任意足够长的元素序列都含有乘积为单位元的
非空子序列”的最小长度，并明确处理 p-群情形。该问题正是 Davenport 常数的乘法记号
版本。

## 本库实际使用

本库只使用其 p-群 Davenport 常数结果作为标准群论输入：若
\[
H\simeq C_{\ell^{a_1}}\oplus\cdots\oplus C_{\ell^{a_r}},
\]
则
\[
D(H)=1+\sum_i(\ell^{a_i}-1).
\]
这使共享 Type II 选择器可以把生成子群阶阈值 \(|H|\) 收紧为精确的 p-primary
零积阈值。具体的 Erdős--Straus 应用、子积构造和算术提升均由本仓库独立实现和验证，
不归因于 Olson 论文。

## 证据边界

本轮核对了出版社元数据、DOI、卷期页码和摘要；尚未取得可供逐式复核的原文 PDF。
因此文献卡标为 verified_with_caveat，新主张卡把公式作为经典定理输入，并单独
保存仓库内的指数恢复、动态子积构造和 10M 回放证据。
