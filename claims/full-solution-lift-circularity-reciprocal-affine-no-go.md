---
kind: claim
claim_id: full-solution-lift-circularity-reciprocal-affine-no-go
title: 未标记全域提升的循环性与逐坐标倒数仿射整值障碍
statement: >-
  若 Sol(n) 非空，则任意集合映射 Sol(n)->Sol(p) 的存在性与 Sol(p) 非空等价；
  因而未附构造限制的全域提升只是猜想本身的改写，目标解诱导的常值映射必须登记为
  terminal 而非递降。对非平凡的质量保持逐坐标倒数仿射候选
  1/A_i=n/(p*a_i)+k_i/p、k_i 为整数且 sum k_i=0，令
  g_i=gcd(n,a_i)、h_i=a_i/g_i。若全部 A_i 为正整数，则每个 A_i 必属于
  {h_i,p*h_i}。因此当 n 为偶数时，标准源解 (n/2,n,n) 已排除整个候选类；
  当 3|n 时，标准源解 (n/3,2n,2n) 也排除整个候选类。故这类公式不能从最常用
  的已知可解较小实例构造核心素数的 Sol(n) 全域提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - marked-solution-descent-closure
  - coordinatewise-affine-lift-rigidity
  - cyclic-reciprocal-transport-obstruction
topics:
  - descent
  - solution-lift
  - circularity
  - reciprocal-affine
  - integrality
  - obstruction
  - proof-program
sources:
  - claim: marked-solution-descent-closure
    role: marked-state-logical-baseline
  - claim: coordinatewise-affine-lift-rigidity
    role: denominator-affine-comparison
  - claim: cyclic-reciprocal-transport-obstruction
    role: cross-coordinate-reciprocal-comparison
  - reproduction: reproductions/full_solution_lift_circularity_reciprocal_affine_no_go.py
    role: focused-integrality-and-standard-source-controls
visibility: public
last_checked: '2026-08-12'
---

# 未标记全域提升的循环性与逐坐标倒数仿射整值障碍

## 1. 任意全域映射的存在性是循环命题

记

\[
\operatorname{Sol}(r)=
\left\{(a,b,c)\in\mathbb N^3:
\frac4r=\frac1a+\frac1b+\frac1c\right\}.
\]

若 \(\operatorname{Sol}(n)\ne\varnothing\)，则

\[
\boxed{
\operatorname{Sol}(p)\ne\varnothing
\iff
\exists\Phi:\operatorname{Sol}(n)\longrightarrow\operatorname{Sol}(p).}
\tag{1}
\]

正向只需固定一个 \(w_p\in\operatorname{Sol}(p)\)，定义常值映射
\(\Phi(u)=w_p\)。反向则取任意 \(u\in\operatorname{Sol}(n)\)，有
\(\Phi(u)\in\operatorname{Sol}(p)\)。

特别地，偶数 \(n\) 总有显式源解

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\tag{2}
\]

所以如果“真分母递降”只要求存在某种全域集合映射而不限制其构造来源，它与先证明
目标方程可解完全等价。由已知目标解定义的常值映射必须直接登记为目标 terminal；
不能再把同一解包装成 E4 递降。

这不否定显式、统一且不读取目标解的全域公式。下面排除其中一个自然候选类。

## 2. 质量保持的逐坐标倒数仿射候选

给定源解

\[
\frac4n=\frac1{a_1}+\frac1{a_2}+\frac1{a_3},
\qquad 2\le n<p,
\tag{3}
\]

取整数 \(k_1,k_2,k_3\) 满足

\[
k_1+k_2+k_3=0,
\tag{4}
\]

并尝试定义

\[
\frac1{A_i}
=\frac{n}{p a_i}+\frac{k_i}{p}
=\frac{n+k_i a_i}{p a_i}.
\tag{5}
\]

式 (3)--(4) 自动给出

\[
\sum_{i=1}^3\frac1{A_i}
=\frac np\sum_{i=1}^3\frac1{a_i}
 +\frac1p\sum_{i=1}^3k_i
=\frac4p.
\tag{6}
\]

因此该候选在有理恒等式层完全正确；唯一问题是正整数性。

## 3. 二值归一化刚性

令

\[
g_i=(n,a_i),
\qquad
n=g_i n_i,
\qquad
a_i=g_i h_i,
\qquad
(n_i,h_i)=1.
\tag{7}
\]

若 \(A_i\) 是正整数，则由 (5)

\[
g_i(n_i+k_i h_i)\mid p g_i h_i.
\tag{8}
\]

而

\[
(n_i+k_i h_i,h_i)=(n_i,h_i)=1.
\]

因为 \(p\) 为素数，正整数 \(n_i+k_i h_i\) 只能是 \(1\) 或 \(p\)。代回
(5) 得

\[
\boxed{
A_i\in\{h_i,p h_i\},
\qquad
h_i=\frac{a_i}{(n,a_i)}.}
\tag{9}

因此所有看似自由的整数平移实际上只允许逐坐标做一次二值选择：把规范分母
\(h_i\) 保持不变，或乘以 \(p\)。

## 4. 偶源与三整除源的全域 no-go

若 \(2\mid n\)，取标准源解 (2)。三个规范分母均为

\[
(h_1,h_2,h_3)=(1,1,1).
\tag{10}
\]

按 (9)，每个目标分母属于 \(\{1,p\}\)。只要一个分母为 1，目标倒数和至少为
\(1>4/p\)；若三个分母全为 \(p\)，倒数和只有 \(3/p\)。所以不存在满足
(4)--(5) 的整数目标。

若 \(3\mid n\)，另有标准源解

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}.
\tag{11}
\]

此时

\[
(h_1,h_2,h_3)=(1,2,2).
\tag{12}
\]

核心素数 \(p\ge73\)。任何未乘 \(p\) 的规范分母都会贡献至少 \(1/2>4/p\)；
若三者全乘 \(p\)，倒数和为 \(2/p\)。仍不可能等于 \(4/p\)。于是

\[
\boxed{
2\mid n\text{ 或 }3\mid n
\Longrightarrow
\text{不存在 (4)--(5) 型 }\operatorname{Sol}(n)\to\operatorname{Sol}(p)
\text{ 全域提升}.}
\tag{13}

## 5. 对下一候选的约束

式 (13) 与逐坐标分母仿射刚性、循环倒数耦合障碍覆盖不同的公式类。它允许
\(k_i\) 依赖具体源解，只要求每个 \(k_i\) 为整数且总和为零；所以扩大固定平移菜单
不会绕过该障碍。

若坚持未标记 \(\operatorname{Sol}(n)\) 全域提升，下一候选至少要改变一项：

1. 使用真正跨坐标的非线性分母；
2. 不采用质量保持的共同系数 \(n/p\)；或
3. 选择不以偶数或三整除标准解为基例的源分母，并证明其全部源解均可提升。

否则应回到严格较弱但逻辑充分的 marked solution set，并单独证明标记集非空。

聚焦验证：

~~~bash
python3 reproductions/full_solution_lift_circularity_reciprocal_affine_no_go.py --verify
~~~

