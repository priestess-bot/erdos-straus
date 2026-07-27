---
kind: claim
claim_id: type-I-mixed-terminal-dense-b1-600m
title: 六亿连续新区间尾遗漏的 B=1 偶终端闭合
statement: 对500000000<p<=600000000的247个普通 Type II p-1 双尾遗漏，完整枚举m<=215、B=1的 Type I 正规形及严格最大尾反向提升后，247个全部有偶源终端桥，未闭合点为零。最大首选缺口为131，点p=550528729达到该值。因此B=1在这个连续新区间足够，但结合p<=500000000中B=1的十个遗漏，B需求不随p单调增长，也不是全称选择律。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- normal-form
- even-source
- terminal-bridge
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿连续新区间尾遗漏的 \(B=1\) 偶终端闭合

从[五亿至六亿连续核心区间的混合终端闭合](type-I-mixed-terminal-dense-600m.md)提取全部
\(247\) 个普通 Type II \(p-1\) 双尾遗漏。对每个点穷尽

\[
3\le m\le215,\qquad m\equiv3\pmod4,\qquad B=1
\]

的 Type I 正规形和每张正规形的所有严格最大尾反向提升；只接受偶源，并逐条检查

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-2R,\qquad 2\mid E.
\]

结果是

\[
247=247_{B=1\ \mathrm{even\ terminal}}+0_{\mathrm{miss}}. \tag{1}
\]

在这条受限选择器中，首选缺口的最大值为

\[
p=550{,}528{,}729,\qquad m=131.
\]

这不能提升为 \(B=1\) 的全称猜想：在 \(p\le500{,}000{,}000\) 的对应审计中，\(B=1\)
已有十个明确遗漏，且需要最高 \(B=8\) 才闭合。新的区间结果只说明低溢出需求既不由
“最早偶源”的 \(B\) 值决定，也不随目标素数单调增长；因此 \(B\) 本身不适合做未证明
递降的单调势函数。

可复现命令：

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_b1_profile.py
python3 -m unittest tests/test_type_i_mixed_terminal_dense_b1_profile.py -q
~~~
