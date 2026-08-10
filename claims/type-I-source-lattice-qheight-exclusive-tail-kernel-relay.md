---
kind: claim
claim_id: type-I-source-lattice-qheight-exclusive-tail-kernel-relay
title: 源格估值移位载体的多层独占尾、单前缀账本与核截面 relay
statement: >-
  设奇素数 q 上的一条带名 rank-one 源边差向量为 delta，content(delta)=q^t g_0，
  且非零角色把 delta 送到 c。对任意 J>=max(1,t) 与 d>=1，可把估值移位载体的
  模数从 q^(J+1) 提升到 q^(J+d)，构造共享同一规范源基 D_0 的 deep/shallow
  source rows 和规范目标 (D_*,A_*)，使 deep source 与 target 至少有 J+d 层、
  shallow source 精确只有 J 层，整数仿射边在第 J 层精确实现 c。该整数数据只先给
  candidate/shared-q block extension；只有同一 realized fiber 的逐前缀 source-switch、
  block lineage 与 occurrence 不重计门通过后，才得到唯一连续幂块
  {1,q,...,q^d}，而不是 d 个独立 rank 请求。另一方面，q-1 条分别精确停在
  J,...,J+q-2 层的 provenance-qualified 阶梯边，在共同 deep source 与 target
  上使用两两不同的绝对层 occurrence key；联合 SNF、真实纤维与 fresh-key 门通过时，
  q-1 个带名请求获得连续层满匹配，并由 shared-q 账本压成唯一的最小 full-cycle
  前缀，而不是 q-1 个独立 q 块。
  显式 cyclotomic 商 eta:U(4D_*)->C_q 把该前缀满射到 C_q；若完整同纤维积集仍遗漏目标，目标的
  eta-kernel 截面必为非空真集并具有严格正 Fourier 能量。反之，固定层首 q 个
  owner 的 q-1 条 deep--shallow 星形边共享同一个 deep occurrence，单位容量下最大流
  只有 1，不能替代上述单前缀块；C_q 商饱和也不推出同余核稳定、E4 或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - type-I-owner-profile-canonical-base-target-slot-capacity
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-source-fiber-shared-q-ledger
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-I-raw-certified-q-layer-charge-key-nonreuse
  - type-II-weighted-source-saturated-quotient-kernel-dispatch
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-stabilizer-kernel-source-box-lattice-criterion
topics:
  - type-I
  - type-II
  - source-lattice
  - q-height
  - owner
  - q-prefix
  - physical-capacity
  - cyclotomic-quotient
  - kernel-fourier
  - strict-obstruction
  - capacity-map
  - proof-program
sources:
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: rank-one-minimal-depth-and-one-layer-carrier
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: actual-q-height-to-single-power-block
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: prefix-compression-and-no-binary-duplication
  - claim: type-I-raw-certified-q-layer-charge-key-nonreuse
    role: one-lineage-depth-rank-price-nonaddition
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: fixed-layer-star-collision-and-distinct-layer-flow
  - claim: type-II-weighted-source-saturated-quotient-kernel-dispatch
    role: quotient-hit-to-proper-kernel-section
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: kernel-section-is-not-kernel-stability-boundary
  - reproduction: reproductions/type_i_source_lattice_qheight_exclusive_tail_kernel_relay.py
    role: focused-depth-two-staircase-star-collision-range-and-kernel-controls
visibility: public
last_checked: '2026-08-10'
---

# 源格估值移位载体的多层独占尾、单前缀账本与核截面 relay

## 1. 固定层星形边不能支付 \(q-1\) 个块

固定核心素数 \(p\)、奇素数 \(q\nmid p\) 与层 \(J\ge1\)。严格 owner 窗口中
前 \(q\) 个 \(q^J\)-prefix 标签的横向数字遍历 \(\mathbb F_q\)，其中恰有一个
标签 \(s_+\) 进入 \(q^{J+1}\) 层，其余 \(q-1\) 个标签精确停在第 \(J\) 层。
因此从 \(s_+\) 到这些 shallow 标签的 exclusive 图是星

\[
K_{1,q-1}.
\tag{1}
\]

每条边在 source 端都要使用同一个绝对层 occurrence

\[
\kappa_{\rm src}=(\mathsf S,s_+,q,J+1).
\tag{2}
\]

若该槽容量为一，则任意请求--token--物理槽流至多取一条星边：

\[
\boxed{\mathsf F(K_{1,q-1})=1.}
\tag{3}
\]

对 \(q\ge3\)，式 (3) 严格小于 \(q-1\)。所以完整 owner 数字窗口虽然有
\(q-1\) 个 shallow 顶点，却不能被解释成 \(q-1\) 个不重复的物理
\(\{1,q\}\) 块。若这些边还绑定同一个 target，target occurrence 会给出第二个
相同的容量一瓶颈。后文构造的是**一个连续幂前缀块**，不是绕过 (3) 复制星边。

## 2. depth-\(d\) 估值移位算术载体

令一条带名有向源边满足

\[
\delta=z_1-z_0\ne0,
\qquad
g=\operatorname{content}(\delta)=q^t g_0,
\qquad
q\nmid g_0,
\tag{4}
\]

并在边格上固定非零角色

\[
\gamma(n\delta)=nc,
\qquad c\in\mathbb F_q^\times.
\tag{5}
\]

取

\[
J\ge\max(1,t),
\qquad d\ge1,
\qquad m=q^{J+d}.
\tag{6}
\]

令 \(r\) 是既有 cyclotomic 构造选出的最小素数，满足

\[
r\mid\Phi_q(q),
\qquad \operatorname{ord}_r(q)=q,
\qquad v_q(r-1)=1.
\tag{7}
\]

这样的 \(r\) 必存在。确实，\(\Phi_q(q)\equiv1+q\pmod {q^2}\)，且其每个素
因子都不等于 \(q\)、并使 \(q\) 的阶恰为 \(q\)。若每个素因子都模 \(q^2\)
同余于 1，则 \(\Phi_q(q)\equiv1\pmod {q^2}\)，矛盾。因此至少一个素因子满足
\(v_q(r-1)=1\)；固定取其中最小者使构造确定化。

记 \(b\) 为 \(-p\cdot4^{-1}\pmod m\) 的最小正代表，并令

\[
\alpha=c(b\bmod q)^{-1}\in\mathbb F_q^\times.
\tag{8}
\]

依固定避让顺序选择最小素数

\[
u\equiv1+\alpha q^J\pmod m,
\qquad u\nmid g_0r,
\tag{9}
\]

再定义

\[
H=\operatorname{lcm}(g_0,r,u),
\qquad A_0=H/\operatorname{rad}(H).
\tag{10}
\]

依次选择最小素数

\[
v\equiv1\pmod m,\quad v\nmid H,
\qquad
\lambda\equiv b(A_0H)^{-1}\pmod m,\quad \lambda\nmid Hv.
\tag{11}
\]

所有剩余类均与 \(m\) 互素，故 Dirichlet 定理保证选择存在。令

\[
\begin{aligned}
D_*&=H\lambda, & A_*&=A_0,
&C_*&=\operatorname{rad}(H)\lambda,\\
x&=A_0H\lambda, & D_0&=D_*v,\\
a_0&=A_0, &a_1&=A_0u,\\
s_0&=D_0a_0=xv, &s_1&=D_0a_1=xuv.
\end{aligned}
\tag{12}
\]

逐素数比较给出

\[
\frac{D_*}{A_*}=\operatorname{rad}(H)\lambda,
\quad
\frac{D_0}{a_0}=\operatorname{rad}(H)\lambda v,
\quad
\frac{D_0}{a_1}=\frac{\operatorname{rad}(H)}u\lambda v,
\tag{13}
\]

三者都平方自由。特别地，\(D_*\mid D_0\)，而两条 source row 的**规范基**均
恰为 \(D_0\)，不只是共享某个 gcd 除子；target 的规范基恰为 \(D_*\)。

若精确范围门

\[
\boxed{p>4xuv}
\tag{14}
\]

通过，则 target 与两个 source labels 全部在严格窗口中。由 (8)--(12)，

\[
x\equiv s_0\equiv b\pmod m,
\qquad
s_1\equiv b(1+\alpha q^J)\pmod m.
\tag{15}
\]

所以

\[
\boxed{
v_q(p+4x)\ge J+d,
\quad
v_q(p+4s_0)\ge J+d,
\quad
v_q(p+4s_1)=J.}
\tag{16}
\]

同时

\[
v_q(s_1-s_0)=J,
\qquad
\frac{s_1-s_0}{q^J}\equiv b\alpha=c\pmod q.
\tag{17}
\]

因为 \(g_0\mid H\mid x\) 且 \(t\le J\)，还有 \(g\mid s_1-s_0\)。取
\(\mathbf r\cdot(\delta/g)=1\)，则

\[
\boxed{
\mathcal L(z)=s_0+
\frac{s_1-s_0}{g}\,\mathbf r\cdot(z-z_0)}
\tag{18}
\]

把 \(z_i\) 送到 \(s_i\)，并在第 \(J\) 层精确实现 (5)。这证明了一个新的
`DEPTH_D_VALUATION_SHIFTED_CARRIER_ARITHMETIC_READY`：同一带名边、共同规范源基、
指定 target 菜单和 depth-\(d\) 高度差同时由一个整数构造实现。

## 3. 高度差只先产生一个 Q-PREFIX 候选

式 (16) 使 deep source \(s_0\) 与 target \(x\) 都拥有绝对前缀
\(1,\ldots,J+d\)，而 shallow source 只有 \(1,\ldots,J\)。由 q-height
source-switch 恒等式，\(q^{J+d}\mid x-s_0\) 把 deep 来源高度送到同一 candidate
fiber。可是高度整除本身不能把尾部写成 \(d\) 个互相独立的 rank 请求。

升级为 typed block 必须另有同一 realized fiber 的合同：

1. source-switch、SNF、范围、prescribed role/anchor 与 `FIBER_REALIZED` 已通过；
2. shared-q ledger 证明所有中间指数都可在同一纤维回译，并把选择限制为前缀；
3. 唯一 `block_lineage_id` 下的层键是 fresh，或属于同一 assignment 的完整 replay；
4. 更深 receipt 只能扩长并替换旧块，不能与旧深度、source rank 或 Kneser 价格相加。

通过这些门后，相对公共前缀得到唯一块

\[
\boxed{B_d=\{1,q,q^2,\ldots,q^d\}.}
\tag{19}
\]

它有 \(d+1\) 个**嵌套前缀选择**，不是 \(2^d\) 个 binary masks。若实现展开绝对层键，

\[
(\mathsf S,s_0,q,J+r),
\qquad
(\mathsf T,x,q,J+r),
\qquad1\le r\le d,
\tag{20}
\]

这些键只属于同一个 lineage；它们不进入 role-request 图成为 \(d\) 个列。准确账本是

\[
\boxed{
\text{source-column rank}=1,
\qquad
\text{relative q-prefix depth}=d.}
\tag{21}
\]

若第 1--4 项缺任一项，只能输出
`EXCLUSIVE_Q_TAIL_QPREFIX_ADMISSION_UNPROVED`，不得定义真实 \(B_d\)。

## 4. 不同停止层的阶梯 star 支付连续物理层匹配

上一节说明单条 depth-\(d\) 边只允许一个 lineage。若确实需要为多个带名请求支付
不同物理 q 层，必须提供多条边和互异的绝对层槽。下面给出一个完整的算术 skeleton。

令

\[
h=q-1,
\qquad m=q^{J+h},
\qquad b=-p\cdot4^{-1}\pmod m,
\tag{S1}
\]

并给定 \(h\) 条以同一基点为中心的带名边 \(\delta_a\)，其中

\[
\operatorname{content}(\delta_a)=q^{t_a}g_a,
\qquad q\nmid g_a,
\qquad t_a\le J+a-1,
\tag{S2}
\]

规范角色值为 \(c_a\in\mathbb F_q^\times\)。这里讨论的是最终压成一个循环
q-primary 方向、角色秩一的 staircase；若请求携带不同角色义务，必须改用完整
evaluation-Rado/耦合超图。本节的 \(h\) 条边只是算术 skeleton，
不自动生成 \(h\) 个请求。调用本节前必须已经有 \(h\) 个两两不同的 physical
request ids，并给出 'COMMON_ROLE_LINE_CERT'：全部请求角色经其合同允许的非零单位
归一化后属于同一个已固定一维线 \(L\)。把 \(c_a\) 同步换算到该共同坐标；若边在
规范可见商中的像为 \(u_a\)，还必须满足

\[
(c_1,\ldots,c_h)\in
\operatorname{im}\!\left[
L\longrightarrow\mathbb F_q^h,\quad
\rho\longmapsto(\rho(u_a))_{a=1}^h
\right].
\tag{S2a}
\]

式 (S2a) 只是共同线性方程的可解条件；等价地，desired vector 必须湮灭该求值映射
转置的核，所以它不依赖后文的算术构造。逐边分别可解不能替代 (S2a)，在较大角色
空间中找到另一个共同角色也不能删除原请求的独立角色义务。若
\(\delta_a=n_a\delta\) 且 \(q\nmid n_a\)，同一个
整数仿射映射又使所有像差具有相同 q-估值，严格不能形成不同停止层。完整请求—深度
分解、联合角色像判据和最小反例见
[F/G q-prefix 的请求—深度分解、联合角色准入与 Jacobi 负陪集零入口](type-I-fg-qprefix-request-depth-admission.md)。

先固定满足 (7) 的 \(r_0\)。对
\(1\le a\le h\)，递归选取
两两不同并避开 \(r_0g_1\cdots g_h\) 及此前所选素数的素数

\[
u_a\equiv
1+c_ab^{-1}q^{J+a-1}
\pmod m.
\tag{S3}
\]

令

\[
H=\operatorname{lcm}(r_0,g_1,\ldots,g_h,u_1,\ldots,u_h),
\qquad A_0=H/\operatorname{rad}(H).
\tag{S4}
\]

再选择素数

\[
v\equiv1\pmod m,
\qquad
\lambda\equiv b(A_0H)^{-1}\pmod m,
\tag{S5}
\]

并使 \(v,\lambda\) 避开 \(H\) 及彼此。所有指定剩余类都与 \(m\) 互素，故这些
选择由 Dirichlet 定理保证存在。定义

\[
\begin{aligned}
D_*&=H\lambda, & A_*&=A_0, &x&=A_0H\lambda,\\
D_0&=D_*v, &a_0&=A_0, &a_a&=A_0u_a,\\
s_0&=D_0a_0=xv, &&&s_a&=D_0a_a=xvu_a.
\end{aligned}
\tag{S6}
\]

与 (13) 相同的逐素数比较证明 target 的规范基为 \(D_*\)，而
\(s_0,s_1,\ldots,s_h\) 的规范基全都恰为 \(D_0\)。若

\[
\boxed{p>4xv\max_{1\le a\le h}u_a,}
\tag{S7}
\]

则所有标签都在严格 owner 窗口。由 (S1)--(S6)，

\[
\begin{aligned}
v_q(p+4x),\ v_q(p+4s_0)&\ge J+h,\\
v_q(p+4s_a)&=J+a-1,\\
v_q(s_a-s_0)&=J+a-1,\\
\frac{s_a-s_0}{q^{J+a-1}}&\equiv c_a\pmod q.
\end{aligned}
\tag{S8}
\]

而 (S2)、(S4) 保证 \(\operatorname{content}(\delta_a)\mid s_a-s_0\)，所以每条
source line 都有 (18) 型整数仿射实现。对一般带名 star，仍须运行联合 SNF 以证明
这些逐边实现来自同一来源映射；自由格 skeleton
\(\delta_a=q^{J+a-1}e_a\) 则由坐标线性式同时实现全部边。

现在把第 \(a\) 条边放在 base \(J+a-1\)。式 (S8) 说明 \(s_0\) 与 target
都继承下一层，而 \(s_a\) 精确停在 base 层。于是既有 one-next-layer 定理给出
第 \(a\) 个候选物理层 token，收费键为

\[
\kappa_a^{\rm src}=(\mathsf S,s_0,q,J+a),
\qquad
\kappa_a^{\rm tgt}=(\mathsf T,x,q,J+a).
\tag{S9}
\]

这些键因最后一个 layer 坐标而两两不同。只有当全部边的 named provenance、联合
SNF、prescribed labels、`FIBER_REALIZED`、source-switch 与 fresh-key 门都通过时，
才可把 \(h=q-1\) 个请求满匹配到连续的相对层 \(1,\ldots,q-1\)。随后必须按
shared-q ledger 把同一 q 方向压缩为唯一块

\[
\boxed{
B_{f,q}(q-1)
=\{1,q,q^2,\ldots,q^{q-1}\}.}
\tag{S10}
\]

这里有 \(q-1\) 个互异物理层 assignment，但账本中只有一个 q-prefix lineage，
同一个循环 q-primary 方向上的列秩仍为 1；不得把它们申报为 \(q-1\) 个独立块或
初等角色秩。与固定层 star 的 (3) 相比，阶梯构造不增加同层容量，而是使用
\(J+1,\ldots,J+q-1\) 的互异绝对槽。

最后，一个深度 \(d\) 的同方向前缀块至多有 \(d+1\) 个指数，故覆盖 \(C_q\)
必须 \(d\ge q-1\)。式 (S10) 达到该下界；它是这种单循环方向上的最优物理层
full-cycle staircase。

## 5. 满 \(C_q\) 后强制进入 target-kernel 截面

令 \(r_c=r\) 表示 (12) 的单边载体，或令 \(r_c=r_0\) 表示 (S6) 的阶梯载体。
两种情形都有 \(r_c\mid D_*\)，并由 (7) 得到显式满射

\[
\eta:U(4D_*)\longrightarrow C_q,
\qquad
\eta(z)=(z\bmod r_c)^{(r_c-1)/q},
\tag{22}
\]

且 \(\eta(q)\) 是生成元、\(\eta(-1)=1\)。在 (19) 或 (S10) 已 typed-realized
且与 prescribed labels 联合相容的前提下，

\[
\boxed{
d\ge q-1
\iff
\eta(B_d)=C_q.}
\tag{23}
\]

当 \(d<q-1\) 时，(19) 的 \(d+1<q\) 个像互异，故不能满射；所以
\(d=q-1\) 是最小 full-cycle 深度。

令 \(A\subseteq G_*=U(4D_*)\) 是同一 realized fiber 中其它实际源块的非空积，
并置 \(P=AB_d\)。式 (23) 给出 \(\eta(P)=C_q\)。对目标 \(w\in G_*\)，若
\(w\in P\)，整数回译直接给出该纤维的 Type II 命中。若 \(w\notin P\)，令

\[
K_\eta=\ker\eta,
\qquad
S_w=\{k\in K_\eta:wk\in P\}.
\tag{24}
\]

商像已满保证 \(S_w\ne\varnothing\)；而 \(w\notin P\) 给出 \(1\notin S_w\)，
所以 \(S_w\subsetneq K_\eta\)。在未归一化 Fourier 约定下，Parseval 精确给出

\[
\boxed{
\sum_{\substack{\chi\in\widehat K_\eta\\\chi\ne1}}
|\widehat{1_{S_w}}(\chi)|^2
=|S_w|\bigl(|K_\eta|-|S_w|\bigr)>0.}
\tag{25}
\]

这是一条构造性的
`FULL_CQ_PREFIX_TARGET_OR_KERNEL_SECTION`，但不是同余核稳定定理。一般只有
\(\eta(P)=C_q\)，不能推出

\[
K_\eta\le\operatorname{Stab}_{G_*}(P).
\tag{26}
\]

最小反例可在加法记号下取
\[
G=C_3\oplus C_2,
\quad \eta:G\to C_3,
\quad B_1=\{0,(1,0)\},
\quad B_2=\{0,(1,1)\}.
\tag{26a}
\]
则 \(P=B_1+B_2\) 投满 \(C_3\)，但 \((0,1)\in\ker\eta\) 不稳定 \(P\)。对遗漏
目标 \(w=(0,1)\)，式 (24) 的截面恰为单点 \(\{(0,1)\}\)。这严格排除了从商饱和
直接跳到 kernel source box 的推理。

因此 (25) 只进入 kernel Fourier/source-box 门；它不产生 exact successor、E4 或 E5。

还有一个算术上不可省略的边界。因为 \(\langle q\bmod r_c\rangle\) 的阶是奇数 \(q\)，

\[
\boxed{-1\notin\{q^e\bmod r_c:e\ge0\}.}
\tag{27}
\]

所以 tail-only 的 \(B_d\) 永远不能单独命中 \(-1\pmod {4D_*}\)。full-cycle 角色饱和
不能被误报成 Type II terminal；其它实际块或 (25) 的核截面是必需的。

## 6. 深度窗口的严格 no-go

任意严格 owner 标签 \(0<4s<p\) 若有高度 \(h\)，则

\[
q^h\le p+4s<2p.
\tag{28}
\]

所以任何以单一 q-height 尾实现 full \(C_q\) cycle 的载体都必须满足

\[
\boxed{q^{J+q-1}<2p.}
\tag{29}
\]

若 (29) 失败，输出
`FULL_CQ_SINGLE_QHEIGHT_WINDOW_OBSTRUCTED`。它只否定这一个连续 q-height
full-cycle 入口，不排除其它素数方向、多个真实块或终端。

## 7. 五个聚焦控制

### 7.1 \(q=3,d=2\) 的单边前缀正控制

取

\[
p=557281,\quad q=3,\quad J=t=1,\quad d=2,\quad
\delta=3,\quad c=1.
\tag{30}
\]

规范选择为

\[
r=13,\quad u=7,\quad H=91,\quad A_0=1,\quad v=109,\quad\lambda=2.
\tag{31}
\]

式 (12) 给出

\[
(D_*,A_*,x)=(182,1,182),\quad D_0=19838,
\quad(s_0,s_1)=(19838,138866).
\tag{32}
\]

这里 \(4s_1=555464<p\)，并且

\[
v_3(p+4x)=4,\qquad
v_3(p+4s_0)=3,\qquad
v_3(p+4s_1)=1.
\tag{33}
\]

仿射规则为

\[
\mathcal L(z)=19838+39676z,
\tag{34}
\]

它把 \(0,3\) 送到 \(s_0,s_1\)，且
\((s_1-s_0)/3\equiv1\pmod3\)。typed Q-PREFIX 门通过时，相对块
\(\{1,3,9\}\) 在 (22) 下覆盖 \(C_3\)。模 \(4D_*=728\) 它不含 \(-1\)；
tail-only target kernel slice 是 \(\{-1\}\)，其核大小为 \(96\)，故 (25) 的能量为
\(95\)。

### 7.2 同一算术模板的严格范围失败

取同一剩余类中的核心素数 \(p=555337\)。式 (31)--(32) 不变，但

\[
4s_1=555464>p.
\tag{35}
\]

所以该模板严格返回 `DEPTH_D_CARRIER_RANGE_OBSTRUCTED`；不能由同余正确性冒充
owner-window realization。

### 7.3 完整窗口星形仍只有容量一

对 \(p=97,q=3,J=1\)，首三个 owner 是 \(2,5,8\)，唯一 deep 标签是 \(5\)。
两条边 \((5,2),(5,8)\) 都投影到 source key
\((\mathsf S,5,3,2)\)，所以最大物理流为 \(1<2\)。这正是 (3) 的最小算术控制。

### 7.4 单 q-height full-cycle 的窗口 no-go

对 \(p=73,q=3,J=3\)，full-cycle 至少要求高度 \(J+q-1=5\)，但

\[
3^5=243\ge146=2p.
\tag{36}
\]

故严格窗口中不存在相应 deep owner，直接触发 (29)。

### 7.5 \(q=3\) 的两层物理 staircase

取

\[
p=673184521,\quad q=3,\quad J=1,\quad
(r_0,u_1,u_2,v,\lambda)=(13,7,19,109,47).
\tag{37}
\]

这里 \(m=27\)、\(H=1729\)、\(A_0=1\)，且

\[
x=D_*=81263,\qquad D_0=8857667,
\tag{38}
\]

\[
(s_0,s_1,s_2)=(8857667,62003669,168295673).
\tag{39}
\]

所有规范基判据成立，且 \(4s_2=673182692<p\)。target、deep source 与两个
shallow source 的 3-height 依次为

\[
(4,3,1,2).
\tag{40}
\]

两条边分别在 base 1、2 停止，归一化横向数字都为 1；它们收费的 source/target
层分别是 2、3，因而四个 occurrence key 两两按 state/value/layer 合同区分。
取自由源格
\[
L=3\mathbb Ze_1\oplus9\mathbb Ze_2,
\qquad
\gamma(3n_1e_1+9n_2e_2)=n_1+n_2\pmod3,
\tag{40a}
\]
则同一个整数仿射式
\[
\mathcal L(z_1,z_2)=8857667+17715334(z_1+z_2)
\tag{40b}
\]
把 \(0,3e_1,9e_2\) 分别送到 \(s_0,s_1,s_2\)，并在各自停止层实现角色 1。
在联合来源与真实纤维门通过后，这两个请求满匹配到相对层 1、2，shared-q 账本给出

\[
\{1,3\}\{1,3\}=\{1,3,9\}\longrightarrow C_3.
\tag{41}
\]

## 8. 选择器接线与剩余缺口

~~~text
qualified rank-one named edge (delta, gamma, q)
  -> choose J >= max(1, v_q(content(delta))) and tail depth d
  -> construct common-canonical-base rows and target at modulus q^(J+d)
       range fail:
         DEPTH_D_CARRIER_RANGE_OBSTRUCTED
       arithmetic pass:
         DEPTH_D_VALUATION_SHIFTED_CARRIER_ARITHMETIC_READY
         -> no realized-fiber/prefix/lineage contract:
              EXCLUSIVE_Q_TAIL_QPREFIX_ADMISSION_UNPROVED
         -> typed Q-PREFIX admission passes:
              one block lineage B_d={1,q,...,q^d}
              source-column rank = 1; never d
              d < q-1:
                SET_PHASE_REALIZED proper prefix
              d >= q-1 and joint eta/label gate passes:
                FULL_CQ_PREFIX
                -> target hit: TYPE_II_TERMINAL
                -> target miss: NONEMPTY_PROPER_ETA_KERNEL_SECTION
                                + positive kernel Fourier energy

qualified staircase star (delta_a, gamma_a, q), a=1..q-1
  -> require q-1 pre-existing distinct request ids
  -> require COMMON_ROLE_LINE_CERT
  -> require normalized desired values in that line's joint evaluation image
  -> assign stopping bases J, J+1, ..., J+q-2
  -> construct one common canonical source base and common target
       range/joint-SNF/provenance/fiber gate fails:
         STAIRCASE_PHYSICAL_ADMISSION_UNPROVED or strict range receipt
       all gates pass and layer keys are fresh:
         q-1 requests matched to distinct consecutive absolute layers
         one shared-q block lineage; never q-1 independent q blocks
         elementary q-primary role rank = 1
         Q-PREFIX block = {1,q,...,q^(q-1)}
         -> FULL_CQ_PREFIX_TARGET_OR_KERNEL_SECTION
~~~

本定理新增的是从一个带名 source-line 角色到 depth-\(d\) 共同规范基算术载体、再到
单一 typed Q-PREFIX 的入口，以及从不同停止层的 qualified staircase 到互异
occurrence slots、连续层满匹配和最优 full-cycle 前缀的算术接线。幂块的 Kneser 价格、
full-cycle 饱和和 kernel Fourier
分派沿用既有定理。它没有证明每个实际 F/G 请求都通过范围、prefix、label 与
`FIBER_REALIZED`，也不从一条角色请求生成 staircase 所需的 \(q-1\) 个 request ids，
更没有把 \(D_*<D_0\) 冒充不可重置的 owner-base E5。下一步必须
证明真实请求族中该入口全称非空，或把 (29)、范围失败及 kernel slice 送入直接终端、
完整 kernel source box 或已封闭的良基下降。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_source_lattice_qheight_exclusive_tail_kernel_relay.py \
  --verify
~~~

验证器只重算 (30)--(41) 的聚焦素数控制、规范 rows、单边与阶梯层高、星形 occurrence
碰撞、互异阶梯键、full-cycle 角色像、tail-only kernel slice 与窗口 no-go；不运行
历史扫描。
