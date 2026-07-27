---
kind: claim
claim_id: type-II-h19-pure-new-marked-tail-bridge-profile
title: 纯新标记尾遗漏的独立双尾高缺口压力谱
statement: 对十亿范围、移位20<=s<=1008的541个 H19 纯新标记尾状态，211个标记遗漏精确分为210个独立普通 Type II 双尾严格递降和1个自适应外源严格递降。210个普通尾中194个最小缺口 m<=23、206个 m<=63；仅16个有 m>23，最大为171。这是固定有限剖面的替代分支压力谱，不是从纯新失败推出替代递降的一般定理。
claim_status: computationally_reproduced
topics:
- type-II
- pure-new-factor
- marked-solution
- strict-descent
- external-source
- finite-audit
- h19
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-II-certificate-and-tail-lift-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# 纯新标记尾遗漏的独立双尾高缺口压力谱

这张卡片把三个已经分别精确复核的有限存档作集合交叉：

1. [纯新规范证书的缩放首项标记尾在十亿 H19 状态中的边界](type-II-h19-pure-new-scaled-tail-mark-boundary-1b.md) 给出移位
   \(20\le s\le1008\) 中没有同证书标记尾的 211 个状态；
2. [H19 十亿残余的双尾递降加两点 AC 闭合](type-II-h19-tail-deflation-short-closure.md) 给出不受该纯新窗口约束的最小普通 Type II 双尾；
3. [H19 十亿残余的全严格递降闭合](type-II-h19-all-strict-descent-closure.md) 给出普通双尾遗漏的外源严格递降。

结果是无交叠的有限分流

\[
211=210_{\text{独立普通 Type II 双尾}}+1_{\text{自适应外源}}. \tag{1}
\]

唯一外源点为

\[
p=225289,\qquad (k,q,g)=(2,7,41),\qquad n=197128. \tag{2}
\]

这里的“独立”只表示该普通双尾的缺口由完整 \(p-1\) 因子搜索选出，未要求它来自纯新
规范窗口中的同一张证书。每个源、目标恒等式已经在其原始审计中用精确有理数验证；本卡的
复现器重新检查三份表的集合分割和记录一致性。

## 缺口压力谱

210 个独立双尾的最小缺口 \(m\) 的统计为

\[
194_{m\le23}+12_{23<m\le63}+4_{m>63}=210. \tag{3}
\]

因此如果已知的小缺口机制覆盖 \(m\le23\)，这一交叉后的有限压力集只余 16 个
\(m>23\) 的状态；若把阈值扩至 63，则只余四个。阈值 23 是诊断切片，不是新的理论界。
完整直方图为

\[
\begin{array}{c|rrrrrrrrrrrrrrrrr}
m&3&7&11&15&19&23&27&35&39&43&47&59&63&71&119&135&171\\
\hline
\#&62&62&43&9&9&9&3&2&1&2&1&2&1&1&1&1&1.
\end{array} \tag{4}
\]

16 个高缺口记录如下。\(n\) 是该独立普通双尾的严格较小源，`divisor` 是其 Type II
证书除子，而非 \(m+1\)。

| \(m\) | \(p\) | \(n\) | divisor |
| ---: | ---: | ---: | ---: |
| 27 | 382,619,161 | 13,664,971 | 224,903 |
| 27 | 912,979,369 | 32,606,407 | 3,269 |
| 27 | 977,342,521 | 34,905,091 | 587,951 |
| 35 | 192,369,241 | 5,343,591 | 7,551 |
| 35 | 972,433,081 | 27,012,031 | 115,821 |
| 39 | 680,223,721 | 17,005,594 | 50 |
| 43 | 235,435,201 | 5,350,801 | 2,771 |
| 43 | 358,424,089 | 8,146,003 | 31,939 |
| 47 | 321,700,369 | 6,702,092 | 25,548 |
| 59 | 119,502,601 | 1,991,711 | 23,175 |
| 59 | 398,757,241 | 6,645,955 | 25 |
| 63 | 367,015,489 | 5,734,618 | 1,832 |
| 71 | 227,018,089 | 3,153,030 | 20 |
| 119 | 334,152,361 | 2,784,604 | 61,760 |
| 135 | 201,866,569 | 1,484,314 | 104 |
| 171 | 165,882,649 | 964,435 | 215 |

## 含义与限制

这完成了当前“纯新标记尾遗漏是否只是未闭合递降”的有限排查：不是。该剖面中的每个
遗漏都已有另一条严格递降，且绝大多数由小缺口普通双尾闭合。真正尚未解释的是为何纯新
窗口失败会**强制**出现这张替代证书，或在唯一外源模式处强制出现外源状态。

式 (1)--(4) 不能推出任何全称选择器。特别地，不能从“这 16 个有限高缺口点被列出”
推出某个统一的 \(m\le171\) 界，也不能把带标记的缩放首项提升当作普通归纳步骤。下一步的
可检验目标应是对这 16 个点的 \(p-1\) 因子、Type II 除子残数与纯新失败标签作符号分类，
寻找可证明的替代缺口分支，而不是继续扩大同证书标记搜索窗口。

## 复现

~~~bash
python3 reproductions/type_ii_h19_pure_new_marked_tail_bridge_profile.py \
  --marked-profile reproductions/type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json \
  --tail-profile reproductions/type-ii-h19-tail-deflation-short-closure-1b-results.json \
  --strict-closure reproductions/type-ii-h19-all-strict-descent-closure-1b-results.json \
  --output reproductions/type-ii-h19-pure-new-marked-tail-bridge-1b-results.json
python3 -m unittest tests/test_type_ii_h19_pure_new_marked_tail_bridge_profile.py -q
~~~
