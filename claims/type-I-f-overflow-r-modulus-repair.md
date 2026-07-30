---
kind: claim
claim_id: type-I-f-overflow-r-modulus-repair
title: 盒外见证的 R 因子修复分支
statement: 对满足 4K=pR+1 的目标见证 A/B（A+B=Rm_0、(A,B)=1），令 g_R=gcd(R,B-1)。任取 m|g_R、m=3 (mod 4)、3<=m<=p-2，则 e=KA 满足 4e+1=0 (mod m)，并定义新的合法状态 R'=(4e+1)/m、K'=((p+m)/4)R'-e，且 4K'=pR'+1。若 e|((p+m)/4)^2，则得到直接 Type I 目标除子证书；否则该 m 是精确的平方整除失败标签。冻结的 253 个半径六见证在正反方向共出现 138 个非平凡 g_R、149 个候选缺口，0 个直接平方命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-rational-gap-denominator
topics:
- type-I
- F-state
- rational-gap
- q-adic
- modulus-repair
- descent
- proof-program
sources:
- claim: type-I-f-overflow-rational-gap-denominator
  role: overflow-witness-arithmetic
visibility: public
last_checked: '2026-07-30'
---

# 盒外见证的 \(R\) 因子修复分支

## 定理

令 \(p\equiv1\pmod {24}\) 为核心素数，\(R\equiv3\pmod4\) 为一个合法状态模数，并令

\[
K=\frac{pR+1}{4}.
\]

设目标仿射见证给出互素分解

\[
\frac AB\equiv-1\pmod R,
\qquad
(A,B)=1,
\qquad
N=\frac{4KA+B}{R}\in\mathbb Z_{>0}.
\]

定义

\[
g_R=\gcd(R,B-1).
\tag{1}
\]

对任意

\[
m\mid g_R,
\qquad
m\equiv3\pmod4,
\qquad
3\le m\le p-2,
\tag{2}
\]

令

\[
e=KA,
\qquad
R_m=\frac{4e+1}{m},
\qquad
x_m=\frac{p+m}{4},
\qquad
K_m=x_mR_m-e.
\tag{3}
\]

则 \(R_m\) 是正奇数且 \(R_m\equiv3\pmod4\)，\(K_m\) 为正整数，并满足

\[
4K_m=pR_m+1.
\tag{4}
\]

因此 \((p,m,R_m,K_m)\) 是一个新的合法 Type I 状态。若进一步

\[
e\mid x_m^2,
\tag{5}
\]

则 \(e\) 是该新状态的 Type I 目标除子，因为

\[
4e\equiv-1\pmod m.
\tag{6}
\]

## 证明

由 \(RN=4KA+B\)，有

\[
4e+1=4KA+1=RN-(B-1).
\tag{7}
\]

条件 (1)--(2) 使 \(m\mid R\) 且 \(m\mid B-1\)，所以 \(m\mid4e+1\)，
从而 \(R_m\in\mathbb Z\)。由于 \(4e+1\) 与 \(m\) 都是奇数，
\(R_m\) 为奇数；又 \(4e+1\equiv1\pmod4\)、\(m\equiv3\pmod4\)，故
\(R_m\equiv3\pmod4\)。

由 \(4x_m=p+m\) 和 \(4e+1=mR_m\)，

\[
4K_m=(p+m)R_m-4e=pR_m+1,
\]

得到 (4)。同时

\[
4K_m
=\frac{p(4e+1)+m}{m}
=\frac{4pKA+p+m}{m}>0,
\]

故 \(K_m>0\)。由 (4) 立即得到 \(\gcd(K_m,R_m)=1\)。若 (5) 成立，
则 \(e\mid x_m^2\)，而 (6) 是 Type I 目标除子同余，故证书成立。

## 平方失败的精确 \(q\)-进缺口

写 \(R=mt\)。由 \(4K=pR+1\) 和 \(4x_m=p+m\)，直接消去 \(p\) 得

\[
4mt\,x_m=4K+m^2t-1.
\]

对任意 \(q\mid K\)，因为 \((K,R)=1\)，有 \(q\nmid mt\)，从而

\[
v_q(x_m)
=v_q(4K+m^2t-1)-2\mathbf1_{q=2}.
\]

写 \(K=\prod_q q^{\nu_q}\)，若 \(z\) 是原见证的方向指数，则
\[
v_q(e)=v_q(KA)=\nu_q+\max(z_q,0).
\]
因此定义

\[
\delta_{q,m}
=\max\left\{\nu_q+\max(z_q,0)-2v_q(x_m),0\right\}.
\]

则
\[
e\mid x_m^2
\iff
\delta_{q,m}=0\quad\text{对所有 }q\mid K.
\]

所以每个 \(R\)-因子候选都携带一个精确的平方缺口向量
\((\delta_{q,m})_{q\mid K}\)，可以作为后续跨状态 \(q\)-进容量的需求，而不是只记录
“平方整除失败”这一位信息。

## 与有理缺口分母的关系

这条分支不把

\[
\frac{4K(A/B)+1}{R}
\]

误当成整数缺口，而是利用同一个清分子恒等式 (7)，把 \(B-1\) 与原模数 \(R\) 的
公共因子提取为新的合法缺口。它与 \(B\mid K\) 时的规范候选 \(e=(K/B)A\)
不同：这里 \(e=KA\) 保持整数，但允许模数从 \(R\) 变成 \(R_m\)。

若 (5) 失败，令

\[
D_m=\gcd(e,x_m^2),
\qquad
M_m=\gcd(m,4D_m+1).
\tag{8}
\]

则 \(D_m\mid x_m^2\)，且 \(D_m\equiv-1/4\pmod {M_m}\)。因此 \(M_m\) 的每个
满足 (2) 的因子 \(m'\) 都是一个二次修复候选；只有再次检查
\(D_m\mid((p+m')/4)^2\)，才得到直接证书。若所有候选均失败，\((g_R,M_m)\)
是带模数标签的失败对象，可接入跨状态容量或良基下降。

## 冻结审计

对有理缺口分母桥中的 253 个半径六见证同时审计正向和反向见证：

~~~text
input_record_count: 253
orientation_record_count: 506
nontrivial_repair_modulus_count: 138
candidate_orientation_count: 116
candidate_gap_count: 149
direct_square_hit_count: 0
square_deficit_layers: 1736
deficient_q_coordinate_count: 581
maximum_square_deficit: 31
forward_nontrivial_repair_modulus_count: 33
forward_candidate_gap_count: 27
forward_direct_square_hit_count: 0
forward_square_deficit_layers: 268
forward_deficient_q_coordinate_count: 121
reverse_nontrivial_repair_modulus_count: 105
reverse_candidate_gap_count: 122
reverse_direct_square_hit_count: 0
reverse_square_deficit_layers: 1468
reverse_deficient_q_coordinate_count: 460
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-r-modulus-repair-results.json
~~~

结果文件 SHA-256：

~~~text
eb261d60a8a3395b4a28b69818ec3e5650a5b272428cf5df4d23b95becff348f
~~~

这条分支在冻结样本中没有直接平方命中，但产生了 149 个经过严格同余和状态重构
检查的候选缺口；其平方失败精确累计 1736 层、涉及 581 个 \((q,m)\) 坐标。它的理论增量是把“盒外见证失败”拆成两个可验证出口：

1. \(e\mid x_m^2\)：直接获得新的 Type I 证书；
2. \(e\nmid x_m^2\)：得到带 \(R\)-因子和修复模数标签的失败状态，继续进入容量或递降。

它仍不是全称选择器：候选状态的 \(R_m\) 可能变大，平方整除失败也没有自动给出严格
算术下降。因此后续必须证明 \(R_m\)、\(M_m\) 或相位标签在某个良基势函数下严格下降，
或者证明这些标签在跨状态中发生容量超载。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_r_modulus_repair.py
~~~
