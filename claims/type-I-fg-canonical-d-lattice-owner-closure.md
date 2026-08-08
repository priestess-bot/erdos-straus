---
kind: claim
claim_id: type-I-fg-canonical-d-lattice-owner-closure
title: 固定 D 一跳 F/G source-map 的 canonical—SNF—owner 闭合三分
statement: 固定核心素数 p、原始 D 和声明的一跳保持来源 D-格 universe。canonical D-格原子菜单对该 universe 有限且 source-complete；把其行附加到 H x Z/eZ 的带标记表后，任意有限 F/G 角色请求先按 marked-SNF 分为 source-menu group/label escape、source-target phase obstruction 或相位已实现。对 G 型源差分恒等角色，直接得到支撑分离且 q 需求为零；对 F 型非恒相位，只有与 beta_h(p)=-p*4^{-1} (mod q^h) 对齐且 owner 表存在时才进入 q-prefix owner。进入后继承 tight/slack/strict q-deficit 分解和 q-adic 边界。p=57,399,241、D=41 的完整原始 canonical 菜单对 C2 非剩余 escape 给出显式 G residual；D'=1 的非剩余因子明确属于下一层，不被伪装成当前递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-escape-canonical-d-lattice-source-menu
  - type-I-fg-marked-source-menu-saturation
  - type-I-fg-fourier-phase-owner-capacity-bridge
  - type-II-qprefix-owner-escape-capacity-decomposition
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - canonical-menu
  - divisor-lattice
  - marked-SNF
  - Fourier
  - owner-map
  - q-prefix
  - capacity
  - residual-escape
  - proof-program
sources:
  - claim: type-I-linear-escape-canonical-d-lattice-source-menu
    role: finite-D-source-completeness
  - claim: type-I-fg-marked-source-menu-saturation
    role: marked-group-saturation-and-phase-obstruction
  - claim: type-I-fg-fourier-phase-owner-capacity-bridge
    role: phase-alignment-and-owner-capacity
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: tight-slack-deficit-split
  - reproduction: reproductions/type_i_fg_canonical_d_lattice_owner_closure.py
    role: p57399241-D41-G-residual-control
visibility: public
last_checked: '2026-08-09'
---

# 固定 \(D\) 一跳 F/G source-map 的 canonical—SNF—owner 闭合三分

## 1. 声明的有限 universe

固定核心素数 \(p\) 和正整数 \(D\)，只声明一跳、保持来源的 D-格 universe
\(\mathfrak U_D^{(1)}\)：

\[
\mathcal A_D(p)=
\{a:a\mid D,\ D/a\text{ 平方自由},\ 4aD<p\},
\]

\[
\mathcal L_D(p)=
\{(D',A):D'\mid D,\ A\mid D',\ D'/A\text{ 平方自由},\ 4AD'<p\}.
\]

一条原子 route 是 \((a,D',A,q)\)，其中

\[
q\mid p+4Da,
\qquad
q\mid p+4AD',
\]

并保留最大共同高度

\[
e_{a,D',A,q}
=\min\{v_q(p+4Da),v_q(p+4AD')\}.
\tag{1}
\]

对每个 route 只允许选择一个前缀 \(1,\ldots,e_{a,D',A,q}\)，重复 q 先由 shared-q
ledger 合并。由 D-格 canonical menu 定理，原子菜单
\(\mathcal E_D^{\mathrm{can}}(p)\) 有限，并对该声明 universe source-complete；其
大小满足

\[
|\mathcal E_D^{\mathrm{can}}(p)|
\le \tau(D)^3\lfloor\log_2(2p)\rfloor.
\tag{2}
\]

式 (2) 只量化这一声明 universe，不包括 raw、外部 F/G alternate 或下一递归层。

## 2. 带标记 source table 与 SNF 门

固定目标纤维 \(f=(D',A)\)，令 \(H_f\) 为其有限单位群或已经固定的源差分商，令
\(E=\mathbb Z/e\mathbb Z\) 是当前角色标签群。完整 canonical source table 记为

\[
\mathcal A_f\subseteq H_f\oplus E,
\]

其中每一行保存真实 route、群像和 phase/source 标签。当前有限菜单为
\(\mathcal M_f\subseteq\mathcal A_f\)。假设完整表已通过独立 canonical
source-completeness，且

\[
V(\Gamma(\mathcal A_f))=0,
\qquad
\Gamma(\mathcal B)
=\langle(u,\lambda):(u,\lambda)\in\mathcal B\rangle.
\tag{3}
\]

则有限 SNF 给出：

1. 若 \(\Gamma(\mathcal M_f)\ne\Gamma(\mathcal A_f)\)，取字典序最小的失败行；
   若其群坐标不在菜单投影子群中，输出
   'MARKED_SOURCE_MENU_GROUP_ESCAPE'；若群坐标已在投影中但标签关系失败，输出
   'MARKED_SOURCE_MENU_LABEL_RELATION_OBSTRUCTED'；
2. 若 \(\Gamma(\mathcal M_f)=\Gamma(\mathcal A_f)\)，再把目标表
   \(\mathcal T_f\) 加入。若
   \[
   V(\Gamma(\mathcal M_f)+\Gamma(\mathcal T_f))\ne0,
   \]
   输出 'MARKED_TARGET_PHASE_RELATION_OBSTRUCTED'；
3. 若上式的竖直交集为零，则 source-target phase 已由某个复角色实现，输出
   'F_FOURIER_SOURCE_TARGET_LIFTED'，但尚未称为 q-height 或递降边。

这是一个穷尽的有限 SNF 三分：source menu 逃逸、source-target 关系障碍和 phase
实现互斥。固定 q-primary 阶仍需 exact-order SNF 门；一般复角色延拓不能替代它。

## 3. 与 F/G 角色和 owner 容量的接线

令 \(\Delta_Q\) 是当前目标指数纤维的源支撑差分群。

### G 型

若规范角色在 \(\Delta_Q\) 上恒等、在目标支撑陪集上非恒等，则 SNF/角色回执直接为

\[
\mathrm{G\_SUPPORT\_SEPARATION},
\qquad
R_j=0\quad\text{for every q-prefix layer }j.
\tag{4}
\]

G 型支撑分离不进入 Type II q 容量；它可以在非平凡源商上形成严格群商，但不能把
角色阶再收费一次。

### F 型未对齐或未闭合

若角色在 \(\Delta_Q\) 上非恒等，先由 F/G 角色—源秩桥产生
\(\mathrm{SOURCE\_RANK\_DEMAND}(q)\)。只有以下条件同时成立才可进入 owner：

\[
\gamma_i\equiv-p4^{-1}\pmod{q^{h_i}},
\qquad
s_i\equiv\gamma_i\pmod{q^{h_i}},
\tag{5}
\]

且有限 source table 已通过第 2 节的 canonical/SNF 饱和。

若第一同余失败，输出 'FOURIER_PHASE_OWNER_NONIDENTIFIED'；若第一同余成立但
有限标签表找不到 \(s_i\)，输出 'FOURIER_PHASE_NO_LOCAL_LIFT'；若 canonical
source universe 之外仍有未枚举来源，保留 'F_SOURCE_MAP_UNCLOSED'。这三类都不
进入 q 容量。

### F 型已实现 owner

若 (5) 对完整 table 通过，且每个真实 source column 有唯一 owner，定义

\[
e_i=v_q(p+4s_i),
\qquad
O_j=\{i:e_i\ge j\},
\qquad
C_j=\max_{a\bmod q^j}\#\{s_i:s_i\equiv a\pmod{q^j}\}.
\tag{6}
\]

则 q-prefix owner 分解直接给出

\[
\Delta_j=C_j-|O_j|\ge0,
\tag{7}
\]

\[
(R_j-\mu C_j)_+
=\bigl((R_j-\mu|O_j|)_+-\mu\Delta_j\bigr)_+.
\tag{8}
\]

若 \(i\notin O_j\)、\(e_i=k<j\)、且 \(O_j\ne\varnothing\)，任取 \(a\in O_j\)，则

\[
\boxed{v_q(s_i-s_a)=k.}
\tag{9}
\]

因此 owner 分支只有三种 typed 结果：

* \(\Delta_j=0\)：紧链 owner escape；若 \(R_j>\mu|O_j|\)，同时是严格
  'Q_ADIC_LAYER_CAPACITY_DEFICIT'；
* \(\Delta_j>0\)：至多 \(\mu\Delta_j\) 的缺口可尝试通过 alternate-owner
  source-switch，不能把松弛自动当作已有边；
* \(R_j>\mu C_j\)：完整残类容量也不足，直接是严格 q 进超载。

## 4. 闭合定理

对固定 \(D\)、固定目标纤维和有限 F/G 角色表，按下列优先级运行：

\[
\boxed{
\begin{array}{rcl}
\text{canonical route 未在菜单中}
&\Rightarrow&\text{SOURCE\_MENU\_GROUP/LABEL\_ESCAPE};\\
\text{菜单饱和但 source-target 有竖直关系}
&\Rightarrow&\text{TARGET\_PHASE\_RELATION\_OBSTRUCTED};\\
\text{G 源差分恒等}
&\Rightarrow&\text{G\_SUPPORT\_SEPARATION};\\
\text{F phase 未与算术残类识别}
&\Rightarrow&\text{OWNER\_NONIDENTIFIED/NO\_LOCAL\_LIFT};\\
\text{F phase 与 owner 对齐}
&\Rightarrow&\text{紧链/松弛/q-deficit 分派 (7)--(9)}.
\end{array}}
\tag{10}
\]

每一行都有有限 SNF、整数 q-adic 或 canonical route 见证。由 canonical menu
source-completeness，声明 universe 内不存在未枚举的 primitive source；若最小失败行
来自菜单外，它被明确标为 'SOURCE_UNCLOSED'，不能被误写成当前 universe 的空集。

### 证明

式 (1)--(2) 和 source-completeness 给出有限原子菜单及其穷尽性。对固定目标纤维，
带标记 source saturation 的 SNF 等价式给出第 2 节三分；竖直关系恰是联合 source—
target 标签的相位矛盾。G/F 的源差分恒等/非恒等给出第 3 节前两类分派。

在 F 对齐分支，由 \(q\nmid4\)，式 (5) 推出 \(q^{h_i}\mid p+4s_i\)。于是
\(O_j\)、\(C_j\) 正是 q-prefix owner 分解的输入，式 (7)--(8) 由其容量恒等式得到。
若 \(e_i=k<j\) 而 \(e_a\ge j\)，相减

\[
4(s_i-s_a)
=q^k(q^{e_a-k}u_a-u_i)
\]

的括号模 q 为单位，得到式 (9)。所以 (10) 穷尽且每个回执保留了正确的算术层次。
证毕。

## 5. 实际 G residual 控制：\(p=57{,}399{,}241,D=41\)

取已有固定层控制

\[
p=57{,}399{,}241,\qquad R=59,\qquad D=41.
\]

此时

\[
\mathcal A_{41}(p)=\{1,41\},
\]

两条原始 source 行的完整因子为

\[
p+4\cdot41\cdot1
=3\cdot5\cdot7\cdot546661,
\]

\[
p+4\cdot41\cdot41
=5\cdot2861\cdot4013.
\tag{11}
\]

这些 canonical source 因子在 \(\mathbb F_{59}^{\times}\) 中全为二次剩余；它们生成
\(\langle15\rangle\)，一个 29 阶子群。声明的 escape 方向可取
\(2693\langle15\rangle\)，因为

\[
\left(\frac{2693}{59}\right)=-1.
\tag{12}
\]

因此固定 \(D=41\) 的 canonical source table 已经 source-complete，但
\(\Delta_Q\notin J_{41}\)，输出

\[
\mathrm{CANONICAL\_D\_LATTICE\_ESCAPE\_OBSTRUCTED}.
\tag{13}
\]

这不是 source-map 未闭合，也不是 Erdős--Straus 的全局 no-go；它是一个完成了有限
source-map 后的 G/F residual 对偶证书。

同一核心素数在 \(D'=1\) 层有

\[
p+4=5\cdot11{,}479{,}849,
\qquad
\left(\frac{11{,}479{,}849}{59}\right)=-1.
\tag{14}
\]

式 (14) 的非剩余来源不属于当前 \(D=41\) 一跳 universe。因而选择器必须将其记录为
'LOWER_LAYER_SOURCE_OUTSIDE_CURRENT_UNIVERSE'，而不能把 (13) 错写成已经存在的
\(41\to1\) 严格递降。

## 6. 研究边界

本定理把“固定 D 一跳 universe 内 source-map 是否闭合”从假设推进为有限、可判定的
canonical/SNF/owner 三分；并给出一个真实 G residual 控制，证明 source-complete
并不等于目标必支付。它仍不覆盖 raw、外部 F/G alternate 或递归后继，也不证明
\(D'=1\) 的来源可由当前 D=41 状态通过 E1--E5 提升得到。

全局决定性缺口现在更具体：证明未命中 F/G 状态总能落入某个声明的有限 universe，
或为 'LOWER_LAYER_SOURCE_OUTSIDE_CURRENT_UNIVERSE' 构造保持标签、严格势下降的
跨层 adapter。

## 聚焦复现

~~~bash
python3 reproductions/type_i_fg_canonical_d_lattice_owner_closure.py --verify
~~~

