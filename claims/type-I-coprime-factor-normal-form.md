---
kind: claim
claim_id: type-I-coprime-factor-normal-form
title: Type I 除子证书的互素因子正规形
statement: 固定核心素数 p 与合法缺口 m，令 x=(p+m)/4。Type I 证书除子 d 与满足 x=ABC、d=A^2C、gcd(A,B)=1、m|(Bp+A) 的三元组 (A,B,C) 一一对应；这等价于 Elsholtz--Tao 参数化在自然缺口范围 0<f<p 内的互素化，且外部源条件恰为 B=a=1。
claim_status: established
topics:
- certificate
- type-I
- divisor-parametrization
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: standard-Type-I-parametrizations
- paper: bello2026
  locator: "equation (13) and Remark 7"
  role: Mordell-parameter-comparison
visibility: public
last_checked: '2026-07-23'
---

# Type I 除子证书的互素因子正规形

## 定理

令 \(p\equiv1\pmod{24}\) 是素数，\(m\equiv3\pmod4\)、
\(3\le m\le p-2\)，并令 \(x=(p+m)/4\)。则 Type I 证书除子 \(d\) 与三元组
\((A,B,C)\in\mathbb N^3\) 一一对应，条件为

\[
x=ABC,\qquad d=A^2C,\qquad \gcd(A,B)=1,
\qquad m\mid Bp+A.
\]

因此也可把存在性写成：存在互素正整数 \(A,B\)，使

\[
4AB\mid p+m,\qquad m\mid Bp+A,
\]

其中 \(C=(p+m)/(4AB)\)。由 \(p=4ABC-m\) 还得到 Mordell 型恒等式

\[
(4BCD-1)A=(B+D)p,\qquad D=\frac{Bp+A}{m}.
\]

`external-source-type-I-certificate` 恰是 \(B=1\) 的子类；此时 \(A=i\)、
\(C=x/i\)，两个条件变为 \(m\mid p+i\)、\(4i\mid p+m\)。

## 证明

先给定 Type I 证书 \(d\mid x^2\)、\(m\mid px+d\)。令

\[
g=\gcd(d,x),\qquad A=\frac dg,\qquad B=\frac xg.
\]

则 \(\gcd(A,B)=1\)。由 \(d\mid x^2\) 得

\[
Ag\mid B^2g^2,
\]

故 \(A\mid B^2g\)。互素性推出 \(A\mid g\)，令 \(C=g/A\)。于是

\[
x=ABC,\qquad d=A^2C.
\]

又

\[
px+d=AC(Bp+A).
\]

因为 \(\gcd(x,m)=1\)，也有 \(\gcd(AC,m)=1\)，所以 Type I 同余条件等价于
\(m\mid Bp+A\)。这给出正向映射。

反向地，上述等式保证 \(d=A^2C\mid A^2B^2C^2=x^2\)，并且
\(m\mid AC(Bp+A)=px+d\)。所以它确实是 Type I 证书。由 \(g=AC\) 可反向恢复
\(A=d/g\)、\(B=x/g\)、\(C=g/A\)，从而映射唯一。

最后，令 \(D=(Bp+A)/m\)。利用 \(p=4ABC-m\) 化简

\[
A(4BCD-1)=4ABCD-A=D(p+m)-A=Dp+(mD-A)=(B+D)p.
\]

## 与 Elsholtz--Tao 参数化的精确桥接

Elsholtz--Tao Proposition 2.3 的一个 Type I 等价条件是存在正整数
\((a,c,d,f)\)，使

\[
p=4acd-f,\qquad f\mid4a^2d+1,\qquad \gcd(c,p)=1.
\]

该命题本身不限制 \(f\) 的大小。为了与短缺口框架比较，以下只取
\(0<f<p\) 的参数点。对 \(p\equiv1\pmod4\)，此时自动有
\(f\equiv3\pmod4\)，故 \(f\) 是合法缺口。取 \(f=m\)、\(x=acd\)，
则 Bradford 证书正是

\[
d_{\mathrm{cert}}=c^2d.
\]

事实上，\(d_{\mathrm{cert}}\mid x^2\)，并且模 \(f\) 有

\[
px+d_{\mathrm{cert}}
 \equiv4a^2c^2d^2+c^2d
 =c^2d(4a^2d+1)\equiv0.
\]

若 \(h=\gcd(a,c)\)，把该证书代入上面的正规化映射，得到

\[
A=\frac ch,\qquad B=\frac ah,\qquad C=dh^2.
\]

反过来，从任意正规三元组取

\[
a=B,\qquad c=A,\qquad d=C,\qquad f=m,
\]

便有 \(p=4acd-f\)。又由 \(m\mid Bp+A\) 及 \(p=4ABC-m\) 得

\[
m\mid A(4B^2C+1).
\]

因为 \(A\mid x\) 且 \(\gcd(x,m)=1\)，可消去 \(A\)，所以
\(m\mid4B^2C+1\)。这正是上述 Elsholtz--Tao 条件；\(A\mid x<p\)
也给出 \(\gcd(A,p)=1\)。故正规三元组与满足 \(\gcd(a,c)=1\) 的该组
Elsholtz--Tao 坐标（再加 \(0<f<p\)）一一对应。

特别地，Elsholtz--Tao 的 \(a=1\) 切片恰对应 \(B=1\)，也就是外部源。
因此文献中对 \(a=1\) 子族的高效计算覆盖，并不自动控制全部 Type I 情形：
真正剩余的自由度是 \(B>1\)。

## 对证明计划的含义

这不是对每个 \(p\) 的存在性证明，而是把 Type I 的全部自由度显式分成互素的
\((A,B)\)。外部源只控制 \(B=1\)，其有限窗口遗漏不能说明一般 Type I 无证书；
反之，要把该路线闭合，必须为所有残余素数构造某个 \((A,B)\)，或证明其能归约到
真正的可提升递降实例。
