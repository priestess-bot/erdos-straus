---
kind: claim
claim_id: linear-ratio-ansatz-type-I-translation
title: 线性比例主族精确等价于固定缺口 Type I 证书
statement: 令 p=1 mod24 为素数，3<=a<=p-2、a=3 mod4，r,s 为正整数且 p 不整除 ars。若 X=(p+a)/4，且 Bado 主线性比例公式 Y=X(ps+r)/(as)、Z=pX(ps+r)/(ar) 都为整数，则 d=rX/s 是整数，d|X^2，且 (m,x,d)=(a,X,d) 是 Type I 证书，恢复分母正是 (X,Y,Z)。故每个固定 (a,r,s) 主族在自然范围内只是固定缺口 Type I 证书的一个同余切片。
claim_status: established
topics:
- certificate
- type-I
- congruence-family
- fixed-gap
- translation
- proof-program
sources:
- paper: linear_ratio_ansatz2026
  locator: "Lemma 3.1, Corollary 3.2, Proposition 4.1"
  role: original-ansatz-and-Type-I-context
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-24'
---

# 线性比例主族精确等价于固定缺口 Type I 证书

## 定理

设

\[
p\equiv1\pmod {24},\qquad
3\le a\le p-2,\qquad a\equiv3\pmod4,\qquad
r,s\in\mathbb N,\qquad p\nmid ars. \tag{1}
\]

令

\[
X=\frac{p+a}{4}. \tag{2}
\]

假设 Bado 主线性比例公式中的

\[
Y=\frac{X(ps+r)}{as},\qquad
Z=\frac{pX(ps+r)}{ar} \tag{3}
\]

都是正整数。则

\[
d=\frac{rX}{s} \tag{4}
\]

是正整数且 \(d\mid X^2\)，并且

\[
a\mid pX+d. \tag{5}
\]

所以 \((m,x,d)=(a,X,d)\) 是 \(p\) 的 Type I 除子证书；Bradford 的恢复分母恰为

\[
\left(X,\frac{pX+d}{a},
\frac{p(X+pX^2/d)}a\right)=(X,Y,Z). \tag{6}
\]

## 证明

由 \(Y\in\mathbb N\)，

\[
aY=\frac{X(ps+r)}s=pX+\frac{rX}s. \tag{7}
\]

左侧和 \(pX\) 都是整数，故 (4) 中的 \(d\) 是整数，并立即得到 (5) 与
\(Y=(pX+d)/a\)。

又 \(Z\in\mathbb N\)，且 \(p\nmid ar\)，故

\[
ar\mid X(ps+r). \tag{8}
\]

特别地 \(r\mid X(ps+r)\)。因 \(\gcd(p,r)=1\)，模 \(r\) 化简 (8) 得

\[
r\mid sX. \tag{9}
\]

由 (4) 和 (9)，

\[
\frac{X^2}{d}=\frac{sX}{r}\in\mathbb N, \tag{10}
\]

即 \(d\mid X^2\)。最后，

\[
\frac{p(X+pX^2/d)}a
=\frac{pX(r+ps)}{ar}=Z, \tag{11}
\]

与 (3) 一致。式 (5)、(10) 和 (11) 正是 Type I 证书及其恢复公式。

## 有限覆盖边界

对固定原始 \((a,r,s)\)，(3) 的整数性只取决于

\[
p\bmod L(a,r,s),\qquad
L(a,r,s)=\operatorname{lcm}(24,4as,4ar). \tag{12}
\]

原稿 Lemma 5.1 证明残数 \(1\bmod L(a,r,s)\) 不会命中该三元组；对任意有限个三元组
合并这些模数后，Dirichlet 素数列同时逃过它们。这也直接解释了为什么此族不能成为本目标
所需的有限参数全称选择器。

## 边界

本翻译只处理主比例 \(Z/Y=ps/r\)。原稿的 shifted-ratio 变体需要不同的、随 \(p\)
变化的除子表达式；无论如何，它仍是固定参数的有限残数族，且论文没有声称递降或全覆盖。
