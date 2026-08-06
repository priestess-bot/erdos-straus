---
kind: claim
claim_id: type-II-anchor-rank-fourier-dispatch
title: Type II 锚点外置—关系初等秩的 Fourier dispatch
statement: 对固定稳定子商中的规范源相对支撑 R 和目标锚点 alpha，若 alpha 不属于源差分群 Delta=<R>，则存在在 Delta 上平凡而在 alpha 上非平凡的纯锚点分离角色；若 alpha 属于 Delta，则任何分离 alpha 与单位元的有限角色都在某个 ell-primary 方向上非恒相位，并强制 Delta/ell Delta 至少有一个初等方向。因而零投影能量分支可严格分派为锚点环境商证书、SOURCE_RANK_INCONSISTENT 或真实 ell-rank/q-height 需求，不能把锚点幅度重复收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-anchor-separating-character-certificate
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-hall-bundle-target-residue-fourier-gate
  - type-II-source-fiber-elementary-rank-qheight-injection
topics:
  - type-II
  - anchor
  - rank
  - Fourier
  - dispatch
  - zero-energy
  - source-relation
  - capacity
  - proof-program
sources:
  - claim: type-II-source-fiber-anchor-separating-character-certificate
    role: ambient-anchor-separation
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: nonconstant-role-to-rank-demand
  - claim: type-II-hall-bundle-target-residue-fourier-gate
    role: zero-energy-input
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: rank-capacity-injection
visibility: public
last_checked: '2026-08-05'
---

# Type II 锚点外置—关系初等秩的 Fourier dispatch

## 1. 规范源相对支撑

在固定稳定子商 \(G\) 中，取一个源相对支撑
\[
R\subseteq G,\qquad 1\in R,
\]
并令
\[
\Delta=\langle R\rangle\le G.
\]
设规范化目标截面为
\[
S=\alpha R,\qquad \alpha\in G,
\]
且 \(1\notin S\)，即当前目标缺失。因为 \(1\in R\)，目标缺失保证
\(\alpha\ne1\)。

这里的 \(\Delta\) 是去重源相对点生成的差分群；稳定子已经被吸收，不能把被
稳定子吸收的重复列再次计入 \(\Delta\) 或容量。

## 2. 锚点外置分支

若
\[
\alpha\notin\Delta,
\]
则 \(\alpha\Delta\) 是 \(G/\Delta\) 中的非单位陪集。有限阿贝尔角色分离给出
\[
\exists\chi\in\widehat G:
\qquad
\chi|_\Delta=1,\qquad \chi(\alpha)\ne1.
\tag{1}
\]
于是对 \(r\in R\)，\(\chi(\alpha r)=\chi(\alpha)\)，并有
\[
\boxed{
\widehat{1_S}(\chi)
=\overline{\chi(\alpha)}\,|R|,
\qquad
|\widehat{1_S}(\chi)|=|R|.
}
\tag{2}
\]
这是纯锚点 Fourier 负证书：关系支撑 \(R\) 全部同相，不能把 \(|R|\) 的幅度误计为
\(|R|\) 个 q-height 需求。

角色 \(\chi\) 若还满足低模数商核平凡和源关系仿射相容性，则可降为低模数
F/G 证书；否则回执为 ANCHOR_SEPARATING_CHARACTER/LIFT_OBSTRUCTED，但角色
本身仍是环境商中的精确证书。

## 3. 锚点在差分群内的初等秩分支

若
\[
\alpha\in\Delta,
\]
取任意有限角色 \(\chi\in\widehat G\) 满足
\[
\chi(\alpha)\ne1.
\tag{3}
\]
因为 \(\alpha\in\Delta\)，\(\chi|_\Delta\) 不可能恒为 1。取
\(\ell\) 为 \(\chi(\alpha)\) 的阶的任一素因子，并令 \(\chi_\ell\) 为 \(\chi|_\Delta\)
的 \(\ell\)-primary 分量；取适当的 \(\ell\)-幂可得到一个在 \(\Delta\) 上非平凡的
\(\ell\)-阶角色 \(\psi\)。于是
\[
\boxed{
\dim_{\mathbb F_\ell}(\Delta/\ell\Delta)\ge1.
}
\tag{4}
\]
此外，由 \(\Delta=\langle R\rangle\)，若 \(\psi\) 在 \(R\) 上恒为 1，则它在
\(\Delta\) 上恒为 1，矛盾；所以 \(\psi\) 在源相对支撑上非恒相位。这是一个真实
\(\ell\)-初等关系方向，而不是纯锚点相位。

### 证明
有限阿贝尔群的 \(\ell\)-primary 分解把 \(\chi|_\Delta\) 写成各素数分量乘积。
\(\chi(\alpha)\ne1\) 保证至少一个 \(\ell\)-分量在 \(\alpha\) 上非平凡；对该分量
取适当幂得到阶 \(\ell\) 角色 \(\psi\)。非平凡的阶 \(\ell\) 角色等价于
\(\Delta/\ell\Delta\) 有非零对偶，故 (4) 成立。若 \(\psi\) 在生成集 \(R\) 上恒为
1，则按生成性在 \(\Delta\) 上恒为 1，矛盾。证毕。

## 4. 零投影能量的严格 dispatch

设前置残数门按
\(e=\gcd(M,\exp H)\) 投影后得到零非平凡能量，即
\[
m(y)=c+\mathbf 1_{y=\pi_e(\alpha)}
\]
的常数背景形式。该事实只说明当前源群允许的参数角色看不见目标洞，不能决定
锚点是否外置。先计算 \(\alpha\) 与 \(\Delta\) 的归属：

1. **ANCHOR_ENVIRONMENT**：\(\alpha\notin\Delta\)。用 (1)--(2) 构造环境商分离角色；
   若角色可降且相容，得到 F/G 证书；否则保留
   ANCHOR_SEPARATING_CHARACTER/LIFT_OBSTRUCTED；
2. **SOURCE_RANK_INCONSISTENT**：\(\alpha\in\Delta\)，但当前真实源列账本给出
   \(c_\ell(\Delta)=0\)；由 (4) 不可能存在声称的分离角色，任何外部频率都不能
   计入 q-height；
3. **SOURCE_RANK_DEMAND(\ell,1)**：\(\alpha\in\Delta\) 且
   \(c_\ell(\Delta)\ge1\)。分离角色至少支付一个真实 \(\ell\)-初等方向，随后才
   允许进入 Hall q 进容量或多-primary 数字终端。

因此零能量不是第四种“无信息”状态：它先被锚点外置测试，再被 source-rank
二分，避免纯锚点 Fourier 和真实关系需求重复收费。

## 5. 边界样例

### \(p=97\) 的环境锚点

取 \(G=U(24)\)、源相对支撑 \(R=\{1\}\)、目标锚点
\(\alpha=13\)。则 \(\Delta=1\)、\(\alpha\notin\Delta\)。角色
\(\chi(5)=1,\chi(13)=\chi(17)=-1\) 满足 (1)，并给出幅度 1 的纯锚点证书；
当前源群没有关系方向，不能把它收费为 q-height。

### \(C_5\) 的关系方向

取 \(G=\Delta=C_5=\langle g\rangle\)、\(R=\{1,g\}\)、\(\alpha=g^2\)。
则 \(1\notin\alpha R=\{g^2,g^3\}\)，且 \(\alpha\in\Delta\)。任意
\(\chi(g)=e^{2\pi i/5}\) 都在 \(\alpha\) 上非平凡，并在 \(R\) 上非恒相位；
(4) 给出一个 \(\ell=5\) 初等方向需求。

## 研究边界

该 dispatch 把零投影能量从模糊的 LIFT_OBSTRUCTED 回执分成环境锚点证书、
源秩矛盾或真实初等容量需求，并严格排除纯锚点的重复收费。它仍未证明
SOURCE_RANK_DEMAND 的一个初等方向必有足够 q 进资源；下一步应把它接入 Hall
最小割和多-primary 数字终端，或在资源不足时构造保持标签的严格递降。
