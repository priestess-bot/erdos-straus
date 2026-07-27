---
kind: claim
claim_id: type-II-two-tail-deflation-descent
title: Type II 双尾去 p 给出严格递降的充要整除条件
statement: 设 p 为奇素数，4/p=1/x+1/y+1/z 是一个合法 Bradford Type II 证书，3<=m=4x-p<=p-2。若 m+1 整除 p-1，则 n=(p+m)/(m+1) 是满足 2<=n<p 的整数，且 4/n=1/x+1/(y/p)+1/(z/p)。反之，保持 x 并把源解的后两个分母同乘 p 所得到的这种两尾提升，必满足该 n 及 m+1 整除 p-1。对 p=1 mod24，只须检查 m=d-1，其中 d|p-1 且 4|d。
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
  locator: Section 2, Type II parametrization
  role: certificate-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 双尾去 $p$ 的严格递降

## 定理

设 $p$ 为奇素数，且

\[
\frac4p=\frac1x+\frac1y+\frac1z
\tag{1}
\]

是一个合法 Bradford Type II 证书，即 $p\mid y,z$ 且其缺口满足
$3\le m\le p-2$。写

\[
m=4x-p.
\tag{2}
\]

若 $m+1\mid p-1$，则

\[
n=\frac{p+m}{m+1}
\tag{3}
\]

是整数，满足 $2\le n<p$，并且

\[
\frac4n=\frac1x+\frac1{y/p}+\frac1{z/p}.
\tag{4}
\]

把 (4) 的后两个分母同时乘回 $p$，便精确恢复 (1)。

反过来，任何保持首分母 $x$、把源解的后两个分母同乘 $p$ 的提升，若目标的
缺口为 (2)，则其源分母只能是 (3)；所以其存在必迫使 $m+1\mid p-1$。

## 证明

令 $Y=y/p$、$Z=z/p$。由 (1) 得

\[
\frac1Y+\frac1Z=4-\frac px=\frac mx.
\tag{5}
\]

于是

\[
\frac1x+\frac1Y+\frac1Z=\frac{m+1}{x}.
\tag{6}
\]

又因 $4x=p+m$，右端恰为 $4/n$，其中 $n$ 如 (3)。整性等价于

\[
m+1\mid p+m=(p-1)+(m+1),
\]

即 $m+1\mid p-1$。在通常 Bradford 范围 $3\le m\le p-2$ 内，
$n=(p+m)/(m+1)$ 自动满足 $2\le n<p$。这证明正向结论。

反向时，从目标式减去两尾按 $p$ 缩放后的源式，得到 (5)；重新相加即得 (6)，
从而源分母必为 (3)。其为整数时同一个整除条件不可避免。

## 规范 Type II 参数中的形式

在规范参数

\[
x=ABC,\qquad y=pACK,\qquad z=pBCK,\qquad
m=\frac{A+B}{K}
\]

中，递降条件为 $m+1\mid p-1$。若把 Type II 射线写为

\[
p=(4ACK-1)m-4A^2C,
\]

则它等价于

\[
m+1\mid4AC(A+K).
\tag{7}
\]

因此这不是任意 Type II 射线自动具备的性质，而是一个明确的、很强的因子选择
约束。它把可尝试缺口压缩成 $p-1$ 的因子：

\[
m=d-1,\qquad d\mid p-1.
\]

对核心素数 $p\equiv1\pmod {24}$，还必须有 $4\mid d$，以保证
$m\equiv3\pmod4$。

## 剩余选择器的精确形式

令 $d=m+1$，并写

\[
x=\frac{p+d-1}{4}.
\]

由 Type II 除子证书的同余判据，若存在

\[
e\mid x^2,\qquad e\le x,\qquad e\equiv-x\pmod{d-1}, \tag{8}
\]

则该 $d$ 同时给出 Type II 证书和上述带标记严格提升。因此下一步真正的逐点目标可表述为：

\[
\boxed{\ \forall p\equiv1\pmod {24}\ \exists d\mid(p-1),\ 4\mid d,\
\exists e\mid\left(\frac{p+d-1}{4}\right)^2
\text{ 满足 (8)}\ }. \tag{9}
\]

这不是原猜想的简单改写：它强制缺口来自 $p-1$ 的因子，并在成功时额外给出一个
带标记源表示。它也准确暴露了障碍所在：需要把 $p-1$ 的因子结构与
$x=(p+d-1)/4$ 的除子残数联系起来。

## 作用与边界

这是一个严格的带标记提升核：源分母严格变小，且提升规则固定、可验证。由
`type-II-scaled-tail-marked-lift-equivalence` 的 \(k=1\) 情形，取得该标记源解
等价于取得目标的固定 Type II 证书；因此它本身不是从任意较小实例解出发的归纳步骤。
它没有给出总能选到成功 $d\mid p-1$ 的定理，故不是对猜想的证明；真正的剩余问题是
在这些因子标记缺口中建立一个逐点的 Type II 选择器。相对于扫描全部
$m\equiv3\pmod4$，该选择器只面对 $\tau(p-1)$ 个候选。
