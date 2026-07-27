---
kind: claim
claim_id: type-II-h19-bounded-r-even-split-boundary
title: H19 固定 r 残余的非标准偶分裂边界
statement: 在 r<=9999 未命中的15个 H19 残余上，156个兼容状态产生245条偶源射线，全部满足 p/2<n<p。对每条射线完整枚举 4/n=1/(n/2)+1/a+1/b 的非标准偶分裂及两分母保留提升，均无命中。因此这245条已知偶源不能用该最小的改标记分裂族闭合。
claim_status: computationally_reproduced
topics:
- descent
- even-source
- solution-lift
- egyptian-fractions
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-factorization-and-lift-context
visibility: public
last_checked: '2026-07-25'
---

# H19 固定 \(r\) 残余的非标准偶分裂边界

对 \(r\le9999\) 的 15 个平方尾残余，所有 156 个兼容状态共给出 245 条不同的偶源
射线 \(n=p-c\)。每条均满足

\[
\frac p2<n<p,\qquad 2\mid n.
\]

因而可完整枚举非标准偶分裂

\[
\frac4n=\frac1{n/2}+\frac1a+\frac1b,\qquad
(2a-n)(2b-n)=n^2,
\]

并对每个尾项应用精确的两分母保留提升判据。245 条射线均没有命中。

这排除了一个自然的替代方案：从已经找到的偶源射线出发，只改变一个尾项、保留
\(n/2\) 与另一个尾项，不能解除这 15 点在给定 \(r\) 盒内的平方尾障碍。

该结论不涉及其它偶数源 \(n\)、不含 \(n/2\) 的源解、一个分母保留提升，或多步和
非线性传递；它是这 245 条已知射线上的完整有限边界。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_tail_obstruction_profile.py
python3 reproductions/type_ii_h19_bounded_r_even_split_boundary.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_even_split_boundary.py -q
~~~
