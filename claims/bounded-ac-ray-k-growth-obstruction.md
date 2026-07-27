---
kind: claim
claim_id: bounded-ac-ray-k-growth-obstruction
title: 有界 A,C 的 Type II 射线在无穷核心素数上强制近对数 K
statement: 设 S 是任意非空有限正整数对 (A,C) 集。存在常数 c_S>0 和无穷多个素数 p=1 mod24，使得任意 A,C 属于 S、K>=1 且 4ACK-1 整除 Kp+A 的 Type II 原始射线见证都满足 K>c_S log(p)/log(log(p))。特别地，固定 A,C 盒上的可变 K 选择器不可能在全体核心素数上保持有界 K。
claim_status: established
topics:
- type-II
- factorization
- obstruction
- primes-in-progressions
- proof-program
sources:
- paper: linnik1944
  locator: least-prime theorem in arithmetic progressions
  role: quantitative-prime-selection
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 有界 \(A,C\) 的 Type II 射线在无穷核心素数上强制近对数 \(K\)

## 定理

令 \(\mathcal S\) 为任意非空有限集合

\[
\mathcal S\subset\mathbb N^2.
\]

则存在只依赖于 \(\mathcal S\) 的常数 \(c_{\mathcal S}>0\)，以及无穷多个
素数 \(p\equiv1\pmod{24}\)，使得对于任意

\[
(A,C)\in\mathcal S,\qquad K\ge1,
\]

若

\[
4ACK-1\mid Kp+A, \tag{1}
\]

则

\[
K>c_{\mathcal S}\frac{\log p}{\log\log p}. \tag{2}
\]

因而，任何固定有限 \(A,C\) 盒上的 Type II 射线方案，即使允许 \(K\) 随
\(p\) 变化，也不能在所有核心素数上把 \(K\) 限制为常数，或限制在
\(o(\log p/\log\log p)\) 的量级。

## 证明

固定正整数 \(L\)。对每个 \((A,C)\in\mathcal S\) 和
\(1\le K\le L\)，令

\[
q_{A,C,K}=4ACK-1,
\qquad
M_L=\operatorname{lcm}\left(24,\{q_{A,C,K}\}\right). \tag{3}
\]

若 \(p\equiv1\pmod {M_L}\)，则特别有 \(p\equiv1\pmod {q_{A,C,K}}\)，从而

\[
Kp+A\equiv K+A\pmod {q_{A,C,K}}. \tag{4}
\]

而

\[
q_{A,C,K}-(K+A)
  =K(4AC-1)-A-1
  \ge3A-2>0. \tag{5}
\]

所以 \(0<K+A<q_{A,C,K}\)，式 (4) 表明 (1) 对所有
\((A,C)\in\mathcal S\)、\(K\le L\) 同时失败。

现在对模数 \(M_L\) 和剩余类 \(1\) 应用 Linnik 定理。存在绝对常数
\(C_0,L_0>0\)，可取一个素数

\[
p_L\equiv1\pmod {M_L},
\qquad
p_L\le C_0M_L^{L_0}. \tag{6}
\]

它是核心素数，且由上一段可知：在 \(\mathcal S\) 内的每条满足 (1) 的射线
都必须有 \(K>L\)。

设 \(R=\max_{(A,C)\in\mathcal S}AC\)、\(s=|\mathcal S|\)。由 (3) 的粗略乘积界，
对某个仅依赖于 \(\mathcal S\) 的常数 \(D\)，有

\[
\log M_L\le D L\log(2L). \tag{7}
\]

联立 (6) 得

\[
\log p_L\le D' L\log(2L). \tag{8}
\]

另一方面，任选 \((A_0,C_0)\in\mathcal S\)，式 (3) 含有
\(4A_0C_0L-1\)，故 \(p_L>M_L\ge4A_0C_0L-1\)。这说明 \(p_L\) 随
\(L\) 无界，也允许从 (8) 反解：若 \(L<\log p_L\)，则
\(\log(2L)\ll\log\log p_L\)；若 \(L\ge\log p_L\)，所需下界更是平凡。
于是对充分大的 \(L\)，

\[
L\ge c_{\mathcal S}\frac{\log p_L}{\log\log p_L}. \tag{9}
\]

将 (9) 与 \(K>L\) 合并，并取无穷子列，得到 (2)。

## 对选择器的含义

这一定理严格增强了 type-II-finite-template-obstruction：后者仅说明固定的
\((A,C,K)\) 三元组盒必须失效；这里允许每个 \(p\) 自适应选择任意 \(K\)，仍证明
在无穷目标上 \(K\) 至少需要近对数增长。

它不反驳 type-II-ac-ray-saturation-conjecture。后者只要求 \(A,C\) 有界，
允许 \(K\) 很大；本定理恰说明任何证明该猜想的选择器必须处理这种不可避免的
增长，而不能退化成有限模板或恒定 \(K\) 搜索。因而它缩小了可行的全称证明形态，
但尚未构造所需的因子，也没有产生递降边。
