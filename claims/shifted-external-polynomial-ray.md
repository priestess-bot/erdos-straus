---
kind: claim
claim_id: shifted-external-polynomial-ray
title: 平移外部源的固定因子多项式递降射线
statement: 令 d,r,s 为正整数，r>=2、s>=1、dr=3 mod4，k=(dr+1)/4，f=d(r-1)，n=f(drs-1)，p=d^2r^2s-d(d-1)rs-ds-dr+d-1。若 p>d 且 p 是 p=1 mod24 的素数，则 4/n 的显式标记解 (kn,kfs,kns) 严格提升为 4/p 的 (knp/d,kfs,kns)，并给出 gap m=d(r-1)+1、x=kfs、D=dkfs^2 的 Type I 证书。该射线在 p=31849 上命中，而完整未平移 adaptive 外部源族失败。
claim_status: established
topics:
- descent
- certificate
- type-I
- external-source
- polynomial-family
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-certificate-equivalence
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# 平移外部源的固定因子多项式递降射线

## 定理

取正整数

\[
d,\ r,\ s,\qquad r\ge2,\quad s\ge1,\quad dr\equiv3\pmod4, \tag{1}
\]

并定义

\[
\begin{aligned}
q&=dr, &
k&=\frac{dr+1}{4}, &
f&=d(r-1),\\
n&=d(r-1)(drs-1), &
p&=d^2r^2s-d(d-1)rs-ds-dr+d-1. \tag{2}
\end{aligned}
\]

若 \(p>d\) 且 \(p\equiv1\pmod{24}\) 是素数，则

\[
\frac4n
=\frac1{kn}+\frac1{kfs}+\frac1{kns}
\quad\Longrightarrow\quad
\frac4p
=\frac1{knp/d}+\frac1{kfs}+\frac1{kns} \tag{3}
\]

是一条严格的带标记递降边。其目标 Type I 证书为

\[
m=d(r-1)+1,\qquad x=kfs,\qquad D=dkfs^2. \tag{4}
\]

## 证明

条件 (1) 使 \(k\) 为正整数，且 \(q=4k-1\)。由 (2)，有

\[
n=f(qs-1). \tag{5}
\]

直接整理 \(p\) 的多项式，得到

\[
p-n=ds(r-1)-1,\qquad
p-d=4k\bigl(ds(r-1)-1\bigr), \tag{6}
\]

以及

\[
qp+d=4kn. \tag{7}
\]

因 \(p>d\)，(6) 给出 \(n<p\)、\(p\equiv d\pmod{4k}\)。又 \(d\mid n\mid kn\)，
而 (5) 的互补因子是 \(qs-1\)。所以它恰满足 shifted-external-source-descent
的因子条件；将该定理中的参数 \((k,d,f,s)\) 代入，即得 (3)。

同一代入给出

\[
m=\frac{4kf+d}{q}
=\frac{(dr+1)d(r-1)+d}{dr}
=d(r-1)+1, \tag{8}
\]

以及 \(x=kfs\)、\(D=dkfs^2\)。因此 (4) 是 Type I 证书；自然缺口范围
由一般平移外部源定理给出。

## 与未平移族的严格有限分离

取

\[
(d,r,s)=(5,15,6).
\]

则

\[
(p,k,n,f,m)=(31849,19,31430,70,71), \tag{9}
\]

其源解是

\[
\frac4{31430}
=\frac1{597170}+\frac1{7980}+\frac1{3583020}.
\]

证书数据为

\[
(m,x,D)=(71,7980,239400). \tag{10}
\]

test_shifted_external_polynomial_ray 同时精确枚举所有
\(k\mid(p-1)/4\) 的未平移 adaptive 外部源条件，并确认它们在
\(p=31849\) 全部失败。故这条平移射线相对于完整未平移 adaptive 族确有严格的
有限扩张。

## 有限射线障碍

固定一对 \((d,r)\) 后，令

\[
T=d(r-1)(dr+1)=4kf,\qquad m=d(r-1)+1. \tag{11}
\]

式 (2) 恰可改写为

\[
p=Ts-m. \tag{12}
\]

而 \(dr\equiv3\pmod4\) 蕴含 \(f\ge2\)，所以

\[
0<m+1=f+2<T. \tag{13}
\]

因此任取有限多对 \((d,r)\)，令 \(M\) 为 \(24\) 与相应所有 \(T\) 的最小公倍数。
对任何素数 \(p\equiv1\pmod M\)，若它落在某条 (12) 射线上，则
\[
T\mid p+m\quad\Longrightarrow\quad T\mid m+1,
\]
这与 (13) 矛盾。Dirichlet 定理给出无穷多个这样的核心素数。

所以有限叠加这些固定因子多项式射线不可能完成目标猜想；一个可能的全称选择器
必须让 \((d,r)\) 真正随 \(p\) 增长，或转向不同的递降机制。

## 边界

该定理是 shifted-external-source-descent 的一个固定因子子族，而不是新的全称
存在性定理。它只在多项式 (2) 取到核心素数时给出边，且没有证明每个残余
\(p\) 都可反向写成这种形式。它扩张了可用的标记递降图，但尚未提供全局选择器。
