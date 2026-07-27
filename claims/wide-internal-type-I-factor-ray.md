---
kind: claim
claim_id: wide-internal-type-I-factor-ray
title: 宽内部 Type I 因子射线
statement: 令 A 是 4 的倍数、B>=3 为奇数、gcd(A,B)=1、A>2B，且 p=1 mod24 为素数、p>A+2B+2。若 m|Bp+A 且 m=-p mod4AB，则 m 是自然范围内的 Type I 除子证书缺口，正规形为 (A,B,(p+m)/(4AB))；若不存在这种因子，则 Bp+A 的素因子残数落在模 4AB 单位群的一个半大小横截面中。
claim_status: established
topics:
- certificate
- type-I
- internal-parameter
- factorization
- ray
- sieve
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: Type-I-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-24'
---

# 宽内部 Type I 因子射线

## 定理

设

\[
4\mid A,\qquad B\ge3\text{ 为奇数},\qquad (A,B)=1,\qquad A>2B,
\]

并令 $p\equiv1\pmod{24}$ 为满足 $p>A+2B+2$ 的素数。若正因子

\[
m\mid Bp+A,\qquad m\equiv-p\pmod{4AB}, \tag{1}
\]

则

\[
x=\frac{p+m}{4},\qquad
d=A^2\frac{p+m}{4AB} \tag{2}
\]

是自然范围 $3\le m\le p-2$ 内的 Type I 除子证书。其互素正规形为

\[
(A,B,C)=\left(A,B,\frac{p+m}{4AB}\right). \tag{3}
\]

此外，若不存在满足 (1) 的因子，则 $N=Bp+A$ 的全部素因子残数落在

\[
(\mathbb Z/(4AB)\mathbb Z)^\times
\]

的某个半大小横截面中。

## 证明

由 (1)，$C=(p+m)/(4AB)$ 为正整数。因此

\[
x=ABC,\qquad d=A^2C,
\]

并且 $m\mid Bp+A$。`type-I-coprime-factor-normal-form` 立刻给出 Type I
证书；这里只剩自然缺口范围需要验证。

记

\[
h=\frac{Bp+A}{m},\qquad M=4AB.
\]

条件 $p>A+2B+2$ 保证 $(p,M)=1$。令 $u$ 是 $p^{-1}\pmod{4B}$ 的
最小正代表元。因为 $1\le u\le4B-1$，从 $m\equiv-p\pmod M$ 得

\[
h\equiv-B-Au\equiv A(4B-u)-B\pmod M. \tag{4}
\]

右边本身位于 $1,\ldots,M-1$，且

\[
A(4B-u)-B\ge A-B>B.
\]

故 $h\ge A-B>B$，特别有

\[
m\le\frac{Bp+A}{A-B}\le p-2. \tag{5}
\]

最后一个不等式等价于

\[
(A-2B)p\ge3A-2B,
\]

而在 $p>A+2B+2$ 时左边严格大于

\[
(A-2B)(A+2B+2)=A^2-4B^2+2A-4B.
\]

它再减去 $3A-2B$ 为

\[
A^2-4B^2-A-2B>0,
\]

其中最后一步由 $A>2B$ 及 $4\mid A,\ B$ 为奇数给出的最小可能值
$A\ge2B+2$ 可直接验证。又 $m\equiv-p\equiv3\pmod4$，所以
$m\ge3$，定理的证书部分成立。

现在考虑失败条件。由 $p>A$、$(A,B)=1$，有

\[
(N,4AB)=1.
\]

所以 $N$ 的每个素因子都属于单位群。目标残数

\[
t=-p\pmod M
\]

在模 $8$ 下为 $7$，而任意奇单位平方模 $8$ 都是 $1$，故 $t$ 在该
单位群中没有平方根。反演平移 $r\mapsto tr^{-1}$ 因此把单位群分成无固定点的
二元组。若 $N$ 的素因子来自同一二元组的两类，它们的乘积就是一个满足 (1) 的
因子，矛盾。每个二元组任选尚可出现的一类，即得包含全部素因子残数的半大小横截面。

## 例子与关系

取 $(A,B)=(12,5)$、$p=1033$。此时

\[
5p+12=5177=167\cdot31,\qquad 167\equiv-1033\pmod{240}.
\]

公式给出

\[
(m,x,d)=(167,300,720),\qquad(A,B,C)=(12,5,5).
\]

这说明该射线覆盖的是真正的 $B>3$ 内部区域。`three-p-plus-power-two-internal-type-I-ray`
是 $B=3$ 的特例；对于 $A\ge8$，这里的 $A>2B$ 自动给出其自然范围界。

## 边界

这是一条围绕同一 $p$ 的直接因子证书分支，不是从较小分母实例提升解的递降边。每个
固定 $(A,B)$ 的失败只给出一个半维筛条件；即便取很多参数对，也不能把密度界误作
逐点全覆盖或本题所需的全称递降选择器。
