---
kind: claim
claim_id: p-plus-one-sqrt-certificate
title: 来自 (p+1)/2 的平方根级 Type I 证书
statement: 对核心素数 p=1 mod 24，若 N=(p+1)/2 含有 q=3 mod 4 的素因子，则存在 Type I 证书，且可取缺口 m=q<=sqrt(N)<sqrt(p)、首分母 x=(p+q)/4 和除子 d=x。
claim_status: established
topics:
- certificate
- type-I
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1 and Corollary 1"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 来自 (p+1)/2 的平方根级 Type I 证书

## 精确表述与证明

令 \(p\equiv1\pmod{24}\)，\(N=(p+1)/2\)。此时 \(N\equiv1\pmod4\)。若 \(q\equiv3\pmod4\) 是 \(N\) 的任一素因子，令

\[
m=q,\qquad x=\frac{p+q}{4},\qquad d=x.
\]

因为 \(q\mid p+1\)，有

\[
m\mid px+d=x(p+1).
\]

又 \(d=x\mid x^2\)，所以这是 Bradford 的 Type I 证书。由 \(N\equiv1\pmod4\)，所有 \(3\pmod4\) 素因子的总指数为偶数；取最小这样的 \(q\)，必有 \(q^2\le N\)。因此可选择

\[
m=q\le\sqrt{N}<\sqrt p.
\]

恢复出的分母可写为

\[
x,\qquad \frac{x(p+1)}q,\qquad \frac{px(p+1)}q.
\]

## 剩余集

该家族唯一未覆盖的核心素数满足 \((p+1)/2\) 的每个素因子均为 \(1\pmod4\)。这不是空集：\(p=73,193,1129\) 都在其中。因此该定理是非平凡的平方根界子族，不能单独完成猜想。
