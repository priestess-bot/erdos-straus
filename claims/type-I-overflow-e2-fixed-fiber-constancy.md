---
kind: claim
claim_id: type-I-overflow-e2-fixed-fiber-constancy
title: overflow 固定纤维的 E2 carry 常值性
statement: 设 p 为素数、0<d<p、A>0，并令 a=A/gcd(A,p-d)。对每个实际 overflow carrier M（A|M 且存在 n>0 使 pn=4dM+1），M mod ap 被两个同余 M=0 (mod a)、4dM=-1 (mod p) 唯一确定。因此 u=[M/a]_p、kappa=floor(M/p) mod a 与带账本 E2 条件在整个固定 (p,A,d) 纤维上恒定；特别地 E2 当且仅当 a 整除 r_d=[-(4d)^(-1)]_p。有限 Fourier/SNF source 行在固定纤维内不能通过选择某一行来修复 E2，物理因子账本只在跨 A/d/bundle 的 lcm 或重图表 transition 中才可能改变该门。本结论不排除已证明完整的跨纤维 source map。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-ledger-e2-gate
topics:
  - type-I
  - overflow
  - E2
  - carry
  - fixed-fiber
  - CRT
  - source-map
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: ledger-preserving-E2-equivalence
visibility: public
last_checked: '2026-08-06'
---

# overflow 固定纤维的 E2 carry 常值性

## 1. 定理

固定素数 \(p\)、整数 \(0<d<p\) 与 \(A>0\)，并令

\[
C=p-d,
\qquad
a=\frac{A}{(A,C)}.
\tag{1}
\]

一个实际 fixed-\((p,A,d)\) overflow carrier 是正整数 \(M\)，满足

\[
A\mid M,
\qquad
\exists n>0:\quad pn=4dM+1,
\qquad
4M-n>p.
\tag{2}
\]

**定理。** 若此纤维非空，则所有满足 (2) 的 \(M\) 在模 \(ap\) 下属于同一剩余类。更精确地，
令

\[
r_d=\left[-(4d)^{-1}\right]_p\in\{1,\ldots,p-1\},
\tag{3}
\]

则每个 carrier 都满足

\[
\boxed{
M\equiv0\pmod a,
\qquad
M\equiv r_d\pmod p.
}
\tag{4}
\]

因此，令

\[
u(M)=\left[\frac Ma\right]_p,
\qquad
\kappa_a(M)=\left\lfloor\frac Mp\right\rfloor\bmod a
\quad\text{（取 }0,\ldots,a-1\text{ 中的代表）},
\tag{5}
\]

则 \(u(M)\)、\(\kappa_a(M)\) 及 E2 都在整条纤维上恒定，并且

\[
\boxed{
\mathrm{E2}
\quad\Longleftrightarrow\quad
a\mid r_d
\quad\Longleftrightarrow\quad
\kappa_a(M)=0.
}
\tag{6}
\]

## 2. 证明

由 (2) 模 \(p\)，\(p\nmid M\) 且

\[
4dM\equiv-1\pmod p,
\tag{7}
\]

从而得到第二个同余。又 \(a\mid A\mid M\)。因为 \(p\nmid M\)，也有
\(p\nmid A\) 与 \((a,p)=1\)，所以中国剩余定理给出 (4) 的唯一模 \(ap\) 解。

若 \(M'=M+apt\)，则

\[
\frac{M'}a\equiv\frac Ma\pmod p,
\qquad
\left\lfloor\frac{M'}p\right\rfloor
=\left\lfloor\frac Mp\right\rfloor+at.
\tag{8}
\]

故 (5) 的两个量不随 carrier 改变。最后，带账本 cofactor E2 恰为
\(a\mid(M\bmod p)\)；由 (4) 这等价于 \(a\mid r_d\)，也等价于
\(\kappa_a(M)=0\)。证毕。

## 3. 对 source-map 的后果

固定纤维内的有限 source row table 即使有不同 Fourier/SNF 标签、不同 multiplicity 或不同
素数赋值，也不能选择出“某些 E2 通过而另一些失败”的行：E2 是该纤维的预筛，而不是
row-selector。

例如

\[
(p,d,A,a)=(73,1,27,3)
\tag{9}
\]

时 \(r_d=18\)。三个实际 carrier

\[
675,\qquad2646,\qquad10530
\tag{10}
\]

分别对应 \(n=37,145,577\)，并都有

\[
\left(M\bmod73,\kappa_3(M)\right)=(18,0).
\tag{11}
\]

所以同一 fixed fiber 的不同因子账本不会改变 E2；它们的差异只会在后续
\(\operatorname{lcm}\) 或换图表时变得相关。

要让一个 source map 对 E2 具有非平凡选择性，行必须显式跨越 \(A\)、\(d\) 或
complete-excess bundle。此时参数 \(a\) 自身也可能变化，因而必须给出跨纤维的实际
integer transition、typed lift 与穷尽证明；不能把固定纤维的相位选择冒充为 E2 修复。

## 4. 边界

本卡不构造这样的跨纤维 source map，也不说明任意 \(M\) 的 factor profile 在 lcm 后如何
演化。它只排除固定 \((p,A,d)\) 内通过有限角色或行选择来支付 E2 的路线；不排除
独立的 terminal、固定 \(n/s\) 除子、已付款 support reset 或跨状态递降。
