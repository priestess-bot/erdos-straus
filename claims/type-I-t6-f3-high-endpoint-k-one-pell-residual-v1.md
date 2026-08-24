---
kind: claim
claim_id: type-I-t6-f3-high-endpoint-k-one-pell-residual-v1
title: F3 high endpoint 的 k=1 Pell 型残差参数化
statement: >-
  对 ACTUAL_PERSISTENT、PROPER_FACTOR_ROOT、h>p、terminal_first_miss 的 high
  stutter state，若高域内重新推得的 N=a^2-a(e-1)+(e-1)^2=hk 满足 k=1，则
  gcd(a,e-1)=1，且存在唯一正整数 d,x,y，使 e=d x^2、a=dxy-1、gcd(x,y)=1、
  y>x、d=2 (mod 3)、3 不整除 x、3 整除 y。再存在正整数 c=1 (mod 3)，满足
  y^2+xy-x^2=c(dxy-1)。并有 m=d(x^2-xy+y^2)-1、
  h=d^2x^2(x^2-xy+y^2)-dx(x+y)+1，及 p 的显式整式商公式。反之这些整数曲线
  条件不保证 actual maximal receipt、terminal-first miss 或 persistent admission；
  特别地现有 low k=1 empty theorem 不能用于 y>x 的本支。该结论把
  HIGH_STUTTER_GATE 精确分成 k=1 Pell residual 与 odd k>=3 residual，但不关闭任何一个。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-high-endpoint-normal-form-v1
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-actual-maximality-boundary
topics:
  - type-I
  - root-capacity
  - f3
  - high-endpoint
  - stutter
  - k-one
  - Pell-equation
  - residual
  - proof-boundary
sources:
  - claim: type-I-t6-f3-high-endpoint-normal-form-v1
    role: high-domain N=hk derivation
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual maximal receipt and stutter equations
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual root cyclotomic input
  - reproduction: reproductions/type_i_t6_f3_high_endpoint_k_one_pell.py
    role: symbolic parameterization and boundary controls
visibility: public
last_checked: '2026-08-24'
---

# F3 high endpoint 的 \(k=1\) Pell 型残差

## 1. 范围

只在下列 high stutter 分支内工作：

\[
\mathrm{ACTUAL\_PERSISTENT}\land\mathrm{PROPER\_FACTOR\_ROOT}
\land h>p\land\mathrm{terminal\_first\_miss}\land c_{\rm root}=p-1.
\tag{1}
\]

前一张 high-domain normal-form card 在这个范围内重新证明

\[
b=e-1,\qquad a=em-h>e,\qquad
N=a^2-ab+b^2=hk.
\tag{2}
\]

本卡额外假设 \(k=1\)，即 \(h=N\)。这不是引用 low-height \(k=1\) empty
theorem；high 分支的关键不等式是 \(a>e\)，方向正好相反。

## 2. Actual root 先给出 primitive Eisenstein coordinates

令 \(g=(a,b)\)、\(a=gA,b=gB\)、\(H=A^2-AB+B^2\)。因 \(h=N=g^2H\)，
而 \(pa+b=eh\)，有

\[
pA+B=egH.
\tag{3}
\]

直接代入 \(A^2(p^2+p+1)\) 得

\[
A^2(p^2+p+1)
 =H\left(e^2g^2H+eg(A-2B)+1\right).
\tag{4}
\]

actual root condition \(h\mid p^2+p+1\) 令左边为 \(g^2H\) 的倍数；约去 \(H\)
后，右括号必须被 \(g^2\) 整除，但它模 \(g\) 为 \(1\)。所以

\[
\boxed{(a,b)=1.}
\tag{5}
\]

## 3. Square-factor parameterization

由 \(3\mid h=N=(a+b)^2\pmod3\) 及 (5)，逐一检查 \(e\pmod3\) 得

\[
e\equiv a\equiv2\pmod3,\qquad m\equiv1\pmod3.
\tag{6}
\]

将 \(h=N=em-a\) 展开，得到

\[
m=\frac{(a+1)^2}{e}+e-a-2,
\tag{7}
\]

故 \(e\mid(a+1)^2\)。标准互素平方因子分解给出唯一正整数 \(d,x,y\)：

\[
\boxed{e=dx^2,\qquad a=dxy-1,\qquad (x,y)=1.}
\tag{8}
\]

high inequality \(a>e\) 强制 \(y>x\)。由 (6)--(8) 还有

\[
\boxed{d\equiv2\pmod3,\qquad 3\nmid x,\qquad3\mid y.}
\tag{9}
\]

## 4. Pell 型整数曲线

\(p\) 的整性门和 (5) 中的互素性给出

\[
a\mid(x-y)(x^2-xy-y^2),\qquad (a,x-y)=1.
\tag{10}
\]

因为 \(y>x\)，第二因子严格为负。因此存在正整数 \(c\)，使

\[
\boxed{
y^2+xy-x^2=c(dxy-1),\qquad c\equiv1\pmod3.}
\tag{11}
\]

末个同余来自左边 \(\equiv-x^2\equiv2\pmod3\) 和
\(dxy-1\equiv2\pmod3\)。这与 low branch 的正号方程不同：low proof 的
Vieta descent 不能搬运到 (11)。

## 5. 显式恢复式与 exact residual

记 \(Q=x^2-xy+y^2\)。由 (7)--(8) 直接恢复

\[
\boxed{
m=dQ-1,\qquad
h=d^2x^2Q-dx(x+y)+1,}
\tag{12}
\]

\[
\boxed{
p=\frac{d^3x^4Q-d^2x^3(x+y)+1}{dxy-1}.}
\tag{13}
\]

因此 high \(k=1\) residual 已精确缩为满足 (9)、(11)--(13) 的整数点，并额外要求：

1. (13) 是核心素数；
2. \(h=3u\) 且 \(u=(2r+1,(p^2+p+1)/3)\) 为真 proper factor；
3. \(D=mp+1-h\) 是 canonical maximal receipt 的实际 \(D\)，而不只是曲线的
   shadow divisor；
4. 全部 active terminal-first checks 均 miss；
5. 该 endpoint 具有真实 persistent admission envelope。

条件 (1)--(3) 的整数 shadow 不能替代 (4)--(5)。例如
\((d,x,y)=(11,101,1020)\) 给出核心素数
\(p=115815206209\)、\(h=1169617882071\) 和曲线 shadow
\(D_0=1207185892628946440\)，但 \(D_0\nmid K\)，其 actual maximal receipt 的
\(D\) 不是 \(D_0\)，并且 \((p+3)/4\) 有 \(2\pmod3\) 素因子 \(8363\)，故 gap-3
Type II terminal 在 persistent routing 之前抢占。该控制只否定错误的
curve-as-actual inference。

## 6. 状态

\[
\mathrm{HIGH\_STUTTER\_GATE}
=
\mathrm{HIGH\_K1\_PELL\_RESIDUAL}
\;\dot\cup\;
\mathrm{HIGH\_KGE3\_RESIDUAL}.
\]

二者都仍是 OPEN_MINIMAL_RESIDUAL。下一条可判真假的定理是：在保留 canonical
maximality、terminal-first 和 persistent source 的前提下，证明 (11) 的 high \(k=1\)
surface family-empty、terminal，或构造一条 E1--E5 paid successor。
