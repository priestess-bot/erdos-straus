---
kind: claim
claim_id: type-II-h19-overflow-same-tail-deflation-profile
title: H19 高溢出偶源尾的同参数外部源分流
statement: 一个 r 偶源平方尾的同证书缩减当且仅当 r+1|p-1；它正是完整平方因子外部源的 q=r、k=(r+1)/4 分支。在十亿 H19 的91个高溢出首状态中70个满足该同参数外部源条件；31个纯复合状态中25个满足，剩余6个全部由 q!=r 的二次外部源严格递降闭合。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- overflow
- descent
- external-source
- normal-form
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: even-source-and-external-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# H19 高溢出偶源尾的同参数外部源分流

令一个偶源平方尾诱导的 Type I 正规形为

\[
x=ABC,\qquad e=B^2C,\qquad m=\frac{4e+1}{r}.
\]

通用正规尾缩减选择器中的商为

\[
R=\frac{4B^2C+1}{m}=r. \tag{1}
\]

表面上的同尾判据为

\[
r+1\mid4BC(A+B). \tag{2}
\]

但由 \(M=BC(rA-B)\)、\(4M=rp+1\)，这个条件模 \(r+1\) 精确化为

\[
r+1\mid p-1. \tag{3}
\]

因此它不依赖所选尾的 \(A,B,C\)：固定 \((p,r)\) 后，所有尾的同证书缩减性完全一致。
又 \(k=(r+1)/4\)、\(q=r\) 时，(3) 正是 \(k\mid(p-1)/4\)。故所谓“同尾缩减”
正是完整平方因子外部源的**同参数** \(q=r\) 分支，见
[偶源尾同证书缩减的 r 除子判据](odd-distance-even-source-same-tail-deflation-divisibility.md)。

满足时，令

\[
u=BC(Ar-B),\qquad n=\frac{4u}{r+1}; \tag{4}
\]

则 \(2\le n<p\)，并且保持该证书的前两个分母，有

\[
\frac4n=\frac1x+\frac1y+\frac1u,\qquad
\frac4p=\frac1x+\frac1y+\frac1{pu}. \tag{5}
\]

这只是 [Type I 正规形的规范尾部递降选择器](type-I-normal-tail-deflation-selector.md)
在偶源坐标的 \(R=r\) 特例，不是新的递降族。

## H19 剖面

将 (2) 逐张施加到十亿 H19 首 \(r\) 的完整高溢出尾表：

| 范围 | 状态数 | \(r+1\mid p-1\)（同参数外部源） | 需改选 \(q\ne r\) |
| --- | ---: | ---: | ---: |
| 全部高溢出 | 91 | 70 | 21 |
| 纯复合溢出 | 31 | 25 | 6 |

21 个同参数失败点的替代二次外部源首尺度 \(k\) 分布为

| \(k\) | 1 | 2 | 3 | 4 | 6 | 7 | 11 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 状态数 | 7 | 4 | 6 | 1 | 1 | 1 | 1 |

故在这一联合有限规则中，只有同参数外部源失败的 21 点才需改选 \(q\ne r\) 的外部源，且其所需尺度最大为
\(11\)，低于把所有 91 点都交给外部源时观察到的最大 \(20\)。对六个纯复合失败点，尺度
更只为 \(1,1,3,3,3,2\)。同时，这 21 点都另有半径至多 6 的直接 AC Type II 证书，见
[H19 同参数外部源失败的半径六直接 AC 证书](type-II-h19-same-r-failure-ac-profile.md)。
这是有限范围的参数压缩，不能宣称 \(k\le11\) 或半径 6 是一般选择器。

六个纯复合同参数未命中点为

\[
11{,}054{,}401,\ 20{,}958{,}961,\ 90{,}527{,}089,\ 113{,}509{,}489,\
540{,}645{,}121,\ 660{,}142{,}081.
\]

它们都仍有独立的完整平方因子外部源严格递降，所用 \(k\) 依次为
\(1,1,3,3,3,2\)。特别地，两个三支持复合状态中
\(p=26{,}410{,}609\) 满足 \(2352\mid p-1\)，故其唯一 \(B=735\) 尾落在 \(q=r\) 分支；
而 \(p=540{,}645{,}121\) 不满足 \(760\mid p-1\)，属于上述六点并需改选 \(q=11\)。
这严格排除了“复合支持必自动缩减”的过强说法，也把可证明的联合分流收缩为：当给定偶源
\(r\) 不满足 \(r+1\mid p-1\) 时，如何构造另一个允许的外部模数 \(q\)。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_overflow_tail_deflation_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --quadratic reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --output reproductions/type-ii-h19-overflow-tail-deflation-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_overflow_tail_deflation_profile.py -q
~~~
