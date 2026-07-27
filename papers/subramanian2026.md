---
kind: paper
citation_key: subramanian2026
title: Observations of the Erdos-Straus conjecture
authors:
- Pradhyumnaa Ganapathi Subramanian
year: 2026
first_publication_date: '2026-07-19'
publication_status: preprint
assessment_status: verified_with_caveat
corpus_tier: C
reading_status: verified
language: en
source_pointer: https://zenodo.org/records/21442607
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-24'
topics:
- classical-identities
- congruence-classes
- reduction
- proof-boundary
- gray-literature
references:
- erdos1950
- salez2014
- elsholtz_tao2013
visibility: public
last_checked: '2026-07-24'
doi: 10.5281/zenodo.21442607
---

# Observations of the Erdos-Straus conjecture

## 定位

2026 年 7 月的 Zenodo 预印本。本文整理偶数、\(n\equiv3\pmod4\)，以及
\(n\equiv5\pmod8\) 的显式三项分解，并明确说明其方法对
\(n\equiv1\pmod8\) 的素数没有结论。

## 已核对的内容

Section 2 的缩放恒等式和 \(n=8k+5\) 族

\[
\frac4{8k+5}
=\frac1{2k+2}
+\frac1{(8k+5)(k+1)}
+\frac1{2(8k+5)(k+1)}
\]

可直接验证。文中对合数的缩放约化也正确：若 \(d\mid n\) 且 \(4/d\) 有三项解，
把三个分母乘以 \(n/d\) 即给出 \(4/n\) 的解。

## 对当前目标的边界

作者在 Remark 2.5 和结论中明确留下 \(n\equiv1\pmod8\) 的素数。对当前核心类，

\[
p\equiv1\pmod{24}\quad\Longrightarrow\quad p\equiv1\pmod8,
\]

故本文没有覆盖任何尚未由标准约化排除的核心素数，不能给出短证书或递降选择器。
它的价值是把该经典约化边界透明地记录为已验证的公式，而不是提出完整证明。
