---
kind: claim
claim_id: adaptive-external-source-descent
title: 自适应外部源 Type I 证书的严格递降族
statement: 令 p=1 mod24 为素数，k|(p-1)/4，q=4k-1，n=(qp+1)/(q+1)。若 n 有因子 f=-1 modq，则取 f<=n/f、r=(n/f+1)/q，可显式构造 4/n 的标记解 (kn,kfr,knr)，并将其严格提升为 4/p 的解 (knp,kfr,knr)。同时 m=(4kf+1)/q、d=kfr^2 是 Type I 除子证书，且 m<=4sqrt(p)/3+1/3。
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

# 自适应外部源 Type I 证书的严格递降族

## 定理

令 \(p\equiv1\pmod{24}\) 为素数，取

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1}. \tag{1}
\]

于是 \(2\le n<p\) 且 \(n\equiv1\pmod q\)。若 \(n\) 有因子

\[
f\equiv-1\pmod q, \tag{2}
\]

则可把 \(f\) 替换为 \(n/f\)，故不妨令 \(f\le n/f\)。定义

\[
r=\frac{n/f+1}{q},\qquad
x=kfr,\qquad
m=\frac{4kf+1}{q},\qquad
d=kfr^2. \tag{3}
\]

则 \(r,m\) 都是正整数，且

\[
\frac4n
=\frac1{kn}+\frac1{kfr}+\frac1{knr}
\quad\Longrightarrow\quad
\frac4p
=\frac1{knp}+\frac1{kfr}+\frac1{knr}. \tag{4}
\]

因而 (4) 是一条到严格更小实例 \(n<p\) 的带标记提升边。与此同时
\((m,d)\) 是缺口 \(m\) 的 Type I 除子证书，互素正规形为

\[
(A,B,C)=(r,1,kf), \tag{5}
\]

并满足

\[
3\le m\le\frac{4\sqrt p+1}{3}\le p-2. \tag{6}
\]

## 证明

由 \(4k=q+1\) 和 \(4k\mid p-1\)，(1) 中的 \(n\) 是整数。并且

\[
p-n=\frac{p-1}{4k}>0,\qquad n\equiv1\pmod q. \tag{7}
\]

若 \(f\) 满足 (2)，则 \(s=n/f\equiv-1\pmod q\)。故

\[
r=\frac{s+1}{q}\in\mathbb N,\qquad n=f(qr-1). \tag{8}
\]

直接计算给出

\[
\frac1{kfr}+\frac1{knr}
=\frac{n+f}{kfnr}
=\frac{q}{kn}.
\]

加上 \(1/(kn)\) 即为 \(4/n\)，因为 \(q+1=4k\)。又由
\((q+1)n=qp+1\)，有

\[
\frac1{knp}+\frac q{kn}
=\frac{1+qp}{knp}
=\frac4p,
\]

所以 (4) 给出显式严格提升。

由 (3) 及 (8)，

\[
4x-p=\frac{4kf+1}{q}=m, \tag{9}
\]

而 \(q\mid4kf+1\) 正来自 \(f\equiv-1\pmod q\)。以 (5) 代入
Type I 互素正规形，只须检验 \(m\mid p+r\)。事实上

\[
ms-p=r,\qquad s=\frac nf,
\]

所以

\[
px+d=px+xr=x(p+r)=xms=m(k n r),
\]

证明了 Type I 条件；恢复的两个其余分母正是 (4) 中的 \(knr\) 与 \(knp\)。

由于 \(n\equiv1\pmod q\)，若 \(f\) 满足 (2)，其互补因子 \(n/f\) 也满足
(2)，故可取 \(f\le\sqrt n\)。再由 \(q\ge3\) 和 \(n<p\)，

\[
m=\frac{(q+1)f+1}{q}
\le\frac{4\sqrt n+1}{3}
\le\frac{4\sqrt p+1}{3}.
\]

核心素数的最小值为 \(73\)，故最后一项不超过 \(p-2\)。式 (9) 还给出
\(m\equiv-p\equiv3\pmod4\)，所以 \(m\ge3\)，证毕。

## 例子

\[
\begin{array}{c|c|c|c|c|c}
p&k&q&n&f&r\\
\hline
193&2&7&169&13&2\\
1489&3&11&1365&21&6\\
1033&6&23&990&22&2\\
1777&4&15&1666&14&8
\end{array}
\]

第一行给出

\[
\frac4{169}=\frac1{338}+\frac1{52}+\frac1{676}
\quad\Longrightarrow\quad
\frac4{193}=\frac1{65234}+\frac1{52}+\frac1{676},
\]

以及 \((m,d)=(15,104)\) 的 Type I 证书。最后一行说明 \(q\) 不必为素数；
素数性只在后续把失败条件转成半大小残数横截面时才有用。

当 \(k=1\) 时，\(q=3\)，这正是已有的 q=3 递降族。对核心素数恒可选的
\(k=2,3,6\) 分别给出 \(q=7,11,23\) 的补充分支；允许所有
\(k\mid(p-1)/4\) 则是自适应扩张，而非固定有限模板。

## 边界

该定理并未证明每个 \(p\) 至少有一个允许的 \(k\) 和因子 \(f\)。例如
\(p=97\) 对所有 \(k\mid24\) 都不满足 (2)。因此它是目标引理的一条可验证、
平方根级的直接证书和递降分支，而不是全称选择器。
