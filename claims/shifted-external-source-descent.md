---
kind: claim
claim_id: shifted-external-source-descent
title: 带平移参数的外部源严格递降
statement: 令 p=1 mod24 为素数，k,d>0，q=4k-1，n=(qp+d)/(q+1)。若 d<p、p=d mod4k、d|kn，且 n=f(qr-1) 对某个正因子 f 成立，则 (kn,kfr,knr) 是 4/n 的标记解，并严格提升为 (knp/d,kfr,knr) 的 4/p 解。同时 m=(4kf+d)/q、D=dkfr^2 是自然范围内的 Type I 证书，正规形为 (dr,1,kf/d)。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-equivalence
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# 带平移参数的外部源严格递降

## 定理

令 \(p\equiv1\pmod{24}\) 为素数，取正整数 \(k,d\)，并令

\[
q=4k-1,\qquad n=\frac{qp+d}{q+1}. \tag{1}
\]

设

\[
0<d<p,\qquad p\equiv d\pmod{4k},\qquad d\mid kn. \tag{2}
\]

若 \(n\) 有因子 \(f\)，使

\[
s=\frac nf\equiv-1\pmod q,\qquad r=\frac{s+1}{q}, \tag{3}
\]

则

\[
\frac4n
=\frac1{kn}+\frac1{kfr}+\frac1{knr}
\quad\Longrightarrow\quad
\frac4p
=\frac1{knp/d}+\frac1{kfr}+\frac1{knr}. \tag{4}
\]

这是严格的带标记提升，因为 \(n<p\)。此外

\[
x=kfr,\qquad
m=\frac{4kf+d}{q},\qquad
D=dkfr^2 \tag{5}
\]

是自然范围内的一张 Type I 证书，其互素正规形为

\[
(A,B,C)=\left(dr,1,\frac{kf}{d}\right). \tag{6}
\]

## 证明

由 \(4k=q+1\) 和 (2)，\(n\) 是整数，且

\[
p-n=\frac{p-d}{4k}>0,\qquad n\equiv d\pmod q. \tag{7}
\]

从 (3) 得 \(n=f(qr-1)\)，所以 \(f\equiv-d\pmod q\)。由
\(d\mid kn\)、(1) 及 \(d<p\)，有

\[
d\mid kq. \tag{8}
\]

又 \((k,q)=1\)、\((s,q)=1\)。按素因子幂次分别考察 (8) 的 \(k\)-部分和 \(q\)-部分：
前者被 \(k\) 吸收，后者不能整除 \(s\)，故必整除 \(f\)。因此

\[
d\mid kf. \tag{9}
\]

于是 (6) 中的 \(C\) 是正整数。与未平移情形一样，

\[
\frac1{kfr}+\frac1{knr}=\frac q{kn}.
\]

再由 \((q+1)n=qp+d\)，有

\[
\frac1{knp/d}+\frac q{kn}
=\frac{d+qp}{knp}
=\frac4p,
\]

从而得到 (4)。

由 \(f\equiv-d\pmod q\)，\(m\) 是整数。利用 \(n=f(qr-1)\) 计算，

\[
4x-p=m,\qquad ms-p=dr. \tag{10}
\]

故

\[
px+D=x(p+dr)=xms=m(knr).
\]

连同 (6) 即满足 Type I 正规形的全部条件。特别地，它恢复的两个其余分母正是
\(knr\) 与 \(knp/d\)。

最后，\(s\ge q-1\)、\(d\le kf\) 和 (10) 给出

\[
p-m=\frac{4kf(s-1)-2d}{q}\ge2. \tag{11}
\]

当 \(q\ge7\) 时 (11) 立即由 \(s-1\ge q-2\) 得出；当 \(q=3\) 时，
\(k=d=1\)、\(f\ge2\)，也直接成立。又 \(m=4x-p\equiv3\pmod4\) 且为正，
所以 \(3\le m\le p-2\)。

## 新例子

取

\[
p=2473,\qquad k=7,\qquad d=9,\qquad q=27,\qquad n=2385=45\cdot53.
\]

此时 \(r=2\)，因此

\[
\frac4{2385}
=\frac1{16695}+\frac1{630}+\frac1{33390}
\quad\Longrightarrow\quad
\frac4{2473}
=\frac1{4586415}+\frac1{630}+\frac1{33390}.
\]

这里第一项精确为 \(knp/d=4{,}586{,}415\)，并且

\[
(m,D)=(47,11340),\qquad(A,B,C)=(18,1,35).
\]

该例给出一个 (d=9) 的不同参数化递降见证；它不应被解读为已经证明
该素数不被完整的 (d=1) 自适应族覆盖。

## 边界

令 \(d=1\) 时，本定理退化为 adaptive-external-source-descent。一般 \(d\) 给出更多
可验证的参数化见证，但尚未证明其逐点覆盖严格大于完整的 \(d=1\) 自适应族，亦没有
证明每个核心素数都有满足 (2)--(3) 的参数。因此它不是全称选择器。
