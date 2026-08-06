---
kind: claim
claim_id: type-II-composition-kernel-role-rank-capacity-bridge
title: Type II 合成列顶层核角色的锚点—初等秩容量二分
statement: 在有限阿贝尔源纤维的顶层素数核 Fourier 分支中，若延拓角色在目标相对支撑上恒相位，则它只提供锚点证书且关系 q-height 需求为零；若角色非恒相位，则目标差分群含有一个对应的 ell 初等方向，任何保持纤维的真实源列账本必须支付至少一个独立 ell 容量单位。多个独立角色的需求不超过源关系列的初等商秩。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-kernel-fourier-pair-energy-qheight-demand
topics:
  - type-II
  - composition-series
  - kernel-fourier
  - anchor
  - elementary-rank
  - q-height
  - capacity
  - source-relation
  - proof-program
sources:
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: top-prime-kernel-fourier
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: source-column-rank-capacity
  - claim: type-II-kernel-fourier-pair-energy-qheight-demand
    role: nonconstant-phase-demand
visibility: public
last_checked: '2026-08-05'
---

# Type II 合成列顶层核角色的锚点—初等秩容量二分

## 1. 顶层核和源差分商

沿有限阿贝尔合成列 relay 的顶层分支，令

\[
H\longrightarrow \overline H=H/K,
\qquad
K\simeq C_\ell,
\tag{1}
\]

其中 \(K\) 是顶层素数核。设 \(Q\) 是固定参数纤维中目标相对支撑的去重源指数
集合，\(\phi(Q)\subseteq H\)，并定义

\[
\Delta_Q=\left\langle\phi(n-n'):\ n,n'\in Q\right\rangle\le H.
\tag{2}
\]

顶层 Fourier 回执给出 \(F_t\subsetneq K\) 的非平凡角色
\(\psi\in\widehat K\)，并将其延拓为 \(\chi\in\widehat H\)。把角色在源相对支撑
上的相位写成

\[
z_n=\chi(\phi(n)),\qquad n\in Q.
\tag{3}
\]

## 2. 锚点—关系二分

定义

\[
\mathrm{constant}(\chi,Q)
\iff z_n=z_{n'}\quad\text{对所有 }n,n'\in Q.
\tag{4}
\]

若 (4) 成立，则 \(\chi\) 在 \(\Delta_Q\) 上平凡，顶层 Fourier 系数只剩一个
锚点单位相位：

\[
\widehat{1_{S_t}}(\chi)
=\overline{\chi(\alpha)}\,|Q|.
\tag{5}
\]

因此关系边的成对能量为零，不应从 q-height 账本收费；该分支记录为
\(\mathrm{ANCHOR\_ONLY\_FOURIER}\)。

若 (4) 不成立，则存在 \(n,n'\) 使
\(\chi(\phi(n-n'))\ne1\)。取 \(\chi\) 在 \(H\) 的 \(\ell\)-primary 分量上的延拓，
并对其限制到 \(\Delta_Q\) 的非平凡像取适当的 \(\ell\)-幂次，可得到一个非平凡
\(\ell\)-阶角色。因此 \(\Delta_Q\) 含有一个非平凡 \(\ell\)-阶商，故

\[
\boxed{
\dim_{\mathbb F_\ell}
\bigl(\Delta_Q/\ell\Delta_Q\bigr)\ge1.
}
\tag{6}
\]

这一步只使用真实源支撑，不把外部参数 Fourier 当作乘法角色；若角色来自外部标签，
仍需先通过 SNF/仿射相容性。

## 3. 源列容量下界

令 \(A_{\ell,Q}\) 为当前参数纤维中保持目标商关系的真实源列在
\(\Delta_Q\) 所在 \(\ell\)-primary 商中的像，并令

\[
c_\ell(Q)
=\dim_{\mathbb F_\ell}
\bigl(A_{\ell,Q}/\ell A_{\ell,Q}\bigr).
\tag{7}
\]

由固定纤维源列注入 \(\Delta_Q\le A_{\ell,Q}\)，有

\[
\dim_{\mathbb F_\ell}
\bigl(\Delta_Q/\ell\Delta_Q\bigr)
\le c_\ell(Q).
\tag{8}
\]

结合 (6)，非恒相位分支满足

\[
\boxed{c_\ell(Q)\ge1.}
\tag{9}
\]

换言之，任何保持纤维的真实 q-height/源关系账本若给出
\(c_\ell(Q)=0\)，则顶层角色不可能在源支撑上非恒相位；若回执声称非恒相位，
必须输出 \(\mathrm{SOURCE\_RANK\_INCONSISTENT}\)，而不能继续计入容量。

更一般地，若 \(\chi_1,\ldots,\chi_r\) 的限制在
\(\operatorname{Hom}(\Delta_Q,\mu_\ell)\) 中线性独立，则

\[
\boxed{r\le c_\ell(Q).}
\tag{10}
\]

因此多个顶层角色只能按独立初等方向收费；pair-energy 的多条重复关系边不能被
误计为 \(r^2\) 个容量单位。

## 4. 与顶层 Fourier 回执的严格分派

对合成列 relay 的顶层截面，先选一个非平凡 \(\psi\)，再按 (4) 分派：

1. ANCHOR_ONLY_FOURIER：相位恒定，关系需求为零；保留锚点负证书；
2. SOURCE_RANK_DEMAND(ell,1)：相位非恒定，至少需要一个真实 \(\ell\) 初等源列；
3. 若 \(c_\ell(Q)=0\) 却检测到非恒相位，输出 SOURCE_RANK_INCONSISTENT；
4. 若 \(c_\ell(Q)\ge1\)，才允许继续比较 q-height 的实际层数、稳定子活跃容量和
   其它状态的重复使用上界。

这一步把顶层 Fourier 从“存在某个角色”推进为最小的有向容量需求；它不声称
\(c_\ell(Q)\ge1\) 已经足以填满目标。

## 5. 边界样例

### 纯锚点

若 \(Q\) 只有一个去重相对点，则所有 \(z_n\) 自动恒定，(5) 成立，即使顶层
截面 \(F_t\) 有非零 Fourier 系数，也不能收费 q-height。这包括 \(p=97\) 伪命中
中的单点目标纤维。

### 一条真实关系方向

在 \(H=C_\ell\) 中取 \(Q=\{0,1\}\)，令 \(\chi(1)=e^{2\pi i/\ell}\)。相位
\(\{1,e^{2\pi i/\ell}\}\) 非恒定，\(\Delta_Q=H\)，故
\(c_\ell(Q)\ge1\)。若源账本只有稳定子吸收列而没有非零 \(\ell\)-列，则该角色
不能由当前纤维产生，回执必须是 SOURCE_RANK_INCONSISTENT。

## 研究边界

本引理完成了“顶层素数核角色 \(\to\) 最小初等秩容量需求”的严格映射，并排除了
纯锚点 Fourier 的误收费。它仍不证明一个容量单位足以命中目标，也不解决不同
参数纤维之间的列复用；后续必须在 \(c_\ell(Q)\) 饱和或超载时使用 Kneser/数字
终端，或构造保持标签的严格递降。
