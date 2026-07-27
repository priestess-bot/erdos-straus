---
kind: paper
citation_key: shute2022
title: 'Existence and density problems in Diophantine geometry: From norm forms to Campana points'
authors:
- Alec Shute
year: 2022
first_publication_date: '2022-09-01'
publication_status: thesis
assessment_status: verified
corpus_tier: B
reading_status: verified
language: en
source_pointer: https://research-explorer.ista.ac.at/download/12072/12073
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-24'
topics:
- sieve
- fundamental-lemma
- beta-sieve
references: []
visibility: public
last_checked: '2026-07-24'
source_sha256: 3d94509fd7a0cf0c55c02a4616f5e8d0b105949e4718a4c88d271e6f4c47cbf9
---

# Existence and density problems in Diophantine geometry

## 用途

这是一份方法学来源，不是 Erdős--Straus 专题论文。第 5.5 节以明确的
筛维 $\kappa$、正则性常数 $K$ 和 $s=\log D/\log z$ 表述基本筛引理：
若 $s\ge9\kappa+1$，上界筛主项相对筛积的误差为
$e^{9\kappa-s}K^{10}$，外加截断余项。

## 本库中的作用

`type-II-growing-canonical-fan-superlog-tail` 使用该引理处理随 $H$ 增长的
规范 Type II 扇。关键不是把筛维当作固定常数，而是显式令
$s\gg H^2$，吸收该问题的 $K=\exp(O(H^2))$。因此它给出可核查的增长扇
密度结论，但不处理筛法的奇偶障碍，也不产生逐点证书。

## 核查

- 已取得 ISTA 官方存档的 2022 年博士论文并核对第 5.5 节、Lemma 5.5.1。
- 该引理在论文中归因于标准 Brun/Rosser--Iwaniec 筛理论；本库只使用其明确陈述，
  不把论文的几何数论结果移植到本问题。
