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
visibility: public
last_checked: '2026-08-01'
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

该子类型的 state_id 由版本号、\(p_0,R_S,A_S\) 生成；\(K_S\)、完整因子分解、
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
absorbed-support 势严格下降。初始 \(A=1\) 的 overflow 另用特化 verifier
`verify_overflow_determinant_charged_support_v1`：它证明 \(d\ge2\)，固定取 \(L=d\)，
因此该层候选集永不为空。

`overflow_determinant` 不是旧节点的 complete-excess bundle，不能把 \(d\) 伪写成
path-anchored \(Q\)。反过来，在 \(A>1\) 时也不得把支撑重置为较小对偶载体；只有
\(A\mid L\)、\(L>A\) 的边可留在当前 phase。完整证明与反例见
[overflow 固定 \(n\) 对偶图谱](../claims/type-I-overflow-determinant-fixed-n-dual-support-conflict.md)。

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
\(A_T/A_S\ge2\)，同一个势证明原样成立。该势允许 \(R_T>R_S\)。v1 中已吸收素数
不能重新以 \(q\nmid K\) 身份收费；bundle v2 允许同一素数以后以严格更高的完整块
重现，但只有 lcm 账本确实增长时才能收费。若另一边丢弃或重置 \(A_S\)，必须把一个
严格下降的外层秩放在 (6) 之前。规范图表超过 \(p_0\) 时只输出 overflow receipt，
不伪造后继。

对已验证 overflow receipt，固定 \(n\) 图谱中的 \(L\in\mathcal W_{A_S}\) 也满足
\(A_S\mid L\)、\(L>A_S\)，故同一个势证明适用。特别地，\(A_S=1\) 时规范
determinant carrier \(d\ge2\) 总给出这种边。一般 \(A_S>1\) 的
\(\mathcal W_{A_S}\) 可以为空；此时不得把任一较小对偶载体直接写入 \(A_T\)。

可替代方案可以加入规范 Fourier 导子、marked 复杂度或 q-adic 提升深度，但每个分量
都必须是非负整数、从状态本身可重算，并且必须重新证明全体允许边严格下降。

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
| 同 \(1\pmod4\) 的较小 D-only rank | source-supported 只重复中心 Type I，non-source 标记纤维全空 |
| overflow 的某个 \(R_t<p\) 对偶图表 | 若 \(\operatorname{lcm}(A,t)\nmid K_t\)，它丢失旧 charged support，只是 candidate_transition |
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
收费得到一条 verified edge。因此“裸 G source”和“初始 overflow 无出口”不再是主缺口。

当前唯一集中的全称问题是：对每个递归历史可达的 \(A>1\) overflow，是否必有

\[
\mathcal W_A\ne\varnothing,
\quad\text{或某个 source/path/node alternate 保持并增加 }A,
\quad\text{或直接 Type I/II 终端？}
\]

若三者都没有，就必须构造改变 marked state 的新边，并以一个严格下降的外层 phase
支付 support reset。任何 overflow 至少有一个 \(R<p\) 的算术对偶图表，但反例证明该
图表可能不保留 \(A\)；这正是“表示--对偶”已经完成而“容量或递降”仍未闭合的接口。
在该问题解决以前，商群压缩、目标纤维距离、q-adic 必要同余和冻结图无环都只能作为
候选输入，不能单独写成统一选择器定理。
