---
kind: claim
claim_id: type-I-small-b-tail-deflation-profile
title: 小 B 小缺口 Type I 严格递降的两千万剖面
statement: 对所有 p<=2*10^7、p=1 mod24，完整枚举 m<=239、B<=4 的 Type I 正规形，并只保留规范 p-尾可严格去缩放的证书。158595 个核心素数中有156239个命中，首命中 B 的频数为 B=1:153784、B=2:969、B=3:1332、B=4:154；余2356个未在该盒内命中。该递降分支正是完整平方因子外部 source 递降的受限坐标切片，不是新机制。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- external-source
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-certificate-equivalence
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-25'
---

# 小 B 小缺口 Type I 严格递降的两千万剖面

## 审计

对每个核心素数，完整枚举

\[
3\le m\le239,\quad m\equiv3\pmod4,\quad 1\le B\le4,
\]

以及每个 \(A\mid x/B\)、\((A,B)=1\)，其中 \(x=(p+m)/4\)。除 Type I 条件
\(m\mid Bp+A\) 外，还要求由 [规范尾部递降选择器](type-I-normal-tail-deflation-selector.md)
给出的严格源整除条件。每个命中均直接核验源、目标的三个单位分数恒等式。

## 结果

| 项目 | 数值 |
|---|---:|
| 素数上界 | 20,000,000 |
| 核心素数 | 158,595 |
| 严格递降命中 | 156,239 |
| 盒内未命中 | 2,356 |

按联合选择器首次命中的 \(B\) 分类：

| \(B\) | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| 个数 | 153,784 | 969 | 1,332 | 154 |

因此，允许非最小但仍很小的 \(B\) 后，额外得到 2,455 条严格递降。代表性内部
\(B>1\) 见证为

\[
p=409,\quad (A,B,C,m)=(1,2,56,39),\quad n=392,
\]

以及

\[
p=1801,\quad (A,B,C,m)=(2,3,76,23),\quad n=1786.
\]

## 正确解释

这并不发现新的递降族。证书侧的规范尾去缩放与
[完整平方因子外部 source 递降](quadratic-factor-external-source-descent.md) 等价；这里的
贡献是将该已知机制压缩到 \(B\le4,m\le239\) 的一个小参数盒，并完整测量其覆盖。

与“先选最小 \(B\)”不同，联合选择器允许改选另一张证书。最小 \(B\) 证书本身可递降的
比例很低，但联合盒在相同有限参数内覆盖约 98.5%。这表明后续若研究这一机制，选择规则
必须同时考虑目标残数和源整除条件，而不能按 \(B\) 贪心。

仍有 2,356 个有限盒内遗漏，故这不是全称选择器，也不说明固定 \(B\) 或固定缺口有效。

## 重建

    python3 reproductions/type_i_small_b_tail_deflation_profile.py
    python3 -m unittest tests/test_type_i_small_b_tail_deflation_profile.py -q
