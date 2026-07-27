---
kind: claim
claim_id: type-II-automatic-residual-k-one-funnel
title: 四自动缺口残余到 k=1 与 k>1 共享证书的精确漏斗
statement: 在 p<=10^7 的四自动共享缺口 m=3,7,11,23 未命中的 973 个核心素数中，889 个仍有 k=1 的 p-1 因子 Type II 选择器；其余 84 个恰为 k=1 选择器的全部范围残余。对这 84 个点，m<=239 的无界首尺度共享因子扫描全部找到 k>1 的 Type II 证书。故当前有限压力集可精确缩为 84 个非 k=1 共享因子实例；这仍只是带标记证书选择，不构成无标记递降。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- k-one
- residual-funnel
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 四自动缺口残余到 \(k=1\) 与 \(k>1\) 共享证书的精确漏斗

## 两层选择器

对共享因子 \(D\mid p+m\)、\(D\equiv1\pmod m\)，令

\[
k=\frac{D-1}{m}. \tag{1}
\]

\(k=1\) 等价于 \(D=m+1\)，也就是

\[
m+1\mid p-1. \tag{2}
\]

这正是 `type-II-tail-deflation-selector-audit` 的 \(p-1\) 因子选择器。若 (2)
失败但仍有 \(k>1\)，它给出的是 `type-II-scaled-first-tail-deflation` 的带标记
表示，不能被当作从任意较小实例开始的递降。

## 精确有限漏斗

先以 `type-II-shared-gap-23-automatic-fan` 的四自动缺口

\[
m\in\{3,7,11,23\}
\]

筛掉直接 Type II 命中。再对其残余完整枚举 \(p-1\) 的因子，以及所有
\(m\le239\) 中 \(p+m\) 的共享因子。

```bash
python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
  --limit 10000000 --gap-cap 239
```

对 \(p\le10^7\)，得到

\[
82{,}887
\longrightarrow973
\longrightarrow889+84
\longrightarrow84\text{ 个 }k>1\text{ 证书}. \tag{3}
\]

更精确地：

\[
\begin{array}{c|r}
\text{阶段}&\text{核心素数个数}\\
\hline
\text{四自动缺口未命中}&973\\
\text{其中有某个 \(k=1\) Type II 选择器}&889\\
\text{其中无 \(k=1\) 选择器}&84\\
\text{这 84 个有 \(m\le239\) 的 \(k>1\) 共享证书}&84
\end{array} \tag{4}
\]

这 84 个点与 `type-II-tail-deflation-selector-audit` 的一千万范围 \(k=1\)
遗漏完全一致；它们不是“尚无 Type II 证书”的点，而是“无法由 \(D=m+1\) 解释”的
最小有限压力集。

## 研究意义

因此下一条真正新的选择定理不必重新覆盖所有核心素数。一个更聚焦的目标是：

\[
\text{对每个 \(k=1\) 残余核心素数，构造某个 }D=km+1\mid p+m
\text{ 与同缺口 Type II 除子。} \tag{5}
\]

有限审计表明 \(k\) 不能预先取固定小常数，但没有否定随 \(p\) 增长或由
\(p+m\) 的特定因子形状选择 \(k\) 的可能性。证明 (5) 仍必须使用实际因子分解和
跨缺口关联；它不能从带标记提升本身推出无标记归纳。

同样不能把 Type II 正规形的 \(A\) 预先取小常数：
`type-II-shared-small-a-boundary` 在这个 84 点压力集中的 \(p=878089\) 给出
全缺口反例，最小 \(A\) 已为 \(69\)。
