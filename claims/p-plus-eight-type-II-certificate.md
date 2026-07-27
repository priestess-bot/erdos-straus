---
kind: claim
claim_id: p-plus-eight-type-II-certificate
title: 来自 p+8 的 7 模 8 因子 Type II 证书
statement: 对核心素数 p=1 mod24，若 h|p+8 且 h=7 mod8，则令 k=(h+1)/8；参数 (A,C,K)=(1,2,k) 给出直接 Type II 证书。换言之，p+8 的任意7模8因子都触发规范位移2射线。
claim_status: established
topics:
- certificate
- type-II
- canonical-ray
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 2 and 3
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# 来自 \(p+8\) 的 \(7\bmod8\) 因子 Type II 证书

令 \(p\equiv1\pmod{24}\)，且

\[
h\mid p+8,\qquad h\equiv7\pmod8,\qquad k=\frac{h+1}{8}.
\]

则 \(h=8k-1\)，并且

\[
8(kp+1)=(h+1)p+8\equiv p+8\equiv0\pmod h.
\]

故 \(h\mid kp+1\)。取 Type II 因子射线参数

\[
A=1,\qquad C=2,\qquad K=k,\qquad B=\frac{kp+1}{h}.
\]

由 \(hB=kp+1\) 模 \(k\) 化简得 \(B\equiv-1\pmod k\)，所以

\[
m=\frac{1+B}{k},\qquad x=2B,\qquad d=2
\]

为整数。又

\[
B-1=\frac{k(p-8)+2}{h}>0
\]

（核心素数 \(p\ge73\)），故 \(A\le B\)。由非互素 Type II 因子射线的证书恒等式，
\((m,x,d)\) 是合法 Type II 证书。

该条件覆盖一千万双严格递降边界中的

\[
214729,\quad3942409,\quad6294649,
\]

它们可分别取 \(h=31,71,1671\)。这只是一个显式充分分支；并不声称每个
\(p+8\) 都有这样的因子。

## 重建

~~~bash
python3 -m unittest tests/test_short_certificate.py -q
~~~
