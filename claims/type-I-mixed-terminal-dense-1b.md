---
kind: claim
claim_id: type-I-mixed-terminal-dense-1b
title: 九亿至十亿连续核心区间的混合终端闭合
statement: 对900000000<p<=1000000000的605085个核心素数，604862个具有完整普通 Type II p-1 双尾证书；其余223个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，未闭合点为零，最大首选缺口为183。
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

# 九亿至十亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
900{,}000{,}000<p\le1{,}000{,}000{,}000,
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
| 普通 Type II \(p-1\) 双尾 | 604,862 |
| Type I 正规形偶终端桥 | 223 |
| 未闭合 | 0 |
| 合计 | 605,085 |

因此有精确分流

\[
605{,}085=604{,}862_{\mathrm{Type\ II\ tail}}
+223_{\mathrm{Type\ I\ even\ terminal}}.
\]

223 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&67&71&75&83&95&135&143&183\\
\hline
\text{数量}&89&35&12&38&9&10&3&8&1&4&2&1&4&1&2&1&1&1&1
\end{array}
\]

该段最大缺口为 \(m=183\)，未出现 \(m\le215\) 盒外遗漏。

## 十亿以内的累计有限压力基准

将本段与仓库已归档的 \(500\text{M}<p\le900\text{M}\) 四段连续审计合并，得到

\[
\begin{array}{c|r}
\text{对象}&\text{数量}\\ \hline
\text{核心素数}&3{,}062{,}084\\
\text{普通 Type II 命中}&3{,}060{,}899\\
\text{普通 Type II 遗漏}&1{,}185\\
\text{\(m\le215\) Type I 偶桥}&1{,}185\\
\text{未闭合}&0
\end{array}
\]

这不是把有限搜索升级为定理：五段 Type I 分支都明确受 \(m\le215\) 限制，且首选缺口在
95、111、183、215 等值之间波动。它只说明在十亿以内的连续压力层中，尚未找到这个
有限 Type I 盒的反例。

## 结论边界

下一阶段的关键问题不是继续宣称“高覆盖率证明猜想”，而是解释为什么 Type II 遗漏的
因子结构会在某个有限或可递降的正规形缺口上产生偶桥；否则仍可能在更大范围出现
\(m>215\) 或完全未闭合的核心素数。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \
  --lower-exclusive 900000000 \
  --upper 1000000000 \
  --gap-cap 215 \
  --output reproductions/type-i-mixed-terminal-dense-900m-1b-results.json
~~~

结果文件：
[type-i-mixed-terminal-dense-900m-1b-results.json](../reproductions/type-i-mixed-terminal-dense-900m-1b-results.json)
