---
kind: claim
claim_id: type-I-f-overflow-rational-gap-denominator
title: 盒外目标见证的精确有理缺口分母
statement: 对满足 4K=1 (mod R) 的状态和目标仿射见证 z（prod q_i^z=-1 (mod R)），令 A/B=prod q_i^{z_i} 为互素分解。则 N=(4KA+B)/R 为正整数，且 gcd(N,B)=gcd(4K,B)。形式缺口 (4K(A/B)+1)/R=N/B 的约分分母为 B/gcd(B,4K)，其 q_i 指数恰为 max(-z_i-v_q(4K),0)。同时 m_0=(A+B)/R 为整数，形式 Type I 首分母 x_z=K m_0/B 的约分分母为 B/gcd(B,K)，其奇素数指数恰为负向盒外溢出；若 B|K，则 e_z=(K/B)A 自动满足 4e_z+1=m_zR，且 D_z=gcd(e_z,x_z^2)、M_z=gcd(m_z,4D_z+1) 给出可检验的候选缺口修复分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- rational-gap
- q-adic
- descent
- proof-program
sources:
- claim: type-I-f-relation-lattice-certificate-reconstruction
  role: affine-target-witness-interface
- claim: type-I-target-divisor-overflow
  role: integer-overflow-context
visibility: public
last_checked: '2026-07-30'
---

# 盒外目标见证的精确有理缺口分母

## 定理

令 \(R\) 为奇数，\(\gcd(K,R)=1\)，并满足

\[
4K\equiv1\pmod R,
\qquad
K=\prod_iq_i^{\nu_i}.
\]

设 \(z=(z_i)\in\mathbb Z^r\) 是目标仿射格中的任意见证：

\[
\prod_iq_i^{z_i}\equiv-1\pmod R.
\]

分解

\[
A=\prod_iq_i^{\max(z_i,0)},
\qquad
B=\prod_iq_i^{\max(-z_i,0)},
\qquad
(A,B)=1.
\]

于是 \(A/B\equiv-1\pmod R\)。定义

\[
N=\frac{4KA+B}{R}.
\]

则 \(N\) 是正整数，并且

\[
\gcd(N,B)=\gcd(4K,B).
\tag{1}
\]

因此形式缺口

\[
m_z=\frac{4K(A/B)+1}{R}=\frac NB
\tag{2}
\]

约分后的分母是

\[
B_z=\frac{B}{\gcd(B,4K)}.
\tag{3}
\]

此外，令

\[
m_0=\frac{A+B}{R}.
\]

则 \(m_0\) 为正整数，\((m_0,B)=1\)，并且形式 Type I 首分母满足精确恒等式

\[
x_z=\frac{p+m_z}{4}=\frac{K m_0}{B}.
\tag{4}
\]

所以 \(x_z\) 的约分分母为

\[
X_z=\frac{B}{\gcd(B,K)},
\qquad
v_{q_i}(X_z)=\max\{-z_i-\nu_i,0\}.
\tag{5}
\]

若 \(X_z=1\)，令 \(H=K/B\) 并定义候选目标除子
\[
e_z=HA.
\]
此时 \(m_z\) 与 \(x_z\) 都是整数，且
\[
4e_z+1=m_zR,
\]
所以 \(e_z\equiv-1/4\pmod {m_z}\)。这只是规范同余候选；要成为 Type I 除子证书，
仍需验证 \(e_z\mid x_z^2\)、自然范围和正规形条件。

即使 \(e_z\nmid x_z^2\)，令
\[
D_z=\gcd(e_z,x_z^2),
\qquad
M_z=\gcd(m_z,4D_z+1).
\]
则 \(D_z\mid x_z^2\)，且 \(D_z\equiv-1/4\pmod {M_z}\)。因此 \(M_z\) 的每个
\(m'\equiv3\pmod4\)、\(3\le m'\le p-2\) 的因子都是候选缺口；只有进一步验证
\(D_z\mid ((p+m')/4)^2\) 后，才得到缺口 \(m'\) 的合法 Type I 目标除子证书。
若候选模数或新首分母平方整除失败，则 \(M_z\) 是精确的修复失败标签。

对形式缺口本身，逐素数地有

\[
v_{q_i}(B_z)
=\max\{-z_i-v_{q_i}(4K),0\}
=\max\{-z_i-\nu_i-2\mathbf1_{q_i=2},0\}.
\tag{6}
\]

特别地，对奇素数 \(q_i\)，

\[
v_{q_i}(B_z)=v_{q_i}(X_z)=\max\{-z_i-\nu_i,0\},
\tag{7}
\]

正是 \(z_i\) 的负向盒外溢出层数。

## 证明

由 \(A/B\equiv-1\pmod R\) 和 \(4K\equiv1\pmod R\)，有

\[
4KA+B\equiv A+B\equiv0\pmod R,
\]

故 \(N\in\mathbb Z_{>0}\)。又每个 \(q_i\mid K\) 且 \(\gcd(K,R)=1\)，所以

\[
(B,R)=1.
\]

从 \(RN=4KA+B\) 出发，因 \(R\) 与 \(B\) 互素，

\[
\gcd(N,B)=\gcd(RN,B)=\gcd(4KA+B,B).
\]

而 \((A,B)=1\)，故

\[
\gcd(4KA+B,B)=\gcd(4KA,B)=\gcd(4K,B),
\]

得到 (1)--(3)。又由 \(A+B\equiv0\pmod R\) 得
\(m_0=(A+B)/R\in\mathbb Z_{>0}\)。因 \((B,R)=1\)，

\[
\gcd(m_0,B)=\gcd(A+B,B)=1.
\]

利用 \(p=(4K-1)/R\) 和 \(m_z=N/B\)，有

\[
\frac{p+m_z}{4}
=\frac{(4K-1)B+(4KA+B)}{4BR}
=\frac{K(A+B)}{BR}
=\frac{K m_0}{B},
\]

得到 (4)。再对 \(q_i\) 取赋值得到 (5)。最后，

若 \(X_z=1\)，则 \(B\mid K\)。令 \(H=K/B\)，由 (2)--(3) 得
\[
m_z=\frac{4HA+1}{R}\in\mathbb Z,\qquad
e_z=HA,\qquad
4e_z+1=m_zR,
\]
故 \(e_z\equiv-1/4\pmod {m_z}\)。这一步只给出同余候选，不包含
\(e_z\mid x_z^2\) 或自然范围。

令 \(D_z=\gcd(e_z,x_z^2)\)、\(M_z=\gcd(m_z,4D_z+1)\)，则前者显然整除 \(x_z^2\)，
后者整除 \(4D_z+1\)，所以 \(D_z\equiv-1/4\pmod {M_z}\)。任何满足自然范围的
\(3\bmod4\) 因子 \(m'\mid M_z\) 都保留这个同余；还必须用新首分母
\(x'=(p+m')/4\) 检查 \(D_z\mid {x'}^2\)。

\[
v_{q_i}(4K)=\nu_i+2\mathbf1_{q_i=2},
\qquad
v_{q_i}(B)=\max(-z_i,0),
\]

立即得到 (6)--(7)。

## 对统一选择器的意义

这条结果把“盒外见证”转换为一个无条件的算术对象，但要准确区分两种情形：

1. \(X_z=1\)：形式 Type I 首分母是整数，并且上面的 \(e_z\) 给出同一缺口的规范
   同余候选；若它不整除 \(x_z^2\)，则 \(D_z,M_z\) 给出一个可检验的修复分支：
   \(M_z\) 只提供候选缺口，还要用新首分母检查平方整除；若该检查失败，仍需把 \(M_z\)
   作为失败标签接入容量或递降。\(B_z\) 还可能因 \(4\) 的二因子比 \(X_z\) 多吸收两层，
   因此二者要分开记录。
2. \(B_z>1\)：形式缺口不是整数。其分母的每一层都不能由 \(4K\) 自身吸收；对奇素数
   坐标，层数恰等于盒外溢出。这是一个严格的“未支付溢出”证书，而不是启发式的
   载体高度。

因此，任何真正的跨状态容量证明都必须完成下面二者之一：

\[
\boxed{
\text{将 }B_z\text{ 的素因子幂映射到可比较的标签/模数/块差容量}
\quad\text{或}\quad
\text{由 }B_z>1\text{ 构造严格可提升的较小标记状态}.
}
\]

这比直接假设“每个溢出层收费一个已有载体高度”更精确：已有载体只证明 \(q\mid4K\)，
而 \(B_z\) 记录的是超出 \(v_q(4K)\) 后仍无法被 \(4K\) 吸收的部分。

## 冻结见证验证

对冻结分色 F 状态中半径不超过六的 253 个目标见证逐项验证：

~~~text
record_count: 253
orientation_with_nontrivial_denominator_count: 253
odd_overflow_denominator_record_count: 253
formal_first_denominator_integral_record_count: 8
formal_reverse_first_denominator_integral_record_count: 96
formal_first_denominator_nontrivial_in_either_orientation_count: 253
canonical_target_divisor_candidate_count: 8
canonical_target_divisor_square_divisibility_count: 0
canonical_repair_modulus_nontrivial_count: 1
canonical_repair_modulus_admissible_count: 0
canonical_repair_gap_candidate_count: 0
canonical_repair_square_hit_count: 0
reverse_canonical_repair_modulus_nontrivial_count: 18
reverse_canonical_repair_gap_candidate_count: 6
reverse_canonical_repair_square_hit_count: 0
~~~

正向见证的分母层总数为 1182；将见证取反后得到的反向分母层总数为 519。两者分别
记录负向和正向溢出，不能相加解释为新的独立需求。正向首分母在 245 个状态中非整数，
反向首分母在 157 个状态中非整数；但每个状态至少有一个方向的首分母非整数，并且
每个状态至少有一个方向出现额外奇素数分母。该验证确认：当前严格缺口不是“已有块高度
不足”的单纯数值现象，而是某一方向的形式 Type I 缺口确实带有无法由 \(K\) 消除的
额外奇素数幂。8 个正向整数首分母方向都能构造规范同余候选 \(e_z\)，但 8 个候选
均不整除对应的 \(x_z^2\)，所以整数化仍没有直接给出 Type I 命中。
对这 8 个方向取最大平方投影后，\(M_z\) 只有一个非平凡值（为 5），且没有一个
含有自然范围内的 \(3\bmod4\) 因子；因此该规范修复分支在冻结样本上没有产生候选
缺口，更没有进入新首分母平方整除检查，但把失败形式化成了可比较的修复模数。
取反方向后，96 个整数首分母方向中有 18 个非平凡修复模数，产生 6 个候选缺口；
这 6 个候选全部未通过新首分母的平方整除，故没有形成直接 Type I 命中。

复现：

~~~bash
python3 reproductions/type_i_f_overflow_rational_gap_denominator.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-rational-gap-denominator-results.json
~~~

结果文件 SHA-256：

~~~text
8463e8885202506b680d31f9c62b98f5b63f63e421fe4722cd72ad46ab13fee0
~~~

该有限验证仍不构成跨状态容量矛盾，也不说明每个盒外见证都能产生递降；它把下一步
需要证明的算术映射精确化为 \(B_z\) 或 \(X_z\) 的分母幂如何进入状态选择或可提升
标记集。
