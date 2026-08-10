---
kind: claim
claim_id: type-I-fg-qprefix-kernel-depth-neutral-cargo-capacity
title: F/G q-prefix 的 labelled kernel-depth、中性载荷与物理合成边界
statement: >-
  设有限阿贝尔群 A 上的 labelled exponent box 为 E=prod_i[0,e_i]，其角色映射为
  phi(a)=sum_i a_i w_i，并令 K=E intersect ker(phi)。若 kappa_i 是 K 在第 i 坐标
  的最大值，则 K 被 principal prefix B_c 包含当且仅当 c_i>=kappa_i 对所有 i
  成立；相对当前深度 c 的唯一最小修复是 c join kappa，缺层向量为
  delta_i=(kappa_i-c_i)_+。全部 kernel records 所要求的 labelled owner layers 的
  并集恰为 I(kappa)。零权坐标满足 kappa_i=e_i，故在角色商中不可见的方向仍须作为
  neutral cargo 吃满深度。该 layer map 只有在另证 product/source synthesis 后才是
  充分物理容量；只有另证 labelled divisor downclosure 后，才可用 maximal kernel
  antichain 压缩记录检查；residue collision 还必须用 fiber section 单独处理。对
  p=557281 的 N=3^4*83^2 控制，ambient labelled kernel 的 kappa=(3,2)，唯一
  maximal kernel record 为 (3,2)。原 s0=19838 lineage 的 c0=(2,0)、delta0=(1,2)
  仍是严格局部边界；后续规范基替代已在空的单请求 ledger 上构造 standalone
  depth-3 q=3 lineage，可选择 c_fresh=(3,0)、delta_fresh=(0,2)，但旧 assignment
  已活跃时的 atomic migration 尚未证明。同纤维因子盒又证明 arithmetic factor-depth
  已是 (4,2)，所以 83 与 83^2 是精确算术 neutral cargo；未证的是它们的 F/G physical
  membership、owner token 与 state map。因而当前只剩两个条件性 typed-owner layers，
  不是算术缺层或两个 83-primary roles；在 exact physical-source predicate 证明真实
  来源必须覆盖这些 ambient records 之前，它们也不是物理来源的无条件必要容量，并且
  不给出 KERNEL_SECTION_SOURCE_COMPLETE、物理后继或 E4/E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-full-section-annihilator-boundary
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-raw-certified-q-layer-charge-key-nonreuse
  - type-II-same-fiber-factor-box-neutral-role-capacity
topics:
  - type-I
  - F-state
  - q-prefix
  - kernel-section
  - exponent-box
  - neutral-cargo
  - owner-layer
  - capacity-map
  - source-completeness
  - proof-boundary
sources:
  - claim: type-I-fg-qprefix-full-section-annihilator-boundary
    role: ambient-divisor-kernel-section-and-physical-source-boundary
  - claim: type-I-fg-qprefix-block-bound-first-overflow-terminal
    role: actual-F-depth-two-binding-and-valuation-data
  - claim: type-I-raw-certified-q-layer-charge-key-nonreuse
    role: typed-layer-owner-and-single-lineage-accounting-contract
  - claim: type-II-same-fiber-factor-box-neutral-role-capacity
    role: exact-arithmetic-factor-depth-neutral-fiber-and-primary-role-boundary
  - claim: type-I-fg-qprefix-depth3-replacement-lineage
    role: subsequent-depth-three-typed-lineage-update
  - reproduction: reproductions/type_i_fg_qprefix_kernel_depth_neutral_cargo_capacity.py
    role: focused-kernel-depth-downset-collision-and-p557-capacity-verification
visibility: public
last_checked: '2026-08-10'
---

# F/G q-prefix 的 labelled kernel-depth、中性载荷与物理合成边界

## 1. labelled exponent box

令 \(A\) 为有限阿贝尔群，以下用加法记号。固定权重

\[
w_1,\ldots,w_r\in A,
\qquad
E=\prod_{i=1}^r\{0,\ldots,e_i\},
\tag{1}
\]

并定义

\[
\phi(a)=\sum_{i=1}^r a_iw_i,
\qquad
K=\{a\in E:\phi(a)=0\}.
\tag{2}
\]

\(a\) 始终是 **labelled exponent record**。即使整数或剩余类映射

\[
\beta(a)=\prod_i q_i^{a_i}
\tag{3}
\]

发生碰撞，也不在 (1)--(2) 中合并记录。对深度向量 \(c\le e\)，记 principal
prefix

\[
B_c=\prod_i\{0,\ldots,c_i\}.
\tag{4}
\]

本卡先求覆盖 labelled kernel 的最小 \(B_c\)，再分别说明它与 residue section、
owner layers 和 physical source realization 之间还需要哪些合同。

## 2. kernel-depth 的精确最小完成定理

对每个坐标定义其它方向的有界和集

\[
S_{-i}=\sum_{j\ne i}\{0,w_j,\ldots,e_jw_j\}\subseteq A
\tag{5}
\]

以及

\[
\kappa_i
=\max\{t\in\{0,\ldots,e_i\}:-tw_i\in S_{-i}\}.
\tag{6}
\]

集合非空，因为 \(t=0\) 总可取。第 \(i\) 坐标在 \(K\) 上的投影精确为

\[
\pi_i(K)
=\{t\in\{0,\ldots,e_i\}:-tw_i\in S_{-i}\}.
\tag{7}
\]

这是因为 \(a_i=t\) 可出现在 kernel record 中，当且仅当其它坐标能抵消 \(tw_i\)。
因此

\[
\boxed{
K\subseteq B_c
\quad\Longleftrightarrow\quad
c_i\ge\kappa_i\quad(1\le i\le r).}
\tag{8}
\]

所以 \(\kappa=(\kappa_i)\) 是覆盖全部 labelled kernel records 的唯一最小
principal-prefix depth。这里“最小”是坐标偏序意义；一般并不保证 \(\kappa\in K\)。

相对当前 prefix \(c\)，定义

\[
\delta_i(c)=(\kappa_i-c_i)_+,
\qquad c^*=c\vee\kappa.
\tag{9}
\]

则 \(c^*\) 是唯一最小修复，且每个 \(\delta_i>0\) 都有显式障碍
\(a^{(i)}\in K\)，满足 \(a_i^{(i)}=\kappa_i>c_i\)。若第 \(i\) 个新增 labelled
layer 的价格固定为 \(\lambda_i>0\)，principal-prefix 模型中的最小加权修复价格为

\[
\boxed{\sum_i\lambda_i\delta_i(c).}
\tag{10}
\]

式 (10) 是 labelled depth price，不是 Hall/Rado 的独立物理槽数。

还有一个规范 Fourier 计数证书。对 \(c\le e\)，令
\(N(c)=|K\cap B_c|\)，则角色正交关系给出

\[
N(c)=\frac1{|A|}\sum_{\chi\in\widehat A}
\prod_i\left(\sum_{t=0}^{c_i}\chi(w_i)^t\right).
\tag{11}
\]

故 \(K\subseteq B_c\) 当且仅当 \(N(c)=N(e)\)，而 \(N(e)-N(c)\) 是遗漏的
labelled kernel records 精确数目。式 (11) 计算记录数，不自动计算 image fiber 数。

## 3. owner-layer ideal 与 product-synthesis 边界

令 labelled prime-power layers 为

\[
\mathcal L=\{(i,j):1\le i\le r,\ 1\le j\le e_i\},
\tag{12}
\]

记录 \(a\) 所需的 layer ideal 为

\[
I(a)=\{(i,j):1\le j\le a_i\}.
\tag{13}
\]

由 \(\kappa_i=\max_{a\in K}a_i\)，立即得到

\[
\boxed{
\bigcup_{a\in K}I(a)=I(\kappa)
=\{(i,j):1\le j\le\kappa_i\}.}
\tag{14}
\]

因此当前 \(c\) 到全部 kernel records 的缺失 layer 集大小精确为

\[
|I(\kappa)\setminus I(c)|=\sum_i\delta_i(c).
\tag{15}
\]

式 (14)--(15) 是“覆盖全部 ambient labelled kernel”的精确 layer requirement。
它只在 exact physical-source contract 另证真实来源必须覆盖该 ambient kernel 时，
才成为物理来源的必要义务。若再有同一规范来源上的独立积合成合同，保证各坐标
prefix layers 可相容地组成每个 \(a\in B_{c^*}\)，它才同时成为充分物理容量图。
没有这些合同，逐坐标 layer 都出现仍不能推出联合 physical record 存在。

严格反例取 \(A=C_2\)、\(E=\{0,1\}^2\)、\(w_1=w_2=1\)。此时

\[
K=\{(0,0),(1,1)\},\qquad\kappa=(1,1).
\tag{16}
\]

若 physical records 只有

\[
U=\{(0,0),(1,0),(0,1)\},
\tag{17}
\]

则两个 labelled layers 分别出现，却没有所需联合 record \((1,1)\)。因此统一
selector 必须在 (15) 之外保存 `PRODUCT_SYNTHESIS_PROVEN` 或等价的跨坐标来源回执。

## 4. neutral cargo 不能被角色约化删除

令

\[
Z=\{i:w_i=0\},\qquad J=\{1,\ldots,r\}\setminus Z.
\tag{18}
\]

并定义

\[
K_J=
\left\{a_J\in\prod_{j\in J}\{0,\ldots,e_j\}:
\sum_{j\in J}a_jw_j=0\right\}.
\tag{18a}
\]

零权坐标不影响 (2)，故有精确直积分解

\[
\boxed{
K=K_J\times\prod_{i\in Z}\{0,\ldots,e_i\}.}
\tag{19}
\]

特别地，

\[
\boxed{
i\in Z\Longrightarrow
\kappa_i=e_i,
\quad\delta_i=e_i-c_i.}
\tag{20}
\]

稳定子商或 source-SNF 可以在**角色判定**中删除零权方向，却不能在 labelled
capacity 中删除它们。任何声明要覆盖完整 ambient kernel 的分支都必须输出
`AMBIENT_KERNEL_NEUTRAL_CARGO_REQUIREMENT` 并恢复到完整 ambient 深度；
exact physical-source image 若更小，则须在其真实 record box 上重新计算。恢复这些
层不增加角色秩，也不能克隆 request id 或 charge key。

更一般地，若 \(o_i=\operatorname{ord}(w_i)\)，纯坐标 kernel records 给出

\[
\kappa_i\ge o_i\left\lfloor\frac{e_i}{o_i}\right\rfloor.
\tag{21}
\]

所以非零权方向也可能因周期回返强制额外的 role-neutral depth。

## 5. maximal kernel antichain 的适用边界

在 \(E\) 上采用坐标偏序，令 \(\mathcal M=\operatorname{Max}(K)\)。有限性给出

\[
\boxed{\downarrow K=\downarrow\mathcal M.}
\tag{22}
\]

因此对任意已经证明为 labelled downset 的来源集 \(D\subseteq E\)，

\[
\boxed{K\subseteq D\Longleftrightarrow\mathcal M\subseteq D.}
\tag{23}
\]

这会把全 kernel 检查压缩到 maximal antichain。但必须区分最小 downset 与最小
principal box：

\[
\downarrow\mathcal M\subseteq B_\kappa,
\qquad
\downarrow\mathcal M=B_\kappa
\Longleftrightarrow\kappa\in K.
\tag{24}
\]

例如 \(A=C_3\)、\(E=\{0,1,2\}^2\)、\(w_1=w_2=1\) 时，

\[
K=\{(0,0),(1,2),(2,1)\},
\quad
\mathcal M=\{(1,2),(2,1)\},
\quad
\kappa=(2,2)\notin K.
\tag{25}
\]

此时 \(\downarrow\mathcal M=E\setminus\{(2,2)\}\)，严格小于 \(B_\kappa=E\)。
若 physical source 未证明 divisor-downward closure，即使所有 maximal kernel records
出现也不能推出较小 records 出现；统一 selector 必须输出
`DIVISOR_CLOSURE_UNPROVED`，不得调用 (23)。

## 6. residue collision 与 section capacity

令 \(R=\beta(K)\)。定义

\[
\begin{aligned}
L(c)&:\quad K\subseteq B_c,\\
Q(c)&:\quad\beta(K\cap B_c)=R.
\end{aligned}
\tag{26}
\]

对每个 right inverse section \(s:R\to K\)、\(\beta\circ s=\mathrm{id}_R\)，有

\[
\boxed{
L(c)\Longleftrightarrow\text{每个 section 都落在 }B_c,}
\tag{27}
\]

\[
\boxed{
Q(c)\Longleftrightarrow\text{存在一个落在 }B_c\text{ 的 section}.}
\tag{28}
\]

式 (27) 对任意 \(\beta\) 都成立。若 \(\beta|_K\) 单射，则进一步有
\(Q(c)\Longleftrightarrow L(c)\)；否则 image coverage 可以漏掉同一 fiber 内的
labelled records。令

\[
\rho(c)=|\beta(K\cap B_c)|,
\quad
\lambda(c)=|K\cap B_c|-\rho(c),
\quad
u(c)=|R|-\rho(c),
\tag{29}
\]

则

\[
\boxed{u(c)=|R|-|K\cap B_c|+\lambda(c),}
\tag{30}
\]

且 \(Q(c)\) 当且仅当 \(u(c)=0\)。所以 labelled record 数超过 \(|R|\) 也不能替代
fiber-hit 检查。统一容量对象必须区分

\[
\text{depth defect }\delta(c),\qquad
\text{fiber defect }u(c),\qquad
\text{physical synthesis defect}.
\tag{31}
\]

## 7. \(p=557281\) 的精确 ambient 完成图

沿用 actual-F 控制

\[
p=557281,\quad D_*=182,\quad 4D_*=728,
\quad N_x=p+4D_*=558009=3^4 83^2.
\tag{32}
\]

以 record \((a,b)\) 表示 \(3^a83^b\)，则 ambient box 为

\[
E=\{0,\ldots,4\}\times\{0,1,2\}.
\tag{33}
\]

在 \(\eta(u)=(u\bmod13)^4\in C_3\) 中，\(w_3\) 的阶为 \(3\)，而
\(w_{83}=0\)。所以

\[
K=\{(a,b)\in E:a\equiv0\pmod3\},
\tag{34}
\]

\[
\boxed{
\kappa=(3,2),\qquad c=(2,0),\qquad\delta=(1,2).}
\tag{35}
\]

当前 record prefix \(B_c=\{(0,0),(1,0),(2,0)\}\) 满足
\(\beta(B_c)=\{1,3,9\}\)。到最小 ambient-kernel-complete principal box 的九条
新增 records 与 residue images 是

\[
\begin{array}{c|ccccccccc}
(a,b)&(0,1)&(0,2)&(1,1)&(1,2)&(2,1)&(2,2)&(3,0)&(3,1)&(3,2)\\
\hline
3^a83^b\bmod728&83&337&249&283&19&121&27&57&363.
\end{array}
\tag{36}
\]

该最小 box 有十二个不同 residue images：

\[
\{1,3,9,19,27,57,83,121,249,283,337,363\}.
\tag{37}
\]

它恰好从十五点 ambient box 中删除非 kernel 的 \(a=4\) 行
\(\{81,171,361\}\)，同时保留六条 kernel records

\[
(0,0),(0,1),(0,2),(3,0),(3,1),(3,2).
\tag{38}
\]

十五条 residue images 彼此不同，故本控制没有 collision 缺口。又因
\(\mathcal M=\{(3,2)\}\) 且 \(\kappa=(3,2)\in K\)，

\[
\downarrow K=B_{(3,2)}.
\tag{39}
\]

因此，如果以后独立证明 actual physical record **membership** 在 (33) 中
divisor-downward closed，并命中顶记录

\[
(3,2),\qquad 3^3 83^2=186003=N_x/3,
\tag{40}
\]

则一次 top-record membership 检查可压缩全部十二条 record membership 检查。
这仍不能从顶记录自动生成各因子的 provenance、state map 或 owner token；要压缩这些
typed maps，必须另证 `PROVENANCE_PRESERVING_DIVISOR_CLOSURE`。当前仓库连
set-level 下闭合同也没有，更没有 (40) 的 record-to-state/owner map，所以 (39)
目前只是精确的条件性 set compression，不是 source realization。

相对 legacy depth-\(2\) prefix，覆盖全部 ambient labelled kernel 的 layer
requirement 只新增

\[
\boxed{
\{(3,3),(83,1),(83,2)\}.}
\tag{41}
\]

第一项表示现有 \(3\)-lineage 的第三层，后两项是角色不可见的 neutral cargo。
这些是 ambient-completion 分支的三个 labelled missing layers，不是三个独立
elementary roles 或三个可收费 physical slots。

固定 legacy \(p=557281,x=182,s_0=19838,J=1\) lineage，已有 candidate binding
的数据满足

\[
\bigl(v_3(p+4s_0),v_3(x-s_0),v_3(p+4x)\bigr)=(3,3,4).
\tag{42}
\]

depth \(d\) 要求三者至少为 \(J+d\)，故

\[
d_{\max}=\min(3,3,4)-1=2.
\tag{43}
\]

所以只否定这条固定 lineage 的 depth 3，不排除替代 source-switch、另一 canonical
base 或新的 lineage。该 legacy row 不能生成 (41) 的 \(3\)-第三层。另一方面，
\((a,h)=(1,83)\) 是合法 Type II arithmetic factor block，但它的 F/G physical
membership 与 q-prefix owner token 未证；\(83^2\) 的算术 factor record 已由后续
因子盒定理证明，而 F/G square-owner receipt 仍未证。于是 legacy
ambient-completion 分支的精确 typed 状态是

\[
\boxed{
\texttt{AMBIENT\_KERNEL\_PREFIX\_DEPTH\_CERT}
(\kappa=(3,2),\delta=(1,2))}
\tag{44}
\]

连同

\[
\texttt{P557\_Q3\_X182\_S19838\_J1\_LINEAGE\_DEPTH3\_BINDING\_FAILED},
\quad
\texttt{H83\_OWNER\_TOKEN\_UNPROVED},
\quad
\texttt{FG\_H83\_SQUARE\_OWNER\_LAYER\_RECEIPT\_UNPROVED}.
\tag{45}
\]

## 8. 后续构造后的双账本更新

式 (35)--(45) 记录的是原 depth-\(2\) typed assignment 仍活跃时的 legacy ledger。
后续
[depth-\(3\) 规范基分类](type-I-fg-qprefix-depth3-replacement-lineage.md)
构造了 witness

\[
(s_0,s_1,D_0)=(14924,104468,7462)
\]

以及空的单请求 ledger 上的显式 fresh owner assignment。因此存在另一张合法选择：

\[
\boxed{
c_{\rm fresh}=(3,0),\qquad
\delta_{\rm fresh}=(0,2).}
\]

它不能直接写回旧 ledger：新旧 target keys 在绝对层 \(2,3\) 部分重叠，source keys
却改变，故不是 all-fresh 或同 assignment full replay。旧账本若已经活跃，当前回执是

\[
\texttt{Q\_PREFIX\_ATOMIC\_REPLACEMENT\_LEDGER\_UNPROVED}.
\]

两张账本是 alternatives，不可叠加。存在性选择器可以从空 ledger 直接选 depth \(3\)；
增量迁移器则必须保留 legacy depth \(2\)，直到另证原子 replacement transaction。

独立的
[同纤维因子盒定理](type-II-same-fiber-factor-box-neutral-role-capacity.md)
又给出

\[
\boxed{
\text{arithmetic factor-depth}=(4,2),\qquad
\kappa^\eta=(2,0),\qquad \nu_{83}^\eta=3.}
\]

所以 \(83^2\) 已在固定 Type II 算术合同中精确存在，且交叉 factor products 由唯一
分解自动合成；尚未证明的是 F/G physical membership、owner map 和 state realization。
又因 \(83\nmid|U(728)|=288\)，

\[
\operatorname{Hom}(U(728),C_{83})=0,
\]

故剩余两个 conditional owner layers 不能通过寻找 \(83\)-primary roles 来支付。
当前应并列保存

\[
\begin{gathered}
\texttt{TYPEII\_SAME\_FIBER\_H83\_SQUARE\_FACTOR\_RECORD\_EXACT},\\
\texttt{FG\_H83\_PHYSICAL\_MEMBERSHIP\_UNPROVED},\qquad
\texttt{FG\_H83\_SQUARE\_OWNER\_LAYER\_RECEIPT\_UNPROVED},\\
\texttt{H83\_C83\_PRIMARY\_ROLE\_RANK\_ZERO}.
\end{gathered}
\]

## 9. 统一选择器分派

~~~text
PREFIX_LOCAL_KERNEL_SECTION
  -> build labelled ambient exponent box and beta fibers
  -> AMBIENT_KERNEL_PREFIX_DEPTH_CERT(kappa, delta)
       (requirement for the full ambient-kernel completion branch only)
  -> alternative q-prefix assignment available?
       standalone fresh ledger: choose maximal available depth
       legacy ledger active + partial overlap: ATOMIC_REPLACEMENT_LEDGER_UNPROVED
       never add alternative lineages for one charge
  -> neutral coordinate present?
       yes: separate arithmetic factor depth from typed owner depth
            q not dividing ambient group order: Q_PRIMARY_ROLE_RANK_ZERO
  -> beta injective on the relevant kernel records?
       no: compute fiber defect u(c) and a supported section
  -> exact physical-source predicate + record-to-owner maps proved?
       no: EXACT_PHYSICAL_SOURCE_PREDICATE_UNPROVED
       yes: replace ambient K by the exact physical kernel records
            and recompute depth/fiber defects
  -> labelled divisor closure or independent product synthesis proved?
       set downclosure: maximal records compress membership only
       provenance-preserving downclosure: may also propagate typed maps
       exact factor-box synthesis: arithmetic divisors only
       typed product synthesis: realize all F/G layers in I(kappa) compatibly
       neither: DIVISOR_CLOSURE_UNPROVED / PRODUCT_SYNTHESIS_UNPROVED
  -> only after exact source image equality:
       KERNEL_SECTION_SOURCE_COMPLETE -> state realization -> E4 -> E5
~~~

本卡关闭的是 kernel-depth 的组合数学和 \(p=557281\) 的精确 ambient-completion
双账本。只有 exact physical-source predicate 证明真实来源必须覆盖相应 ambient
kernel 后，\(\delta\) 才能升级为物理必要容量；source predicate 的 exactness 本身
也不蕴含 divisor/owner closure。它严格排除了两个跳步：

\[
\text{逐 prime-power layer 出现}
\not\Longrightarrow
\text{kernel products physically present},
\tag{46}
\]

\[
\text{足够多 labelled records}
\not\Longrightarrow
\text{每个 residue fiber 被命中}.
\tag{47}
\]

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_kernel_depth_neutral_cargo_capacity.py --verify
~~~

验证器只枚举本卡基础定理的有限 exponent boxes、两个严格边界反例和
\(p=557281\) 的十五条 ambient records；legacy/fresh 双账本与 exact arithmetic
factor box 分别由上链接的两个聚焦 verifier 检查。不运行历史范围测试，也不验证
尚未建立的 physical-source predicate、typed product synthesis、state realization
或 E4/E5。
