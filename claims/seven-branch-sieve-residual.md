---
kind: claim
claim_id: seven-branch-sieve-residual
title: 加入 source-6 后的七分支共同残余有 9/2 维筛界
statement: 令 R_7(X) 为核心素数中同时未被六条既有因子分支与 p+6 的 source-6 分支覆盖的数目，则 R_7(X)=O(X/(log X)^(9/2))。这仍不构成逐点的短证书或递降选择器。
claim_status: established
topics:
- sieve
- density
- certificate
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-formulation
visibility: public
last_checked: '2026-07-23'
---

# 加入 source-6 后的七分支共同残余有 \(9/2\) 维筛界

令 \(R_7(X)\) 是 `six-branch-sieve-residual` 的共同残余中还没有
`p-plus-six-external-source-certificate` 证书的核心素数数目。则

\[
R_7(X)\ll\frac{X}{(\log X)^{9/2}}. \tag{1}
\]

## 证明

由 `p-plus-six-external-source-certificate`，source-6 分支失败是两个事件的并：

\[
E_j:\quad\text{所有 }p+6\text{ 的素因子均落在 }H_j\quad(j=1,2).
\]

对每个 \(j\)，在 `six-branch-sieve-residual` 的线性筛系统上附加筛除：当
\(\ell\pmod{24}\notin H_j\) 时，筛去

\[
24t+7\equiv0\pmod\ell.
\]

在八个可逆模 \(24\) 素数类中，恰有四类被附加筛除。因此，除有限个线性式根重合的
素数外，筛维从 \(4\) 增加 \(1/2\)。与六分支证明相同的 Selberg 上界筛给出

\[
\#\{p\le X:p\in R_6,\ E_j\}
\ll\frac{X}{(\log X)^{4+1/2}}.
\]

对 \(j=1,2\) 求和即得 (1)。

## 边界

该结论只说明七条明确分支的共同补集更稀薄。比如 \(p=5569\) 仍在这个补集中，因为
\(5569+6=5^2\cdot223\) 的素因子残数都落在 \(H_2\)。它有别的 Type I 证书，故再次
说明筛残余不等于无解或无证书残余；全称引理仍需新的统一强制机制或真正的可闭合递降。
