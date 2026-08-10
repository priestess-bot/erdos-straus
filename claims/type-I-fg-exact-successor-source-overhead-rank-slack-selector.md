---
kind: claim
claim_id: type-I-fg-exact-successor-source-overhead-rank-slack-selector
title: F/G exact successor 的最小 source 开销、选择秩松弛与变开销 Grassmann 选择器
statement: >-
  设广义 Rado 正亏损割给出 Q=Q_U、m=dim Q、r=|P-U| 与
  delta=m-r>0。对一个已经独立实现的 exact successor，令 S_omega 为 r 条
  completion 列的张成空间，T_omega 为后继全部真实 source-evaluation 列的张成
  空间。则覆盖后继源列所需的最小 provenance-preserving 辅助开销精确等于
  h_omega^*=dim((T_omega+S_omega)/S_omega)，而同时湮灭 completion 与后继源列
  的角色维数精确为 e_omega=delta+(r-dim S_omega)-h_omega^*。因此具体后继保留
  非零角色当且仅当 h_omega^*<delta+(r-dim S_omega)；选择列的秩亏可严格支付
  source 开销。对任意带不同 T_omega 的 exact-successor 家族，s 维共同角色切片
  的总 incidence 等于 sum_omega [e_omega choose s]_q；若目标投影不在
  T_omega+S_omega 中，目标可见切片还有精确的
  [e_omega choose s]_q-[e_omega-1 choose s]_q 双计数。物理 owner mincut
  只有附带规范 source-column 秩时才能给出该容量；相同物理割可分别留下正角色
  容量或使容量饱和。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-exterior-grassmann-slice-successor-descent
  - type-I-fg-generalized-rado-fixed-quotient-defect
  - type-I-fg-snf-canonical-role-evaluation-quotient
  - type-I-II-fg-universal-finite-source-map-completion
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-owner-exact-flow-negative-certificate-relay
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - exact-successor
  - source-overhead
  - rank-slack
  - Grassmannian
  - target-visible
  - owner-mincut
  - residual-capacity
  - proof-program
sources:
  - claim: type-I-fg-exterior-grassmann-slice-successor-descent
    role: uniform-fixed-overhead-grassmann-input
  - claim: type-I-fg-generalized-rado-fixed-quotient-defect
    role: fixed-rado-defect-quotient
  - claim: type-I-fg-snf-canonical-role-evaluation-quotient
    role: canonical-role-source-pairing
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: exact-successor-source-contract
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-owner-mincut-input
  - claim: type-II-owner-exact-flow-negative-certificate-relay
    role: source-preserving-owner-columns
  - reproduction: reproductions/type_i_fg_exact_successor_source_overhead_rank_slack_selector.py
    role: focused-minimal-overhead-variable-incidence-target-and-mincut-boundaries
visibility: public
last_checked: '2026-08-10'
---

# F/G exact successor 的最小 source 开销、选择秩松弛与变开销 Grassmann 选择器

## 1. 只在真实 exact successor 上定义

固定素数 \(q\)。由广义 Rado 正亏损割 \(U\subseteq P\) 取得

\[
Q=Q_U=K_R/W_U,\qquad
m=\dim Q,\qquad
C=P\setminus U,\qquad
r=|C|,\qquad
\delta=m-r>0.
\tag{1}
\]

这里 \(Q^*\simeq Z_U\le R\) 是已经由 fixed-order source-SNF 构造的真实角色
空间。以下对象不能从任意 kernel filter 或菜单删点伪造。令

\[
\Omega^{\mathrm{ex}}
=
\{\omega:\text{a labelled exact successor }\Sigma'_\omega
          \text{ is attached to }\omega\}
\tag{2}
\]

是有限非空的带标签族，其中每个 \(\omega\) 是物理可行 completion，而
\(\Sigma'_\omega\) 已经独立通过
`SELECTED_SOURCE_STATE_REALIZATION`：它属于允许的递归状态族，保存全部
record provenance，并有回到原整数状态的 branch/certificate lift。

在 \(Q\) 中定义

\[
S_\omega
=
\operatorname{span}
\{b_p(\omega):p\in C\},
\qquad
s_\omega=\dim S_\omega,
\qquad
a_\omega=r-s_\omega\ge0.
\tag{3}
\]

\(a_\omega\) 是 **selection-rank slack**：请求仍有 \(r\) 条，但它们只占
\(s_\omega\) 个线性方向。再令 \(\mathcal S(\Sigma'_\omega)\) 是后继的全部真实
source generators，并定义

\[
T_\omega
=
\operatorname{span}
\{\pi_U\kappa(g):g\in\mathcal S(\Sigma'_\omega)\}
\le Q,
\qquad
Y_\omega=S_\omega+T_\omega.
\tag{4}
\]

需要角色同时湮灭 \(S_\omega\) 与真实后继源列，所以正确的角色空间是

\[
A_\omega=Y_\omega^\perp\le Q^*,
\qquad
e_\omega=\dim A_\omega=m-\dim Y_\omega.
\tag{5}
\]

只给出过滤后的记录集而没有 \(\Sigma'_\omega\) 时，\(T_\omega\) 没有合法定义，
本卡不能运行。

## 2. 最小 provenance-preserving source 开销

考虑所有满足

\[
T_\omega\subseteq X+S_\omega
\tag{6}
\]

的辅助空间 \(X\le Q\)。定义

\[
\boxed{
h_\omega^*
=
\dim\frac{T_\omega+S_\omega}{S_\omega}
=
\dim(T_\omega+S_\omega)-\dim S_\omega
=
\dim T_\omega-\dim(T_\omega\cap S_\omega).
}
\tag{7}
\]

则

\[
\boxed{
h_\omega^*
=
\min\{\dim X:X\le Q,\ T_\omega\subseteq X+S_\omega\}.
}
\tag{8}
\]

而且若 \(T_\omega\) 由带 provenance 的真实 source columns 生成，可以从这些
带标签列中贪心选出 \(h_\omega^*\) 条，其像在
\((T_\omega+S_\omega)/S_\omega\) 中形成基；这些列的张成空间达到 (8)。
因此 (8) 不只是裸维数最小值，而有一个保留来源的构造性证书。

### 证明

商映射

\[
\varpi_\omega:Q\longrightarrow Q/S_\omega
\tag{9}
\]

把 (6) 送成

\[
\varpi_\omega(T_\omega)\subseteq\varpi_\omega(X).
\tag{10}
\]

所以任意可行 \(X\) 都满足

\[
\dim X
\ge\dim\varpi_\omega(X)
\ge\dim\varpi_\omega(T_\omega)
=h_\omega^*.
\tag{11}
\]

反过来，在 \(T_\omega\) 中取
\(T_\omega\cap S_\omega\) 的补空间 \(X_\omega^*\)。则

\[
T_\omega=(T_\omega\cap S_\omega)\oplus X_\omega^*,
\qquad
T_\omega\subseteq S_\omega+X_\omega^*,
\qquad
\dim X_\omega^*=h_\omega^*.
\tag{12}
\]

若指定带标签生成列，按固定标签顺序做模 \(S_\omega\) 的 Gaussian elimination，
保留首次增加商秩的列；所得列像是
\(\varpi_\omega(T_\omega)\) 的基，故其原列线性无关且张成一个达到 (12) 的
provenance-preserving \(X_\omega^*\)。证毕。

## 3. 选择秩松弛的精确容量恒等式

由 (3)、(5) 和 (7)，直接得到

\[
\begin{aligned}
e_\omega
&=m-\dim(S_\omega+T_\omega)\\
&=m-s_\omega-h_\omega^*\\
&=(m-r)+(r-s_\omega)-h_\omega^*.
\end{aligned}
\]

因此

\[
\boxed{
e_\omega
=
\delta+a_\omega-h_\omega^*.
}
\tag{13}
\]

这不是下界，而是具体 exact successor 的**精确剩余角色容量**。特别地，

\[
\boxed{
A_\omega\ne0
\quad\Longleftrightarrow\quad
h_\omega^*<\delta+a_\omega.
}
\tag{14}
\]

旧 fixed-overhead 定理中的 \(h<\delta\) 是只知道“至多 \(r\) 条选择列”时的
completion-independent 统一充分条件。式 (14) 表明，对一个具体后继，
selection-rank slack \(a_\omega\) 可以支付同样多的额外 source directions。

若 completion 列本身也属于后继真实源集，即
\(S_\omega\le T_\omega\)，则

\[
Y_\omega=T_\omega,\qquad
h_\omega^*=\dim T_\omega-\dim S_\omega,\qquad
\boxed{e_\omega=\operatorname{codim}_Q T_\omega.}
\tag{15}
\]

因此此常见情形中，真正的正容量条件只是
\(T_\omega\ne Q\)；不能再从 \(h_\omega^*\ge\delta\) 单独判死，因为
\(a_\omega>0\) 可能补回该差额。

### 固定开销定理是它的统一推论

若有一个 completion-independent 空间 \(X\le Q\) 满足

\[
T_\omega\subseteq X+S_\omega
\qquad(\forall\omega\in\Omega^{\mathrm{ex}}),
\tag{16}
\]

则 (8) 给出 \(h_\omega^*\le\dim X\)，所以

\[
e_\omega
\ge\delta+a_\omega-\dim X
\ge\delta-\dim X.
\tag{17}
\]

故 \(\dim X<\delta\) 仍保证每个后继都有统一正容量；它只是没有使用
\(a_\omega\) 和实际 \(T_\omega\) 的信息。

## 4. 变开销 Grassmann 双计数

对 \(1\le s\le m\) 及
\(L\in\operatorname{Gr}_s(Q^*)\)，定义

\[
\Omega_L^{\mathrm{ex}}
=
\{\omega:L\le A_\omega\}
=
\{\omega:L\le(S_\omega+T_\omega)^\perp\}.
\tag{18}
\]

约定 \({n\brack s}_q=0\) 当 \(s<0\) 或 \(s>n\)。则有精确恒等式

\[
\boxed{
\sum_{L\in\operatorname{Gr}_s(Q^*)}
|\Omega_L^{\mathrm{ex}}|
=
\sum_{\omega\in\Omega^{\mathrm{ex}}}
{e_\omega\brack s}_q.
}
\tag{19}
\]

因此至少一个 \(L\) 满足

\[
\boxed{
\frac{|\Omega_L^{\mathrm{ex}}|}{|\Omega^{\mathrm{ex}}|}
\ge
\frac{\sum_\omega{e_\omega\brack s}_q}
     {{m\brack s}_q|\Omega^{\mathrm{ex}}|}.
}
\tag{20}
\]

若全部 \(e_\omega\ge e_0\ge s\)，则右端进一步至少为

\[
\frac{{e_0\brack s}_q}{{m\brack s}_q}>0.
\tag{21}
\]

与 fixed-\(X\) 版本不同，(19) 允许每个 exact successor 有不同的
\(T_\omega\)、\(h_\omega^*\) 和 \(e_\omega\)，角色切片统一在固定 ambient
\(Q^*\) 中枚举。

### 证明

固定 \(\omega\)。满足 \(L\le A_\omega\) 的 \(s\) 维子空间恰有
\({e_\omega\brack s}_q\) 个。对
\(\{(L,\omega):L\le A_\omega\}\) 先按 \(L\) 再按 \(\omega\) 计数即得
(19)；除以 \(|\operatorname{Gr}_s(Q^*)|={m\brack s}_q\) 得 (20)，
Gaussian 系数的单调性给出 (21)。证毕。

## 5. 目标可见的精确切片

令目标 \(t\) 在 \(K_R\) 中的 evaluation column 为 \(\kappa_t\)，并取其固定割商像

\[
\bar\kappa_t=\pi_U(\kappa_t)\in Q.
\tag{22}
\]

对单个后继，

\[
\boxed{
\exists\rho\in A_\omega,\ \rho(\bar\kappa_t)\ne0
\quad\Longleftrightarrow\quad
\bar\kappa_t\notin Y_\omega.
}
\tag{23}
\]

这是因为 \(A_\omega=Y_\omega^\perp\) 且
\((Y_\omega^\perp)^\perp=Y_\omega\)。

假设 \(\bar\kappa_t\ne0\)，并定义 ambient target-visible Grassmannian

\[
\operatorname{Gr}_s^t(Q^*)
=
\{L\in\operatorname{Gr}_s(Q^*):
L\not\le\bar\kappa_t^\perp\}.
\tag{24}
\]

其大小为

\[
|\operatorname{Gr}_s^t(Q^*)|
=
{m\brack s}_q-{m-1\brack s}_q.
\tag{25}
\]

若 \(\bar\kappa_t\notin Y_\omega\)，则目标求值在
\(A_\omega\) 上是非零线性泛函，其核维数为 \(e_\omega-1\)。所以

\[
\boxed{
\sum_{L\in\operatorname{Gr}_s^t(Q^*)}
|\Omega_L^{\mathrm{ex}}|
=
\sum_{\substack{\omega\in\Omega^{\mathrm{ex}}\\
                  \bar\kappa_t\notin Y_\omega}}
\left(
{e_\omega\brack s}_q
-
{e_\omega-1\brack s}_q
\right).
}
\tag{26}
\]

若 (26) 右端为正，等价地至少一个 target-visible 后继满足
\(e_\omega\ge s\)，则存在一个看见目标且至少支持一个后继的共同角色切片；其
支持量至少为 (26) 右端除以 (25)。当 \(s=1\) 时，每个 target-visible 后继贡献
精确的

\[
{e_\omega\brack1}_q-{e_\omega-1\brack1}_q
=q^{e_\omega-1}
\tag{27}
\]

条 projective role lines。

若 \(\bar\kappa_t=0\)，全部 \(Q^*\)-角色都湮灭目标，target-visible 分支为空。
当 \(e_\omega>0\) 且已经选到非零 \(L\le A_\omega\) 时，只能进入
joint-kernel 的 subgroup 分支；当 \(e_\omega=0\) 时则已容量耗尽。式 (26) 不在
该退化情形使用。

## 6. Owner mincut 必须升级为 ranked mincut

令 \(J\) 是与式 (1) **同一个广义 Rado 割 \(U\)** 配对的 owner 请求割。假设已经通过
source-preserving canonicalization，使每个物理槽 \(c\) 有请求无关的真实源列
\(v_c\)，并令 \(B_0\le K_R\) 是 completion-independent 的其它固定源列空间。
在固定的 \(Q=Q_U=K_R/W_U\) 中定义

\[
\boxed{
X_{U,J}
=
\operatorname{span}
\left(
\pi_U(B_0),
\pi_U(v_c):c\in\mathcal C(J)
\right),
\qquad
h_{U,J}=\dim X_{U,J}.
}
\tag{28}
\]

\(X_{U,J}\) 是包含全部这些规范固定列的唯一最小子空间，且

\[
\boxed{
h_{U,J}
\le
\dim\pi_U(B_0)+|\mathcal C(J)|
\le
\dim\pi_U(B_0)+\mathsf P(J),
}
\tag{29}
\]

其中
\(\mathsf P(J)=\sum_{c\in\mathcal C(J)}b(c)\)，且每个实际槽容量
\(b(c)\ge1\)。

若某个 independently realized exact successor 还通过

\[
T_\omega\subseteq X_{U,J}+S_\omega,
\tag{30}
\]

则

\[
\boxed{
e_\omega
\ge
\delta+a_\omega-h_{U,J}
\ge
\delta+a_\omega
-\dim\pi_U(B_0)-\mathsf P(J).
}
\tag{31}
\]

所以物理 mincut 只有和规范 source-column rank 及 source closure (30) 一起，
才能支付 Grassmann successor。普通缺口
\(\mathsf P(J)<|J|\) 不蕴含
\(h_{U,J}<\delta+a_\omega\)。

## 7. 三个严格边界

### 7.1 旧统一阈值可被选择秩松弛严格改进

取

\[
Q=\mathbb F_2^4,\qquad
r=2,\qquad
\delta=2,
\tag{32}
\]

并令两条 completion 列相同，使

\[
S=\langle e_1\rangle,\qquad
a=r-\dim S=1.
\tag{33}
\]

取 exact successor source span

\[
T=\langle e_1,e_2,e_3\rangle.
\tag{34}
\]

则

\[
h^*=\dim T-\dim S=2=\delta,
\qquad
e=\delta+a-h^*=1.
\tag{35}
\]

旧 fixed-\(X\) 统一条件 \(h<\delta\) 在等号处不能推出任何东西，但该具体后继仍
严格留下 \(\langle e_4^*\rangle\)。这不否定旧阈值的 uniform sharpness：
旧阈值没有使用两条选择列相关所产生的 \(a=1\)。

### 7.2 source domination 正好耗尽全部松弛

保持 (32)--(33)，改取 \(T=Q\)。则

\[
h^*=m-\dim S=3=\delta+a,
\qquad
e=0.
\tag{36}
\]

一般地，

\[
\boxed{
T_\omega=Q
\quad\Longrightarrow\quad
h_\omega^*=\delta+a_\omega,\quad e_\omega=0.
}
\tag{37}
\]

所以当前 source-dominating 饱和状态不能靠重新记 owner 或重新选择 completion
制造正角色容量；必须构造一个真实 source span 严格收缩的 exact successor。

### 7.3 相同物理 mincut 不决定 residual capacity

取

\[
Q=\mathbb F_2^3,\qquad
r=1,\qquad
\delta=2,\qquad
S=\langle e_3\rangle.
\tag{38}
\]

让三个 owner 请求都连接到两个容量为一的物理槽
\(c_1,c_2\)。两种模型的请求图、最大流 \(2\)、物理割容量
\(\mathsf P=2\) 及缺口 \(3-2=1\) 完全相同。

* 模型 A：
  \(v_{c_1}=v_{c_2}=e_1\)。则
  \(X=\langle e_1\rangle\)、\(h=1\)，取
  \(T=X+S=\langle e_1,e_3\rangle\) 时 \(e=1\)。
* 模型 B：
  \(v_{c_1}=e_1,\ v_{c_2}=e_2\)。则
  \(X=\langle e_1,e_2\rangle\)、\(h=2=\delta\)，取
  \(T=X+S=Q\) 时 \(e=0\)。

因此

\[
\boxed{
\text{physical mincut data}
\not\Longrightarrow
\text{Grassmann residual capacity}.
}
\tag{39}
\]

必须保存 (28) 的 source-column rank，不能用 owner 数、槽数或流值代替。

## 8. 构造性回执与分派

~~~text
EXACT_SUCCESSOR_SOURCE_OVERHEAD_CAPACITY_CERT
  rado_cut: U
  quotient: Q_U
  completion: omega
  selected_span: S_omega
  selected_rank_slack: a_omega
  exact_successor: Sigma'_omega
  successor_source_span: T_omega
  joint_span: Y_omega
  minimal_labelled_overhead_generators: X^*_omega
  minimal_overhead_rank: h^*_omega
  exact_role_capacity: e_omega
  target_projection: bar(kappa_t)
  target_visible: bar(kappa_t) notin Y_omega

exact successor realization absent:
  SELECTED_SOURCE_STATE_REALIZATION_UNPROVED
e_omega = 0:
  EXACT_SUCCESSOR_ROLE_CAPACITY_EXHAUSTED
e_omega > 0:
  enumerate Gr_s(Q_U^*) against Y_omega
  emit VARIABLE_GRASSMANN_SUCCESSOR_SLICE_CERT
  target projection outside Y_omega:
    TARGET_VISIBLE_GRASSMANN_SLICE
  target projection inside Y_omega:
    TARGET_KERNEL_SUBGROUP_ONLY
owner mincut without canonical source columns:
  OWNER_GRASSMANN_OVERHEAD_RANK_UNPROVED
owner columns present but source closure (30) absent:
  OWNER_SELECTED_SOURCE_CLOSURE_UNPROVED
integer lift gates incomplete:
  EXACT_SUCCESSOR_INTEGER_LIFT_OBSTRUCTED
FIBER_REALIZED + provenance + SNF/CRT + range + marked E4 + nonresetting E5:
  STRICT_LIFTABLE_SUCCESSOR
~~~

所有空间均可用固定列顺序的 RREF 构造；(12) 给出最小带标签开销列，(19) 与
(26) 可枚举达到最大支持量的第一项作为确定性 Grassmann 证书。

## 9. 研究边界

本卡把此前 completion-independent 的 \(\delta-\dim X\) 下界升级为每个真实
exact successor 的精确容量

\[
\boxed{
e_\omega=\delta+a_\omega-h_\omega^*.
}
\tag{40}
\]

它还首次允许不同后继具有不同 source span，并直接选择看见指定目标的共同角色
slice。它严格证明：选择秩亏可以支付 source overhead，而物理 mincut 若不附带
source-column rank，不能决定任何 residual role capacity。

本卡没有从任意 F/G 状态自动制造 \(\Sigma'_\omega\)，也没有证明整数 E1--E5。
primary-filter 的活动源差分现已精确证明为全源张成：规范 Type I 盒有
\(D_B=H\)。在 realization 之前，保留全部活动源的 filter-only 候选只能证明
\(T_\omega^{\mathrm{cand}}=Q_U\) 并输出候选饱和；若它 independently realized
为 exact successor，则其合法 \(T_\omega=Q_U\) 与 \(e_\omega=0\)。所以
primary-filter 只有先附加一个独立证明的算术 source contraction 才能重新进入本门。
下一决定性算术问题因而更窄：在实际
nearest-fiber、owner，或 primary-filter 加真实 source contraction 的候选中，
构造一个带来源的 exact successor 并验证

\[
Y_\omega=S_\omega+T_\omega\ne Q_U
\quad\Longleftrightarrow\quad
h_\omega^*<\delta+a_\omega.
\tag{41}
\]

只有另证 \(S_\omega\le T_\omega\) 时，(41) 才可简化为
\(T_\omega\ne Q_U\)。若全部实际候选都达到等号，则必须把
\(Y_\omega=Q_U\)（等价 \(h_\omega^*=\delta+a_\omega\)）的饱和证书转成 Type I/II
终端或另一良基下降。

primary-filter 零容量定理及实际 \(p=73,R=27\) 的 sharp deficit 饱和控制见
[primary filter 的活动源差分饱和与 source-preserving successor 零容量](type-I-primary-filter-active-source-saturation-zero-successor-capacity.md)。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_exact_successor_source_overhead_rank_slack_selector.py --verify
~~~

验证器只检查新定理涉及的小维有限域对象：最小开销公式、选择秩松弛等号例、
source domination 饱和例、变开销 Grassmann incidence、目标可见 incidence，以及
相同物理 mincut 的不同 source-rank 容量；不运行历史测试。
