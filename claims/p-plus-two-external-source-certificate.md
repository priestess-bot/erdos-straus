---
kind: claim
claim_id: p-plus-two-external-source-certificate
title: 来自 p+2 的 source-2 Type I 证书
statement: 对核心素数 p=1 mod24，若 p+2 有一个 7 mod8 的正因子 m，则 m 给出 Type I 证书 x=(p+m)/4、d=2x。该分支失败当且仅当 p+2 的所有素因子均为 1 或 3 mod8。
claim_status: established
topics:
- certificate
- type-I
- external-source
- factorization
- proof-program
sources:
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-formulation
- paper: bradford2024
  locator: "Proposition 1"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 来自 \(p+2\) 的 source-2 Type I 证书

## 定理

令 \(p\equiv1\pmod{24}\) 为素数。若 \(m\mid p+2\) 且

\[
m\equiv7\pmod8,
\]

则

\[
x=\frac{p+m}{4},\qquad d=2x
\]

构成缺口 \(m\) 的 Type I 除子证书。特别地，\(3\le m\le p-2\)。

这恰是 `external-source-type-I-certificate` 的外部源 \(i=2\) 切片。

## 证明

由 \(p\equiv1\pmod8\) 与 \(m\equiv7\pmod8\)，有 \(8\mid p+m\)，故
\(x\) 是偶数，因而

\[
d=2x\mid x^2.
\]

又因 \(m\mid p+2\)，

\[
px+d=x(p+2)\equiv0\pmod m.
\]

这就是 Type I 条件。

最后，\(m\ne p+2\)，因为 \(p+2\equiv3\pmod8\)。令
\(h=(p+2)/m\)；由 \(h\equiv3\cdot7^{-1}\equiv5\pmod8\)，有 \(h\ge5\)，故

\[
7\le m\le\frac{p+2}{5}\le p-2.
\]

所以该构造处于自然缺口范围。

## 精确剩余条件

\(p+2\equiv3\pmod8\)。若其所有素因子都为 \(1\) 或 \(3\pmod8\)，每个因子
的乘积只能为 \(1\) 或 \(3\pmod8\)，因而不存在 \(7\pmod8\) 因子。

反之，若某个素因子为 \(7\pmod8\)，它本身可取作 \(m\)。若有
\(5\pmod8\) 素因子而没有 \(7\pmod8\) 素因子，因全部素因子的乘积为
\(3\pmod8\)，必同时有 \(3\pmod8\) 素因子；两者之积为 \(7\pmod8\)。故分支失败
当且仅当所有素因子均为 \(1\) 或 \(3\pmod8\)。

例如 \(2521+2=3\cdot29^2\)，取 \(m=3\cdot29=87\)，得到

\[
(m,x,d)=(87,652,1304).
\]

这给出 Type I 证书，但仍是围绕目标 \(p\) 的直接构造，不是从较小实例解提升的递降。
