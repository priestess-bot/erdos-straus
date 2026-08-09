---
kind: claim
claim_id: type-I-prescribed-target-occurrence-rado-contraction
title: 指定 target occurrence 的先验割、矩形 Hall--Rado 收缩与耦合反例
statement: >-
  对已经通过 owner profile、共同规范源基、指定目标、带名 edge、角色 SNF 与
  next-layer 算术门的有限请求族，完整候选必须同时保存 deep occurrence、shallow
  canonical slot、共同空间源列与 target occurrence，不能把四者独立选择。若每个请求
  已固定 target state-id 和整数目标，则可在共享 occurrence ledger 上先验收缩：先
  预收费 target；同一 edge 的 d=t(r) 映为私有零增量 atom，其它 deep 使用 b_O-m_T。
  完整选择存在当且仅当每个 target key 的请求重数不超容量，且该增量
  deep--shallow--column source 系统可选。
  若每个请求的剩余 source 候选进一步严格因子化为 deep、shallow 与 column 三个允许
  集的笛卡尔积，则后者精确等价于 deep Hall、shallow Hall 和 column Rado 三组子集
  不等式；该 column 分支要求物理请求的角色方向本身独立，相关角色仍带不同物理义务
  时须回到尚未收缩的一般耦合系统。固定 D、只按非零相位 c 分型时化为 target 预收费后的 deep residual
  capacity 与各 shallow phase capacity 不等式，再加
  source-column Rado；只要求 deep--shallow 二维矩形再另验 Rado 仍有四边扭结反例。
  p=4441,q=5,J=1,D=66 给出严格反例：匿名三部容量为 1，但
  prescribed rank-one profile 的唯一共同基 target tuple 两端均 shallow，故该算术
  控制的带名 next-layer 候选超图为空。若 target 随候选变化，则 source 与 target
  两个投影 Hall 也不充分，最小两请求三候选扭结即失败。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-owner-profile-canonical-base-target-slot-capacity
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-owner-source-preserving-fiber-uniformity-criterion
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-cross-state-qcapacity-deficit-annihilator-relay
  - type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - prescribed-target
  - physical-occurrence
  - hypergraph
  - Rado
  - Hall
  - source-rank
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-owner-profile-canonical-base-target-slot-capacity
    role: finite-profile-canonical-base-prescribed-target-candidates
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: source-and-target-next-layer-occurrence-keys
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: prescribed-role-and-source-target-label-gate
  - claim: type-II-owner-source-preserving-fiber-uniformity-criterion
    role: source-column-signature-gate
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-column-representative-criterion
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-key-capacity-and-source-column-deficit-split
  - claim: type-II-cross-state-qcapacity-deficit-annihilator-relay
    role: source-dominating-deficit-relay-boundary
  - claim: type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
    role: p2113-empty-marked-fiber-and-reset-boundary
  - concept: denominator-escape-state-contract
    role: marked-E4-and-nonresetting-E5-contract
  - reproduction: reproductions/type_i_prescribed_target_occurrence_rado_contraction.py
    role: focused-profile-coupling-target-collision-rectangular-and-twisted-controls
visibility: public
last_checked: '2026-08-10'
---

# 指定 target occurrence 的先验割、矩形 Hall--Rado 收缩与耦合反例

## 1. 完整候选必须是同一个 witness

固定核心素数 \(p\)、奇素数 \(q\nmid p\) 和 owner 层 \(J\ge1\)。令
\(\mathcal R\) 是有限个按语义/content id 去重的 F/G \(q\)-primary 请求。固定角色的
初等素数 \(\ell\)，并令共同 source-column 空间为 \(V=V_\ell\)。对需要 column-Rado
支付的分支，本卡只处理请求方向 \((\rho_r)_{r\in\mathcal R}\subset V\) 本身独立的
情形。进入本卡前只能合并“代数角色与全部物理义务都相同”的重复请求；相关角色若
仍带不同 occurrence/target 义务，就不能用角色基替换请求集，而须保留独立的物理
请求集、代数基集及二者耦合，回到一般联合选择问题。下文的矩形 Hall--Rado 定理
不声称处理该情形。纯物理请求在删除 column 坐标的分支处理。fixed-layer 请求的
\(J\) 已经冻结；unlayered 请求必须先通过上尾门并冻结 \(J\)，才能进入本卡。

一个请求 \(r\in\mathcal R\) 保存 source state id、整数源格 \(L_r\)、带基点记录集
\(X_r\)、不可缩放的角色 \(\gamma_r\)、prescribed source/target label 合同与 target
准入合同；target state \(T(w)\) 和整数目标 \(x(w)\) 可以由请求固定，也可以在候选间
变化。它的一个完整算术候选必须是同一个 tuple

\[
\begin{aligned}
w=(&r;\mathbf a,y,c,u,(s_z)_{z\in X_r},D,T(w),x(w),
\sigma_{\rm SNF},\Pi,z_d,z_s,\\
&d(w),h(w),a(w),t(w),v_{a(w)}).
\end{aligned}
\tag{1}
\]

其中同一 tuple 逐项满足

\[
\mathbf B_L^T\mathbf a=q^Jy,\qquad
y\equiv g\pmod q,\qquad
u=c\mathbf1+N_Xy\in[0,M_J]^{X_r},
\tag{2}
\]

\[
s_z=\beta_J+q^Ju_z,\qquad
D_{s_z}=D\ \ (z\in X_r),\qquad
D_{x(w)}\mid D,
\tag{3}
\]

并且 \(\Pi=(z_d,z_s)\) 是带名整数 provenance 产生的非零 edge，满足

\[
u_{z_d}\equiv\delta_J\pmod q,\qquad
u_{z_s}\not\equiv\delta_J\pmod q,\qquad
x(w)\equiv\beta_{J+1}\pmod {q^{J+1}}.
\tag{4}
\]

\(\sigma_{\rm SNF}\) 是同一 source rows、target 与 prescribed labels 的联合角色解，
且实际整数类 \(q\) 在该角色中非零。任何一项失败都保留其原始局部回执；不能从其它
profile、其它 \(D\)、其它 edge 或其它角色各取一个存在见证后拼成 (1)。

## 2. 四个角色坐标与三个共享 ledger

扣除全局 ledger 已收费部分。候选 (1) 使用四个带角色坐标：

1. deep next-layer occurrence
   \[
   d(w)=(\operatorname{source\_state\_id},s_{z_d},q,J+1);
   \tag{5}
   \]
2. shallow canonical source-slot atom
   \[
   h(w)=(\operatorname{source\_state\_id},s_{z_s},q,J,D);
   \tag{6}
   \]
3. 已通过 source-SNF 的 column atom \(a(w)\)，其共同初等商向量为
   \(v_{a(w)}\in V\)；
4. target next-layer occurrence key
   \[
   t(w)=(T(w),x(w),q,J+1).
   \tag{7}
   \]

式 (5)--(7) 均不含 edge id 或局部记录坐标；\(z_d,z_s\) 仍保留在 witness provenance
中。同一 state 内同一整数层槽即使来自不同记录位置，也映到同一 key；不同 states
仍是不同资源。尤其 \(d(w)\) 与 \(t(w)\) 都进入同一个全局 occurrence key 集
\(\mathcal O\)，不是两个互不相交的容量部。式 (6) 记录匿名容量公式中不可重复使用的
shallow source slot。若某个具体 source
合同允许复用，必须把相应容量写入 atom ledger；不能因为 shallow 端没有独占
\(q^{J+1}\) 因子就默认无限复用。

occurrence 与 shallow key 的剩余整数容量分别记为 \(b_O(o)\) 与 \(b_S(h)\)。只有当
合同证明同一 key 的容量副本具有完全相同的候选邻接、因而是可互换 true twins 时，
才允许把它们聚合成 \(b>1\)；否则必须展开成不同的单位 key 并保留各自邻接。本文的
\(d,h,t\) 均指这种合法聚合后的 key。

进入本卡前先处理历史 ledger：完整 key 集已由同一 assignment-id 拥有的精确 replay
记为已满足并移出 fresh 请求族；任意部分重叠或不同 owner 的重叠候选直接保留原冲突
回执。下文只讨论经过该预处理的 fresh、content-deduplicated batch，\(b_O,b_S\) 是
预处理后的剩余容量。

局部 \(z\) 的折叠只发生在物理容量 key，不自动认定 source class 相同。若要把多个
候选聚合成同一个可互换 source atom，它们必须有一致的完整签名
\[
\eta=(q\text{-layer},\text{source record/provenance }\sigma,v_a).
\]
若 \(\eta\) 不一致且没有 source-class 分槽合同，保留共同物理 occurrence key 与各自
不同的 column/source-class 坐标；需要单一 atom 的分支先输出

~~~text
PRESCRIBED_TARGET_SOURCE_ATOM_SIGNATURE_NONUNIFORM
~~~

一般候选因此构成带线性拟阵约束的有限 5-部对象

\[
\mathcal E\subseteq
\mathcal R\times\mathcal D\times\mathcal S\times\mathcal A\times\mathcal T,
\qquad \mathcal D,\mathcal T\subseteq\mathcal O.
\tag{8}
\]

完整算术 assignment 是每个请求选一条超边 \(w_r\)，并按现有 unique-key ledger
计算 occurrence 载荷

\[
\ell_O(o)=
\#\{r:d(w_r)=o\ \text{或}\ t(w_r)=o\}.
\tag{8a}
\]

因此同一 assignment 内 \(d(w_r)=t(w_r)\) 只登记一次；不同请求或不同
assignment-id 对同一 key 分别收费，并在总载荷超过 \(b_O(o)\) 时冲突，unit ledger
下即为直接冲突。要求 \(\ell_O(o)\le b_O(o)\)，每个 shallow
key 的载荷不超过 \(b_S(h)\)，且所选 \(v_a\) 线性独立。容量为一时即为不重复。该对象
有限，因为 owner 盒有限、\(1\le D\le B_p\)、\(x(w)\mid D^2\)、有限群角色和所有
ledgers 均有限。

## 3. 固定 target occurrence 的先验割

现在增加本卡的核心假设：请求已经同时绑定 target state id \(T_r\) 与整数目标
\(x_r\)，因此

\[
\boxed{
T(w)=T_r,\quad x(w)=x_r,\quad
t(w)=t(r)=(T_r,x_r,q,J+1)
\quad\text{对每个 }w\in\mathcal E(r).}
\tag{9}
\]

只绑定整数 \(x_r\)、但允许候选构造不同 target states 时，不满足 (9)。记固定
target 在共享 occurrence ledger 上产生的载荷为

\[
m_T(o)=\#\{r\in\mathcal R:t(r)=o\}.
\tag{10}
\]

若 \(m_T(o)\le b_O(o)\)，在证明中先保留这些 target 收费，并定义其它请求的 source deep
可用的剩余容量

\[
b_D^{\,T}(o)=b_O(o)-m_T(o).
\tag{10a}
\]

同一请求可以用自己的 target claim 支付相同的 deep key。为精确保存该幂等语义，
给每个请求加入只对它可见、容量为一的私有原子 \(\star_r\)，并定义增量收费映射

\[
\widehat d_r(w)=
\begin{cases}
\star_r,&d(w)=t(r),\\
d(w),&d(w)\ne t(r).
\end{cases}
\tag{10b}
\]

删除 (8) 的 target 坐标并应用 (10b)，得到 source-side 候选

\[
\widehat{\mathcal E}_{\rm src}(r)
=\{(\widehat d_r(w),h(w),a(w)):w\in\mathcal E(r)\}.
\tag{11}
\]

**固定 target 割定理。** 在 (9) 下，完整算术 assignment 存在，当且仅当

\[
\boxed{m_T(o)\le b_O(o)\qquad\text{对每个 }o\in\mathcal O}
\tag{12}
\]

且 source-side 系统 (11) 存在一个选择：真实 deep key \(o\) 的载荷不超过
\(b_D^{\,T}(o)\)，每个私有 \(\star_r\) 的载荷不超过一，shallow key 的载荷不超过
\(b_S\)，并且 columns 独立。

**证明。** 任意选择都对 occurrence key \(o\) 产生 \(m_T(o)\) 个固定 target
收费，所以它们可行当且仅当 (12) 成立。若某请求另选 \(d(w)=t(r)=o\)，由 (8a)
不会增加 \(o\) 的载荷，恰由 \(\star_r\) 表示；若 \(d(w)\ne t(r)\)，它在相应真实
key 上增加一次收费，只能使用 (10a) 的剩余容量。因此完整选择投影到 (11) 必为上述
增量 source-side 选择。反向地，把任一这种选择与固定 target 收费合并：私有原子不
增加 occurrence 载荷，真实 deep 原子的总增量至多 \(b_D^{\,T}(o)\)，所以每个
\(o\) 的最终载荷至多 \(m_T(o)+b_D^{\,T}(o)=b_O(o)\)。这与 (8a) 完全一致。证毕。

这里的“保留”只是组合证明中的容量预约，不提前写 ledger。只有完整 edge、\(\Pi\) 与
全部 source/target keys 选定后，才按既有 assignment-id 合同原子登记；\(\star_r\)
绑定到请求 \(r\) 的同一个 target 容量副本，不能被其它请求使用。

这一定理只剥离 target 坐标；它没有把相关的 deep--shallow pair 擅自压成一个普通
source key。

## 4. 矩形乘积 Hall--Rado 定理

对每个请求从 \(\widehat{\mathcal E}_{\rm src}\) 定义三个投影

\[
\mathcal D(r),\qquad \mathcal S(r),\qquad \mathcal A(r),
\tag{13}
\]

其中真实 deep atom 的 \(b_D(d)\) 指 \(b_D^{\,T}(d)\)，私有
\(b_D(\star_r)=1\)，shallow 容量仍为 \(b_S(h)\)。容量克隆后，
\(\mathcal D(r)\) 和 \(\mathcal S(r)\) 等价地替换为请求可使用的具名副本集；下列求和
形式避免把副本标签写进算术 witness。

并假设所有局部门之后仍有严格的**矩形性**

\[
\boxed{
\widehat{\mathcal E}_{\rm src}(r)
=\mathcal D(r)\times\mathcal S(r)\times\mathcal A(r)
\qquad(r\in\mathcal R).}
\tag{14}
\]

式 (14) 不是投影定义自动给出的等式；它断言任意分别合法的 deep、shallow 与 column
选择都能由同一个完整 witness 组合。profile、prescribed label 或 source-switch 删除
某些组合时，矩形性失败。

**矩形乘积定理。** 在 (9) 与 (14) 下，完整算术 assignment 存在，当且仅当 (12)
成立，并且对每个请求子集 \(U\subseteq\mathcal R\)，

\[
\boxed{
\sum_{d\in\bigcup_{r\in U}\mathcal D(r)}b_D(d)\ge |U|,}
\tag{15}
\]

\[
\boxed{
\sum_{h\in\bigcup_{r\in U}\mathcal S(r)}b_S(h)\ge |U|,}
\tag{16}
\]

\[
\boxed{
\operatorname{rank}_V
\{v_a:a\in\bigcup_{r\in U}\mathcal A(r)\}
\ge |U|.}
\tag{17}
\]

**证明。** 必要性分别来自 deep/shallow 的 capacitated Hall 条件、线性拟阵的 Rado
条件和 target 计数。反向地，把每个 deep/shallow key 展开为其剩余容量个具名副本。
(15) 给出 deep 的不同副本代表 \(d_r\)，(16) 给出 shallow 的不同副本代表 \(h_r\)，
(17) 由 Rado 定理给出 column 的独立代表 \(a_r\)。遗忘副本标签后三组代表仍按同一个
请求索引；由矩形性，

\[
(d_r,h_r,a_r)\in\widehat{\mathcal E}_{\rm src}(r).
\]

再合并已经保留的 fixed-target 收费，即得完整 assignment。证毕。

如果当前只要求物理不重复而没有独立 column 请求，可删除 (17)。如果一个已证明的
source-class 合同把全部 source-side 冲突忠实压成单一 atom，则 (15)--(17) 相应退化
为该 atom 集上的普通 Hall 或 Rado；没有这种 conflict-faithful 合同时不得压缩。

矩形性假设不能删除。取两个请求、unit deep keys \(d_1,d_2\)、unit shallow keys
\(h_1,h_2\)、彼此互异且与 \(\{d_1,d_2\}\) 不交的 fixed target keys，以及独立
columns \(a_1,a_2\)，并令

\[
\widehat{\mathcal E}_{\rm src}(r_1)=\{(d_1,h_1,a_1)\},\qquad
\widehat{\mathcal E}_{\rm src}(r_2)=
\{(d_1,h_2,a_2),(d_2,h_1,a_2)\}.
\]

deep Hall、shallow Hall、column Rado 与 target 容量全部通过；但 \(r_1\) 的唯一
选择固定占用 \(d_1,h_1\)，而 \(r_2\) 的两个候选分别碰撞 \(d_1\) 与 \(h_1\)，所以
没有完整 assignment。这是

~~~text
NONRECTANGULAR_SOURCE_PROJECTION_FALSE_POSITIVE
~~~

两个请求若总共只有两个非空候选，则每个请求恰有一个；两个投影 Hall 会强制两条边
的 deep 与 shallow 均互异，因此三候选在该 unit 二请求模型中最小。

### 固定 \(D\) 的相位矩形特化

固定 \(D\) 与共同 source state \(S_0\)。对 owner index \(u\) 令
\(s(u)=\beta_J+q^Ju\)，并定义 lifted keys

\[
\kappa_D(u)=(S_0,s(u),q,J+1),\qquad
\kappa_S(u)=(S_0,s(u),q,J,D),
\]

\[
\Delta^{\rm key}
=\{\kappa_D(u):u\in\mathcal U_{\delta_J}\},\qquad
S_c^{\rm key}
=\{\kappa_S(u):u\in\mathcal U_{\delta_J+c}\}
\quad(c\in\mathbb F_q^\times).
\tag{18}
\]

若 \(m=|\mathcal R|\) 个请求只固定定向非零数字 \(c_r\)，所有
\(\kappa_D(u)\ne t(r)\)，且应用 (10b) 后每个 source 邻域恰为完整三维矩形

\[
\widehat{\mathcal E}_{\rm src}(r)
=\Delta^{\rm key}\times S_{c_r}^{\rm key}\times\mathcal A(r),
\tag{19}
\]

令 \(R_c=\#\{r:c_r=c\}\)。因为不同 \(S_c^{\rm key}\) 互不相交，(15)--(16)
精确化为

\[
\boxed{
m\le\sum_{d\in\Delta^{\rm key}}b_D(d),
\qquad
R_c\le\sum_{h\in S_c^{\rm key}}b_S(h)\quad(c\ne0).}
\tag{20}
\]

式 (19) 不能弱化成 deep--shallow 二维矩形后再单独检查 column Rado。作为抽象 unit
control，取
deep \(d_1,d_2\)、私有 shallow \(h_1,h_2\)、独立列 \(a_1,a_2\) 及互异且不与
deep 相交的 fixed targets，并令

\[
\begin{aligned}
\widehat{\mathcal E}_{\rm src}(r_1)
 &=\{(d_1,h_1,a_1),(d_2,h_1,a_2)\},\\
\widehat{\mathcal E}_{\rm src}(r_2)
 &=\{(d_1,h_2,a_2),(d_2,h_2,a_1)\}.
\end{aligned}
\]

两请求的 deep--shallow 投影分别是
\(\{d_1,d_2\}\times\{h_i\}\)，所以 (20) 通过；column 投影均为
\(\{a_1,a_2\}\)，故 (17) 也通过。但任何使用不同 deep 的选择都会选到相同 column，
所以没有 assignment。这给出严格回执

~~~text
FIXED_D_TWO_COORDINATE_RECTANGLE_FALSE_POSITIVE
~~~

原匿名公式使用 unit source-slot 容量，此时 (20) 正好化为
\(m\le|\Delta^{\rm key}|=n_{\rm deep}\) 与
\(R_c\le|S_c^{\rm key}|=n_{\delta_J+c}\)。这恢复并解释了
匿名 phase 容量公式的适用边界。target 已 prescribed 时先执行 (12) 与 (10a)；
(20) 还须与 column 条件 (17) 联合使用；无 column 约束时删除第三坐标及 (17)。
若 profile 把 (19) 删成非矩形子图，(20) 与 (17) 只剩必要投影，不能作为充分条件。
若存在 \(\kappa_D(u)=t(r)\)，必须回到带私有
\(\star_r\) 的一般式 (15)，不能套用本闭式。

## 5. 缺口对偶与 marked 下降边界

在矩形分支中，若 (12) 失败，输出纯 occurrence 回执

~~~text
PRESCRIBED_TARGET_OCCURRENCE_DEFICIT
~~~

它不产生 source annihilator。若 (15) 或 (16) 失败，输出带最小请求子集和邻域的
`DEEP_SOURCE_HALL_DEFICIT` 或 `SHALLOW_SOURCE_HALL_DEFICIT`。若 (17) 失败，令

\[
D_U=\operatorname{span}\{\rho_r:r\in U\},\qquad
V_U=\operatorname{span}\{v_a:a\in\bigcup_{r\in U}\mathcal A(r)\}.
\tag{21}
\]

有限维线性对偶给出精确判据

\[
\boxed{
\exists\lambda\in V^*:\quad
\lambda|_{V_U}=0,\qquad
\lambda|_{D_U}\ne0
\quad\Longleftrightarrow\quad
D_U\not\subseteq V_U.}
\tag{22}
\]

证明是在 \(V/V_U\) 上分离一个非零陪集再拉回。主定理的独立角色基前提给出
\(\dim D_U=|U|\)，所以 (17) 的失败 \(\dim V_U<|U|\) 强制
\(D_U\not\subseteq V_U\)，从而产生 (22)。若调用者没有先取独立需求基，则 Rado
缺口本身不充分：在 \(V=\mathbb F_\ell\) 中令两个相关需求都为 \(e_1\)，且
\(V_U=D_U=\langle e_1\rangle\)，有 \(\dim V_U=1<2\)，但不存在所需 \(\lambda\)。
此时输出 RADO_DEFICIT_WITHOUT_DEMAND_SEPARATION。

式 (22) 只有再通过 fixed-order 角色提升与全源列闭包

\[
\lambda(v_i)=0\qquad\text{对每个真实 source generator }v_i
\tag{23}
\]

时，才进入 annihilator 子群/商 relay。SOURCE-DOMINATING-CUT 是 (23) 的可计算
充分条件；否则输出 `SOURCE_COLUMN_ESCAPE`。

缺少 (23) 连抽象 relay 都不成立。用加法记号取

\[
V=H=\mathbb F_\ell^3,\qquad
R=\langle e_1,e_2\rangle,\qquad
\tau=e_2+e_3,\qquad
D_U=\langle e_2\rangle,\qquad
V_U=\langle e_1\rangle.
\tag{24}
\]

Rado 对偶 \(\lambda(x_1,x_2,x_3)=x_2\) 满足 (22)，却不湮灭遗漏的真实 source
\(e_2\)。在商中 source 已含非零像，并且 target 具有同一像，所以目标没有被分离。
事实上任何满足 (23) 的泛函都湮灭 \(D_U\subset R\)，因而不可能同时满足 (22)。
这是“Rado deficit 自动下降”的严格 no-go。

即使 (23) 给出严格有限群 relay，它也不是 marked 递降。仍须构造合法后继 \(T\)、
通过 E1--E3、给出全域

\[
\Phi_{T\to S}:W_T\longrightarrow W_S,
\tag{25}
\]

并证明预先定义且不可重置的全局势严格下降。现有 \(p=2113,D=70,x=14\) 控制的自然
较小余因子 \(241\) 具有空 marked fiber，且局部 \(70\to14\) 后仍可重新选择共同基
\(122\)；所以裸 target 变小或裸 \(D\) 变小均不能支付 E4/E5。

## 6. variable target 的投影 Hall 严格假阳性

式 (9) 是必要假设。若 target key 随候选变化，分别检查 source 与 target 投影 Hall
会丢失相关性。取两个请求 \(r_1,r_2\)、两个 unit source keys \(a,b\) 和两个 unit
target keys \(\alpha,\beta\)，候选为

\[
\begin{array}{c|cc}
&\text{candidate 1}&\text{candidate 2}\\ \hline
r_1&(a,\alpha)&--\\
r_2&(a,\beta)&(b,\alpha).
\end{array}
\tag{26}
\]

两个投影都满足每个请求子集的 Hall 条件。但 \(r_1\) 的唯一候选固定占用
\((a,\alpha)\)，而 \(r_2\) 的两个候选分别共享 \(a\) 与 \(\alpha\)，均不可行。这是

~~~text
VARIABLE_TARGET_PROJECTION_HALL_FALSE_POSITIVE
~~~

即使没有 shallow 或 column 约束也成立。两个请求若总共只有两个非空候选，则每个
请求恰有一个，两个投影 Hall 会直接使它们兼容；所以三候选最小。此时必须保留 (8)
的耦合超图或等价整数系统。

## 7. \(p=4441\)：匿名容量为正但命名 profile 删光 next-layer 边

取

\[
p=4441,\quad q=5,\quad J=1,\quad D=66,\quad
L=\mathbb Z,\quad X=\{0,1\},\quad\gamma(1)=2,\quad x=396.
\tag{27}
\]

\(p\equiv1\pmod {24}\) 为素数，且

\[
B_p=1110,\qquad
\beta_1=1,\qquad
\beta_2=21,\qquad
\delta_1=4.
\tag{28}
\]

固定 \(D=66\) 的槽字典为

\[
\begin{array}{c|c|c|c|c}
u&s&A&c&u\bmod5\\ \hline
13&66&1&66&3\\
79&396&6&11&4\\
145&726&11&6&0.
\end{array}
\tag{29}
\]

所以 \(u=79\) 是唯一 deep，另外两个是 shallow。deep selectable targets 恰为

\[
\mathcal T_2^{\rm sel}(66;4441)=\{121,396\},
\tag{30}
\]

相应 \((D_x,\operatorname{ord}_{4D_x}(5))\) 是 \((11,5),(66,10)\)。四个匿名候选
三元组恰为

\[
(79,13,121),(79,13,396),(79,145,121),(79,145,396),
\tag{31}
\]

故

\[
E_{\rm arith}=4,\qquad \nu_{\rm arith}=1.
\tag{32}
\]

但 \(\gamma(1)=2\) 强制 rank-one profile 满足

\[
u_1-u_0\equiv2\pmod5.
\tag{33}
\]

指定 \(x=396\) 后 \(D_x=66\)。穷尽 \(66\mid D\le1110\) 的规范槽字典：只有

\[
\mathcal U_1(66;4441)=\{13,79,145\},\qquad
\mathcal U_1(264;4441)=\{211\}
\tag{34}
\]

非空，其余十四个倍数全部为空。单槽 \(D=264\) 不能实现非零 role；在 \(D=66\)
中满足 (33) 的唯一有序 pair 是

\[
\boxed{(u_0,u_1)=(13,145),\qquad(s_0,s_1)=(66,726).}
\tag{35}
\]

两端相位为 \((3,0)\)，均为 shallow。因此 profile--canonical-base--prescribed-target
算术控制集非空且唯一，但加入 next-layer typed edge 后，该控制候选集为空：

\[
\boxed{\mathcal E_{\rm ctrl}=\varnothing.}
\tag{36}
\]

这在 occurrence、完整 role-SNF、E4 与 E5 之前严格反驳“匿名容量正即可支付带名
profile”。它是带名候选非空性或 singleton Hall 的失败；由于通过全部门后的投影也
为空，它本身不证明 (14) 的非空非矩形性。后者由上一节的三候选 source 控制严格证明。

## 8. \(p=10273\)：target 与 source occurrence 缺口可独立发生

取 \(p=10273,q=3,J=1,D=70\)，并在该接口控制中固定互异 state ids
\(S_0\ne T_0\)：全部 source slots 属于 \(S_0\)，全部 targets 属于 \(T_0\)。有

\[
\beta_1=2,\qquad\beta_2=8,\qquad\delta_1=2,
\tag{37}
\]

且固定基 slots 为

\[
\begin{array}{c|c|c|c|c}
u&s&A&c&u\bmod3\\ \hline
46&140&2&35&1\\
116&350&5&14&2\\
326&980&14&5&2\\
816&2450&35&2&0.
\end{array}
\tag{38}
\]

deep targets 是 \(35,98,350,980\)，故匿名容量为 \(\min(2,2,4)=2\)。考虑两个
带名 rank-one profile

\[
\begin{array}{c|c|c|c}
&X&u&\text{labels}\\ \hline
r_1&\{0,70\}&(46,116)&(140,350)\\
r_2&\{0,490\}&(326,816)&(980,2450).
\end{array}
\tag{39}
\]

它们的 deep 与 shallow slots 均互异。若二者使用同一个 target state 并都 prescribed
\(x=35\)，source-side 选择通过，但同一个 target key

\[
(T_0,35,3,2)
\tag{40}
\]

的载荷为 2、容量为 1，严格触发 (12)。把第二个 target 改为 350 后，尽管整数 350
也出现在 source 侧，\(S_0\ne T_0\) 使其 occurrence keys 互异；该接口的物理 matching
通过。

反过来，保留不同 targets \(35,350\)，但把第二条 edge 改为

\[
X=\{0,700\},\qquad u=(116,816),\qquad(s_0,s_1)=(350,2450),
\tag{41}
\]

则两个请求共享 deep occurrence \(s=350\)，target 割通过而 deep Hall 失败。这把
`PRESCRIBED_TARGET_OCCURRENCE_DEFICIT` 与 source-side 缺口严格分开。

这些是 canonical-profile/next-layer 到 occurrence 接口的算术控制，不是完整 F/G
states；真实调用仍须保存 prescribed-role SNF、完整 source table、E4 与 E5。

## 9. 统一选择器分派

~~~text
CANONICAL_PROFILE_PRESCRIBED_TARGET_READY
  preprocess historical occurrence ledger:
    exact full-key replay by the same assignment-id:
      mark satisfied without new charge
    partial overlap or different owner:
      preserve PHYSICAL_Q_LAYER_ASSIGNMENT_CAPACITY_OBSTRUCTED
  deduplicate only requests with identical role and identical physical obligations
  dependent role directions remain with distinct physical obligations:
    DEPENDENT_ROLE_PHYSICAL_COUPLING_REQUIRED
  physical-only branch:
    delete the column coordinate and preserve every physical obligation
  otherwise require the request directions themselves to be independent
  enumerate one-piece named witnesses through role-SNF and next-layer gates
  some request has no witness:
    preserve its first local obstruction
  otherwise:
    target key varies inside one request:
      VARIABLE_TARGET_COUPLED_HYPERGRAPH_REQUIRED
    target key is fixed:
      some target load exceeds shared occurrence capacity:
        PRESCRIBED_TARGET_OCCURRENCE_DEFICIT
      otherwise:
        build incremental deep charge:
          d equals its own target key:
            use private star_r; no second occurrence charge
          otherwise:
            charge residual b_O - m_T
        build source-side (incremental-deep, shallow, column) candidate system
        exact rectangularity fails:
          COUPLED_SOURCE_HYPERGRAPH_REQUIRED
        rectangularity passes:
          run deep Hall, shallow Hall and column Rado
          deep/shallow deficit:
            emit the corresponding minimal Hall cut
          column Rado deficit:
            compute D_U and V_U
            D_U is contained in V_U:
              RADO_DEFICIT_WITHOUT_DEMAND_SEPARATION
            D_U is not contained in V_U:
              emit lambda on the deficient request subset
              source-dominating closure fails:
                SOURCE_COLUMN_ESCAPE
              closure passes:
                ANNIHILATOR_SUBGROUP_OR_QUOTIENT_RELAY_CANDIDATE
          all gates pass:
            PRESCRIBED_TARGET_NAMED_ARITHMETIC_ASSIGNMENT
            E4 and non-resetting E5 remain mandatory
~~~

## 10. 研究边界

本卡把原先未定义的“实际耦合超图”拆成了精确层次。绑定 target state-id 与整数目标后，
target occurrence 可经 (10b) 的增量收费映射精确剥离；source 侧只有在完整矩形性
成立时才化成两组 Hall 和一组 Rado。三候选 source 控制证明矩形性不可省略，
\(p=4441\) 证明匿名正容量不保证带名候选非空，\(p=10273\) 则证明 target collision
与 source 缺口彼此独立。

它没有证明每个实际 F/G 请求的完整 witness 集非空，也没有解决非矩形 source
hypergraph 的全称匹配或相关角色与不同物理义务的双层耦合。Rado 对偶仍需全源列闭包，抽象有限群 relay 仍需整数后继、
marked E4 与不可重置 E5。下一决定性缺口是：从真实 F/G source table 证明候选
矩形性或直接处理其非矩形最小割；若失败，则把 \(p=4441\) 型 profile--phase 缺口、
source-column escape 或 target collision 转成完整 kernel source box、Type I/II
终端或严格 marked 下降。

## 聚焦验证

~~~bash
python3 reproductions/type_i_prescribed_target_occurrence_rado_contraction.py --verify
~~~

验证器只重算共享 occurrence 的增量收费、矩形乘积分派、二维 fixed-\(D\) 矩形与
三候选非矩形 source/variable-target 反例，以及两个算术接口控制；不运行历史扫描。
