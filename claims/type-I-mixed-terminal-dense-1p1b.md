---
kind: claim
claim_id: type-I-mixed-terminal-dense-1p1b
title: 十亿至十一亿连续核心区间的混合终端闭合
statement: 对1000000000<p<=1100000000的601660个核心素数，601416个具有完整普通 Type II p-1 双尾证书；其余244个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，未闭合点为零，最大首选缺口为159。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- terminal-bridge
- even-source
- descent
- mixed-selector
- finite-audit
- continuous-interval
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-29'
---

# 十亿至十一亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
1{,}000{,}000{,}000<p\le1{,}100{,}000{,}000,
\qquad p\equiv1\pmod {24},
\]

先穷尽每个 \(d\mid p-1\)、\(4\mid d\) 的普通 Type II 双尾条件。对遗漏点再按

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

枚举全部 Type I 正规形及其严格最大尾反向提升，并保留首个偶源。程序逐条重建
\(p^2E\)，核验

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R,\qquad 2\mid E.
\]

## 结果

| 分支 | 核心素数数目 |
| --- | ---: |
| 普通 Type II \(p-1\) 双尾 | 601,416 |
| Type I 正规形偶终端桥 | 244 |
| 未闭合 | 0 |
| 合计 | 601,660 |

因此有精确分流

\[
601{,}660=601{,}416_{\mathrm{Type\ II\ tail}}
+244_{\mathrm{Type\ I\ even\ terminal}}.
\]

244 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&71&79&87&107&111&119&159\\
\hline
\text{数量}&90&48&12&46&9&10&2&10&3&3&2&2&2&1&1&1&1&1
\end{array}
\]

该段最大缺口为 \(m=159\)，没有出现 \(m\le215\) 盒外遗漏。

## 十一亿以内的累计有限压力基准

与仓库已归档的 \(500\text{M}<p\le1\text{B}\) 五段连续审计合并，得到

\[
\begin{array}{c|r}
\text{对象}&\text{数量}\\ \hline
\text{核心素数}&3{,}663{,}744\\
\text{普通 Type II 命中}&3{,}662{,}315\\
\text{普通 Type II 遗漏}&1{,}429\\
\text{\(m\le215\) Type I 偶桥}&1{,}429\\
\text{未闭合}&0
\end{array}
\]

这仍是有限盒证据：首选缺口在前几段中从 95、111、159、183、215 等值之间波动，
不能解释为随 \(p\) 单调下降或上升。

## 结论边界

当前最关键的未解决问题是为 Type II 遗漏建立一个不依赖有限 \(m\) 截断的正规形
构造，或证明缺口可以沿某种严格递降势函数下降。若未来出现 \(m>215\) 或完全未闭合
点，应优先对其完整因子结构和所有一般 \(B\) 源做独立核验，而不是把它直接归因于
搜索截断。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \
  --lower-exclusive 1000000000 \
  --upper 1100000000 \
  --gap-cap 215 \
  --output reproductions/type-i-mixed-terminal-dense-1b-1p1b-results.json
~~~

结果文件：
[type-i-mixed-terminal-dense-1b-1p1b-results.json](../reproductions/type-i-mixed-terminal-dense-1b-1p1b-results.json)
