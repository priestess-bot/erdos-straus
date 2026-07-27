---
kind: claim
claim_id: type-II-h19-hybrid-bounded-r-p-minus-one-descent
title: H19 十亿残余的受控 r 或 p-1 缩放严格递降闭合
statement: 在存储的 p<=10^9 H19 残余中，r<=9999 的兼容偶源严格递降覆盖649个；剩余15个恰由 p-1 的 b=2,4 非倍数缩放严格递降覆盖。因此该有限剖面有严格递降闭合664=649+15。
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

# H19 十亿残余的受控 \(r\) 或 \(p-1\) 缩放严格递降闭合

在存储的 \(p\le10^9\) H19 残余剖面中，按

\[
r\equiv7\pmod8,\qquad r\le9999
\]

枚举兼容偶源因子对和完整平方尾，严格递降覆盖 649 个残余。其余集合与
\(p-1\) 非倍数缩放源审计的输入集合逐项相同；后者的 \(b=2,4\) 候选对 15 点全数
给出严格提升及 Type I 证书。因此此有限剖面有另一种纯递降分解：

\[
664=649+15.
\]

它不应与“存在统一 \(r\le9999\) 选择器”混同。第二分支是 Type I 证书的一个受限
参数化，且只在当前存储残余上验证；证明全称结论仍须控制 \(r\) 的增长，或强制存在
满足 \(p-1\) 归一化条件的证书。

## 重建

~~~bash
python3 reproductions/type_ii_h19_hybrid_bounded_r_p_minus_one_descent.py
python3 -m unittest tests/test_type_ii_h19_hybrid_bounded_r_p_minus_one_descent.py -q
~~~
