---
kind: claim
claim_id: type-I-odd-owner-incidence-edge-source-preserving-capacity
title: 奇阶 owner 关联边的来源保持规范化与精确一维秩容量
statement: >-
  固定奇素数 q、层 j 和核心素数 p。若两条带名源记录通过一个可复核整数规则产生
  不同横向数字的真实 q^j-prefix owner，并且横向数字与源相位满足同一个非退化仿射式，
  则这条来源合格的有向 owner 边在关联格商中可规范化为源列 1；该源列同时由真实
  余因子差分整数实现。取字典序最小的来源合格边作为唯一规范 token 后，关联
  token/slot 流、source-preserving 纤维一致性和 Rado 门对一个可达该边的 q-rank
  请求全部通过。所有同层横向边
  的规范源列仍共线，故该载体的精确源秩容量为 1；两个或更多独立请求必给严格
  OWNER_TRANSVERSE_SOURCE_RANK_DEFICIT。仅有仿射 phase-to-owner 指派而没有带名
  整数来源边时，必须输出 INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED。该证书支付
  additive source rank，不冒充 Type II 物理因子槽、因子积、终端或 E1--E5 递降。
  对 p=97,q=11，两个 endpoint 及其合并单位群均无 11-primary 部分，故关联 C_11
  到当前 endpoint 乘法 source 环境的直接同态 lift 严格为零。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-fiber-incidence-lattice-source-map
  - type-I-odd-fourier-owner-cylinder-transverse-rank-map
  - type-II-owner-source-preserving-fiber-uniformity-criterion
  - type-II-owner-arithmetic-menu-rado-fourier-closure
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-I
  - type-II
  - Fourier
  - owner
  - incidence-edge
  - source-provenance
  - source-preserving
  - Rado
  - q-primary
  - rank-capacity
  - strict-deficit
  - proof-program
sources:
  - claim: type-I-odd-owner-fiber-incidence-lattice-source-map
    role: incidence-lattice-and-integer-cofactor-realization
  - claim: type-I-odd-fourier-owner-cylinder-transverse-rank-map
    role: inversion-pair-integer-owner-construction
  - claim: type-II-owner-source-preserving-fiber-uniformity-criterion
    role: canonical-resource-fiber-uniformity-gate
  - claim: type-II-owner-arithmetic-menu-rado-fourier-closure
    role: flow-rank-and-factor-menu-separation
  - reproduction: reproductions/type_i_odd_owner_incidence_edge_source_preserving_capacity.py
    role: focused-positive-rank-deficit-provenance-and-endpoint-primary-no-go-controls
visibility: public
last_checked: '2026-08-10'
---

# 奇阶 owner 关联边的来源保持规范化与精确一维秩容量

## 1. 来源合格的关联边

固定奇素数 \(q\nmid p\) 和 \(j\ge1\)。沿用标准窗口

\[
\mathcal O_j(p)=\{s:0<4s<p,\ q^j\mid p+4s\}
\]

及其横向数字、规范 Type II 顶点和余因子

\[
\tau_j(s)=\frac{s-\beta_j(p)}{q^j}\pmod q,
\qquad v_s=(D_s,A_s),
\qquad N_s=\frac{p+4s}{q^j}.
\tag{1}
\]

设源记录集 \(X\) 带有第 \(q\) 层相位

\[
\gamma:X\longrightarrow\mathbb F_q.
\]

一条**来源合格的有向关联边**不是任意的二点相位匹配，而是一张有限回执

\[
\Pi=(x,y;\ \sigma_x,\sigma_y;\ \mathcal L;\ s_x,s_y;\ v_{s_x},v_{s_y}),
\tag{2}
\]

其中：

1. \(x,y\) 是带原始记录编号和算术数据的不同源记录，且
   \(\gamma(x)\ne\gamma(y)\)；
2. \(\mathcal L\) 是回执中明确登记的整数构造规则，它从
   \((\sigma_x,\sigma_y)\) 重新产生有序端点 \(s_x,s_y\)，而不是只按相位查表；
3. 两个端点逐项通过 \(s_x,s_y\in\mathcal O_j(p)\) 及规范
   \((D,A,C)\) 分解；
4. 存在同一 \(a\in\mathbb F_q^\times,c\in\mathbb F_q\) 使

\[
\tau_j(s_z)=a\gamma(z)+c
\qquad(z=x,y),
\tag{3}
\]

   且回执保存 \(a,c\)、两个端点高度及 \(N_{s_x},N_{s_y}\)。

条件 2 是来源语义门。只知道 owner 窗口覆盖相位的仿射像，或事后为每个相位挑选
一个合法 \(s\)，并不产生式 (2) 的回执。反过来，式 (2) 只把**整条边**绑定到原始
记录对；它不声称两个端点分别是两个可独立收费的 Type II 因子 token。

## 2. 规范源列与整数 realization

在 owner 顶点增广格 \(L_0\) 上，已有规范同态

\[
\Theta_j(e_{v_s}-e_{v_t})=\tau_j(s)-\tau_j(t)
=4^{-1}(N_s-N_t)\pmod q.
\tag{4}
\]

对来源合格边 \(\Pi\)，定义其相位标量和规范源列

\[
\lambda_\Pi=a\bigl(\gamma(x)-\gamma(y)\bigr)\in\mathbb F_q^\times,
\tag{5}
\]

\[
u(\Pi)=\lambda_\Pi^{-1}
\Theta_j(e_{v_{s_x}}-e_{v_{s_y}}).
\tag{6}
\]

由 (3) 逐差分，

\[
\Theta_j(e_{v_{s_x}}-e_{v_{s_y}})
=a\bigl(\gamma(x)-\gamma(y)\bigr)=\lambda_\Pi,
\]

故

\[
\boxed{u(\Pi)=1\in\mathbb F_q.}
\tag{7}
\]

再由 (4)，同一规范列具有真实整数表达

\[
\boxed{
u(\Pi)
=\frac{N_{s_x}-N_{s_y}}
       {4a(\gamma(x)-\gamma(y))}
=1\pmod q.}
\tag{8}
\]

式 (8) 中的除法只发生在 \(\mathbb F_q\)；分母非零由来源合格性保证。回执仍保存
\(\lambda_\Pi\)，所以规范化可逆，不会丢失原始边的方向或相位尺度。

这给出一个比“相位和横向数字同为一维”更强的结论：每条合格边的源列既来自
带名源记录，又由两个真实整数余因子的差实现。

## 3. 一个规范 token 的 source-preserving 闭合

设当前角色至少有一条来源合格边。按冻结的源记录编号、端点
\((s_x,s_y)\) 和构造规则编号排序，取最小边 \(\Pi_*\)。定义唯一规范 token

\[
t_*=(q,j,\Pi_*,\lambda_{\Pi_*},u(\Pi_*)=1)
\tag{9}
\]

及一个横向源槽 \(c^{\rm tr}_{q,j}\)，容量副本只取
\((c^{\rm tr}_{q,j},1)\)。该副本的完整签名为

\[
\eta_*=(j,\Pi_*,\lambda_{\Pi_*},1).
\tag{10}
\]

这里只有一个 token，故该关联槽的 source-preserving 纤维一致性不是假设，而是平凡
成立。对一个可达该边的 rank-one 请求 \(r\)：

\[
\mathsf F_{\rm tok}(\{r\})
=\mathsf F_{\rm slot}(\{r\})=1,
\qquad
\rho(\{r\})=\operatorname{rank}_{\mathbb F_q}\{1\}=1.
\tag{11}
\]

因此 token 流、投影流和 Rado 条件同时通过，构成

~~~text
TRANSVERSE_INCIDENCE_CANONICAL_RESOURCE_CERT
  resource_class = additive_incidence_source
  q_layer = (q,j)
  source_edge = Pi_*
  normalized_column = 1
  token_flow = slot_flow = source_rank = 1
  physical_owner_projection = unproved
~~~

选择最小边只为给出确定性充分证书；其它边仍保存在 provenance ledger 中，但不能因
标签不同而把同一个关联格商重复收费。这里的 slot 是由真实余因子差实现的加法
incidence source slot，不是某个 endpoint 内的物理因子 \(h\)。因此 (11) 不调用
Type II owner-token 的 physical-occurrence 投影门；该门必须等待实际因子掩码。

## 4. 精确一维容量与严格过载

由 (7)，任意来源合格边的规范源列都是 \(1\in\mathbb F_q\)。不做规范化时，它们的
列也是非零标量 \(\lambda_\Pi\in\mathbb F_q\)，仍全部落在同一条直线上。因此对仅由
固定 \((p,q,j)\) 横向关联格提供的任意请求子族 \(U\)，

\[
\boxed{
\rho_{q,j}^{\rm tr}(U)
\le \dim_{\mathbb F_q}\operatorname{im}\Theta_j
\le1.}
\tag{12}
\]

若至少一条来源合格非零边存在，右端等号成立；所以该载体的精确源秩容量为 1，而
不是 owner 数量或边数量。若 \(R=|U|\ge2\) 个请求被声明为线性独立，则 Rado 必要
条件在 \(U\) 上严格失败：

\[
\boxed{
\rho_{q,j}^{\rm tr}(U)=1<R,
\qquad
\mathrm{OWNER\_TRANSVERSE\_SOURCE\_RANK\_DEFICIT}(U,1,R).}
\tag{13}
\]

式 (13) 只断言这个横向载体不能支付第二个独立方向；若另有不同深度、不同素数或
独立 source-SNF 的真实列，它们必须作为新资源另行验证，而不能复制当前边。

若 \(\operatorname{im}\Theta_j=0\)，输出
'OWNER_WINDOW_RANK_DEFICIT'。若
\(\operatorname{im}\Theta_j\ne0\) 但没有式 (2) 的来源合格边，则输出

~~~text
INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED
~~~

而不能用一个 phase-only 完整仿射 lift 代替真实 token。

## 5. \(p=97,q=11\) 的来源保持正控制

取核心记录

\[
x_+=(1,0),\qquad x_-=(-1,0),
\qquad \gamma(x_+)=2,\quad\gamma(x_-)=9\pmod {11}.
\tag{14}
\]

它们的有理单项式为 \(5/1\) 与 \(1/5\)。令

\[
\sigma=5+1=6,
\qquad
\mathcal L_{\rm inv}(x_+,x_-)=(\sigma,\sigma+11)=(6,17).
\tag{15}
\]

这是带名反演对的整数构造，而非丢弃记录后按相位选择 owner。逐项有

\[
97+4\cdot6=121=11^2,
\qquad
97+4\cdot17=165=3\cdot5\cdot11,
\tag{16}
\]

\[
(D,A)=(6,1),(17,1),
\qquad
(\tau_1(6),\tau_1(17))=(0,1),
\tag{17}
\]

且共同仿射式为

\[
\tau_1=8\gamma+6\pmod {11}.
\tag{18}
\]

取方向 \(x_+\to x_-\)，则

\[
\lambda_\Pi=8(2-9)=10,
\qquad
N_6=11,\quad N_{17}=15,
\tag{19}
\]

\[
\Theta_1(e_6-e_{17})=10,
\qquad
u(\Pi)=10^{-1}\cdot10=1,
\tag{20}
\]

并且

\[
(11-15)\bigl(4\cdot8(2-9)\bigr)^{-1}=1\pmod {11}.
\tag{21}
\]

所以此前的 'PHYSICAL_SOURCE_PROVENANCE = partial_pair_only' 可以精确升级为

~~~text
EDGE_SOURCE_PROVENANCE = verified_inversion_pair
SOURCE_RELATION_SCOPE = one_edge
TRANSVERSE_SOURCE_CAPACITY = 1
INCIDENCE_FLOW_RADO = pass_for_one_request
ADJACENT_FIXED_BASE_QJ_SOURCE_CRT = obstructed_required_6_target_1
HETEROGENEOUS_EXTERNAL_PHYSICAL_FLOW = unproved
~~~

但两个端点的完整 Type II 因子菜单仍分别为空：
\(p+4s=121\) 的除数没有 \(-1\bmod24\)，
\(p+4s=165\) 的除数没有 \(-1\bmod68\)。当前乘法 source 环境还满足

\[
|U(24)|=8,\qquad |U(68)|=32,\qquad |U(408)|=128.
\tag{22}
\]

这些阶都与 11 互素，所以任意群同态

\[
C_{11}\longrightarrow U(24),\quad
C_{11}\longrightarrow U(68),\quad
C_{11}\longrightarrow U(408)
\tag{23}
\]

都平凡。换言之，两个实际 11 因子 occurrence 虽然存在，但它们在当前 endpoint
单位群商中的 11-primary 源列为零，不能通过这些单位群直接承载式 (20) 的非零
关联列。后续共同固定基定理还给出另一条独立 no-go：相邻标签 \(6,17\) 互素，故
同时容纳两端的固定源基只能是 \(D_0=1\)，其除子格目标只有
\(D_*=A=x=1\)；但 exact-11 source CRT 要求 \(x\equiv6\pmod {11}\)，所以在 E2
即严格失败。于是 \(p=97\) 有如下分层状态：

~~~text
DIRECT_ENDPOINT_UNIT_GROUP_LIFT = obstructed_no_11_primary
ADJACENT_FIXED_BASE_QJ_SOURCE_CRT = obstructed_required_6_target_1
HETEROGENEOUS_EXTERNAL_PHYSICAL_FLOW = unproved
~~~

共同固定基障碍覆盖所有 \(s_i=D_0a_i\)、\(D_*\mid D_0\) 的相邻边合同，但不排除
异质源基的外部 token，也不排除换用新模数、新状态或 external source-switch；因此
不能把这两个 no-go 外推为所有 physical-owner flow 的不可能性。

因此当前 \(q=11\) 关联边的准确状态仍是

~~~text
DIRECT_TERMINAL = false
STRICT_SOURCE_SWITCH = false
recursive_edge_eligible = false
~~~

这些字段只针对当前 \(q=11\) 关联边。素数 \(p=97\) 本身另有
\(s=2,h=7\) 的独立 Type II 终端；该终端不保留此 11 阶来源角色。

若把同一 11 阶横向载体复制给两个独立请求，式 (13) 立即给出
'OWNER_TRANSVERSE_SOURCE_RANK_DEFICIT(requests=2, rank=1)'。

## 6. 反控制与选择器位置

在 \(p=97,q=3,j=1\) 中，标准窗口覆盖全部三个横向数字，所以任意
\(\mathbb F_3\) phase support 都有抽象仿射顶点赋值。但如果输入没有登记一个从原始
记录算术数据产生两个端点的规则 \(\mathcal L\)，来源合格边集合仍为空，必须返回
'INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED'。这严格区分：

\[
\text{phase lift}\quad\not\Rightarrow\quad
\text{source-preserving edge token}.
\tag{24}
\]

终端优先的 odd-owner 分派由此细化为

~~~text
ODD_HALL_SOURCE_RANK(q,j)
  -> OWNER_WINDOW / SMALL_COFACTOR_TERMINAL_MENU
       -> terminal hit: TYPE_II_TERMINAL
       -> incidence rank 0: OWNER_WINDOW_RANK_DEFICIT
       -> incidence rank 1:
            -> no qualified arithmetic edge:
                 INCIDENCE_EDGE_SOURCE_PROVENANCE_OBSTRUCTED
            -> qualified edge:
                 TRANSVERSE_INCIDENCE_CANONICAL_RESOURCE_CERT
                 -> one independent request: INCIDENCE_FLOW_RADO_PASS
                 -> at least two independent requests:
                      OWNER_TRANSVERSE_SOURCE_RANK_DEFICIT
                 -> global D1 raw menu (already terminal-first):
                      hit: unreachable_here / TYPE_II_TERMINAL already returned
                      empty -> adjacent common-fixed-base menu:
                        beta_j(p) != 1:
                          ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED
                        beta_j(p) = 1:
                          ADJACENT_EDGE_FIXED_BASE_QJ_PHYSICAL_OCCURRENCE
                          DIRECT_TARGET_U4_Q_PRIMARY_LIFT_OBSTRUCTED
                          NO_D1_SINGLE_FACTOR_RAW_OR_STRICT_D_EDGE
                 -> nonadjacent / heterogeneous source base:
                      common-base square target menu
                      endpoint cofactor residues always collide
                      -> exclusive q^(j+1) layer inherited by target:
                           arithmetic-ready physical {1,q} block
                           provenance + global occurrence assignment required
                           freely selectable q-role exists iff q | ord_{4D_*}(q)
                           prescribed role still requires joint SNF/eta
                      -> otherwise: direct next-layer lift obstructed
                      -> E4 / marked lift / global E5 still required
~~~

该定理关闭的是 \(p=97\) 一条反演边的来源保持、规范化和加法单 rank 容量门。后续
[奇阶相邻 owner 边的共同固定基塌缩、终端与源秩障碍](type-I-odd-owner-adjacent-edge-fixed-base-physical-lift-dichotomy.md)
已精确完成相邻边的共同固定基子问题：共同算术行基必塌缩到 1，且 exact-\(q^j\)
source CRT 可解当且仅当
\(\beta_j(p)=1\)。因此 \(p=97\) 当前边得到 E2 障碍；正分支只得到目标处真实
\(q^j\) occurrence，而 \(U(4)\) 无奇 \(q\)-primary，不能承载当前源列。独立的
\(D=1\) 单因子 raw 菜单已由 terminal-first 预检；菜单空时仍缺非同态 factor-toggle、
异质源基接口，或严格、可提升的跨纤维下降。后续
[非相邻共同基下一层 lift](type-I-odd-owner-nonadjacent-common-base-next-layer-lift.md)
已关闭一个非相邻正子类：全部共同基目标由 \(x\mid D_0^2\) 穷尽，cofactor residue
路线严格碰撞，但唯一 deep endpoint 被目标继承时，独占的 \(q^{j+1}\) 层给出真实
\(\{1,q\}\) arithmetic-ready block。只有输入边已经 provenance-qualified，且
source/target 两个不含 edge id 的全局 occurrence key 均未占用时，才能登记 verified
source-class token；局部 \(D_*<D_0\) 仍不自动升级为 E5，所以不适用于这里的
\(p=97\) 相邻 E2 反控。

## 7. 对抗边界

本定理有四个不可删除的限制。

1. \(\mathcal L\) 必须是可复算的整数规则，并保存原记录数据；只读取
   \(\gamma(x)\) 后查找 owner 的规则不合格。
2. \(p=97\) 的正例证明的是一个反演 edge receipt。它不把全部十条 negative 记录
   提升为 owner 顶点，也不证明一个全局 source homomorphism。
3. 规范化只按非零标量重标一维源列，保持线性秩；它不创造第二个 q-primary 层。
4. incidence slot 是加法余因子差资源。没有 endpoint 因子
   \(h\equiv-1\pmod {4D}\) 及 E1--E3 时，不得送入 Type II physical-owner flow；
   没有 E4/E5 时不得登记递归边。

因此最强反驳“给任意 phase map 命名一个 lift rule 就得到物理 Type II 容量”不成立：
条件 1 排除 phase-only 命名，条件 2 限定来源范围，条件 4 明确阻断物理因子结论。
在 \(p=97\) 控制中，式 (22)--(23) 把经当前 endpoint 单位群的直接乘法 source
lift 收紧为严格不可能；共同固定基定理又在当前 \(p=97\) 边上排除了全部
\(D_*\mid D_0\) 的目标 occurrence。一般相邻正分支仍只排除直接 \(U(4)\)
q-primary 同态 lift；非相邻边的独占下一层子类在 provenance 与全局 occurrence
分配门通过时现已关闭 physical E1，但异质源基、
其它非相邻高度型、换状态与全局 E5 仍未闭合。

## 聚焦验证

~~~bash
python3 reproductions/type_i_odd_owner_incidence_edge_source_preserving_capacity.py --verify
~~~

该 verifier 只重算 \(p=97,q=11\) 的来源边、规范源列、单请求 incidence
flow--Rado 通过、endpoint 11-primary no-go、双请求秩缺口，以及 \(q=3\) 的
phase-only 来源阻塞；不运行历史扫描。
