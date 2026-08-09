---
kind: claim
claim_id: type-I-source-lattice-owner-window-affine-profile-admission
title: 有限源集 q-height 对偶剖面的 owner 窗口仿射格准入
statement: >-
  固定奇素数 q、不被 q 整除的核心素数 p、物理层 J 和源格 L。对非空有限带基点源集
  X subset z0+L，所有实现给定角色 gamma 的整数 q-height 对偶产生一个基不变的整数
  高度剖面仿射格 P。存在同一个整数对偶和同一个自由平移，把 X 的全部记录同时送入
  真实 q^J-prefix owner 窗口，当且仅当 P 与有限盒 [0,M_J]^X 相交；等价地，某个
  允许对偶剖面的振幅不超过 M_J。固定剖面的全部平移形成显式整数区间。该交集可通过
  逐盒点 Smith 判定完全决定，空交时每个盒点的首个 Smith 整除失败组成严格有限证书。
  加上本地最大重数、单射或未被本地源标签使用的 q^(J+1)-深层索引条件后，仍是同一
  有限交集的精确子集判据。二点情形进一步化为一个一维仿射理想到 0 的距离。成功回执
  给出实际整数仿射 provenance、规范 Type II owner 顶点和真实横向角色；它不自动
  支付全局 occurrence、既定标签、共同基 target、E4 或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - type-I-source-lattice-filtered-dual-tail-hall-capacity
  - type-I-odd-owner-fiber-incidence-lattice-source-map
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
topics:
  - type-I
  - type-II
  - source-lattice
  - q-height
  - affine-lattice
  - owner-window
  - Smith-normal-form
  - source-provenance
  - occurrence-capacity
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: exact-layer-dual-image-and-normalized-integer-dual
  - claim: type-I-source-lattice-filtered-dual-tail-hall-capacity
    role: algebraic-role-layer-admission-before-physical-edges
  - claim: type-I-odd-owner-fiber-incidence-lattice-source-map
    role: exact-owner-window-and-canonical-cross-fiber-vertices
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: boundary-between-deep-owner-label-and-physical-next-layer-toggle
  - reproduction: reproductions/type_i_source_lattice_owner_window_affine_profile_admission.py
    role: focused-direct-owner-box-and-local-depth-controls
visibility: public
last_checked: '2026-08-10'
---

# 有限源集 \(q\)-height 对偶剖面的 owner 窗口仿射格准入

## 1. 真实缺口：同一个整数对偶必须同时容纳全部记录

固定奇素数 \(q\)、\(q\nmid p\)、层 \(J\ge1\)，并记

\[
Q=q^J,
\qquad
B_p=\left\lfloor\frac{p-1}{4}\right\rfloor.
\tag{1}
\]

令 \(0<\beta_J<Q\) 是
\(p+4\beta_J\equiv0\pmod Q\) 的唯一代表，并定义

\[
M_J=\left\lfloor\frac{B_p-\beta_J}{Q}\right\rfloor.
\tag{2}
\]

当 \(M_J\ge0\) 时，严格窗口 \(0<4s<p\) 中全部
\(Q\)-prefix owner 恰为

\[
\mathcal O_J(p)
=\{\beta_J+Qu:0\le u\le M_J\}.
\tag{3}
\]

若 \(M_J<0\)，则 \(\mathcal O_J(p)=\varnothing\)，应先输出
OWNER_WINDOW_EMPTY；这不是对偶格的 Smith 障碍。以下范围定理只讨论 \(M_J\ge0\)。

已有层对偶定理判定一个角色是否属于
\(\operatorname{im}\rho_J\)，但这还不够：实际 F/G 请求给出有限个带来源记录，
必须由**同一个**整数对偶和**同一个**仿射平移同时进入 (3)。逐相位另选最小剩余数
只保留模 \(q\) 标签，不保留这个整数来源合同。

令 \(L\le\mathbb Z^d\) 的秩为 \(r\)，并取其一个真正的整数格基矩阵

\[
\mathbf B_L=(b_1\ \cdots\ b_r)\in\mathbb Z^{d\times r}.
\tag{4}
\]

令 \(\gamma:L\to\mathbb F_q\) 在该基上的值为

\[
g=(\gamma(b_1),\ldots,\gamma(b_r))^T\in\mathbb Z^r,
\tag{5}
\]

其中任取整数代表。固定非空有限源集

\[
X=\{x_0=z_0,x_1,\ldots,x_{m-1}\}\subset z_0+L,
\qquad
x_i-z_0=\mathbf B_Ln_i.
\tag{6}
\]

把 \(n_i^T\) 组成坐标矩阵
\(N_X\in\mathbb Z^{m\times r}\)；其第零行为零。把 \(z_0\) 纳入 \(X\)
表示该基点本身也必须获得 owner 标签，并使平移可从输出的第零坐标直接恢复。

## 2. 归一化对偶值格与基不变高度剖面

定义层 \(J\) 的归一化整数对偶值集合

\[
\boxed{
\mathcal Y_J(L,\gamma;\mathbf B_L)
=\left\{y\in\mathbb Z^r:
\begin{array}{l}
\exists a\in\mathbb Z^d,\ \mathbf B_L^Ta=Qy,\\
y\equiv g\pmod q
\end{array}\right\}.}
\tag{7}
\]

若 \(a\) 对应于 \(y\)，则
\(a\in\mathcal A_J(L)\)，且

\[
\rho_J(a)(b_i)=y_i\equiv g_i\pmod q.
\tag{8}
\]

反向也显然。因此

\[
\boxed{
\mathcal Y_J\ne\varnothing
\iff\gamma\in\operatorname{im}\rho_J
\iff\gamma(L\cap q^{J+1}\mathbb Z^d)=0.}
\tag{9}
\]

令

\[
\mathcal I_J
=\left\{\frac{\mathbf B_L^Ta}{Q}\in\mathbb Z^r:
a\in\mathbb Z^d\right\}.
\tag{10}
\]

若 (7) 非空并固定 \(y_0\in\mathcal Y_J\)，则

\[
\boxed{
\mathcal Y_J=y_0+\Lambda_J,
\qquad
\Lambda_J=\mathcal I_J\cap q\mathbb Z^r.}
\tag{11}
\]

每个 \(y\in\mathcal Y_J\) 在 \(X\) 上产生整数高度剖面

\[
h_y(x_i)=n_i^Ty,
\qquad h_y(z_0)=0.
\tag{12}
\]

它保留原角色，因为

\[
h_y(x_i)-h_y(x_k)
\equiv\gamma(x_i-x_k)\pmod q.
\tag{13}
\]

这一定义不依赖所选格基。事实上若
\(\mathbf B_L'=\mathbf B_LU\)、\(U\in\mathrm{GL}_r(\mathbb Z)\)，则

\[
n_i'=U^{-1}n_i,
\qquad
g'\equiv U^Tg\pmod q,
\qquad
y'=U^Ty,
\qquad
(n_i')^Ty'=n_i^Ty.
\tag{14}
\]

而且 \(\mathcal Y_J'=U^T\mathcal Y_J\)。因此以下剖面仿射格是内禀对象：

\[
\boxed{
\mathcal P_{J,X}(L,\gamma)
=\{c\mathbf1+N_Xy:c\in\mathbb Z,\ y\in\mathcal Y_J\}
=N_Xy_0+\mathbb Z\mathbf1+N_X\Lambda_J
\subset\mathbb Z^X.}
\tag{15}
\]

## 3. owner 窗口仿射剖面定理

**定理。** 假设 \(M_J\ge0\) 且 (9) 通过。下列条件等价：

1. 存在 \(a\in\mathcal A_J(L)\) 实现 \(\gamma\)，并存在自由的
   \(c\in\mathbb Z\)，使

   \[
   \Phi_{a,c}(x)
   =\beta_J+Qc+a\cdot(x-z_0)
   \tag{16}
   \]

   对所有 \(x\in X\) 都属于真实 owner 窗口 \(\mathcal O_J(p)\)；
2. \(\mathcal P_{J,X}(L,\gamma)\cap[0,M_J]^X\ne\varnothing\)；
3. 存在 \(y\in\mathcal Y_J\) 满足

   \[
   \boxed{
   \operatorname{osc}_X(h_y)
   :=\max_{x\in X}h_y(x)-\min_{x\in X}h_y(x)
   \le M_J.}
   \tag{17}
   \]

对固定的 \(y\)，全部可行平移恰为整数区间

\[
\boxed{
[-\min_Xh_y,\ M_J-\max_Xh_y]\cap\mathbb Z.}
\tag{18}
\]

**证明。** 若 \(\mathbf B_L^Ta=Qy\)，则

\[
\Phi_{a,c}(x_i)
=\beta_J+Q(c+n_i^Ty).
\tag{19}
\]

由 (3)，(19) 在窗口中当且仅当

\[
0\le c+h_y(x_i)\le M_J
\qquad(0\le i<m).
\tag{20}
\]

这正是 (15) 与有限盒相交。所有下界的最大值是
\(-\min_Xh_y\)，所有上界的最小值是
\(M_J-\max_Xh_y\)，故可行整数 \(c\) 恰为 (18)；该区间非空当且仅当 (17)。
三项等价。

成功时令

\[
u_x=c+h_y(x),
\qquad
s_x=\beta_J+Qu_x.
\tag{21}
\]

则 (16) 是真实整数仿射 provenance，而非事后相位赋值，并且

\[
\tau_J(s_x)-\tau_J(s_w)
\equiv\gamma(x-w)\pmod q.
\tag{22}
\]

更明确地，左侧是 \(\mathbb F_q\) 中的
\([u_x-u_w]_q\)。

每个 \(s_x\) 唯一写成
\(s_x=A_x^2C_x\)、\(C_x\) 平方自由；令 \(D_x=A_xC_x\)，即得到规范
Type II owner 顶点 \((D_x,A_x)\)。又因
\(q\mid p+4s_x\) 且 \(q\nmid p\)，有 \(q\nmid D_x\)。

## 4. 有限 Smith 判定与严格盒空证书

式 (17) 看似仍在无限仿射格上取最小值，但 owner 盒本身给出完全有限的等价判定。
写

\[
y=g+qk,
\qquad k\in\mathbb Z^r,
\tag{23}
\]

并对每个 \(u\in\{0,1,\ldots,M_J\}^m\) 定义整数系统

\[
\mathsf A_{J,X}
\begin{pmatrix}a\\k\\c\end{pmatrix}
=b_u,
\tag{24}
\]

其中

\[
\mathsf A_{J,X}
=\begin{pmatrix}
\mathbf B_L^T&-QqI_r&0\\
0&qN_X&\mathbf1
\end{pmatrix},
\qquad
b_u=\begin{pmatrix}Qg\\u-N_Xg\end{pmatrix}.
\tag{25}
\]

第一组行等价于
\(\mathbf B_L^Ta=Q(g+qk)\)，第二组行等价于
\(u=c\mathbf1+N_X(g+qk)\)。所以

\[
\boxed{
u\in\mathcal P_{J,X}(L,\gamma)
\iff (24)\text{ 有整数解}.}
\tag{26}
\]

取 Smith 分解

\[
R\mathsf A_{J,X}S
=\operatorname{diag}(d_1,\ldots,d_t,0,\ldots,0),
\qquad
d_i>0,\quad d_i\mid d_{i+1},
\tag{27}
\]

其中 \(R,S\) unimodular。系统 (24) 有整数解，当且仅当

\[
d_i\mid(Rb_u)_i\quad(1\le i\le t),
\qquad
(Rb_u)_i=0\quad(i>t).
\tag{28}
\]

因此算法不是截断无界搜索：枚举有限盒中全部 \(u\)，对每个点检查 (28)。若没有
任何点通过，则为每个 \(u\) 保存首个失败的

\[
(u,i,d_i,(Rb_u)_i)
\tag{29}
\]

（零行用 \(d_i=0\) 记），得到可独立重放的严格
OWNER_WINDOW_DUAL_PROFILE_BOX_EMPTY 证书。改变 (5) 的整数代表只改变未知量
\(k\)，不改变 (26)。

这个证书最坏含 \((M_J+1)^{|X|}\) 个盒点。它是严格有限证书，但不是统一有界的
短证书；不能用本定理单独宣称已经关闭最终短证书目标。

## 5. 本地重数容量与未使用深层索引

对 \(u\in\mathbb Z^X\) 定义局部 owner 标签重数

\[
\mu(u)=\max_{n\in\mathbb Z}\#\{x\in X:u_x=n\}.
\tag{30}
\]

若每个本地 owner 标签至多允许 \(\mu_0\) 个源记录，则精确准入集合是

\[
\boxed{
\mathcal U_{\mu_0}
=\mathcal P_{J,X}\cap[0,M_J]^X
\cap\{u:\mu(u)\le\mu_0\}.}
\tag{31}
\]

特别地，\(\mu_0=1\) 当且仅当
\(X\to\mathcal O_J(p)\) 单射。若范围交非空但 (31) 为空，可只枚举有限盒中
重数不超过 \(\mu_0\) 的点并给出 (28) 的失败行，从而得到严格
OWNER_WINDOW_LOCAL_INDEX_MULTIPLICITY_DEFICIT。这只是**本地统一标签容量**；
真实 state 的 prescribed label、已占用 occurrence key 与跨请求 Hall 约束仍未计入。

令 \(0<\beta_{J+1}<q^{J+1}\) 为下一层代表。存在唯一

\[
\delta_J=\frac{\beta_{J+1}-\beta_J}{Q}
\in\{0,\ldots,q-1\}.
\tag{32}
\]

owner 指标 \(n\) 进入下一层，当且仅当

\[
q^{J+1}\mid p+4(\beta_J+Qn)
\iff n\equiv\delta_J\pmod q.
\tag{33}
\]

记

\[
T_{J+1}(M_J)
=\{0\le n\le M_J:n\equiv\delta_J\pmod q\}.
\tag{34}
\]

在要求一个额外本地记录使用与全部 source owner 标签**数值不同**的新标签的合同下，
存在这种深层索引的充要条件是

\[
\boxed{
\exists u\in\mathcal U_{\mu_0}:
T_{J+1}(M_J)\setminus\{u_x:x\in X\}\ne\varnothing.}
\tag{35}
\]

取差集最小元素 \(n_*\)，则

\[
s_*=\beta_J+Qn_*
\tag{36}
\]

是真实窗口中的 owner 标签，并唯一确定一个规范 Type II 顶点 \((D_*,A_*)\)，且
\(q^{J+1}\mid p+4s_*\)。成功只输出
OWNER_WINDOW_LOCAL_UNUSED_DEEP_INDEX_AVAILABLE；若所有可行 \(u\) 都耗尽 (34)，
输出 OWNER_WINDOW_LOCAL_UNUSED_DEEP_INDEX_EMPTY。后一回执只否定“同一 owner
窗口内另取数值不同的深层标签”的本地合同：

* 本地未使用的数值仍可能已被其它 token 的全局 key 占用，所以它不充分于全局
  occurrence 可用；
* source 与 target 的 state-id 不同时，同一数值可以对应不同 occurrence key，
  所以本地数值已使用也不必要地阻碍全局 assignment。

对一条带名二点边 \(e=(x_-,x_+)\)，若

\[
\gamma(x_+-x_-)\ne0,
\tag{37}
\]

则两个 source 指标模 \(q\) 不同，故至多一个属于 (34)。恰有一个 deep endpoint
的充要条件是

\[
\delta_J\in\{u_{x_-},u_{x_+}\}\pmod q.
\tag{38}
\]

式 (35)、(38) 只提供 local-depth source/label 的算术候选。要升级为已有的
NEXT_LAYER_EXCLUSIVE_Q_FACTOR_TOGGLE，仍须另证共同源基、target 除子关系、
既定 Fourier 角色以及 source/target 全局 occurrence key；本卡不把 (35)
冒充物理终端，也不把 deep source 改标成新的固定层请求。

## 6. 二点闭式：仿射理想到零的距离

令 \(X=\{z_0,z_1\}\)，并写
\(z_1-z_0=\mathbf B_Ln\)。固定
\(y_0\in\mathcal Y_J\)，则所有可能的高度差组成

\[
\mathcal T_e=n^T\mathcal Y_J
=n^Ty_0+n^T\Lambda_J.
\tag{39}
\]

若 \(\lambda_1,\ldots,\lambda_s\) 是 \(\Lambda_J\) 的格基，令

\[
\kappa_e=\gcd(n^T\lambda_1,\ldots,n^T\lambda_s)\ge0.
\tag{40}
\]

全零时约定 \(\kappa_e=0\)。于是

\[
\boxed{
\mathcal T_e=n^Ty_0+\kappa_e\mathbb Z,}
\tag{41}
\]

其中 \(\kappa_e=0\) 表示单点集合。二点范围准入的充要条件化为

\[
\boxed{
\operatorname{dist}(0,\mathcal T_e)
=\min_{t\in\mathcal T_e}|t|
\le M_J.}
\tag{42}
\]

若 (37) 成立，则每个 \(t\in\mathcal T_e\) 都满足
\(t\equiv\gamma(z_1-z_0)\not\equiv0\pmod q\)，所以任何通过 (42) 的实现自动单射。
这比粗略的 \(Q<p/4\) 窗口必要条件更精确：它同时保留 source content、指定角色与
真实有限窗口。

## 7. 三个严格控制

### 7.1 \(p=97,q=3,J=1\)：边界正例与本地新深层索引

取 \(L=\mathbb Z\)、\(\gamma(1)=1\)、\(X=\{0,7\}\)。这里

\[
\beta_1=2,
\qquad
M_1=7,
\qquad
\mathcal Y_1=1+3\mathbb Z.
\tag{43}
\]

高度差集合为 \(7+21\mathbb Z\)，到零的距离恰为 7。唯一可行剖面取
\(y=1,c=0\)，得到 owner 指标 \((0,7)\) 和标签

\[
(s_0,s_7)=(2,23).
\tag{44}
\]

它们分别满足 \(v_3(97+4s)=1,3\)，且横向差为
\(7\equiv1\pmod3\)。下一层
\(\beta_2=5\)，故 \(\delta_1=1\)、深层指标为
\(\{1,4,7\}\)。指标 1 未被 source 使用，给出规范新标签 \(s_*=5\)，并有
\(v_3(97+4s_*)=2\)。三个 canonical 顶点分别为
\((D,A)=(2,1),(23,1),(5,1)\)。

但这条 source 边的横向步长为
\((23-2)/3=7\)，最大共同基是
\(\gcd(2,7)=1\)，而 \(5\nmid1^2\)。所以新标签 5 不在共同基 target 菜单中，
不能调用 next-layer physical toggle。这个控制只通过 local-depth 合同。

### 7.2 同一窗口的严格范围反例

保持 \(p,q,J,L,\gamma\) 不变，改取 \(X=\{0,8\}\)。所有高度差为

\[
8(1+3k)=8+24k,
\tag{45}
\]

其最小绝对值为 8，大于 \(M_1=7\)。所以层对偶 (9) 已通过、角色非零，但不存在
任何整数对偶和平移把两个记录同时放入 owner 窗口。这里输出
OWNER_WINDOW_DUAL_PROFILE_BOX_EMPTY，不能再记为模相位 lift 成功。

### 7.3 \(p=97,q=11,J=1\)：source 通过但本地新深层索引耗尽

取 \(L=\mathbb Z\)、\(\gamma(1)=1\)、\(X=\{0,1\}\)。此时

\[
\beta_1=6,
\qquad
M_1=1,
\qquad
\mathcal Y_1=1+11\mathbb Z.
\tag{46}
\]

唯一可行剖面为 \(y=1,c=0\)，owner 指标是 \((0,1)\)，标签为 \((6,17)\)，故
source 范围与单射都通过。但
\(\beta_2=6\)、\(\delta_1=0\)，而窗口内唯一深层指标集合

\[
T_2(1)=\{0\}
\tag{47}
\]

已被 source 使用。因此 (35) 严格失败。这区分了“源剖面可实现”和“同窗口另有
数值不同的新深层标签”两个本地容量门；它不构成全局 occurrence obstruction。

## 8. 统一选择器接口与边界

对一个已经选定物理层的有限源请求，分派为：

~~~text
FINITE_SOURCE_OWNER_PROFILE_REQUEST(q, J, L, gamma, X, local_multiplicity)
  M_J < 0:
    OWNER_WINDOW_EMPTY
  otherwise:
    gamma not in im(rho_J):
      SOURCE_LATTICE_QHEIGHT_DUAL_OBSTRUCTED
    otherwise:
      build the intrinsic affine profile lattice P_J,X
      P_J,X intersect [0,M_J]^X is empty:
        OWNER_WINDOW_DUAL_PROFILE_BOX_EMPTY(Smith box certificate)
      local-index-multiplicity-bounded intersection is empty:
        OWNER_WINDOW_LOCAL_INDEX_MULTIPLICITY_DEFICIT
      otherwise:
        OWNER_WINDOW_AFFINE_DUAL_PROFILE_READY
        emit (a, y, c, owner indices, canonical source vertices)
        optional local unused deep-index contract:
          success -> OWNER_WINDOW_LOCAL_UNUSED_DEEP_INDEX_AVAILABLE
          failure -> OWNER_WINDOW_LOCAL_UNUSED_DEEP_INDEX_EMPTY
        intersect surviving receipts with prescribed-label/global-occurrence/
        common-base-target/source-switch edges
        run general physical Hall/Rado
~~~

固定层请求始终在原 \(J\) 上运行本判据；不得用更深层重新标记失败请求。对尚未
绑定层且只受最小 q-height 约束的请求，先由过滤上尾定理选择并冻结层，再调用本卡。
若合同只指定一维角色子空间、允许非零缩放，则必须显式取

\[
\bigcup_{\lambda\in\mathbb F_q^\times}
\mathcal P_{J,X}(L,\lambda\gamma).
\tag{48}
\]

带名不可缩放角色只能使用原 \(\gamma\)，不能暗中选择 \(\lambda\)。

若下游已经固定 \(c\bmod q\)、指定某个 source 必须 deep，或绑定某个 owner 标签，
则还须把允许的平移集合与 (18) 相交；自由平移版 (17) 不能覆盖这些额外条件。

本卡关闭的是“代数 q-height 通过以后，同一整数对偶能否同时进入真实 owner 窗口”的
精确门，并把 source 标签重数与本地新深层索引变成有限容量映射。它没有证明任意实际
F/G 请求都通过盒交，也没有自动满足 prescribed target/source label、共同 source base、
单位群 Fourier 角色、全局 occurrence、E2、E4 或 E5。失败证书必须继续接到另一
Type I/II terminal、完整 kernel source box 或保持标记的严格下降，才会推进最终猜想。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_source_lattice_owner_window_affine_profile_admission.py \
  --verify
~~~

验证器只直接枚举上述有限 owner 盒，重算三个控制的实际标签、估值、规范顶点和本地
深层索引集合，并比较一族二点闭式；不运行历史扫描。
