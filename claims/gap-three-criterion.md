---
kind: claim
claim_id: gap-three-criterion
title: 缺口 m=3 的精确素因子判据
statement: 对每个核心素数 p=1 mod 24，m=3 的 Type I 或 Type II 除子证书存在，当且仅当 x=(p+3)/4 含有一个 q=2 mod 3 的素因子；此时取 d=q 即给出 Type II 证书。
claim_status: established
topics:
- certificate
- congruences
- type-II
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2 and Corollary 2"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 缺口 m=3 的精确素因子判据

## 精确表述

令 \(p=24t+1\) 是素数，\(x=(p+3)/4=6t+1\)。则存在缺口 \(m=3\) 的 Type I 或 Type II 证书，当且仅当 \(x\) 有一个素因子 \(q\equiv2\pmod3\)。

## 证明

此时 \(p\equiv x\equiv1\pmod3\)。按首分母缺口证书的判据，Type I 要求

\[
d\mid x^2,\qquad d\equiv-px\equiv2\pmod3,
\]

而 Type II 要求

\[
d\mid x^2,\quad d\le x,\qquad d\equiv-x\equiv2\pmod3.
\]

若 \(q\mid x\) 且 \(q\equiv2\pmod3\)，取 \(d=q\) 即满足 Type II 的所有条件。反之，若某个 \(d\mid x^2\) 满足 \(d\equiv2\pmod3\)，其素因子分解中必有一个 \(2\pmod3\) 素数；由于 \(d\mid x^2\)，这个素数也整除 \(x\)。

## 边界条件

该判据将 \(m=3\) 未覆盖的核心素数限制为 \((p+3)/4\) 的所有素因子均为 \(1\pmod3\) 的情形。它没有证明这样的素数不存在，也没有给出到较小实例的解提升；因此只是证明计划的一个显式子族，而不是递降步骤。
