---
kind: claim
claim_id: type-I-fg-qprefix-request-depth-admission
title: F/G q-prefix 的请求—深度分解、联合角色准入与 Jacobi 负陪集零入口
statement: >-
  对一个 source-visible 的规范 F 型 q-primary 角色，Fourier--source-rank 桥只生成
  一个最小物理请求记录；source-SNF 菜单的列数、角色阶 q^e、q-height 深度 d 和
  occurrence 层数都不能把该请求克隆。若一条实际带名边经整数载体与
  candidate-fiber q-block binding 提升，
  它可以作为一个请求承载唯一 depth-d Q-PREFIX lineage，d>=q-1 时可饱和一个显式
  C_q 商，但在该单例请求子系统中角色秩和请求数仍均为一。若改走声明压成同一循环方向的 q-1 请求
  staircase，则这些请求必须预先具有不同 request id，且其角色 restriction 经允许的
  单位归一化后属于同一固定一维线 L；给定边向量 u_a 和归一化非零值 c_a，存在一个
  共同角色实现全部边，当且仅当 c 属于 evaluation map L -> F_q^(q-1) 的像。
  q-单位 scalar copies 在任一共同整数仿射映射下具有相同
  q-估值，严格不能形成连续停止层。另一方面，规范 G-anchor/Jacobi 负 endpoint 菜单
  的所有 theta_delta=K delta 都在同一 Jacobi 负陪集，故该菜单内 source 差分和
  divisor-factor raw edges 均落入角色核；这个二阶角色不能为任何奇 q 提供
  q-primary staircase 入口。纳入 anchor 或跨出该陪集的 raw row 必须扩张 source
  contract，不能向负 endpoint 子菜单收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-empty-fiber-target-odd-source-demand
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-I-fg-dependent-role-evaluation-rado-tensor-selector
  - type-I-source-lattice-qheight-exclusive-tail-kernel-relay
  - type-I-f-target-involution-fourier-phase-collapse
  - type-i-target-odd-qprefix-direct-owner-no-go
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - q-primary
  - q-prefix
  - source-SNF
  - request-depth
  - Jacobi-symbol
  - physical-capacity
  - strict-obstruction
  - proof-program
sources:
  - claim: type-i-empty-fiber-target-odd-source-demand
    role: actual-p73-empty-F-fiber-and-target-odd-role
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: one-minimal-request-per-canonical-role-restriction
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: canonical-role-edge-evaluation
  - claim: type-I-source-lattice-qheight-exclusive-tail-kernel-relay
    role: single-lineage-depth-and-layered-staircase-carriers
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: exact-G-Jacobi-negative-endpoint-menu
  - reproduction: reproductions/type_i_fg_qprefix_request_depth_admission.py
    role: focused-request-depth-joint-role-and-Jacobi-zero-controls
  - reproduction: reproductions/type_i_fg_qprefix_block_bound_first_overflow.py
    role: same-p-actual-F-full-C3-binding-and-p73-strict-no-go
visibility: public
last_checked: '2026-08-10'
---

# F/G q-prefix 的请求—深度分解、联合角色准入与 Jacobi 负陪集零入口

## 1. 四个不可互换的量

固定奇素数 \(q\)。对已经通过 exact source contract、ambient extension 与
source-SNF 的 F/G 请求系统 \(P\)，对任意请求子系统 \(P_0\subseteq P\) 分别记

\[
n_{\mathrm{req}}(P_0)
=\#\{\text{\(P_0\) 中 content-deduplicated physical request ids}\},
\tag{1}
\]

\[
k_{\mathrm{role}}(P_0)
=\dim_{\mathbb F_q}
\langle\rho_p:p\in P_0\rangle,
\qquad
d_{\mathrm{pref}}(P_0)
=\text{一个 typed Q-PREFIX lineage 的深度},
\tag{2}
\]

以及 \(c_{\mathrm{occ}}(P_0)\) 为同一 source/target ledger 上可同时用于 \(P_0\) 的
互异 occurrence 键数。这里 \(\rho_p\) 是请求实际携带的 source-visible elementary
role。全部比较都在同一个 \(P_0\) 内进行；不得用单例子系统的秩覆盖全局角色秩。

这四个量没有默认等式。具体地：

1. 一个请求可有任意多候选 source-SNF columns，但完整 assignment 对该请求只选一列；
2. 多个带不同物理义务的请求可携带同一个角色，所以
   \(n_{\mathrm{req}}(P_0)>k_{\mathrm{role}}(P_0)\) 合法；
3. 一个 depth-\(d\) receipt 可有 \(d\) 个内部绝对层键，但 shared-q ledger 只登记
   一个 block lineage；
4. 角色求值向量相同不允许复用 source、target 或 layer occurrence。

因此菜单列数、pair-energy 边数、角色阶 \(q^e\)、q-height 和 occurrence 数都不能
增加 \(n_{\mathrm{req}}(P_0)\) 或 \(k_{\mathrm{role}}(P_0)\)。反过来，相关请求可以
共享代数秩，但不能删除其物理义务。

## 2. 单个 F 角色的请求—深度分解

令 \(V_q\) 是闭合 source universe 的初等可见商，
\(\rho\in V_q^*\) 是一个非零的规范 F 型 q-primary 初等角色。假设带 provenance 的
实际 source edges \(e\) 的向量 \(u_e\in V_q\) 生成当前源差分空间。于是至少存在
一条边满足

\[
c_e:=\rho(u_e)\ne0.
\tag{3}
\]

否则 \(\rho\) 湮灭全部生成元，与 source-visible 矛盾。按固定 source-table 顺序取
第一条满足 (3) 的边，得到规范带名边 \(e_\rho\)。

Fourier--source-rank 桥为该规范 restriction 生成一个最小
'SOURCE_RANK_DEMAND(q)' 请求。式 (3) 可以为该请求建立非空 column menu；它不会为
菜单中的每条边再生成请求。若同一角色原本已经附着于多个不同 target/occurrence
义务，那些 request ids 必须由上游合同显式给出，不能从 (3) 推造。

令该最小请求为 \(\mathfrak r_\rho\)，并只取单例子系统
\(P_\rho=\{\mathfrak r_\rho\}\)。以下秩等式只属于 \(P_\rho\)；当前完整系统中可以同时
存在其它独立角色。

令 \(\delta\) 是 \(e_\rho\) 的整数源格差向量，

\[
\operatorname{content}(\delta)=q^t g_0,
\qquad q\nmid g_0,
\qquad \rho(\delta)=c\in\mathbb F_q^\times.
\tag{4}
\]

若该请求尚未绑定层，则对任意

\[
J\ge\max(1,t),\qquad d\ge1
\tag{5}
\]

既有估值移位构造给出一个确定的 depth-\(d\) 整数算术候选：deep source 与 target
至少到 \(J+d\) 层，shallow source 精确停在 \(J\)，且归一化差值实现 \(c\)。这一步
仍必须通过当前 \(p\) 的范围、共同规范 source base、prescribed target、联合 SNF、
source-switch、`CANDIDATE_FIBER_QBLOCK_BOUND`、prefix lineage 与 occurrence 门。
终局 target residue、完整积、\(B'>A\) 和 `FIBER_REALIZED` 在 typed prefix 之后检查，
不能作为本步前提。

所有门通过时，准确回执为

\[
\boxed{
n_{\mathrm{req}}(P_\rho)=1,\quad
k_{\mathrm{role}}(P_\rho)=1,\quad
\#\{\text{\(P_\rho\) 的 lineages}\}=1,\quad
d_{\mathrm{pref}}(P_\rho)=d.
}
\tag{6}
\]

其唯一块为

\[
B_d=\{1,q,\ldots,q^d\}.
\tag{7}
\]

式 (6) 是本卡的请求—深度分解定理：深度不生成请求或角色秩。若显式 cyclotomic
商中 \(q\) 的像阶为 \(q\)，则 \(d\ge q-1\) 时 (7) 覆盖 \(C_q\)；这仍只是一个
请求承载的 full-cycle lineage。若任一 typed 门失败，只能输出
'FG_QPREFIX_SINGLE_LINEAGE_ADMISSION_UNPROVED' 或相应严格范围回执。

## 3. 多请求 staircase 的联合角色充要门

现在另给 \(h=q-1\) 个预先存在且两两不同的物理请求；第 \(a\) 个请求携带非零
source-visible restriction \(\rho_a\) 与指定值
\(c_a^{\mathrm{req}}\in\mathbb F_q^\times\)。若要把它们压成角色秩一的同一循环方向，
必须先给出

~~~text
COMMON_ROLE_LINE_CERT
  common_line: L=<rho_0> <= V_q^*
  request_roles: rho_a
  normalization_units: alpha_a in F_q^x with rho_a=alpha_a rho_0
  normalization_is_allowed_by_each_request_contract: true
~~~

也就是

\[
\langle\rho_1,\ldots,\rho_h\rangle
=L,\qquad \dim L=1.
\tag{8}
\]

若请求合同固定了角色的绝对归一化而不允许单位换基，则证书还必须固定同一个
\(\rho_0\)，不能只保存角色线。把原指定值按同一证书改写为共享坐标

\[
\widetilde c_a=\alpha_a^{-1}c_a^{\mathrm{req}}.
\tag{8a}
\]

以下令共同允许角色空间 \(\Gamma=L\)，并把 \(\widetilde c_a\) 简记为 \(c_a\)。
为每个请求选定一条带名候选边 \(u_a\in V_q\)，定义联合求值映射

\[
E_U:\Gamma\longrightarrow\mathbb F_q^h,
\qquad
E_U(\rho)=(\rho(u_1),\ldots,\rho(u_h)).
\tag{9}
\]

若 'COMMON_ROLE_LINE_CERT' 失败，即使较大的角色空间中存在某个角色实现全部数字，
也不能删除原请求的独立角色义务；必须保留完整 role--request evaluation matrix 并
运行 generalized Rado/耦合超图。

**联合角色准入定理。** 存在一个共同角色 \(\rho\in\Gamma\) 同时满足

\[
\rho(u_a)=c_a\qquad(1\le a\le h)
\tag{10}
\]

当且仅当

\[
\boxed{c=(c_1,\ldots,c_h)\in\operatorname{im}E_U.}
\tag{11}
\]

等价地，对每个 \(\lambda\in\mathbb F_q^h\)，

\[
\boxed{
\sum_a\lambda_a u_a\in\Gamma^\perp
\quad\Longrightarrow\quad
\sum_a\lambda_a c_a=0.
}
\tag{12}
\]

这里

\[
\Gamma^\perp
=\{v\in V_q:\rho(v)=0\text{ for every }\rho\in\Gamma\}.
\tag{12a}
\]

**证明。** (11) 是线性方程 (10) 的像判据。对标准点积取正交补，
\(c\in\operatorname{im}E_U\) 当且仅当 \(c\) 湮灭
\(\ker E_U^{\mathsf T}\)。而

\[
\lambda\in\ker E_U^{\mathsf T}
\iff
\rho\left(\sum_a\lambda_a u_a\right)=0
\quad(\forall\rho\in\Gamma),
\]

即左侧和向量属于 \(\Gamma^\perp\)。这正是 (12)。证毕。

“每条边分别有某个角色实现”不蕴含 (11)。最小反例取

\[
q=3,\quad
V_q=\mathbb F_3,\quad
\Gamma=V_q^*,\quad
u_1=u_2=1,\quad
c=(1,2).
\tag{13}
\]

两条方程分别可解，但共同方程要求同一个数同时为 \(1\) 和 \(2\)。此时
\(\lambda=(1,-1)\) 使 \(u_1-u_2=0\in\Gamma^\perp\)，而
\(c_1-c_2=-1\ne0\)，严格违反 (12)。

还必须防止“先在大角色空间求出共同角色，再删除原角色义务”。取

\[
V_q=\mathbb F_3^2,\qquad
\rho_1(x,y)=x,\qquad \rho_2(x,y)=y,
\qquad u_1=e_1,\quad u_2=e_2,\quad c=(1,1).
\tag{13a}
\]

在 \(\Gamma=V_q^*\) 中，\(\rho=x+y\) 使 (11) 通过；但
\(\langle\rho_1,\rho_2\rangle\) 维数为二，所以 'COMMON_ROLE_LINE_CERT' 失败。
这两个请求必须保留 rank-two 义务并回到完整 evaluation-Rado，不能登记 rank-one
staircase。

式 (11) 通过后仍只完成共同角色门。一个
'FG_QPREFIX_STAIRCASE_ADMISSION_CERT' 还必须保存：

~~~text
distinct_request_ids
common_role_line_cert_and_normalization_units
common_role_space_and_evaluation_matrix
desired_evaluation_vector_and_joint_solution
joint_integer_source_map_or_joint_SNF
consecutive_layer_full_matching
common_candidate_fiber_qblock_binding_and_block_lineage
source_and_target_occurrence_ledger
prescribed_target_and_source_switch_receipts
~~~

缺少 request ids 输出 'FG_STAIRCASE_REQUEST_DEFICIT'；角色线证书失败输出
'FG_STAIRCASE_ROLE_LINE_MISMATCH'；(11) 失败输出
'FG_STAIRCASE_JOINT_ROLE_OBSTRUCTED'；其它门缺失保持
'FG_STAIRCASE_INGRESS_UNPROVED'。已有 staircase 的算术 skeleton 只消费这些请求，
不生成这些请求。

## 4. q-单位 scalar copies 的过滤层严格 no-go

设多条候选关系只是同一关系的 q-单位倍数

\[
\delta_a=n_a\delta,
\qquad q\nmid n_a,
\tag{14}
\]

并由同一个整数仿射 source map 实现。令 \(L_{\mathrm{lin}}\) 为其线性部分。若
\(L_{\mathrm{lin}}(\delta)=0\)，全部 endpoints 已经重合，不能形成 staircase；否则

\[
v_q(L_{\mathrm{lin}}(\delta_a))
=v_q(n_aL_{\mathrm{lin}}(\delta))
=v_q(L_{\mathrm{lin}}(\delta))
\tag{15}
\]

对每个 \(a\) 相同。因此这些 scalar copies 不可能分别精确停在
\(J,J+1,\ldots,J+q-2\)。即使它们在同一个一维角色上都非零，也只能输出
'FG_STAIRCASE_FILTERED_STAR_OBSTRUCTED'。真正的 staircase 必须提供不同过滤高度的
关系；不能由一个 SNF 非零列或其 q-单位 copies 伪造。

## 5. target-odd F 入口必须使用非零仿射偏移

若目标是对合 \(\tau=-1\)，则任意奇 q-primary 分量在目标上的加法相位满足

\[
2\gamma(\tau)=0,
\qquad
\boxed{\gamma(\tau)=0.}
\tag{16}
\]

而真实 owner 中心为

\[
\beta_e(p)=-p4^{-1}\pmod {q^e},
\qquad \beta_e(p)\ne0.
\tag{17}
\]

所以 identity map \(s=\gamma\) 不可能进入 q-prefix。第 2 节的估值移位载体用
\(\beta_{J+d}(p)\) 作为 deep/target 的非零仿射中心，再用边差实现 \(c\)；它绕开的
是 identity 同余冲突，不是 source provenance、范围或 candidate-fiber 门。特别地，不能把
\(p=73\) 的真实 F 请求与另一个 \(p\) 上的算术正控制拼成一张已实现证书。

## 6. G/Jacobi 负 endpoint 菜单的零入口

固定规范 G-anchor

\[
R=p-2,\qquad K=(p-1)^2/4,\qquad Q=(p-3)/2
\tag{18}
\]

及 Jacobi 角色 \(\chi_R\)。只在已经声明的负 endpoint 菜单

\[
\mathcal D_p^-=
\{\delta:\delta\mid Q,\ \chi_R(\delta)=-1\}
\tag{19}
\]

中讨论。对其物理行，沿用无损标记 \(M_\delta,t_\delta\) 并定义

\[
\theta_\delta=M_\delta t_\delta^{-1}\pmod R.
\tag{20}
\]

实际行恒等式给出

\[
\theta_\delta\equiv K\delta\pmod R.
\tag{21}
\]

规范 G-anchor 又有 \(\chi_R(K)=1\)，故

\[
\boxed{\chi_R(\theta_\delta)=-1
\quad(\delta\in\mathcal D_p^-).}
\tag{22}
\]

因此该菜单内部的 source 差分生成群满足

\[
\Delta_{\mathrm{Jac}}^-=
\left\langle
\theta_\delta\theta_{\delta'}^{-1}:
\delta,\delta'\in\mathcal D_p^-
\right\rangle
\le\ker\chi_R.
\tag{23}
\]

若菜单内有 divisor-factor raw edge
\(\delta\xrightarrow{\ell}\ell\delta\)，两个端点都在 (19)，则

\[
\chi_R(\ell)
=\chi_R(\ell\delta)\chi_R(\delta)^{-1}=1.
\tag{24}
\]

所以规范 Jacobi role 在负 endpoint 菜单内的全部 source-edge evaluations 都为零。
更基本地，这个角色阶为二，根本没有奇 q-primary 分量；对每个奇 staircase prime
\(q\)，都没有非零 \(c_a\in\mathbb F_q^\times\) 可交给第 3 节。于是

\[
\boxed{
c_{\mathrm{ingress}}^{G,\mathrm{Jac},-}(q)=0
\qquad(q\text{ odd}).
}
\tag{25}
\]

这是 'G_JACOBI_NEGATIVE_ENDPOINT_MENU_ODD_QPREFIX_INGRESS_ZERO'，不是“尚未找到 lift”。
它不削弱 'G_SUPPORT_SEPARATION'：Jacobi 角色仍分离目标陪集，只是不产生奇 q
source 请求。

本结论不覆盖完整 raw 图。若把 anchor \(\delta=1\) 纳入 source universe，则
\(\theta_1=K\) 是 Jacobi-positive，而
\(\theta_\delta\theta_1^{-1}=\delta\) 对负 \(\delta\) 为 Jacobi-negative；此时
二进 source rank 可以非零。菜单外 raw exits 也可能跨陪集。此类扩张必须输出
'G_JACOBI_SOURCE_COSET_ESCAPE' 并重建 source universe，不能登记为旧负 endpoint
子菜单中的非零列。本结论也不排除另一个独立的 odd-order source-visible 角色或全新
raw-to-fiber adapter。

## 7. 聚焦控制

### 7.1 一个真实 F 角色、一个请求、一个深前缀候选

取真实空纤维控制

\[
p=73,\qquad R=27,\qquad K=493=17\cdot29.
\tag{26}
\]

以 \(2\) 为 \(U(27)\simeq C_{18}\) 的生成元，有

\[
(\log_2 17,\log_2 29)=(15,1),
\]

而指数盒 \(\{-1,0,1\}^2\) 的像坐标为

\[
\{0,1,2,3,4,14,15,16,17\}.
\tag{26a}
\]

目标 \(-1\) 的坐标为 \(9\)，故目标不在盒像而在其生成群中。规范 target-odd
character index \(1\) 按仓库固定的 CRT 投影坐标给出
\(u\mapsto2u\pmod9\)，初等求值为 \(u\mapsto2u\pmod3\)。这与以
\(\zeta_9\) 为基的指数坐标只差共同单位 \(2\)，不改变秩、非零边或像判据。三个剩余类
在 (26a) 中各出现三次，所以 36 条无序 pair 中恰有

\[
36-3\binom{3}{2}=27
\tag{26b}
\]

条非零 evaluation edges；但这些值仍张成一维角色空间，Fourier 桥只生成一个最小
请求。取反向实际源边 \((0,1)\to(0,0)\)，其 exponent 差 content 为 1、初等求值为
1，可作为规范 carrier 输入。27 条边不能生成第二个 request id。

原 empty-fiber 回执按最小素因子只登记 \(q_*=2\)；本控制使用的是随后 all-q
Fourier--role bridge 对角色阶 \(18=2\cdot3^2\) 的逐素数分解。它证明同一规范角色的
q=3 restriction 非平凡，不声称旧的最小-\(q_*\) 回执已经登记 q=3。

这个实际请求虽能在 \(p=73\) 自身形成 depth-2 candidate binding，却不能升级为
typed prefix。允许合法的 \(x=s_0\) 后，全部范围/高度/角色候选仍只有

\[
(J,x,s_0,s_1)=(1,2,2,5),(1,2,2,14),(2,2,2,11),
\tag{26c}
\]

三项的 source canonical bases 都不同；target \(U(8)\) 也没有 3-primary 方向。因此
这里得到严格的 `CANONICAL_COMMON_SOURCE_BASE_PROFILE_EMPTY`，不是把请求与别的素数
拼接。

另一方面，同一 actual F 状态上的正控制取

\[
p=557281,\quad R=199,\quad q=3,\quad J=1,\quad d=2.
\tag{27}
\]

这里 \(K=2\cdot5\cdot11^3\cdot2083\)，模 \(199\) 的指数盒遗漏目标但生成整个单位群。
显式 `EXPLICIT_TARGET_ODD_INDEX_43` digest 选择 \(j=43\)，其 exact Dirichlet
乘积大于 \(8>c(1)=3\)，3-primary 阶为 \(9\)，实际 factor-\(2\) edge 的初等值为
\(1\)。同一 \(p\) 上的 source rows
\(19838,138866\)、target \(182\) 和整数 source line 通过全部 candidate-fiber 与
occurrence 门，故现在严格得到一个 typed \(\{1,3,9\}\) full-\(C_3\) lineage，不再是
跨素数的 conditional pairing。它仍不是终局 `FIBER_REALIZED`：target numerator
\(558009=3^4\cdot83^2\) 的全部因子模 \(728\) 均不为 \(-1\)。完整证明见
[F 请求的 candidate-fiber q-prefix 绑定与首个越界短缺口分派](type-I-fg-qprefix-block-bound-first-overflow-terminal.md)。

### 7.2 两请求 staircase 的正、反控制

在 \(V=\mathbb F_3^2\) 中取

\[
u_1=e_1,\quad u_2=e_2,\quad
\Gamma=\langle(x,y)\mapsto x+y\rangle,\quad c=(1,1).
\tag{28}
\]

(11) 通过，两个不同 request ids 可共享一个角色秩。已有
\(p=673184521\) 算术 staircase 分别在 base \(1,2\) 停止并使用不同层键；在所有
typed 门通过后才得到一个 \(\{1,3,9\}\) lineage。把 (28) 改成 (13)，则逐边可解而
联合角色门严格失败。

### 7.3 真实 target-odd 与 G/Jacobi 控制

对 \(p=73,R=27,K=493,q=3,e=2\)，target phase 为
\(0\pmod9\)，owner center 为 \(2\pmod9\)，直接入口为空。

对 \(p=5281\)，有

\[
R=5279,\quad K=6969600,\quad Q=2639,\quad
\mathcal D^-=\{7,91,203,2639\}.
\tag{29}
\]

四个 \(\theta_\delta\) 全部 Jacobi-negative，菜单内四条边的标签 \(13,29\) 全部
Jacobi-positive。故朴素边数虽为四，规范 G/Jacobi evaluation rank 仍严格为零。
\(p=5281\) 另有 terminal-first gap-7 叶；本控制只验证 (25)，不参与递归。

## 8. 统一选择器接线

~~~text
canonical F q-primary restriction
  -> source-invisible:
       FIXED_LAYER_ONLY_QPRIMARY
  -> source-visible:
       one minimal SOURCE_RANK_DEMAND request
       -> no certified source edge:
            FG_QPREFIX_ROLE_TO_EDGE_UNPROVED
       -> one unlayered named edge:
            depth-(q-1) arithmetic candidate
            -> candidate-fiber + typed gates pass: one FULL_CQ_PREFIX lineage
                 -> terminal FIBER_REALIZED or target-kernel section
            -> otherwise: focused range/admission/first-overflow receipt
       -> q-1 pre-existing physical requests request a staircase:
            distinct ids + COMMON_ROLE_LINE_CERT
            + joint role image + filtered layers
            + joint SNF + candidate-fiber + occurrence ledgers
            -> FG_QPREFIX_STAIRCASE_ADMISSION_CERT
            -> otherwise: exact request/role/filter/ingress obstruction

canonical G/Jacobi separation role
  -> declared negative endpoint menu:
       G_JACOBI_NEGATIVE_ENDPOINT_MENU_ODD_QPREFIX_INGRESS_ZERO
  -> anchor or a new raw row crosses the coset:
       G_JACOBI_SOURCE_COSET_ESCAPE and rebuild the source contract
~~~

这张分派完成的是 F/G 角色到 q-prefix 的类型安全入口和一个严格 G 子菜单 no-go。它
现在已有同一 \(p=557281\) 上的 actual-F depth-2 full-\(C_3\) typed realization，且该
实例由首个越界 gap \(79\) 独立 Type II 终止；也有 \(p=73\) 的共同基和 target
q-direction 双重 no-go。尚未证明 candidate-fiber 对所有未终止核心素数均通过，也
没有把一般 full-cycle kernel slice 或 overflow 菜单空回执升级为 exact successor、
E4 或 E5。新的决定性缺口是：对未被短终端预占的 actual F 请求证明该入口存在，或把
其精确失败和 kernel section 转成可提升且不可重置的良基递降；规范 G/Jacobi 二阶角色
不再作为奇 q 入口。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_request_depth_admission.py --verify
~~~

验证器只重算本卡的新线性判据和三个固定算术控制，不运行历史测试。
