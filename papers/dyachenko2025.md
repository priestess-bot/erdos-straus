---
kind: paper
citation_key: dyachenko2025
title: Constructive Proofs of the Erdos-Straus Conjecture for Prime Numbers with P congruent to 1 modulo 4
authors:
- E. Dyachenko
year: 2025
first_publication_date: '2025-11-07'
publication_status: preprint
assessment_status: claim_with_gap
corpus_tier: A
reading_status: verified
language: en
source_pointer: https://arxiv.org/abs/2511.07465
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- proof-claim
- affine-lattice
- critical-gap
references:
- elsholtz_tao2013
- bradford2021
visibility: public
last_checked: '2026-07-23'
arxiv: '2511.07465'
---

# Constructive Proofs of the Erdos-Straus Conjecture for Prime Numbers with P congruent to 1 modulo 4

## 定位

声称用 ED2 仿射格构造证明每个 P=1 mod4 都有解；关键矩形命中命题的证明存在坐标耦合错误，因此当前不能视为完整证明。

## 主要贡献

- 给出 ED1/ED2 参数化和大量代数等价式。
- Theorem 9.21 声称无条件构造全体困难素数。
- 设计仿射格、窗口、卷积与反卷积算法。

## 证据与核查

- 已核对 Theorem 9.21、Lemmas 9.22-9.24、Proposition 9.25 及 Appendix D。
- Proposition 9.25 独立选择 u*、v* 的同余代表，却令 p=p0+m(d',d') 用同一个 m 同时命中两坐标；由 u 坐标确定的 m 并不保证 v 坐标等于独立选定的 v*。
- Lemma 9.24 把对角循环子群误等同于所有同时固定模 d' 的格点；一般缺少该等号。
- 其命题本身有最小反例：\(g=2,b'=c'=1\) 时 \(d'=1\)、\(L=\{u+v\equiv0\pmod2\}\)，但 \([0,1)\times[1,2)\) 不含格点，尽管两条边均为 \(d'\)。详见 `dyachenko-2025-lattice-gap`。

## 局限与后续

该缺口位于 Theorem 9.21 的存在性主链上；计算示例不能修补全称量词。
