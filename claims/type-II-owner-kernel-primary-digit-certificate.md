---
kind: claim
claim_id: type-II-owner-kernel-primary-digit-certificate
title: Type II owner 核截面到 primary 数字终端的物理去重证书
statement: 在 owner 饱和分支中，若目标核 Fourier 角色通过源关系格仿射相容性，且 owner token 已通过请求—token—物理槽流门，则每条流边只能产生一个按物理槽计数的独立二点关系块。把这些块投影到循环 C_{ell^a} 并按精确 ell 进层计数：所有层达到 ell-1 个块时，动态选择掩码给出目标 Type II 短证书；最高不足层低于顶层时，饱和高尾给出严格较小 primary 商；最高不足层为顶层时，给出可审计的广义 2^j/primary 数字缺口。owner 标签重复、流失败或仿射不相容均在数字终端之前输出各自障碍，不能增加容量。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-saturation-quotient-kernel-dispatch
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-kernel-fourier-energy-role-capacity-dispatch
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-source-fiber-highest-deficit-tail-compression
topics:
  - type-II
  - owner-weight
  - kernel-fourier
  - primary
  - generalized-dyadic
  - digit-terminal
  - physical-capacity
  - constructive-certificate
  - quotient-descent
  - proof-program
sources:
  - claim: type-II-owner-saturation-quotient-kernel-dispatch
    role: saturated-owner-to-kernel-entry
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-slot-flow-and-collision-gate
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-relation-lift
  - claim: type-II-kernel-fourier-energy-role-capacity-dispatch
    role: compatible-primary-role-selection
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: fixed-fiber-column-deduplication
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: primary-layer-cover
  - claim: type-II-source-fiber-highest-deficit-tail-compression
    role: highest-deficit-quotient-relay
  - reproduction: reproductions/type_ii_owner_kernel_primary_digit_certificate.py
    role: owner-flow-gated-constructive-primary-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 核截面到 primary 数字终端的物理去重证书

## 1. 输入合同

固定一个已经通过目标纤维和饱和 owner 分派的缺失目标。前一层的
SATURATED_OWNER_KERNEL_SPLIT 给出一个有限核 \(K\)、目标截面 \(S_t\) 以及至少
一个非平凡 Fourier 角色。只保留同时满足以下两个条件的角色/请求：

1. 角色的相对相位与源关系格、目标锚点满足仿射相容性；失败时直接输出
   KERNEL_FOURIER_LIFT_OBSTRUCTED；
2. 相容角色产生的 owner 请求通过请求—token—物理槽流。若一个物理槽 \(c\) 的
   预算是 \(b(c)\)，流证书 \(M\) 满足
   \[
   \#\{(r,\tau)\in M:\pi_{\rm phys}(\tau)=c\}\le b(c).
   \tag{1}
   \]

失败时输出 OWNER_PROJECTION_CAPACITY_DEFICIT 或
OWNER_TOKEN_ASSIGNMENT_OBSTRUCTED。流边而不是 owner 标签是后续数字块的索引。
若两个 owner 标签投影到同一个物理槽，且没有额外的重复预算，它们至多贡献一条
流边；owner multiplicity 不能把一条物理边复制成多个二点块。

## 2. 相容流边到 primary 二点块

设流边 \((r,\tau)\in M\) 的源关系像在一个循环 primary 商中为
\[
v_\tau\in H_{\ell,a}=C_{\ell^a},\qquad v_\tau\ne0,
\tag{2}
\]
并且二点选择 \(\{0,v_\tau\}\) 保持同一个整数参数纤维、来源标签和目标相位。
这是 source contract 的独立选择条件：任意对这些二点块的 \(0/1\) 选择，都有
相应的合法源关系组合。定义精确层
\[
\nu_\ell(v_\tau)
=\max\{0\le k<a:v_\tau\in\ell^kH_{\ell,a}\},
\qquad
c_k(M)=\#\{(r,\tau)\in M:\nu_\ell(v_\tau)=k\}.
\tag{3}
\]
这里的 \(c_k(M)\) 统计通过物理流的边，允许两个不同物理槽偶然给出同一个
primary 残数，但不允许同一物理槽的 owner 标签重复计数。若某个源关系列已经
被稳定子吸收，\(v_\tau=0\)，它不进入 (3)。

相容流边的二点块和集为
\[
\Sigma_M=\sum_{(r,\tau)\in M}\{0,v_\tau\}
=\left\{\sum_{(r,\tau)\in M}\varepsilon_{r,\tau}v_\tau:
\varepsilon_{r,\tau}\in\{0,1\}\right\}.
\tag{4}
\]
目标核截面经过源关系锚点平移后给出 \(\alpha\in H_{\ell,a}\)。若
\(\alpha\notin H_{\ell,a}\)，立即输出 ANCHOR_OUTSIDE_PRIMARY；下文假设
\(\alpha\in H_{\ell,a}\)。

## 3. 构造性三分

### 全层覆盖：短证书

若
\[
c_k(M)\ge\ell-1\qquad(0\le k<a),
\tag{5}
\]
则循环 primary 进位层覆盖定理给出
\[
\Sigma_M=H_{\ell,a}.
\tag{6}
\]
因此存在 \(\varepsilon\) 使
\(\sum\varepsilon_{r,\tau}v_\tau=\alpha\)。该选择不是只存在性标签：按如下有限
动态递推保存一个选择掩码：
\[
\mathcal R_0=\{(0,\varnothing)\},\qquad
\mathcal R_{i+1}
=\mathcal R_i\cup
\{(x+v_i,\ E\cup\{i\}):(x,E)\in\mathcal R_i\},
\tag{7}
\]
其中第一坐标在 \(C_{\ell^a}\) 中取模，并对每个 residue 保留字典序最小的
掩码。由 (6)，\(\alpha\) 在最终表中出现；保存的掩码与流边、来源标签、q-height
和整数回译一起组成
\[
\mathrm{OWNER\_PRIMARY\_TYPE\_II\_SHORT\_CERTIFICATE}.
\tag{8}
\]
只有 source contract 已保证二点块的整数回译时，(8) 才是原始 Type II 证书；
否则保留为 PRIMARY_MASK_LIFT_OBSTRUCTED，不把群中掩码冒充为整数解。

### 最高不足层：严格 primary 商

若 (5) 失败，取规范最高不足层
\[
k^*=\max\{k:c_k(M)\le\ell-2\}.
\tag{9}
\]
由最高性的定义，所有 \(r>k^*\) 都满足 \(c_r(M)\ge\ell-1\)。令
\[
H_{>k^*}=\ell^{k^*+1}H_{\ell,a},
\qquad
\pi_{k^*}:H_{\ell,a}\to
H_{\ell,a}/H_{>k^*}\simeq C_{\ell^{k^*+1}}.
\tag{10}
\]
高层二点块的和集完整覆盖 \(H_{>k^*}\)。因此
\[
\Sigma_M
=\Sigma_{\le k^*}+H_{>k^*}
=\pi_{k^*}^{-1}
\bigl(\pi_{k^*}(\Sigma_{\le k^*})\bigr).
\tag{11}
\]
若原目标在 \(\Sigma_M\) 中缺失，则必有
\[
\pi_{k^*}(\alpha)
\notin\pi_{k^*}(\Sigma_{\le k^*}).
\tag{12}
\]
当 \(k^*<a-1\) 时，(12) 是严格较小的
HIGHEST_PRIMARY_DEFICIT_QUOTIENT 证书；证书包含 \(k^*\)、被完整吸收的高层
流边、商目标和低层块像。高层 owner 标签不再向商容量收费。

### 顶层不足：广义 \(2^j\)/primary 终端

当 \(k^*=a-1\) 时，(10) 没有非平凡尾，输出
\[
\mathrm{TOP\_PRIMARY\_DIGIT\_DEFICIT}
=(\ell,a,c_{a-1},\text{top-layer flow edges}).
\tag{13}
\]
若 \(\ell=2\)，这正是广义 \(2^a\) 终端的顶层数字缺口；若所有层满足 (5)，
则同一分支给出 \(2^a\) 的构造性短证书。不得把顶层不足改写成同阶商递降。

## 4. 证明

条件 (1) 说明每条后继选择都由真实物理槽支付；重复 owner 标签没有增加
\(\mathcal T\) 的可用边。仿射相容性保证 \(v_\tau\) 和锚点 \(\alpha\) 在同一真实
源关系商中定义，独立选择条件保证 (4) 的每个掩码都可回译。

若 (5) 成立，循环 \(\ell\)-primary 进位层终端逐层覆盖
\(C_{\ell^a}\)，得到 (6)。递推 (7) 只是把有限和集证明改写成可返回一个实际
掩码的动态程序，所以 \(\alpha\) 的出现给出 (8)。

若 (5) 失败，(9) 的最高性使 \(r>k^*\) 的层全部饱和。把这些块缩放
\(\ell^{k^*+1}\) 后应用同一个进位层终端，得到
\(\Sigma_{>k^*}=H_{>k^*}\)，即 (11)。若 \(\alpha\) 的原像不在 (11) 中，
其商像必不在低层商和集中，得到 (12)。指数从 \(a\) 降至 \(k^*+1\) 时严格下降；
若没有尾，(13) 是不可再压缩的顶层见证。证毕。

## 5. 与 owner 饱和选择器的严格接线

该引理的调用顺序固定为
\[
\begin{aligned}
&\text{直接 owner 命中}
\ \longrightarrow\ \text{Type II 短证书},\\
&\text{owner q 块未饱和}
\ \longrightarrow\ \text{物理流/source-column 扩张},\\
&\text{owner q 块饱和}
\ \longrightarrow\ \text{核 Fourier 相容性}
\ \longrightarrow\ \text{物理流}\\
&\hspace{38mm}\longrightarrow\
\begin{cases}
\text{全层掩码短证书},\\
\text{严格 primary 商},\\
\text{顶层 }2^j\text{ 缺口}.
\end{cases}
\end{aligned}
\tag{14}
\]
所以 owner multiplicity、未提升 Fourier 能量和抽象核角色都不会绕过物理槽门；
同一状态只会产生一条最先适用的证书类型。

## 6. 研究边界

本引理闭合了“饱和 owner 核截面如何进入广义 \(2^j\) 数字终端”的构造性接口，
并给出了可返回掩码的有限证书。它仍不证明每个核心素数都能通过仿射相容性、物理
流和独立选择合同；这些门失败时的精确回执分别是
KERNEL_FOURIER_LIFT_OBSTRUCTED、OWNER_PROJECTION_CAPACITY_DEFICIT 和
PRIMARY_MASK_LIFT_OBSTRUCTED。对商递降分支还必须继续检查保持来源标签的
E1--E5 算术回译；因此本引理新增的是严格的 finite selector/证书，而不是把
抽象 primary 商自动宣称为 Erdős--Straus 递归边。
