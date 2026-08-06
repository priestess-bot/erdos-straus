---
kind: claim
claim_id: type-II-hole-fourier-multiprimary-phase-capacity-sum
title: Type II HOLE Fourier 多 primary 到 F/G 分素数相位容量和
statement: HOLE_LOCKED 的非恒相位需求不必共享同一个 q。对每个选定的 q-primary 源关系方向分别建立真实的 F/G q 进清分高度、相位胞和重复 q 账本，则所有 q 的独立需求总和不超过各 q 相位胞容量之和。严格总超载迫使 Type II 命中、源秩不一致、某个 q 的相位或算术提升失败，或已有 F/G 短证书/递降出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hole-fourier-phase-cell-capacity-bridge
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-source-fiber-shared-q-ledger
  - type-I-phase-clearing-cell-capacity-contract
topics:
  - type-II
  - HOLE_LOCKED
  - Fourier
  - primary-decomposition
  - q-adic
  - phase-cell
  - capacity
  - source-switch
  - proof-boundary
sources:
  - claim: type-II-hole-fourier-phase-cell-capacity-bridge
    role: single-primary-hole-to-phase-interface
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: primary-rank-source-injection
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-deduplication
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: per-prime-phase-capacity
visibility: public
last_checked: '2026-08-05'
---

# Type II HOLE Fourier 多 primary 到 F/G 分素数相位容量和

## 1. 分素数关系需求

对每个 HOLE_LOCKED 状态 \(i\)，令 \(\Delta_i\) 是其稳定子商中剩余源积集的
差分群。有限阿贝尔群的 primary 分解写成

\[
\Delta_i=\bigoplus_{q\in\mathcal Q_i}\Delta_{i,q}.
\]

对每个选定的奇素数 \(q\in\mathcal Q_i\)，定义

\[
d_{i,q}
=\dim_{\mathbb F_q}\bigl(\Delta_{i,q}/q\Delta_{i,q}\bigr).
\tag{1}
\]

这些维数来自同一差分群的不同 primary 分量，因而可以相加；它们不是把同一个
q 层按来源块重复收费。固定参数纤维的源列注入逐素数给出：若对应源关系格不能
提供 \(d_{i,q}\) 个保持纤维的独立 q 列，则该状态必须输出
SOURCE_RANK_INCONSISTENT。

对重复的同一 q，先按候选参数的真实 q 高度合并来源层；若来源层总量为
\(L_q(s)\)、候选实际高度为 \(V_q(s)\)，只能使用

\[
d_q(s)=\min\{L_q(s),V_q(s)\}
\tag{2}
\]

个 q 层。式 (2) 是 q 内部去重，不能被跨状态或跨来源重新复制。

## 2. 每个 q 的真实相位接口

设对每个被保留的二元组 \((i,q)\)，已经单独证明它能提升到 F/G 固定载体，并
存在真实高度 \(e_{i,q}\ge d_{i,q}\)、整数表示坐标 \(A_{i,q},R_{i,q}\) 及标签
\(s_{i,q}\)，满足

\[
q\nmid A_{i,q}R_{i,q},\qquad
\gamma_{i,q}=-A_{i,q}R_{i,q}^{-1}
\pmod {q^{e_{i,q}}},
\qquad
s_{i,q}\equiv\gamma_{i,q}\pmod {q^{e_{i,q}}}.
\tag{3}
\]

对固定的 q，按

\[
q^{\min(e_{i,q},e_{j,q})}
\mid
A_{i,q}R_{j,q}-A_{j,q}R_{i,q}
\tag{4}
\]

划分相位胞。设第 \(c\) 个 q 胞的标签区间长度为 \(M_{q,c}\)，最大重复度为
\(\mu_q\)，并令 \(H_{q,c}=\max_{i\in c}e_{i,q}\)。逐 q 的相位胞合同给出

\[
\sum_i e_{i,q}
\le
\mu_q\sum_{c\in\mathcal C_q}
\left(\frac{M_{q,c}}{q-1}+H_{q,c}\right).
\tag{5}
\]

注意式 (5) 只对已经通过 source-switch 参数纤维、固定载体和标签界面的
\((i,q)\) 生效；没有这些资料的 q 方向不能放进容量和。

## 3. 多 primary 容量和

定义总 primary 需求和容量

\[
\mathcal D_{\mathcal Q}
=\sum_q\sum_i d_{i,q},
\qquad
\mathcal C_{\mathcal Q}
=\sum_q\mu_q\sum_{c\in\mathcal C_q}
\left(\frac{M_{q,c}}{q-1}+H_{q,c}\right).
\tag{6}
\]

由 \(d_{i,q}\le e_{i,q}\) 及式 (5)，得到必要条件

\[
\boxed{\quad
\mathcal D_{\mathcal Q}\le\mathcal C_{\mathcal Q}.
\quad}
\tag{7}
\]

因此不需要先假设所有状态共享同一个 q。若某个候选族已经验证了每个
\((i,q)\) 的 primary 注入、真实相位提升、重复 q 合并和相位胞标签，并且

\[
\mathcal D_{\mathcal Q}>\mathcal C_{\mathcal Q},
\tag{8}
\]

则不可能所有选定状态都留在当前 HOLE 分支。逻辑出口为：

* 某个参数纤维被合法新增源块填满，得到 Type II；
* 某个 q 的源列秩不足，输出 SOURCE_RANK_INCONSISTENT；
* 某个 q 的相位提升或带来源算术候选为空，输出 PHASE_LIFT_OBSTRUCTED
  或 ARITHMETIC_LIFT_EMPTY；
* 状态离开当前菜单并进入已有 F/G 短证书或严格递降检查。

## 4. 证明与去重

有限阿贝尔群的 primary 分解使式 (1) 的 q 维数属于互不相交的直接因子。源列
注入在每个 q 分量上分别成立；同一整数源块若同时含有不同素数，只是在不同
primary 坐标各贡献一层，不会把某个 q 层复制到另一个 q 的账本。对固定 q，式
(2) 先消除重复来源，再应用式 (5)。最后对所有 q 求和即可得到式 (7)。

所以式 (8) 是一个安全的必要容量超载判据：它可以因为各 q 的标签边界松而不够
锋利，但不会因为把同一 q 来源或同一 q 层重复计数而虚构超载。

## 5. 边界与下一步

本卡消除了“所有 HOLE 状态必须共享一个 q”这一额外假设，但仍不构造以下对象：

* 并非每个非恒相位角色都自动给出可用的 q-primary 表示坐标；
* \(d_{i,q}\) 到真实 \(e_{i,q}\) 的相位提升仍需逐状态证明；
* 没有通过来源 CRT 和除子格候选集的 q 方向不能计入 \(\mathcal C_{\mathcal Q}\)；
* \(\mathcal D_{\mathcal Q}\le\mathcal C_{\mathcal Q}\) 时不产生证书，只保留逐 q 缺口；
* 失败回执只有在另行给出严格势下降或 Type I/II 终端时才具有递归资格。

因此，下一步应把每个 HOLE 状态的差分群 primary 支持、源列注入、q 真实高度和
算术提升候选写成同一张有限表；先求分素数容量和，再对未覆盖的 q 方向执行
ARITHMETIC_LIFT_EMPTY 或 F/G 端点分类。
