---
kind: claim
claim_id: type-II-small-r-p-minus-one-tail-deflation-closure
title: 小 r、p-1 缩放、偶源与 Type II 双尾抽缩的核心范围闭合
statement: p<=100000 的1181个核心素数中，小 r<=103 或 p-1 非倍数缩放覆盖1174个；其余七点中12601和97561由完整偶源距离提升闭合，余下五点由 Type II 双尾抽缩闭合，故该有限范围有四分支纯递降闭合1181=978+196+2+5。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- even-source
- scaled-source
- tail-deflation
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 小 \(r\)、\(p-1\) 缩放、偶源与 Type II 双尾抽缩的核心范围闭合

在 \(p\le100\,000\) 的 1,181 个核心素数上，四条严格递降分支给出有限分解：

\[
1181=978+196+2+5.
\]

前两项分别是完整见证复核的 \(r\le103\) 偶源提升和 \(p-1\) 非倍数缩放提升。
它们先留下七点；其中
\[
12\,601,\quad97\,561
\]
由完整奇距离偶源扫描在 \(c=1\) 闭合。其余五点为

\[
5\,209,\quad21\,169,\quad27\,481,\quad48\,409,\quad80\,809.
\]

每一点都有某个 Type II 证书，其两个被 \(p\) 整除的尾分母可同时除以 \(p\)，得到
严格更小源分母：

| \(p\) | 缺口 | 源分母 |
|---:|---:|---:|
| 5,209 | 11 | 435 |
| 21,169 | 35 | 589 |
| 27,481 | 7 | 3,436 |
| 48,409 | 7 | 6,052 |
| 80,809 | 3 | 20,203 |

因此五点排除的是先前两种偶源/缩放机制，而不是 Type II 双尾抽缩。该四分支闭合仍仅为
有限计算；它没有证明对全部核心素数必有可抽缩的 Type II 证书。

## 重建

~~~bash
python3 reproductions/type_ii_small_r_p_minus_one_tail_deflation_closure.py
python3 -m unittest tests/test_type_ii_small_r_p_minus_one_tail_deflation_closure.py -q
~~~
