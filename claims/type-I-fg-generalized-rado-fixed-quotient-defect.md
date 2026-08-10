---
kind: claim
claim_id: type-I-fg-generalized-rado-fixed-quotient-defect
title: F/G 广义 Rado 亏损的规范固定割商、精确亏格与标量递降边界
statement: >-
  固定 source-SNF 产生的 perfect evaluation pairing R x K_R 和 n 个非空物理
  请求菜单。对请求割 U，令 W_U 为 U 的全部 evaluation columns 的张成空间，
  Q_U=K_R/W_U，m_U=dim Q_U，r_U=n-|U|。则 Q_U 是湮灭 U 菜单的规范最大线性商，
  Q_U^* 规范同构于不可见角色空间 Z_U；任一完整选择在 Q_U 中只能由补集的 r_U
  条列生成，故其余维数至少为 delta(U)=m_U-r_U。更强地，最优完整选择的精确
  秩亏格满足 k-nu=max_U delta(U)，而每个 delta(U)>0 的割使每次具体完成至少留下
  delta(U) 维角色湮灭空间。若全部菜单已生成 K_R，则不存在对所有完成统一有效的
  非零标量角色；若 U 还支配全部真实 source generators，则 Q_U 必为零，因而不可能
  同时是亏损割。故固定 Q_U 是 completion-independent 容量证书，但不能直接升级为
  当前饱和 source state 的单角色 quotient descent。F_2^3 的三请求非零列系统给出
  最小严格例：固定二维 Q_U 存在，而两个完成的标量湮灭角色不同且公共交为零。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-dependent-role-evaluation-rado-tensor-selector
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-I-II-fg-universal-finite-source-map-completion
  - type-II-annihilator-two-sided-subgroup-quotient-descent
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - generalized-Rado
  - evaluation-pairing
  - quotient
  - exact-defect
  - exterior-power
  - annihilator
  - scalar-no-go
  - physical-capacity
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-dependent-role-evaluation-rado-tensor-selector
    role: generalized-rado-min-max-formula
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: canonical-perfect-evaluation-space
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: exact-source-universe-and-total-span
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: scalar-source-closed-relay-boundary
  - reproduction: reproductions/type_i_fg_generalized_rado_fixed_quotient_defect.py
    role: focused-fixed-quotient-defect-no-common-scalar-and-tight-controls
visibility: public
last_checked: '2026-08-10'
---

# F/G 广义 Rado 亏损的规范固定割商、精确亏格与标量递降边界

## 1. 规范割商

固定素数 \(q\)，以及由 closed source-SNF table 构造的 perfect pairing

\[
\langle\ ,\ \rangle:
R\times K_R\longrightarrow\mathbb F_q,
\qquad
K_R\simeq R^*,
\qquad
k=\dim R=\dim K_R.
\tag{1}
\]

每个物理请求 \(p\in P\) 有一个非空有限菜单
\(\mathcal A(p)\subseteq K_R\)。其中的向量就是带 provenance edge 的规范
evaluation columns \(\kappa(e)\)，而不是裸 source vectors。令

\[
n=|P|,
\qquad
W_U=
\operatorname{span}_{\mathbb F_q}
\bigcup_{p\in U}\mathcal A(p)
\le K_R
\tag{2}
\]

并定义割 \(U\subseteq P\) 的规范固定商

\[
\boxed{
Q_U=K_R/W_U,
\qquad
m_U=\dim Q_U=k-\dim W_U.}
\tag{3}
\]

这里“固定”表示 \(Q_U\) 只依赖完整菜单和割 \(U\)，不依赖补集请求最终选哪条
edge。它也是湮灭 \(U\) 菜单的最大商：若一个线性映射

\[
f:K_R\longrightarrow Y
\tag{4}
\]

在 \(\bigcup_{p\in U}\mathcal A(p)\) 上为零，则 \(W_U\subseteq\ker f\)，故
存在唯一 \(\bar f:Q_U\to Y\) 使 \(f=\bar f\circ\pi_U\)。因此任何其它固定线性
quotient 证书都是 \(Q_U\) 的因子。

由于 (1) 完美，商对偶规范等于不可见角色空间：

\[
\boxed{
Q_U^*
\simeq
W_U^\perp
=
Z_U
=
\{\rho\in R:
\rho(a)=0\text{ for every }a\in\mathcal A(p),\ p\in U\}.}
\tag{5}
\]

这把此前仅作为一个 kernel basis 输出的 \(Z_U\) 提升为一个不依赖坐标的固定
source-evaluation quotient。

## 2. 固定 quotient 亏损定理

给定完整选择

\[
\sigma(p)\in\mathcal A(p)
\qquad(p\in P),
\tag{6}
\]

令补集请求预算

\[
r_U=n-|U|.
\tag{7}
\]

因为 \(p\in U\) 的所选列都落在 \(W_U\)，它们在 \(Q_U\) 中为零。故全部选择
在 \(Q_U\) 中的像由至多 \(r_U\) 个补集向量生成：

\[
\operatorname{rank}
\{\pi_U(\sigma(p)):p\in P\}
\le r_U.
\tag{8}
\]

定义割亏格

\[
\boxed{
\delta(U)
=m_U-r_U
=k-\dim W_U-(n-|U|).}
\tag{9}
\]

若 \(\delta(U)>0\)，则每个完整选择都满足

\[
\operatorname{codim}_{Q_U}
\operatorname{span}
\{\pi_U(\sigma(p)):p\in P\}
\ge\delta(U),
\tag{10}
\]

从而在原 evaluation space 中

\[
\operatorname{rank}
\{\sigma(p):p\in P\}
\le k-\delta(U)<k.
\tag{11}
\]

对偶地，把补集选择限制在 \(Z_U\) 上得到

\[
\operatorname{ev}_{\sigma,U}:
Z_U\longrightarrow\mathbb F_q^{P\setminus U},
\qquad
\rho\longmapsto
\bigl(\rho(\sigma(p))\bigr)_{p\notin U}.
\tag{12}
\]

其定义域维数为 \(m_U\)，值域维数为 \(r_U\)，所以

\[
\boxed{
\dim\ker \operatorname{ev}_{\sigma,U}
\ge m_U-r_U
=\delta(U).}
\tag{13}
\]

因此亏格不只保证“每个完成有一个角色”：亏格为 \(d\) 时，每个具体完成至少留下
\(d\) 个线性独立的实际 SNF-role combinations 湮灭全部所选列。这个 kernel
subspace 可以随 \(\sigma\) 改变，但承载它的 \(Q_U^*=Z_U\) 是固定的。

### exterior/determinantal 形式

若 \(m_U>r_U\)，则

\[
\bigwedge^{m_U}
\operatorname{span}
\{\pi_U(\sigma(p)):p\in P\}
=0,
\qquad
\bigwedge^{m_U}Q_U\ne0.
\tag{14}
\]

等价地，任取 \(Q_U\) 的基，补集选择矩阵的全部 \(m_U\) 阶 minors 都为零，而
\(Q_U\) 自身有非零 top exterior space。但这没有增加 rank 以外的信息：
\(\bigwedge^{m_U}S=0\) 当且仅当 \(\dim S<m_U\)，且 top wedge 不能区分亏格一与
更高亏格。determinant 在 \(m_U\ge2\) 时也不是完成元组加法群上的同态。因此
式 (14) 只能记为 `EXTERIOR_RANK_RESTATEMENT_NO_ARITHMETIC_GAIN`；完整 no-go
及唯一保留的目标依赖 Plücker 分离见
[top-exterior 的秩重述与 Plücker 边界](type-I-fg-exterior-fourier-plucker-boundary.md)。

## 3. 精确全局亏格公式

令

\[
\nu=
\max_{\sigma(p)\in\mathcal A(p)}
\operatorname{rank}
\{\sigma(p):p\in P\}.
\tag{15}
\]

广义 Rado 阈值定理给出

\[
\nu=
\min_{U\subseteq P}
\bigl(\dim W_U+n-|U|\bigr).
\tag{16}
\]

从 (3)、(7) 和 (9) 直接得到

\[
\boxed{
k-\nu
=\max_{U\subseteq P}
\bigl(m_U-r_U\bigr)
=\max_{U\subseteq P}\delta(U).}
\tag{17}
\]

右端自动非负，因为 \(U=P\) 给出
\(\delta(P)=k-\dim W_P\ge0\)。所以不需要人为取 positive part。式 (17) 说明
\(\delta\) 不是松上界：最大割亏格恰好等于最佳完整选择仍缺失的角色维数。

特别地，全部角色可支付当且仅当

\[
\delta(U)\le0
\qquad(\forall U\subseteq P).
\tag{18}
\]

若 total menu span 已由 source saturation 证明为 \(W_P=K_R\)，则
\(\delta(P)=0\)，真正的正亏格只能来自菜单颜色/物理请求在真割上的集中，而不是
总 source rank 不足。

## 4. 饱和分支没有 completion-independent 标量角色

现在假设每个菜单非空且

\[
\boxed{W_P=K_R.}
\tag{19}
\]

若某个固定角色 \(0\ne\rho\in R\) 对每一个完整选择都湮灭全部所选列，则对任意
候选 \(a\in\mathcal A(p)\)，固定选择 \(a\)，并在其它非空菜单中任取列，即得
\(\rho(a)=0\)。所以 \(\rho\) 湮灭全部候选，继而

\[
\rho\in W_P^\perp=K_R^\perp=\{0\},
\tag{20}
\]

矛盾。因此：

\[
\boxed{
W_P=K_R
\Longrightarrow
\text{不存在对所有 completion 统一有效的非零标量 annihilator}.}
\tag{21}
\]

对固定割也可写成

\[
Z_U\cap
\left(
\operatorname{span}
\bigcup_{p\notin U}\mathcal A(p)
\right)^\perp
=W_P^\perp
=\{0\}.
\tag{22}
\]

式 (13) 与 (22) 并不冲突：前者对每个完成给出至少 \(\delta(U)\) 维 kernel，
后者说这些 kernels 的全体公共交在饱和分支中为零。\(Q_U\) 正是保留这种“固定
高维空间、移动标量 kernel”信息的最强线性 quotient。

## 5. SOURCE-DOMINATING 与正亏格严格不相容

令 \(\mathcal S\subseteq V_q\) 是 exact source universe 的真实生成元，并令
\(\bar{\mathcal S}\subseteq K_R\) 为其规范 evaluation 像。closed source-SNF
构造保证

\[
\operatorname{span}\bar{\mathcal S}=K_R.
\tag{23}
\]

若割 \(U\) 在此前 relay 的意义下支配全部真实 source generators，即

\[
\bar{\mathcal S}\subseteq W_U,
\tag{24}
\]

则 (23)--(24) 强制

\[
W_U=K_R,
\qquad
Q_U=0,
\qquad
\delta(U)=-r_U\le0.
\tag{25}
\]

因此在 exact、饱和、source-visible 的当前状态中：

\[
\boxed{
\delta(U)>0
\Longrightarrow
U\text{ 不是 SOURCE-DOMINATING-CUT}.}
\tag{26}
\]

这给出一个此前没有显式记录的接口 no-go。广义 Rado 亏损不能直接送入
`type-II-annihilator-two-sided-subgroup-quotient-descent`：该 relay 要求一个
非零标量角色湮灭后继状态的全部真实 source generators，而 (21) 排除当前饱和状态
上的共同标量，(26) 排除亏损割自身自动完成 source domination。

\(Q_U\) 是 elementary source **capacity quotient**，不是有限目标状态
\(H/K\) 的整数递降。把两者写成同一个“quotient descent”会丢失 source set 和
target preservation 条件。

## 6. 最小非零列严格控制

取

\[
K_R=\mathbb F_2^3
=\langle e_1,e_2,e_3\rangle,
\qquad
P=\{p_1,p_2,p_3\},
\tag{27}
\]

菜单为

\[
\mathcal A(p_1)=\mathcal A(p_2)=\{e_1\},
\qquad
\mathcal A(p_3)=\{e_2,e_3\}.
\tag{28}
\]

所有列均非零，且 total menu span 是 \(K_R\)。取
\(U=\{p_1,p_2\}\)，则

\[
W_U=\langle e_1\rangle,
\qquad
Q_U\simeq\mathbb F_2^2,
\qquad
m_U=2,
\qquad
r_U=1,
\qquad
\delta(U)=1.
\tag{29}
\]

选择 \(e_2\) 时，完整所选列的 annihilator 是
\(\langle e_3^*\rangle\)；选择 \(e_3\) 时则是
\(\langle e_2^*\rangle\)。二者公共交为零，全部候选的 annihilator 也为零；
但固定 quotient 始终是 \(K_R/\langle e_1\rangle\)，一个补集请求不可能生成其
二维空间。

在“\(n\ge k\)、全部菜单列非零、total menu span 为 \(K_R\)、亏损割非空”的
条件下，该例在请求数上最小。若 \(n\le2\)，则 \(k\le n\)；唯一可能的非空真割
在 \(n=2\) 时有 \(r_U=1\)，而非零菜单给
\(\dim W_U\ge1\)，故 \(m_U\le k-1\le1=r_U\)，不能严格亏损。

### 严格不等号的紧边界

仍取 \(K_R=\mathbb F_2^3\)，但令

\[
\mathcal A(p_1)=\{e_1\},
\qquad
\mathcal A(p_2)=\{e_2\},
\qquad
\mathcal A(p_3)=\{e_3\}.
\tag{30}
\]

对 \(U=\{p_1,p_2\}\)，有 \(m_U=r_U=1\) 和
\(\delta(U)=0\)；补集列 \(e_3\) 正好生成 \(Q_U\)，完整选择秩为三。因此
\(m_U>r_U\) 的严格性不可放松为 \(m_U\ge r_U\)。

同一严格例在任意素数 \(q\) 上成立；聚焦 verifier 同时检查 \(q=2,3\)，但证明
不依赖有限枚举。

## 7. 正确的后继接口

规范分派应改为：

~~~text
SNF_CANONICAL_ROLE_EVALUATION_CERT
  total menu span is not K_R:
    MARKED_SOURCE_MENU_GROUP_ESCAPE
  total menu span is K_R:
    compute W_U, Q_U and delta(U) for every request cut
    all delta(U) <= 0:
      ROLE_EVALUATION_PHYSICAL_ASSIGNMENT
    some delta(U) > 0:
      GENERALIZED_RADO_FIXED_QUOTIENT_DEFECT
        request_cut: U
        fixed_quotient: Q_U = K_R / W_U
        quotient_dimension: m_U
        complement_budget: r_U
        exact_defect: delta(U)
        dual_role_space: Q_U^* = Z_U
        top_exterior: rank restatement only
      do not emit a global scalar annihilator
      do not call current-state SOURCE_DOMINATING relay
      build the physically feasible completion set Omega
      propose fixed successor overhead X <= Q_U
      dim(X) < delta(U):
        GRASSMANN_SLICE_CAPACITY_CERT
        residual_capacity: delta(U) - dim(X)
      dim(X) >= delta(U):
        SELECTED_SOURCE_OVERHEAD_EXHAUSTED
~~~

从这里得到整数终端或递降还需要一个新的实质输入，合法路线只有：

1. 若实际算术目标提供固定秩目标平面，检查其 Plücker line 是否严格落在 reachable
   span 外，并另证高阶相位的 arithmetic realization；裸 top exterior 已被严格排除；
2. 构造固定后继开销 \(X\) 且证明
   \(\dim X<\delta(U)\)。此时
   [Grassmann 切片容量定理](type-I-fg-exterior-grassmann-slice-successor-descent.md)
   给出 \(\delta(U)-\dim X\) 维共同角色和正比例可行完成，再由
   `SELECTED_SOURCE_OVERHEAD_RANK_CERT` 与独立实现的 exact successor 接入
   子群--商二分；
3. 若 (19) 其实失败，回到 source-universe/menu escape，补齐 provenance 后重算，
   而不是把未饱和造成的共同 annihilator 记作递降。

第 1--2 项仍须逐项通过 ambient character lift、source labels、target phase、
SNF/CRT、\(B'>A\) 与 E1--E5。缺少这些输入时，唯一正确回执是

~~~text
FIXED_QUOTIENT_TO_INTEGER_DESCENT_UNPROVED
~~~

## 8. 研究边界

本卡把 generalized-Rado deficit 从“补集选完后才知道一个非零角色”推进为三个固定、
精确的对象：规范最大割商 \(Q_U\)、等于最佳选择真实缺秩的全局亏格 (17)，以及每个
完成至少 \(\delta(U)\) 维的角色 kernel。它同时证明当前饱和 source state 上不存在
统一标量 annihilator，且正亏损割不可能 source-dominating，从而关闭了一条看似自然
但逻辑上不可行的直接递降路线。

后续结果已经关闭裸 top-exterior 终端路线，并对任意非矩形可行完成集证明
Grassmann branch cover。真正剩余的新数学现在是构造一个由实际 arithmetic
provenance 产生、满足 \(\dim X<\delta(U)\) 的 selected-source successor，并证明
全源列闭包、目标保持和整数 E1--E5；或从不可避免的
\(\dim X\ge\delta(U)\) 开销下界导出 Type I/II 终端或另一良基下降。跨素数共用
选择仍不由本卡处理。

## 聚焦验证

~~~bash
python3 \
  reproductions/type_i_fg_generalized_rado_fixed_quotient_defect.py \
  --verify
~~~

验证器只检查二元/三元域严格例、两个移动的一维 completion kernels、公共标量
no-go、\(m_U=r_U\) 紧边界、相关请求通过例与精确公式 (17)；不运行历史扫描。
