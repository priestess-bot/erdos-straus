---
kind: claim
claim_id: type-I-affine-uniform-divisor-rigidity
title: 统一仿射 Type I 平方除子的有限缺口刚性
statement: 令 p(n)=4E(un+v)-m 是原始正仿射进程，m 为奇数，gcd(E,m)=1，gcd(u,v)=1；令 x(n)=E(un+v)。若正非恒定仿射 d(n) 对全部 n 满足 d(n)|x(n)^2 和 m|p(n)x(n)+d(n)，则唯一有 a|E^2 使 d(n)=a(un+v)，并且 m|u、a=-4E^2v modm。反之这些条件充分。故对固定进程，统一仿射 Type I 家族只需枚举 m|S/E 及 E^2 的除子残数；不需要 Type II 的 a<=E 限制。
claim_status: established
topics:
- type-I
- arithmetic-progression
- affine-rigidity
- square-divisor
- divisor-parametrization
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 统一仿射 Type I 平方除子的有限缺口刚性

## 定理

令

\[
p(n)=4E(un+v)-m,\qquad x(n)=E(un+v),
\]

其中 \(m\) 是正奇数，\(\gcd(E,m)=1\)，\(\gcd(u,v)=1\)。设

\[
d(n)=An+B
\]

是正的非恒定整数仿射函数。若对所有 \(n\ge0\)，

\[
d(n)\mid x(n)^2,\qquad m\mid p(n)x(n)+d(n), \tag{1}
\]

则唯一存在正整数 \(a\) 使

\[
d(n)=a(un+v),\qquad a\mid E^2, \tag{2}
\]

并且

\[
mmid u,\qquad a\equiv-4E^2vpmod m. \tag{3}
\]

反之，(2)--(3) 蕴含 (1)。与 Type II 不同，这里不要求 \(a\le E\)。

## 证明

记 \(S=Eu,T=Ev\)。由恒等式

\[
A x(n)=S d(n)+(AT-SB)
\]

和 \(d(n)\mid x(n)^2\)，得到 \(d(n)\mid(AT-SB)^2\)。正非恒定的
\(d(n)\) 无界，故 \(AT-SB=0\)。这给出比例性；由于 \(u,v\) 互素，唯一可写为

\[
d=a(un+v).
\]

再由 \(d\mid x^2\) 对全部参数成立，取 \(un+v\) 的所有值的最大公因子为一，得到
\(a\mid E^2\)。

将 (2) 代入第二个整除式，并模 \(m\) 化简，得到二次多项式

\[
(un+v)\bigl(4E^2(un+v)+a\bigr)\equiv0pmod m. \tag{4}
\]

因 \(m\) 为奇数，(4) 对全部 \(n\) 成立当且仅当其三个整系数均被 \(m\) 整除。
二次项先给出 \(m\mid u^2\)，这里使用 \(\gcd(E,m)=1\)。又 \(\gcd(u,v)=1\)，故
\(\gcd(v,m)=1\)。常数项随即给出

\[
a\equiv-4E^2vpmod m.
\]

把它代入一次项，得到 \(m\mid4E^2uv\)，故 \(m\mid u\)。反向代入 (4) 即完成证明。

## 对原始进程的有限化

若从原始进程 \(p=Pn+C\) 和自然缺口 \(m\) 开始，写

\[
x=\frac{p+m}{4}=Sn+T,\qquad E=\gcd(S,T),\qquad u=S/E, v=T/E,
\]

则 \(m\mid u\) 特别推出 \(m\mid S\)。此外若某素数整除 \(E,m\)，它同时整除
\(P=4S\) 与 \(C=4T-m\)，与原始性矛盾；所以 \(\gcd(E,m)=1\) 自动成立。
因此固定原始进程上的全部统一仿射 Type I 证书，均由

\[
m\mid S/E,\qquad a\mid E^2,\qquad a\equiv-4E^2(T/E)\pmod m
\]

的有限枚举决定。

该引理只处理参数全程有效的仿射除子；它不排除非仿射除子或随参数改变的缺口。
