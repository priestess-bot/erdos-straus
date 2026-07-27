---
kind: claim
claim_id: type-II-shared-residue-fixed-gap-boundary
title: 共享除子残数选择器的固定缺口耦合边界
statement: 核心素数 p=73 在合法缺口 m=47、x=(p+m)/4=30 处同时不满足共享因子条件 1 属于 Pi_m^{>1}(4x)，也不满足 Type II 目标条件 -x 属于 Pi_m(x^2)。所以共享残数选择器不能由“每个预定缺口自动命中”的单缺口命题证明；任何充分路线都必须主动选择缺口，或使用不同移位 p+m 之间的关联。该例不否定存在另一个缺口使 p=73 命中。
claim_status: established
topics:
- type-II
- divisor-residues
- shared-divisor
- fixed-gap
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 共享除子残数选择器的固定缺口耦合边界

## 精确例子

取

\[
p=73,\qquad m=47,\qquad x=\frac{p+m}{4}=30.
\]

这里 \(p\equiv1\pmod {24}\)、\(m\equiv3\pmod4\)，且
\(3\le m\le p-2\)，故这是共享除子残数选择器允许的一个真实核心素数缺口。

先看 Type II 目标。因为

\[
x^2=2^2 3^2 5^2,\qquad -x\equiv17\pmod {47},
\]

其全部除子残数为

\[
\Pi_{47}(x^2)=
\{1,2,3,4,5,6,7,9,10,12,13,15,18,20,25,27,28,30,36,37,39,43,45\}.
\]

这个集合不含 \(17\)，所以固定缺口 \(m=47\) 没有 Type II 证书。

再看共享因子标记。由于

\[
4x=120=2^3\cdot3\cdot5,
\]

它的非平凡正除子为

\[
2,3,4,5,6,8,10,12,15,20,24,30,40,60,120.
\]

它们模 \(47\) 都不等于 \(1\)。故

\[
1\notin\Pi_{47}^{>1}(4x),\qquad
-x\notin\Pi_{47}(x^2). \tag{1}
\]

复现命令为

```bash
python3 reproductions/shared_residue_fixed_gap_boundary.py
python3 -m unittest tests/test_shared_residue_fixed_gap_boundary.py -v
```

## 对证明设计的限制

式 (1) 并不反驳 `type-II-shared-residue-selector-conjecture`，因为后者只要求
**存在**一个合法缺口；\(p=73\) 在其它缺口仍可有证书。它排除的更窄而常见的推理跳跃是：
先固定一个 \(m\)，再企图从 \(x=(p+m)/4\) 的除子乘积集的抽象增长，自动同时推出两个
目标残数。

因此，下一条可证明的中间引理必须含有真正的跨缺口内容，例如对一个随 \(p\) 选择的
合法缺口族 \(\mathcal M(p)\)，证明至少一个 \(m\in\mathcal M(p)\) 满足两个目标。
`divisor-residue-subgroup-exception-boundary` 已排除了对任意单一除子序列作普适
次线性结构压缩；本例进一步表明，即使保留 \(p\equiv1\pmod {24}\) 与
\(p=4x-m\)，也不能把“某一固定缺口的命中”作为无条件起点。

## 研究接口

最有希望利用的额外信息是不同缺口的移位整数

\[
p+m_1,\ p+m_2,\ldots
\]

两两相差固定的事实，以及 \(p\) 本身为素数。单个 \(p+m\) 的任意因子残数模式可以很坏；
证明必须显示这些坏模式无法在一个足够灵活、随 \(p\) 选择的缺口族上同时持续。
