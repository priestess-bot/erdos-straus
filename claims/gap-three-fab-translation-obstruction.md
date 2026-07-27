---
kind: claim
claim_id: gap-three-fab-translation-obstruction
title: 缺口 m=3 的 fab 平移半覆盖障碍
statement: 令 p=24t+1、n=(p+3)/4。若 Bello--Hernandez 等的 fab 平移 n -> n+4abk 恰到达 p，则 t 必为偶数且 abk=9t/2；因此 t 为奇数的核心素数不可能由该自然 m=3 源实例的 fab 平移到达。
claim_status: established
topics:
- descent
- obstruction
- gap-three
- fab
- proof-program
sources:
- paper: bello2026
  locator: "Proposition 20"
  role: translation-invariance
visibility: public
last_checked: '2026-07-23'
---

# 缺口 \(m=3\) 的 fab 平移半覆盖障碍

## 定理

令 \(p=24t+1\) 为核心素数，并令

\[
n=\frac{p+3}{4}=6t+1.
\]

若 Bello--Hernandez、Benito、Fernandez 的 Proposition 20 所给平移

\[
n_1=n+4abk
\]

从该 \(n\) 恰到达 \(p\)，则

\[
t\equiv0\pmod2,\qquad abk=\frac{9t}{2}. \tag{1}
\]

所以所有 \(t\) 为奇数的核心素数均不可能通过这一自然 \(m=3\) 源实例的
`fab` 平移获得证书。

## 证明

由 \(p=4n-3\)，有

\[
p-n=3n-3=18t.
\]

若 \(p=n+4abk\)，则 \(4abk=18t\)。左侧被 4 整除，故 \(t\) 必为偶数；
除以 4 即得 (1)。反过来，(1) 只是达到所需数值差的必要条件，并不声称给定
\(a,b,k\) 对 \(n\) 可采纳。

## 对递降计划的含义

Proposition 20 的前提是源实例已有一个可采纳的 `fab` 证书；结论是同一证书在
目标数仍可采纳。它不读取任意 \(\operatorname{Sol}(n)\) 元素，也不提供
\(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 的映射。因此即使 \(t\) 为偶数，
该平移仍只是潜在的**直接证书转移**而非所需递降；\(t\) 为奇数时则连这一证书
转移也因同余而不可能。
