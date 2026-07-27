---
kind: claim
claim_id: odd-distance-even-source-same-tail-deflation-divisibility
title: 偶源尾同证书缩减的 r 除子判据
statement: 设 p 为核心素数，r=7 mod8，且一个 r 偶源平方尾诱导 Type I 正规形 x=ABC、e=B^2C、m=(4e+1)/r。该尾可保持前两项严格去缩放，当且仅当 r+1|p-1。等价地，它恰是完整平方因子外部源中 q=r、k=(r+1)/4 的分支；并非独立递降机制。
claim_status: established
topics:
- type-I
- even-source
- external-source
- descent
- normal-form
- divisibility
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: even-source-and-external-source-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# 偶源尾同证书缩减的 \(r\) 除子判据

设 \(p\equiv1\pmod {24}\)、\(r\equiv7\pmod8\)，并有一个 \(r\)-偶源平方尾。将其
Type I 证书写为

\[
x=ABC,\qquad e=B^2C,\qquad m=\frac{4e+1}{r}. \tag{1}
\]

则把该证书的 \(p\)-倍尾去缩放为严格更小源的充要条件是

\[
r+1\mid p-1. \tag{2}
\]

## 证明

通用正规尾缩减判据要求

\[
R+1\mid4BC(A+B),\qquad R=\frac{4B^2C+1}{m}. \tag{3}
\]

由 (1)，\(R=r\)。另一方面，偶源尾的原半分母为

\[
M=BC(rA-B),\qquad 4M=rp+1. \tag{4}
\]

模 \(r+1\) 使用 \(r\equiv-1\)，有

\[
4BC(A+B)\equiv-4M\equiv p-1\pmod {r+1}. \tag{5}
\]

故 (3) 与 (2) 等价。

再令

\[
k=\frac{r+1}{4},\qquad q=4k-1=r. \tag{6}
\]

由于 \(r\equiv7\pmod8\)，\(k\) 为正整数；(2) 又等价于
\(k\mid(p-1)/4\)。所以同尾缩减正好是完整平方因子外部源的允许模数 \(q=r\) 的
分支，而不是第二种独立机制。

## 研究含义

这个简化消除了一个表面上依赖 \(A,B,C\) 的选择问题：对固定 \((p,r)\)，该 \(r\) 的
所有有效尾要么全部可同证书缩减，要么全部不可。后续不应再试图通过在同一个 \(r\) 下更换
溢出因子来修复缩减整除性；必须改选满足 \(q+1\mid p-1\) 的外部模数 \(q\)，或改变源状态。

在十亿 H19 首 \(r\) 的 91 个高溢出状态中，恰有 70 个满足 \(r+1\mid p-1\)。余下 21 个
均由 \(q\ne r\) 的完整平方因子外部源闭合，见
[H19 高溢出偶源尾的同参数外部源分流](type-II-h19-overflow-same-tail-deflation-profile.md)。
