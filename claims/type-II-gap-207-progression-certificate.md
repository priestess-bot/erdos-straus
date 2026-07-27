---
kind: claim
claim_id: type-II-gap-207-progression-certificate
title: 条件性窗口状态所在进程的缺口 207 Type II 证书
statement: 令 Q=lcm(24,{4j-1:1<=j<=37})，p=16Qk+153633769，x=(p+207)/4，N=x/9682。则 N 是整数、N=34 mod207，d=47N 满足 d|x、d<=x 且 d=-x mod207。因此对该进程中的每个核心素数 p，(m,d)=(207,47N) 是一张直接 Type II 除子证书。
claim_status: established
topics:
- type-II
- moving-window
- arithmetic-progression
- certificate
- state-closure
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 条件性窗口状态所在进程的缺口 207 Type II 证书

## 定理

令

\[
Q=\operatorname{lcm}\left(24,\{4j-1:1\le j\le37\}\right)
\]

并令

\[
p=16Qk+153{,}633{,}769,\qquad
x=\frac{p+207}{4}. \tag{1}
\]

定义

\[
E=9682=2\cdot47\cdot103,\qquad
N=\frac{x}{E},\qquad d=47N. \tag{2}
\]

则对每个该进程中的核心素数 \(p\)，\((m,d)=(207,47N)\) 是一张 Type II
除子证书。

## 证明

记

\[
x_0=\frac{153{,}633{,}769+207}{4}=38{,}408{,}494.
\]

直接整除给出

\[
E\mid4Q,\qquad E\mid x_0,\qquad
\frac{4Q}{E}\equiv0\pmod {207},\qquad
\frac{x_0}{E}=3967\equiv34\pmod {207}. \tag{3}
\]

由 (1)--(3)，\(N\) 是整数且恒有

\[
N=\frac{4Q}{E}k+\frac{x_0}{E}\equiv34\pmod {207}. \tag{4}
\]

另一方面

\[
x=EN,\qquad
-x\equiv-9682\cdot34\equiv149\pmod {207}, \tag{5}
\]

而

\[
d=47N\equiv47\cdot34\equiv149\equiv-x\pmod {207}. \tag{6}
\]

又 \(d\mid x\mid x^2\)，并且 \(d\le x\)，因为 \(47<E\)。缺口
\(207\equiv3\pmod4\)，且对这里的 \(p\) 有 \(207\le p-2\)。故 (6) 正是
Bradford Type II 除子条件，证毕。

对应分母可显式恢复为

\[
y=\frac{p(x+d)}{207},\qquad
z=\frac{p(x+x^2/d)}{207},
\]

并满足 \(4/p=1/x+1/y+1/z\)。

## 与窗口状态的关系

`type-II-moving-window-one-private-prime-conditional-escape` 的参数进程正是
\(p=16Qk+153633769\)。所以其前 37 个位置在 Dickson/Schinzel 条件下可以共同失败，
但该进程**无条件**在第 52 个移动窗口位置

\[
j=52,\qquad m=4j-1=207
\]

获得直接 Type II 证书。这个闭合不依赖“一个私有余因子是素数”的假设。

更一般地，任何从该进程继续作参数同余细分的状态仍落在 (1) 中，因而同样被该证书
捕获。这解释了自适应状态审计中的第 52 步统一闭合。

运行

    python3 reproductions/type_ii_gap_207_progression_certificate.py

会以整数和精确有理数核对 \(k=0,1,2\) 的证书恒等式。

## 边界

这个进程是原始的：\(\gcd(153633769,16Q)=1\)。因此 Dirichlet 算术级数定理给出
无穷多个核心素数属于它，且它们全部由上述缺口 207 证书覆盖。它仍只覆盖一个极稀疏的
素数子集，不证明所有前 37 窗口状态都在第 52 步闭合，更不证明 Erdős--Straus 猜想。
其价值在于提供严格的“逃逸状态 \(\to\) 未来缺口证书”机制，可作为全状态闭合或递降
定理的原型。
