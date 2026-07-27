---
kind: paper
citation_key: roy_hgdd2026
title: On the Hybrid-Greedy Diophantine Descent for Arbitrary-Length Egyptian Fraction Partitioning
authors:
- Sayantan Roy
year: 2026
first_publication_date: '2026-07-06'
publication_status: preprint
assessment_status: contradicted
corpus_tier: C
reading_status: verified
language: en
source_pointer: https://www.researchgate.net/publication/408484884_On_the_Hybrid-Greedy_Diophantine_Descent_for_Arbitrary-Length_Egyptian_Fraction_Partitioning-Generalizing_the_Erdos-Straus_Conjecture_via_Hybrid-Greedy_Diophantine_Descent_A_Rigorous_Approach_to_mn_Pa
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-24'
topics:
- greedy-algorithm
- exact-length
- two-unit-fractions
- contradicted-claim
- gray-literature
references: []
visibility: public
last_checked: '2026-07-24'
doi: 10.13140/RG.2.2.35011.57121
---

# On the Hybrid-Greedy Diophantine Descent for Arbitrary-Length Egyptian Fraction Partitioning

## 定位

Roy 的 2026 年 7 月 ResearchGate 预印本提出 HGDD：先作贪心单位分数分解，
再在终端用二项单位分数的因子分解，并用拆分恒等式增加项数。它把这一程序宣称为
任意真分数、任意规定项数的构造，因此也把 Erdős--Straus 三项问题视为其中的特例。

## 审计结论

二项方程

\[
\frac{m'}{n'}=\frac1u+\frac1v
\]

确实等价于

\[
(m'u-n')(m'v-n')=n'^2.
\]

但这只在存在因子 (D\mid n'^2) 且 (D\equiv-n'\pmod {m'}) 时给出正整数解；
它不对所有 (0<m'<n') 自动成立。论文从该因子式跳到无条件终端求解器的步骤错误。

具体地，对 (p=73)，首个贪心分母为 (19)，余项为 (3/1387)。因

\[
1387=19\cdot73\equiv1\pmod3,
\]

(1387^2) 的每个正因子均为 (1\pmod3)，却要求

\[
D\equiv-1387\equiv2\pmod3.
\]

故该余项没有二项单位分数分解。本库的 greedy-one-step-terminal-obstruction 给出
完整反例和证明。

## 对本计划的影响

贪心算法可以保证有限长度的通常展开，但不能保证在指定三项处终止，也没有给出
可用于短证书或递降状态图的全称提升边。因此这份稿件只作为一个已反驳的尝试保留，
不作为任何正向结论的来源。
