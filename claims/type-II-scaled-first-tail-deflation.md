---
kind: claim
claim_id: type-II-scaled-first-tail-deflation
title: 缩放首分母的 Type II 双尾递降
statement: 设 p 为奇素数，4/p=1/x+1/y+1/z 为合法 Bradford Type II 证书，缺口 m=4x-p。对任意 k>=1，若 km+1|kp-1，则 n=k(p+m)/(km+1) 是 2<=n<p 的整数，且 4/n=1/(kx)+1/(y/p)+1/(z/p)。反之，指定形状 (kx,Y,Z)->(x,pY,pZ) 的提升必满足这一整除条件。在规范 Type II 坐标中，它等价于 km+1|4AC(K+kA)；k=1 正是普通双尾去 p。
claim_status: established
topics:
- type-II
- descent
- lifting
- factor-selection
- exact-algebra
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
visibility: public
last_checked: '2026-07-24'
---

# 缩放首分母的 Type II 双尾递降

## 定理

设

\[
\frac4p=\frac1x+\frac1y+\frac1z
\tag{1}
\]

为合法 Bradford Type II 证书，故 $p\mid y,z$，且

\[
m=4x-p,\qquad 3\le m\le p-2.
\tag{2}
\]

给定正整数 $k$。若

\[
km+1\mid kp-1, \tag{3}
\]

令

\[
n=\frac{k(p+m)}{km+1}, \tag{4}
\]

则 $n$ 为满足 $2\le n<p$ 的整数，且

\[
\frac4n=\frac1{kx}+\frac1{y/p}+\frac1{z/p}. \tag{5}
\]

将 (5) 的首分母由 $kx$ 缩为 $x$，并将后两个分母各乘 $p$，精确恢复 (1)：

\[
(kx,Y,Z)\longmapsto(x,pY,pZ). \tag{6}
\]

反过来，固定目标 Type II 三元组并要求提升具有 (6) 的形状时，源分母必为 (4)，
所以 (3) 是必要条件。

## 证明

令 $Y=y/p$、$Z=z/p$。由 (1) 可得

\[
\frac1Y+\frac1Z=4-\frac px=\frac mx. \tag{7}
\]

所以

\[
\frac1{kx}+\frac1Y+\frac1Z
=\frac{km+1}{kx}. \tag{8}
\]

又 $4x=p+m$，故右端为 $4/n$，其中 $n$ 是 (4)。其整性等价于

\[
km+1\mid k(p+m).
\]

因为 $km+1$ 与 $k$ 互素，且

\[
k(p+m)=kp+km\equiv kp-1\pmod{km+1},
\]

这恰为 (3)。因为 $k(p+m)>km+1$，该整数满足 $n\ge2$。又由
$x\le(p-1)/2$、$m\ge3$ 有

\[
n=\frac{4kx}{km+1}<p,
\]

从而源分母严格变小。

反向时，目标和源式相减后仍得到 (7)，再与源首项 $1/(kx)$ 相加便得到 (8)，
从而 (4) 与 (3) 均不可避免。

## 规范 Type II 坐标

令

\[
x=ABC,\qquad m=\frac{A+B}{K},\qquad
p=(4ACK-1)m-4A^2C.
\]

将最后一式代入 (3) 的左端，有

\[
kp-1\equiv-4AC(K+kA)\pmod{km+1}.
\]

故 (3) 等价于

\[
km+1\mid4AC(K+kA). \tag{9}
\]

这把选择器从 $p-1$ 的因子条件扩展为一个双参数因子条件。$k=1$ 时 (9) 化为
`type-II-two-tail-deflation-descent` 的
$m+1\mid4AC(K+A)$。

## 消去首尺度

令

\[
D=km+1.
\]

因为 $\gcd(k,D)=1$，有完全等价的因子表述

\[
\begin{aligned}
km+1\mid kp-1
&\Longleftrightarrow D\mid k(p+m)\\
&\Longleftrightarrow D\mid p+m,\qquad D\equiv1\pmod m. \tag{10}
\end{aligned}
\]

于是 $k=(D-1)/m$，并且源分母有分解形式

\[
n=k\frac{p+m}{D}. \tag{11}
\]

这消除了表面上的二维搜索：固定合法缺口 $m$ 后，只需分解同一个
$p+m=4x$，并寻找一个 $+1\pmod m$ 的因子 $D$。与此同时 Type II 证书要求
$x^2$ 有一个 $-x\pmod m$ 的除子。因而后续的统一选择问题是同一整数 $x$ 的两种
除子残数是否能被同时强制，而不是对无结构的 $k$ 穷举。

具体地，足以证明下面的因子选择命题：

\[
\boxed{
\begin{gathered}
\forall p\equiv1\pmod {24}\ \exists m,D,e\ \text{使}\\
3\le m\le p-2,\quad m\equiv3\pmod4,\quad x=(p+m)/4,\\
D\mid4x,\quad D\equiv1\pmod m,\quad D>1,\\
e\mid x^2,\quad e\le x,\quad e\equiv-x\pmod m.
\end{gathered}} \tag{12}
\]

最后一行给出 Type II 证书；前一行令 $k=(D-1)/m$ 并给出对应的带标记严格提升。
因此 (12) 是“短证书或带标记递降”目标的一条单一、可检验的充分路线。

## 边界

这是指定坐标形状的带标记严格递降定理，不是所有可能递降的分类，更没有证明对每个
$p$ 都可选择 $k,m$。更重要的是，`type-II-scaled-tail-marked-lift-equivalence`
证明源端的指定首分母 $kx$ 并非普通归纳假设所自动提供：取得该带标记源解已等价于
取得目标的固定 Type II 证书。因此本机制是完全显式的 Type II 证书选择器，除非另有
独立的标记源解存在定理，否则不能单独作为无标记递归证明。
