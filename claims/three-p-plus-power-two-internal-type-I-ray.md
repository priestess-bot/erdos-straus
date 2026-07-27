---
kind: claim
claim_id: three-p-plus-power-two-internal-type-I-ray
title: 来自 3p+A 的幂二内部 Type I 射线
statement: 令 A=2^a>=4。对核心素数 p=1 mod24，若 m|3p+A 且 m=-p mod12A，则 x=(p+m)/4、d=A(p+m)/12 是自然缺口范围内的 Type I 证书，且其互素正规形为 (A,3,(p+m)/(12A))。每个这样的 m 都满足 m<=(3p+A)/(11A-3)<=p-2。
claim_status: established
topics:
- certificate
- type-I
- internal-parameter
- factorization
- ray
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-23'
---

# 来自 \(3p+A\) 的幂二内部 Type I 射线

## 定理

令

\[
A=2^a\ge4,
\]

且 \(p\equiv1\pmod{24}\) 为素数。若 \(m\) 是 \(3p+A\) 的正因子，满足

\[
m\equiv-p\pmod{12A}, \tag{1}
\]

则

\[
x=\frac{p+m}{4},\qquad
d=\frac{A(p+m)}{12} \tag{2}
\]

构成缺口 \(m\) 的 Type I 除子证书。令

\[
C=\frac{p+m}{12A};
\]

则其互素正规形为

\[
x=A\cdot3\cdot C,\qquad d=A^2C,\qquad(A,3)=1. \tag{3}
\]

所有这样的见证都满足

\[
3\le m\le\frac{3p+A}{11A-3}\le p-2. \tag{4}
\]

## 证明

由 (1)，\(C\) 是正整数，且 (3) 立即给出 \(d\mid x^2\)，因为

\[
\frac{x^2}{d}=9C.
\]

又

\[
px+d=3ACp+A^2C=AC(3p+A),
\]

故 \(m\mid px+d\)。这正是 Type I 条件；等价地，在
`type-I-coprime-factor-normal-form` 中，条件为

\[
m\mid3p+A=Bp+A.
\]

设 \(h=(3p+A)/m\)。因 \(p\equiv1\pmod{12}\) 且 \(m\equiv-p\pmod{12A}\)，有

\[
\begin{aligned}
mh
&=3p+A\\
&\equiv-p(11A-3)\pmod{12A}.
\end{aligned}
\]

这里最后一步用 \(-11Ap\equiv-11A\equiv A\pmod{12A}\)。由于 \(m\) 是单位，

\[
h\equiv11A-3\pmod{12A}.
\]

而 \(0<11A-3<12A\)，故 \(h\ge11A-3\)，给出 (4) 的中间不等式。又
\(m\equiv-p\equiv3\pmod4\)，所以 \(m\ge3\)；最后

\[
(11A-3)(p-2)-(3p+A)
=(11A-6)p-23A+6>0
\]

对 \(A\ge4,p\ge5\) 成立，故 \(m\le p-2\)。

## 残数配对

记 \(M=12A\)、\(N=3p+A\)、\(t=-p\pmod M\)。因为 \(A\) 是 \(2\) 的幂，
\(N\) 为奇数且 \(N\equiv A\not\equiv0\pmod3\)，所以 \(N\) 的全部素因子均在

\[
G_A=(\mathbb Z/M\mathbb Z)^\times
\]

中。另一方面 \(t\equiv-p\equiv7\pmod8\)，而任何奇数平方模 \(8\) 都为 \(1\)。
所以 \(t\) 在 \(G_A\) 中没有平方根。

于是反演平移

\[
r\longmapsto tr^{-1}
\]

把 \(G_A\) 分割为 \(\varphi(M)/2\) 个无固定点的二元组。若 \(N\) 含来自同一
二元组的两种素因子残数，其乘积就是 \(t\pmod M\) 的因子，因而由本定理给出证书。
故该射线失败时，\(N\) 的全部素因子必落入某个包含恰好一半单位类的横截面；而 \(t\)
本身不能出现。这一必要条件是后续筛法的输入，并非失败的精确分类。

## 例子与边界

\(A=4\) 恰是 `three-p-plus-four-internal-type-I-certificate`。新的首个射线例子为

\[
A=8,\quad p=2689,\quad 3p+A=8075,\quad m=95,
\]

它给出

\[
(m,x,d)=(95,696,1856),\qquad(A,B,C)=(8,3,29).
\]

这些都是围绕同一目标 \(p\) 的直接因子证书，不是从较小分母实例提升解的递降。射线
可以把共同残余压得极薄，但并未为任何特定残余素数强制一个见证。事实上，对固定的
\(p\)，若这条射线有见证，则 (4) 和 \(m\ge3\) 强制

\[
A\le\frac{3p+9}{32}. \tag{5}
\]

所以只有有限多个幂二射线甚至可能命中同一个 \(p\)；不能从“使用全部射线”的筛界
错误推出逐点覆盖。
