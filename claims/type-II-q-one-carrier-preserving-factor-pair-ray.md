---
kind: claim
claim_id: type-II-q-one-carrier-preserving-factor-pair-ray
title: q=1 载体保留的 Type II 因子对终端与严格递降射线
statement: >-
  令 J,k,r 为正整数，J=1 (mod 6)、kr=1 (mod 3)，并设
  m=4J+3、c=3+km、X=J((J+1)cr-1)、p=4X-3。若 p 为素数，则 p=1 (mod 24)。
  显式因子对 (A,B,C,K)=(J,c(J+1),r,1+k(J+1)) 满足
  ABC=(p+m)/4、(A,B)=1、A+B=mK 与 m+1|p-1，故同时给出 p 的 Type II
  终端和 n=(p+m)/(m+1)=Jcr<p 的严格 two-tail 递降及显式 lift；其中
  gcd(X,n)=J，故选定的 J-carrier 被精确保留。J=7,k=1,r=1+3s 给出
  p=7585+22848s 的本原算术级数，因而有无穷多个核心素数参数；s=3 的 p=76129
  及 (J,k,r)=(13,1,1) 的 p=42169 都是 q=1 G 控制，分别保留 J=7、13。
  本卡只构造无限 terminal/descent 子族和两个 G 控制，不给出所有 q=1 G 状态的
  selector、E1/E3 adapter 或全局退出定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-three-criterion
  - type-II-factor-pair-carrier-strict-descent
  - type-II-q-one-factor-pair-source-compression
topics:
  - type-II
  - q-one
  - G-state
  - factor-pair
  - terminal-first
  - strict-descent
  - two-tail-lift
  - source-carrier
  - parametrization
  - Dirichlet
  - proof-boundary
sources:
  - claim: gap-three-criterion
    role: exact-q-one-G-classification
  - claim: type-II-factor-pair-carrier-strict-descent
    role: factor-pair-terminal-and-marked-two-tail-lift
  - claim: type-II-q-one-factor-pair-source-compression
    role: exact-carrier-intersection-identity
  - reproduction: reproductions/type_ii_q_one_carrier_preserving_factor_pair_ray.py
    role: fixed-G-controls-and-identity-checks
visibility: public
last_checked: '2026-08-15'
---

# q=1 载体保留的 Type II 因子对终端与严格递降射线

## 1. 参数族

取正整数

\[
J\equiv1\pmod6,
\qquad
kr\equiv1\pmod3,
\tag{1}
\]

并定义

\[
m=4J+3,
\qquad
c=3+km,
\qquad
L=(J+1)cr-1,
\tag{2}
\]

\[
X=JL,
\qquad
p=4X-3.
\tag{3}
\]

这一构造只在 (p) 恰为素数时讨论 Erdős--Straus 的核心素数实例。由
(J\equiv1\pmod6)，有 (m\equiv1\pmod3) 与 (c\equiv k\pmod3)；再由 (1)，

\[
L\equiv 2kr-1\equiv1\pmod3.
\tag{4}
\]

又 (J+1) 为偶数，故 (L) 为奇数。于是 (L\equiv1\pmod6)、
(X\equiv1\pmod6)，从而

\[
p=4X-3\equiv1\pmod{24}.
\tag{5}
\]

所以每个素数参数自动是核心素数。

## 2. 显式因子对与两尾递降

令

\[
a=J+1,
\qquad
(A,B,C,K)=\bigl(J,\ c(J+1),\ r,\ 1+k(J+1)\bigr).
\tag{6}
\]

由于 (c\equiv3\pmod J) 且 ((J,3)=1)，有

\[
(A,B)=\gcd\bigl(J,c(J+1)\bigr)=1,
\qquad A<B.
\tag{7}
\]

直接展开给出

\[
\begin{aligned}
ABC
 &=Jc(J+1)r=X+J=\frac{p+m}{4},\\
A+B
 &=J+\bigl(3+km\bigr)(J+1)
 =m\bigl(1+k(J+1)\bigr)=mK.
\end{aligned}
\tag{8}
\]

另一方面，

\[
X-1=(J+1)(Jcr-1),
\tag{9}
\]

所以

\[
m+1=4(J+1)\mid p-1,
\qquad
n:=\frac{p+m}{m+1}=Jcr.
\tag{10}
\]

这确实是严格较小的源：

\[
p-n=(4J+3)(Jcr-1)>0.
\tag{11}
\]

而且 (Jcr>2) 还给出

\[
p-(m+2)=4(J+1)(Jcr-2)>0,
\tag{12}
\]

故 gap 合法。由 (8)--(10) 的互素因子对正规形，得到两条精确恒等式

\[
\boxed{
\frac4n=\frac1{ABC}+\frac1{ACK}+\frac1{BCK}
}
\tag{13}
\]

以及

\[
\boxed{
\frac4p=\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.
}
\tag{14}
\]

因此 (14) 是直接 Type II terminal，(13) 是严格较小实例的标记两尾解；只把后两尾
乘以 (p) 就得到不读取目标解的显式 lift。

## 3. 载体精确保留

这里的 gap 参数恰为 (a=J+1)。由 (9)，((a,X)=1)，并且

\[
an=X+(a-1)=X+J.
\tag{15}
\]

故

\[
\gcd(X,n)=\gcd(X,an)=\gcd(X,J)=J.
\tag{16}
\]

这也正是标准 two-tail source-compression 恒等式
(\gcd(X,n)=\gcd(X,a-1)) 在本参数族的取等情形。它不只是表明 (J\mid n)：
在来自 (X) 的素数幂层中，进入 (n) 的交集**恰好**是 (J)，其余乘法容量为

\[
\frac XJ=L=(J+1)cr-1.
\tag{17}
\]

若 (p) 为素数，q=1 endpoint 为 G 当且仅当 (X) 的全部素因子为
(1\pmod3)。在这里等价于 (J) 与 (L) 的全部素因子都是 (1\pmod3)。因此该
参数化允许明确检查 G 条件，而不会把仅有 (J\equiv1\pmod6) 误当作 G 条件。

## 4. 一个本原无限 core-prime 射线

取

\[
J=7,
\qquad k=1,
\qquad r=1+3s
\quad(s\ge0).
\tag{18}
\]

则

\[
\begin{aligned}
m&=31,&c&=34,&(A,B,C,K)&=(7,272,1+3s,9),\\
X&=7(271+816s),&p&=7585+22848s,&n&=238(1+3s).
\end{aligned}
\tag{19}
\]

此时 (A+B=279=31\cdot9)，而

\[
\gcd(7585,22848)=1,
\qquad
p\equiv1\pmod{24}.
\tag{20}
\]

Dirichlet 算术级数定理因此给出无穷多个 (s\ge0) 使 (p) 为素数；对每一个这样的
参数，(13)--(14) 都给出核心素数的显式 terminal 与严格两尾递降。这里的无穷性只断言
素数参数的无穷性，**不**断言该整条射线都处于 q=1 G。

## 5. 两个实际 q=1 G 控制

### 5.1 (p=76129)：J=7 的正向 G 控制

在 (18) 中取 (s=3)，即 (r=10)。则

\[
p=76129,
\qquad
X=19033=7\cdot2719,
\qquad
n=2380,
\qquad
\gcd(X,n)=7.
\tag{21}
\]

(7) 与 (2719) 都是 (1\pmod3) 素数，所以该核心素数确为 q=1 G。因子对为

\[
(A,B,C,K)=(7,272,10,9),
\tag{22}
\]

并给出可直接逐项核对的两式：

\[
\frac4{2380}
=\frac1{19040}+\frac1{630}+\frac1{24480},
\tag{23}
\]

\[
\frac4{76129}
=\frac1{19040}+\frac1{47961270}+\frac1{1863637920}.
\tag{24}
\]

### 5.2 (p=42169)：J=13 的独立 G 控制

取

\[
(J,k,r)=(13,1,1).
\tag{25}
\]

得到

\[
p=42169,
\qquad
X=10543=13\cdot811,
\qquad
n=754,
\qquad
\gcd(X,n)=13,
\tag{26}
\]

以及

\[
(m,A,B,C,K)=(55,13,812,1,15).
\tag{27}
\]

这里 (13,811\equiv1\pmod3)，故也为 q=1 G。第二个控制说明 (21) 不是仅依赖
(J=7,m=31) 的偶然接口。

## 6. 边界

本构造给出的是带明确定义参数的 terminal/descent 子族，且证明指定 (J) 可精确穿过
标准 two-tail source；它没有证明每个 q=1 G 核心素数落入某个此类参数族，更没有构造从
任意 G state 到该模板的 E1/E3 adapter。特别地，(13) 的 lift 只适用于保留首分母的
两尾标记解，不能提升为任意 (4/n) 解的无条件全局 lift。它因此是对“载体可否保留”的
正向存在结果，而不是 Erdos--Straus 猜想或 G/Type I 全局 exit 的证明。
