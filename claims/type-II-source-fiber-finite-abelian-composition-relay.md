---
kind: claim
claim_id: type-II-source-fiber-finite-abelian-composition-relay
title: Type II 源纤维有限阿贝尔合成列商缺失—素数核 Fourier 回执
statement: 对固定源纤维的任意有限阿贝尔目标差分商，沿一条素数阶合成列追踪目标与源和集的投影。任意目标缺失要么发生在严格较小的合成商中，要么在顶层素数核中形成非空真截面并产生精确的非平凡 Fourier 角色；该角色是内禀源角色，只有外部参数再解释时才需要额外的 SNF 提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - source-fiber
  - finite-abelian-groups
  - composition-series
  - quotient
  - kernel-fourier
  - descent
  - generalized-dyadic
  - source-switch
sources:
  - claim: type-II-source-fiber-multiprimary-digit-terminal
    role: multiprimary-source-terminal
  - claim: type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
    role: cyclic-composition-special-case
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: finite-kernel-fourier-energy
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: external-parameter-lift-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维有限阿贝尔合成列商缺失—素数核 Fourier 回执

## 1. 合成列设置

令 \(H\) 是固定参数纤维的有限阿贝尔目标差分商，令
\(S\subseteq H\) 为保持该纤维且可以由合法二点源块得到的和集，目标锚点记为
\(t\in H\)，并假设

\[
t\notin S.
\tag{1}
\]

取一条有限阿贝尔合成列

\[
0=H_0\leftarrow H_1\leftarrow\cdots
\leftarrow H_L=H,
\tag{2}
\]

其中每个满射
\(\pi_j:H_j\to H_{j-1}\) 的核

\[
K_j=\ker\pi_j\simeq C_{\ell_j}
\tag{3}
\]

具有素数阶 \(\ell_j\)。令
\(\rho_j:H\to H_j\) 为复合投影，并定义

\[
S_j=\rho_j(S),\qquad t_j=\rho_j(t).
\tag{4}
\]

合成列可以由 \(H\) 的 invariant-factor/Smith 分解递归构造；不同列只改变回执的
坐标，不改变下面的二分完备性。

## 2. 第一个商缺失

定义

\[
j_*=\min\{1\le j\le L:t_j\notin S_j\}.
\tag{5}
\]

集合非空，因为 \(t_L=t\notin S=S_L\)；而 \(S_0=H_0\) 中的投影只有零元，
所以该定义总有意义。

若 \(j_*<L\)，则

\[
\boxed{t_{j_*}\notin S_{j_*}}
\tag{6}
\]

是一个严格较小的有限阿贝尔商中的目标缺失。它可递归交给同一选择器；若该商有
真实 source-switch 参数，则形成较小状态候选，若参数纤维为空则记录
\(\mathrm{ARITHMETIC\_LIFT\_EMPTY}\) 或
\(\mathrm{SOURCE\_RELATION\_LIFT\_OBSTRUCTED}\)，不能把抽象商缺失直接称为递降。

## 3. 顶层素数核 Fourier 分支

若 \(j_*=L\)，则 \(t_{L-1}\in S_{L-1}\)。定义顶层核截面

\[
F_t=\{k\in K_L:t+k\in S\},
\qquad
K_L=\ker(H\to H_{L-1})\simeq C_{\ell_L}.
\tag{7}
\]

由 \(t_{L-1}\in S_{L-1}\) 有 \(F_t\ne\varnothing\)。若
\(F_t=K_L\)，则 \(0\in F_t\)，从而 \(t\in S\)，与 (1) 矛盾。因此

\[
\boxed{\varnothing\ne F_t\subsetneq K_L.}
\tag{8}
\]

在 \(K_L\) 上应用有限循环群 Parseval：

\[
\sum_{\substack{\psi\in\widehat K_L\\\psi\ne1}}
\left|\sum_{k\in F_t}\overline{\psi(k)}\right|^2
=|F_t|(\ell_L-|F_t|)>0.
\tag{9}
\]

于是存在一个非平凡顶层角色 \(\psi\) 及其精确 Fourier 负证书。有限阿贝尔群上的
角色可从 \(K_L\) 延拓到 \(H\)，得到 \(\chi\in\widehat H\)。因为这里的 \(S\) 是
真实源块的和集，\(\chi\) 本身已经满足真实源关系格恒等式；只有把它重新解释成
\(\mathbb Z/h\mathbb Z\) 的外部参数频率时，才需要再次通过 SNF/仿射相容性门。

## 4. 二分完备性与迭代

由 (5) 的定义，任意目标缺失严格满足下列互斥分派：

\[
\boxed{
\begin{array}{ll}
j_*<L:&\text{严格较小合成商缺失};\\[2mm]
j_*=L:&\text{顶层 }C_{\ell_L}\text{ 非空真截面 Fourier 证书}.
\end{array}}
\tag{10}
\]

在第一项中继续沿 \(H_{j_*}\) 的合成列递归，得到一条有限商缺失链，直到遇到
可提升的算术状态或顶层核角色。由于 \(|H_j|<|H|\)，商阶是严格下降势；但它只有
在整数参数纤维非空且保持来源标签时才是原猜想意义下的递降。

在第二项中，若顶层角色对源块的相位是非恒的，则它给出一个源关系对偶证书；若
对所有关系恒相位，则它只检测顶层锚点，记为纯锚点 Fourier，不收费 q-height。
这一区分与 pair-energy/rank ledger 兼容，避免把内禀角色自动误报成容量超载。

## 5. 两个边界

### \(C_4\) 循环例

取 \(S=\{0,1,2\}\subset C_4\)、目标 \(t=3\)，合成列
\(0\leftarrow C_2\leftarrow C_4\)。模 \(2\) 投影命中，故 \(j_*=2\)；
顶层核为 \(C_2=\{0,2\}\)，截面 \(F_t=\{2\}\)，非平凡二值角色给出系数 \(-1\)。

### \(C_2\oplus C_3\) 的相关缺失

取 \(H=C_2\oplus C_3\)，
\[
S=\{(0,0),(1,1),(0,1)\},\qquad t=(1,2).
\]

投影到 \(C_2\) 和 \(C_3\) 各自都可能命中某些坐标，但沿合成列逐级检查时，第一
个未命中层给出一个严格较小商缺失；若先选 \(C_3\) 作为顶层，则其核截面是
\(C_3\) 中的非空真子集并产生三值 Fourier 证书。这个例子说明不能只检查各 primary
投影分别命中就声称直和目标命中，必须沿合成列保留相关性。

## 6. 与多 primary 数字终端和算术门的接线

若所有合成列层都由多 primary 数字终端的合法二点块覆盖，则 (10) 的两项都被
排除，目标必须命中；因此缺失回执必然包含一个
\(\mathrm{MULTIPRIMARY\_DIGIT\_DEFICIT}\) 或顶层 Fourier 角色。对第一项的严格
商递降，仍须执行现有的 source-switch 参数合同、SNF 标签提升和 \(B'>A\) 大小门；
对第二项的外部参数解释，同样必须执行循环/有限阿贝尔 SNF。

## 研究边界

本引理把循环数字缺口推广到任意有限阿贝尔差分商，给出严格较小商或素数核 Fourier
的完备状态级回执。它仍不证明每条商缺失链都有非空算术 source-switch，也不把顶层
角色自动升级为 Type I/II 短证书。全局闭合仍要求：商缺失链的真实参数提升/严格势
下降，或顶层角色与 q-height/容量账本之间的可验证注入。
