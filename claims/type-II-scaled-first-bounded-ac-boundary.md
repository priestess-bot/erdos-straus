---
kind: claim
claim_id: type-II-scaled-first-bounded-ac-boundary
title: 有界 AC Type II 射线不足以统一选择缩放首分母递降
statement: 在 p<=3*10^6 的 41 个普通双尾递降一阶残余中，枚举全部 A,C<=14、K 任意的原始 Type II 射线，并对每张证书枚举 p+m 的所有共享因子 D=1 mod m，缩放首分母递降只命中 30 个，遗漏 11 个。故在这个有限压力集上，“有小 AC 的直接 Type II 证书”不能推出“有小 AC 的共享因子递降证书”。该结论只限制该参数盒，不排除更大 AC 或其它证书。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- factor-selection
- bounded-parameters
- computation
- boundary
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 有界 \(A,C\) 射线不足以统一选择缩放首分母递降

## 审计范围

输入是 \(p\le3\cdot10^6\) 时普通 \(k=1\) 双尾递降遗漏的 41 个核心素数。
对每个 \(p\)，完整枚举

\[
1\le A,C\le14,\qquad
h=4ACK-1\mid p+4A^2C,
\]

从每个允许因子恢复不受界的 \(K\)、合法 Type II 证书及其缺口 \(m\)。随后枚举

\[
D\mid p+m,\qquad D\equiv1\pmod m
\]

的全部因子，并以 \(k=(D-1)/m\) 进行缩放首分母递降的精确验证。

## 结果

    python3 reproductions/type_ii_scaled_first_ac_boundary.py \
      --ac-bound 14 \
      --output reproductions/type-ii-scaled-first-ac14-3m-results.json

得到

\[
\#\{\text{输入}\}=41,\qquad
\#\{\text{命中}\}=30,\qquad
\#\{\text{遗漏}\}=11.
\]

遗漏为

\[
67369,225289,532249,852889,878089,1093129,1854889,
1936489,2020489,2254729,2707609.
\]

例如 \(p=85369\) 可在半径 \(14\) 内取

\[
(A,C,K,m,D,k)=(5,14,10,31,280,9);
\]

但上述 11 点在整个相同 \(A,C\) 盒中都没有这种证书。

## 含义

已有的 type-II-ac-ray-audit 表明小 \(A,C\)、可变 \(K\) 的直接 Type II
射线在很大有限范围具有极高覆盖；本审计表明再加上共享因子
\(D\equiv1\pmod m\) 后，逻辑上是更强的选择问题。直接证书审计因而不能替代递降
选择定理。

这不是对有界 \(A,C\) 方案的无穷否定，也不是对猜想的反例。它只确定下一步不应把
“先找任意小 AC 证书”误当成已解决共享因子选择。
