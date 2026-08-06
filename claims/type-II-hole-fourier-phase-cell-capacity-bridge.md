---
kind: claim
claim_id: type-II-hole-fourier-phase-cell-capacity-bridge
title: Type II HOLE Fourier 非恒相位到 F/G q 进相位胞容量桥
statement: 在 HOLE_LOCKED 分支中，若选定的 quotient 角色在剩余源积集上非恒相位，则它产生非零的源关系初等商秩需求。若该需求可以沿一个共同的 q-primary 方向提升到 F/G 固定载体，并且每个状态的需求 d_i 被一个真实的 q 进清分高度 e_i 支付，则相位中心与嵌套同余进入已有的相位胞容量合同；需求总量超过该合同上界时，当前分支必然退出，出口只能是目标命中、源秩不一致、相位提升受阻、或已有 F/G 容量/递降回执。该桥不证明共同 q 或相位提升存在。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-kneser-saturated-one-coset-hole-certificate
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-I-phase-clearing-cell-capacity-contract
topics:
  - type-II
  - HOLE_LOCKED
  - Fourier
  - source-relation
  - q-adic
  - phase-cell
  - capacity
  - proof-boundary
sources:
  - claim: type-II-kneser-saturated-one-coset-hole-certificate
    role: hole-fourier-and-anchor-relation-split
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: relation-rank-to-source-column-demand
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: conditional-q-adic-phase-capacity
visibility: public
last_checked: '2026-08-05'
---

# Type II HOLE Fourier 非恒相位到 F/G q 进相位胞容量桥

## 1. HOLE 分支中的关系需求

固定一个参数纤维，令

\[
\overline G=G/T,\qquad \overline P=P/T,\qquad
\overline R=\prod_i B_i/T
\]

是稳定子商中的目标积集和剩余合法源积集。HOLE_LOCKED 的定义给出某个
\(x\in\overline G\) 使得

\[
\overline G\setminus\overline P=x\overline R^{-1}.
\tag{1}
\]

对 quotient 角色 \(\overline\chi\) 写

\[
S_{\overline\chi}=\sum_{r\in\overline R}\overline\chi(r),\qquad
\rho_{\overline\chi}=\frac{|S_{\overline\chi}|}{|\overline R|}.
\]

若 \(\rho_{\overline\chi}<1\)，则角色在 \(\overline R\) 上不是恒相位。令

\[
\Delta_R=\langle rr'^{-1}:r,r'\in\overline R\rangle.
\]

成对能量恒等式为

\[
\sum_{r,r'\in\overline R}
 \left|1-\overline\chi(rr'^{-1})\right|^2
=2|\overline R|^2(1-\rho_{\overline\chi}^2)>0.
\tag{2}
\]

因此 \(\Delta_R\) 在该角色下有非平凡像。对任一素数 \(q\) 分量，若

\[
d=\dim_{\mathbb F_q}\bigl(\Delta_R/q\Delta_R\bigr)>0,
\tag{3}
\]
则固定纤维的源关系格必须提供至少 \(d\) 个独立的保持纤维源列；否则由源列注入
得到 SOURCE_RANK_INCONSISTENT。这里的 \(d\) 是关系方向需求，不是角色阶或 Fourier
分母的自动高度。

## 2. 条件性的 F/G 相位提升接口

设有一组状态 \(i\)，并且已经单独证明它们共享同一个奇素数 \(q\) 的 primary
方向。对状态 \(i\)，假设：

1. 其 HOLE 关系需求中有 \(d_i>0\) 个独立的 q 初等商方向；
2. 这些方向能够由同一 F/G 固定载体的清分参数支付，并有一个真实高度
   \(e_i\ge d_i\)；
3. 对应的整数表示坐标满足 \(q\nmid A_iR_i\)，且固定 \(B_i\) 的清分条件确实是
   \(q^{e_i}\mid A_i+R_i s_i\)。

于是相位中心与标签必须满足

\[
\gamma_i\equiv-A_iR_i^{-1}\pmod {q^{e_i}},\qquad
s_i\equiv\gamma_i\pmod {q^{e_i}}.
\tag{4}
\]

若状态 \(i,j\) 被宣称属于同一相位胞，则必须有

\[
q^{\min(e_i,e_j)}\mid
(A_iR_j-A_jR_i),
\tag{5}
\]

并且

\[
s_i\equiv s_j\pmod {q^{\min(e_i,e_j)}}.
\tag{6}
\]

因此，这些状态的高度需求进入 q 进相位胞装箱，而不是进入一个抽象的 Fourier
频率池。若第 \(c\) 个相位胞的标签区间长度为 \(M_c\)、最大重复度为 \(\mu\)，
且 \(H_c=\max_{i\in c}e_i\)，已有相位胞合同给出

\[
\sum_i e_i\le
\mu\sum_c\left(\frac{M_c}{q-1}+H_c\right).
\tag{7}
\]

结合 \(d_i\le e_i\)，得到必要条件

\[
\boxed{\quad
\sum_i d_i\le
\mu\sum_c\left(\frac{M_c}{q-1}+H_c\right).
\quad}
\tag{8}
\]

若一个候选的共同-q、真实高度和相位胞假设均已验证，但 (8) 被严格违反，则不可能
所有状态都留在当前 HOLE 分支。至少一个状态必须发生以下出口之一：

* 目标纤维被合法新增源块填满，得到 Type II 命中；
* 源关系列不能支付所需初等商秩，输出 SOURCE_RANK_INCONSISTENT；
* 共同 q 或相位中心的提升不存在，输出 PHASE_LIFT_OBSTRUCTED；
* 该状态离开当前 F/G 容量菜单，进入已有的 Type I/II 短证书或严格递降检查。

## 3. 证明

式 (2) 把 HOLE_LOCKED 的非恒相位角色转化为差分群的非零初等商方向。固定纤维
的源列注入把每个方向送回保持参数纤维的 q-height 账本，因此得到 \(d_i\) 的
真实需求。对能够提升到 F/G 固定载体的状态，式 (4)--(6) 是清分同余及其交叉
行列式判据；同胞状态的标签形成嵌套 q-adic 链。相位胞合同对每个高度层装箱，先
给出式 (7)，再因 \(d_i\le e_i\) 得式 (8)。所以当式 (8) 超载时，所列出口是一个
完备的逻辑分派，而不是把容量不足误记为猜想反例。

## 4. 边界与下一步

本桥仍是条件性桥接，不包含以下未证明命题：

* 不保证不同 HOLE 状态存在共同的 q-primary 方向；
* 不保证非恒相位角色一定能写成 F/G 的固定 \(A_i,R_i,B_i\) 清分相位；
* 不把角色阶、核大小或 Fourier 振幅直接等同于 \(e_i\)；
* PHASE_LIFT_OBSTRUCTED 本身不是递降，必须另行给出 source-switch 后继或已有
  Type I/II 证书；
* q 进相位胞合同仍要求有界标签、重复度及合法 E1--E5 条件的独立证明。

因此，当前真正的决定性子目标是：从 HOLE 关系群中构造一个跨状态共同 q 的真实
表示坐标，并证明其相位提升满足 (4)。一旦完成，式 (8) 提供可计算的容量超载门；
若提升失败，则应优先把失败实例送入算术 source-switch 候选集，而不是继续扩大
抽象 Fourier 菜单。
