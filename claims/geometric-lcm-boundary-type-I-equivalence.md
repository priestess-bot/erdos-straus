---
kind: claim
claim_id: geometric-lcm-boundary-type-I-equivalence
title: 几何 lcm 边界解等价于 A=1 的 Type I 证书
statement: 对自然缺口 m、x=(p+m)/4，存在 Type I 证书除子 d|x 当且仅当存在解 4/p=1/x+1/y+1/(p*lcm(x,y))；对应满足 d=gcd(x,y)。在 Type I 正规形 x=ABC,d=A^2C 中，这恰为 A=1 的面。
claim_status: established
topics:
- certificate
- type-I
- geometric-reduction
- divisor-parametrization
- proof-program
sources:
- paper: bradford_ionascu2015
  locator: "Definitions 2.1, Proposition 2.2, Conjecture 2.10"
  role: geometric-lcm-pattern-context
- paper: bradford2024
  locator: "Proposition 1"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 几何 \(\operatorname{lcm}\) 边界解等价于 \(A=1\) 的 Type I 证书

## 定理

令 \(p\equiv1\pmod4\) 为素数，\(m\equiv3\pmod4\)、
\(3\le m\le p-2\)，且 \(x=(p+m)/4\)。以下两项等价：

1. 存在 Type I 证书除子 \(d\mid x\)，满足 \(m\mid px+d\)；
2. 存在正整数 \(y\)，使
   \[
   \frac4p=\frac1x+\frac1y+
   \frac1{p\operatorname{lcm}(x,y)}. \tag{1}
   \]

在这个对应中

\[
d=\gcd(x,y),\qquad y=\frac{px+d}{m}. \tag{2}
\]

它在 `type-I-coprime-factor-normal-form` 的坐标
\(x=ABC,d=A^2C\) 中精确等价于 \(A=1\)：此时 \(x=BC,d=C\)，而证书条件为
\(m\mid Bp+1\)。

## 证明

先设 (1) 成立，并令 \(d=\gcd(x,y)\)。两边乘以 \(pxy\)，得到

\[
4xy=p(x+y)+d.
\]

因为 \(m=4x-p\)，这等价于

\[
my=px+d.
\]

故 \(d\mid x\mid x^2\) 且 \(m\mid px+d\)，即为 Type I 证书。

反之，设 \(d\mid x\) 是 Type I 证书。写 \(x=dt\)。自然缺口范围给出
\(\gcd(m,x)=1\)，所以 \(m\mid px+d=d(pt+1)\) 推出

\[
m\mid pt+1.
\]

令 \(y=d(pt+1)/m\)。若一个数同时整除 \(t\) 与 \((pt+1)/m\)，它也整除
\(pt+1\) 和 \(t\)，故为 \(1\)。于是 \(\gcd(x,y)=d\)。Type I 的恢复公式现在给出

\[
z=\frac{p(x+px^2/d)}m
=\frac{pxy}{d}=p\operatorname{lcm}(x,y),
\]

即得到 (1)。最后，正规形中 \(d\mid x\) 等价于 \(A^2C\mid ABC\)，即 \(A\mid B\)；
而 \(\gcd(A,B)=1\)，故 \(A=1\)。

## 与文献及目标的关系

Bradford--Ionascu 2015 研究的带 \(p\operatorname{lcm}(x,y)\) 的边界模式正是这个
\(A=1\) 面，而不是全体 Type I 解，更不是递降映射。外部源
`external-source-type-I-certificate` 则是同一正规形的 \(B=1\) 面。\(p=2521\) 没有
任何自然缺口上的 \(A=1\) 证书，却有 \(m=23\) 的 Type II 证书；因此任何一个边界面
的全覆盖猜想都不能代替完整证书空间或目标引理。
