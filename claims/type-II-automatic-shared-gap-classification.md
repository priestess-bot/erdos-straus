---
kind: claim
claim_id: type-II-automatic-shared-gap-classification
title: 核心同余类上自动共享因子缺口的完全分类
statement: 设 m=3 mod4，m>=3。若存在固定整数 D>1，使对每个 p=1 mod24 都有 D|p+m 且 D=1 modm，则必有 D=m+1，且 m 属于 3,7,11,23。反之这四个 m 分别由 D=4,8,12,24 实现。故这四条是所有可由 p=1 mod24 单独强制的自动共享因子缺口；任何其它缺口的共享因子必须随 p 或其因子分解而变。
claim_status: established
topics:
- type-II
- shared-divisor
- congruences
- classification
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 核心同余类上自动共享因子缺口的完全分类

## 定理

令

\[
m\equiv3\pmod4,\qquad m\ge3.
\]

考虑最强的“自动共享”情形：存在一个与 \(p\) 无关的固定整数 \(D>1\)，使每个
整数 \(p\equiv1\pmod {24}\) 都满足

\[
D\mid p+m,\qquad D\equiv1\pmod m. \tag{1}
\]

则

\[
(m,D)\in\{(3,4),(7,8),(11,12),(23,24)\}. \tag{2}
\]

反过来，(2) 的每一对都满足 (1)。

## 证明

在 (1) 中令 \(p=1+24t\)。由于 \(D\) 整除所有

\[
24t+(m+1),
\]

它同时整除任意两项之差 \(24\)，以及 \(t=0\) 时的 \(m+1\)。因此

\[
D\mid\gcd(24,m+1). \tag{3}
\]

另一方面 \(D>1\) 且 \(D\equiv1\pmod m\)，所以

\[
D\ge m+1. \tag{4}
\]

(3) 给出 \(D\le m+1\)，于是 \(D=m+1\)，并且

\[
m+1\mid24. \tag{5}
\]

再用 \(m\equiv3\pmod4\)、\(m\ge3\)，(5) 只给出

\[
m+1\in\{4,8,12,24\},
\]

即 (2)。反向方向直接由

\[
p+m=(p-1)+(m+1)
\]

以及 \(24\mid p-1\)、\(m+1\mid24\) 得到。

## 对选择器的意义

`type-II-small-shared-gap-explicit-fan` 与
`type-II-shared-gap-23-automatic-fan` 分别使用了这四个且仅这四个缺口。
因而在它们之后，不能再期待仅从核心同余 \(p\equiv1\pmod {24}\) 抽出一个固定
共享因子；任何新的 \(D\equiv1\pmod m\) 必须利用 \(p\) 的具体值、\(p-1\) 的因子，
或 \(p+m\) 的非平凡因子分解。

这给出一个清晰的研究切换点：四个自动缺口适合做无条件 Type II 子扇；其残余应转入
真正的自适应共享因子选择，而不是继续枚举常数 \(D\)。
