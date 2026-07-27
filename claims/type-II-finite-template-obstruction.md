---
kind: claim
claim_id: type-II-finite-template-obstruction
title: 有限 Type II 因子模板不能覆盖全部核心素数
statement: 对任意有限个正整数模板 (A,C,K)，由 4ACK-1 | Kp+A 生成的 Type II 证书不能覆盖所有素数 p=1 mod24；实际上存在一个 p=1 mod24 的 Dirichlet 等差数列，其中每个模板的整除条件都失败。
claim_status: established
topics:
- type-II
- factorization
- congruences
- obstruction
- proof-program
sources:
- paper: bello2026
  locator: "Theorem 8"
  role: parallel-finite-parameter-rigidity
visibility: public
last_checked: '2026-07-23'
---

# 有限 Type II 因子模板不能覆盖全部核心素数

## 定理

取任意有限集合

\[
\mathcal S\subset\mathbb N^3.
\]

对每个 \((A,C,K)\in\mathcal S\)，考虑
`type-II-coprime-factor-normal-form` 的因子生成条件

\[
4ACK-1\mid Kp+A. \tag{1}
\]

则存在无穷多个素数 \(p\equiv1\pmod{24}\)，对所有
\((A,C,K)\in\mathcal S\)，(1) 都不成立。因此，任何固定有限参数模板集都不能
凭此 Type II 生成器覆盖全部核心素数。

## 证明

记

\[
q_{A,C,K}=4ACK-1,\qquad
M=\operatorname{lcm}\bigl(24,\{q_{A,C,K}:(A,C,K)\in\mathcal S\}\bigr).
\]

考虑等差数列 \(p\equiv1\pmod M\)。它当然包含在
\(p\equiv1\pmod{24}\) 中。对任意固定模板，有

\[
Kp+A\equiv K+A\pmod {q_{A,C,K}}.
\]

而

\[
q_{A,C,K}-(K+A)
=4ACK-1-K-A
\ge4AK-1-K-A
=(4A-1)K-A-1>0.
\]

故 \(0<K+A<q_{A,C,K}\)，从而

\[
q_{A,C,K}\nmid Kp+A.
\]

这对 \(\mathcal S\) 中每个模板同时成立。又
\(\gcd(1,M)=1\)，Dirichlet 的等差数列素数定理给出无穷多个素数
\(p\equiv1\pmod M\)。它们逐一避开全部模板，定理得证。

## 含义与边界

这一定理只否定**固定有限**的 \((A,C,K)\) 模板覆盖；它不否定参数随 \(p\)
增长的短证书界，也不否定 Type I 证书或真正的解提升递降。它解释了有限审计中的
窗口现象为何不能形成全称证明：盒 \(A,C,K\le20\) 在 \(p\le10^7\) 时覆盖全部
直接族残余，但扩至 \(p\le10^8\) 已遗漏 7 个；盒 29 则仅在后一有限范围内恢复覆盖。

该结论与 Bello--Hernandez、Benito、Fernandez 对有限 `fab` 参数覆盖的刚性障碍
方向一致，但这里的证明直接作用于当前 Type II 因子生成器，且不依赖其参数体系。
