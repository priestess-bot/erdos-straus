---
kind: claim
claim_id: type-I-fg-fourier-to-type-II-role-demand-bridge
title: F/G Fourier 角色到 Type II 初等 q 请求的跨层分派
statement: 对固定层稳定子约化后的 F 型状态，取规范非平凡 Fourier 角色并分解其 q-primary 分量。若该分量在源指数支撑差分群上平凡，则它只是锚点/固定层相位，不产生 q 进源秩需求；若不平凡，则源差分群含有一个非零的 q 初等商，任何保持参数纤维的真实源关系格必须支付至少一个独立 q 方向，从而生成一个 typed SOURCE_RANK_DEMAND(q) 请求。若该请求没有经过独立整数 source-map 提升，则输出 FOURIER_ROLE_NO_ARITHMETIC_LIFT；若提升通过，则进入单 q 来源纤维的 CRT—前缀—稳定子闭包。G 型支撑外分离角色在源群上恒等，单独输出 G_SUPPORT_SEPARATION，不收费 Type II q 容量。该桥不声称角色需求自动给出整数 q-height。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-single-q-source-fiber-closure-trichotomy
topics:
- type-I
- F-state
- G-state
- finite-fourier
- q-primary
- source-rank
- Type-II
- cross-layer
- target-fiber
- capacity
- proof-program
sources:
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: canonical-F-G-role
  - claim: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
    role: q-primary-phase-data-and-no-lift-boundary
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: nonconstant-role-to-elementary-rank
  - claim: type-II-single-q-source-fiber-closure-trichotomy
    role: q-request-closed-dispatch
visibility: public
last_checked: '2026-08-10'
---

# F/G Fourier 角色到 Type II 初等 q 请求的跨层分派

## 1. 固定层 F/G 状态

设固定层约化后的源群为有限阿贝尔群 \(H\)，由源列
\(u_1,\ldots,u_r\) 生成；若有稳定子 \(P\)，以下均在商群
\(\bar H=H/P\) 中进行。令 \(J\subseteq\bar H\) 是固定层，\(Q\) 是目标指数纤维
在商群中的去重源支撑。定义

\[
\Delta_Q
=\left\langle\phi(z)\phi(z')^{-1}:z,z'\in Q\right\rangle,
\qquad
\Delta_J=\left\langle jj'^{-1}:j,j'\in J\right\rangle.
\tag{1}
\]

实际 Fourier 支撑为

\[
\mathcal S=J\cdot\phi(Q),\qquad
\phi(z)=\prod_i u_i^{z_i}.
\tag{2}
\]

有 \(\Delta_{\mathcal S}=\langle\Delta_Q,\Delta_J\rangle\)，但 \(\Delta_J\) 的
元素不自动是可回译的源关系；本桥只把 \(\Delta_Q\) 计入 Type II 源秩需求。

F 型表示数缺失时，规范 Fourier 证书给出一个非平凡角色
\(\chi\in\widehat{\bar H}\)。记

\[
m=\operatorname{ord}(\chi),\qquad
m=\prod_{\ell\mid m}\ell^{e_\ell}.
\tag{3}
\]

对每个 \(q\mid m\) 定义 q-primary 分量

\[
\chi_q=\chi^{\,m/q^{e_q}},
\qquad
\operatorname{ord}(\chi_q)=q^{e_q}.
\tag{4}
\]

若状态是 G 型，则存在一个外部角色 \(\psi\) 在 \(\bar H\) 上恒等、在目标陪集上
非恒等；G 型不使用 (4) 的源群角色。

## 2. 角色—源秩二分

对每个 \(q\mid m\)，先限制 \(\chi_q\) 到源支撑差分群 \(\Delta_Q\)。有两个互斥分支：

### 2.1 锚点/固定层相位

若

\[
\chi_q|_{\Delta_Q}\equiv1,
\tag{5}
\]

则 \(\chi_q\) 不分离任何源关系边；其非恒相位若存在，只来自固定层 \(J\) 或绝对
锚点，不能直接计入 Type II 源容量。
输出

\[
\mathrm{FIXED\_LAYER\_ONLY\_QPRIMARY}(q,e_q,\chi_q).
\tag{6}
\]

若 \(J\) 是单点，则该回执精化为
\(\mathrm{ANCHOR\_ONLY\_QPRIMARY}\)。该分支的 q 进源秩需求为零；不能把角色阶
\(q^{e_q}\) 当成 Type II q-height。

### 2.2 非恒相位与初等 q 请求

若

\[
\chi_q|_{\Delta_Q}\not\equiv1,
\tag{7}
\]

则源支撑差分群 \(\Delta_Q\) 含有非零 q-primary 分量，并且

\[
\boxed{
r_q(Q):=
\dim_{\mathbb F_q}
\bigl(\Delta_Q/q\Delta_Q\bigr)\ge1.
}
\tag{8}
\]

为选择器生成一个最小 typed 请求

\[
\mathfrak r_q(Q,\chi_q)
=\bigl(q,e_q,\chi_q|_{\Delta_Q},
\text{source columns},\text{relation basis}\bigr),
\tag{9}
\]

类型记为

\[
\mathrm{SOURCE\_RANK\_DEMAND}(q,r_q(Q)\ge1).
\tag{10}
\]

若 \(A_{\mathrm{src},q}\) 是保持当前参数纤维的真实源关系列在 q-primary 商中的
像，则

\[
\Delta_Q\le A_{\mathrm{src},q}
\quad\Longrightarrow\quad
\boxed{
\dim_{\mathbb F_q}(A_{\mathrm{src},q}/qA_{\mathrm{src},q})
\ge r_q(Q)\ge1.
}
\tag{11}
\]

所以任何声称 (7) 已由当前纤维产生的回执，若同时给出
\(\dim(A_{\mathrm{src},q}/qA_{\mathrm{src},q})=0\)，立即得到
\(\mathrm{SOURCE\_RANK\_INCONSISTENT}\)，而不是继续收费。

## 3. 定理证明

若 (5) 成立，则对任意固定层元素 \(j\in J\) 和任意
\(z,z'\in Q\)，有
\(\phi(z)\phi(z')^{-1}\in\Delta_Q\)，故
\(\chi_q(j\phi(z))=\chi_q(j\phi(z'))\)。因此 q-primary 分量在每个固定层陪集
上恒定，只可能贡献固定层/锚点因子，得到 (6)。

若 (7) 成立，存在 \(z,z'\in Q\) 使
\(\chi_q(\phi(z)\phi(z')^{-1})\ne1\)。该元素在有限阿贝尔群中的 q-primary 部分
具有非平凡像，所以 \(\Delta_Q\) 的 q-primary 分量非平凡。这等价于 (8)：有限
阿贝尔群的 q 初等商秩为零，当且仅当其 q-primary 分量平凡。

真实源关系列包含所有 \(\phi(z)\phi(z')^{-1}\)，因此
\(\Delta_Q\le A_{\mathrm{src},q}\)。子群的 q 初等商秩不超过母群，
得到 (11)。这也证明了 (9)--(10) 是一个不会重复收费的最小需求：pair-energy
边数可以很多，但至少需要的独立 q 方向只有 \(r_q\) 个。证毕。

## 4. 从角色请求到算术 q 请求

角色—源秩桥只产生 (9) 的有限群请求，不自动产生整数 q-height。对每个
\(\mathfrak r_q\)，选择器必须再运行独立 source-map 门：

1. 若有整数标签集合 \(\mathcal S_i(q)\)、相位同余和来源纤维，使
   \(\chi_q\) 的 q-primary 相位能提升为
   \(s_i\equiv\gamma_i\pmod{q^{e_i}}\)，则把请求附加到
   'FOURIER_PHASE_LIFTED'，并送入
   [Type II 单 q 来源纤维的 CRT—前缀—稳定子闭包三分](type-II-single-q-source-fiber-closure-trichotomy.md)；
2. 若相位同余在候选标签表中无解，输出
   'FOURIER_ROLE_NO_ARITHMETIC_LIFT'，保存 \(q,e_q,\chi_q\)、关系基和全部候选标签；
3. 若局部标签都可行但跨状态/同纤维容量匹配失败，输出
   'FOURIER_ROLE_ASSIGNMENT_DEFICIT'，并把最小 Hall 集作为后续 Type I/II 分派输入；
4. 若 source-map 尚未被证明是完备的，输出
   'FOURIER_ROLE_SOURCE_UNCLOSED'，不能把未枚举标签默认为不存在。

这四项把 Fourier 角色的“存在”与整数载体的“可回译”分开；只有第一项允许进入
q-prefix/Kneser 价格账本。

进入该账本后还必须区分请求数与前缀深度。一个规范 q-primary restriction 在本桥中
只产生一个最小请求；它的 source-SNF menu、角色阶 \(q^{e_q}\) 或某条整数载体的
depth-\(d\) 都不会生成新的 request id。若一个 unlayered named edge 通过估值移位、
范围和真实纤维门，它可以让这一个请求承载唯一的 depth-\(d\) Q-PREFIX lineage；
若调用压成同一循环方向的不同停止层 staircase，则所需 \(q-1\) 个 request ids 必须
由上游物理义务预先给出，先证明其角色 restriction 共线并保存允许的单位归一化，再
通过共同角色求值像与联合 SNF。精确判据见
[F/G q-prefix 的请求—深度分解、联合角色准入与 Jacobi 负陪集零入口](type-I-fg-qprefix-request-depth-admission.md)。

G 型分支更简单：若 \(\psi|_{\bar H}=1\)、\(\psi(t)\ne1\)，则所有源差分都被
\(\psi\) 湮灭，输出
\[
\mathrm{G\_SUPPORT\_SEPARATION},
\]
不生成 \(\mathrm{SOURCE\_RANK\_DEMAND}\)。这避免把 G 型本来已经完成的支撑外分离
错误地转成 Type II 容量请求。

规范 G-anchor 的 Jacobi 角色还有一个更窄的严格边界：在
\(\mathcal D_p^-\) 负 endpoint 菜单内部，全部带标记行位于同一个 Jacobi 负陪集，
故内部差分求值为零；角色本身阶为二，也不提供任何奇 q-primary 请求。该结论不覆盖
anchor-inclusive source universe、菜单外 raw exits 或其它奇阶角色；出现这些对象时
必须扩张 source contract，而不是向旧负 endpoint 子菜单收费。

## 5. 与 Fourier 预算和多 q 角色的关系

F 型 Fourier 幅度给出相位预算，但角色阶本身不等于 q-height。对所有
\(q\mid m\) 分别执行 (5)--(11)，得到一个 q 角色请求集合

\[
\mathcal R_{\mathrm{role}}
=\{\mathfrak r_q:\chi_q|_{\Delta_Q}\not\equiv1\}.
\tag{12}
\]

同一个 q 的多个角色只按
\[
\dim_{\mathbb F_q}
\left\langle
\chi_q|_{\Delta_Q}:
\mathfrak r_q\in\mathcal R_{\mathrm{role}}
\right\rangle
\tag{13}
\]
计数；相同 q 方向不能按角色数重复收费。不同 q 的请求只有在 source-map/CRT 明确
给出共同纤维时才能进入同一个 Kneser/Hall 图，不能因角色分解的形式互素而直接相加。

这与 F 型相位预算兼容：预算控制哪些 \(\chi_q\) 可能有较大振幅；(8)--(13) 则
控制一个相位真正需要多少独立源方向。二者分别是谱约束和算术需求，不能互换。

## 6. 构造性边界

### 6.1 G 型纯支撑分离

若 \(\bar H\) 是目标单位群的真子群，存在 \(\psi\) 在 \(\bar H\) 上恒等而在
目标上非恒等。所有 \(\Delta_Q\) 都被 \(\psi\) 湮灭，直接输出
\(\mathrm{G\_SUPPORT\_SEPARATION}\)，不产生 q 请求。

### 6.2 F 型纯锚点

若 \(Q\) 只有一个去重元素，则
\(\Delta_Q=1\)，任何 q-primary 角色都满足 (5)。即使固定层 \(J\) 有多个元素、
顶层 Fourier 系数非零，也没有源关系 q-height 需求；这包含 \(p=97\) 伪命中的
单点目标截面。

### 6.3 F 型一条真实 q 方向

取 \(\bar H=C_3\)、\(J=\{1\}\)、\(\phi(Q)=\{1,g\}\)，
\(\chi(g)=\exp(2\pi i/3)\)。则 \(m=q=3\)，
\(\Delta_Q=C_3\)，所以 \(r_3=1\)，输出一个
\(\mathrm{SOURCE\_RANK\_DEMAND}(3,1)\)。若 source-map 只提供标签集合
\(\{0\}\)，则随即输出 \(\mathrm{FOURIER\_ROLE\_NO\_ARITHMETIC\_LIFT}\)；
若提供标签 \(1\pmod3\)，才可继续进入 q-prefix 闭包。

### 6.4 源秩不一致

若回执声称 \(\phi(Q)=\{1,g\}\) 和非平凡三值角色，但当前参数纤维的真实源关系
列全部落在稳定子，因而 \(A_{\mathrm{src},3}/3A_{\mathrm{src},3}=0\)，则 (11) 直接
给出 \(\mathrm{SOURCE\_RANK\_INCONSISTENT}\)。不能用角色幅度填补缺失的整数源列。

## 7. 逻辑边界

本桥完成了 F/G 规范 Fourier 到 Type II 请求图的第一层跨域分派：

\[
\text{F/G role}
\longrightarrow
\begin{cases}
\text{G 支撑外分离};\\
\text{锚点-only，无源 q 需求};\\
\text{SOURCE\_RANK\_DEMAND}(q);\\
\text{明确的算术 no-lift/assignment 障碍}.
\end{cases}
\]

它仍不证明：\(\mathrm{SOURCE\_RANK\_DEMAND}\) 一定有整数 q-height、所有候选标签
都已枚举、或 q 请求闭包后必然命中/递降。剩余的决定性全称命题因此被缩小为：
证明 F 型非恒相位角色的 source-map 完备性，或证明
\(\mathrm{FOURIER\_ROLE\_NO\_ARITHMETIC\_LIFT}\) 能转成 Type I/F/G 或全局良基秩。
对单 F 请求，正向对象现在可进一步收紧为一个 depth-\((q-1)\) 的同纤维 typed
Q-PREFIX，而不是 \(q-1\) 个克隆请求；对规范 G/Jacobi 二阶角色，奇 q 入口已经严格
关闭，不能再作为该正向对象的候选。

多角色进入物理选择器前还须把
\(\langle\chi_q|_{\Delta_Q}\rangle\) 与每条带 provenance 的 source relation
放进同一求值配对；相关角色不能只取基后删除其余物理义务。若 finite source universe
已 exact、fixed-order SNF 已给出 ambient lifts，求值配对由标签矩阵模 \(q\) 和
\((S+qH)/qH\) 的规范商直接构造；见
[source-SNF 的规范初等角色求值商](type-I-fg-snf-canonical-role-evaluation-quotient.md)。
其后的精确 generalized Rado 条件见
[F/G 相关角色物理义务的求值配对、广义 Rado 与张量和选择器](type-I-fg-dependent-role-evaluation-rado-tensor-selector.md)。
