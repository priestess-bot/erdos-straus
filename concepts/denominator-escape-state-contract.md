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
- type-I-formal-target-pair-descent-cycle-boundary
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
last_checked: '2026-07-30'
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
| target_fiber | \(\phi_S(z)=\prod_{q\in\mathcal Q_S}q^{z_q}\bmod R_S\)、目标相位 \(\tau_S\)、关系格 \(\Lambda_S=\ker\phi_S\) 和纤维 \(F_S=\phi_S^{-1}(\tau_S)\) | 验证所有生成元为单位、格基完备且所用见证确在 \(F_S\) |
| signed_defect | 对一个**全局定向**见证 \(z\) 记录 \(D^-(z),D^+(z)\) | 必须按式 (1) 重算；不得逐坐标拼接 \(z\) 与 \(-z\) |
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

### 2.1 合法模数与分析商对象的分离

满足 \(t\mid R\) 的商模数、稳定子商 \(Q/T\) 或某个投影群，可以作为
certificate_context 中的分析对象，但它们默认不是新的算术状态。要把商模数 \(t\)
登记为后继，必须重新构造完整的 equation_target、modulus_context、K_context、
marked_solution_set 和 normal_form。例如 \(t\equiv1\pmod4\) 的商表示不能在没有
额外桥接时冒充要求 \(R\equiv3\pmod4\) 的 Type I 状态。

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

可替代方案可以加入规范 Fourier 导子、marked 复杂度或 q-adic 提升深度，但每个分量
都必须是非负整数、从状态本身可重算，并且必须重新证明全体允许边严格下降。

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

本合同把当前主缺口压缩成两个可以明确证伪或推进的问题：

1. 能否把规范 Fourier、关系格或加法组合 F 证书产生的某个非零
   \(D^-/D^+\) 合同，统一构造成 q_adic_lift、support_switch 或
   generalized_dyadic_terminal 回执？
2. 能否对所有没有 Type I/II 短证书的核心素数证明至少一个回执通过，并让所有
   verified_edge 共享同一个良基势函数？

第一个问题负责“表示--对偶”到真实算术对象的接口；第二个问题负责“容量或递降”闭合。
在二者同时完成以前，商群压缩、目标纤维距离、q-adic 必要同余和冻结图无环都只能作为
构造候选边的输入，不能被单独写成统一选择器定理。
