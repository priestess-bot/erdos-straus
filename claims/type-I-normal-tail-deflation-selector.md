---
kind: claim
claim_id: type-I-normal-tail-deflation-selector
title: Type I 正规形的规范尾部递降选择器与平方因子外部源等价
statement: 设 Type I 正规形为 x=ABC、m|4B^2C+1，令 R=(4B^2C+1)/m。该证书的 p-倍尾唯一写成 p*u，其中 u=BC(AR-B)。保持前两项并将 p*u 去缩放为 u 给出严格源分母 n=4u/(R+1)，当且仅当 R+1|4BC(A+B)；此时 2<=n<p，且所得边恰为完整平方因子外部 source 递降在保留分母 u 上的一个参数化，而非新递降族。对一亿小 B 剖面中全部11个 B>1 的最小证书，该条件均失败。
claim_status: established
topics:
- type-I
- normal-form
- descent
- source-solution
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-certificate-and-recovery
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-25'
---

# Type I 正规形的规范尾部递降选择器与平方因子外部源等价

## 定理

令 \(p\equiv1\pmod{24}\) 的一张 Type I 证书具有互素正规形

\[
x=ABC,\qquad (A,B)=1,\qquad m\mid4B^2C+1.
\]

置

\[
R=\frac{4B^2C+1}{m},\qquad u=BC(AR-B). \tag{1}
\]

则该证书的第三个分母恰为 \(pu\)。保持前两个目标分母 \((x,y)\)，把第三项从
\(1/(pu)\) 改回 \(1/u\)，存在严格源状态

\[
\frac4n=\frac1x+\frac1y+\frac1u,\qquad
\frac4p=\frac1x+\frac1y+\frac1{pu} \tag{2}
\]

当且仅当

\[
R+1\mid4BC(A+B). \tag{3}
\]

此时

\[
n=\frac{4BC(AR-B)}{R+1},\qquad 2\le n<p. \tag{4}
\]

所以 (3) 是由证书因子 \((A,B,C)\) 直接可检验的、非反向搜索的严格递降选择条件。

## 证明

Type I 恢复式给出第三项除以 \(p\) 后为

\[
\frac zp=\frac{x+pB^2C}{m}
=\frac{ABC+(4ABC-m)B^2C}{m}
=BC(AR-B)=u. \tag{5}
\]

所需源分母由 (2) 唯一决定。由目标恒等式，(2) 等价于

\[
p(R+1)=4u+p-1,
\]

故必为 \(n=4u/(R+1)\)。模 \(R+1\) 有 \(R\equiv-1\)，于是

\[
4u=4BC(AR-B)\equiv-4BC(A+B)\pmod{R+1},
\]

给出 (3) 的充要性。

最后，使用 \(mR=4B^2C+1\) 直接计算

\[
p(R+1)-4BC(AR-B)=p-1. \tag{6}
\]

故整数 \(n\) 自动小于 \(p\)。式 (2) 的正单位分数恒等式又排除 \(n=1\)，所以
\(2\le n<p\)。

## 与完整平方因子外部源的等价

由 \(m\equiv3\pmod4\) 和 \(mR=4B^2C+1\)，有 \(R\equiv3\pmod4\)。令

\[
k=\frac{R+1}{4},\qquad q=4k-1=R. \tag{7}
\]

条件 (3) 正说明 \(n=u/k\) 是整数。由 (6) 得

\[
4kn=4u=qp+1,\qquad n=\frac{qp+1}{q+1}. \tag{8}
\]

又从源等式 (2) 有

\[
\frac qu=\frac1x+\frac1y. \tag{9}
\]

取 \(e=qx-u\)（必要时交换 \(x,y\) 以使 \(e\le u\)），则

\[
(qx-u)(qy-u)=u^2. \tag{10}
\]

因此 \(e\mid u^2\)、\(e\equiv-u\pmod q\)，这正是
[平方因子外部源递降](quadratic-factor-external-source-descent.md) 的完整二项尾因子条件，
其保留分母为 \(u=kn\)。反向地，该族的每个保留分母二项尾都给出 (2)，从而恢复 (3)。

故本选择器的价值是从一张给定 Type I 证书直接判定它是否落在该已知递降族，而不是构造
一个独立的递降机制。

## 一亿低溢出边界

在 [小 B 正规形剖面](type-I-small-b-normal-form-profile.md) 的一亿数据中，短缺口
\(m\le239\) 下恰有 11 个最小证书取 \(B>1\)。对这 11 张具体的最小 \((A,B,C)\)
证书，(3) 全部失败；因而它们都不能通过这个保持前两项的规范尾部去缩放直接得到源。

这不是这些素数不存在任何递降，也不是它们的其它 Type I 证书没有递降。它仅说明：
“短缺口、低溢出、首个最小 \(B\) 证书”与“该证书可直接读取的严格源”是两个独立条件。
后续选择器必须同时优化证书残数和 (3)，或改变保留的目标项、扩展源状态。不能将本卡
额外计为对完整平方因子外部源递降覆盖的改进。

## 重建

`short_certificate.type_i_normal_tail_deflation_witness` 直接实现 (1)--(4)。
`type_i_small_b_normal_form_profile.py` 对每张最小 \(B\) 证书记录
`normal_tail_deflation_source`；其一亿工件中 11 个非 \(B=1\) 记录均为 `null`。
