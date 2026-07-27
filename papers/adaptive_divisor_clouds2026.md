---
kind: paper
citation_key: adaptive_divisor_clouds2026
title: Adaptive Divisor Clouds, Split-Capture Semigroups, and a Residual Closure Machine for the Erdos-Straus Equation
authors:
- Deep Bhattacharjee
year: 2026
first_publication_date: '2026-06-06'
publication_status: preprint
assessment_status: verified_with_caveat
corpus_tier: C
reading_status: verified
language: en
source_pointer: https://www.researchgate.net/publication/406177940_Adaptive_Divisor_Clouds_Split-Capture_Semigroups_and_a_Residual_Closure_Machine_for_the_Erdos-Straus_Equation
source_acquired: true
source_verified_against_original: true
source_verification_method: codex_audit
description_source: original
description_last_audit: '2026-07-23'
topics:
- short-certificate
- divisor-parametrization
- moving-window
- proof-program
- gray-literature
references: []
visibility: public
last_checked: '2026-07-23'
---

# Adaptive Divisor Clouds, Split-Capture Semigroups, and a Residual Closure Machine for the Erdos-Straus Equation

## 定位

作者上传至 ResearchGate 的预印本。它把核心素数的首分母缺口写为移动窗口

\[
A_j=4j-1,\qquad X_j=\frac{p+A_j}{4}=6t+j
\quad (p=24t+1),
\]

并把每个固定窗口的 Type II 搜索解释为 \(X_j^2\) 的除子在模 \(A_j\) 下命中
\(-X_j\) 的问题。

## 已核对的数学内容

- Theorem 2.2 的 split-capture 因子式与本库的 Type II 恢复公式一致。
- Lemma 3.1 在 \(\gcd(A,X)=1\) 时推出配对除子具有同一残数；这正是
  gap-residue-reachability 中用配对除子自动满足 \(d\le X\) 的论证。
- Theorem 5.1 的移动窗口只是令缺口 \(m=A_j\) 后的上述固定缺口判据，未给出新的
  全称存在性定理。
- 作者报告 \(J=20\) 的有限实验；本库的独立精确扩展到 \(p\le10^7\) 时发现
  \(p=8{,}803{,}369\) 未被 \(J=20\) 命中，而 \(J=27\) 在该范围内全覆盖，见
  moving-window-type-II-audit。

## 关键缺口

文中 Conjecture 13.1 断言存在固定 \(J_0\)，使每个
\(p=24t+1\) 在某个 \(1\le j\le J_0\) 命中该 Type II 除子条件。若成立，这正是

\[
H(p)=4J_0-1
\]

的统一有界 Type II 短证书命题；Theorem 13.2 只证明该猜想会蕴含
Erdos--Straus 猜想。作者在 Remark 13.3 明确承认它仍是该方法的 final hinge，
没有提供该饱和定理或可替代的递降。

因此文稿的无条件部分是可用的固定缺口重述和有限证书框架；它不证明本项目所需的
“短证书或递降”引理。
