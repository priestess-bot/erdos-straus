---
kind: claim
claim_id: type-I-a3-b2-r23-terminal-descent-ray
title: (A,B,R)=(3,2,23) 的固定图表终端与严格递降射线
statement: 对每个核心素数 p，只要 1608|(23p+1)，就可唯一恢复 C=(23p+1)/536、m=(16C+1)/23，并得到正规 Type I 证书 (A,B,C)=(3,2,C) 与严格递降 n=67C/3=(23p+1)/24<p。源解为 4/n=1/(6C)+1/(201C)+1/(134C)，仅将第三分母乘 p 即提升为 p 的 Type I 解。该门等价于 p=769+1608t；其素数项形成原始等差射线。作为既有八路 p-dispatch 后的第九路，它在 p=2377 命中，给出独立的 gap-71 终端证书及 n=2278 的严格出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-coprime-factor-normal-form
  - type-I-normal-tail-deflation-selector
  - type-I-fixed-normal-chart-tail-descent-rays
  - type-I-a2-b27-square-only-terminal-ray
topics:
  - type-I
  - normal-form
  - terminal-first
  - strict-descent
  - full-solution-lift
  - p-level-selector
  - dirichlet-ray
  - proof-boundary
sources:
  - claim: type-I-fixed-normal-chart-tail-descent-rays
    role: exact-fixed-chart-descent-selector
  - reproduction: reproductions/type_i_a2_b27_square_only_terminal_ray.py
    role: ninth-route-controls-and-reconstruction
visibility: public
last_checked: '2026-08-12'
---

# ((A,B,R)=(3,2,23)) 的固定图表终端与严格递降射线

## 1. 只看 (p) 的精确门

取固定正规图表

\[
(A,B,R)=(3,2,23),
\qquad H=AR-B=67.
\tag{1}
\]

固定图表的尾部递降除数是

\[
L=\frac{R+1}{\gcd(R+1,4B(A+B))}
=\frac{24}{\gcd(24,40)}=3.
\tag{2}
\]

因此通用 (p)-级门 (4BHL\mid pR+1) 专门化为

\[
\boxed{1608\mid23p+1.}
\tag{3}
\]

**定理。** 若核心素数 (p\) 满足 (3)，令

\[
C=\frac{23p+1}{536},
\qquad
m=\frac{16C+1}{23}.
\tag{4}
\]

则 (C\in3\mathbb N)，(m\in\mathbb N)，且

\[
p=24C-m,
\quad
x=6C,
\quad
d=9C,
\quad
y=201C,
\quad
K=134C.
\tag{5}
\]

给出正规 Type I 终端证书和严格源

\[
\boxed{
\frac4p=\frac1{6C}+\frac1{201C}+\frac1{134pC},}
\tag{6}
\]

\[
\boxed{
\frac4n=\frac1{6C}+\frac1{201C}+\frac1{134C},
\qquad n=\frac{67C}{3}=\frac{23p+1}{24}<p.}
\tag{7}
\]

故 (3) 是一个无缺口枚举的、既给 terminal 又给严格下降和全解提升的 (p)-级选择器。

**证明。** 将 (3) 写为 (23p+1=1608j)。由 (4) 得 (C=3j)，故
(3\mid C)。又 (1608\equiv-2\pmod {23})，于是

\[
-2j\equiv1\pmod {23},
\qquad
16C+1=48j+1\equiv2j+1\equiv0\pmod {23},
\tag{8}
\]

从而 (m) 为整数。直接代入即得

\[
24C-m=\frac{536C-1}{23}=p,
\qquad
mR=23m=16C+1=4B^2C+1.
\tag{9}
\]

所以 (5) 正是互素正规形 ((A,B,C)=(3,2,C))。特别地，

\[
4K=536C=23p+1.
\tag{10}
\]

而 (R+1=24) 整除 (4K=536C)，给出 (n=4K/24=67C/3)。利用

\[
\frac1{6C}+\frac1{201C}
=\frac{69}{402C}=\frac{23}{134C}
\tag{11}
\]

并结合 (10)，分别得到 (6) 与 (7)。最后

\[
p-n
=\frac{24p-(23p+1)}{24}
=\frac{p-1}{24}>0,
\tag{12}
\]

所以 (2\le n<p)，且将 (7) 的第三分母乘以 (p) 恰好得到 (6)。证毕。

## 2. 规范原始射线

门 (3) 只有一个正剩余类：

\[
\boxed{
p=769+1608t,
\quad C=33+69t,
\quad m=23+48t,
\quad n=737+1541t,
\qquad t\ge0.}
\tag{13}
\]

这里 (p\equiv1\pmod {24}) 自动成立，且

\[
p-n=32+67t>0,
\qquad \gcd(769,1608)=1.
\tag{14}
\]

因此这是一个原始的候选核心素数等差射线；其每个素数项都由 (6)--(7) 同时闭合
terminal 和严格递降出口。这个无穷射线断言只使用 Dirichlet 定理的通常形式，不声称其
以外的核心素数也能命中该固定图表。

首项 (p=769) 已由既有 gap-7 分支优先处理；新选择器没有改变那条既有路径。第二项

\[
p=2377,
\qquad C=102,
\qquad m=71,
\qquad n=2278
\tag{15}
\]

此前是现有八路 dispatch 的残余。此处 (6) 具体为

\[
\boxed{
\frac4{2377}
=\frac1{612}+\frac1{20502}+\frac1{32488836},}
\tag{16}
\]

而源为

\[
\boxed{
\frac4{2278}
=\frac1{612}+\frac1{20502}+\frac1{13668}.}
\tag{17}
\]

故它不是对 (p=769) 既有分支的重述，而是当前八路 selector 漏掉的独立
gap-(71) Type I 终端/递降叶。

## 3. 覆盖边界

本卡只关闭满足 (3) 的核心素数类，并将其作为第九个有优先级的 (p)-dispatch 分支。
它没有把任意高支持 (A>1) G/Type I 状态归入这个固定图表，因此不能替代全局出口引理。
它的作用是将一个八路残余控制点变成带显式 lift 的严格出口，并提供另一个可组合的
固定图表叶。
