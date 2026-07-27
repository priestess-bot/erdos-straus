---
kind: claim
claim_id: type-I-mixed-terminal-dense-600m
title: 五亿至六亿连续核心区间的混合终端闭合
statement: 对500000000<p<=600000000的621951个核心素数，621704个具有完整普通 Type II p-1 双尾证书；其余247个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。重建的正规形桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，实际最大首选缺口为111。因此该完整连续区间逐点满足目标混合终端析取，未闭合点为零。
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
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿至六亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
500{,}000{,}000<p\le600{,}000{,}000,
\qquad p\equiv1\pmod {24},
\]

先穷尽每个 \(d\mid p-1\)、\(4\mid d\) 的普通 Type II 双尾条件。若该分支遗漏，
则按

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

的顺序枚举每一张 Type I 正规形及其所有严格最大尾反向提升，保留首个偶源。

对一张选中的正规形 \((A,B,C)\)，写

\[
mR=4B^2C+1,\qquad H=AR-B,\qquad K=BCH,
\]

并将反向提升的桥除子写成 \(p^2E\)。测试对每条记录重新检查

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R,\qquad 2\mid E. \tag{1}
\]

所以回退支不是仅有“某个较小源”的标记：它正是当前目标要求的 Type I 偶终端桥。

## 结果

| 分支 | 核心素数数目 |
| --- | ---: |
| 普通 Type II \(p-1\) 双尾 | 621,704 |
| Type I 正规形偶终端桥 | 247 |
| 未闭合 | 0 |
| 合计 | 621,951 |

因而有逐点不交分流

\[
621{,}951=621{,}704_{\mathrm{Type\ II\ tail}}
+247_{\mathrm{Type\ I\ even\ terminal}}. \tag{2}
\]

尽管 Type I 搜索允许 \(m\le215\)，在本连续区间中实际最大首选缺口只是

\[
m=111.
\]

所有 247 条桥均存有原始正规形、目标三元组、偶源三元组和桥因子；测试逐条从这些数据
重建 (1) 和源恒等式，而不是只比较汇总计数。

## 边界

式 (2) 是比先前稀疏族更强的**连续区间**有限审计，但仍然不是全称混合终端选择引理：
第二分支明确受 \(m\le215\) 限制，且两支都从目标 \(p\) 的实际因子状态作选择。它的价值在于：
在已有五亿全体闭合之外，未发现该有限 Type I 盒的首个反例；同时它把下一次寻找反例的
优先区域推进到六亿以上，而不把高覆盖率误写为归纳规则。

可复现命令：

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py
python3 -m unittest tests/test_type_i_mixed_terminal_dense_interval.py -q
~~~
