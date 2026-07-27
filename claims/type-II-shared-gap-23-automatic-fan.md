---
kind: claim
claim_id: type-II-shared-gap-23-automatic-fan
title: 缺口 23 的自动共享因子及九类 Type II 子扇
statement: 对每个核心素数 p=24t+1，m=23 都有自动共享因子 D=24，因为 p+23=24(t+1)。令 x=(p+23)/4=6(t+1)。当 p 模23 属于 7,10,11,15,17,19,20,21,22 时，x^2 的强制除子 1,2,3,4,6,9,12,18,36 中有一个同余于 -x 模23，因而给出共享 Type II 证书。与完整 m=3,7,11 扇合并的精确审计至 10^7 捕获 81914 个核心素数，留下 973 个。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- congruences
- small-gap
- factor-selection
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

# 缺口 \(23\) 的自动共享因子及九类 Type II 子扇

## 自动共享条件

令 \(p=24t+1\)。对 \(m=23\)，

\[
p+23=24(t+1),\qquad
x_{23}=\frac{p+23}{4}=6(t+1). \tag{1}
\]

所以

\[
24\mid p+23,\qquad24\equiv1\pmod {23}. \tag{2}
\]

即 \(D=24\) 对每个核心素数都是共享因子；问题只剩 Type II 目标
\(-x_{23}\pmod {23}\)。

## 九类显式证书

模 \(23\) 中 \(6^{-1}=4\)，故若强制除子 \(d\mid6^2\) 满足

\[
p\equiv-4d\pmod {23}, \tag{3}
\]

就有 \(d\equiv-x_{23}\pmod {23}\)。表为：

\[
\begin{array}{c|ccccccccc}
d&1&2&3&4&6&9&12&18&36\\
\hline
p\bmod23&19&15&11&7&22&10&21&20&17
\end{array} \tag{4}
\]

因此表中九个核心剩余类有共享 Type II 证书。它们的最小正
\(p\equiv1\pmod {24}\) 代表元依次为

\[
433,337,241,145,505,217,481,457,385\pmod {552};
\]

故相应 \(x_{23}\) 均至少为 \(42\)，特别是 (4) 中最大的 \(d=36\) 也满足
\(d\le x_{23}\)。

## 与前三缺口合并的精确审计

```bash
python3 reproductions/type_ii_shared_gap_23_profile.py --limit 10000000
```

先完整检查 \(m=3,7,11\) 的 Type II 除子，再检查 \(m=23\)。对
\(82{,}887\) 个核心素数，分割为

\[
\begin{array}{c|r}
\text{类别}&\text{个数}\\
\hline
\text{前三缺口已有 Type II}&80{,}162\\
\text{\(m=23\) 的表 (4) 命中}&1{,}064\\
\text{\(m=23\) 的其它除子命中}&688\\
\text{四缺口均未命中}&973
\end{array} \tag{5}
\]

所以这四个自动共享缺口已经捕获

\[
81{,}914/82{,}887=98.8261\%\text{（四舍五入）}. \tag{6}
\]

这是有限审计，不是四缺口全称覆盖。其意义在于：在 \(m=23\) 前，额外共享条件
仍然完全消失，剩余的 \(973\) 个点是研究下一个非自动共享缺口前最小、精确的压力集。
