---
kind: claim
claim_id: type-II-h19-bounded-r-selector-boundary
title: H19 十亿残余的固定 r 偶源选择器边界
statement: 在存储的 664 个 p<=10^9 H19 残余上，仅用 r=7 mod8 的偶源兼容因子对和 M1^2 平方尾，r<=103 覆盖564点、r<=999 覆盖640点、r<=9999 覆盖649点，分别留下100、24、15点。因此 r=103 只能是四个标准递降压力点的有限补丁，不能作为整个 H19 剖面的固定选择器。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- selector
- congruences
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿残余的固定 \(r\) 偶源选择器边界

在 H19 十亿残余的全部 664 个素数上，扫描必要的状态类

\[
r\equiv7\pmod8
\]

并对每个兼容因子对及

\[
M_1=\frac{rp+1}{4},\qquad
e_1\mid M_1^2,\quad e_1\le M_1,\quad e_1\equiv-M_1\pmod r
\]

进行精确检验。按三个常数截面，得到：

| \(r\) 上界 | 覆盖数 | 未覆盖数 |
|---:|---:|---:|
| 103 | 564 | 100 |
| 999 | 640 | 24 |
| 9,999 | 649 | 15 |

这严格否定“\(r\le103\) 是 H19 残余的统一偶源选择器”。此前的
\(r\le103\) 结论只针对标准平方因子递降的四个遗漏，因而仍完全有效；它不能被外推到
另外 660 点。

即使上界升至 9,999，仍保留

\[
\begin{split}
&3361,\ 252001,\ 345601,\ 685969,\ 1385521,\ 8243041,\ 8328961,\ 24887641,\\
&99532801,\ 117710401,\ 131053729,\ 399299209,\ 453770689,\ 731024641,\ 749224921.
\end{split}
\]

因此下一条全称引理不能只给出一个未经证明的固定 \(r\) 常数；它必须解释 \(r\) 的增长、
处理该 15 点的特殊因子结构，或者与另一条证书/递降机制组合。这仍是有限实验边界，
不排除每个点在更大的 \(r\) 出现命中。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_selector_boundary.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_selector_boundary.py -q
~~~
