---
kind: claim
claim_id: type-I-overflow-cofactor-ledger-e2-gate
title: overflow cofactor r-图表的带账本 E2 存在性门
statement: 设 overflow 满足 pn=4Md+1、M=kp+r、1<=r<p、0<d<p、C=p-d 且旧 charged ledger A|M。令 g=gcd(A,C)、a=A/g。对 cofactor 目标 K_r=rC，下列条件等价：存在一个持久 target ledger A_T 使 A|A_T|K_r；A|rC；a|r；lcm(A,C)|rC。故 a 不整除 r 时，不仅规范 target lcm(A,C) 失败，而且任何保留旧 A 的 cofactor r-chart target 都不存在；这只排除该 ledger-preserving cofactor 分支，不排除已付款 support reset、其它除子图表、terminal 或容量出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-high-anchor-cofactor-outer-rank-composition
topics:
  - type-I
  - overflow
  - cofactor
  - r-chart
  - charged-support
  - E2
  - divisibility
  - source-lift
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-r-chart-support
    role: cofactor target normal form
  - claim: type-I-high-anchor-cofactor-macro-e1-e4-admission
    role: macro E2 interface
  - claim: type-I-high-anchor-cofactor-outer-rank-composition
    role: E5 payment boundary
visibility: public
last_checked: '2026-08-06'
---

# overflow cofactor \(r\)-图表的带账本 E2 存在性门

## 1. 问题是 target 是否存在，而非势是否足够

令一个已经通过来源/路径门的 overflow 满足

\[
pn=4Md+1,
\qquad
M=kp+r,
\qquad
1\le r<p,
\qquad
0<d<p,
\qquad
C=p-d,
\qquad
A\mid M.
\tag{1}
\]

cofactor \(r\)-图表的算术目标为

\[
K_r=rC.
\tag{2}
\]

这里的 E2 问题不是能否为一个已经存在的 target 支付 E5，而是：是否存在一个新
ledger \(A_T\)，既保留旧账本又能成为该 target 的 carrier，亦即

\[
A\mid A_T\mid K_r.
\tag{3}
\]

记

\[
g=(A,C),
\qquad
A=ga,
\qquad
C=gc,
\qquad
(a,c)=1.
\tag{4}
\]

## 2. 精确 E2 等价式

**引理。** 在 (1)--(4) 下，下列四项等价：

\[
\begin{aligned}
&\exists A_T\in\mathbb Z_{>0}:\ A\mid A_T\mid K_r,\\
&A\mid rC,\\
&a\mid r,\\
&[A,C]\mid rC.
\end{aligned}
\tag{5}
\]

**证明。** 第一项当且仅当 \(A\mid K_r=rC\)：正向由整除传递，反向直接取
\(A_T=A\)。由 (4)，

\[
A\mid rC
\ \Longleftrightarrow\
ga\mid rgc
\ \Longleftrightarrow\
a\mid rc
\ \Longleftrightarrow\
a\mid r,
\tag{6}
\]

最后一步使用 \((a,c)=1\)。又

\[
[A,C]=gac=Ca,
\tag{7}
\]

故 \([A,C]\mid rC\) 也当且仅当 \(a\mid r\)。证毕。

当门通过时，除了最小的持久账本 \(A_T=A\) 外，已有 cofactor 正规形采用的规范
吸收账本

\[
A_C=[A,C]
\tag{8}
\]

同样整除 \(K_r\)。若还满足该正规形的正性、canonical chart、来源和 typed fiber
条件，则后续的 macro E1--E4 与现有 \(\Lambda_p\) E5 合同可以各自适用；这些额外
条件不由 (5) 自动推出。

## 3. 对当前 source lift 的整数要求

overflow 方程模 \(p\) 给出 \(p\nmid M\)，从而 \(p\nmid A\) 和 \(p\nmid a\)。又
\(a\mid M=kp+r\)，所以

\[
\boxed{a\mid r\quad\Longleftrightarrow\quad a\mid k
=\left\lfloor\frac Mp\right\rfloor.}
\tag{9}
\]

设 \(t\in\{0,\ldots,p-1\}\) 是 \(M/a\) 模 \(p\) 的最小非负剩余。由于
\(at\equiv M\equiv r\pmod p\)，且 \(0<r<p\)，还有等价的无进位形式

\[
\boxed{a\mid r\quad\Longleftrightarrow\quad at<p.}
\tag{10}
\]

因此 Fourier 角色、群像或相位匹配本身并不能完成 cofactor lift：它们还必须产出一个
实际的 \(M\)，其 quotient/no-carry 数据满足 (9) 或 (10)。这把“相位能否落地”的
剩余工作缩成一个明确整数目标。

## 4. 局部障碍与边界

若 \(a\nmid r\)，(5) 表明没有任何 \(A_T\) 能同时保留旧 \(A\) 并整除 \(K_r\)。
这比“标准 \(A_C\) 没有通过”更强，但只是否定 ledger-preserving cofactor \(r\)-chart；
它不否定 fixed-\(n\)、fixed-\(s\)、已付款 support reset、直接 Type I/II 或跨状态
容量出口。

例如

\[
(p,A,M,d,n,r)=(73,18,1242,18,1225,1)
\tag{11}
\]

满足 \(73\cdot1225=4\cdot1242\cdot18+1\)。此时 \(C=55\)、\(g=1\)、\(a=18\)，而
\(K_r=55\)，故 \(18\nmid1\)，不存在满足 (3) 的 \(A_T\)。这并非全 atlas 无出口：
同一纯算术例还有另一个 fixed-\(n\) 除子 \(L=414\) 给出已付费的正目标，正是不能把
本引理误读为完整递降反例的原因。
