---
kind: claim
claim_id: scaled-source-descent-rigidity
title: 缩放一坐标提升的四分母刚性与非倍数 Type I 递降
statement: 设 p=1 mod24 为素数，2<=n<p，且 4/n=1/A+R、4/p=1/(Ap/d)+R，其中 0<d<p 且 Ap/d 为整数。将 A/n=a/b 约为最简分数，则 b|4。故除 A=an 外，缩放型一坐标递降只可能有 A=an/2 或 A=an/4 两种非倍数源。对 b∈{1,2,4}，若 b(p-d)=4at、n=p-t、b|n、d|an/b，并且 (an)^2 的因子 e 满足完整二项尾同余、bd|e 和自然缺口范围，则显式构造严格提升及 Type I 证书。
claim_status: established
topics:
- descent
- certificate
- type-I
- unit-fractions
- factorization
- rigidity
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-24'
---

# 缩放一坐标提升的四分母刚性与非倍数 Type I 递降

## 比例刚性

设 \(p\equiv1\pmod{24}\) 是素数，\(2\le n<p\)，并设有相同的两项尾 \(R\)：

\[
\frac4n=\frac1A+R,\qquad
\frac4p=\frac1{Ap/d}+R. \tag{1}
\]

其中 \(A,d\) 是正整数、\(0<d<p\)，且 \(Ap/d\) 为整数。把

\[
\frac An=\frac ab,\qquad \gcd(a,b)=1 \tag{2}
\]

约为最简分数。则

\[
b\mid4. \tag{3}
\]

### 证明

从 (1) 相减，得到

\[
4A(p-n)=n(p-d). \tag{4}
\]

由于 \(A=an/b\)，有 \(b\mid n\)；将其代入 (4) 得

\[
4a(p-n)=b(p-d). \tag{5}
\]

令 \(g=\gcd(b,4)\)。由 \(\gcd(a,b)=1\)，(5) 蕴含
\(b/g\mid p-n\)。而 \(b/g\mid n\)，故 \(b/g\mid p\)。
又 \(b/g\le b\le n<p\)，素数性迫使 \(b/g=1\)，即 \(b\mid4\)。

因此，在这一“只缩放被替换分母、保留同一二项尾”的一般模型中，源首分母只有

\[
A=an,\qquad A=\frac{an}{2},\qquad A=\frac{an}{4}. \tag{6}
\]

前者是已分类的 \(M=kn\) 外部源；后两者是所有真正的新比例源。

## 统一的平方因子构造

取

\[
b\in\{1,2,4\},\qquad \gcd(a,b)=1,\qquad 0<d<p, \tag{7}
\]

并设存在正整数 \(t\) 使

\[
b(p-d)=4at,\qquad n=p-t,\qquad b\mid n,\qquad
d\mid\frac{an}{b}. \tag{8}
\]

记

\[
L=an,\qquad A=\frac{L}{b},\qquad q=4a-b>0. \tag{9}
\]

若存在正整数 \(e\) 满足

\[
e\mid L^2,\quad e\le L,\quad bd\mid e,\quad
q\mid L+e,\quad q\mid L+\frac{L^2}{e}, \tag{10}
\]

并且以下缺口在自然范围内，

\[
u=\frac{L+e}{q},\qquad
m=\frac{4e+bd}{q}=4u-p,\qquad
3\le m\le p-2, \tag{11}
\]

则令

\[
v=\frac{Lu}{e},\qquad D=\frac{bd\,u^2}{e}, \tag{12}
\]

有严格提升

\[
\frac4n=\frac1A+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{Ap/d}+\frac1u+\frac1v, \tag{13}
\]

且 \((m,D)\) 是 Type I 除子证书。

### 证明

由 (10)，\(u,v\) 都是正整数，并且

\[
\frac1u+\frac1v=\frac{L+e}{Lu}=\frac qL.
\]

因此左式为

\[
\frac bL+\frac{4a-b}{L}=\frac4n.
\]

由 (8) 得

\[
4L=qp+bd. \tag{14}
\]

所以右式为

\[
\frac{d}{Ap}+\frac qL
=\frac{bd+qp}{Lp}
=\frac4p.
\]

式 (14) 也立即给出 (11) 中 \(m=4u-p\)。再计算

\[
mv-pu
=u\left(\frac{L(4e+bd)}{qe}-p\right)
=\frac{bd\,u(L+e)}{qe}=D. \tag{15}
\]

由于 \(bd\mid e\)，有 \(D=u^2/(e/(bd))\mid u^2\)。最后，

\[
qbd\left(u+\frac{pe}{bd}\right)
=bd(L+e)+pqe
=L(bd+4e)
=qmL. \tag{16}
\]

故 Type I 的两个恢复分母正是

\[
\frac{pu+D}{m}=v,\qquad
\frac{p(u+pu^2/D)}m=\frac{pL}{bd}=\frac{Ap}{d}.
\]

所以 \((m,D)\) 是所需证书，(13) 是严格递降。

## 新比例例子

取

\[
p=80809,\quad a=67,\quad b=2,\quad d=7,\quad t=603,\quad n=80206.
\]

此时 \(A=an/b=2686901\)、\(q=266\)、\(e=4718\)。构造给出

\[
\frac4{80206}
=\frac1{2686901}+\frac1{20220}+\frac1{23030580}
\]

以及

\[
\frac4{80809}
=\frac1{31017968987}+\frac1{20220}+\frac1{23030580},
\]

并恢复 Type I 证书

\[
(m,D)=(71,1213200).
\]

这个 \(p\) 不命中先前固定 \(M=kn\) 的零平移或非零平移平方因子尾项；这里的
\(A=67n/2\) 因而提供了真正不同的源。

当 \(d=1\) 时，两个非倍数比例均被奇偶性排除：若 \(b=2\)，则 \(n\) 偶迫使
\(t,a\) 都为奇数，而 \(p-1=2at\) 与 \(p\equiv1\pmod4\) 矛盾；若 \(b=4\)，
则 \(n\equiv0\pmod4\) 迫使 \(t\) 与 \(a\) 为奇数，而 \(p-1=at\) 不可能。
所以新的比例源本质上需要非零平移。

## 边界

式 (3) 只分类目标分母是 \(Ap/d\) 的一坐标缩放提升；它不排除一般
two-denominator-lift-criterion 的替换分母。式 (10)--(11) 也没有构造所有
\(p\) 都成功的 \(a,b,d,e\) 选择器。因此该结论显著缩小了下一搜索空间，但仍不是
目标引理的全称证明。
