---
kind: claim
claim_id: type-I-odd-fourier-owner-cylinder-transverse-rank-map
title: 奇阶 Fourier 源差分到 owner 圆柱横向数字的秩容量映射
statement: >-
  固定奇素数 q 不整除 p。第 j 层真实 q-prefix owner 全落在唯一绝对剩余类
  beta_j+q^j Z，因此任何单位斜率的直接仿射 phase-owner 映射若覆盖一个非恒
  Fourier 相位集，必将其压成常相位，不能支付源差分 q 秩。对 owner 定义横向数字
  tau_j(s)=(s-beta_j)/q^j mod q 后，tau_j 的差分恰检测 v_q(s-t)=j，且所有高度
  至少 j+1 的 owner 都落在唯一深层数字 delta_j；所以非零横向秩必需一个精确高度
  j 的 owner。反演记录 U/V 与 V/U 若 sigma=U+V 满足 q|p+4sigma 且
  4(sigma+q)<p，则 sigma、sigma+q 构成一对真实 q-prefix owner，其横向数字相差
  1，并通过唯一仿射数字映射保存一个 F_q 源差分方向。p=97 的 5 与 1/5 由此映到
  q=11 owner 6、17；该映射真实保留一维横向秩，但两个单独 Type II 纤维都无
  11-primary 单位群方向，也没有直接证书或严格 source-switch，故它是跨纤维容量映射，
  不是 E1--E5 递降。后续关联格定理证明任何固定参数纤维的横向秩恒为零，并把该
  二点映射实现为跨纤维增广格的 C_11 source-SNF。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-jacobi-punctured-kernel-primary-selector
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-i-target-odd-affine-offset-repair-gate
  - type-II-qprefix-owner-height-source-closure
  - type-II-qprefix-owner-escape-capacity-decomposition
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-I
  - type-II
  - Fourier
  - q-primary
  - owner
  - q-prefix
  - transverse-digit
  - source-rank
  - inversion-pair
  - capacity-map
  - proof-program
sources:
  - claim: type-I-core-jacobi-punctured-kernel-primary-selector
    role: p97-order-11-source-rank-input
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: source-difference-rank-semantics
  - claim: type-II-qprefix-owner-height-source-closure
    role: physical-owner-height-semantics
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: tight-chain-valuation-boundary
  - reproduction: reproductions/type_i_odd_fourier_owner_cylinder_transverse_rank_map.py
    role: p97-owner-digit-rank-and-boundary-control
visibility: public
last_checked: '2026-08-09'
---

# 奇阶 Fourier 源差分到 owner 圆柱横向数字的秩容量映射

## 1. 绝对 owner 类必然压掉非恒相位

固定奇素数 \(q\nmid p\)。对 \(j\ge1\)，取唯一相容剩余类

\[
0\le \beta_j<q^j,
\qquad p+4\beta_j\equiv0\pmod {q^j}.
\tag{1}
\]

给定实际整数标签集 \(S\)，其第 \(j\) 层 owner 为

\[
\mathcal O_j(S)
=\{s\in S:q^j\mid p+4s\}
=S\cap(\beta_j+q^j\mathbb Z).
\tag{2}
\]

设 \(X\) 是一组源记录，

\[
\gamma:X\longrightarrow\mathbb Z/q^j\mathbb Z
\]

是非恒 Fourier 相位。若存在固定

\[
a\in(\mathbb Z/q^j\mathbb Z)^\times,
\qquad c\in\mathbb Z/q^j\mathbb Z
\]

和标签 \(s_x\in\mathcal O_j(S)\)，使

\[
s_x\equiv a\gamma(x)+c\pmod {q^j}
\qquad(x\in X),
\tag{3}
\]

则 (2)--(3) 强制

\[
a\gamma(x)+c=\beta_j
\qquad(x\in X).
\]

由于 \(a\) 是单位，\(\gamma\) 必须恒定。这证明：

\[
\boxed{
\text{非恒 source phase 不能直接编码在第 }j
\text{ 层 owner 的绝对剩余类中。}}
\tag{4}
\]

即使 \(\beta_j\) 出现在 phase support 中，求交后也只剩单一相位纤维；该纤维的
相位差分秩为零。常数偏移 \(c\) 本身不消秩，真正消秩的是 owner 条件把所有绝对
剩余类固定为同一个 \(\beta_j\)。

## 2. 横向 owner 数字与 depth--rank 门

对 \(s\in\mathcal O_j(S)\)，定义圆柱内的下一位数字

\[
\tau_j(s)
=\frac{s-\beta_j}{q^j}\pmod q
\in\mathbb F_q.
\tag{5}
\]

再定义唯一深层数字

\[
\delta_j
=\frac{\beta_{j+1}-\beta_j}{q^j}\pmod q.
\tag{6}
\]

由定义立即有

\[
\boxed{
s\in\mathcal O_{j+1}(S)
\Longleftrightarrow
\tau_j(s)=\delta_j.}
\tag{7}
\]

对任意 \(s,t\in\mathcal O_j(S)\)，

\[
\tau_j(s)-\tau_j(t)
\equiv\frac{s-t}{q^j}\pmod q.
\tag{8}
\]

因此，当 \(s\ne t\) 时，

\[
\boxed{
\tau_j(s)\ne\tau_j(t)
\Longleftrightarrow
v_q(s-t)=j.}
\tag{9}
\]

令横向秩容量为

\[
r_j^{\rm tr}(S)
=\dim_{\mathbb F_q}
\left\langle
\tau_j(s)-\tau_j(t):s,t\in\mathcal O_j(S)
\right\rangle.
\tag{10}
\]

这里是标量数字，所以 \(r_j^{\rm tr}\in\{0,1\}\)。它等于 1 当且仅当实际
owner 至少占两个横向数字。特别地，若全部 owner 的高度至少为 \(j+1\)，式 (7)
使所有数字都等于 \(\delta_j\)，从而

\[
r_j^{\rm tr}(S)=0.
\tag{11}
\]

故任何支付一个非零 \(\mathbb F_q\) 源差分方向的 owner 族都必须包含至少一个
高度恰为 \(j\) 的 owner。深 owner 可以提供纵向高度，但不能单独支付同层横向秩。

式 (9) 的估值边界与已有 q-prefix 紧链分解一致；这里新增的内容不是重复该估值，
而是把归一化差商送入 \(\mathbb F_q\)，定义式 (10) 的 Fourier source-rank 容量，
并在下面构造由实际反演记录产生的非零横向基。

若 \(\gamma(x_+)\ne\gamma(x_-)\) 且
\(\tau_j(s_+)\ne\tau_j(s_-)\)，则有唯一

\[
a=
\frac{\tau_j(s_+)-\tau_j(s_-)}
{\gamma(x_+)-\gamma(x_-)}\in\mathbb F_q^\times,
\qquad
c=\tau_j(s_+)-a\gamma(x_+),
\tag{12}
\]

使

\[
\tau_j(s_\pm)=a\gamma(x_\pm)+c.
\tag{13}
\]

所以两个不同横向数字对一个 rank-one phase basis 是充分且必要的。完整 phase
support 的提升仍需检查全部 affine image、范围、来源标签和 Hall/Rado 门；式 (12)
不把二点基自动扩张为全支撑 source-map。

## 3. 反演对的真实整数横向构造

设一对实际反演记录对应既约正有理数

\[
\rho=\frac UV,
\qquad \rho^{-1}=\frac VU,
\qquad (U,V)=1,
\tag{14}
\]

并令

\[
\sigma=U+V.
\tag{15}
\]

设其阶 \(q\) 相位为

\[
\gamma(\rho)=u,
\qquad \gamma(\rho^{-1})=-u,
\qquad u\ne0.
\tag{16}
\]

若

\[
q\mid p+4\sigma,
\qquad 4(\sigma+q)<p,
\tag{17}
\]

定义有向 owner 标签

\[
s_+=\sigma,
\qquad s_-=\sigma+q.
\tag{18}
\]

两者均满足 \(q\mid p+4s_\pm\)，并处于标准 Type II 正性窗口。它们在第 1 层的
横向数字相差 1：

\[
\tau_1(s_-)-\tau_1(s_+)=1.
\tag{19}
\]

此外

\[
(p+4s_-)-(p+4s_+)=4q,
\]

所以二者不可能同时被 \(q^2\) 整除，得到

\[
\boxed{
\min\{v_q(p+4s_+),v_q(p+4s_-)\}=1.}
\tag{20}
\]

写 \(s_\pm=A_\pm^2C_\pm\)，其中 \(C_\pm\) 平方自由，并置

\[
D_\pm=A_\pm C_\pm,
\qquad a_\pm=A_\pm.
\]

则

\[
D_\pm a_\pm=s_\pm,
\qquad q\mid p+4D_\pm a_\pm,
\qquad(q,4D_\pm)=1.
\tag{21}
\]

所以式 (18) 给出两条真实、可逐项核验的 Type II q-prefix 整数记录。由式 (12)，
它们唯一承载反演相位对的一维横向差分。shared-\(q\) 账本必须把它们记为一个
rank-one 载体的两个端点，不能把同一个 \(q\) 收费两次。

式 (21) 只完成整数 owner 与横向 rank map。要得到 Type II 终端，还必须有某个
实际因子积 \(h\equiv-1\pmod {4D_\pm}\)；要得到递降，还必须有保持来源的较小
\(D'\) 和全部 E1--E5。这些结论都不由 (17)--(21) 自动推出。

## 4. \(p=97\) 的 11 阶真实控制

取

\[
(p,R,K)=(97,67,5^3\cdot13).
\tag{22}
\]

在 \(L=\langle4\rangle\simeq C_{33}\) 上，前一引理的全局 11 阶角色对 negative
记录 \(z=(z_5,z_{13})\) 的相位为

\[
\gamma(z)=2z_5+4z_{13}\pmod {11}.
\tag{23}
\]

取反演对

\[
z_+=(1,0),\qquad z_-=(-1,0).
\]

其有理单项式为 \(5\) 与 \(1/5\)，故

\[
\sigma=5+1=6,
\qquad
\gamma(z_+)=2,
\qquad
\gamma(z_-)=9=-2.
\tag{24}
\]

另一方面，

\[
\beta_1=\beta_2=6,
\qquad
97+4\cdot6=121=11^2,
\qquad
97+4\cdot17=165=3\cdot5\cdot11.
\tag{25}
\]

因此标准窗口 \(4s<97\) 中的全部 11-owner 恰为

\[
\mathcal O_1=\{6,17\},
\qquad
(e_6,e_{17})=(2,1),
\qquad
(\tau_1(6),\tau_1(17))=(0,1).
\tag{26}
\]

式 (12) 在这里给出

\[
\boxed{
\tau_1(s_z)=8\gamma(z)+6\pmod {11},
\qquad
z\in\{z_+,z_-\}.}
\tag{27}
\]

确实，\(8\cdot2+6=0\)、\(8\cdot9+6=1\pmod {11}\)。所以这是一个实际整数
owner 对上的 rank-one 横向映射，而不是把抽象角色阶直接称为高度。

这个控制同时给出三条严格边界。

第一，绝对 owner 映射仍失败：所有 11-prefix 标签都等于 \(6\pmod {11}\)，不能
直接保存相位 \(2\) 与 \(9\) 的差。

第二，两个 canonical Type II 纤维分别为

\[
(A,C,D,M)=(1,6,6,24),
\qquad(1,17,17,68).
\tag{28}
\]

有

\[
|U(24)|=8,\qquad |U(68)|=32,\qquad
\varphi(\operatorname{lcm}(24,68))=\varphi(408)=128.
\tag{29}
\]

三者都没有 11-primary 子群或商。因此式 (27) 是外部 owner-cylinder 数字坐标，
不是任一单纤维单位群中的 11 阶同态。后续关联格定理进一步证明这不是选错模数：
固定 \((D,A)\) 本来就固定 \(s=AD\)，故单纤维横向秩恒为零；正确 source-SNF 是
两个参数顶点之间的增广关联格商 \(C_{11}\)。它仍未提供单一目标群积块或 E1--E5。

第三，两个 owner 都没有当前路线内的 E4/E5 出口。\(s=6\) 时

\[
p+4s=121,\qquad
\{h:h\mid121\}=\{1,11,121\},
\]

没有 \(h\equiv-1\pmod {24}\)；\(s=17\) 时 \(p+4s=165\) 的全部因子也没有
\(h\equiv-1\pmod {68}\)。保持 11-prefix 的 divisor-lattice 菜单在 \(D=6\) 与
\(D=17\) 中都只返回原标签，没有 \(D'<D\) 的严格 source-switch。

\(p=97\) 本身已有独立的规范移位 \(s=2,h=7\) Type II 终端，例如

\[
\frac4{97}
=\frac1{28}+\frac1{194}+\frac1{2716}.
\tag{30}
\]

但该终端不保留 11 阶 owner-cylinder 路线。后续来源边规范化定理已把带名反演记录、
整数规则 \((\sigma,\sigma+11)\) 与余因子差绑定为一个规范 edge token；其归一化
源列为 1，一个请求通过 flow--Rado，两个独立请求严格出现 rank \(1<2\)。故式 (27)
的准确状态更新为

```text
OWNER_CYLINDER_TRANSVERSE_RANK_ONE
FIBER_INCIDENCE_SNF = C11
EDGE_SOURCE_PROVENANCE = verified_inversion_pair
SOURCE_RELATION_SCOPE = one_edge
TRANSVERSE_SOURCE_CAPACITY = 1
INCIDENCE_FLOW_RADO = pass_for_one_request
DIRECT_ENDPOINT_UNIT_GROUP_LIFT = obstructed_no_11_primary
PHYSICAL_OWNER_FLOW = unproved_external_contract_required
DIRECT_TERMINAL = false
STRICT_SOURCE_SWITCH = false
recursive_edge_eligible = false
```

## 5. 选择器接口

奇阶 source-rank 请求不应再直接与绝对 owner residue 对齐，而应按以下顺序处理：

```text
SOURCE_RANK_DEMAND(q)
  -> ABSOLUTE_OWNER_PHASE_COLLAPSE
  -> OWNER_CYLINDER_TRANSVERSE_DIGITS
       -> rank 0: EXACT_HEIGHT_OWNER_MISSING / anchor only
       -> rank 1: INVERSION_PAIR_OR_AFFINE_DIGIT_MAP
            -> fiber-incidence C_q source-SNF
            -> qualified arithmetic edge
                 -> additive source resource / exact rank capacity 1
                 -> physical owner projection / actual factor mask / E1--E5
```

这条分派首次给出一个不会被唯一 owner 剩余类压平的嵌套相位中心。后续结果已经严格
排除同纤维横向 lift，并在参数纤维增广格上构造规范 \(C_q\) 商；标准 owner 窗口
覆盖全部 \(q\) 个数字时，任意 \(\mathbb F_q\) phase support 都有完整关联格 lift。
一般 affine-digit 指派仍未证明总保持原记录的算术来源；只有带名整数边才能进入新
source-resource 门。即使该门通过，也未把关联格边变成实际 Type II 因子积块或
E1--E5。大尺度完整窗口、小尺度深 owner 的四值余因子终端菜单及来源边容量见
[奇阶 owner 横向数字的跨纤维关联格源映射与同纤维 no-go](type-I-odd-owner-fiber-incidence-lattice-source-map.md)
、[odd-owner 窗口的尺度二分与深层小余因子 Type II 终端菜单](type-I-odd-owner-scale-dichotomy-small-cofactor-terminal.md)
及[奇阶 owner 关联边的来源保持规范化与精确一维秩容量](type-I-odd-owner-incidence-edge-source-preserving-capacity.md)。

## 聚焦验证

```bash
python3 reproductions/type_i_odd_fourier_owner_cylinder_transverse_rank_map.py --verify
```

复现只重建 \(p=97\) 的 11-owner 窗口、横向数字、反演相位、两个 Type II 纤维的
E4/E5 阻碍和独立终端，不运行历史扫描。
