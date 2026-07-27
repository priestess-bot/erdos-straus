---
kind: claim
claim_id: type-II-h19-hybrid-small-r-descent
title: H19 十亿标准递降或受控 r 偶源递降闭合
statement: 在存储的 p<=10^9 H19 残余剖面中，664点里660点有完整平方因子外部源严格递降；其余四点均由 r<=103 的偶源严格递降闭合，首个 r 为103、31、31、15。每条源解、目标解和 Type I 证书均以精确有理数复核，故该有限剖面有纯严格递降闭合664=660+4，且第二分支使用受控 r 而非固定距离。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- external-source
- selector
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿标准递降或受控 r 偶源递降闭合

先对每个 H19 残余尝试完整平方因子外部源严格递降。它在十亿范围命中 660 点。对其余
四点，不把距离作为选择参数，而扫描

\[
r\equiv3\pmod4,\qquad r\le103,
\]

从 \(rp+1=(cr+1)(dr+1)\) 恢复偶源，并逐项构造

\[
\frac4{p-c}=\frac1{dM_1}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{pM_1}+\frac1u+\frac1v.
\]

每条严格提升均以精确有理数复核。结果为

\[
664=660+4. \tag{1}
\]

| \(p\) | \(r\) | \(c\) | \(d\) |
|---:|---:|---:|---:|
| 35,840,809 | 103 | 7 | 49,641 |
| 132,285,169 | 31 | 3 | 1,407,289 |
| 141,326,089 | 31 | 3 | 1,503,469 |
| 640,775,689 | 15 | 34,091 | 1,253 |

这比“短证书或递降”的混合闭合更强：有限剖面中的每一点都已有严格更小源分母。它也比
固定小距离结论更准确：第四点距离很大，但尾参数仍很小。

式 (1) 是存储剖面的有限审计，不是全称定理。待证明的选择器仍须从 H19 与标准递降的
共同失败，强制某个受控 \(r\) 的兼容因子对和平方尾命中。

## 重建

~~~bash
python3 reproductions/type_ii_h19_hybrid_small_r_descent.py
python3 -m unittest tests/test_type_ii_h19_hybrid_small_r_descent.py -q
~~~
