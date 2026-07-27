---
kind: paper
citation_key: audige_divisor_lattice2026
title: An Erdos-Straus divisor-lattice construction for 4/n
authors:
- Salomon Emmanuel Audige Youmbi
year: 2026
first_publication_date: '2026-01-25'
publication_status: preprint
assessment_status: claim_with_gap
corpus_tier: C
reading_status: verified
language: en
source_pointer: https://zenodo.org/records/18481651
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-24'
topics:
- proof-claim
- divisor-lattice
- greedy-algorithm
- proof-audit
- gray-literature
references: []
visibility: public
last_checked: '2026-07-24'
doi: 10.5281/zenodo.18481651
---

# An Erdos-Straus divisor-lattice construction for 4/n

## 定位

Zenodo 的 2026 年预印本。PDF 本文标题为 *A Greedy Divisor-Lattice Approach to
Egyptian Expansions of 4/n*。它令 \(L_n=\operatorname{lcm}(1,\ldots,n)\)、
\(D_n=\{d:d\mid L_n\}\)、\(T=4L_n/n\)，并试图把 \(T\) 写成三个 \(D_n\) 中元素之和，
从而给出三个都整除 \(L_n\) 的分母。

## 已核对的代数

若 \(d,e,f\in D_n\) 且 \(d+e+f=T\)，取

\[
x=L_n/d,\qquad y=L_n/e,\qquad z=L_n/f
\]

确实有 \(4/n=1/x+1/y+1/z\)。论文的 \(n=10\) 表项

\[
T=1008=840+140+28,\qquad (x,y,z)=(3,18,90)
\]

由此直接复核无误。

## 主链缺口

Section 2 定义 \(u_x(n)\) 前，必须先证明存在 \(d,e,f\in D_n\) 满足

\[
d+e+f=T. \tag{1}
\]

但 Lemma 2 仅从 \(T\) 为整数和 \(1\in D_n\) 宣称该集合非空；这些事实并不推出 (1)。
精确等价关系见 `audige-divisor-lattice-completion-equivalence`：该非空性本身就是
一个受限三项单位分数存在命题，不能作为立即引理使用。

Section 8 的 Proposition 4 也没有补上这一步：其构造先选取已定义的 \(u_x(n)\)，并最终
要求 \(T-u_x(n)\) 正好是两个 \(D_n\) 元素之和。这正是定义 \(u_x(n)\) 时尚未证明的
完成条件。一个泛泛的 \(4A_n\) 的多项除子分割并不指定其包含和为 \(T\) 的三项子分割。

因此本文的有限例子和恒等式可以核验，但“对每个 \(n\)”的核心非空性没有被证明，不能
用于当前的短证书或递降引理。
