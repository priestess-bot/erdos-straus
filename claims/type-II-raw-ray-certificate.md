---
kind: claim
claim_id: type-II-raw-ray-certificate
title: 非互素 Type II 因子射线仍直接给出证书
statement: 设 p=1 mod4 为素数，A,C,K 为正整数，h=4ACK-1，且 h|Kp+A。令 B=(Kp+A)/h。若 A<=B，则 m=(A+B)/K、x=ABC、d=A^2C 构成合法 Type II 除子证书；不需要 gcd(A,B)=1。令 g=gcd(A,B) 后，该证书归一化为 (A/g,B/g,Cg^2,K/g) 的互素正规形。
claim_status: established
topics:
- type-II
- certificate
- factorization
- parametrization
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-statement-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 非互素 Type II 因子射线仍直接给出证书

## 定理

设 \(p\equiv1\pmod4\) 为素数，\(A,C,K\) 为正整数，令

\[
h=4ACK-1,\qquad B=\frac{Kp+A}{h}.
\]

若 \(B\) 是正整数且 \(A\le B\)，则

\[
m=\frac{A+B}{K},\qquad x=ABC,\qquad d=A^2C \tag{1}
\]

定义一张合法的 Type II 证书。这里不需要 \(\gcd(A,B)=1\)。

## 证明

由 \(hB=Kp+A\) 模 \(K\) 化简，因 \(h\equiv-1\pmod K\)，得到

\[
A+B\equiv0\pmod K.
\]

故 \(m\) 是正整数。再由 \(hB=Kp+A\)，有

\[
Kp=4ACKB-(A+B)=K(4ABC-m),
\]

所以

\[
p=4ABC-m. \tag{2}
\]

若 \(m=2ABC\)，则由 \(m\le A+B\le2B\le2ABC\) 中全部取等，
得到 \(K=A=B=C=1\)，继而 (2) 给出 \(p=2\)，矛盾。因此 \(m<2ABC\)，
结合 (2) 可得 \(0<m<p\)。又 \(m=4ABC-p\equiv3\pmod4\)，所以

\[
3\le m\le p-2.
\]

式 (1) 给出 \(d\mid x^2\)，而 \(A\le B\) 给出 \(d\le x\)。最后

\[
x+d=AC(A+B)=ACKm,
\]

从而 \(m\mid x+d\)。这正是 Type II 的除子条件。

## 与互素正规形的关系

令 \(g=\gcd(A,B)\)。由 \(g\mid A,B\) 和 \(hB=Kp+A\)，有 \(g\mid Kp\)。
式 (2) 与 \(0<m<p\) 表明 \(p\nmid A\)，故 \(g\mid K\)。于是

\[
A_0=\frac Ag,\qquad B_0=\frac Bg,\qquad
C_0=Cg^2,\qquad K_0=\frac Kg
\]

都是正整数，且

\[
\gcd(A_0,B_0)=1,\qquad
ABC=A_0B_0C_0,\qquad
A^2C=A_0^2C_0.
\]

它们给出同一 \((x,d,m)\) 的互素 Type II 正规形。因此互素条件的作用是消除
参数冗余，而不是判定证书是否存在。

## 对因子射线的含义

在 \(A,C\) 有界、\(K\) 可变的搜索中，允许非互素参数可使原始坐标的
\(\max(A,C)\) 更小；代价是其规范化后的 \(C_0\) 可能更大。例如

\[
p=313,\qquad(A,B,C,K)=(2,40,1,6)
\]

给出

\[
(m,x,d)=(7,80,4),
\]

虽 \(\gcd(2,40)=2\)，仍是有效 Type II 证书。它归一化为
\((A_0,B_0,C_0,K_0)=(1,20,4,3)\)。

## 缺口上界

同一构造还给出精确恒等式

\[
m=\frac{p}{h}+\frac AK\left(1+\frac1h\right),
\qquad h=4ACK-1. \tag{3}
\]

因为 \(h\ge3\)，若一族射线满足 \(A\le B_0\)，则其每张证书都有

\[
m\le\frac p3+\frac{4B_0}{3}. \tag{4}
\]

因此 `type-II-ac-ray-saturation-conjecture` 若以某个全局 \(B\) 成立，不仅会给出
Type II 解，而且给出显式的相对短缺口界

\[
H(p)=\frac p3+\frac{4B}{3}.
\]

式 (3) 由 \(B=(Kp+A)/h\) 直接代入 \(m=(A+B)/K\) 得到。这个界仍是线性的，
但严格小于自然范围上端 \(p-2\) 的主项；它把射线饱和与“短证书”分支定量地连接起来。

## 序条件何时自动成立

射线构造中的唯一序条件也有精确的差值公式：

\[
B-A=\frac{K(p-4A^2C)+2A}{h}. \tag{5}
\]

因此

\[
A\le B
\quad\Longleftrightarrow\quad
K(p-4A^2C)+2A\ge0. \tag{6}
\]

特别地，若

\[
p\ge4A^2C, \tag{7}
\]

则任何满足 \(h\mid Kp+A\) 的正整数射线参数都自动满足 \(A\le B\)。
式 (5) 只需从 \(B=(Kp+A)/h\) 减去 \(A\) 即得。故在固定 \(A,C\) 的射线中，
充分大的目标素数不再需要单独检查序条件；真正剩余的是移位数
\(p+4A^2C\) 是否有合适的因子残数。
