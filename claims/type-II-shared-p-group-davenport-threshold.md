---
kind: claim
claim_id: type-II-shared-p-group-davenport-threshold
title: 共享 Type II 选择器的 p 群 Davenport 阈值
statement: 设核心素数 p=1 mod24，合法缺口 m=3 mod4 已有 Type II 证书，并令 H 为 p+m 中与 m 互素的素因子残数生成的单位子群。若 H 是有限阿贝尔 ell 群，H 同构于直和 C_(ell^a_i)，且单位素因子按重数计数为 t>=D(H)=1+sum_i(ell^a_i-1)，则存在非平凡 D|p+m 且 D=1 modm；结合已有 Type II 证书得到共享选择器，并可重建 scaled-first marked Type II witness。这是对 t>=|H| 前缀阈值的严格 p-primary 收紧，不是所有 H 的统一阈值，也不消除未命中压力点。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-shared-subgroup-threshold-lemma
  - type-II-two-tail-deflation-descent
topics:
- type-II
- shared-divisor
- finite-abelian-groups
- p-groups
- davenport-constant
- zero-sum-theory
- product-sets
- short-certificate
- marked-lift
- proof-boundary
sources:
  - reproduction: reproductions/type_ii_automatic_residual_k1_funnel.py
    role: p-group-Davenport-data-and-subproduct-verifier
  - result: reproductions/type-ii-automatic-residual-p-group-davenport-profile-10m-results.json
    role: focused-10m-profile
  - claim: type-II-shared-subgroup-threshold-lemma
    role: prior-generated-subgroup-order-threshold
  - paper: olson1969_davenport_p_groups
    locator: "p-group Davenport constant result"
    role: exact-p-group-threshold
  - paper: grynkiewicz_marchan_ordaz2009
    locator: "finite abelian subsequence-sum framework"
    role: finite-abelian-zero-sum-background
visibility: public
last_checked: '2026-08-04'
---

# 共享 Type II 选择器的 p 群 Davenport 阈值

## 命题

设

\[
p\equiv1\pmod {24},\qquad 3\le m\le p-2,
\qquad m\equiv3\pmod4,
\qquad x=\frac{p+m}{4}.
\]

假设该缺口已经有 Type II 证书

\[
-x\in\Pi_m(x^2).
\tag{1}
\]

把 \(p+m\) 中所有与 \(m\) 互素的素因子按重数列成

\[
q_1,\ldots,q_t,
\qquad \gcd(q_i,m)=1,
\]

并令

\[
H=\langle q_1\bmod m,\ldots,q_t\bmod m\rangle
\le (\mathbb Z/m\mathbb Z)^\times.
\tag{2}
\]

若 \(H\) 是有限阿贝尔 \(\ell\)-群，写成

\[
H\simeq C_{\ell^{a_1}}\oplus\cdots\oplus C_{\ell^{a_r}},
\]

并且

\[
t\ge D(H):=1+\sum_{i=1}^r(\ell^{a_i}-1),
\tag{3}
\]

则存在一个非空子序列 \(I\subseteq\{1,\ldots,t\}\)，使

\[
D_I:=\prod_{i\in I}q_i>1,
\qquad D_I\mid p+m,
\qquad D_I\equiv1\pmod m.
\tag{4}
\]

因此 (1) 与 (4) 同时成立，缺口 \(m\) 满足共享 Type II 选择器的两个残数条件。
取

\[
k=\frac{D_I-1}{m},
\]

即可用现有重建器得到

\[
km+1=D_I\mid p+m,
\]

以及相应的 scaled-first marked Type II witness。

## 证明

有限阿贝尔 \(\ell\)-群的 Davenport 常数满足

\[
D(H)=1+\sum_i(\ell^{a_i}-1).
\tag{5}
\]

其定义性质是：任意长度至少 \(D(H)\) 的 \(H\) 中元素序列都有一个非空子序列积为
单位元。把 (2) 中的 \(q_i\bmod m\) 看成 \(H\) 中的序列，条件 (3) 直接给出
一个非空 \(I\) 使

\[
\prod_{i\in I}(q_i\bmod m)=1.
\]

于是得到 (4)。因为每个 \(q_i\) 都是 \(p+m\) 的素因子，\(D_I\) 是 \(p+m\) 的
非平凡除子。最后，(1) 是同一缺口的 Type II 证书，故共享选择器两项同时成立。
证毕。

这里的新收紧只发生在 p-primary 情形。此前的生成子群阶引理要求

\[
t\ge |H|,
\]

并用前缀碰撞构造子积；(3) 使用完整的子序列零积定理，通常允许更短的阈值。例如

\[
H\simeq C_2\oplus C_4
\quad\Longrightarrow\quad
|H|=8,\qquad D(H)=1+(2-1)+(4-1)=5.
\]

所以五个单位素因子已经足以替代旧的八因子阈值。对一般非 p-primary 的有限阿贝尔
群，本卡不声称使用同一公式；应改用相应群的 Davenport 常数或其它零积结构定理。

## 可构造性与验证边界

脚本不会把 (5) 当成一个不透明的群结构猜测，而是按精确的扭元计数恢复指数。令

\[
c_k=\log_\ell |H[\ell^k]|,
\qquad c_0=0.
\]

差分 \(c_k-c_{k-1}\) 给出指数至少为 \(k\) 的循环因子数，再由相邻差分恢复
\(a_i\)，最后重算 (5)。通过阈值后，动态状态表在单位残数集合上构造任意非空子积
\(\equiv1\pmod m\)，并逐项验证 \(D_I\mid p+m\)、\(D_I>1\) 以及 scaled-first
Type II 提升。这个实现验证的是应用链和算术对象；它不替代 (5) 的一般群论证明。

## 10M 聚焦回放

对四自动缺口后的 84 个非 \(k=1\) 压力点，完整扫描

\[
p\le10^7,
\qquad m\le239,
\qquad m\equiv3\pmod4,
\]

并只在已有 Type II 证书的缺口上应用本阈值，得到：

- p-primary 生成子群缺口数：51；
- 达到 Davenport 阈值的缺口数：28；
- 由本阈值构造共享除子并重建 marked witness 的压力点数：28/84；
- 阈值分布（按缺口计）：\(D(H)=5\) 有 28 个，\(D(H)=17\) 有 23 个；
- 本阈值未覆盖的压力点：56/84。

28 个压力点的见证、素因子重数、生成子群阶、Davenport 常数和 \(\ell\)-指数均保存在
[10M p 群 Davenport 回放结果](../reproductions/type-ii-automatic-residual-p-group-davenport-profile-10m-results.json)
中。可用以下命令重建：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 10000000 --gap-cap 239 --p-group-davenport-profile \
      --output reproductions/type-ii-automatic-residual-p-group-davenport-profile-10m-results.json

## 研究含义与限制

这条引理把“共享除子必须由很多单位素因子组成”的粗计数，推进为“在 p-primary
残数子群中达到精确零积阈值”。它给出了当前 Type II 主线第一个严格利用群结构、且在
有限压力集产生新命中的正向分支。

它仍不关闭共享 Type II 选择器猜想：

1. 56 个压力点没有被这条 p-primary 阈值覆盖；
2. 非 p-primary 的生成子群没有进入本卡；
3. 未达到 \(D(H)\) 的序列仍可能有更短零积，反之 profile 的 miss 也不证明没有共享
   除子；
4. 即使得到共享除子，现有接口给出的是 marked Type II 表示，不能直接冒充无标记的
   全域递降。

因此下一步应研究非 p-primary 群的 Davenport/Kneser 分层、低于 \(D(H)\) 的短零积
逆结构，以及跨多个缺口的共同避靶条件；不应把本卡的 28/84 有限回放写成全称结果。
