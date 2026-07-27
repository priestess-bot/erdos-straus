---
kind: claim
claim_id: type-II-support-defect-orbit-constraint
title: Type II 支撑内失败的缺失集补因子轨道约束
statement: 固定 Type II AC 射线，令 M=4AC、N=p+4A^2C，K 为 N 的素因子残数生成子群，Pi 为全部除子残数。若 -1 属于 K 但不属于 Pi，则支撑内缺失集 D=K minus Pi 在对合 x maps to p/x 下不变。若 p 不等于 1 mod M 且 |D|=2，则 D 恰为 {-1,-p}；若 p 不等于 1 mod M 且 |D| 为奇数，则 D 含有 rho 满足 rho squared equals p mod M，故 p 是模 M 的二次剩余。
claim_status: established
topics:
- type-II
- divisor-residues
- subgroup-structure
- critical-sequence
- involution
- quadratic-residue
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework; Theorem C"
  role: structural-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 支撑内失败的缺失集补因子轨道约束

## 定理

固定正整数 \(A,C\)，写

\[
M=4AC,\qquad N=p+4A^2C=p+AM,
\]

并假设 \(\gcd(p,M)=1\)。把 \(N\) 的素因子按重数取模 \(M\)，得到
\(U(M)\) 中的序列 \(S\)。记

\[
\Pi=\Pi(S),\qquad K=\langle S\rangle,\qquad D=K\setminus\Pi,\qquad
P=\prod_{s\in S}s\equiv N\equiv p\pmod M. \tag{1}
\]

假设这是一个支撑内失败，即

\[
-1\in D. \tag{2}
\]

则 \(D\) 在对合

\[
\iota_P(x)=Px^{-1} \tag{3}
\]

下不变。进一步：

1. 若 \(P\ne1\) 且 \(\lvert D\rvert=2\)，则

\[
D=\{-1,-P\}=\{-1,-p\}\pmod M. \tag{4}
\]

2. 若 \(P\ne1\) 且 \(\lvert D\rvert\) 是奇数，则存在
\(\rho\in D\)，使

\[
\rho^2\equiv P\equiv p\pmod M. \tag{5}
\]

特别地，后一类失败强制 \(p\) 是模 \(4AC\) 的二次剩余。

## 证明

对任意 \(x\in\Pi\)，选择产生 \(x\) 的子序列并取其补子序列，所得乘积为
\(Px^{-1}\)。故 (3) 在 \(\Pi\) 上是双射。因 \(P\in K\)，它同时是 \(K\) 上
的双射，所以保持补集 \(D\)。

由 (2)，

\[
\iota_P(-1)=-P. \tag{6}
\]

当 \(P\ne1\) 时，这两个元素不同，故 \(\{-1,-P\}\) 是 \(D\) 中一个二元轨道。
若 \(\lvert D\rvert=2\)，立即得到 (4)。

若 \(\lvert D\rvert\) 为奇数，移除该二元轨道后仍留下奇数个元素。一个有限集合在
对合下分解为长度一或二的轨道；故剩余部分至少有一个不动点 \(\rho\)。由
\(\iota_P(\rho)=\rho\)，有 \(\rho^2=P\)，即 (5)。

## 与一孔同余陷阱的关系

当 \(\lvert D\rvert=1\) 时，(6) 迫使 \(P=1\)，这正是
`type-II-support-critical-congruence-trap` 的 \(p\equiv1\pmod M\) 结论。
本条处理其后的两种缺陷大小，但条件 \(P\ne1\) 必不可少：若 \(P=1\)，则 \(-1\)
本身是不动点，二孔或奇孔不再给出 (4) 或新的平方根限制。

同样必须要求 (2)。若 \(-1\notin K\)，则射线虽失败但 \(D\) 没有目标元素；
(6) 无法启动。这是与支撑内多孔临界不同的主型，不能由本定理或一孔结论覆盖。

## 精确审计

在 \(p\le10^5\)、\(A,C\le5\) 的精确审计中，22,944 条失败射线分成：

| 类别 | 数量 |
|---|---:|
| \(-1\notin K\) 的支撑外失败 | 20,089 |
| \(-1\in K\) 的支撑内失败 | 2,855 |
| 其中 \(P\ne1\) 的两孔失败 | 77 |
| 其中 \(P\ne1\) 的奇孔失败 | 369 |

所有支撑内缺失集都通过 (3) 的不变性检查；77 条两孔实例均满足 (4)，369 条奇孔
实例均有 (5) 的缺失平方根。有限审计验证实现，定理本身不依赖这些计数。

## 复现

运行 python3 reproductions/divisor_residue_structure.py --audit-limit 100000 --ac-bound 5。
