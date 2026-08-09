---
kind: claim
claim_id: type-I-odd-owner-fiber-incidence-lattice-source-map
title: 奇阶 owner 横向数字的跨纤维关联格源映射与同纤维 no-go
statement: >-
  固定奇素数 q 不整除 p 和深度 j。标准窗口中的 q^j-prefix owner 恰为
  s_m=beta_j+m q^j，其横向数字为 m mod q；每个 s_m 唯一确定 Type II 参数
  (D_m,A_m)，且固定参数纤维固定 s=A D，故任何单纤维横向 owner 秩恒为零。
  在 owner 纤维顶点的增广格 L_0 上，Theta_j(sum n_v e_v)=sum n_v tau_j(v) mod q
  是规范同态，其像恰等于横向差分空间；非零时 L_0/ker Theta_j 同构于 C_q。
  真实余因子 N_m=(p+4s_m)/q^j 又满足 N_m=N_0+4m，使 Theta_j 等于
  4^(-1) 倍余因子差分模 q。因而同纤维横向 source-map 不存在，但跨纤维关联格
  给出具有整数加法 realization 的精确 source-SNF。若 Fourier
  phase 与横向数字仿射相容，该关联格同态逐差分保存 phase q 秩。owner 窗口含至少
  q 个连续 q^j-prefix 标签时覆盖全部 F_q 数字；特别地 p>4q^(j+1) 是充分条件，
  此时任意 F_q phase support 都有完整跨纤维仿射 lift，且首 q 个 owner 中恰有
  一个深度至少 j+1，其余 q-1 个深度恰为 j。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-fourier-owner-cylinder-transverse-rank-map
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-I
  - type-II
  - Fourier
  - q-primary
  - owner
  - transverse-digit
  - source-lattice
  - Smith-normal-form
  - cross-fiber
  - no-go
  - capacity-map
  - proof-program
sources:
  - claim: type-I-odd-fourier-owner-cylinder-transverse-rank-map
    role: transverse-owner-digit-input
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: fixed-parameter-fiber-semantics
  - reproduction: reproductions/type_i_odd_owner_fiber_incidence_lattice_source_map.py
    role: focused-window-incidence-SNF-and-boundary-controls
visibility: public
last_checked: '2026-08-09'
---

# 奇阶 owner 横向数字的跨纤维关联格源映射与同纤维 no-go

## 1. 标准 owner 窗口与规范 Type II 顶点

固定奇素数 \(q\nmid p\) 和 \(j\ge1\)。令

\[
0<\beta_j<q^j,
\qquad p+4\beta_j\equiv0\pmod {q^j},
\qquad B=\left\lfloor\frac{p-1}{4}\right\rfloor.
\tag{1}
\]

严格正性窗口 \(4s<p\) 中的全部 \(q^j\)-prefix owner 恰为

\[
\mathcal O_j(p)
=\{s_m=\beta_j+m q^j:0\le m\le M_j\},
\qquad
M_j=\left\lfloor\frac{B-\beta_j}{q^j}\right\rfloor,
\tag{2}
\]

其中 \(B<\beta_j\) 时集合为空。其横向数字为

\[
\boxed{\tau_j(s_m)=m\pmod q.}
\tag{3}
\]

把每个 \(s_m\) 唯一写成

\[
s_m=A_m^2C_m,
\qquad C_m\text{ 平方自由},
\qquad D_m=A_mC_m.
\tag{4}
\]

则

\[
s_m=A_mD_m,\qquad
A_m\mid D_m,\qquad D_m/A_m=C_m,\qquad4A_mD_m<p.
\tag{5}
\]

又因 \(q^j\mid p+4s_m\) 且 \(q\nmid p\)，必有 \(q\nmid s_m\)，从而

\[
q\nmid4D_m.
\tag{6}
\]

所以

\[
v_m=(D_m,A_m)
\tag{7}
\]

是一个真实、规范的 Type II 源参数纤维顶点，\(q^j\) 是该顶点的合法来源幂。
不同 \(s_m\) 给出不同顶点，因为顶点本身恢复 \(s_m=A_mD_m\)。

## 2. 固定参数纤维的横向秩恒为零

现有 Type II source-fiber 固定 \((D,A)\)。在该纤维内，owner 标签恒为

\[
s=AD.
\tag{8}
\]

因此所有记录具有同一个

\[
\tau_j(AD)=\frac{AD-\beta_j}{q^j}\pmod q.
\]

任意两个纤维内记录的横向差均为零。特别地，任何经过固定参数标签投影的映射都满足

\[
\boxed{r^{\rm tr}_j(\text{fixed }D,A)=0.}
\tag{9}
\]

这不是 \(p=97\) 的偶发现象，而是参数化本身的 no-go。单纤维单位群或因子积块仍
可能携带纵向 \(q\)-height；但它不能在不改变参数顶点的情况下冒充横向 owner 数字。
因此“把非零横向秩提升到同一个固定 Type II 参数纤维”应从目标列表中删除。

## 3. 跨纤维增广关联格给出规范 source-SNF

令 \(V_j(p)=\{v_m:s_m\in\mathcal O_j(p)\}\)，并取顶点自由格及其增广核

\[
C_0=\mathbb Z^{V_j(p)},
\qquad
L_0=\ker\!\left[\epsilon:C_0\to\mathbb Z\right],
\qquad
\epsilon\!\left(\sum_vn_ve_v\right)=\sum_vn_v.
\tag{10}
\]

定义

\[
\Theta_j:L_0\longrightarrow\mathbb F_q,
\qquad
\Theta_j\!\left(\sum_vn_ve_v\right)
=\sum_vn_v\tau_j(v)\pmod q.
\tag{11}
\]

\(L_0\) 由所有边 \(e_v-e_w\) 生成，且

\[
\Theta_j(e_v-e_w)=\tau_j(v)-\tau_j(w).
\tag{12}
\]

所以

\[
\boxed{
\operatorname{im}\Theta_j
=\left\langle\tau_j(v)-\tau_j(w):v,w\in V_j(p)\right\rangle_{\mathbb F_q}.}
\tag{13}
\]

右侧正是 owner-cylinder 横向差分空间。由于 \(q\) 为素数，它只有秩 0 或 1；
非零时 \(\Theta_j\) 满射，并由第一同构定理得到

\[
\boxed{L_0/\ker\Theta_j\simeq C_q.}
\tag{14}
\]

式 (11)--(14) 是此前缺失的跨纤维 source-SNF。它不把不同 \(U(4D_m)\) 强行池化，
而是把 \(q\) 方向放在参数纤维的关联格上；每条 shared-\(q\) 横向边只贡献同一个
\(C_q\) 商，不能在两个端点重复收费。

该商还有一个规范整数 realization。定义真实 owner 余因子

\[
N_m=\frac{p+4s_m}{q^j}\in\mathbb N,
\qquad
N_0=\frac{p+4\beta_j}{q^j}.
\tag{15}
\]

由 \(s_m=\beta_j+m q^j\) 得到

\[
\boxed{N_m=N_0+4m.}
\tag{16}
\]

所以对任意 \(\sum_mn_me_{v_m}\in L_0\)，增广和为零消去常数 \(N_0\)，并有

\[
\boxed{
\Theta_j\!\left(\sum_mn_me_{v_m}\right)
=4^{-1}\sum_mn_mN_m\pmod q.}
\tag{17}
\]

特别地，

\[
\Theta_j(e_{v_m}-e_{v_n})
=4^{-1}(N_m-N_n)\pmod q.
\tag{18}
\]

因此 \(C_q\) 关联格商不是人为附加的 phase 坐标，而是实际整数余因子差分的模
\(q\) 像。深层数字条件也化成 \(q\mid N_m\)：首 \(q\) 个余因子构成步长 4 的
完整模 \(q\) 系，恰有一个进入下一 \(q\)-进层。

设源记录集 \(X\) 带相位 \(\gamma:X\to\mathbb F_q\)，并有顶点赋值
\(f:X\to V_j(p)\) 满足

\[
\tau_j(f(x))=a\gamma(x)+c,
\qquad a\in\mathbb F_q^\times.
\tag{19}
\]

在记录增广格 \(L_X=\ker[\mathbb Z^X\to\mathbb Z]\) 上，顶点赋值诱导
\(f_\#:L_X\to L_0\)。常数项因增广和为零而消失，故

\[
\boxed{
\Theta_j\circ f_\#
=a\,\Gamma,
\qquad
\Gamma\!\left(\sum_xn_xe_x\right)=\sum_xn_x\gamma(x).}
\tag{20}
\]

所以全记录赋值 (19) 精确保留 source phase 的 \(q\)-差分秩；只在两个记录上成立
时，式 (20) 只是一条 rank-one basis map，不能伪称完整支撑 lift。即使 (19) 对
全部记录成立，它证明的也是关联格 phase lift；若顶点赋值仅由相位任意选取，还必须
另证原记录的算术来源标签与这些 Type II 顶点相容，才能升级为物理 source-map。

## 4. owner 窗口容量与完整相位 lift 的精确门

由 (2)--(3)，窗口出现的横向数字是

\[
\{0,1,\ldots,M_j\}\pmod q.
\tag{21}
\]

因此：

1. \(M_j=0\) 时横向秩为 0；
2. \(M_j\ge1\) 时横向秩为 1；
3. \(M_j\ge q-1\) 当且仅当窗口覆盖全部 \(\mathbb F_q\) 数字。

第三种情形下，对任意 phase support \(\Gamma\subseteq\mathbb F_q\) 和任意
\(a\ne0,c\)，取 \([a\gamma+c]_q\in\{0,\ldots,q-1\}\) 并定义

\[
s_\gamma
=\beta_j+q^j[a\gamma+c]_q.
\tag{22}
\]

则所有 \(s_\gamma\) 都在标准窗口内，且给出式 (19) 的完整跨纤维 phase lift。
这一步不自动保留相位以外的原记录来源数据。
一个方便的充分条件是

\[
\boxed{p>4q^{j+1}.}
\tag{23}
\]

事实上此时 \(B\ge q^{j+1}\)，而

\[
\beta_j+(q-1)q^j\le q^{j+1}-1<B.
\]

再令

\[
\delta_j=\frac{\beta_{j+1}-\beta_j}{q^j}\pmod q.
\tag{24}
\]

首 \(q\) 个 owner 的数字遍历 \(\mathbb F_q\)，恰有数字 \(\delta_j\) 的一个 owner
进入 \(q^{j+1}\)-圆柱；其余 \(q-1\) 个 owner 都满足精确高度 \(j\)。所以完整窗口
不仅提供一个 \(C_q\) source-SNF，还自动提供 \(q-1\) 个 exact-height escape 顶点。

当 \(M_j<q-1\) 时，给定 phase support \(\Gamma\) 的完整 lift 存在，当且仅当有
\(a\ne0,c\) 使所有最小剩余数

\[
[a\gamma+c]_q\le M_j
\qquad(\gamma\in\Gamma).
\tag{25}
\]

这是一个有限且精确的准入门；二点相位只需两个不同数字，但一般全支撑不能由
rank-one basis map 自动推出。

## 5. 三个聚焦控制

### 5.1 \(p=97,q=11,j=1\)：二点关联格 \(C_{11}\)

这里

\[
B=24,\qquad\beta_1=6,\qquad M_1=1,\qquad
\mathcal O_1=\{6,17\}.
\]

两个规范顶点为

\[
v_6=(D,A)=(6,1),\qquad v_{17}=(17,1),
\]

且

\[
\Theta_1(e_{17}-e_6)=1,\qquad
L_0/\ker\Theta_1\simeq C_{11}.
\tag{26}
\]

对核心相位 \(2,9\)，映射

\[
\tau_1=8\gamma+6\pmod {11}
\]

分别给出数字 \(0,1\)。所以旧结果中的二点横向映射现在有了精确跨纤维 source-SNF；
但 \(M_1<10\)，它仍不是全部相位支撑的 lift，也不属于任一单纤维单位群。

### 5.2 \(p=97,q=3,j=1\)：完整窗口正控制

此时

\[
\beta_1=2,\qquad M_1=7,\qquad
\mathcal O_1=\{2,5,8,11,14,17,20,23\}.
\]

首三个 owner \(2,5,8\) 的数字为 \(0,1,2\)，规范顶点分别是

\[
(D,A)=(2,1),(5,1),(4,2).
\]

所以任意 \(\mathbb F_3\) phase support 都可由 (22) 完整提升。这里
\(\beta_2=5\)，故 \(\delta_1=1\)：\(s=5\) 的高度至少 2，而 \(s=2,8\) 的
高度恰为 1，精确验证第 4 节的 depth--rank 分派。

### 5.3 \(p=73,q=17,j=1\)：单 owner 零秩边界

这里

\[
B=18,\qquad\beta_1=3,\qquad M_1=0,\qquad
\mathcal O_1=\{3\}.
\]

虽然 \(73+4\cdot3=85\) 具有精确 17-height 1，但没有第二个横向数字，故
\(L_0=0\) 且横向秩为零。这说明 exact-height owner 的存在本身不够支付 source rank。

## 6. 对统一选择器的修正

odd-Hall 路线应改为

```text
ODD_HALL_SOURCE_RANK(q)
  -> OWNER_WINDOW(p,q,j)
       -> fixed (D,A) fiber: TRANSVERSE_RANK_ZERO_NO_GO
       -> fiber-incidence lattice L_0
            -> Theta_j rank 0: OWNER_WINDOW_RANK_DEFICIT
            -> Theta_j rank 1: CANONICAL_C_q_SOURCE_SNF
                 -> full affine record lift: INCIDENCE_PHASE_LIFT_VERIFIED
                 -> basis only: PARTIAL_PHASE_SUPPORT
```

这解决了“横向数字应放在哪个 source-SNF 中”的问题，并严格排除了同纤维目标。
它尚未证明任意 phase 指派都保留原记录的算术来源，也未把关联格的 \(C_q\) 商变成
某个单一 Type II 因子积块，更没有为跨纤维边给出 E4/E5。因此
`INCIDENCE_PHASE_LIFT_VERIFIED` 仍是规范格证书而非递归边。下一决定性缺口已从
“寻找同纤维 q-primary 单位群”收缩为：将关联格边上的 shared-\(q\) 来源与实际
记录来源、因子选择/Hall--Rado 门组合，或者在组合失败时构造保持标记的严格
跨纤维下降。

## 聚焦验证

```bash
python3 reproductions/type_i_odd_owner_fiber_incidence_lattice_source_map.py --verify
```

该 verifier 只重算三个控制的 owner 窗口、规范 Type II 顶点、横向关联格秩、
仿射 lift 和高度分派，不运行历史扫描。
