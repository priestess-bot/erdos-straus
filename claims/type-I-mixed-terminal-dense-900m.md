---
kind: claim
claim_id: type-I-mixed-terminal-dense-900m
title: 八亿至九亿连续核心区间的混合终端闭合
statement: 对800000000<p<=900000000的607985个核心素数，607750个具有完整普通 Type II p-1 双尾证书；其余235个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，未闭合点为零，最大首选缺口为95。
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

# 八亿至九亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
800{,}000{,}000<p\le900{,}000{,}000,
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
| 普通 Type II \(p-1\) 双尾 | 607,750 |
| Type I 正规形偶终端桥 | 235 |
| 未闭合 | 0 |
| 合计 | 607,985 |

因此有精确分流

\[
607{,}985=607{,}750_{\mathrm{Type\ II\ tail}}
+235_{\mathrm{Type\ I\ even\ terminal}}.
\]

235 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&63&67&71&79&95\\
\hline
\text{数量}&89&45&24&33&11&3&2&9&3&3&3&2&1&5&1&1
\end{array}
\]

该段最大缺口为 \(m=95\)，没有出现新的盒边界或未闭合点。

## 结论边界

该区间把有限连续覆盖推进到 900M，仍未发现 \(m\le215\) 盒内的混合终端反例。
与上一段 700M–800M 出现的 \(m=215\) 峰值相比，本段最大缺口回落到 95；因此首选
缺口既不随 \(p\) 单调增加，也不能直接作为严格递降势函数。

这仍然不是全称证明：Type I 分支受 \(m\le215\) 限制，且区间实验没有解释为什么
缺口在所有核心素数上必有有限上界。后续应优先研究普通 Type II 遗漏的因子结构与
Type I 正规形 \(m\) 之间的可证明映射，而不是只依赖更高的数值上界。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \
  --lower-exclusive 800000000 \
  --upper 900000000 \
  --gap-cap 215 \
  --output reproductions/type-i-mixed-terminal-dense-800m-900m-results.json
~~~

结果文件：
[type-i-mixed-terminal-dense-800m-900m-results.json](../reproductions/type-i-mixed-terminal-dense-800m-900m-results.json)
