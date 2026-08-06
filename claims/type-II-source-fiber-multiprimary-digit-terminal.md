---
kind: claim
claim_id: type-II-source-fiber-multiprimary-digit-terminal
title: Type II 源纤维有限阿贝尔多 primary 进位终端
statement: 设固定参数纤维的目标差分商分解为若干循环 primary 因子，并将保持纤维且可独立选择的二点源块按因子分组。若每个 primary 因子的每个精确进位层都有至少 ell-1 个合法块，则这些块的和集覆盖整个差分商，锚点在商内时直接给出 Type II 命中；目标缺失则给出锚点外置或一个明确的 primary/进位层容量缺口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-source-lattice-fibered-kneser-selector
topics:
  - type-II
  - source-fiber
  - finite-abelian-groups
  - multiprimary
  - cyclic
  - digit-terminal
  - generalized-dyadic
  - q-height
  - capacity
  - constructive-certificate
sources:
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: cyclic-primary-digit-cover
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: q-height-source-column-input
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: integer-Type-II-lift
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维有限阿贝尔多 primary 进位终端

## 1. 目标商与合法二点块

固定一个参数纤维，并令目标关系差分商为有限阿贝尔群

\[
H=\bigoplus_{\nu=1}^{m}C_{\ell_\nu^{a_\nu}},
\qquad
\ell_\nu\ne\ell_\mu\quad(\nu\ne\mu),
\tag{1}
\]

其中 \(C_{\ell_\nu^{a_\nu}}\) 使用加法记号。设已有基积集和目标锚点已经被投影到
\(H\)，并且剩余源关系由一组可以独立选择的二点块

\[
B_j=\{0,v_j\}\subseteq H
\tag{2}
\]

给出。把这些块分成不交的组 \(J_\nu\)，要求

\[
v_j\in C_{\ell_\nu^{a_\nu}}\subseteq H
\qquad(j\in J_\nu).
\tag{3}
\]

也就是说，第 \(\nu\) 组只改变一个 primary 因子；每个二点选择仍必须通过当前
参数纤维的 source-switch、整数回译和来源标签合同。条件 (3) 是一个便于核验的
分组条件，不把不同因子的块任意池化。

对 \(v\ne0\) 属于 \(C_{\ell_\nu^{a_\nu}}\)，定义精确进位层

\[
\operatorname{val}_\nu(v)
=\max\{0\le k<a_\nu:v\in\ell_\nu^kC_{\ell_\nu^{a_\nu}}\}.
\tag{4}
\]

记第 \(\nu\) 个 primary 的第 \(k\) 层块数为

\[
c_{\nu,k}
=\#\{j\in J_\nu:\operatorname{val}_\nu(v_j)=k\},
\qquad
0\le k<a_\nu.
\tag{5}
\]

## 2. 多 primary 覆盖定理

假设对所有 \(\nu,k\) 都有

\[
\boxed{c_{\nu,k}\ge\ell_\nu-1.}
\tag{6}
\]

令

\[
\Sigma=\sum_{j}\,B_j
=\left\{\sum_j\varepsilon_jv_j:\varepsilon_j\in\{0,1\}\right\}.
\tag{7}
\]

则

\[
\boxed{\Sigma=H.}
\tag{8}
\]

### 证明

固定 \(\nu\)。由 (3)，第 \(\nu\) 组的和集
\(\Sigma_\nu=\sum_{j\in J_\nu}B_j\) 完全位于
\(C_{\ell_\nu^{a_\nu}}\)。条件 (6) 正是循环
\(\ell_\nu\)-primary 进位层终端的假设，故

\[
\Sigma_\nu=C_{\ell_\nu^{a_\nu}}.
\tag{9}
\]

由于不同组支撑在不同直和因子，任意
\((x_1,\ldots,x_m)\in H\) 可分别取
\(x_\nu\in\Sigma_\nu\)，再把这些选择相加；于是
\(\Sigma=\Sigma_1\oplus\cdots\oplus\Sigma_m=H\)。证毕。

## 3. Type II 命中与缺口回执

设剩余目标锚点为 \(\alpha\in H\)。若

\[
\alpha^{-1}\in H
\tag{10}
\]

并且 (6) 成立，则由 (8) 选出 \(\varepsilon_j\) 使
\(\sum_j\varepsilon_jv_j=\alpha^{-1}\)。把这些关系块按原参数纤维的整数回译，
得到 \(-1\) 的实际目标命中，因而构造 Type II 短证书。

反之，若目标在该纤维中缺失，则至少有一个可复核的出口：

\[
\boxed{
\alpha^{-1}\notin H
\quad\text{或}\quad
\exists(\nu,k):c_{\nu,k}\le\ell_\nu-2.
}
\tag{11}
\]

第二项记录为
\(\mathrm{MULTIPRIMARY\_DIGIT\_DEFICIT}(\nu,k)\)，并保留该层所有合法源块及其
q-height/来源标签；它不是把未证明的跨 primary 容量误写成全局矛盾。

当 \(\ell_\nu=2\) 时，条件 (6) 只要求每个 2 进位层有一个合法块，所以 (11)
给出广义 \(2^j\) 终端的最小缺口。对单一 primary，(8) 退化为已有的
\(C_{\ell^a}\) 数字终端。

## 4. 与 q-height 列注入的接线

若第 \(\nu\) 个 primary 的每个二点块由一个真实 q-height 源列产生，则先用固定
纤维列注入计算其在 \(H/\ell_\nu H\) 及各进位层的合法代表，再按 (5) 去重。重复
q 或稳定子吸收的列不增加 \(c_{\nu,k}\)。因此 (6) 是一个可直接核验的容量条件：

* 所有层达到阈值：得到构造性 Type II 终端；
* 某层低于阈值：得到带 primary、层号、源列清单的严格缺口；
* 锚点不在差分商：得到 ANCHOR_OUTSIDE_DIFFERENCE，而不是容量失败。

这一步只在分组条件 (3) 和独立选择条件成立时调用；不同 primary 的混合块需要先
做一个保持纤维的三角化/源关系证明，不能仅凭群分解自动分组。

## 5. 小型校验样例

取

\[
H=C_4\oplus C_3.
\]

在 \(C_4\) 中取一个精确层 0 块 \(\{0,1\}\) 和一个精确层 1 块
\(\{0,2\}\)；在 \(C_3\) 中取两个非零块 \(\{0,1\},\{0,1\}\)。于是

\[
\{0,1\}+\{0,2\}=C_4,\qquad
\{0,1\}+\{0,1\}=C_3,
\]

从而四个块的总和为 \(C_4\oplus C_3\)。若删去 \(C_4\) 的层 1 块，
\(\mathrm{MULTIPRIMARY\_DIGIT\_DEFICIT}(2,1)\) 被精确触发；若锚点投影不在
\(C_4\oplus C_3\)，则改记锚点外置。

## 研究边界

本定理把单一循环 primary 终端提升为有限阿贝尔分块终端，完成了从真实 q-height
列到广义 \(2^j\) 命中/层缺口的构造性映射。但它不证明任意核心素数都满足分组条件
(3)、独立选择或全部层阈值；层缺口仍需连接到另一条 Type I/II 射线、低模数商或
严格良基递降，才能闭合全称选择器。对每个循环因子，先应用
[Type II 循环 primary 最高缺口的饱和尾压缩与严格递降](type-II-source-fiber-highest-deficit-tail-compression.md)，
再把各因子的严格商/顶层缺口分别记录；不能把不同 primary 的饱和尾跨因子相加。
