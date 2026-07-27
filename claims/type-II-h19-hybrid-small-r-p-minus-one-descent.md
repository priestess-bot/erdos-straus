---
kind: claim
claim_id: type-II-h19-hybrid-small-r-p-minus-one-descent
title: H19 十亿残余的小 r 或 p-1 缩放严格递降闭合
statement: 在存储的 p<=10^9 H19 残余中，r<=103 的兼容偶源严格递降覆盖564个；其余100个均由 p-1 的 b=2,4 非倍数缩放严格递降覆盖。因此该有限剖面有严格递降闭合664=564+100，且 r 上界可从9999降至103。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- scaled-source
- p-minus-one
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

# H19 十亿残余的小 \(r\) 或 \(p-1\) 缩放严格递降闭合

在存储的 \(p\le10^9\) H19 残余剖面中，按

\[
r\equiv7\pmod8,\qquad r\le103
\]

枚举兼容偶源因子对和完整平方尾，严格递降覆盖 564 个残余。对余下 100 个素数，
完整枚举源 \(n=p-1\) 的 \(an/2\)、\(an/4\) 候选及其强制平方尾；每点至少有一个
严格提升，且每个见证均以精确有理数和 Type I 证书复核。故有更强的有限纯递降分解：

\[
664=564+100.
\]

流式分块审计共检查 10,046 个去重候选、97,636,776 个尾因子组合，记录 723 个命中。
它保留每个目标的首个见证并避免因子枚举缓存随范围累积。
它仍不证明统一 \(r\le103\) 选择器，也不证明每个核心素数均有 \(p-1\) 缩放证书；
但把此前 \(r\le9999\) 的有限析取收紧到小 \(r\) 析取。

## 重建

~~~bash
python3 reproductions/type_ii_h19_hybrid_small_r_p_minus_one_descent.py
python3 -m unittest tests/test_type_ii_h19_hybrid_small_r_p_minus_one_descent.py -q
~~~
