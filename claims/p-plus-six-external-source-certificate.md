---
kind: claim
claim_id: p-plus-six-external-source-certificate
title: 来自 p+6 的 source-6 Type I 证书及精确残余分类
statement: 对核心素数 p=1 mod24，若 p+6 有一个 23 mod24 的因子 m，则 x=(p+m)/4、d=6x 是 Type I 证书。该分支失败当且仅当 p+6 的全部素因子模24都落在 H_1={1,7,13,19} 或都落在 H_2={1,5,7,11}。
claim_status: established
topics:
- certificate
- type-I
- external-source
- factorization
- finite-abelian-group
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

# 来自 \(p+6\) 的 source-6 Type I 证书及精确残余分类

## 定理

令 \(p\equiv1\pmod{24}\) 为素数。若 \(m\mid p+6\) 且

\[
m\equiv23\pmod{24},
\]

则

\[
x=\frac{p+m}{4},\qquad d=6x
\]

构成缺口 \(m\) 的 Type I 证书，且 \(3\le m\le p-2\)。

## 证明

由 \(p+m\equiv1+23\equiv0\pmod{24}\)，\(x\) 是 \(6\) 的倍数，故

\[
d=6x\mid x^2.
\]

又 \(m\mid p+6\)，所以

\[
px+d=x(p+6)\equiv0\pmod m.
\]

这正是 Type I 条件。并且 \(m\ne p+6\)，因为 \(p+6\equiv7\pmod{24}\)。令
\(h=(p+6)/m\)，则

\[
h\equiv7\cdot23^{-1}\equiv17\pmod{24},
\]

故 \(h\ge17\)，进而 \(23\le m\le(p+6)/17\le p-2\)。

## 精确失败分类

令

\[
G=(\mathbb Z/24\mathbb Z)^\times\cong(\mathbb F_2)^3,
\quad
H_1=\{1,7,13,19\},\quad H_2=\{1,5,7,11\}.
\]

这两个集合是恰好包含 \(7\) 而不包含 \(23\) 的两个指数 \(2\) 子群。由于
\(p+6\equiv7\pmod{24}\)，其素因子残数在 \(G\) 中生成的子空间含有 \(7\)。
从各个素因子中选取一个子集所得到的因子残数，恰为这个子空间的元素。因此存在
\(23\pmod{24}\) 因子，当且仅当该子空间含有 \(23\)。

若不含 \(23\)，该子空间包含在某个不含 \(23\) 的超平面中；又它含 \(7\)，故只能包含在
\(H_1\) 或 \(H_2\) 中。反向显然。这证明分支失败当且仅当所有素因子都落在 \(H_1\)，或
所有素因子都落在 \(H_2\)。

例如 \(937+6=23\cdot41\)，可取 \(m=23\)，得到

\[
(m,x,d)=(23,240,1440).
\]

这仍是目标 \(p\) 周围的直接证书构造，而不是严格递降提升。
