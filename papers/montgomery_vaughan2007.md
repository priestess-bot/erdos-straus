---
kind: paper
citation_key: montgomery_vaughan2007
title: 'Multiplicative Number Theory I: Classical Theory'
authors:
- Hugh L. Montgomery
- Robert C. Vaughan
year: 2006
first_publication_date: '2006-11-16'
publication_status: book
assessment_status: verified
corpus_tier: B
reading_status: verified
language: en
source_pointer: https://personal.science.psu.edu/rcv4/568s20/568chapter11.pdf
published_chapter_pointer: https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/15.0_pp_358_396_Primes_in_arithmetic_progressions_II.pdf
bibliographic_pointer: https://www.cambridge.org/core/books/multiplicative-number-theory-i/4E45519B26115AEEA4839C6C38206ACD
source_acquired: true
source_verified_against_original: true
source_verification_method: manual_grep
description_source: original
description_last_audit: '2026-07-27'
topics:
- analytic-number-theory
- primes-in-arithmetic-progressions
- siegel-walfisz
references: []
visibility: public
last_checked: '2026-07-27'
doi: 10.1017/CBO9780511618314
series: Cambridge Studies in Advanced Mathematics 97
source_acquired_at: '2026-07-27'
source_distribution_status: local_research_only
source_files:
- filename: montgomery-vaughan-chapter11.pdf
  sha256: ac6f71e606b929007cf337d6edbbd00d8e09e06ee15a96304f27270dbaf00f55
  role: author-hosted-course-version
- filename: montgomery-vaughan-mnti-chapter11.pdf
  sha256: 7675e6bc45e7f03a292ecef13832f652a6acb395d10d4ac43c119f384953ef03
  role: author-hosted-published-chapter
---

# Multiplicative Number Theory I: Classical Theory

## 用途

这是一份解析数论方法学来源，不是 Erdős--Straus 专题文献。这里核验的是
第 11 章算术级数中的素数分布，尤其是正式章节版印刷页 381--382 的
Corollaries 11.19 与 11.21（Siegel--Walfisz theorem 及其
\(\vartheta,\pi\) 版本）。

## 原文结论

Corollary 11.19 固定任意 $A>0$。当

$$
q\le (\log x)^A,\qquad (a,q)=1,
$$

时，存在绝对常数 $c_1>0$，使

$$
\psi(x;q,a)=\frac{x}{\varphi(q)}
+O_A\!\left(x\exp\!\left(-c_1\sqrt{\log x}\right)\right).
$$

原文紧接着说明，$\vartheta(x;q,a)$ 与 $\pi(x;q,a)$ 有相应估计；正式章节版
印刷页 382 的 Corollary 11.21 随后明确写出这两个版本。

## 取得与核验

- 2026-07-27 取得题示的 Robert C. Vaughan 作者域课程版章节 PDF。
  该版本在印刷页 376 写作 ``Corollary 19``，并在印刷页 378 以
  ``Corollary 21`` 写出 \(\vartheta,\pi\) 版本。
- 同日从 Vaughan 的个人出版页取得正式 Cambridge 章节 PDF。该版本覆盖
  印刷页 358--396，在印刷页 381 写作 ``Corollary 11.19``，并在印刷页 382
  写作 ``Corollary 11.21``。
- 两个文件的 SHA-256 已分别写入 frontmatter 和来源清单。PDF 仅作本地研究
  核验，未判断具有公开再分发许可。

## 书目核验

Cambridge University Press 的书目页列出作者 Hugh L. Montgomery、
Robert C. Vaughan，纸本出版日 2006-11-16，丛书
*Cambridge Studies in Advanced Mathematics* 第 97 卷，以及 DOI
`10.1017/CBO9780511618314`。部分参考文献习惯记作 2007；本卡保留建议的
兼容 citation key `montgomery_vaughan2007`，但 `year` 与
`first_publication_date` 采用出版社记录的 2006 年纸本首发信息。

## 本库中的边界

该来源支持在 $q\le(\log x)^A$ 范围内统一使用 Siegel--Walfisz 估计。
把它用于某个随参数增长的筛问题时，仍须在仓库推导中单独证明具体模数确实
落入这一范围；本书结论本身不提供 Erdős--Straus 的证书或例外集为空结论。
