---
kind: claim
claim_id: type-II-h19-bounded-r-overflow-profile
title: H19 十亿残余首个 r 尾命中的 Type I 溢出分布
statement: 在存储的 664 个 p<=10^9 H19 残余中，r<=9999 的首个偶源尾命中覆盖649点。其最小 Type I 目标除子溢出 B=1 的有558点，余91点需要 B>1，最小溢出最大为4563（p=605553001,r=311）。故变量 r 的零溢出偶源选择器在该有限剖面上已不成立；任何正向势量还必须处理高溢出状态或将其转入其它递降。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- normal-form
- overflow
- selector
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# H19 十亿残余首个 \(r\) 尾命中的 Type I 溢出分布

对存储的 664 个 \(p\le10^9\) H19 残余，沿既有 \(r\equiv7\pmod8\)、
\(r\le9999\) 审计的**首个**尾命中，重新穷尽该状态的 \(M_1^2\) 残数因子。每个尾因子
经

\[
g=\frac{4e+1}{r},\qquad x=\frac{M_1+e}{r},\qquad B=\frac{e}{(e,x)}
\]

归一化为一个 Type I 正规形溢出。649 点在给定 \(r\) 窗口内有首命中，15 点仍无命中。

最小溢出的主分布为：

| 最小 (B) | 点数 |
| ---: | ---: |
| 1 | 558 |
| 2 | 20 |
| 3 | 11 |
| 4 | 14 |
| 5 或更大 | 46 |

因此零溢出在已闭合首命中中占多数，但不是全称规律：91 点的最小 \(B>1\)。最大实例为

\[
p=605553001,\qquad r=311,\qquad \min B=4563,
\]

且该状态只含一个尾命中。故不能把四个压力点的 \(B=1\) 现象升级为“变量 \(r\) 的零溢出
选择器”。同样，数据也不支持一个未经证明的很小固定 \(B\) 上界。

这给出下一势量的最低要求：除了记录首个 \(r\)，还必须量化最小溢出 \(B\) 的大小、素支撑或
可通过替代尾/替代源降低的程度。可行的正向命题应证明高 \(B\) 会强制另一条短证书、一个可读
源状态，或某种跨距离碰撞饱和；单独追求 \(B=1\) 已被这份有限剖面排除。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_bounded_r_overflow_profile.py \
  --input reproductions/type-ii-h19-bounded-r-selector-boundary-1b-results.json \
  --output reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_bounded_r_overflow_profile.py -q
~~~
