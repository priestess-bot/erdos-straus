---
kind: claim
claim_id: type-I-mixed-terminal-full-gap-audit-10m
title: 一千万以内无缺口上界的混合终端全审计
statement: 对 p<=10000000 的 82887 个核心素数，82803 个有普通 Type II p-1 双尾证书；余下 84 个逐项穷尽全部 3<=m<=p-2、m=3 mod4 的 Type I 目标除子 e|((p+m)/4)^2 及全部 E|4K^2，均找到偶终端桥，零未闭合点。该结果取消了这一范围内 Type I 分支的人为缺口上界，但仍是有限审计。
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
- negative-boundary
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

# 一千万以内无缺口上界的混合终端全审计

## 审计定义

对每个核心素数

\[
p\le10^7,\qquad p\equiv1\pmod {24},
\]

先检查普通 Type II \(p-1\) 双尾分支：穷尽每个 \(d\mid p-1\)、\(4\mid d\)，并验证
相应的 \(d\mid x^2\) 除子残数。

若普通分支失败，则**不设 Type I 缺口上界**，逐项枚举

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,\qquad x=\frac{p+m}{4}.
\]

对每个 \(m\)，穷尽所有目标侧除子 \(e\mid x^2\)，保留满足

\[
4e\equiv-1\pmod m,\qquad
R=\frac{4e+1}{m}\equiv3\pmod4,\qquad
K=xR-e.
\]

随后穷尽 \(E\mid4K^2\)，并要求

\[
E\equiv1\pmod R,\qquad 2\mid E,\qquad
E\le4K-2R.
\]

每个命中都由[目标除子与偶终端桥双因子等价](type-I-target-divisor-even-terminal-selector.md)
重新构造目标与源的两个单位分数恒等式。

## 结果

| 分支 | 数量 |
| --- | ---: |
| 核心素数 | 82,887 |
| 普通 Type II \(p-1\) 双尾 | 82,803 |
| 普通双尾遗漏 | 84 |
| 无缺口上界 Type I 偶桥 | 84 |
| 未闭合 | 0 |

因此该有限范围有精确分流

\[
82{,}887
=82{,}803_{\mathrm{ordinary\ Type\ II}}
+84_{\mathrm{Type\ I\ even\ terminal}},
\qquad
\text{unclosed}=0.
\]

84 个普通双尾遗漏的 Type I 搜索不是 \(m\le215\) 之类的盒，而是完整范围
\(3\le m\le p-2\)。实际首个命中缺口的最大值为

\[
\max m=71.
\]

这给出当前最强的“有限无缺口上界”证据：在一千万以内，没有发现依赖更大 \(m\) 才能闭合的
普通双尾遗漏，也没有发现原混合终端析取的反例。

## 结论边界

该结果仍然不是全称证明，原因有三：

1. 核心素数范围被截断在 \(10^7\)；
2. 普通分支固定为 \(p-1\) 双尾；
3. 计算依赖完整因子分解，尚未给出随 \(p\) 有效的构造规则。

它排除了“当前 \(m\le215\) 闭合只是盒子太小”这一解释，并把下一步重点推进到：

- 从 \(p\) 的因子状态直接构造一个无需扫描 \(m\) 的 \(e,E\) 对；
- 证明普通双尾失败时，源谱 \(\mathcal R_{\rm src}(p)\) 与目标谱
  \(\mathcal R_{\rm tgt}(p)\) 必有交；
- 或在该无缺口审计中继续向更高的 \(p\) 推进，以寻找首个真正的结构性反例。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_full_gap_audit_10m.py
python3 -m unittest tests.test_type_i_mixed_terminal_full_gap_audit_10m -q
~~~

结果文件：
[type-i-mixed-terminal-full-gap-audit-10m-results.json](../reproductions/type-i-mixed-terminal-full-gap-audit-10m-results.json)
