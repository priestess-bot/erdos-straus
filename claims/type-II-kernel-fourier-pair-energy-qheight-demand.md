---
kind: claim
claim_id: type-II-kernel-fourier-pair-energy-qheight-demand
title: Type II 核 Fourier 对偶能量到源关系边的 q 进需求
statement: 对目标伪命中陪集的去重源关系支撑 Q_t，任意核角色的 Fourier 系数满足精确的成对能量恒等式 2|Q_t|^2(1-rho^2)，其中 rho 是归一化系数模长。因此至少有 |Q_t|^2(1-rho^2)/2 个有序源关系对在该角色下具有非平凡相位差；若为这些关系边定义可验证的 q 进源成本，则得到相应的最小总需求。该需求只有在证明跨边复用上界后才能升级为全局容量矛盾；纯锚点或单点纤维的能量为零，是必须单独处理的边界。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-source-fiber-shared-q-ledger
  - type-II-source-fiber-qheight-kneser-bridge
topics:
- type-II
- kernel-fourier
- pair-energy
- source-relation-lattice
- q-height
- capacity
- edge-reuse
- target-fiber
- proof-program
sources:
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-Fourier-pullback
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-cost-accounting
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: distinct-q-layer-cost-accounting
visibility: public
last_checked: '2026-08-04'
---

# Type II 核 Fourier 对偶能量到源关系边的 q 进需求

## 去重源支撑与归一化系数

沿用核 Fourier—源关系格判据的设置。目标截面去重后写成

\[
S_t=\alpha\,\phi(Q_t),
\qquad
Q_t\subseteq L_\pi/L_G,
\]

其中 \(\phi\) 在 \(L_\pi/L_G\) 上是单射。令

\[
N=|Q_t|=|S_t|,
\qquad
z_{\bar n}=\chi(\phi(n))\in\mathbb C,\quad |z_{\bar n}|=1,
\]

并定义归一化核 Fourier 幅度

\[
\rho_\chi
 =\frac{|\widehat{1_{S_t}}(\chi)|}{N}
 =\frac{\left|\sum_{\bar n\in Q_t}\overline{z_{\bar n}}\right|}{N}
 \in[0,1].
\tag{1}
\]

锚点 \(\alpha\) 只贡献一个单位模相位，不影响 \(\rho_\chi\)。因此该量只测量源
关系支撑中的相对相位结构。

## 成对能量恒等式

定义有序关系边的相位能量

\[
\mathcal E_\chi(Q_t)
 =\sum_{\bar n,\bar n'\in Q_t}
 \left|1-z_{\bar n}\overline{z_{\bar n'}}\right|^2.
\tag{2}
\]

展开平方并使用
\(\sum_{\bar n,\bar n'}z_{\bar n}\overline{z_{\bar n'}}
=|\sum_{\bar n}z_{\bar n}|^2\)，得到精确恒等式

\[
\boxed{
\mathcal E_\chi(Q_t)
 =2N^2-2\left|\sum_{\bar n\in Q_t}z_{\bar n}\right|^2
 =2N^2(1-\rho_\chi^2).
}
\tag{3}
\]

令

\[
\mathcal D_\chi(Q_t)
 =\{(\bar n,\bar n')\in Q_t^2:
   \chi(\phi(n-n'))\ne1\}
\]

为非平凡相位差的有序关系边集合。每条边的平方距离不超过 \(4\)，所以由 (3)

\[
\boxed{
|\mathcal D_\chi(Q_t)|
 \ge \frac{N^2(1-\rho_\chi^2)}{2}.
}
\tag{4}
\]

式 (4) 是一个纯有限群事实，不依赖角色枚举或指数盒是否是直积。若
\(\rho_\chi=1\)，相对支撑上的角色相位全部相同；若 \(\rho_\chi<1\)，则至少有
一个真实源关系边被该角色分离。

## q 进源边成本

对一条关系边选取 \(n\in\mathbb Z^r\) 代表 \(\bar n-\bar n'\)，定义一个只依赖
来源账本的非负成本 \(\mathfrak c_q(n)\)。在互异来源 q 的逐层模型中可取

\[
\mathfrak c_q(n)=\sum_i |n_i|,
\]

并要求 \(|n_i|\) 不超过该纤维两端可用的 q-height；重复 q 时必须改用共同账本允许的
最小标记层数，不能按来源重复相加。对支撑中的非平凡边定义

\[
\mathfrak c_{\min}(\chi,Q_t)
 =\min_{(\bar n,\bar n')\in\mathcal D_\chi(Q_t)}
    \mathfrak c_q(n-n').
\tag{5}
\]

若 \(\mathcal D_\chi(Q_t)\ne\varnothing\)，则由 (4) 得到可验证的总边需求下界

\[
\boxed{
\sum_{(\bar n,\bar n')\in\mathcal D_\chi(Q_t)}
 \mathfrak c_q(n-n')
 \ge
 \frac{N^2(1-\rho_\chi^2)}{2}\,
 \mathfrak c_{\min}(\chi,Q_t).
}
\tag{6}
\]

式 (6) 不是把边成本自动称作全局容量；它只把 Fourier 缺陷转换成一个明确的
source-relation demand。若能另外证明每个真实 q 层至多服务 \(R_{\mathrm{reuse}}\) 条
这样的边，则立刻得到

\[
\text{所需 q 层数}
\ge
\frac{N^2(1-\rho_\chi^2)\,
      \mathfrak c_{\min}(\chi,Q_t)}
     {2R_{\mathrm{reuse}}}.
\tag{7}
\]

这正是后续容量证明必须补上的算术接口：证明 \(R_{\mathrm{reuse}}\) 的有限上界，或
证明某些边不能共享同一个 q 层。没有该上界，(6) 仍只是状态内对偶需求。

## 与核 Fourier 和 Kneser 缺口的连接

由 Parseval，未饱和目标截面总能量给出一个非平凡核角色。对规范选择的角色
\(\chi_*\)，先计算 \(\rho_{\chi_*}\)，再按 (4)--(6) 生成
PAIR_QHEIGHT_DEMAND 回执：

1. \(\rho_{\chi_*}=1\) 时，角色只看见锚点，关系边需求为零，不能伪称 q 进超载；
2. \(\rho_{\chi_*}<1\) 时，至少有 (4) 所示数量的非平凡源关系边；
3. 只有在 source-fiber 账本证明边复用受限时，(7) 才能与 Kneser 缺口相比较；
4. 若相容性判据失败，先记 LIFT_OBSTRUCTED，不得生成本回执。

因此“核 Fourier 有能量”与“q 进容量被耗尽”现在被严格分成两个步骤，避免把
角色幅度直接误读成算术矛盾。

## 两个边界

### 单点或纯锚点边界

\(p=97\)、\(G=U(24)\)、\(P=\{1,11\}\) 的目标截面为 \(S_t=\{13\}\)，所以
\(N=1\)、\(\rho_\chi=1\)，式 (3) 给出零关系能量。这里的非平凡核角色只检测
锚点 \(\alpha=13\)，不能从该证书收费一个 q 层；这解释了为什么 p=97 伪命中不会
自动转成容量矛盾。

### 两相位边界

若某个源关系支撑有两个点，角色相位为 \(\{1,-1\}\)，则 \(N=2\)、\(\rho_\chi=0\)，
式 (3) 给出 \(\mathcal E_\chi=8\)，式 (4) 给出至少两条有序非平凡边，且达到下界。
这是一条可直接用于验证边复用规则的最小非平凡 profile。

## 差分群的多角色秩修正

定义目标支撑的差分群

\[
\Delta_t=\left\langle \bar n-\bar n':
  \bar n,\bar n'\in Q_t\right\rangle
\le L_\pi/L_G.
\tag{8}
\]

对每个素数 \(\ell\)，令

\[
r_\ell(Q_t)
 =\dim_{\mathbb F_\ell}\bigl(\Delta_t/\ell\Delta_t\bigr).
\tag{9}
\]

有限阿贝尔群对偶性给出

\[
r_\ell(Q_t)
 =\dim_{\mathbb F_\ell}
   \operatorname{Hom}(\Delta_t,\mu_\ell).
\tag{10}
\]

因此 \(r_\ell(Q_t)\) 正好是由该目标支撑产生的独立 \(\ell\)-角色方向数；可以选取
\(r_\ell(Q_t)\) 个在 \(\Delta_t\) 上线性独立的角色，并延拓到 \(K\)。这组角色的
联合源关系矩阵在 \(\mathbb F_\ell\) 上秩为 \(r_\ell(Q_t)\)，不会把同一方向的
\(m^2\) 条 pair-energy 边重复当成 \(m^2\) 个独立需求。

于是容量路线有一个不依赖边复用的候选接口：若 source-fiber 账本证明每个可用
\(\ell\)-primary q 层至多提供一个独立差分方向，便有

\[
\#\{\text{可用 }\ell\text{-primary q 层}\}
 \ge r_\ell(Q_t).
\tag{11}
\]

式 (11) 仍需要具体的 q-height 到 \(\mathbb F_\ell\) 关系矩阵注入；它不是由群阶
自动推出的全局容量不等式。但它把“多角色”分支的目标从二次边数改成了可验证的
初等商秩。

### 成对能量的复用饱和反例

成对能量本身不能给出与独立源方向数成正比的下界。令

\[
H=C_2\times C_m,\qquad
\chi(\varepsilon,j)=(-1)^\varepsilon,\qquad
Q_t=H.
\]

则 \(N=2m\)，两种相位各出现 \(m\) 次，故

\[
\rho_\chi=0,\qquad
\mathcal E_\chi(Q_t)=2N^2,\qquad
|\mathcal D_\chi(Q_t)|=N^2/2.
\]

但是 \(\chi\) 的有效相位商只有
\(H/\ker\chi\simeq C_2\)，即只有一个二元源方向；其余 \(C_m\) 坐标全部被角色
看不见。于是若把每条非平凡边都当作一个独立 q 层，收费会随 \(m^2\) 增长，而真实
活跃角色秩仍为 \(1\)。具体地，\(H=U(15)\) 时可取
\(\chi(x)=1\)（\(x\equiv1\pmod3\)）和
\(\chi(x)=-1\)（\(x\equiv2\pmod3\)），\(Q_t=U(15)\) 就得到同样的饱和 profile。

因此 \(R_{\mathrm{reuse}}\) 不能预设为常数；容量证明必须满足下列至少一项：

* 证明 source-fiber 的同一个 q 层只能服务一个有界数量的独立相位商类；
* 同时使用多个独立角色，把需求从边数改成角色像/商群秩；
* 直接把 \(\ker\chi\) 的方向纳入稳定子商递降，而不是继续按边收费。

## 研究边界

本引理把相容核 Fourier 系数转成了精确的关系边数量和 q 进成本下界，但复用饱和反例
说明不能仅凭边数推出独立容量。后续的决定性子问题现在可以明确表述为：

\[
\boxed{
\text{证明 source-fiber 关系边的有限复用上界，或改用多角色/商群秩构造 Type II/递降。}
}
\]

在该子问题解决前，式 (7) 只能作为 analysis_evidence，不能升级为
verified_edge 或全称选择器定理。对于已经提取出有限相容回路族的状态，可以改用
[owner 相容回路族的 q 进需求—物理容量流桥](type-II-owner-circuit-qcapacity-flow-bridge.md)
直接计算实际复用最小割，不再假设一个全局常数 \(R_{\mathrm{reuse}}\)；若该流仍有
缺口，回执依然只表示 q 容量障碍，后继递降仍需单独验证。
