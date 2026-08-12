---
kind: claim
claim_id: type-I-fixed-normal-chart-tail-descent-rays
title: 固定 Type I 正规图表的严格尾部递降射线
statement: 设互素正整数 A,B 和 R=3 mod4，H=AR-B>B。对固定正规图表 mR=4B^2C+1、p=4ABC-m，正规尾去缩放严格递降精确等价于 L|C，其中 L=(R+1)/gcd(R+1,4B(A+B))。该门与 C=-4B^2的逆元(mod R) 兼容当且仅当 gcd(R,L)=1；兼容时 CRT 给出唯一 C 类(mod RL)。若此类存在自然核心基点且其候选进程原始，则每个素数项都有正规形 (A,B,C)，并显式严格递降到 n=4BCH/(R+1)<p；源解为 4/n=1/(ABC)+1/(ACH)+1/(BCH)，将第三分母乘 p 即提升为 4/p。L=1 时每个图表项自动递降，包含 (2,27,35) 的平方专用射线。该选择器不选择任意 G/Type I 状态的图表。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-coprime-factor-normal-form
  - type-I-normal-tail-deflation-selector
topics:
  - type-I
  - normal-form
  - strict-descent
  - full-solution-lift
  - dirichlet-ray
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-coprime-factor-normal-form
    role: normal-form-reconstruction
  - claim: type-I-normal-tail-deflation-selector
    role: exact-descent-gate
  - reproduction: reproductions/type_i_fixed_normal_chart_tail_descent_rays.py
    role: algebraic-controls-and-ray-verification
visibility: public
last_checked: '2026-08-12'
---

# 固定 Type I 正规图表的严格尾部递降射线

## 1. 图表内的精确递降选择器

取正整数 \(A,B,R\)，满足

\[
(A,B)=1,
\qquad R\equiv3\pmod4,
\qquad H=AR-B>B.
\tag{1}
\]

令 \(C\) 是任意正整数，使

\[
m=\frac{4B^2C+1}{R},
\qquad p=4ABC-m
\tag{2}
\]

为整数、\(m\) 为自然 Type I 缺口、且 \(p\equiv1\pmod {24}\)。令

\[
K=BCH.
\tag{3}
\]

定义

\[
g=\gcd(R+1,4B(A+B)),
\qquad L=\frac{R+1}{g}.
\tag{4}
\]

**定理。** 对满足 (1)--(3) 的每个正常图表，保持前两个分母的正规尾严格递降存在当且仅当

\[
\boxed{L\mid C.}
\tag{5}
\]

在此情形，若 \(p\) 为素数，则 (2) 给出 Type I 正规形 \((A,B,C)\)，且

\[
\boxed{
n=\frac{4BCH}{R+1}<p}
\tag{6}
\]

是一个严格源；具体有

\[
\boxed{
\frac4n
=\frac1{ABC}+\frac1{ACH}+\frac1{BCH},}
\tag{7}
\]

\[
\boxed{
\frac4p
=\frac1{ABC}+\frac1{ACH}+\frac1{pBCH}.}
\tag{8}
\]

**证明。** 从 (2) 得 \(mR=4B^2C+1\)，所以正规形恒等式给出

\[
4K=pR+1.
\tag{9}
\]

已知正规尾选择器要求 \(R+1\mid4BC(A+B)\)。这与
\(R+1\mid4BCH\) 等价，因为 \(H\equiv-(A+B)\pmod {R+1}\)。按 (4)，该整除
恰等价于 (5)。故 (6) 为整数。恒等式 (9) 随即给出

\[
p-n=\frac{p(R+1)-(pR+1)}{R+1}=\frac{p-1}{R+1}>0.
\tag{10}
\]

另一方面，\(H+B=AR\)，因此

\[
\frac1{ABC}+\frac1{ACH}=
\frac{H+B}{ABCH}=\frac R{BCH}.
\tag{11}
\]

将 (11) 与 \(4K=(R+1)n\) 或 \(4K=pR+1\) 合并，即分别得到 (7) 和 (8)。
源等式右侧是三个正单位分数，故 \(n\ne1\)；因而 (10) 给出 \(2\le n<p\)。证毕。

这将选择成本精确压缩为固定图表的一条除法：一旦 \((A,B,R,C)\) 已给定，(5) 可立即判定；
命中时证书、源和 lift 都没有剩余搜索。它不声称每个核心素数、特别是每个 G/Type I 状态，
都能选到通过该门的图表。

## 2. CRT 相容性与原始等差进程

式 (2) 等价于

\[
C\equiv c_R:=-(4B^2)^{-1}\pmod R.
\tag{12}
\]

这里逆元存在：若 (2) 有解，则 \((B,R)=1\)，否则 \(mR=4B^2C+1\) 模任何
\((B,R)\) 的素因子矛盾。将 (12) 与 \(C\equiv0\pmod L\) 合并，CRT 相容当且仅当

\[
\boxed{\gcd(R,L)=1.}
\tag{13}
\]

必要性是因为 \((c_R,R)=1\)；充分性给出唯一正类 \(C_\ast\pmod {RL}\)。

现在设该类中存在一个自然核心基点 \(C_0\)，即对应 (2) 的 \(m_0,p_0\) 满足
\(3\le m_0\le p_0-2\) 及 \(p_0\equiv1\pmod {24}\)。令

\[
\lambda=\frac6{\gcd(6,BHL)}.
\tag{14}
\]

则最小的正 \(C\)-步长同时保持 (2)、(5) 和 \(p\equiv1\pmod {24}\) 是 \(\lambda RL\)。
也就是说，

\[
C(t)=C_0+\lambda RLt
\tag{15}
\]

给出

\[
p(t)=p_0+4BHL\lambda t,
\qquad m(t)=m_0+4B^2L\lambda t.
\tag{16}
\]

事实上 (12)--(13) 给出 \(C\) 模 \(RL\) 的唯一类，而 \(24\mid4BHL\lambda\) 恰是 (14) 的定义。
又 \(H>B\) 使 \(p(t)-m(t)\) 随 \(t\) 严格增加，故自然 gap 范围由基点传递到全部
\(t\ge0\)。因此 (16) 是规范的候选核心素数进程；在

\[
\gcd(p_0,4BHL\lambda)=1
\tag{17}
\]

时它是原始的，因而含无穷多个素数项。每个素数项都自动携带 (4)--(6) 的严格递降，而不是仅有
一张 direct terminal。

## 3. 三个独立控制

### 非平凡 \(L=3\) 控制

取

\[
(A,B,R,H)=(1,1,23,22),
\qquad L=3,
\qquad C=63+69t.
\tag{18}
\]

此时 \(C\equiv-4^{-1}\pmod {23}\) 且 \(3\mid C\)，正是 (12)--(15) 的非自动
CRT 命中。于是

\[
m=11+12t,
\qquad p=241+264t,
\qquad n=231+253t.
\tag{19}
\]

首项给出

\[
\frac4{231}=\frac1{63}+\frac1{1386}+\frac1{1386}
\longmapsto
\frac4{241}=\frac1{63}+\frac1{1386}+\frac1{334026}.
\tag{20}
\]

这说明精确门 \(L\mid C\) 真正扩大了 \(L=1\) 的自动递降扇。

### \(B=3\) 控制

取

\[
(A,B,R,H)=(1,3,23,20),
\qquad C=7+23t.
\tag{21}
\]

有 \(24\mid4B(A+B)=48\)。由 (2)，

\[
m=11+36t,
\qquad p=73+240t,
\qquad n=70+230t.
\tag{22}
\]

这个进程原始；对每个素数项，(5)--(6) 给出严格递降。首项为

\[
\frac4{70}=\frac1{21}+\frac1{140}+\frac1{420}
\longmapsto
\frac4{73}=\frac1{21}+\frac1{140}+\frac1{30660}.
\tag{23}
\]

### \(B=27\) 的平方专用控制

取

\[
(A,B,R,H)=(2,27,35,43),
\qquad C=19+70t.
\tag{24}
\]

则 \(36\mid4\cdot27(2+27)\)，并恢复

\[
m=1583+5832t,
\qquad p=2521+9288t,
\qquad n=2451+9030t.
\tag{25}
\]

它是原始进程，并正是
[\((A,B)=(2,27)\) 的平方专用 Type I 终端射线](type-I-a2-b27-square-only-terminal-ray.md)
中 \(R=35\) 的严格递降分支。它表明该定理不局限于 \(d\mid x\)；这里
\(d=4C\nmid54C=x\)，但仍有 \(d\mid x^2\)。

## 4. 对全局出口的边界

这里的必要未解步骤是图表选择：必须从任意 G/Type I 状态构造一个正常图表，其
\(C\) 同时命中 (5) 与 (13) 的 CRT 门，或给出另一种严格出口。因而该引理提供的是一族
完全显式、可提升、可递降的射线，而非 G/Type I 全局出口定理本身。

定向复现：`python3 reproductions/type_i_fixed_normal_chart_tail_descent_rays.py --verify`
