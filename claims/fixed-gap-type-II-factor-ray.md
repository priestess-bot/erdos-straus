---
kind: claim
claim_id: fixed-gap-type-II-factor-ray
title: 固定缺口的 A=1 Type II 变量因子射线
statement: 令 q 为 q=3 mod4 的素数，p=1 mod24 为素数且 q<=p-2。令 x=(p+q)/4。若 x 有正因子 B=-1 modq，则 d=x/B 是缺口 q 的 Type II 除子证书；其正规形为 (A,B,C)=(1,B,x/B)。该射线失败时 x 的所有素因子落在模 q 单位群的某个半大小横截面中。
claim_status: established
topics:
- certificate
- type-II
- fixed-gap
- factorization
- ray
- sieve
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-certificate-equivalence
- paper: elsholtz_tao2013
  locator: "Section 2, Proposition 2.3"
  role: Type-II-parametrization
visibility: public
last_checked: '2026-07-23'
---

# 固定缺口的 \(A=1\) Type II 变量因子射线

## 定理

令 \(q\equiv3\pmod4\) 为素数，\(p\equiv1\pmod{24}\) 为素数，且

\[
q\le p-2.
\]

写

\[
x=\frac{p+q}{4}.
\]

若 \(B\mid x\) 且

\[
B\equiv-1\pmod q, \tag{1}
\]

则

\[
d=\frac{x}{B}
\]

是缺口 \(q\) 的 Type II 除子证书。其 Type II 正规形是

\[
(A,B,C)=\left(1,B,\frac{x}{B}\right). \tag{2}
\]

## 证明

由 (2) 有 \(x=ABC\)、\(d=A^2C=C\)，故 \(d\mid x^2\) 且 \(d\le x\)。
条件 (1) 给出

\[
q\mid A+B=1+B.
\]

`type-II-coprime-factor-normal-form` 的 Type II 条件遂全部满足。直接检验也有

\[
x+d=BC+C=C(B+1)\equiv0\pmod q.
\]

由于 \(q\le p-2\) 且 \(q\equiv3\pmod4\)，这是自然缺口范围中的证书。

## 半大小残数条件

由 \(q\nmid p\) 可知 \(q\nmid x\)，所以 \(x\) 的全部素因子属于

\[
G_q=(\mathbb Z/q\mathbb Z)^\times.
\]

在 \(q\equiv3\pmod4\) 时，\(-1\) 在 \(G_q\) 中不是平方。映射

\[
r\longmapsto-r^{-1}
\]

遂把 \(G_q\) 分成 \((q-1)/2\) 个无固定点二元组。若 \(x\) 同时有某一对中两种
残数的素因子，则它们的乘积是 \(-1\pmod q\) 的因子，满足 (1)。因此这条射线失败时，
\(x\) 的所有素因子只能落在某个每对选一类的横截面 \(T\) 中，其中

\[
|T|=\frac{q-1}{2}.
\]

这只是失败的必要条件；横截面内更多素因子的积仍可能满足 (1)。

## 例子与边界

\(p=5569,q=7\) 时 \(x=1394\)，可取 \(B=34\equiv-1\pmod7\)、\(d=41\)，
得到正规形 \((1,34,41)\) 的 Type II 证书。\(p=21529,q=11\) 时可取
\((B,d)=(1077,5)\)。

这里缺口 \(q\) 固定，但除子 \(B\) 随 \(p\) 的因子分解变化；故它不同于
`fixed-divisor-gap-template-obstruction` 所排除的固定除子模板。它是直接证书，不是递降。
