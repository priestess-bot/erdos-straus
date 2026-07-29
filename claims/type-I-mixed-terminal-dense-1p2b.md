---
kind: claim
claim_id: type-I-mixed-terminal-dense-1p2b
title: 十一亿至十二亿连续核心区间的混合终端闭合
statement: 对1100000000<p<=1200000000的599267个核心素数，599047个具有完整普通 Type II p-1 双尾证书；其余220个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，未闭合点为零，最大首选缺口为95。普通 Type II 命中的最小缺口直方图尾部达到5843，故该审计不提供统一 Type II 短缺口上界。
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
- gap-boundary
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

# 十一亿至十二亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
1{,}100{,}000{,}000<p\le1{,}200{,}000{,}000,
\qquad p\equiv1\pmod {24},
\]

先穷尽每个 \(d\mid p-1\)、\(4\mid d\) 的普通 Type II 双尾条件。对普通尾遗漏点再按

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
| 普通 Type II \(p-1\) 双尾 | 599,047 |
| Type I 正规形偶终端桥 | 220 |
| 未闭合 | 0 |
| 合计 | 599,267 |

因此有精确分流

\[
599{,}267=599{,}047_{\mathrm{Type\ II\ tail}}
+220_{\mathrm{Type\ I\ even\ terminal}}.
\]

220 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&63&67&71&75&79&95\\
\hline
\text{数量}&79&39&10&43&11&10&6&9&1&3&1&3&1&1&1&1&1
\end{array}
\]

该段最大首选缺口为 \(m=95\)，没有出现 \(m\le215\) 盒外遗漏。

值得单独记录的是，普通 Type II 分支的最小 gap 直方图最大达到 \(5843\)。这说明普通
\(p-1\) 双尾虽然覆盖了绝大多数点，却不能被当前数据解释为一个统一的短缺口上界；Type I
回退的有限盒仍是另一条独立的证书机制。

## 十二亿以内的累计有限压力基准

与仓库已归档的 \(500\text{M}<p\le1.1\text{B}\) 六段连续审计合并，得到

\[
\begin{array}{c|r}
\text{对象}&\text{数量}\\ \hline
\text{核心素数}&4{,}263{,}011\\
\text{普通 Type II 命中}&4{,}261{,}362\\
\text{普通 Type II 遗漏}&1{,}649\\
\text{\(m\le215\) Type I 偶桥}&1{,}649\\
\text{未闭合}&0
\end{array}
\]

该累计结论仍是有限盒证据：它没有排除未来出现 \(m>215\) 或完全未闭合的核心素数，
也没有给出对普通 Type II 最小 gap 的统一上界。

## 结论边界

当前最需要的理论工作是解释普通尾遗漏的因子结构如何必然产生一个有限或可递降的 Type I
正规形缺口。若把 gap 截断去掉，必须证明一个与 \(p\) 无关的构造界，或给出严格下降势函数；
否则本页只能作为截至十二亿的可复现实验压力基准。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \\
  --lower-exclusive 1100000000 \\
  --upper 1200000000 \\
  --gap-cap 215 \\
  --output reproductions/type-i-mixed-terminal-dense-1p1b-1p2b-results.json
~~~

结果文件：
[type-i-mixed-terminal-dense-1p1b-1p2b-results.json](../reproductions/type-i-mixed-terminal-dense-1p1b-1p2b-results.json)
