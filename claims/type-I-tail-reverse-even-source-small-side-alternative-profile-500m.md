---
kind: claim
claim_id: type-I-tail-reverse-even-source-small-side-alternative-profile-500m
title: 五亿同状态大侧残余由替代 Type I 正规形全部释放
statement: 五亿普通 Type II 双尾遗漏的1717条 Type I 偶源终端记录中，95条在已选正规形的同一L=2K、R状态内没有小侧普通除子对。对这95条逐一完整枚举m<=215的所有 Type I 正规形及严格偶源反向桥后，95条全部有替代的小侧a<b桥；合并同状态小侧剖面，1717条全部在该有限盒内存在小侧终端桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- even-source
- divisor-pairs
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-divisor-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿同状态大侧残余由替代 Type I 正规形全部释放

[小侧普通除子对剖面](type-I-tail-reverse-even-source-small-side-profile-500m.md)留下 95 条记录：
它们的**已选**正规形中，完整枚举同一 \(L=2K,R\) 的因子对仍没有 \(a<b\) 的桥。这里
重新选择正规形，而不是把这 95 条误当作全局大侧障碍。

对每个点完整枚举

\[
3\le m\le215,\qquad m\equiv3\pmod4,
\]

中的全部 Type I 正规形与严格最大尾偶源反向边，保留满足

\[
\frac E{2K}=\frac ab,\qquad a<b
\]

的桥。每个候选同时以精确分数核验目标和偶源两条单位分数恒等式。

## 结果

| 项目 | 数值 |
| --- | ---: |
| 同状态大侧残余输入 | 95 |
| 替代正规形小侧桥命中 | 95 |
| 遗漏 | 0 |
| 完整检查的正规形 | 3,993 |
| 完整检查的严格反向边 | 7,493 |
| 合并后有小侧桥的终端记录 | 1,717 |

首个点 \(p=67369\) 原先选中的同状态大侧为

\[
(R,L,E,a,b)=(87,2930552,4726276,1087,674).
\]

在另一张正规形

\[
(m,A,B,C)=(119,74,3,76)
\]

中，得到

\[
(R,K,E,a,b,n)=(23,387372,24,1,32281,67368),
\]

这是一个小侧 \(a<b\) 的 \(p-1\) 终端桥。

## 含义与边界

在这组完整有限数据中，桥大小预算可以从最终 Type I 选择问题中完全移除：每个点都能选择
小侧普通除子对。真正未解决的全称问题因而是，如何对任意核心素数选择一个 Type I 正规形，
使其 \(L=2K\) 有互素因子 \(a,b\) 满足 \(a<b\)、\(a\equiv2b\pmod R\) 及偶性条件，
或直接给出普通 Type II 双尾。

这是 \(p\le5\cdot10^8,m\le215\) 的有限重选结果；它既不提供统一缺口界，也不证明
全局混合终端选择引理。

重建命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_small_side_alternative_profile.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_small_side_alternative_profile.py -q
~~~
