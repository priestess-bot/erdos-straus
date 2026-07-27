---
kind: claim
claim_id: middle-coordinate-lift-certificate-equivalence
title: 中间分母的一分母提升等价于直接除子证书
statement: 设 p=1 mod4 为素数且 p/4<c<p/2，m=4c-p。则存在 u,v 使 4/p=1/c+1/u+1/v，当且仅当 m 处存在 Type I 或 Type II Bradford 除子证书；此时 c 是该目标解的严格最小分母。故从任意较小源实例保留 c 的一分母提升，在此范围内只是直接证书的另一种写法。
claim_status: established
topics:
- descent
- obstruction
- certificate
- type-I-II
- egyptian-fractions
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: first-denominator-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: ordered-type-classification
visibility: public
last_checked: '2026-07-23'
---

# 中间分母的一分母提升等价于直接除子证书

## 定理

设 \(p\equiv1\pmod4\) 为素数，且

\[
\frac p4<c<\frac p2,\qquad m=4c-p.
\]

下列条件等价：

1. 存在正整数 \(u,v\)，使
   \[
   \frac4p=\frac1c+\frac1u+\frac1v; \tag{1}
   \]
2. 存在正除子 \(e\mid(pc)^2\)，满足
   \[
   4c-p\mid pc+e,\qquad
   4c-p\mid pc+\frac{(pc)^2}{e}; \tag{2}
   \]
3. 在缺口 \(m\) 处存在一张 Type I 或 Type II Bradford 除子证书。

此外，(1) 中必有 \(u>c,v>c\)，所以 \(c\) 是目标解的严格最小分母。

## 证明

从 (1) 减去 \(1/c\) 得

\[
\frac1u+\frac1v
=\frac4p-\frac1c
=\frac{4c-p}{pc}. \tag{3}
\]

对 (3) 使用二项单位分数的因子分解，得到

\[
((4c-p)u-pc)((4c-p)v-pc)=(pc)^2.
\]

这正是条件 2 以及

\[
u=\frac{pc+e}{4c-p},\qquad
v=\frac{pc+(pc)^2/e}{4c-p}
\]

之间的等价；也就是 one-denominator-lift-factor-criterion 的判据。

由 \(p/4<c<p/2\)，(3) 的右端严格介于 \(0\) 和 \(1/c\) 之间。故

\[
\frac1u<\frac1c,\qquad\frac1v<\frac1c,
\]

即 \(u,v>c\)。所以把目标三元组排序后，其首分母仍是 \(c\)。又

\[
0<m<p,\qquad m\equiv-p\equiv3\pmod4,
\]

从而 \(3\le m\le p-2\)。short-certificate-equivalence 于是把“首分母为
\(c=(p+m)/4\) 的目标解”精确等价于缺口 \(m\) 的 Type I/II 证书，证明条件 1 与
条件 3 等价。

## 对递降的含义

若某个较小源实例的解含有 \(c\)，保留它并重组其余两项能否提升到 \(p\)，完全只取决于
(1)，与该源实例的其余两个分母无关。在 \(p/4<c<p/2\) 的范围，这个问题已经等价于
直接构造 \(p\) 的除子证书；源实例的可解性没有带来额外杠杆。

尤其，令 \(n=2c<p\)，偶数源的标准解

\[
\frac4{2c}=\frac1c+\frac1{2c}+\frac1{2c}
\]

确实总可用作一个形式上的源解，但从它保留 \(c\) 的提升有且仅有 \(p\) 本身已经在
缺口 \(4c-p\) 获得证书。因此这不是“短证书失败时”的独立递降分支。

只有保留 \(c\ge p/2\) 的非首目标分母，或使用会改变全部三个分母的提升，才可能避开
这个等价障碍。
