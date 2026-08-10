---
kind: claim
claim_id: type-I-primary-filter-active-source-saturation-zero-successor-capacity
title: primary filter 的活动源差分饱和与 source-preserving successor 零容量
statement: >-
  对有限阿贝尔群 H 中的盒映射 phi(z)=prod_i g_i^{z_i}，令
  B=prod_i[-nu_i,nu_i]、I_+={i:nu_i>0}。则盒差分格精确等于
  direct_sum_{i in I_+} Z e_i，盒像差分群精确等于
  D_B=<g_i:i in I_+>。因此规范 Type I 素因子盒中所有 nu_i>=1 时必有
  D_B=H，q-primary filtered Fourier deficit 的 support-annihilator 分支不可能
  出现。一般地，过滤角色若在 D_B 上平凡，只看见冻结或 fixed-layer 商；若在
  D_B 上非平凡，则其局部初等 q 角色要么严格失败于 ambient-extension cut，要么
  活动源列张成全部规范 role-evaluation quotient。后一情形对任意广义 Rado 固定割
  Q_U 都有候选列空间 T_omega^cand=Q_U；未通过 state realization 时只能输出候选
  饱和。若一个 independently realized exact successor 保留这些列，则其实际
  T_omega=Q_U，并恰满足 h_omega^*=delta+a_omega、e_omega=0。故 primary
  filtering 本身不能产生正容量 exact successor；必须另证真实算术 source
  contraction 及 E4/E5 lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-primary-filtered-support-source-dichotomy
  - type-I-fixed-layer-qprimary-representation-dual-capacity-selector
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-I-fg-exact-successor-source-overhead-rank-slack-selector
topics:
  - type-I
  - F-state
  - G-state
  - primary-filter
  - active-source
  - difference-lattice
  - source-saturation
  - ambient-extension
  - exact-successor
  - zero-capacity
  - strict-no-go
  - proof-program
sources:
  - claim: type-I-target-fiber-primary-filtered-support-source-dichotomy
    role: support-annihilator-versus-source-difference-input
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: ambient-extension-and-perfect-evaluation-quotient
  - claim: type-I-fg-exact-successor-source-overhead-rank-slack-selector
    role: exact-successor-rank-slack-capacity-identity
  - reproduction: reproductions/type_i_primary_filter_active_source_saturation_zero_successor_capacity.py
    role: active-lattice-frozen-extension-and-p73-saturation-controls
visibility: public
last_checked: '2026-08-10'
---

# primary filter 的活动源差分饱和与 source-preserving successor 零容量

## 1. 活动坐标完全决定盒差分群

令 \(H\) 为有限阿贝尔群，取 \(g_1,\ldots,g_r\in H\)，并定义

\[
\mathcal B_\nu
=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad
\phi(z)=\prod_i g_i^{z_i},
\qquad \nu_i\in\mathbb Z_{\ge0}.
\tag{1}
\]

记

\[
I_+=\{i:\nu_i\ge1\},\qquad
S=\phi(\mathcal B_\nu),
\tag{2}
\]

以及

\[
L_B=\langle z-z':z,z'\in\mathcal B_\nu\rangle\le\mathbb Z^r,
\qquad
D_B=\langle ss'^{-1}:s,s'\in S\rangle\le H.
\tag{3}
\]

本卡中的 **filter-only** 精确指过滤密度桥只选择角色子群 \(X\) 或角色
\(\chi\)，而保持 \(\mathcal B_\nu,\phi\)、全部真实 source provenance 及它们在
固定求值商中的规范 columns 不变。若另行删除盒点、单位差分、源记录，或把同一
记录重编码为不同 column，那已经是待证明的 arithmetic source
contraction/retyping，不属于 filter-only。

则有精确恒等式

\[
\boxed{
L_B=\bigoplus_{i\in I_+}\mathbb Z e_i,
\qquad
D_B=\phi(L_B)=\langle g_i:i\in I_+\rangle.
}
\tag{4}
\]

**证明。** 若 \(i\notin I_+\)，盒中每个点的第 \(i\) 坐标都是零，所以每个差
\(z-z'\) 的该坐标也为零。反之，若 \(i\in I_+\)，则
\(0,e_i\in\mathcal B_\nu\)，故 \(e_i=e_i-0\in L_B\)。这证明第一式。
第二式由 \(\phi\) 是群同态及 \(D_B\) 的定义立即得到。证毕。

式 (4) 还给出

\[
1\in S,\qquad S\subseteq D_B.
\tag{5}
\]

因此若角色 \(\chi\) 在 \(D_B\) 上平凡，则它在盒支撑上的常数不是任意
\(c\in\mathbb S^1\)，而精确为 \(c=1\)。

## 2. 规范 Type I 盒消灭 support-annihilator 分支

在规范 Type I 图表中

\[
K=\frac{pR+1}{4}=\prod_{i=1}^r q_i^{\nu_i},
\qquad \nu_i\ge1,
\qquad
H=\langle q_1,\ldots,q_r\rangle\le U(R).
\tag{6}
\]

将 \(g_i=q_i\bmod R\) 代入 (4)，得到

\[
\boxed{D_B=H.}
\tag{7}
\]

所以目标纤维 primary-filter Fourier deficit 所选的任一非平凡角色
\(\chi\in\widehat H\) 必满足

\[
\chi|_{D_B}\ne1.
\tag{8}
\]

现有 SUPPORT_ANNIHILATOR_SEPARATION 分支在规范全素因子盒中因而为空；它只能
在某些 \(\nu_i=0\) 的冻结坐标，或 ambient/fixed layer 含有未由活动
\(g_i\) 生成方向的扩张模型中出现。

更一般地，若 \(\chi|_{D_B}=1\)，则
\(\widehat B(\chi)=|\mathcal B_\nu|\)。若 \(\chi\) 同时来自严格 filtered
Fourier deficit，则

\[
-\operatorname{Re}\bigl(\overline{\chi(y)}\widehat B(\chi)\bigr)>0
\tag{9}
\]

强制 \(\operatorname{Re}\chi(y)<0\)，特别地 \(y\notin D_B\)。于是该支精确输出

\[
\mathrm{PRIMARY\_FILTER\_FROZEN\_QUOTIENT\_SEPARATION}
\quad\text{in }H/D_B,
\tag{10}
\]

而不是 source-rank 或 exact-successor 容量。对 fixed-layer 选择器，这正是
fixed-layer/anchor-only 方向；对 (6) 则由 (7) 根本不可能发生。

## 3. 非平凡源角色的 extension--saturation 二分

以下改用加法记号。设 \(\chi\) 是 \(q\)-primary 角色，且
\(\chi|_{D_B}\ne1\)。若其限制的精确阶为 \(q^k\)，固定
\(\zeta_q\leftrightarrow1\in\mathbb F_q\)，由

\[
(\chi|_{D_B})^{q^{k-1}}(d)=\zeta_q^{\ell_\chi(d)}
\tag{11}
\]

得到非零局部同态

\[
\ell_\chi:D_B\longrightarrow\mathbb F_q.
\tag{12}
\]

由 (4)，活动生成元生成 \(D_B\)，所以

\[
\operatorname{span}_{\mathbb F_q}
\{\ell_\chi(g_i):i\in I_+\}=\mathbb F_q.
\tag{13}
\]

但 (12) 未必是 ambient elementary role。规范 ambient-extension 门给出精确二分：

\[
\ell_\chi(D_B\cap qH)\ne0
\Longrightarrow
\mathrm{PRIMARY\_FILTER\_ELEMENTARY\_AMBIENT\_EXTENSION\_OBSTRUCTED};
\tag{14}
\]

\[
\ell_\chi(D_B\cap qH)=0
\Longleftrightarrow
\ell_\chi\text{ extends to some }\rho:H\to\mathbb F_q.
\tag{15}
\]

若 (15) 通过，令

\[
V_q=\frac{D_B+qH}{qH}.
\tag{16}
\]

所有活动 \(g_i\) 的像张成 \(V_q\)。对任意一组已经通过 extension 或
fixed-order SNF 的 source-visible elementary roles，令

\[
\mathcal R\le V_q^*,\qquad
N_{\mathcal R}=\mathcal R^\perp,\qquad
K_{\mathcal R}=V_q/N_{\mathcal R}\simeq\mathcal R^*.
\tag{17}
\]

每个活动源的规范 evaluation column 是

\[
\kappa(g_i)(\rho)=\rho(g_i).
\tag{18}
\]

因为 \(g_i\ (i\in I_+)\) 张成 \(V_q\)，商映射保持生成，故

\[
\boxed{
\operatorname{span}\{\kappa(g_i):i\in I_+\}=K_{\mathcal R}.
}
\tag{19}
\]

这不是“至少一个 q 请求”，而是 primary-filter 活动源在规范可见商中的精确
source domination。若 \(\mathcal R=0\)，则 \(K_{\mathcal R}=0\)，同样没有可收费的源角色容量。
在规范 Type I 情形 (6) 中 \(D_B=H\)，所以 (12) 已经是 ambient 同态，
(14) 也不可能发生；每个非平凡 q-primary 源角色都直接进入 (19) 的饱和分支。

## 4. filter-only 候选饱和与 exact successor 零容量定理

固定广义 Rado 正亏损割 \(U\)，并在同一个求值商中写

\[
Q_U=K_{\mathcal R}/W_U,\qquad m=\dim Q_U,\qquad
r=|P\setminus U|,\qquad \delta=m-r>0.
\tag{20}
\]

设一个候选只对 primary Fourier 数据做过滤，并为每个 \(i\in I_+\) 保留
实现单位差分 \(e_i-0\) 的真实 source record、provenance 以及同一
\(Q_U\) 中的 \(\pi_U\kappa(g_i)\)。在 state-realization 门之前，只定义候选记录
列空间

\[
T_\omega^{\mathrm{cand}}
=\operatorname{span}\{\pi_U\kappa(g):g\text{ 是候选保留的真实源记录}\}.
\tag{21}
\]

由 (19)，

\[
\boxed{T_\omega^{\mathrm{cand}}=Q_U.}
\tag{22}
\]

式 (22) 在候选记录层输出
\[
\mathrm{PRIMARY\_FILTER\_CANDIDATE\_SOURCE\_SATURATED}.
\tag{23}
\]
它不定义 exact-successor 的 \(T_\omega,e_\omega,h_\omega^*\)。若独立
state realization 尚未通过，必须同时输出
SELECTED_SOURCE_STATE_REALIZATION_UNPROVED，并在此停止。

现在额外假设候选已经 independently realized 为允许状态族中的 exact successor，
且其实际后继源集合保留上述候选列。此时基础定理中的合法对象 \(T_\omega\) 包含
\(T_\omega^{\mathrm{cand}}=Q_U\)，故

\[
\boxed{T_\omega=Q_U.}
\tag{24}
\]

对任意 completion 列空间 \(S_\omega\le Q_U\)，立刻有

\[
Y_\omega=S_\omega+T_\omega=Q_U,
\qquad e_\omega=m-\dim Y_\omega=0.
\tag{25}
\]

用 source-overhead/rank-slack 记号，(25) 等价于精确等号

\[
h_\omega^*=m-\dim S_\omega
=\delta+\bigl(r-\dim S_\omega\bigr)
=\delta+a_\omega.
\tag{26}
\]

故选择秩松弛也无法救回该路线。得到严格 no-go：

\[
\boxed{
\text{independently realized primary-filter successor + 全活动源保留}
\Longrightarrow
\mathrm{PRIMARY\_FILTER\_SOURCE\_PRESERVING\_SUCCESSOR\_CAPACITY\_EXHAUSTED}.
}
\tag{27}
\]

要使 \(e_\omega>0\)，必须另行构造算术 source contraction，使至少一个
\(Q_U\) 方向不再属于 \(S_\omega+T_\omega\)，并证明被删除或重类型化的每个源记录
具有全解 E4 lift 与不可重置 E5。改变过滤子群 \(X\)、重选 Fourier 角色或仅删除
菜单记录，都不构成这种证明。

## 5. 三个严格控制

### 5.1 冻结坐标正是支撑分离的来源

取 \(H=C_4\)、生成元 \((2,1)\)、预算 \((4,0)\)、目标 \(y=1\)。活动群为

\[
D_B=\langle2\rangle=\{0,2\}<C_4.
\]

奇偶角色在 \(D_B\) 上平凡，九个盒点全落在偶类，而目标在奇类。该实例进入
(10)。若把第二个预算改为正数，则 \(D_B=C_4\)，该分支立即消失。

### 5.2 局部角色可以严格失败于 ambient extension

取 \(H=C_4=\langle g\rangle\)、\(D_B=\langle2g\rangle\)，并令
\(\ell(2g)=1\in\mathbb F_2\)。则

\[
D_B\cap2H=D_B,\qquad \ell(D_B)\ne0,
\]

所以命中 (14) 的 obstruction 分支。这个局部 source 方向来自四阶角色在
\(D_B\) 上的二阶限制，但
不能冒充 \(H\to\mathbb F_2\) 的 elementary role。

### 5.3 实际 \(p=73\) Fourier deficit 已经 source-dominate

取 \(p=73,R=27,K=493=17\cdot29\)。以 \(2\) 为
\(U(27)\simeq C_{18}\) 的生成元，有

\[
17=2^{15},\qquad29=2,
\qquad \mathcal B=\{-1,0,1\}^2,
\qquad -1=2^9.
\tag{28}
\]

两个预算都为正，且 \(\langle15,1\rangle=C_{18}\)，所以 \(D_B=H\)。取
\(q=2\) 初等角色 \(\rho(x)=x\bmod2\)。精确目标计数为零，目标奇陪集计数为
\(4=2^2\)，而盒体积 \(9>2\cdot2^2\)。此外

\[
\widehat B(\rho)
=\sum_{z_1,z_2=-1}^{1}(-1)^{15z_1+z_2}=1,
\qquad
-(-1)^9\widehat B(\rho)=1.
\tag{29}
\]

所以这是真实 Type I 图表中的 sharp filtered Fourier deficit。两个 source columns
都是 \(1\in\mathbb F_2\)，已经张成 \(Q=\mathbb F_2\)；保留它们的候选满足
\(T^{\mathrm{cand}}=Q\)，候选 annihilator 维数为零。若它 independently
realized 且保留这些列，才有合法 \(T=Q\) 与 \(e=0\)。这严格否定“正
Fourier deficit 本身留下正 successor 容量”。

## 6. 选择器收缩

primary-filter 路线现在按以下顺序分派：

~~~text
chi trivial on D_B:
  PRIMARY_FILTER_FROZEN_QUOTIENT_SEPARATION
chi nontrivial on D_B and elementary extension fails:
  PRIMARY_FILTER_ELEMENTARY_AMBIENT_EXTENSION_OBSTRUCTED
elementary role extension/SNF passes, candidate active sources retained:
  PRIMARY_FILTER_CANDIDATE_SOURCE_SATURATED
state realization absent:
  SELECTED_SOURCE_STATE_REALIZATION_UNPROVED
exact successor realized and active source columns retained:
  PRIMARY_FILTER_SOURCE_PRESERVING_SUCCESSOR_CAPACITY_EXHAUSTED
explicit arithmetic source contraction + exact state + E4/E5:
  return to EXACT_SUCCESSOR_SOURCE_OVERHEAD_CAPACITY_CERT
~~~

因此 raw primary filtering 已从“可能直接产生正容量 successor”的候选中排除。
它仍能选择算术 source contraction 所需的角色，但收缩、状态实现和 lift 必须来自
nearest-fiber、owner、重图表或新的整数构造，不能由 Fourier 过滤本身推出。

## 聚焦验证

~~~bash
python3 reproductions/type_i_primary_filter_active_source_saturation_zero_successor_capacity.py --verify
~~~

验证器只检查式 (4) 的三个小群控制、冻结商、\(C_4\) ambient-extension 严格障碍、
两角色求值饱和，以及实际 \(p=73,R=27\) 的 sharp Fourier deficit 与零容量；不运行
历史扫描。
