---
kind: claim
claim_id: type-II-h19-bounded-r-residual-three-split-boundary
title: H19 固定 r 残余的 n/3 残余分裂边界
statement: 在 r<=9999 未命中的15个 H19 残余的245条偶源射线中，101条满足 3|n 且 p/4<n/3<=p/2。对这101条射线完整枚举保留 n/3 的所有残余分裂 4/n=1/(n/3)+1/a+1/b 及两分母保留提升，均无命中。因此该自然 n/3 改标记分裂不能闭合给定射线盒。
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

# H19 固定 \(r\) 残余的 \(n/3\) 残余分裂边界

对固定 \(r\) 残余给出的 245 条偶源 \(n=p-c\)，其中 101 条满足

\[
3\mid n,\qquad \frac p4<\frac n3\le\frac p2.
\]

它们恰处于保留 \(n/3\) 后目标首分母自然可恢复短证书的范围。对每条源完整枚举

\[
\frac4n=\frac1{n/3}+\frac1a+\frac1b,\qquad
(a-n)(b-n)=n^2,
\]

并对两个尾分母逐一应用两分母保留提升判据，101 条均无命中。

所以在当前射线盒内，\(n/2\) 的非标准偶分裂和 \(n/3\) 的残余分裂都不能绕开平方尾
障碍。\(n\) 作为固定首分母则不在 \(p/4<x\le p/2\) 的自然短证书范围内。

这不排除其它源 \(n\)、不固定首分母的源解、保留一个分母并重组两项，或多步非线性
提升；结论仅覆盖这 101 条适用射线。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_tail_obstruction_profile.py
python3 reproductions/type_ii_h19_bounded_r_residual_three_split_boundary.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_residual_three_split_boundary.py -q
~~~
