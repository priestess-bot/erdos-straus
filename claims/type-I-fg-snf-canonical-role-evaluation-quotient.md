---
kind: claim
claim_id: type-I-fg-snf-canonical-role-evaluation-quotient
title: F/G source-SNF 的规范初等角色求值商与可见秩容量
statement: >-
  固定有限阿贝尔 ambient source group H、素数 q 和由 exact source contract
  封闭的源群 S。一个局部 q-标签同态 ell:S->F_q 可延拓为 H 上的初等角色，当且
  仅当 ell 在 S intersect qH 上为零；因此真实初等 source 空间是
  V_q=(S+qH)/qH，而不是 S/qS。对所有通过 ambient-extension 或 fixed-order SNF
  的 source-visible roles，令 R<=V_q^* 为其限制空间、N=R^perp；则
  R x (V_q/N) 的求值配对规范且完美，每条带 provenance edge e 的实现列就是
  kappa(e)(rho)=rho(u_e)。在 invariant-factor 坐标中，该列等于 lifted role 标签
  模 q 组成的 evaluation matrix 的对应列；它与 SNF lift 在 S 外的选择无关。
  因而请求子集 U 的真实角色容量是这些列的线性秩，是一个可计算的拟阵秩函数，
  并可直接代入 generalized Rado。若全部菜单在群像上生成封闭 source universe，
  总 evaluation rank 自动等于 dim R；总秩不足只能来自菜单未饱和、anchor-only
  方向误收费或 provenance 错配。C_4 中 S=<2g>、ell(2g)=1 给出局部相容但不可
  ambient 延拓的最小严格反例；C_2^2 给出 source universe 未闭合时 lift 选择影响
  新 edge 的严格反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-II-fg-universal-finite-source-map-completion
  - type-I-fg-marked-source-menu-saturation
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-raw-finite-abelian-source-lift-snf
  - type-I-fg-dependent-role-evaluation-rado-tensor-selector
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - source-SNF
  - finite-abelian
  - elementary-role
  - evaluation-pairing
  - quotient
  - Rado
  - matroid-rank
  - physical-capacity
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: exact-finite-source-universe
  - claim: type-I-fg-marked-source-menu-saturation
    role: marked-source-span-and-fixed-order-gate
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: lifted-source-role-input
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: invariant-factor-character-construction
  - claim: type-I-fg-dependent-role-evaluation-rado-tensor-selector
    role: generalized-rado-consumer
  - reproduction: reproductions/type_i_fg_snf_canonical_role_evaluation_quotient.py
    role: focused-extension-perfect-quotient-and-capacity-controls
visibility: public
last_checked: '2026-08-10'
---

# F/G source-SNF 的规范初等角色求值商与可见秩容量

## 1. 局部 source 标签必须先通过 ambient extension

固定有限阿贝尔群 \(H\)，以下用加法记号；固定素数 \(q\)。设一个已经由 exact
source contract 和带标记饱和门封闭的有限 source universe 为
\(\mathcal A\)，每条记录或带请求 edge \(e\) 携带同一 provenance 给出的群元素

\[
u_e\in H,
\qquad
S=\langle u_e:e\in\mathcal A\rangle\le H.
\tag{1}
\]

一个 q-primary role 的初等标签行是函数

\[
\lambda:\mathcal A\longrightarrow\mathbb F_q.
\tag{2}
\]

它先要通过纯 source relation 门：对任意整数系数 \(c_e\)，

\[
\sum_e c_eu_e=0\text{ in }H
\quad\Longrightarrow\quad
\sum_e c_e\lambda(e)=0\pmod q.
\tag{3}
\]

式 (3) 当且仅当 (2) 唯一下降为群同态

\[
\ell:S\longrightarrow\mathbb F_q,
\qquad
\ell(u_e)=\lambda(e).
\tag{4}
\]

但 (3) 仍不保证 \(\ell\) 是 ambient source group 上角色的限制。定义

\[
H_q=H/qH,
\qquad
V_q=\operatorname{im}(S\to H_q)
=\frac{S+qH}{qH}
\simeq\frac{S}{S\cap qH}.
\tag{5}
\]

**初等 ambient-extension 定理。** 存在

\[
\rho\in\operatorname{Hom}(H,\mathbb F_q),
\qquad
\rho|_S=\ell,
\tag{6}
\]

当且仅当

\[
\boxed{\ell(S\cap qH)=0.}
\tag{7}
\]

**证明。** 若 (6) 存在，则 \(\rho(qh)=q\rho(h)=0\)，故它在
\(S\cap qH\) 上为零。反之，(7) 使 \(\ell\) 下降为 \(V_q\) 上的线性泛函。
由于 \(V_q\) 是 \(H_q\) 的 \(\mathbb F_q\)-子空间，该泛函可延拓到
\(H_q\)；再与 \(H\to H_q\) 复合即得 (6)。证毕。

因此正确的 typed 回执是

~~~text
ELEMENTARY_ROLE_AMBIENT_EXTENSION_CERT
  ambient_group: H
  prime: q
  closed_source_span: S
  relation_consistency: lambda descends to ell:S->F_q
  ambient_cut: ell(S intersect qH)=0
  visible_source_space: V_q=(S+qH)/qH
~~~

若 (3) 失败，仍输出已有的 source-relation SNF obstruction；若 (3) 通过而 (7)
失败，则输出

~~~text
ELEMENTARY_ROLE_AMBIENT_EXTENSION_OBSTRUCTED
  witness: s in S intersect qH with ell(s) != 0
~~~

不能把局部 source 角色或任意复角色延拓当作 \(\mu_q\)-值 ambient role。

### fixed-order SNF 自动提供 (3) 与 (7)

若已有 fixed-order source-SNF 构造

\[
\chi:H\longrightarrow\mu_{q^a},
\qquad
\chi(u_e)=\zeta_{q^a}^{\lambda_a(e)},
\tag{8}
\]

则取初等化

\[
\chi(h)^{q^{a-1}}=\zeta_q^{\rho(h)}
\tag{9}
\]

得到 (6)，并且

\[
\boxed{\rho(u_e)=\lambda_a(e)\pmod q.}
\tag{10}
\]

所以 `F_FOURIER_SOURCE_TARGET_LIFTED` 的 source-visible 分支不需要再猜一个
role--column transport；SNF 的实际标签行模 \(q\) 已经给出它。若 (9) 在
\(S\) 上为零，则该分量是 anchor-only 或更高层记账，不属于当前 elementary
source-rank 请求。

## 2. lift 在闭合 source span 上唯一，在外部并不唯一

假设 (7) 通过，并固定一个延拓 \(\rho_0\)。全部 ambient 延拓组成仿射空间

\[
\rho_0+V_q^\perp
\subseteq H_q^*,
\qquad
V_q^\perp=\{\psi\in H_q^*:\psi|_{V_q}=0\}.
\tag{11}
\]

所以任意两个延拓在每个 \(u\in S\) 上取值相同。只要 source contract 已保证所有
eligible edge 都携带 \(u_e\in S\)，其 evaluation column 与 SNF 求解器选出的具体
ambient lift 无关。改变 invariant-factor 基、primitive root 或 SNF 自由变量不会
改变后续秩。

反之，若 source universe 未闭合并可能出现 \(u\notin S\)，两个延拓可在 \(u\)
上给出不同值。因此 `F_SOURCE_MAP_UNCLOSED` 或
`SOURCE_CONTRACT_EXACTNESS_UNPROVED` 不能仅凭已有行的一个 SNF 解升级为规范
edge evaluation。

## 3. 规范 perfect quotient

对同一素数 \(q\)，保留全部已经通过 (7) 或 fixed-order SNF 的 source-visible
角色限制，并令

\[
R=\operatorname{span}_{\mathbb F_q}
\{\rho_p|_{V_q}:p\in P\}
\le V_q^*,
\qquad
k=\dim R.
\tag{12}
\]

相关请求仍保留各自的物理义务；这里只在代数收费中取角色空间。定义右根基

\[
N_R=R^\perp
=\{v\in V_q:\rho(v)=0\text{ for every }\rho\in R\}
\tag{13}
\]

以及角色可见 source quotient

\[
K_R=V_q/N_R.
\tag{14}
\]

**规范求值商定理。** 配对

\[
\langle\ ,\ \rangle:
R\times K_R\longrightarrow\mathbb F_q,
\qquad
\langle\rho,v+N_R\rangle=\rho(v)
\tag{15}
\]

定义良好且完美。特别地，

\[
\boxed{
K_R\xrightarrow{\sim}R^*,
\qquad
v+N_R\longmapsto(\rho\mapsto\rho(v)).}
\tag{16}
\]

**证明。** \(N_R\) 的定义保证 (15) 定义良好且右侧非退化。左侧若有非零
\(\rho\in R\) 湮灭全部 \(K_R\)，它便湮灭 \(V_q\)，与
\(R\le V_q^*\) 矛盾。也可直接看出 (16) 的核是 \(N_R\)，而秩为

\[
\dim V_q-\dim N_R=\dim R=k;
\tag{17}
\]

故 (16) 是同构。证毕。

每条 edge 的规范 relation vector 与角色实现列分别为

\[
\bar u_e=u_e+qH+N_R\in K_R,
\qquad
\kappa(e)\in R^*,
\qquad
\kappa(e)(\rho)=\rho(u_e).
\tag{18}
\]

式 (16) 识别 \(\bar u_e\) 与 \(\kappa(e)\)。因此对任意 edge 集 \(X\)，

\[
\boxed{
\operatorname{rank}\{\kappa(e):e\in X\}
=\dim\frac{\operatorname{span}(\bar X)+N_R}{N_R}.}
\tag{19}
\]

裸 source quotient 中落在 \(N_R\) 的方向完全不可见，不能收费角色秩。

## 4. invariant-factor/SNF 矩阵公式

写

\[
H=\bigoplus_{\nu=1}^d C_{m_\nu},
\qquad
u_e=(c_{\nu e})_\nu,
\tag{20}
\]

并令

\[
I_q=\{\nu:q\mid m_\nu\}.
\tag{21}
\]

则 \(H_q\) 的规范 invariant-factor 坐标由 \(I_q\) 给出，source visible
matrix 是

\[
U_q=(c_{\nu e}\bmod q)_{\nu\in I_q,e\in\mathcal A}.
\tag{22}
\]

对第 \(p\) 个 fixed-order lift，令
\(y_{p\nu}\in\mathbb Z/q^{a_p}\mathbb Z\) 是 SNF 角色变量，即

\[
\chi_p(g_\nu)=\zeta_{q^{a_p}}^{y_{p\nu}}.
\tag{23}
\]

其 elementary coefficient row 是

\[
b_p=(y_{p\nu}\bmod q)_{\nu\in I_q}.
\tag{24}
\]

取这些行在 \(V_q\) 上限制的任一基 \(b_1,\ldots,b_k\)，定义

\[
\boxed{
E_R=BU_q,
\qquad
(E_R)_{p,e}=b_p(u_e)=\lambda_p(e)\pmod q.}
\tag{25}
\]

第 \(e\) 列正是 \(\kappa(e)\) 在对偶角色基下的坐标。若不显式保存
\(y_{p\nu}\)，直接把 closed source table 中的强制标签行模 \(q\) 排成矩阵并做
行消元，得到同一个 \(E_R\)。改变角色基只会把 (25) 左乘
\(\operatorname{GL}_k(\mathbb F_q)\)，所有列秩不变。

因此可输出有限回执

~~~text
SNF_CANONICAL_ROLE_EVALUATION_CERT
  prime: q
  ambient_invariant_factors: (m_nu)
  exact_source_universe: edge ids and provenance
  q_visible_source_matrix: U_q
  elementary_role_basis: B or basis label rows modulo q
  evaluation_matrix: E_R = B U_q
  role_radical: N_R = ker(B|V_q)
  edge_columns: e |-> E_R[:,e]
  role_rank: rank(E_R)
~~~

该回执完全由已有 source-SNF 和闭合 edge table 计算，不增加新的算术假设。

## 5. source 饱和自动给出总秩，颜色分配仍由 generalized Rado 决定

设全部物理请求的 column menus 为 \(A(p)\subseteq\mathcal A\)，并假设其群像联合
生成闭合 source span：

\[
\left\langle u_e:e\in\bigcup_{p\in P}A(p)\right\rangle=S.
\tag{26}
\]

带标记 source-menu saturation 蕴含 (26)，但 (26) 只使用其群像部分。由 (5)，
这些 edge 的 \(q\)-像张成 \(V_q\)；再由 (16)，

\[
\boxed{
\operatorname{rank}E_R[:,A(P)]=k.}
\tag{27}
\]

因此 closed source universe 上不会出现“所有候选合起来仍看不见某个 source-visible
role”的黑箱。若 (27) 失败，至少有一项输入声明错误：

1. 菜单群像没有生成 source universe，保留
   `MARKED_SOURCE_MENU_GROUP_ESCAPE`；
2. 一个只在 anchor/外部方向非平凡的角色被误计为 source-visible；
3. edge relation vector 与 source-SNF provenance 不来自同一记录。

对请求子集 \(U\subseteq P\) 定义实际角色容量

\[
c_R(U)
=\operatorname{rank}_{\mathbb F_q}
E_R[:,A(U)],
\qquad
A(U)=\bigcup_{p\in U}A(p).
\tag{28}
\]

\(c_R\) 是 normalized、monotone、submodular 的线性拟阵秩容量。令
\(n=|P|\)；相关角色求值选择器现在得到完全可计算的精确条件

\[
\boxed{
\exists\text{ 每请求恰选一列并支付 }R
\iff
c_R(U)+n-|U|\ge k
\quad(\forall U\subseteq P).}
\tag{29}
\]

失败割 \(U\) 的不可见角色空间在角色基坐标中就是

\[
Z_U=\ker E_R[:,A(U)]^{\mathsf T},
\qquad
\dim Z_U=k-c_R(U)>n-|U|.
\tag{30}
\]

其中每个非零向量都给出原 SNF-lifted elementary roles 的一个实际线性组合，故
\(Z_U\) 不再是抽象 source-column separator，而是规范 Fourier role subspace。
补集任意选定 \(n-|U|\) 列后，至多再切去同样多维，仍留下一个非零实际角色湮灭
完整选择。输出

~~~text
SNF_ROLE_EVALUATION_GENERALIZED_RADO_DEFICIT
  request_cut: U
  capacity: c_R(U)
  complement_budget: n-|U|
  invisible_role_basis: ker(E_R[:,A(U)]^T)
  source_labels: the corresponding combinations of SNF rows
~~~

该角色可依赖补集的具体选择，但失败割仍规范定义

\[
Q_U=K_R/\operatorname{span}E_R[:,A(U)],
\qquad
Q_U^*\simeq Z_U.
\tag{30a}
\]

若 \(m_U=\dim Q_U\)、\(r_U=n-|U|\)，任一完成至少留下
\(m_U-r_U\) 维角色 kernel，且最大正值精确等于最佳完整选择的缺秩。另一方面，
(27) 的 source saturation 蕴含不存在对所有完成统一有效的非零标量角色；正亏损割
若支配全部真实 source generators 又会强制 \(Q_U=0\)。因此 (30a) 是固定容量
quotient，不能直接调用当前 source state 的单角色 annihilator descent。详见
[广义 Rado 亏损的规范固定割商](type-I-fg-generalized-rado-fixed-quotient-defect.md)。

## 6. 四个严格控制

### 6.1 局部关系相容但 ambient extension 失败

取

\[
H=C_4=\langle g\rangle,
\qquad q=2,
\qquad S=\langle2g\rangle,
\qquad \ell(2g)=1.
\tag{31}
\]

\(\ell:S\to\mathbb F_2\) 是合法同态，且复角色 \(\chi(g)=i\) 在 \(2g\)
上取 \(-1\)。但

\[
S\cap2H=S,
\qquad
\ell(S\cap2H)\ne0,
\]

所以不存在 \(H\to\mathbb F_2\) 的延拓。它严格证明“无纯标记元/复角色可延拓”
不能替代 fixed-order 或 (7) 的 elementary ambient gate。它在 ambient 群阶上最小：
阶小于 4 时，平凡群和 \(C_2\) 的每个二值子群角色都显然可延拓，而奇阶群没有
非平凡 \(\mathbb F_2\)-角色。

### 6.2 source universe 未闭合时 lift 选择不规范

取 \(H=C_2^2\)、\(S=\langle e_1\rangle\)，并要求 \(\ell(e_1)=1\)。两个
ambient 延拓

\[
\rho_0(x,y)=x,
\qquad
\rho_1(x,y)=x+y
\]

在全部 \(S\) 上相同，但在新 edge \(e_2\notin S\) 上分别取 \(0,1\)。所以
closed source span 内的 evaluation 是规范的；未证明 source universe 完备时，
对外部 edge 则不是。

### 6.3 裸 source rank 可完全落入角色根基

仍取 \(H_q=C_2^2\)，但 \(R=\langle\rho_x\rangle\)。此时

\[
N_R=\langle e_2\rangle.
\]

裸 source vector \(e_2\) 的秩为一，而它在 \(K_R\) 中为零，evaluation rank
也为零。这是此前 raw-source-rank 假阳性的规范商解释。

### 6.4 三个物理请求、两个实际角色方向

取 \(H=C_4\oplus C_2\)、\(q=2\)，source rows 为 \(g_1,g_2\)，角色基为

\[
\rho_x(x,y)=x\pmod2,
\qquad
\rho_y(x,y)=y.
\]

三个物理请求的唯一 evaluation columns 依次为

\[
(1,0),(1,0),(0,1).
\]

矩阵总秩和 generalized Rado value 都为二，所以全部请求可保留并支付真实角色空间；
要求三个独立 source columns 会错误拒绝该分支。

## 7. 统一分派修正

~~~text
F_FOURIER_SOURCE_TARGET_LIFTED(q)
  exact source contract or closed source span unavailable:
    ROLE_TO_COLUMN_EVALUATION_UNPROVED
  source table closed:
    reduce every actual fixed-order SNF label row modulo q
    only local source relation consistency is known:
      test ell(S intersect qH)=0
      fail:
        ELEMENTARY_ROLE_AMBIENT_EXTENSION_OBSTRUCTED
    ambient elementary roles available:
      discard anchor-only zero restrictions
      build V_q, R, N_R and E_R
      edge lies outside certified source span or provenance mismatches:
        ROLE_TO_COLUMN_EVALUATION_UNPROVED
      all edges certified:
        SNF_CANONICAL_ROLE_EVALUATION_CERT
        total menu group span is not S:
          MARKED_SOURCE_MENU_GROUP_ESCAPE
        total span is S:
          rank(E_R)=dim R automatically
          run generalized Rado capacities c_R(U)
          deficit:
            GENERALIZED_RADO_FIXED_QUOTIENT_DEFECT
            save Q_U, Z_U and delta(U)
          pass:
            continue with physical deep/shallow/target gates
~~~

## 8. 研究边界

本卡关闭了 `ROLE_TO_COLUMN_EVALUATION_UNPROVED` 的一个实质分支：只要实际 F/G
状态已经有 exact finite source universe、每条 edge 的同源群坐标，以及 fixed-order
SNF lift 或等价的 ambient-extension 回执，角色--column pairing、右根基商和全部
evaluation ranks 都是规范可计算的，不再需要额外存在性假设。

它没有证明每个 F/G 状态都进入一个 exact source contract；也没有处理 edge 超出
闭合 source span、非矩形物理 hypergraph、跨不同素数角色的同一选择，或把 (30)
自动升级为整数 kernel source box、Type I/II 终端和不可重置 E5。规范固定割商已经
证明 source-dominating closure 不能在饱和正亏损割上直接发生；下一决定性缺口因而
进一步缩为：对实际 F/G edge 证明 source-universe/provenance 覆盖，并构造
exterior/determinantal 算术终端或保持目标与整数标签的 selected-source successor。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_fg_snf_canonical_role_evaluation_quotient.py \
  --verify
~~~

验证器只检查 \(C_4\)、\(C_2^2\)、\(C_4\oplus C_2\) 与
\(C_9\oplus C_3\) 的 ambient-extension、lift-independence、perfect quotient、
subset rank 和相关角色容量；不运行历史扫描。
