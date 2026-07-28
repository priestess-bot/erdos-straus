---
kind: claim
claim_id: type-I-mixed-terminal-dense-700m
title: 六亿至七亿连续核心区间的混合终端闭合
statement: 对600000000<p<=700000000的615520个核心素数，615303个具有完整普通 Type II p-1 双尾证书；其余217个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。重建的每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，实际最大首选缺口为131。因此该连续区间在明确的有限 Type I 盒内逐点满足混合终端析取，未闭合点为零。
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

# 六亿至七亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
600{,}000{,}000<p\le700{,}000{,}000,
\qquad p\equiv1\pmod {24},
\]

先穷尽每个 \(d\mid p-1\)、\(4\mid d\) 的普通 Type II 双尾条件。若该分支遗漏，则按

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

的顺序枚举每一张 Type I 正规形及其所有严格最大尾反向提升，保留首个偶源。

对每条 Type I 记录，程序从原始正规形、目标三元组、反向提升和偶源三元组重建桥除子
\(p^2E\)，并逐项核验

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R,\qquad 2\mid E.
\]

## 结果

| 分支 | 核心素数数目 |
| --- | ---: |
| 普通 Type II \(p-1\) 双尾 | 615,303 |
| Type I 正规形偶终端桥 | 217 |
| 未闭合 | 0 |
| 合计 | 615,520 |

因此有精确分流

\[
615{,}520=615{,}303_{\mathrm{Type\ II\ tail}}
+217_{\mathrm{Type\ I\ even\ terminal}}.
\]

217 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&63&71&79&87&131\\
\hline
\text{数量}&78&36&15&42&9&13&3&2&2&2&2&3&5&2&2&1
\end{array}
\]

最大首选缺口为

\[
p=690{,}400{,}489,\qquad m=131.
\]

该点在第 19 张正规形、第二条严格反向提升处得到偶源；它不是未闭合点。

## 结论边界

这次连续区间审计把此前 \(500\text{M}<p\le600\text{M}\) 的有限闭合向前推进了
100M，并且没有发现 \(m\le215\) 盒内的混合终端反例。它仍不是全称证明：Type I 分支
明确受 \(m\le215\) 限制，未检查更大的正规形缺口，也没有给出 \(m\) 的统一理论上界。

因此当前最直接的下一步是继续把连续区间推进到 \(700\text{M}\) 以上，同时单独研究
为什么回退缺口在这些区间保持有限，以及能否把“首个偶源”改造成无界的正规形选择或
严格递降命题。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \
  --lower-exclusive 600000000 \
  --upper 700000000 \
  --gap-cap 215 \
  --output reproductions/type-i-mixed-terminal-dense-600m-700m-results.json
~~~

结果文件：
[type-i-mixed-terminal-dense-600m-700m-results.json](../reproductions/type-i-mixed-terminal-dense-600m-700m-results.json)
