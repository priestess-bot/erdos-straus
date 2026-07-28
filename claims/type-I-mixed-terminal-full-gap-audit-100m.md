---
kind: claim
claim_id: type-I-mixed-terminal-full-gap-audit-100m
title: 一亿以内无缺口上界的混合终端全审计
statement: 对 p<=100000000 的 719781 个核心素数，719281 个有普通 Type II p-1 双尾证书；余下 500 个逐项穷尽全部 3<=m<=p-2、m=3 mod4 的 Type I 目标除子 e|((p+m)/4)^2 及全部 E|4K^2，均找到偶终端桥，零未闭合点。该结果取消了这一范围内 Type I 分支的人为缺口上界，但仍是有限审计。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- mixed-selector
- full-gap
- terminal-bridge
- even-source
- exhaustive-finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-29'
---

# 一亿以内无缺口上界的混合终端全审计

## 审计定义

对每个核心素数

\[
p\le10^8,\qquad p\equiv1\pmod {24},
\]

先穷尽普通 Type II \(p-1\) 双尾条件。对普通分支遗漏，完全枚举

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,\qquad x=\frac{p+m}{4},
\]

以及所有目标侧除子 \(e\mid x^2\)，保留

\[
4e\equiv-1\pmod m,\qquad
R=\frac{4e+1}{m}\equiv3\pmod4,\qquad
K=xR-e.
\]

随后穷尽全部 \(E\mid4K^2\)，并验证

\[
E\equiv1\pmod R,\qquad 2\mid E,\qquad
E\le4K-2R.
\]

每个命中都重建 Type I 目标解和偶源解，逐项验证两个单位分数恒等式。

## 结果

| 分支 | 数量 |
| --- | ---: |
| 核心素数 | 719,781 |
| 普通 Type II \(p-1\) 双尾 | 719,281 |
| 普通双尾遗漏 | 500 |
| 无缺口上界 Type I 偶桥 | 500 |
| 未闭合 | 0 |

即

\[
719{,}781
=719{,}281_{\mathrm{ordinary\ Type\ II}}
+500_{\mathrm{Type\ I\ even\ terminal}},
\qquad
\text{unclosed}=0.
\]

Type I 分支没有预设 \(m\) 上界；每个遗漏均搜索到 \(p-2\)。500 个首个命中缺口的最大值为

\[
\max m=151.
\]

相对于一千万范围的 84 个遗漏，这次审计把无缺口闭合推进到一亿，并且没有出现首个结构性
反例。

## 结论边界

这仍然不是全称证明：

1. 素数范围仍截断在 \(10^8\)；
2. 普通分支仍取 \(p-1\) 双尾；
3. 计算使用完整因子分解，尚未给出无界的 \(e,E\) 构造规律。

它支持的最强判断是：当前障碍不是有限 \(m\)-盒遗漏，而是如何证明普通双尾失败时
源谱与目标谱必相交。下一阶段应把固定 \(R=7,E=8\) 等射线推广为可随 \(p\) 自适应的
因子状态选择，而不是继续把有限上界误作全称界。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_full_gap_audit_10m.py \
  --limit 100000000 \
  --output reproductions/type-i-mixed-terminal-full-gap-audit-100m-results.json
python3 -m unittest tests.test_type_i_mixed_terminal_full_gap_audit_100m -q
~~~

结果文件：
[type-i-mixed-terminal-full-gap-audit-100m-results.json](../reproductions/type-i-mixed-terminal-full-gap-audit-100m-results.json)
