---
kind: claim
claim_id: p-minus-one-source-descent
title: p 减一源的完整平移平方因子递降扇
statement: 设 p=1 mod24 为素数。p-1 的每个 d=1 mod4 因子产生一个严格递降源 n=p-1；写 s=(p-1)/d、r=s-1、k=(p-d)/4、M1=ks。该源上的全部可恢复 Type I 的平移平方因子尾，恰由 e1|M1^2、e1<=M1、e1=-M1 modr 参数化，并给出 4/(p-1) 到 4/p 的显式提升与自然范围 Type I 证书。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- factorization
- p-minus-one
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-reconstruction
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# \(p-1\) 源的完整平移平方因子递降扇

## 定理

设 \(p\equiv1\pmod{24}\) 为素数。取任意满足

\[
d\mid p-1,\qquad d\equiv1\pmod4, \tag{1}
\]

的正因子，并定义

\[
s=\frac{p-1}{d},\qquad r=s-1,\qquad
k=\frac{p-d}{4},\qquad M_1=ks. \tag{2}
\]

则 \(r\) 为正奇数，且

\[
4M_1=rp+1,\qquad (r,M_1)=1. \tag{3}
\]

若有正整数 \(e_1\) 满足

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad
e_1\equiv-M_1\pmod r, \tag{4}
\]

令

\[
u=\frac{M_1+e_1}{r},\qquad
v=\frac{M_1u}{e_1},\qquad
m=\frac{4e_1+1}{r},\qquad D=\frac{u^2}{e_1}. \tag{5}
\]

则这些量均为正整数，\(3\le m\le p-2\)，并有严格提升

\[
\frac4{p-1}
=\frac1{dM_1}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p
=\frac1{pM_1}+\frac1u+\frac1v. \tag{6}
\]

同时 \((m,D)\) 是 \(p\) 的 Type I 除子证书，首分母为 \(u\)。

反过来，完整平移平方因子外部源递降的所有见证中，源分母恰为 \(p-1\) 的部分都唯一来自
(1)--(4)。因此 (4) 不是这个源上的额外限制，而是该完整平移平方因子扇的精确单同余
参数化。

## 证明

由 (1) 写 \(p-1=ds\)。因 \(p,d\equiv1\pmod4\)，\(k\) 为整数，且

\[
4k=p-d=d(s-1)+1=dr+1. \tag{7}
\]

于是

\[
4M_1=4ks=s(dr+1)=rp+1.
\]

又 \(s=2\) 会使 \(d=(p-1)/2\) 被 \(4\) 整除，与 (1) 矛盾，故 \(r=s-1>1\)。
\((r,s)=1\)，且任意同时整除 \(r,k\) 的数由 (7) 整除 \(1\)，故
\((r,M_1)=(r,ks)=1\)，证明 (3)。

由 (4) 和互素性，互补因子也满足

\[
\frac{M_1^2}{e_1}\equiv-M_1\pmod r. \tag{8}
\]

所以 \(u,v\) 都是整数。又 \(e_1\mid M_1^2\) 与
\(r\mid M_1+e_1\) 蕴含 \(e_1\mid u^2\)，故 \(D\) 为整数。直接计算

\[
\frac1u+\frac1v=\frac r{M_1}.
\]

连同 (3) 即给出 (6) 的两端：

\[
\frac1{dM_1}+\frac r{M_1}
=\frac{dr+1}{dM_1}=\frac4{ds}=\frac4{p-1},
\qquad
\frac1{pM_1}+\frac r{M_1}=\frac4p.
\]

再由 (3) 与 (5)，

\[
4u-p=\frac{4e_1+1}{r}=m. \tag{9}
\]

为验证自然范围，注意 \(e_1=M_1\) 会与 \((r,M_1)=1\) 及 (4) 矛盾。并且

\[
M_1-e_1\equiv2M_1\equiv\frac{r+1}{2}\pmod r,
\]

故 \(M_1-e_1\ge(r+1)/2\)。利用 (3) 得

\[
p-m=\frac{4(M_1-e_1)-2}{r}\ge2. \tag{10}
\]

式 (9) 还给出 \(m\equiv3\pmod4\)，因此 \(3\le m\le p-2\)。

最后，

\[
m v-pu
=u\left(\frac{M_1(4e_1+1)}{re_1}-p\right)
=\frac{u(M_1+e_1)}{re_1}=D,
\]

且 \(u^2/D=e_1\)。另有

\[
u+pe_1
=\frac{M_1+e_1+(4M_1-1)e_1}{r}
=\frac{M_1(4e_1+1)}{r}
=mM_1. \tag{11}
\]

因此 Bradford 的两个 Type I 恢复式分别给出

\[
\frac{pu+D}{m}=v,\qquad
\frac{p(u+pu^2/D)}m=pM_1,
\]

恰恢复 \((u,v,pM_1)\)。这证明证书断言。

对于反向的完整性，原平移参数满足 \(n=p-1\) 时必有

\[
d=p-4k,\qquad q=4k-1=d(s-1)=dr,\qquad M=kn=dM_1.
\]

原条件 \(d\mid e\) 写作 \(e=de_1\)。它的第二个尾项同余迫使
\(d\mid M^2/e\)；代入 \(M=dM_1\) 得 \(e_1\mid M_1^2\)。第一个同余则化为
\(r\mid M_1+e_1\)，而 (3) 自动推出互补同余 (8)。所以原见证恰恢复 (4)--(5)，
并且参数由 \(d,e_1\) 唯一决定。

## 例子与边界

对

\[
p=313,\qquad d=13,\qquad s=24,\qquad r=23,\qquad
k=75,\qquad M_1=1800,
\]

可取 \(e_1=40\)。由 (5) 得

\[
(m,D)=(7,160),
\]

并有

\[
\frac4{312}
=\frac1{23400}+\frac1{80}+\frac1{81000}
\quad\Longrightarrow\quad
\frac4{313}
=\frac1{563400}+\frac1{80}+\frac1{81000}.
\]

在 \(p\le10^4\) 的 143 个核心素数中，此扇命中 64 个；这只是有限审计。
其失败仍是因子 \(e_1\) 的逐点存在问题，因此没有完成目标引理。
