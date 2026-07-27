---
kind: claim
claim_id: type-I-overflow-gap-tradeoff-100m
title: 一亿小溢出压力点的外部 source 缺口代价
statement: 在 p<=10^8、m<=239 的 Type I 最小正规形剖面中，恰有11个核心素数需要 B>1，且 B 属于 {2,3,4}。对这11点完整搜索 B=1 的外部 source 证书至 m<=999，全部恢复，首个 B=1 缺口最大为775。此为有限的溢出-缺口比较，不推出任何统一 B=1 缺口界。
claim_status: computationally_reproduced
topics:
- type-I
- external-source
- normal-form
- divisor-selector
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-divisor-certificate-equivalence
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-25'
---

# 一亿小溢出压力点的外部 source 缺口代价

## 问题

[小 B 正规形剖面](type-I-small-b-normal-form-profile.md) 在
\(p\le10^8,m\le239\) 中留下 11 个没有 \(B=1\) 证书、却有 \(B\in\{2,3,4\}\)
证书的点。这里比较两种不同的修复方式：

- 固定较短缺口范围，允许目标平方除子有小溢出 \(B=e/(e,x)>1\)；
- 坚持 \(B=1\)，即只在 \(x\) 的普通除子中寻找目标残数，但允许更远缺口。

对每个压力点，逐个扫描 \(m=3\pmod4\) 至 999，并完整枚举 \(x=(p+m)/4\) 的除子
\(e\)，检查 \(e\equiv-1/4\pmod m\)。每个命中都通过 \(B=1\) 正规形重建和有理数
恒等式核验。

## 结果

| \(p\) | 短缺口最小 \(B\) | 该证书的 \(m\) | 首个 \(B=1\) 缺口 |
|---:|---:|---:|---:|
| 1,282,009 | 2 | 71 | 583 |
| 3,364,561 | 2 | 63 | 323 |
| 4,962,049 | 3 | 23 | 247 |
| 16,337,281 | 4 | 159 | 355 |
| 17,307,721 | 3 | 23 | 255 |
| 20,377,729 | 2 | 23 | 299 |
| 31,807,441 | 2 | 23 | 335 |
| 38,559,481 | 2 | 47 | 263 |
| 42,193,321 | 2 | 207 | 775 |
| 64,210,441 | 2 | 23 | 279 |
| 99,762,601 | 3 | 119 | 359 |

故 11/11 均在 \(m\le999\) 恢复 \(B=1\)，最大首次缺口为 775。

## 研究含义

这个有限现象将当前 Type I 路线拆成可比较的两个变量：缺口大小和目标除子的溢出
\(e/(e,x)\)。它支持研究一个**自适应二择一选择律**：当短窗口中普通除子不命中时，
要么某个短缺口有低溢出目标除子，要么较远但可控制的缺口恢复普通除子命中。

这比“固定 \(B\)”或“固定缺口扇”更符合已知边界：固定窗口的完整 Type I 条件本身有
条件性逃逸，所以任何全称结果必须让至少一个变量随状态更新。该表也不能说明二者存在
单调代价关系，例如不能从 \(B=2\) 推出首个 \(B=1\) 缺口的统一上界。

## 重建

    python3 reproductions/type_i_overflow_gap_tradeoff.py
    python3 -m unittest tests/test_type_i_overflow_gap_tradeoff.py -q
