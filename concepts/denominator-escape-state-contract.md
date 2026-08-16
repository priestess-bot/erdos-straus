---
kind: concept
concept_id: denominator-escape-state-contract
title: 分母缺陷逃逸的合法状态与转移合同
summary: 规定统一选择器可接受的算术状态、终端叶和递降边；所有跨状态输出必须从带符号分母缺陷出发，同时给出合法后继、正规形验证、解提升和逐边严格下降。该合同是研究规范，不声称这些输出对每个核心素数都存在。
topics:
- proof-program
- selector
- marked-solution
- signed-denominator-defect
- q-adic
- state-transition
- well-founded-descent
- type-I
- type-II
- dyadic-terminal
used_by:
- type-I-f-denominator-clearing-qadic-lift-contract
- type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
- type-I-f-psi-one-nearest-fiber-escape-boundary
- type-I-generalized-dyadic-natural-lift-equivalence
- type-I-generalized-dyadic-standard-even-lift-boundary
- type-I-canonical-complete-support-rechart-g-obstruction
- type-I-psi-one-full-spectrum-terminal-descent-boundary
- type-I-formal-target-pair-descent-cycle-boundary
- type-I-formal-external-slab-collision-absorption-rechart
- two-denominator-lift-d-only-marked-normal-form
- two-denominator-lift-source-supported-tail-ratio-rigidity
- type-I-formal-linear-chart-p-transience-large-slab-anchor
- type-I-phase-labeled-candidate-selector-well-founded-schedule
- type-I-marked-support-accumulation-rechart-saturation
- type-I-large-slab-three-alpha-arithmetic-boundaries
- type-I-overflow-d-only-square-excess-no-go
- two-denominator-lift-same-one-mod-four-no-go
- type-I-bottom-sink-scc-complete-excess-bundle-selector
- type-I-universal-p-source-capacity-anchor-orbit
- type-I-overflow-determinant-fixed-n-dual-support-conflict
- type-I-overflow-fixed-n-bounded-divisor-saturation
- type-I-overflow-unbounded-full-product-quotient-fold
- type-I-overflow-full-product-d-one-g-anchor-retention-rigidity
- type-I-overflow-cofactor-r-chart-support
- type-I-overflow-outer-rank-reset
- type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
- type-I-high-support-rank-aware-sink-bundle-selector
- type-I-high-support-bundle-carry-capacity-terminal-dispatch
- type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
- type-I-high-support-c2-centered-vieta-antipodal-no-go
- type-I-high-support-c2-rank-one-retention-exhaustion
- type-I-p-minus-one-equal-tail-marker-capacity-terminal-collapse
- type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
- type-II-p-minus-one-endpoint-envelope-large-prime-allocation
- type-II-p-minus-one-divisor-downset-prime-power-allocation
- type-I-overflow-d-one-p-minus-two-g-rechart
- type-I-unified-terminal-first-selector-contract
- type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
- type-I-source-lattice-qheight-dual-valuation-shift-carrier
- type-II-odd-kernel-overflow-natural-tail-relation-graph
- type-II-relation-reach-proper-endpoint-descent
- type-II-relation-reach-gcd-shadow-endpoint-descent
- type-II-q-one-full-carrier-phase-root-entry
- type-II-q-one-full-carrier-second-anchor-fixed-n-macro
- type-I-path-anchored-atomic-split-complete-excess-admission
sources:
- claim: marked-solution-descent-closure
  role: marked-state-and-solution-lift-criterion
- claim: type-I-f-current-block-saturation-and-signed-denominator-defect
  role: signed-defect-and-current-block-boundary
- claim: type-I-f-denominator-clearing-qadic-lift-contract
  role: q-adic-necessary-lift-interface
- claim: type-I-coprime-factor-normal-form
  role: type-I-normal-form-verifier
- claim: type-II-coprime-factor-normal-form
  role: type-II-normal-form-verifier
- claim: type-I-general-dyadic-terminal-transfer
  role: generalized-dyadic-terminal-verifier
- claim: type-I-p-minus-one-equal-tail-marker-capacity-terminal-collapse
  role: equal-tail-source-admission-and-terminal-collapse
- claim: type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
  role: fixed-source-rank-Type-II-finite-menu-and-capacity-bound
- claim: type-II-p-minus-one-endpoint-envelope-large-prime-allocation
  role: endpoint-capacity-large-prime-allocation-and-complete-F-G-empty-dispatch
- claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
  role: divisor-downset-forbidden-antichain-and-prime-power-allocation
- claim: type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
  role: Type-II-signed-box-physical-occurrence-and-range-terminal
- claim: type-II-relation-reach-proper-endpoint-descent
  role: source-reachable-proper-endpoint-E1-E5-contract
- claim: type-II-relation-reach-gcd-shadow-endpoint-descent
  role: universal-q-owned-shadow-endpoint-E1-E5-and-q-one-base
- claim: type-II-q-one-full-carrier-phase-root-entry
  role: ordinary-q-one-G-to-fresh-full-carrier-Type-I-phase-reindexing
visibility: public
last_checked: '2026-08-15'
---

# 分母缺陷逃逸的合法状态与转移合同

## 1. 地位与目的

本文件是一份**证明对象规范**，不是存在性定理。它规定“表示--对偶--容量”统一选择器
何时可以把一次计算、同余变换或关系格操作登记为：

1. 一张直接 Type I/II 短证书；
2. 一个已经闭合的广义 \(2^j\) 终端；或
3. 一条严格可提升的跨状态递降边。

它不声称对每个核心素数都能产生上述输出。全称目标仍然是证明：对每个
\(p\equiv1\pmod {24}\)，选择器必停在直接短证书，或沿本合同认可的良基边到达这样的
终端。

本合同采用以下方向约定：

\[
S\longrightarrow T
\]

表示证明搜索从当前状态 \(S\) 递归到更小状态 \(T\)；相应的解提升方向相反：

\[
\Phi_{T\to S}:W_T\longrightarrow W_S.
\]

直接 Type I/II 命中是**终端叶**，没有后继状态，因而不伪造“严格下降”。任何实际写出
后继 \(T\) 的输出都是边，必须通过第 5 节的全部五项检查。

## 2. 合法状态模式

一个可进入递归选择器的状态 \(S\) 必须携带下表中的字段。字段可以由 Markdown、JSON
或证明助理对象实现，但其数学语义不得改变。

| 字段 | 必须记录的内容 | 验证要求 |
|---|---|---|
| state_id | 内容寻址或可重复生成的状态标识 | 由全部规范字段重算；不得依赖枚举顺序 |
| equation_target | 根状态取 \(4/p\)；广义标记状态取既约 \(c_S/n_S\)，并记录根素数 \(p_0\) | \(c_S,n_S>0\)、\((c_S,n_S)=1\)；根状态必须有 \(c_S=4,n_S=p_0\) |
| marked_solution_set | 明确定义的 \(W_S\subseteq\operatorname{Sol}(c_S,n_S)\) 及标签 \(\theta_S\) | 不预设 \(W_S\ne\varnothing\)；成员判定条件必须有限且可核验 |
| induction_rank | \(\rho(S)\in\mathbb N\)；普通状态默认 \(\rho(S)=n_S\) | 若不取 \(n_S\)，必须证明该秩与解提升合同相容 |
| modulus_context | 合法模数 \(R_S\)、同余类型和定义 \(R_S\) 的整数恒等式 | 检查正性、奇偶、所需模 \(4\) 类、互素性及全部整除条件 |
| K_context | \(K_S\)、完整素因子赋值 \(\nu_{S,q}=v_q(K_S)\) 与支撑 \(\mathcal Q_S\) | 重乘得到 \(K_S\)；根线性状态还须验证 \(4K_S=p_0R_S+1\) |
| absorbed_support | 默认取 \(1\)；兼容字段名保留，但语义扩展为 charged support \(A_S\mid K_S\) | verifier 重算整除；边回执记录 bundle 或 overflow-determinant provenance；该字段只增不减，除非由更外层秩支付重置 |
| source_tree_scope | 来源树域：通常为 `charged_history_only`；结构化 raw 默认根及其后继为 `fresh_source_tree_only` | 纳入 state_id；`fresh_source_tree_only` 只能由具名 root-entry 创建并沿边原样传播，任何 charged-history 入边都不得生成它 |
| target_fiber | \(\phi_S(z)=\prod_{q\in\mathcal Q_S}q^{z_q}\bmod R_S\)、目标相位 \(\tau_S\)、关系格 \(\Lambda_S=\ker\phi_S\) 和带类型的纤维状态 | F/hit 记录规范见证；G 记录 `status=empty` 及分离角色，不伪造纤维元素 |
| signed_defect | F/hit 对一个**全局定向**见证 \(z\) 记录 \(D^-(z),D^+(z)\)；G 记录 `status=not_applicable` | 非空时必须按式 (1) 重算；不得逐坐标拼接 \(z\) 与 \(-z\)，也不得用零向量冒充 G 态缺陷 |
| certificate_context | F/G 分类以及实际使用的规范 Fourier 角色、关系格基或加法组合证书 | 写明规范选择规则、完备性范围、哈希或精确代数见证 |
| normal_form | 当前状态所属的 Type I、Type II、marked-source、dyadic 或其它已定义正规形 | 调用具名 verifier；“由搜索程序生成”本身不是验证 |
| potential_record | 候选势函数方案、重算值和比较顺序 | 每个分量取值于明示的良基集合；不得使用只对冻结图定义的拓扑编号 |

这里

\[
\operatorname{Sol}(c,n)=
\left\{(x,y,z)\in\mathbb N^3:
\frac cn=\frac1x+\frac1y+\frac1z
\right\}.
\]

允许 \(c_S\ne4\) 的目的，是容纳确有显式解提升的标记分子状态；这并不自动扩大可用
状态类。任何新 \((c_S,n_S)\) 都必须定义 \(W_S\)、给出合法正规形，并在边上证明
\(\Phi_{T\to S}\) 对 \(W_T\) 的每个元素都有定义。

### 2.1 F、G 与 hit 的类型化纤维字段

状态合同必须允许 G 态的目标纤维严格为空。三种分类使用互斥模式：

```text
hit/F:
  target_fiber.status = nonempty
  target_fiber.witness = <canonical exponent vector>
  signed_defect.status = defined

G:
  target_fiber.status = empty
  target_fiber.emptiness_certificate = <canonical separating character>
  signed_defect.status = not_applicable
  signed_defect.reason = G_empty_target_fiber
```

G 态的 `not_applicable` 是类型信息，不是数值零。验证器必须重算分离角色在所有
\(q\mid K_S\) 上为平凡、而在目标相位上非平凡。任何从 F/hit 换图表到 G 的边还必须
重新计算分类；不得继承旧图表的见证或缺陷。

这个修订只使 G 图表成为可准确记录的状态，不会自动证明其
`marked_solution_set` 非空，也不会给出解提升。若边使用与图表无关的
\(W_S=\operatorname{Sol}(p_0)\)，必须单独验证提升映射和良基势；若使用中心标记集，
G 态的该集合为空，不能作为递降来源。

### 2.2 合法模数与分析商对象的分离

满足 \(t\mid R\) 的商模数、稳定子商 \(Q/T\) 或某个投影群，可以作为
certificate_context 中的分析对象，但它们默认不是新的算术状态。要把商模数 \(t\)
登记为后继，必须重新构造完整的 equation_target、modulus_context、K_context、
marked_solution_set 和 normal_form。例如 \(t\equiv1\pmod4\) 的商表示不能在没有
额外桥接时冒充要求 \(R\equiv3\pmod4\) 的 Type I 状态。

### 2.2a 固定层商 Fourier 的 typed 对偶证书

固定层稳定子约化产生的是 `certificate_context`，不是第六种递归边。其规范载荷为：

```text
certificate_type = fixed_layer_quotient_fourier
selector_status = analysis_evidence
state_class = F 或 G
phase = DUAL_CERTIFICATE
quotient_order = |H/P|
stabilizer_order = |P|
character_order = ord(chi_bar)
amplitude_squared = |A_J(chi)|^2
threshold_fraction = [|bar J| product_i(2 b_i + 1), |H/P|-1]
lifted_threshold_fraction = [|J| product_i(2 b_i + 1), |H/P|-1]
finite_order_debt_fraction = [numerator, denominator]
carrier_mapping_status = unproved
recursive_edge_eligible = false
```

固定目标的计数字段必须使用 `N_J(t)=N_bar(pi(t))`，而不能把 `|P|` 乘入单个目标；
`|P|` 只在目标陪集求和时出现。Fourier 系数则在 `P^perp` 上按 `|P|` 放大、其外
为零。由于 `amplitude_squared` 与阈值分数可以用整数/有理数保存，typed 回执不依赖
浮点相位。规范选择键为
`(|H/P|, ord(chi_bar), -|A_J(chi)|^2, phase(chi_bar))`。

`finite_order_debt_fraction` 记录
\(
\sum_{\bar\chi(\pi(q_i))\ne1}\min\{1,(b_i/d_i)^2\}
\)
的精确有理数；它属于表示—对偶分析字段。`carrier_mapping_status` 在没有把角色阶、
方向颜色和 \(q\)-进载荷连接起来之前必须保持 `unproved`，因此该字段不能增加递归边
资格或替代 E1--E5。

该对象只能说明状态内 F/G 对偶结构。若要升级为 `support_switch`、`q_adic_lift` 或
`verified_edge`，仍必须重新完成第 4 节的 E1--E5 和全域解提升；稳定子商阶下降或
Fourier 幅度超过阈值本身不能承担递归。

### 2.2b 终端优先的统一 typed 回执

近邻偶前驱、广义 \(2^j\) 偶前驱和商 Fourier 证书共用以下选择顺序：

```text
direct_type_i_or_type_ii
target_fiber_neighbor_terminal
generalized_dyadic_terminal
fixed_layer_quotient_fourier
```

前两类回执必须保存 `terminal_kind=even_predecessor`、标准偶方程解和
`lift_status=unproved`；在没有非空标记集、全域解提升和严格势下降时，统一保持
`selector_status=analysis_evidence`、`recursive_edge_eligible=false`。这使“较小偶数
前驱”与真正的 `terminal_leaf` 或 `verified_edge` 在类型上分离。精确的近邻、二进和
对偶字段见[Type I 终端优先统一选择器合同](../claims/type-I-unified-terminal-first-selector-contract.md)。

### 2.2c q 进清分相位胞容量字段

固定 \(B\) 的盒外见证还可以输出一个精确的相位中心：若奇素数 \(q\) 的盒外高度为
\(e>0\)，则所有保留该固定分母局部结构的清分移位都满足

\[
s\equiv-A R^{-1}\pmod{q^e}.
\]

跨状态使用该条件时，不能只记录 \(e\)。必须同时保存：

```text
phase_clearing_prime = q
phase_clearing_height = e
phase_center_modulus = q**e
phase_center_residue = -A * inverse(R, q**e) mod q**e
phase_cell_id = explicit compatible-cell identifier
phase_cross_determinant = A_i * R_j - A_j * R_i, for a pair
phase_separation_height = v_q(phase_cross_determinant), or null if it is zero
phase_label = bounded integer representative, if one is supplied
phase_label_interval = [lower, upper], if one is supplied
phase_label_multiplicity_bound = mu
phase_capacity_status = compatible / incompatible / unproved
```

只有在同一 `phase_cell_id` 中验证

\[
\gamma_i\equiv\gamma_j
\pmod{q^{\min(e_i,e_j)}}
\]

并且标签落在已给出的有限区间时，才可调用
[q 进清分相位胞与跨状态容量合同](../claims/type-I-phase-clearing-cell-capacity-contract.md)。
相位胞兼容可以直接由 `phase_cross_determinant` 的 \(q\)-进赋值重算：共同高度为
\(k=\min(e_i,e_j)\) 时，兼容当且仅当 \(q^k\) 整除
\(A_iR_j-A_jR_i\)；小于 \(k\) 的赋值是明确的分离层数。
标签重复必须乘入显式重数；相位不兼容的状态不得共享同一个容量账本，但可以按
上述兼容关系分成两两兼容的等价胞。每个胞的首层相位是非零残基，但不同胞可能
共享同一个首层残基，因此 `phase_cell_count <= q - 1` 需要额外的
`phase_first_layer_residue_injective=true` 假设。若第 \(c\) 个胞的标签区间宽度为
\(M_c\)、最大高度为 \(H_c\)，且全局重复度上界为 \(\mu\)，则可逐胞记录

```text
phase_cell_first_layer_residue = nonzero residue mod q
phase_cell_height_sum = sum(e_i) within the cell
phase_cell_capacity_bound = mu * (M_c/(q-1) + H_c)
phase_first_layer_residue_injective = explicit additional hypothesis
phase_layer_profile = [{height, modulus, active_state_count,
  distinct_phase_residue_count, phase_residues, layer_capacity_bound}]
phase_diversity_tax = sum_k mu*(D_k-1)*(floor(M/q**k)+1)
```

并核验

\[
\sum_i e_i
\le
\mu\sum_c\left(\frac{M_c}{q-1}+H_c\right).
\]

当不同等价胞在更高层继续分裂时，逐层残基谱还给出

\[
D_k=\#\{\gamma_i\bmod q^k:e_i\ge k\},
\qquad
\sum_i e_i
\le
\mu\sum_{k=1}^{H}
D_k\left(\left\lfloor\frac{M}{q^k}\right\rfloor+1\right).
\]

这条相位树界不需要把等价胞数压到 \(q-1\)；`phase_diversity_tax` 显式记录相对于
每层单残基界的高层相位分裂成本。它仍以每个胞存在有界清分标签为前提；若首层
残基不满足单射，就不能把逐胞求和压缩成单个 \(M\) 项。最小正相位代表只是诊断标签，不自动提供
正性、标记解非空、解提升或 E1--E5，因此这些字段默认属于 `analysis_evidence`，
不能把 `carrier_mapping_status=unproved` 升级为递归边。

### 2.3 累积外部支撑状态

linear_absorbed_support_v1 是一个已定义的线性图表子类型。字段名为兼容既有 artifact
继续保留；从 v2 边开始，其数学语义是 **charged support ledger**，既包括实际吸收的
complete-excess block，也包括由已验证 overflow determinant 收费的规范因子。它保持

\[
\texttt{equation\_target}=4/p_0,
\qquad
W_S=\operatorname{Sol}(4,p_0),
\qquad
A_S\mid K_S.
\]

该子类型的 state_id 由版本号、\(p_0,R_S,A_S,\texttt{source\_tree\_scope}\) 生成；\(K_S\)、完整因子分解、
目标纤维、F/G/hit、规范见证或分离角色、带符号缺陷及势均从这些字段确定性重算。
重图表时不得继承旧 F/G 标签，也不得只记录新的模数。

若 v1 clean external receipt 给出 \(Q=q^e\)、\(q\nmid K_S\)，则合法累积边只能把
\(A_S\) 更新为 \(A_SQ\)。任意其它更新都不是该 v1 正规形。完整构造、具名 verifier、
恒等解提升和势证明见
[外部支撑累积重图表的良基下降与 overflow 边界](../claims/type-I-marked-support-accumulation-rechart-saturation.md)。

更一般地，bottom sink-SCC 的最小节点会给出 `complete_excess_bundle`：若

\[
Q=\prod_{v_q(y)>v_q(K_S)}q^{v_q(y)},
\]

则 \(Q\) 可以是复合数，也可以含 \(K_S\) 已有的素数。此时规范更新是逐素数容量并

\[
\boxed{A_T=\operatorname{lcm}(A_S,Q),}
\]

不能一般写成 \(A_SQ\)。所以 absorbed_support 记录的是带指数的乘法容量承诺，不只是
素数 radical。完整 bundle receipt、lcm 来源规则和 marked edge 见
[底层汇 SCC 的完整超额 bundle 选择器](../claims/type-I-bottom-sink-scc-complete-excess-bundle-selector.md)。

bundle receipt 允许两种 E1 provenance：

1. `sink_minimum`：重放完整 sink-SCC，并由最小小坐标证明剩余侧落入 \(K_S\) 容量；
2. `path_anchored`：重放从已验证 source 到该 bottom 节点的完整路径，并直接逐素数验证
   \(x\beta\mid K_S\)、\((Q,x\beta)=1\) 与 \(Q\nmid K_S\)。

第二种不能冒充第一种，但一旦这些整数条件成立，后续 lcm 更新、恒等解提升和势下降
完全相同。特别地，source-anchored clean \(Q=q^e,\ q\nmid K_S\) 可以沿 \(q\)-peeling
到达 \(\{1,R-1\}\)，再从该 anchor 构造新的 complete-excess bundle。

另有一个不可还原成两条单侧 action 的双色 primitive：
`path_anchored_atomic_split_complete_excess_v1`。若同一条已绑定 source 的 raw path
到达 \(x+y=R\)，且两侧唯一完整超额块 \(Q_x,Q_y>1\) 都 \(p\)-free，则 receipt
必须把该 path/node occurrence 作为单一 owner，原子携带两个有颜色 payload，并更新

\[
A_T=\operatorname{lcm}(A_S,Q_x,Q_y).
\]

它不得在同一 action 内导出两个可独立调度的旧单侧 token；跨 action 的全局 one-use
只有在强制 owner ledger 进入 target identity 时才能声称。E1--E3 schema 必须重算双色
maximality、canonical occurrence、逐素数 charge conservation、scope 和 canonical
typed target，并以通用 source/target validator 成功为前提；E4 仍取
\(\operatorname{Sol}(p)\) 恒等映射。若 \(A_S>B_p\)，E5 的精确额外门为
\(K_T/A_T<K_S/A_S\)；未通过者不能登记 standalone edge，只能被 guard 抢占、保留为
evidence，或作为从真实 persistent parent 一次重放的严格宏内 checkpoint。完整条件
表示定理、非最大分块反例和 stutter 宏边界见
[双侧完整超额原子来源的条件准入 schema](../claims/type-I-path-anchored-atomic-split-complete-excess-admission.md)。

当前 raw 合同还有一个对所有 F/G/hit 图表统一的具名来源：

\[
\texttt{universal\_p\_source\_v1}:
\qquad
(U,V,m)=\bigl(p,R(p-1)-p,p-1\bigr).
\]

verifier 检查 \(V>0\)、\((U,V)=1\)、\(p\nmid K\)，再重放唯一的 \(q=p,t=1\)
边并核对终点为 \((1,R-1,1)\)、gcd reduction 为 \(1\)。因此 G 的空目标纤维不再意味
没有实际形式源；该边只承担 E1 path provenance，不是递归状态边。证明见
[通用 \(p\) 源与容量锚点轨道](../claims/type-I-universal-p-source-capacity-anchor-orbit.md)。

一个更窄的根构造可把该 raw source 接到新鲜的默认支撑：只有同一回执额外序列化
`state_origin=universal_raw_default_entry_v1`、`state_scope=fresh_source_tree_only`、
\(A=1\) 的 anchor orbit 和 complete-excess bundle 时，才允许创建该 source tree 的
默认根。这个入口本身仍不是递归边，也不能从任意 \(A>1\) 的 charged history 调用来
重置支撑；它只为随后的 path-anchored bundle/overflow 产生一个 source-local 的合法
前提。该根和它的后继必须把 `source_tree_scope=fresh_source_tree_only` 写入状态；
选择器只允许它在这里创建并沿边原样传播。缺少这个结构化入口时，raw source 仍只承担 E1。

charged support 的允许来源现在有两类，必须在边回执中区分：

1. `complete_excess_bundle`：保存 `sink_minimum` 或 `path_anchored` receipt，并更新为
   \(\operatorname{lcm}(A,Q)\)；
2. `overflow_determinant`：保存产生 \(pn=4Md+1\) 的原 bundle overflow receipt，并从
   固定 \(n\) 因子图谱选择新的 \(L\)。

第二类定义

\[
S=Md=\frac{pn-1}{4},
\qquad
\mathcal W_A=
\{L:A\mid L,\ L>A,\ L\mid S,\ n<4L<p+n\}.
\]

`verify_overflow_fixed_n_charged_support_v1` 取 \(\mathcal W_A\) 的最小元素，重算

\[
R_L=4L-n,
\qquad
K_L=L\left(p-\frac SL\right),
\]

并验证 \(3\le R_L\le p-2\)、\(pR_L+1=4K_L\)、\(L\mid K_L\)、恒等解提升及
absorbed-support 势严格下降。若额外有 \(A=1\) 且 \(M<p\)，则 \(d\ge2\)，固定取
\(L=d\) 可证明该小载体子族的候选集非空；这不是任意 \(A=1\) determinant overflow
的自动性质。无 \(M<p\) 的负边界
\((p,M,d,n)=(73,1297,29,2061)\) 已由选择器作为 `analysis_evidence` 记录，见
[A=1 overflow 的小载体假设边界](../claims/type-I-overflow-a-one-generic-determinant-boundary.md)。

`overflow_determinant` 不是旧节点的 complete-excess bundle，不能把 \(d\) 伪写成
path-anchored \(Q\)。反过来，在 \(A>1\) 时也不得把支撑重置为较小对偶载体；只有
\(A\mid L\)、\(L>A\) 的边可留在当前 phase。完整证明与反例见
[overflow 固定 \(n\) 对偶图谱](../claims/type-I-overflow-determinant-fixed-n-dual-support-conflict.md)。

固定-\(n\) 分支还允许一个更宽的有界除子选择器
`overflow_fixed_n_bounded_divisor_outer_rank_v1`。令

\[
B_p=\frac{(p-1)^2}{4},
\qquad S=Md=\frac{pn-1}{4}.
\]

从全部 \(L\mid S\) 中只保留

\[
A_S<L\le B_p,
\qquad 4L>n,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A_S}\right\rfloor.
\tag{6}
\]

对任意这样的 \(L\)，回执重算

\[
R_L=4L-n,
\qquad
K_L=L\left(p-\frac SL\right),
\qquad
pR_L+1=4K_L.
\tag{7}
\]

因为 \(4L>n\) 强制 \(S/L<p\)，所以 \(K_L>0\)；\(L\mid K_L\) 和 (6) 则分别承担
E2 与 E5。该分支仍使用图表无关的 \(W_T=\operatorname{Sol}(p)\) 恒等提升，目标
\(R_L<p\) 时为 `marked_absorb`，目标 \(R_L>p\) 时为可继续处理的 overflow。
选择器按最大合格 \(L\) 规范化，但候选集为空时必须停留在
`analysis_evidence`，不得把较小对偶载体直接登记为后继。

该分支允许两种明确类型：若 \(A_S\mid L\)，后继保留旧 charged support；若
\(A_S\nmid L\)，则不能声称支撑单调，而必须把同一个
\(\Pi_A(L)<\Pi_A(A_S)\) 记录为 support_reset_paid=true 的外层秩重置。后一类
仍可使用图表无关的 \(\operatorname{Sol}(p)\) 恒等提升，但不是当前 phase 的
support-preserving 边；这一区分由回执的 support_monotone 与
outer_rank_reset 字段共同核验。

若 \(S/A_S\ge2\) 且 \(S\le B_p\)，则 \(L=S\) 自动满足 (6)；而
\(S\le B_p\iff n\le p-2\)。这只是条件性充分条件，不能替代对一般递归可达
\(A_S>1\) overflow 的有界除子存在性证明。完整引理、低互补量推论和 12 个聚焦回执见
[overflow 固定 \(n\) 的有界除子外层秩递降](../claims/type-I-overflow-fixed-n-bounded-divisor-saturation.md)。

对真实 persistent source 的完整乘积 \(S=Md\) 还有一个独立的无界 support 分支。若
\(1\le A_S\le B_p\) 且 \(S/A_S\ge2\)，令 target support 为 \(A_T=S\)，并取

\[
(M_T,d_T,n_T;A_T)=(S,1,n;S),
\qquad
R_T=(p-1)n-1,
\qquad
K_T=S(p-1).
\]

这里不要求 \(S\le B_p\)：charged state 只要求 \(A_T\mid K_T\)。严格性由

\[
\left\lfloor\frac{B_p}{S}\right\rfloor
<
\left\lfloor\frac{B_p}{A_S}\right\rfloor
\]

在 \(\Lambda_p^\sharp\) 的第一坐标支付。target 的 F/G/hit、normal form、scope 和
内容地址仍必须独立重算；因此当前它是已有 typed-adapter 准入合同下的条件性 E1--E5
分支，不能把未序列化的旧 receipt 直接升格。该规则消去全部
\(A_S\le B_p\)、\(Md>A_S\) 的算术 overflow，包括 \(M=A_S,d>1\) 的有界因子空菜单；
它的唯一严格停顿是 \(M=A_S,d=1\)。完整证明与聚焦回执见
[overflow 固定 \(n\) 完整乘积商折叠的无界 support 严格递降](../claims/type-I-overflow-unbounded-full-product-quotient-fold.md)。

若来源载体落在 \(M>B_p\)，同一有界后继还自动满足 \(L\le B_p<M\)，从而
\(R_L=4L-n<R_M=4M-n\)。选择器把它记录为 high_carrier_R_descent 次级秩；
该字段只在候选边已经通过 E1--E5 时有效，不能证明候选存在或替代全局 phase 的良基
性。详见[高载体 overflow 固定 \(n\) 有界除子的 \(R\) 严格递降](../claims/type-I-overflow-high-carrier-fixed-n-R-descent.md)。

对来源可达的 complete-excess bundle overflow，还必须优先检查同图表支撑升级。
对真实 persistent overflow receipt，只要 \(A\mid M\)、\(M/A\ge2\)，就直接把
absorbed support 从 \(A\) 升到 \(M\)，不再要求 \(M\le B_p\)。因为
\(M\mid K_M\)、\(\operatorname{Sol}(p)\) 对 chart 独立，精确秩

\[
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,\frac{K_M}{A}\right)
\]

的第一坐标若不降，第二坐标仍从
\((M/A)(K_M/M)\) 严降到 \(K_M/M\)，故完整满足 E1--E5。
若 overflow chart 只是 parent 内部 receipt，则必须比较真实 parent 与 target；
当 parent \(A\le B_p\) 时第一坐标自动严格下降，当 \(A>B_p\) 时精确门为
\(K_M/M<K_H/A\)。完整主张与 sharp 反例见
[overflow 同图表支撑升级的无界精确秩与高支撑父端点边界](../claims/type-I-overflow-unbounded-same-chart-promotion-persistence-boundary.md)。

高支撑 source 不得把该门只应用于 sink 最小节点。对 source path 已进入的有限 sink
SCC，选择器必须枚举每个定向节点的唯一完整超额分解 \(y=Q\beta\)，以
\(M_Q=\operatorname{lcm}(A,Q)\) 和规范余因子
\(c_Q=K_Q/M_Q=(4M_Q)^{-1}\bmod p\) 标价。若某行满足 \(c_Q<K_H/A\)，则其
path-anchored 宏是完整 E1--E5；若没有这样的行，完整候选表才是该 bundle 宏族的
容量 no-go。\(p=73\) 的 minimum-node 行为 \(45\to47\)，但一条额外 raw 边后的
\(Q=1247\) 行给出 \(45\to44\)。详见
[高支撑 rank-aware sink-bundle 有限选择器](../claims/type-I-high-support-rank-aware-sink-bundle-selector.md)。

若当前状态已经是 canonical 高支撑形 \(K=AC\)、\(1\le C<p\)，将候选写成
\(M=AL\) 后不得再把 target cofactor 当成黑箱。唯一 \(0\le h_L<L\) 满足
\(C+ph_L\equiv0\pmod L\)，且

\[
c=\frac{C+ph_L}{L},
\qquad
L(c-C)=ph_L-C(L-1).
\]

因此回执必须保存 `L,h,c,Delta`；只有 `Delta<0` 才通过 E5，`Delta=0` 是 stutter，
`Delta>0` 是上升。完整候选均非负时输出 `CARRY_NO_GO`，并转交
terminal、alternate、dual、total-cofactor 或 paid reset，不得把 SCC 强连通升级为
不存在的下降定理。\(p=73,C=2,A=1305\) 已给出 10 行全正的严格反例，并由直接
Type II 终端抢占；相反，既有 \(C=44\) 状态有一条 \(L=1521269\) 的
\(44\to2\) 严格边。见
[高支撑 bundle 的精确 carry 容量门、空改善反例与终端分派](../claims/type-I-high-support-bundle-carry-capacity-terminal-dispatch.md)。

最小 \(C=2\) 高支撑边界还有一个更强的专用合同。对每个核心素数，其首个边界图表为

\[
(R,K;A)=\left(2p-3,\frac{(p-1)(2p-1)}4;
\frac{(p-1)(2p-1)}8\right).
\]

任意合法 complete-excess 行都必须记录 `c>2` 和 `Delta>0`；不存在下降或 stutter，
也不得继续扩张 sink 搜索。唯一满足 \(A\mid M\mid K\) 的同图表 divisor upgrade
\(A\to K\) 需要 \(L=2\)，但 full-block complete-excess 不能生成该乘子。选择器
随后可以登记关系

\[
\rho=\frac2{2p-1}\equiv1\pmod{2p-3},
\qquad E=2(p-1),\qquad n=p-1,\qquad\alpha=A,
\]

这条自然标记现在不再保留为待判候选。写 \(p=4U+1\)，则相应中心余项为

\[
\frac{8U-1}{U(8U+1)}.
\]

反足 Vieta 递降证明它对每个 \(U\ge1\) 都不能分成两个正单位分数；因此自然标记源
对每个核心素数无条件为空，而不只是 F/G 控制上为空。见
[最小 \(C=2\) 图表的反足 Vieta 全称 no-go](../claims/type-I-high-support-c2-centered-vieta-antipodal-no-go.md)。

同一偶前驱 \(n=p-1\) 的全部双尾保持 `D-only` 尝试也已有完整分派。令

\[
\mathscr E_p=\{E:4\mid E,\ E\mid (p-1)^2/4\},
\qquad
(R_E,K_E)=\left(E-1,\frac{p(E-1)+1}{4}\right).
\]

source-supported 候选与 \(\mathscr E_p\) 一一对应；其中任一非空标记恰是
\((R_E,K_E)\) 的 centered Type I 命中，并立即恢复直接短证书。non-source-supported
候选全部为空。若 \(p-1=2^e u\)、\(u\) 为奇数，则不重复的图表容量精确为
\((2e-3)\tau(u^2)\)。固定 gap-\(7\) 单标记的边界已推广到所有等尾显式单标记：令
\(B=(p-1)/4\)、\(m=4h-1\)、\(c=B+h\)，则唯一等尾源
\((c,T_h,T_h)\in\operatorname{Sol}(p-1)\) 存在当且仅当 \(h\mid2B^2\)。对每个
准入项，保留 \(c\) 的目标纤维非空当且仅当某个 \(q\mid c^2\) 满足
\(m\mid4q+1\) 或 \(m\mid c+q\)，即原 Type I/II 终端门。因此整个等尾语法的
terminal-first 新增容量为零；它也不取代更早的标准短证书检查。见
[最小 \(C=2\) 偶前驱的跨图表重索引与双尾保持穷尽](../claims/type-I-high-support-c2-rank-one-retention-exhaustion.md)。
全参数定理见
[\(p-1\) 等尾显式标记的精确容量与单坐标终端坍缩](../claims/type-I-p-minus-one-equal-tail-marker-capacity-terminal-collapse.md)。

所以该边界的合同分派为：先跑含 gap-\(3\) 在内的标准 terminal-first 扇，再跑跨图表
有限 Type I 菜单与完整等尾适配器；全部 miss 后删除自然标记和整个双尾保持
`D-only` 分支，再转交改变保留尾的 alternate、dual、
total-cofactor 或 paid reset。完整 carry 入口证明见
[最小 \(C=2\) 边界的严格 carry no-go 与内部二进容量转导](../claims/type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction.md)。

### overflow 的 cofactor-supported r-chart 支撑升级

另一个独立的 `overflow_cofactor_r_chart_support_v1` 正规形只适用于带完整来源的
overflow。设

\[
pn=4Md+1,\qquad M=kp+r,\qquad C=p-d,\qquad
g=(A,C),\qquad a=A/g,\qquad A_C=\operatorname{lcm}(A,C)=Ca.
\]

令 \(s=(4rd+1)/p\)、\(R_r=4r-s\)、\(K_r=rC\)。接收门必须逐项重算

\[
a\mid r\Longleftrightarrow A_C\mid K_r,\qquad
p<R_r,\qquad
\operatorname{canonical\_chart}(p,A_C)=(R_r,K_r),
\]

并要求 \(A<A_C\le B_p\) 与
\(\lfloor B_p/A_C\rfloor<\lfloor B_p/A\rfloor\)。来源必须保存 universal raw source、
anchor、complete-excess bundle 和原 determinant；若 \(A>1\)，还必须保存并经具名
normal-form verifier 重放把 support 合法收费到 \(A\) 的父回执。默认 \(A=1\) 也必须来自结构化
`universal_raw_default_entry_v1`，且只在新鲜 source tree 内建立；绝不能借此抹去
另一条已收费状态的 ledger。缺少任一来源条件只能是 `analysis_evidence`。

这里的后继载体是 \(M_T=A_C\)，不是余数 \(r\)。令

\[
C_T=r/a,\qquad d_T=p-C_T,\qquad n_T=4A_C-R_r,
\]

则 \(K_r=M_TC_T\) 和 \(pn_T=4M_Td_T+1\)，所以目标重新闭合在现有 overflow
状态类型。E4 仍须显式取 \(W_S=W_T=\operatorname{Sol}(p)\) 和恒等 lift，并重算
source/target 的完整 F/G 类型；F/hit 还须重算同一全局定向的 \(D^-,D^+\)。
`r=M` 只是 `same_chart` 标记，不能作为拒绝条件。

当前回执有两个新鲜 source-tree 默认支撑的 source-local candidate 控制及一个父 ledger
缺失的分析边界。前两者的 absorbed-support 势严格下降，但尚未接入禁止后续 reset 的全局
phase scheduler，故不标为递归 `verified_edge`。详见
[overflow 的余因子支撑 r-图表候选与同图表正控制](../claims/type-I-overflow-cofactor-r-chart-support.md)。

同一 overflow receipt 还可生成 `overflow_carrier_reset_v1` 候选。取任一对偶小图表
\(t\in\{d,r\}\) 且 \(R_t<p\)，则有严格整数下降 \(t<M\)。该候选保持
\(\operatorname{equation\_target}=4/p\) 和 \(W_T=\operatorname{Sol}(p)\)，但可能丢弃
旧 \(A\)。因此它只能登记为 `candidate_transition`，除非回执同时声明不可逆的
outer phase、秩 \(\Pi_M(T)=t<M\)，以及 reset 后所有允许边的 phase-compatible E5。
当前合同不允许用 \(t<M\) 单独掩盖后续 marked 边重新增大 carrier 的可能性。

## 3. 选择器的唯一缺陷输入

对线性 F 状态，取目标纤维见证

\[
z=(z_q)_{q\in\mathcal Q_S}\in F_S,
\qquad
A=\prod_q q^{(z_q)_+},
\qquad
B=\prod_q q^{(-z_q)_+}.
\]

选择器的分母输入必须是

\[
\boxed{
d_q^-(z)=(-z_q-\nu_{S,q})_+,
\qquad
d_q^+(z)=(z_q-\nu_{S,q})_+.
}
\tag{1}
\]

其中 \(D^-(z)\) 属于 \(A/B\) 方向，\(D^+(z)=D^-(-z)\) 属于整个见证取反后的方向。
无向量

\[
e_q(z)=d_q^-(z)+d_q^+(z)=(|z_q|-\nu_{S,q})_+
\]

可以用于记录总价格或定义完整纤维距离，但不能把不同坐标分别选成正向或负向后拼成
一个不存在的见证。

尤其禁止把

\[
(e_q-h_{q,\mathrm{current}})_+,
\quad
(d_q^--h_{q,\mathrm{current}})_+,
\quad\text{或}\quad
(d_q^+-h_{q,\mathrm{current}})_+
\tag{2}
\]

作为原状态的真实残余。奇素数处，当前两个线性块已经在 \(K_S\) 中耗尽全部
\(q\)-进高度；式 (2) 会重复使用已约掉的因子。若另一个状态提供新的高度，必须通过
一条显式跨状态映射计入，而不能从当前缺陷中直接扣除。

在 \(q=2\) 处，还必须注明使用的是以 \(K\) 约分的首分母阈值，还是以 \(4K\) 约分的
形式缺口阈值。二者相差的两层不能混记为可复用容量。

完整纤维的一个规范标量可定义为

\[
\Delta_{\mathrm{den}}(S)=
\min_{z\in F_S}
\sum_{q\in\mathcal Q_S}
\bigl(d_q^-(z)+d_q^+(z)\bigr).
\tag{3}
\]

式 (3) 是候选势函数分量和状态诊断，不单独给出证书、容量注入或递降。

## 4. 允许的选择器输出

选择器只能返回下列五种带类型回执。除此之外的计算结果先登记为
analysis_evidence，不得进入递归证明图。

### 4.1 type_I_hit

至少记录

\[
m\equiv3\pmod4,\quad 3\le m\le H(p_0),\quad
x=\frac{p_0+m}{4},\quad d\mid x^2,\quad m\mid p_0x+d,
\]

以及所用短界 \(H\) 的版本。正规形 verifier 应重建互素坐标

\[
x=ABC,\qquad d=A^2C,\qquad (A,B)=1,\qquad m\mid Bp_0+A,
\]

并由这些数据恢复一组 \(4/p_0\) 的正整数分母。若目标是标记状态，还须验证恢复解属于
\(W_S\)，而不只是属于未标记的 \(\operatorname{Sol}(4,p_0)\)。这是终端叶；只有在它
另行引用较小状态时，才转而按边合同验收。

### 4.2 type_II_hit

至少记录

\[
m\equiv3\pmod4,\quad 3\le m\le H(p_0),\quad
x=\frac{p_0+m}{4},\quad d\mid x^2,\quad d\le x,\quad m\mid x+d.
\]

正规形 verifier 应重建

\[
x=ABC,\qquad d=A^2C,\qquad (A,B)=1,\qquad A\le B,\qquad m\mid A+B,
\]

并恢复目标解及标记成员关系。与 Type I 相同，直接命中是终端叶，不借用一个虚假的
“更小状态”来满足形式。

### 4.3 support_switch

该输出构造一个具有新 \(K_T\) 或新支撑 \(\mathcal Q_T\) 的合法后继 \(T\)。回执除通用
边字段外，还须记录：

1. 旧、新支撑及其赋值映射；
2. 新模数和 \(K_T\) 的定义恒等式；
3. 旧目标纤维见证如何产生新状态数据，或为何新数据可以独立重建；
4. 新状态中重新计算的 \(D_T^-,D_T^+\)，而不是把旧向量机械投影；
5. 支撑退出的素数能否在后续重入，以及势函数为何仍严格下降。

仅有 \(|\mathcal Q_T|<|\mathcal Q_S|\) 不够，因为后续边可能重新吸收已经退出的素数。

### 4.4 q_adic_lift

该输出先选择一个**全局方向**。若选择 \(z\) 方向，就只能从同一见证的非零
\(d_q^-\) 集合中取素数；若选择 \(-z\) 方向，就只能从对应的非零 \(d_q^+\) 集合中
取素数，不得逐坐标混合两个方向。只有一个构造明确要求同时处理 \(z\) 与 \(-z\) 时，
才同时登记两个带方向标签的合同。

对每个选定奇素数 \(q\)，若候选保留原局部分母指数并试图用清分子整除它，回执必须
先满足已知必要合同：若缺陷为 \(e>0\)、\(\nu=v_q(K_S)\)，则候选清分子改变量除以
\(q^\nu\) 后，必须命中由原见证唯一确定的非零模 \(q^e\) 剩余类。同一方向内的多素数
条件必须以 CRT 同时求解，不能逐素数选取彼此不兼容的替代对。降低局部分母指数、删除
该素数或切换支撑的候选不受这项同需求合同约束，但必须按其实际新状态重新验收。

但满足该同余只允许把对象标为 necessary_condition_passed。要升级为
verified_edge，还必须：

1. 显式构造替代的 \(A',B',m_0'\) 或等价整数数据；
2. 验证全部分母确实清除，而非只清除一个局部素数幂；
3. 由这些数据生成合法后继 \(T\) 或直接 Type I/II 终端；
4. 给出 \(W_T\to W_S\) 的全域解提升；
5. 验证候选良基势函数在本边严格下降。

同需求清分子合同的整数解、制造公因子后的约分端点，或一层缺陷迁移后形式参数
\(m_0\) 的下降，默认都只登记为 analysis_evidence。若约分结果回到 Type I/II 或二进
终端，应改用相应终端回执；若产生 \(K\) 不能吸收的外部分母因子，应先完成
support_switch 的全部字段。形式目标对上的势函数不是合法状态上的
potential_record，也不能替代 \(W_T\to W_S\) 的解提升。

### 4.5 generalized_dyadic_terminal

对 \(L=2K\) 的 \(2^j\) 传输，至少记录

\[
j,\ L,\ a,\ b,\quad a,b\mid L,\quad(a,b)=1,\quad
a\equiv2^jb\pmod R,
\]

以及

\[
E_j=2^{1-j}L\frac ab,\qquad
1\le j\le v_2(L)+v_2(a)-v_2(b),\qquad
a<2^jb.
\]

verifier 必须重算 \(E_j\)，检查其为偶整数、\(E_j\mid L^2\)、
\(E_j\equiv1\pmod R\)，再重建

\[
n=\frac{2L-E_j}{R},\qquad 0<n<p_0,\qquad 2\mid n.
\]

“\(n\) 为偶数”只说明它可以进入已知基例；回执仍须附上该基例的显式解或具名构造，
以及从该解到 \(W_S\) 的公式。若把它表示为边 \(S\to T_n\)，则必须验证
\(\Pi(T_n)<\Pi(S)\)；若已经在同一回执中恢复目标解，则可登记为终端叶。

对 finite-exponent F 状态还可排除一类容易误计的自然提升。若

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
n=\frac{4K-E}{R},\qquad \alpha=\frac{nK}{E},
\]

则 \(\alpha\) 自动为整数，但包含 \(\alpha\) 的较小方程解非空，当且仅当原状态已经
存在中心 Type I 除子。并且当 \(R>3\) 时，\(\alpha\notin\{n/2,n\}\)，所以偶数基例
\((n/2,n,n)\) 不能承担这个标记。证明见
[广义二进偶前驱的自然标记提升等价](../claims/type-I-generalized-dyadic-natural-lift-equivalence.md)。
因此在 F 状态中，只有上述 \(E,n\) 而没有不同的非空标记集和全域提升公式时，回执必须
标为 `unlifted_generalized_dyadic_candidate`，不得标为终端或 verified edge。

## 5. 每条边的统一回执

任何带后继状态的输出都必须含有下列五个部分，缺一项即不是证明图中的边。

### E1. premises

列出并验证所有算术前提，包括正性、整除、互素、奇偶、模类、自然范围、支撑分解、
目标纤维成员关系和方向。前提不能写成“搜索发现可行”；必须保存使其可独立重算的整数
见证。

### E2. construction

给出从 \(S\) 和有限见证 \(w_e\) 到 \(T\) 全部字段的确定公式

\[
T=C_e(S,w_e).
\]

构造必须闭合于第 2 节的合法状态类型。只输出较小模数、商群或新支撑集合，不算完成
构造。

### E3. normal_form_verifier

提供一个具名、确定性的 verifier，它至少执行

\[
\operatorname{verify\_state}(S),\quad
T=C_e(S,w_e),\quad
\operatorname{verify\_state}(T),\quad
\operatorname{verify\_edge\_normal\_form}(S,T,w_e).
\]

verifier 必须从原始整数重算派生字段，不能相信缓存的 F/G 标签、因子分解、缺陷向量
或势函数值。程序通过是算术核验的一种实现；它不能替代说明 verifier 究竟检查了哪些
恒等式。

### E4. solution_lift

给出显式全域映射

\[
\Phi_e:W_T\longrightarrow W_S.
\]

必须证明对每个 \(u\in W_T\)：

1. \(\Phi_e(u)\) 的所有分母为正整数；
2. 单位分数恒等式成立；
3. 输出满足 \(W_S\) 的全部标签条件。

只展示一个碰巧可提升的源解，不能证明映射在 \(W_T\) 上全域；此时应把 \(W_T\) 缩成
准确的可提升标记集，并继续证明该标记集非空。

若 \(W_T=\operatorname{Sol}(n)\ne\varnothing\)，则“存在某个集合映射
\(W_T\to\operatorname{Sol}(p)\)”本身与 \(\operatorname{Sol}(p)\ne\varnothing\)
等价：已知目标解总能定义常值映射。因而 E4 回执必须保存不读取目标解的显式公式及其
整数性证明；若公式由一个已知目标解定义，应把该解直接登记为 terminal，而不是递降边。
质量保持的逐坐标倒数仿射式也有严格障碍：对偶数或三整除源的标准解，它的全部整值输出
退化为规范分母 \(h_i=a_i/(n,a_i)\) 是否乘 \(p\) 的二值选择，并且无一满足目标等式。
见[未标记全域提升的循环性与逐坐标倒数仿射整值障碍](../claims/full-solution-lift-circularity-reciprocal-affine-no-go.md)。

### E5. strict_decrease

回执必须保存 \(\Pi(S)\)、\(\Pi(T)\) 及可复核的比较证明

\[
\boxed{\Pi(T)<\Pi(S)}.
\]

顺序必须预先定义在良基集合上，并能用于所有递归产生的新状态。对冻结有限图事后赋予
拓扑编号不满足这一条件。

只有 E1--E5 全部通过后，状态才可标记为 verified_edge。若 E1--E3 通过而 E4 或
E5 缺失，应保留为 candidate_transition，不得用于归纳闭包。

## 6. 候选良基势函数字段

第一版可试验下列词典序自然数元组：

\[
\boxed{
\Pi_0(S)=
\bigl(
\rho(S),
\Delta_{\mathrm{den}}(S),
R_S,
K_S,
|\mathcal Q_S|
\bigr)
\in\mathbb N^5.
}
\tag{4}
\]

这里 \(\Delta_{\mathrm{den}}\) 由完整目标纤维按式 (3) 计算，不用某个首见证替代。对没有
目标纤维的新增状态，必须先给出与 (3) 可比较的规范缺陷定义，不能随意填零。

式 (4) 只是一个**候选字段方案**，没有证明现有或未来的 support switch、q-adic lift、
合法 \(R\)-修复会沿它下降。特别地：

1. 若 \(\rho(T)<\rho(S)\)，后续分量可以增大，但仍须验证实际秩和解提升；
2. 若 \(\rho\) 不变，则必须逐边验证第一个发生变化的分量严格减小；
3. 较小 \(R\) 不能补救此前 \(\Delta_{\mathrm{den}}\) 增大；
4. \(R\) 或 \(K\) 增大的合法修复只有在更早分量已严格下降时才可能被接受；
5. 若任何合法边系统性违反此顺序，应更换**全局预先定义**的势函数，而不是逐边重排
   分量。

### 6.1 已验证的 PRE--ABSORB 分型调度

对“固定 \(s\) 因子重选 + 降 \(R\) absorption + formal 剪枝”这一具名边菜单，
普通的统一字段次序已经不可能成立：前向因子边增大 \(R\)，其代数逆边又会与之形成
精确二环；完整 \(m=1\) 图还含 terminal-free 自环。该菜单必须增广不可逆阶段

\[
\mathrm{PRE}\longrightarrow\mathrm{ABSORB}
\]

并在 ABSORB 提交时固定

\[
\varepsilon\in\{\min,\max\}.
\]

相应的已验证 E5 调度为

\[
\boxed{
\Pi_{\mathrm{phase}}(S)=
\begin{cases}
(1,a,0,0),&S\in\mathrm{PRE},\\
(0,R,m,r_\varepsilon),&S\in\mathrm{ABSORB},
\end{cases}}
\tag{5}
\]

其中 PRE 只允许严格降低 \(a\) 的固定 \(s\) 边；ABSORB 只允许严格降低 \(R\) 的
rechart，以及固定 \(R\) 时降低 \(m\) 或所选 \(r_\varepsilon\) 的 formal 剪枝。
禁止无成本返回 PRE。若另有真正 equation rank \(\rho\)，应把它置于最外层并只在
\(\rho\) 严格下降时允许重置全部阶段字段。

式 (5) 只供应 E5。它不能把缺少合法后继或解提升的 formal cursor 边升级为
verified_edge；每条实际递归边仍须单独通过 E1--E4。完整证明、二环和自环边界见
[重图表与形式吸收的两阶段良基调度](../claims/type-I-phase-labeled-candidate-selector-well-founded-schedule.md)。

`overflow_carrier_reset_v1` 应放在 PRE/ABSORB 之外的不可逆 `RESET` phase。其局部秩
可以取载体大小 \(M\)，因为每条 reset 候选满足 \(M_T<M_S\)；但 RESET 不能无条件
复用 ABSORB 的增支撑边。若允许 reset 后再次进入会增大 \(M\) 的 marked phase，必须
再增加一个更外层 rank 或证明一个封闭的 phase 组合势；否则只能保留为
`candidate_transition`，不能承担统一递归。

这一限制有精确回执：在 \(p=73\) 上，\(M=38\) 的 reset 载体 \(t=12\) 经
\(Q=11\) 的 anchor/lcm 重入到 \(M=132\)；随后 \(M=132\) 经 \(t=30\) 重入到
\(M=330\)，而 \(M=330\) 又回到 \(M=132\)。因此任何允许普通 ABSORB 回边的 RESET
合同都不能把 \(M\) 作为全局秩。该路径已登记为
`reset_reentry_carrier_cycle`，RESET 要么封闭在终端/严格外层降秩内，要么必须引入
不可重置的额外状态分量。

### 6.2 已验证的 absorbed-support 势

对固定核心素数 \(p_0\) 的 linear_absorbed_support_v1 子程序，定义

\[
B_{p_0}=\frac{(p_0-1)^2}{4},
\qquad
\Pi_A(S)=\left\lfloor\frac{B_{p_0}}{A_S}\right\rfloor.
\tag{6}
\]

若一条 v1 clean external 边吸收 \(Q=q^e>1\)，并且规范后继仍满足
\(R_T<p_0\)，则

\[
A_T=A_SQ\ge2A_S,
\qquad
A_T\mid K_T\le B_{p_0}.
\]

所以 \(\Pi_A(T)<\Pi_A(S)\)。对 complete-excess bundle 则令

\[
A_T=\operatorname{lcm}(A_S,Q).
\]

每个 \(q\mid Q\) 的新完整块指数都严格超过 \(v_q(K_S)\ge v_q(A_S)\)，故仍有
\(A_T/A_S\ge2\)。当 source \(A_S\le B_{p_0}\) 时，同一个第一坐标证明对
\(R_T>p_0\) 的 overflow target 也原样成立，不要求 \(A_T\le B_{p_0}\)。该势允许
\(R_T>R_S\)。v1 中已吸收素数
不能重新以 \(q\nmid K\) 身份收费；bundle v2 允许同一素数以后以严格更高的完整块
重现，但只有 lcm 账本确实增长时才能收费。若另一边丢弃或重置 \(A_S\)，必须把一个
严格下降的外层秩放在 (6) 之前。若 source 已有 \(A_S>B_{p_0}\)，则不能仅凭内部
overflow receipt 入队；必须用真实 parent--target 的第二坐标 \(K/A\) 比较支付 E5。

对已验证 overflow receipt，固定 \(n\) 图谱中的 \(L\in\mathcal W_{A_S}\) 也满足
\(A_S\mid L\)、\(L>A_S\)，故同一个势证明适用。特别地，\(A_S=1\) 时规范
determinant carrier \(d\ge2\) 总给出这种边。一般 \(A_S>1\) 的
\(\mathcal W_{A_S}\) 可以为空；此时不得把任一较小对偶载体直接写入 \(A_T\)。

可替代方案可以加入规范 Fourier 导子、marked 复杂度或 q-adic 提升深度，但每个分量
都必须是非负整数、从状态本身可重算，并且必须重新证明全体允许边严格下降。

### 6.2a RESET 的 joined-support 外层秩

对 overflow determinant 回执

\[
pn=4Md+1,
\qquad A\mid M,
\]

以及对称双载体 \(t\in\{d,M\bmod p\}\)，允许一个单独命名的
`overflow_outer_rank_reset_v1`。它不得把小载体 \(t\) 直接写成新支撑，而必须先取

\[
A'=\operatorname{lcm}(A,t).
\]

该分支先要求 \(1\le A\le B_p=(p-1)^2/4\)。若 \(A'>A\)、\(A'\mid K_t\)，并且

\[
\left\lfloor\frac{(p-1)^2}{4A'}\right\rfloor
<
\left\lfloor\frac{(p-1)^2}{4A}\right\rfloor,
\tag{7}
\]

则目标状态带 \(A'\) 而不是 \(t\)。目标 \(R_t<p\) 时属于已有
`marked_absorb`；目标 \(R_t>p\) 时仍是 overflow，但可作为新的合法 overflow 状态
继续进入选择器。两种情形都用图表无关的 \(\operatorname{Sol}(p)\) 恒等映射完成 E4，
并用 (7) 完成 E5。目标仍为 overflow 并不取消秩下降，也不能被误报成直接终端。
若源 \(A>B_p\)，当前 \(\Pi_A=0\)，本分支不接受该 RESET，必须改用另一个外层秩。

该边的 E2 还必须明确重算 \(A'\mid K_t\)。若 \(A'=A\) 或整除失败，不能用
`carrier-size` 的局部下降掩盖旧支撑退出；该通道只能是 `analysis_evidence`。这是一条
比普通 `overflow_carrier_reset_v1` 更强的类型边界，因为它把“支撑只增不减”作为
不可重置外层秩的一部分。当前聚焦回执见
[overflow RESET 的 joined-support 外层秩递降](../claims/type-I-overflow-outer-rank-reset.md)。

### 6.3 同 \(1\pmod4\) 秩的 D-only 拒绝门

若候选把核心素数 \(p\equiv1\pmod4\) 送到

\[
2\le n<p,
\qquad
n\equiv1\pmod4,
\]

并保持同一双尾，只替换 distinguished coordinate，则不得仅凭 \(n<p\) 登记递降。
完整 \(D\)-only 支撑二分现在给出：

1. \(D\mid n^2\) 时只复述中心 Type I 尾谱；中心 miss 后输出 `rejected_branch`；
2. \(D\nmid n^2\) 时，三个规范目标由同余类 Vieta no-go 全部排空，同样输出
   `rejected_branch`。

因此该门没有 E2 后继、E4 lift 或 E5 边。它尤其适用于 absorbed-support overflow 的
严格补秩 \(u\equiv1\pmod4\)。这只是删除一类无效边，不代表 overflow 已有其它出口。
证明见
[同 1 mod 4 秩的 non-source D-only 标记纤维全域空定理](../claims/two-denominator-lift-same-one-mod-four-no-go.md)。

### 6.4 \(p-1\) 因子 Type II 的固定源秩门

对

\[
p=4qr+1,
\qquad m=4q-1,
\qquad x=q(r+1),
\]

兼容的 Type II 双尾合同把目标降至源秩 \(n=r+1\)。固定 \(r\) 时不得继续把 \(q\)
视为无界搜索参数；全部证书精确对应于

\[
\left\lceil\frac{r+2}{4}\right\rceil
\le k\le K_r:=\left\lfloor\frac{2r+1}{3}\right\rfloor,
\quad
d\mid k^2,
\quad
q=\frac{d+k}{4k-r-1},
\quad
d<q(r+1),
\]

并另过素数门。命中项应先登记为直接 Type II terminal；同一公式同时提供源解与全域
双尾提升。菜单为空则可输出该固定 \(r\) 的 `FIXED_SOURCE_RANK_NO_GO`，但不能排除其它
\(r\)。令

\[
k_0=\left\lceil\frac{r+2}{4}\right\rceil,
\qquad
a_0=4k_0-r-1.
\]

候选上包络必须保存线性分母，得到

\[
q\le Q_r^{\rm end}:=
\left\lfloor\frac{k_0(k_0+1)}{a_0}\right\rfloor
\le\frac{(r+2)(r+6)}{16},
\qquad
p-1\le\frac{r(r+2)(r+6)}4.
\]

所以任何把 \(r\) 限制在固定上界的选择器都不可能全称覆盖。规范预处理不再只识别
单大素数，而是构造

\[
\mathcal C_U=\{q\mid U:q\le Q_{U/q}^{\rm end}\}.
\]

端点函数沿整除关系单调，故 \(\mathcal C_U\) 是因子下闭容量域；其补集由最小禁止反链
\(\mathcal B_U\) 唯一生成。选择器先输出 `P_MINUS_ONE_ENDPOINT_DOWNSET` 与
`MINIMAL_FORBIDDEN_CHUNKS`。若 \(L\in\mathcal B_U\)，任何实际命中都不能满足
\(L\mid q\)；\(L=\ell^h\) 给出 \(\ell\)-进层分配，复合 \(L\) 则保留联合容量语义，
不得拆成未经证明的单坐标排除。

随后只对 \(q\in\mathcal C_U\) 建立完整 signed divisor box；目标在生成子群外时
输出 G 角色证书，在生成子群内但有界盒 miss 时输出 F 对数/Fourier 证书。

若 signed box 命中，则不再保留独立的 \(d<x\) 范围候选门。指数取反
\(z\mapsto-z\) 保持目标 \(-1\)，相应真实除子满足

\[
d(z)d(-z)=x^2.
\]

目标纤维没有固定点，故每个反足对恰有一个 \(d<x\) 成员；任一命中直接登记为
Type II terminal。该结论对每个循环 Jacobi parity 子盒分别成立，也不依赖源群循环。
完整证明见
[Type II 对称除子纤维的反足物理容量与逐奇核模式终端](../claims/type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal.md)。

所有压缩后纤维为空时只能输出 `P_MINUS_ONE_TYPE_II_EMPTY`，它不是终端，也不是递降，
必须转交其它 terminal 或 verified edge。\(p=67369\) 给出精确控制：
\(U=42\cdot401\) 把候选压到 \(q\mid42\)，形成五张 G 与三张 F 空证书，随后由
gap-\(31\) Type I terminal 接管。这个反例证明“自适应 \(r\) 总命中”不能成为合同
默认项。基础有限菜单见
[固定源秩有限菜单与三次容量界](../claims/type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity.md)，
端点分配与完整控制见
[端点容量包络、大素因子分配与 \(p=67369\) 分派](../claims/type-II-p-minus-one-endpoint-envelope-large-prime-allocation.md)，
因子格预处理见
[\(p-1\) 因子 Type II 的下闭容量域与素数幂分配](../claims/type-II-p-minus-one-divisor-downset-prime-power-allocation.md)。

### 6.5 Type II 盒外自然尾关系图

对任意合法 Type II 缺口 \(m\)、\(x=(p+m)/4\)，盒外整数目标表示可写成

\[
A+B=m\kappa,
\qquad (A,B)=1.
\]

该关系自动满足 \((AB,m\kappa)=1\)。自然两尾

\[
\frac{px\kappa}{A},
\qquad
\frac{px\kappa}{B}
\]

同时为整数当且仅当 \(AB\mid px\)；这是直接 Type I/II terminal。否则可对每个满足
\(v_\ell(AB)>v_\ell(px)\) 的素数构造规范关系迁移，并在 \(\kappa>1\) 时严格降低
\(\kappa\)。该对象的规范载荷为：

```text
certificate_type = type_ii_natural_tail_relation_graph
prime = p
gap = m
first_denominator = x
relation_pair = [A, B]
relation_quotient = kappa
natural_tail_capacity = p*x
split_deficit = [A/gcd(A,p*x), B/gcd(B,p*x)]
total_deficit = A*B/gcd(A*B,p*x)
transition = [ell, t, normalization_g, A_next, B_next, kappa_next]
selector_status = analysis_evidence
recursive_edge_eligible = false
```

该关系图内部的 terminal-first 顺序必须固定为：

\[
\text{natural-tail }AB\mid px
\longrightarrow
\text{fresh quotient divisors }h\mid\kappa
\longrightarrow
\text{over-capacity edge labels }\ell
\longrightarrow
\text{relation transition}
\longrightarrow
\kappa=1\text{ SCC}.
\]

每个 \(h\) 或 \(\ell\) 只有在合法自然范围内通过统一短证书 verifier 后才能终止。
\(p=1153,q=16,m=63,x=304\) 给出底层标签完备性的严格反例：
\(\{1,62\}\leftrightarrow\{2,61\}\) 的内部标签为 \(31,61\)，唯一合法标签 \(31\)
没有证书；但两个物理最小源关系在进入周期前分别由 quotient gap \(23\) Type II
和 quotient divisor \(3\) Type I 抢占。因此不得省略 fresh-quotient 层，也不得声称
每个 SCC 自含终端。

这里的 \(\kappa\) 降层只是有限 `certificate_context` 搜索秩，不是 E5：迁移会引入
新素因子，后继没有完整合法状态字段，也没有 \(W_T\to W_S\) 的全域解提升。若完整图
未出现自然尾终端或通过 verifier 的 alternate-gap 终端，必须输出
`KAPPA_ONE_RELATION_SCC`；不得把底层周期压成伪递降。精确定理见
[Type II 奇核盒外关系的 \(px\) 自然尾容量与 \(\kappa=1\) 周期归约](../claims/type-II-odd-kernel-overflow-natural-tail-relation-graph.md)。

### 6.6 Type II 真因子端点递降

对 \(p=4U+1\) 的端点允许状态 \(q\mid U\)，关系图完成自然尾、fresh quotient 和
边标签终端检查后，允许从任一 source-reachable 底层节点 \(\{a,4q-1-a\}\) 创建
下列候选，但必须满足

\[
a\mid q,\qquad a<q.
\]

规范载荷为：

```text
certificate_type = type_ii_relation_reach_proper_endpoint_descent
source_cofactor = q
source_bottom_node = [a, 4*q-1-a]
target_cofactor = a
target_gap = 4*a-1
target_first_denominator = U+a
solution_set = Sol(p)
solution_lift = identity
rank_before = q
rank_after = a
phase = p_minus_one_endpoint_descent
```

目标端点必须从原始整数重算 factorization、signed box、源子群和 G/F/hit 分类。hit
先登记 Type II terminal；G/F 空态才登记后继。E1 由完整 source path 与底层节点支付，
E2--E3 由端点公式和因子下闭域支付，E4 是 \(\operatorname{Sol}(p)\) 恒等映射，E5
是预先定义的自然数势 \(a<q\)。该 phase 不允许无付款地重置到更大的 \(q\)。

不得把整个抽象 bottom graph 的不可达节点用于该边；\(p=6529,q=48\) 的完整底层图
含不可达的非因子 sink \(\{5,186\}\)，而真实源 Reach 只进入 \(\{1,190\}\) sink。
也不得只检查 sink minimum；\(p=9601,q=40\) 的 transient 底层节点
\(\{5,154\}\) 已产生 gap \(19\) Type II。若完整可达底层没有任何 \(a\mid q,a<q\)，
该精确坐标分支输出 `KAPPA_ONE_RELATION_REACH_NO_PROPER_ENDPOINT`，随后必须进入
第 6.7 节的 gcd-shadow fallback，而不是把整坐标失败误报为全称失败。精确定理见
[Type II 关系图可达底层的真因子端点递降](../claims/type-II-relation-reach-proper-endpoint-descent.md)。

### 6.7 Type II \(q\)-owned gcd-shadow 全称递降

对任一 source-reachable 底层节点

\[
\{a,b\},
\qquad
a+b=4q-1,
\qquad
q>1,
\]

定义

\[
\mathcal D_q(a,b)=\{(a,q),(b,q)\}\setminus\{q\}.
\]

该集合必非空，否则 \(q\mid a,b\) 会推出 \(q\mid4q-1\)。选择器可以先枚举所有
可达节点的 shadow 并优先检查终端；若无终端，则规范取最小
\(q'\in\mathcal D_q\)。
回执为：

```text
certificate_type = type_ii_relation_reach_gcd_shadow_endpoint_descent
source_cofactor = q
source_bottom_node = [a, b]
shadow_formula = gcd(a, q) or gcd(b, q)
target_cofactor = q_prime
target_gap = 4*q_prime-1
target_first_denominator = U+q_prime
solution_set = Sol(p)
solution_lift = identity
rank_before = q
rank_after = q_prime
phase = p_minus_one_endpoint_descent
```

E1 必须保存实际 bottom path、被选坐标和 gcd 等式；E2--E3 从原始整数重建目标
端点和 G/F/hit 分类；E4 对普通状态取 \(\operatorname{Sol}(p)\) 恒等映射；E5 由
\(q'\mid q\)、\(q'<q\) 支付。若重算命中，普通状态直接输出 terminal；若重算为 G/F
空态，输出 `verified_edge`。

当 \(q=1\) 时 \(m=3\)。若目标 \(-1\) 在源像内，则至少一个源生成元模 \(3\) 为
\(-1\)，其单位指数已在 signed box 内，所以 F-empty 基例不存在。F 状态的 shadow
因子链因此必终止；G 状态退出本 phase 并转交 Type I selector，不允许重新进入更大
\(q\)。完整证明见
[Type II 关系 Reach 的 \(q\)-owned gcd shadow 全称端点递降](../claims/type-II-relation-reach-gcd-shadow-endpoint-descent.md)。

这里的 G 出口不得自动改写成 \(R=3\) Type I 成功。令
\(X=(p+3)/4\)、\(N=(3p+1)/4\)。前者的全部素因子为 \(1\pmod3\) 恰等价于
\(q=1\) Type II 为 G 及 gap 3 失败；后者的全部素因子为 \(1\pmod3\) 恰等价于
\(R=3\) Type I 为 G 及既有 \((3p+1)/4\) 标记源为空。\(p=241\) 已使两者同时
发生；\(p=2521\) 更同时逃过 gaps \(3,7,11,15,19\)。所以 `q_one_G_to_R_three`
只能是重新分类，不能登记 terminal、真分母递降或新的 E4。精确反例见
[模三双 G 出口的精确等价与小缺口严格反例](../claims/type-I-type-II-mod-three-double-g-exit-obstruction.md)。

在把这个未闭合交接交给 Type I/Fourier 机制之前，仍须执行根素数的直接
`terminal-first` 筛。特别地，若 \(p=24h+1\) 的 \(h\) 为奇数且
\(p\) 是模 \(23\) 二次非剩余，则 gap \(23\) 的显式 Type II 表给出一张
`terminal_leaf`；它在 \(p=2521\) 上取 \(d=8\)。该分支的回执仅保存
\((m,d)\) 和重建的三分母，结论为 `terminal_leaf`，所以不要求 E1--E5，也不把
其附带的 \(n=h+1\) 标记两尾 lift 计作 G/Type I 的递归边。未命中时才保留原有的
G/Type I handoff。见[奇 \(h\) 的 gap-23 二次非剩余 Type II 终端与两尾递降]
(../claims/type-II-gap-23-odd-h-qnr-terminal-descent.md)。

对非平凡 `marked_solution_set`，非终端边只有在目标状态逐字保留同一个 mark 谓词时
才可使用恒等 lift；普通短证书还必须另验 mark membership，不能自动登记 marked
terminal。

该边降低的是 endpoint phase 的 \(q\)，不是 equation target 的分母 \(p\)。只有
phase 不可重入及 \(q=1\) F-empty 基例同时写入全局势时，才允许把它标为 E5；任何
无付款的较大 \(q\) reset 都会使该资格失效。

### 6.8 \(q=1\) G 到 full-carrier Type I tree 的 phase-root 重索引

ordinary \(q=1\) G endpoint 不必回退到失败的 \(R=3\) companion chart。定义

\[
X=\frac{p+3}{4},
\qquad
R_X=\frac{8X+1}{3},
\qquad
K_X=X(R_X-2).
\tag{40}
\]

该选择由根素数 \(p\) 的闭式规则预先确定；它不是从当前 raw node、charged support 或
事后命中的 Type I chart 倒推。它是唯一低图表 \(3\le R\le p-2\) 中满足 \(X\mid K\)
的 chart，且有独立的 universal raw source

\[
\bigl(p,R_X(p-1)-p,p-1\bigr)\longmapsto(1,R_X-1,1).
\tag{41}
\]

因此只对下列 ordinary source state 允许具名 root-entry：

```text
q_one_full_carrier_phase_root_entry_v1
source phase         = type_ii_q_one_g_endpoint
source q             = 1
source marked set    = Sol(p)
target scope         = fresh_source_tree_only
target normal form   = type_i_full_carrier_low_root_v1
target chart          = (p, R_X, K_X)
target support        = 1
```

它是同方程、同解集的有向 phase reindexing，而不是把 Type II raw word 延续为 Type I
raw word。回执必须保存 q=1 G separator、(40)--(41)、actual p-edge 和 source/target
state digest。E4 为

\[
\Phi:\operatorname{Sol}(p)\longrightarrow\operatorname{Sol}(p),
\qquad\Phi(u)=u.
\tag{42}
\]

该映射不读取任何未知解，也不适用于非平凡 marked state。

它的 E5 只在如下不可回返 global phase prefix 中成立：

\[
\operatorname{rank}(\text{Type II q=1 G})=2,
\quad
\operatorname{rank}(\text{full-carrier Type I tree})=1,
\quad
\operatorname{rank}(n<p)=0,
\tag{43}
\]

非终端动作仅可为 \(2\to1\)、\(1\to1\) 或 \(1\to0\)；full-carrier tree 之后的
Type II 证书只能是 terminal leaf，禁止 \(1\to2\) 重入。于是 root-entry 的势首坐标
严格下降。该规则不替代 phase-1 的 total selector；任何未通过其自身 E1--E5 的 Type I
候选仍不得递归。root 后的第一个 complete-excess step 已由 carrier rail 的 parity
dispatch 提供严格 local support payment。完整 receipt 与边界见
[q=1 G full-carrier phase-root 准入](../claims/type-II-q-one-full-carrier-phase-root-entry.md)。

### 6.8b \(q=1\) G 到 c=3 source-lineage tree 的条件性 relay

另一条不与 full-carrier tree 混同的 phase root 只在 c=3 chart 已由根素数闭式预先确定，且
存在一份从其 declared universal \(p\)-source 出发的实际 source-lineage raw receipt 时允许：

\[
R=104h-9,
\qquad M=26h+1,
\qquad x=p-3,
\qquad K=Mx.
\tag{44}
\]

receipt 必须逐边保存 \(q_i\)、gcd reduction \(g_i\) 与 source 首坐标的后代 \(z_i\)，并在
尾部的 \(t=4,2,1\) physical rows 验证

\[
\sigma=-p^{-1},
\qquad
\Theta_i=\sigma\prod_{j\le i}q_jg_j,
\qquad
\Theta_t=-\epsilon(4M/t)\pmod R,
\tag{45}
\]

其中 \(z_t=\epsilon tx\)、\(\epsilon\in\{+1,-1\}\)。唯一允许的 metadata 坐标交换是
canonical \(p\)-edge 后 anchor 的一次换向；非 \(p\)-first source-bypass 仍必须从同一个
declared source 起步。任何 formal p-parent 或 charged-history path 都不能替代这个 E1。

若 source state 是 ordinary `q=1 G` endpoint，且两端都标记为 \(\operatorname{Sol}(p)\)，则
可登记

```text
q=1 G endpoint (phase 2)
  -> fresh c=3 source-lineage tree (phase 1, A=1)
  -> R=11 d=3 RESET (phase 1, A=3)
```

第一条边的 E4 是 \(\operatorname{Sol}(p)\) 恒等映射，E5 是 phase \(2\to1\)；第二条的 E4
仍是恒等映射，E5 由 \(A:1\to3\) 支付。非终端策略允许 \(2\to1,1\to1,1\to0\)，禁止
c=3 tree 返回 Type II；tree 后的 Type II 结果只能是 terminal leaf。c=3 和 \(R=11\) 的
typed fiber 必须分别重算。这个 conditional relay 不证明 source-lineage receipt 对所有
endpoint 存在，也不替代 phase-1 的独立全称 selector。详见
[q=1 G c=3 source-lineage phase relay](../claims/type-II-q-one-c3-source-lineage-phase-root-entry.md)。

## 7. 明确不构成递降的对象

下列结果可以是重要的分析证据，但单独出现时不得标记为 verified_edge：

| 对象 | 缺失的证明义务 |
|---|---|
| \(|Q/T|<|Q|\) 或稳定子商变小 | 没有合法新算术状态、解提升和全局势函数 |
| \(t\mid R\) 且 \(t<R\) | \(t\) 可能不属于合法模类，也不是源分母 |
| 冻结有限图无环 | 未定义的新状态处没有出边；有限无环不推出统一良基性 |
| 满足一个或多个 q-adic/CRT 提升同余 | 只是清分母的必要条件，不证明替代整数存在或产生解 |
| 支撑素数退出或支撑维数下降 | 素数可能在后续状态重入；没有解提升 |
| 某个 Fourier 角色、格向量或加法组合证书 | 还未映到终端证书或合法边 |
| 单个规范见证的溢出下降 | 可能不是完整目标纤维的选择不变量 |
| \((e-h_{\mathrm{current}})_+\) 变小 | 重复使用了当前 \(K\) 已吸收的 q 进层 |
| 有限扫描中每个样本都有出口 | 不给出全称构造，也不证明递归闭合 |
| 把同一 Type I 证书改写成 marked source | 没有产生独立的第三出口或新的下降机制 |
| Type II 盒外关系的 \(\kappa\) 严格降层 | 只是 `certificate_context` 内部搜索；底层有周期，且未构造合法后继状态或 E4 lift |
| 同 \(1\pmod4\) 的较小 D-only rank | source-supported 只重复中心 Type I，non-source 标记纤维全空 |
| overflow 的某个对偶图表 | 只有 \(A'=\operatorname{lcm}(A,t)>A\)、\(A'\mid K_t\) 且 (7) 成立时才是 joined-support verified edge；否则仍是 candidate/analysis evidence |
| overflow 固定-n 的有界除子 \(L\mid Md\) | 只有 \(A<L\le B_p\)、\(4L>n\) 且严格外层势下降时才是 overflow_fixed_n_bounded_divisor_outer_rank_v1；\(A\nmid L\) 时必须显式支付 support reset，候选集为空不能伪造后继 |
| d=1 overflow 的 \(p-2\) G 重图表 | \(M\bmod p=(p-1)/4\) 只给出普适 G 分离和空支撑纤维；它丢弃旧支撑，不能作为 RESET 或恒等 marked lift |
| overflow 余数 \(r=1\) 的对称边界 | \(s=1\)、\(d=(p-1)/4\)，两侧固定为 \((p-2,(p-1)^2/4)\) 与 \((3,(3p+1)/4)\)；不自动支付旧 support，不能作为新的递归出口 |
| \(q=1\) Type II G 改挂到 \(R=3\) Type I | 两个模三源群可以同时为 G；\(p=2521\) 还逃过 gaps \(3,7,11,15,19\)，所以伴随换图表不是终端或真分母递降 |
| 由一个已知目标解定义的 \(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 常值映射 | 映射存在性与目标可解性等价；应直接登记目标 terminal，不能重复收费为 E4 递降 |
| 反复令 \(M\leftarrow\operatorname{lcm}(A,d)\) | determinant/lcm 更新存在精确二环，未给出全局良基量 |

## 8. 验收表

每个新选择器分支在合并到主证明图前，应填写以下表格。N/A 只允许用于没有后继状态
的直接终端叶，并必须说明原因。

| 验收项 | Type I hit | Type II hit | support switch | q-adic lift | generalized \(2^j\) terminal |
|---|:---:|:---:|:---:|:---:|:---:|
| 根或标记目标已规范化 | 必须 | 必须 | 必须 | 必须 | 必须 |
| 合法 \(R,K,\mathcal Q\) 已重算 | 必须 | 必须 | 必须 | 必须 | 必须 |
| 使用 \(D^-,D^+\)，未用 \(e-h_{\rm current}\) | 若涉及纤维 | 若涉及纤维 | 必须 | 必须 | 若涉及纤维 |
| 直接短界 \(m\le H(p)\) | 必须 | 必须 | N/A | 若终端则必须 | 若导出 I/II 则必须 |
| 输出专属正规形 verifier | 必须 | 必须 | 必须 | 必须 | 必须 |
| 构造完整合法后继状态 | N/A | N/A | 必须 | 若为边则必须 | 若为边则必须 |
| 解恢复或 \(W_T\to W_S\) 全域提升 | 直接恢复 | 直接恢复 | 必须 | 必须 | 必须 |
| \(\Pi(T)<\Pi(S)\) 的逐边证明 | N/A | N/A | 必须 | 若为边则必须 | 若为边则必须 |
| 可重复用于新状态而非仅冻结样本 | 必须 | 必须 | 必须 | 必须 | 必须 |
| 结论状态 | terminal_leaf | terminal_leaf | verified_edge | verified_edge 或终端叶 | verified_edge 或终端叶 |

建议每条回执另附一个简短结论枚举：

~~~text
analysis_evidence
necessary_condition_passed
candidate_transition
verified_edge
terminal_leaf
rejected
~~~

只有 verified_edge 与 terminal_leaf 可以进入带标记解的严格递降闭包。

## 9. 与统一选择器目标的衔接

complete-excess 定理已经把每个完整 Reach 压成直接 Type I、bundle marked edge 或
bundle overflow，并消除了 `COMPETING_EXCESS` 作为独立 sink-SCC 余项。通用
\(p\)-source 又覆盖所有 F/G/hit 图表；初始 \(A=1\) overflow 也总能通过 determinant
的固定-\(n\) 小载体或[对偶 \(d/r\) RESET 引理](../claims/type-I-overflow-a-one-dual-outer-rank-reset.md)
得到一条 verified edge。因此“裸 G source”和
“初始 overflow 无出口”不再是主缺口。

在统一 typed charged-chart adapter 尚未实现前，当前集中的全称问题是：对每个递归历史
可达的 \(A>1\) overflow，是否必有

\[
\mathcal W_A\ne\varnothing
\quad\text{或存在满足有界除子条件的 }L\mid Md,
\quad\text{或在 }A\le B_p,\ Md>A\text{ 时通过完整乘积无界折叠},
\quad\text{或某个 source/path/node alternate 保持并增加 }A,
\quad\text{或直接 Type I/II 终端？}
\]

第三项的算术、E4 与 E5 已经完成；其缺口仅是 target typed normal-form 的统一
序列化准入。因而在该 adapter 被接入后，低 support 段会精确缩到
\(M=A,d=1\)，而不是所有有界除子空菜单。源端 \(A>B_p\) 时第一秩坐标已为零，完整乘积
不再自动付款，仍须使用高支撑 capacity gate 或新的严格第二坐标机制。

若这些出口都没有，就必须构造改变 marked state 的新边，并以一个严格下降的外层 phase
支付 support reset。任何 overflow 至少有一个 \(R<p\) 的算术对偶图表，但反例证明该
图表可能不保留 \(A\)；这正是“表示--对偶”已经完成而“容量或递降”仍未闭合的接口。
在该问题解决以前，商群压缩、目标纤维距离、q-adic 必要同余和冻结图无环都只能作为
候选输入，不能单独写成统一选择器定理。

对 overflow 的 \(d=1\) 子分支，已有更强的算术分类：其对偶规范图表固定为
\((p-2,(p-1)^2/4)\)，并且普适地属于 G 态。完整乘积折叠的 d=1 饱和 target 更满足
刚性 \(A=(pn-1)/4\mid B_p\Longleftrightarrow n=1\)；真正 overflow 的 \(n>1\)
因而没有任何 \(A\mid D\mid B_p\) 的 target support。故该 G 重图表不仅不是现成
support-preserving 边，也不能借由把旧 support 再扩大来修复；它若进入递归，必须是
另有全域 E5 支付的 RESET。若 \(p+4\) 没有 \(3\bmod4\) 因子，仍需回到上述非支撑
终端、RESET 或容量问题。详见[d=1 overflow 的 p-2 G 重图表正规形](../claims/type-I-overflow-d-one-p-minus-two-g-rechart.md)
及[完整乘积 d=1 饱和支到 p-2 G 锚点的支撑保留刚性](../claims/type-I-overflow-full-product-d-one-g-anchor-retention-rigidity.md)。

对称的 \(r=1\) 分支也已分类：它强制 \(s=1,d=(p-1)/4\)，d 侧仍是上述 G 图表，
r 侧是 \(R=3\) 的单位载体。它可以在 \(M=kp+1\) 中真实出现，但不能绕过
`lcm(A,t)>A`、支撑整除和外层势条件；详见[overflow 余数 r=1 的对偶边界](../claims/type-I-overflow-r-one-dual-boundary.md)。
