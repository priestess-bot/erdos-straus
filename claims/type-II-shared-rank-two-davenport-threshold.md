---
kind: claim
claim_id: type-II-shared-rank-two-davenport-threshold
title: 共享 Type II 选择器的秩至多二 Davenport 阈值
statement: 设核心素数 p=1 mod24，合法缺口 m=3 mod4 已有 Type II 证书，并令 H 为 p+m 中与 m 互素的素因子残数生成的单位子群。若 H 的不变因子秩至多二，写 H=C_n 或 H=C_n1⊕C_n2 且 n1|n2；当单位素因子按重数计数 t>=D(H)（循环情形 D(H)=n，秩二情形 D(H)=n1+n2-1）时，存在非空 D|p+m 且 D=1 modm，结合已有 Type II 证书可重建 scaled-first marked witness。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-shared-subgroup-threshold-lemma
  - type-II-shared-p-group-davenport-threshold
  - type-II-two-tail-deflation-descent
topics:
- type-II
- shared-divisor
- finite-abelian-groups
- invariant-factors
- rank-two-groups
- davenport-constant
- zero-sum-theory
- product-sets
- short-certificate
- marked-lift
- proof-boundary
sources:
  - reproduction: reproductions/type_ii_automatic_residual_k1_funnel.py
    role: invariant-factor-recovery-and-dynamic-subproduct-verifier
  - result: reproductions/type-ii-automatic-residual-rank-two-davenport-profile-10m-results.json
    role: focused-10m-rank-two-profile
  - paper: zhong2025_davenport_rank_two
    locator: "rank-two Davenport formula in publisher abstract"
    role: exact-rank-two-threshold-input
  - paper: olson1969_davenport_p_groups
    locator: "p-group Davenport constant result"
    role: p-primary-subcase-background
  - claim: type-II-shared-subgroup-threshold-lemma
    role: prior-generated-subgroup-order-threshold
visibility: public
last_checked: '2026-08-04'
---

# 共享 Type II 选择器的秩至多二 Davenport 阈值

## 命题

设

\[
p\equiv1\pmod {24},\quad m\equiv3\pmod4,
\]

且缺口已有 Type II 证书

\[
-x\in\Pi_m(x^2),\quad x=\frac{p+m}{4}.
\tag{1}
\]

把 \(p+m\) 中所有与 \(m\) 互素的素因子按重数列成
\(q_1,\ldots,q_t\)，并令

\[
H=\langle q_1\bmod m,\ldots,q_t\bmod m\rangle
\le (\mathbb Z/m\mathbb Z)^\times.
\tag{2}
\]

若 \(H\) 的不变因子秩至多二，则有两种情形：

\[
H\simeq C_n,\quad D(H)=n,
\]

或

\[
H\simeq C_{n_1}\oplus C_{n_2},\quad n_1\mid n_2,
\quad D(H)=n_1+n_2-1.
\tag{3}
\]

当 \(t\ge D(H)\) 时，存在非空指标集 \(I\) 使

\[
D_I:=\prod_{i\in I}q_i>1,\quad D_I\mid p+m,\quad
D_I\equiv1\pmod m.
\tag{4}
\]

因此 (1) 与 (4) 同时成立，缺口满足共享 Type II 选择器条件。令

\[
k=\frac{D_I-1}{m},
\]

即可由现有重建器得到 \(km+1=D_I\mid p+m\) 及相应的 scaled-first marked
Type II witness。

## 证明

有限阿贝尔群的 Davenport 常数 \(D(H)\) 是任意长度至少 \(D(H)\) 的群元素序列都含有
非空子序列积为单位元的最小阈值。把 (2) 中的残数序列视为 \(H\) 中的序列，(3) 与
\(t\ge D(H)\) 直接给出非空 \(I\) 使

\[
\prod_{i\in I}(q_i\bmod m)=1.
\]

于是得到 (4)。每个 \(q_i\) 都是 \(p+m\) 的素因子，故 \(D_I\) 是非平凡除子；
最后一步只是同一缺口 Type II 证书与共享除子的 scaled-first 算术重建。证毕。

循环公式 \(D(C_n)=n\) 是经典结论；秩二公式
\(D(C_{n_1}\oplus C_{n_2})=n_1+n_2-1\)（\(n_1\mid n_2\)）由 Zhong 的秩二
Davenport 常数文献卡提供输入。这里使用的是 \(k=1\) 情形；不把该文献归因于
Erdős--Straus 结论。

## 可构造性与边界

脚本先按精确的 \(H[\ell^j]\) 扭元计数恢复每个素数一次分量的指数，再左补齐各
primary 分量并相乘得到不变因子；随后仅对秩至多二的群应用 (3)。通过阈值后，动态
状态表构造实际子积并逐项验证 \(D_I\mid p+m\)、\(D_I>1\)、
\(D_I\equiv1\pmod m\) 和 scaled-first 提升。因此实现验证的是应用链和算术对象，
不替代一般 Davenport 公式的群论证明。

秩至少三的子群在本卡中明确留空；低于 \(D(H)\) 的短零积、多个缺口之间的共同避靶、
以及 marked 表示到无标记递降的提升也不由本阈值推出。

## 10M 聚焦回放

对四自动缺口后的 84 个非 \(k=1\) 压力点，完整扫描

\[
p\le10^7,\quad m\le239,\quad m\equiv3\pmod4,
\]

并只在已有 Type II 证书的缺口上应用本阈值，得到：

- 秩至多二的 Type II 缺口数：933（循环 496，秩二 437）；
- 达到 Davenport 阈值的缺口数：29；
- 构造共享除子并重建 marked witness 的压力点数：29/84；
- 其中 28 个是此前的 p-primary \(C_2\oplus C_4\) 见证，新增 1 个为
  \(p=1497049,m=39,H\simeq C_2\oplus C_{12}\)，
  \(t=13,D(H)=13,D_I=44032,k=1129\)；
- 本 profile 未覆盖的压力点：55/84。

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \\
      --limit 10000000 --gap-cap 239 --rank-two-davenport-profile \\
      --output reproductions/type-ii-automatic-residual-rank-two-davenport-profile-10m-results.json

“未覆盖”只表示未达到本卡的阈值，不能推出没有其它共享除子；同样，29 个 marked
witness 也不是无标记递降或旗舰猜想的全称证明。
