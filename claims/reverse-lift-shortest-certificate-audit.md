---
kind: claim
claim_id: reverse-lift-shortest-certificate-audit
title: 最短证书的二分母保留反向提升在万级核心素数中稀少
statement: 对所有 \(p\le10000\) 的143个核心素数，先取其最小缺口 Bradford Type I/II 证书，再对该目标三元组的每个坐标穷尽 \(2\le n<p\) 的二分母保留反向提升。仅 \(p=193,1201\) 的最短证书存在此类提升，共3条；每条都替换目标三元组的最大分母。因此真实读取源解的提升确实存在，但不能从最短证书或固定低复杂度反向模板中期待密集覆盖。
claim_status: computationally_reproduced
topics:
- descent
- reverse-lift
- marked-solution
- type-I
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-25'
---

# 最短证书的二分母保留反向提升在万级核心素数中稀少

## 审计对象

对每个 \(p\equiv1\pmod{24}\)、\(p\le10000\)，先完整枚举自然缺口

\[
3\le m\le p-2,\qquad m\equiv3\pmod4
\]

并取第一个 Bradford Type I/II 证书

\[
\frac4p=\frac1x+\frac1y+\frac1z. \tag{1}
\]

然后逐一选择目标坐标 \(t\in\{x,y,z\}\)，以及每个 \(2\le n<p\)，检查是否存在正整数
\(a\) 使

\[
\frac4n=\frac1a+\sum_{w\in\{x,y,z\}\setminus\{t\}}\frac1w. \tag{2}
\]

这是二分母保留的一项替换提升的反向完全枚举。每个返回点都以精确有理数复核 (1)、(2)
和把 \(a\) 替换为 \(t\) 的目标恒等式。

## 精确结果

| 项目 | 数量 |
|---|---:|
| 核心素数 | 143 |
| 最短证书有反向提升的目标 | 2 |
| 全部反向提升边 | 3 |

完整记录仅为：

| \(p\) | 证书类型 | 缺口 | 被替换目标项 | 源 \(n\) | 源替换项 |
|---:|:---:|---:|---:|---:|---:|
| 193 | I | 7 | 1,331,700 | 192 | 9,200 |
| 1201 | I | 23 | 172,727,820 | 1,020 | 1,692 |
| 1201 | I | 23 | 172,727,820 | 1,200 | 359,550 |

例如第一条边为

\[
\frac4{192}
=\frac1{9200}+\frac1{50}+\frac1{1380}
\quad\Longrightarrow\quad
\frac4{193}
=\frac1{1331700}+\frac1{50}+\frac1{1380}. \tag{3}
\]

这与 [二分母保留一项替换判据](two-denominator-lift-criterion.md) 完全一致，但比单个局部
例子多出一个选择器校准：在最短证书截面中，真实读取源解的边并不常见。

## 含义与边界

这条审计不排除：

- 同一 \(p\) 的非最短证书；
- 保留一个而非两个源分母的提升；
- 更高维、非线性或多状态提升；
- 由专门构造的带标记源解产生的边。

所以它不是递降不可能性结论。它排除的仅是一种研究直觉：不能仅从“每个 \(p\) 有很短的
目标证书”推断该目标证书通常会反向暴露一个低复杂度、二分母保留的严格源。

后续若使用 [带标记解的严格递降闭包](marked-solution-descent-closure.md)，应直接构造
可闭合的源标记，而不是期望最短目标证书自动提供这类标记。

## 重建

```bash
python3 reproductions/reverse_lift_shortest_certificate_audit.py
python3 -m unittest tests/test_reverse_lift_shortest_certificate_audit.py -q
```
