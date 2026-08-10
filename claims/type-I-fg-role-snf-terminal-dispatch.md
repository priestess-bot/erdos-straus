---
kind: claim
claim_id: type-I-fg-role-snf-terminal-dispatch
title: F/G 角色请求的 source-label SNF 四分终端
statement: 对固定层约化后的 F 型 q-primary 源秩请求，若给定的源列与目标锚点标签表已经由完整 source-map 封闭，则源标签—目标标签的有限阿贝尔 SNF 恰有四种互斥回执：纯源关系障碍、源目标角色已提升、锚点外置的严格商分离或源内目标相位错配。源目标角色已提升才允许进入 Type II 的 q-prefix/稳定子闭包；锚点外置在非平凡源子群时给出严格群阶下降，在源子群平凡时只是 ANCHOR_ONLY；源内错配给出 SOURCE_RELATION_LIFT_OBSTRUCTED。若 source-map 未证明完备，则只能输出 F_SOURCE_MAP_UNCLOSED，不能把 Fourier 角色阶当作 q-height。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-fg-marked-source-menu-saturation
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
  - type-II-single-q-source-fiber-closure-trichotomy
topics:
- type-I
- F-state
- G-state
- Fourier
- SNF
- source-map
- anchor
- quotient-descent
- Type-II
- q-primary
- proof-program
sources:
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: role-to-source-demand
  - claim: type-I-fg-marked-source-menu-saturation
    role: finite-menu-saturation-and-phase-realization
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-lift
  - claim: type-II-source-label-snf-failure-anchor-relation-dichotomy
    role: four-way-snf-dichotomy
  - claim: type-II-single-q-source-fiber-closure-trichotomy
    role: lifted-q-dispatch
visibility: public
last_checked: '2026-08-10'
---

# F/G 角色请求的 source-label SNF 四分终端

## 1. 输入：一个已经产生的 F 型 q 请求

固定稳定子约化后的有限阿贝尔源群 \(H\)，源列为

\[
u_1,\ldots,u_r\in H,
\qquad L=\langle u_1,\ldots,u_r\rangle.
\tag{1}
\]

目标纤维的规范锚点记为 \(t\in H\)。F/G 角色—源秩桥先给出一个 q-primary
角色 \(\chi_q\)；只有在

\[
\chi_q|_{\Delta_Q}\not\equiv1
\tag{2}
\]

时才进入本卡。设 \(e=q^a\) 是所选标签根群的阶，给定一个有限标签表

\[
(u_i,\lambda_i)\quad(1\le i\le r),
\qquad (t,\lambda_0),
\qquad \lambda_i,\lambda_0\in\mathbb Z/e\mathbb Z.
\tag{3}
\]

标签表的含义是：若一个真实源角色 \(\chi\) 承担当前 Fourier 请求，则必须满足

\[
\chi(u_i)=\zeta_e^{\lambda_i},
\qquad
\chi(t)=\zeta_e^{\lambda_0}.
\tag{4}
\]

这一步不是由角色阶自动得到的；它必须来自一个已声明完备的整数 source-map，或
明确标为未闭合。若该 source-map 已被缩成有限同纤维 table，则在进入本卡前还必须
验证候选菜单的带标记子群等于完整 table 的带标记子群。失败时输出
\(\mathrm{MARKED\_SOURCE\_MENU\_ESCAPE}\)，而不能把部分菜单直接送入 (5) 的
SNF 四分。通过后，再用联合目标表的无竖直元检查相位是否可由复角色实现；若本卡要求
一个新 \(q\)-primary 角色，还须额外通过 fixed-order SNF 门。精确判据见
[有限带标记 source 菜单的饱和与相位实现](type-I-fg-marked-source-menu-saturation.md)。
G 型外部支撑分离角色满足源群上恒等，直接在本卡之前输出
\(\mathrm{G\_SUPPORT\_SEPARATION}\)，不进入 (3)。

## 2. 四个可判定状态

先删去目标行，只对源列运行有限阿贝尔 SNF；再将目标行加入。记对应解集为

\[
\mathcal X_{\rm src}
=\{\chi\in\widehat H:\chi(u_i)=\zeta_e^{\lambda_i}\},
\qquad
\mathcal X_{\rm all}
=\{\chi\in\mathcal X_{\rm src}:\chi(t)=\zeta_e^{\lambda_0}\}.
\tag{5}
\]

在 source-map 已封闭时，SNF/source-label 四分为

\[
\boxed{
\begin{array}{ll}
\mathcal X_{\rm src}=\varnothing
&\Longrightarrow \mathrm{F\_SOURCE\_LABEL\_OBSTRUCTED};\\
\mathcal X_{\rm all}\ne\varnothing
&\Longrightarrow \mathrm{F\_FOURIER\_SOURCE\_TARGET\_LIFTED};\\
\mathcal X_{\rm src}\ne\varnothing,\ \mathcal X_{\rm all}=\varnothing,\ t\notin L
&\Longrightarrow \mathrm{F\_ANCHOR\_QUOTIENT\_SEPARATION};\\
\mathcal X_{\rm src}\ne\varnothing,\ \mathcal X_{\rm all}=\varnothing,\ t\in L
&\Longrightarrow \mathrm{F\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}.
\end{array}}
\tag{6}
\]

若 source-map 的候选标签表不是有限且完备的，(6) 不得执行；唯一合法回执是
\[
\mathrm{F\_SOURCE\_MAP\_UNCLOSED}.
\tag{7}
\]

## 3. 与 q 请求和下降的精确接口

### 3.1 源标签障碍

在第一行中，SNF 失败行给出一个整数关系向量 \(w\)，满足

\[
\sum_i w_i u_i=0\quad\text{in }H,
\qquad
\sum_i w_i\lambda_i\not\equiv0\pmod e.
\tag{8}
\]

它是纯源 Fourier/LIFT 障碍；目标锚点没有参与，不能登记为
\(\mathrm{SOURCE\_RANK\_DEMAND}\)，也不能从角色阶中扣除 q-height。若其它已知
Type I/F/G 菜单承接该关系，保存关系载荷后转入相应出口；否则保留
\(\mathrm{F\_SOURCE\_LABEL\_OBSTRUCTED}\) 作为明确的 arithmetic no-lift。

### 3.2 源目标均可提升

在第二行中，SNF 给出一个真实角色 \(\chi_0\)。对于 (2) 的非恒 q-primary
分支，源差分群

\[
\Delta_Q=\left\langle\phi(z)\phi(z')^{-1}:z,z'\in Q\right\rangle
\tag{9}
\]

已有非零 q 初等商秩

\[
r_q(Q)=\dim_{\mathbb F_q}(\Delta_Q/q\Delta_Q)\ge1.
\tag{10}
\]

因此只能把
\(\mathrm{F\_FOURIER\_SOURCE\_TARGET\_LIFTED}\) 记为一个已通过 source-map 的
\(\mathrm{SOURCE\_RANK\_DEMAND}(q,r_q)\)，然后把其真实整数标签送入
[单 q 来源纤维闭包](type-II-single-q-source-fiber-closure-trichotomy.md)。本行仍不
把 \(a\) 自动改写成 q-height；q-height 必须由标签区间、CRT 和前缀匹配实际支付。

若同一 finite source universe 已经证明 exact 并保存每条 edge 的 \(H\)-坐标，则本行
还规范产出角色--edge 求值：把 fixed-order SNF 角色提升到
\(\mu_{q^a}\) 的标签行模 \(q\)，在
\[
V_q=(L+qH)/qH
\]
上取 source-visible role space \(R\)，再商去 \(R^\perp\)。所得
\(K_R=V_q/R^\perp\simeq R^*\) 与 evaluation matrix 的列均与 SNF 自由变量无关，
可直接送入相关角色 generalized Rado；详见
[source-SNF 的规范初等角色求值商](type-I-fg-snf-canonical-role-evaluation-quotient.md)。

### 3.3 锚点外置

在第三行中，取任意 \(\chi_0\in\mathcal X_{\rm src}\)。所有源一致角色之比组成
\(L^\perp\simeq\widehat{H/L}\)。由于 \(t\notin L\)，存在
\(\psi\in L^\perp\) 使 \(\psi(t)\ne1\)，而 \(\psi\) 在每个源列上恒等。于是

\[
\mathrm{F\_ANCHOR\_QUOTIENT\_SEPARATION}
\tag{11}
\]

是一个真实支撑外分离角色，而不是源 q 容量请求。若
\(1<|L|<|H|\)，投影到 \(H/L\) 给出严格群阶下降；若 \(L=1\)，它只是
\(\mathrm{ANCHOR\_ONLY\_QPRIMARY}\)，没有严格下降。两种情况都不能重复收费
Type II q-height。

### 3.4 源内目标错配

在第四行中，写出 \(t=\sum_i c_i u_i\) 于 \(H\) 中。因为所有
\(\psi\in L^\perp\) 在 \(t\) 上恒等，目标失败只能是

\[
\lambda_0-\sum_i c_i\lambda_i\not\equiv0\pmod e.
\tag{12}
\]

所以 SNF 行给出带目标系数的
\(\mathrm{F\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}\)。该回执是精确关系相位矛盾，
不产生 q-height；应转入 alternate source-map、Type I/F/G 关系证书，或在外层
势函数中证明严格下降。

## 4. 定理证明

有限阿贝尔源商 SNF 给出 (5) 的两个解集是否为空，并且在非空时显式构造角色。
若源解集为空，第一失败行立即给出 (8)。若源解集非空，固定
\(\chi_0\in\mathcal X_{\rm src}\)；任何其它源一致角色都唯一写成
\(\chi_0\psi\)，其中 \(\psi\in L^\perp\)。有限阿贝尔对偶性识别
\(L^\perp\simeq\widehat{H/L}\)。

若 \(t\notin L\)，商中的 \(\bar t\) 非单位，必有一个 \(\psi\) 在其上非平凡，
得到 (11)；当 \(L\) 非平凡且非全群时商阶严格变小。若 \(t\in L\)，所有
\(\psi\in L^\perp\) 在 \(t\) 上恒等，目标行失败等价于 (12)。若目标行成功，
得到第二行角色提升。四行互斥且穷尽，(9)--(10) 则由 F/G 角色—源秩桥给出。
证毕。

## 5. 最小边界例子

### 三值真实源方向

取 \(H=C_3=\langle g\rangle\)，源列 \(u_1=g\)，目标 \(t=g\)，标签群
\(\mu_3\)。若 \(\lambda_1=\lambda_0=1\)，则
\(\mathcal X_{\rm all}\ne\varnothing\)，产生一个真实的三值 source lift；若
\(\lambda_0=0\)，则 \(t\in L\) 且产生
\(\mathrm{F\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}\)。

### 锚点外置

取 \(H=C_2\oplus C_3\)、\(L=\langle(1,0)\rangle\)、\(t=(0,1)\)。源标签可由
\(L^\perp\) 内角色实现，而目标标签若不在其三值像中，则分离角色来自
\(H/L\simeq C_3\)，得到严格商；这里分离不是一个额外的 Type II q 列。

### source-map 未闭合

若同一个抽象 \(H=C_3\) 与角色 \(\chi(g)=\exp(2\pi i/3)\) 同时允许候选标签
\(\{0\}\) 和未枚举的标签 \(\{1\}\)，则有限表并不完备。此时不能输出
\(\mathrm{F\_SOURCE\_LABEL\_OBSTRUCTED}\)；必须保留 (7)，直到 source-map 完备性
被证明。

## 6. 研究边界

本卡把“F/G 角色已经出现但还没有整数载体”的宽泛状态压缩为四个可复核终端，
并明确了严格商下降、纯锚点、源关系错配和真实 q 请求的边界。对于已经声明
Type I/II 整数 source contract 的状态，先使用
[Type I/II F-G 源映射的有限整数宇宙完备化](type-I-II-fg-universal-finite-source-map-completion.md)
把 `F_SOURCE_MAP_UNCLOSED` 精化为最小漏项或带标记 SNF 回执；本卡仍未证明实际
Erdős--Straus 源映射对所有核心素数、所有候选纤维都是完备的；也未证明
\(\mathrm{F\_FOURIER\_SOURCE\_TARGET\_LIFTED}\) 后必然通过 q-prefix/Kneser
闭包。对已经 exact、fixed-order lifted 且 edge provenance 完整的分支，角色到
column 的 typed transport 现由规范求值商自动给出；不再是额外假设。因此全局决定性
缺口变为：证明实际 source-map 完备，或对
\(\mathrm{F\_SOURCE\_MAP\_UNCLOSED}\) / 关系错配建立独立 Type I/F/G/下降承接。
