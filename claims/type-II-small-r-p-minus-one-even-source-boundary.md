---
kind: claim
claim_id: type-II-small-r-p-minus-one-even-source-boundary
title: 小 r 与 p-1 联合残余的完整偶源距离边界
statement: 在 p<=100000 的小 r/p-1 联合残余七点上，完整枚举所有奇距离偶源后，仅12601和97561在距离1有严格提升；5209、21169、27481、48409、80809在所有0<c<p的标准偶源上均失败。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- p-minus-one
- boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 3
  role: even-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 小 \(r\) 与 \(p-1\) 联合残余的完整偶源距离边界

小 \(r\le103\) 和 \(p-1\) 非倍数缩放的联合审计在 \(p\le100\,000\) 留下七点。对每一点，
完整枚举所有奇距离

\[
0<c<p,\qquad n=p-c,
\]

并运行完整标准偶源严格提升构造，而非只检查尾部残数。该构造逐项验证源、目标的
三单位分数恒等式与 Type I 证书。

仅有
\[
p=12\,601,\quad97\,561
\]
在 \(c=1\) 有命中（对应 \(r=119\)）。其余五点
\[
5\,209,\quad21\,169,\quad27\,481,\quad48\,409,\quad80\,809
\]
对全部奇距离都没有这种严格提升。总共进行了 91,538 次距离检查。

因此，后续不能仅提高标准偶源的距离上界；这五点同时排除了当前的小 \(r\)、\(p-1\)
缩放和**完整标准偶源距离**三条分支。它们不是猜想反例，仍可能有其它 Type I/II
证书、非标准源或不同尾部模型。

## 重建

~~~bash
python3 reproductions/type_ii_small_r_p_minus_one_even_source_boundary.py
python3 -m unittest tests/test_type_ii_small_r_p_minus_one_even_source_boundary.py -q
~~~
