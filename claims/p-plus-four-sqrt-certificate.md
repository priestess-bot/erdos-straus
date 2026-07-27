---
kind: claim
claim_id: p-plus-four-sqrt-certificate
title: 来自 p+4 的平方根级 Type II 证书
statement: 对核心素数 p=1 mod 24，若 p+4 含有 q=3 mod 4 的素因子，则存在 Type II 证书，且可取缺口 m=q<=sqrt(p+4)、首分母 x=(p+q)/4 和除子 d=1。
claim_status: established
topics:
- certificate
- type-II
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2 and Corollary 2"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 来自 p+4 的平方根级 Type II 证书

## 精确表述与证明

令 \(p\equiv1\pmod{24}\)。若 \(q\equiv3\pmod4\) 整除 \(p+4\)，令

\[
m=q,\qquad x=\frac{p+q}{4},\qquad d=1.
\]

由于 \(q\mid p+4\)，

\[
q\mid p+q+4=4(x+1).
\]

\(q\) 是奇数，故 \(q\mid x+1\)。于是 \(d=1\mid x^2\)、\(d\le x\)，且 \(m\mid x+d\)，恰为 Type II 证书。恢复出的分母为

\[
x,\qquad \frac{p(x+1)}q,\qquad \frac{px(x+1)}q.
\]

又 \(p+4\equiv1\pmod4\)。若它有 \(3\pmod4\) 素因子，取最小者 \(q\)，同余类 \(3\pmod4\) 素因子的总指数为偶数，故 \(q^2\le p+4\)。所以 \(m\le\sqrt{p+4}\)。

## 剩余集

该家族未覆盖的核心素数满足 \(p+4\) 的所有素因子均为 \(1\pmod4\)。例如 \(p=193,313,1201\)；因此它与 `(p+1)/2` 和 \(m=3\) 家族互补，但不闭合全称命题。
