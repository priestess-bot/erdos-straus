# T6 Global Selector 当前进度（复核整理版）

> 复核日期：2026-08-17
> 文档角色：T6 的状态入口；技术推导和候选引理见 [T6-V1.md](T6-V1.md)。
> 结论状态：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`。本页不把 T6、任一 high-support exit 或 Erdős--Straus 猜想标记为已证明。

## 1. 当前结论

对每个核心素数 \(p\equiv1\pmod{24}\)，T6 要求一个确定性的 selector
\(\Sigma(p,S)\)，它对每个由已验证边实际可达的 legal state
\(S\in\mathcal R_p\) 输出终端，或输出一条完整的递归边：

\[
\operatorname{terminal}(S)
\quad\text{or}\quad
\operatorname{verified\_edge}(S,T).
\]

后一项必须同时包含 E1--E5：实际 source/path、确定 target、target normal form、
\(W_T\to W_S\) 的全域解提升，以及固定 T5 势的严格下降。selector 不能读取未知目标解，
不能依赖有限搜索上界，并且必须对自己的后继继续有定义。精确量词见
[旗舰证明纲领](../concepts/flagship-proof-program-2026-08-16.md) 和
[状态合同](../concepts/denominator-escape-state-contract.md)。

目前已经建立的是“已承认 recursive edge 必然下降”，而不是“每个 nonterminal state 都已有边”：

\[
\boxed{
\operatorname{verified\_edge}(S,T)
\Longrightarrow
\Pi_{T5}(T)<\Pi_{T5}(S),
\qquad
\text{但 }\operatorname{Out}_{\mathrm{verified}}(S)\text{ 的非空性仍待证明。}
}
\]

因此，在当前合同的实际可达域中排除 dead end 是 T6 的首要存在性缺口；随后还须把可用
出口固定为不读取未知解的确定性规则。T6 不是 T5 的同义改写。

## 2. 已接纳结果与边界

| 项目 | 当前状态 | 已接纳范围 | 仍未覆盖的部分 |
|---|---|---|---|
| T1 / H4 clean \(q\) | 相对闭包已建立 | 归档的 actual arm 与其具名 receipt | 其它 H4 selector branch、后续 F/G 出口 |
| T2 | 当前具名 atomic surface 闭合；full open | H4 \(a=1\) 与 c=8 double-low 两个 `v1` arm 恰好穷尽当前 taxonomy | future raw arm、pooled-capacity、输入覆盖与全域 admission |
| T3 | 抽象命题开放；当前具名图中不可达 | 当前 15 个 concrete generators 都保持 \(W=\operatorname{Sol}(p)\)，无 nontrivial-mark seed | 任意 future marked edge 的 serializer、membership 与 lift |
| T4 | ordinary \(q\ge1\) 相对闭包已建立 | actual terminal-first ordinary G 统一进入同一个 p-only fresh full-carrier root，并通过 origin-normalized 首条 local edge | nontrivial mark、首条边之后的 Type-I totality |
| T5 | 合同层闭合 | 所有 contract-recognized persistent edge 的七元势严格下降 | 任何 E1--E4 candidate 自动有 ticket，或 selector totality |
| 初始 \(q=1\) 根 | 已闭合 | 每个核心 \(p\) 均按 \(X=(p+3)/4\) 分派为 gap-3 root terminal，或 ordinary G 到 full-carrier 的 actual E1--E5 handoff | handoff 后 Type-I totality 与全局 reachable-state exhaustion |
| T6 | 开放 | terminal-first 与五类输出的验收规则 | 每个实际可达 nonterminal state 的 terminal 或 verified successor |

closed-world 审计说明 full T2 与 nontrivial T3 不是**当前具名图**的 live blocker；但 future
selector 若新增 atomic arm 或 marked generator，就必须重开相应义务。其它 T1 input、c=8
outgoing existence、一般 overflow 与 high-support 分支仍没有全局归约定理，不能把 T6 缩写为
只剩 proper-root。

## 3. 已确认不能使用的捷径

1. **只凭 \(A\mid K\) 重置到 fresh low chart。** 这会丢弃 charged history；缺少实际
   persistent receipt 时不能通过 E1--E5。
2. **PRE/ABSORB 的形式调度或有限图无环。** 它们至多提供 E5 的相位规则。没有 E1--E4 和
   全域 lift 的 cursor edge 仍不是递归边。
3. **Fourier、商群或 q-adic 必要条件。** `analysis_evidence` 不会自动成为
   `support_switch`、`q_adic_lift` 或 `verified_edge`。
4. **把更小整数或一张 Type-I chart 当作递降。** \(n<p\) 或 \(k\mid K\) 不产生
   \(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 的 lift，也不支付旧 support 的账。

这些边界由 [状态合同的 E1--E5 规则](../concepts/denominator-escape-state-contract.md) 和
[T5 合同](../concepts/t5-global-well-foundedness-contract-v2.md) 固定。

## 4. 当前研究焦点

### 4.0 初始 \(q=1\) 根序列化已闭合，但只闭合 base construction

对每个核心素数取 \(q=1\)、\(m=3\)、\(X=(p+3)/4\)。若 \(X\) 含有
\(2\pmod3\) 的素因子，最小这样的素因子直接给出 Type II root terminal；若没有，
\(X\) 的全部素因子均为 \(1\pmod3\)，从而得到 ordinary q=1 G receipt，并由既有
full-carrier rule 给出一条 actual E1--E5 `PHASE_DROP`。这个 base receipt 由 \(p\)
单独重放；它的 terminal-first digest 只覆盖 q=1 gap-3 predicate，不伪造 incoming
recursive edge，也不把 gap-3 之外的 terminal 扫描说成已完成。

因此 O1 的 initial-root 子义务和 `initial_state_serializer` gate 已关闭。G target 的后续
Type I selector 仍落在 `GAP-O1-POST-G-TYPE-I`，而所有实际可达状态的穷尽仍是
`GAP-O1-GLOBAL-EXHAUSTION`；`T6_GLOBAL_SELECTOR_TOTALITY` 保持 `OPEN`。

### 4.1 Ordinary G 的 positive-\(q\) adapter 已相对闭合

对每份 actual、terminal-first、ordinary positive-\(q\) G source，新增 adapter 从当前整数重算
endpoint downset 与 canonical finite-abelian G separator，重放 source state / terminal-first
摘要和 target universal \(p\)-source，并构造不含 source \(q\) 的 target serialization。因此

\[
\text{every actual ordinary positive-}q\text{ G endpoint}
\longrightarrow
\text{fresh full-carrier Type-I root}.
\]

已在相对 source hypothesis 下建立。E4 是 \(\operatorname{Sol}(p)\) 上的恒等 lift，E5 使用
canonical T5 major phase \(3\to2\)。focused controls 不制造 actual source receipt，所以仍标为
conditional adapter controls；actual root 的两种注册 origin 已由同一个 semantic projection
接入首条 Type-I local edge，并以 `LOCAL_DROP` 支付。

### 4.2 High-support / proper-root stutter 是优先残余，而非全局压缩定理

对已进入 Type-I `CHARGED` 的状态，\(A>B_p=(p-1)^2/4\) 时
\(\lfloor B_p/A\rfloor=0\)。此时必须通过 \(K/A\) 的真实下降、phase drop、outer-rank
source 或 terminal 处理；不能只凭内部 checkpoint 支付 E5。

proper-root stutter 提供了较强的算术结构：正定 Eisenstein 范数、小商和约化除子；详见
[T6-V1.md](T6-V1.md)。它是当前最具体的 Type-I 残余之一，但尚未证明所有实际可达状态都会
归入此分支。

对 residual `A>1` overflow，`total_cofactor_typed_projection_v1` 已把一个**外部已登记**的
persistent source 加 terminal-first miss 处理为内容寻址的 source/target，并独立重算
hit/F/G、Smith F witness、HNF-dual G separator、scope 和 Type-I local-drop。它因而消除了
一般 typed serialization 的实现缺口；但它不能从一条 determinant 或非空 digest 推出 source
确实已入队，也不证明每个 residual state 都拥有这类登记。该相对 adapter 不是 O1 的全称 exit，
详见 [total-cofactor adapter 接入记录](T6-total-cofactor-typed-adapter-integration-2026-08-18.md)。

该子域已有两项全称收缩：\(c=h\) 的 named odd-distance fan 已严格排空；Eisenstein quotient
的 \(k=1\) actual 子域也由 cyclotomic common-divisor 排除与 Vieta 无限下降严格排空。另有
\(\gcd(a,e-1)\mid\gcd(h,k)\) 的公共因子对齐：共享 Eisenstein 因子必是 \(h\)-supported，
而 \(q\mid k,\ q\nmid h\) 的 quotient-only 因子不能被误投到旧 root-capacity source menu。
这只是 provenance 收缩，不保证菜单命中或 physical edge。真正剩余的是 \(k>1\) quotient
carrier 的 physicalization（QC1），或 transverse \(D_*\) carrier 的全称 E1--E5 出口（TR1）。
其中 \(k=3\) 现在还有四个等价的严格 primitive fiber 坐标：写
\(A=a/3,B=(e-1)/3\) 后，fixed-\(d\) 候选满足
\(A\mid3d^2+d-1\)；若 \(\rho=B-A\)，则同一整数曲线还满足
\(A\mid3\rho^2+\rho-1\) 与 \(3(A+\rho)+1\mid9\rho^2-6\rho-2\)。每个
固定 \(d\) 或固定 \(\rho\) 都只剩有限 divisor fiber。再令
\(j=m-\rho\)，则 \(A\mid9j^2+7j+1\) 且
\(\rho(3j+1)+j=3A(A-j+1)\)，所以固定 \(j\) 亦为精确有限 fiber。再写
\(t=B-m=A-j\)，则严格 \(A<m<B\)，并有
\(A\mid9t^2-7t+1\) 与 \(d\mid9t^2+6t-2\)，固定 \(t\) 亦只留下有限
\(d\)-divisor fiber。\(t=1\) 仍唯一恢复
\((A,B,p)=(1,7,939)\) 的非核心 \(A=1,d=1\) 边界，因而 actual core candidate 满足
\(1\le j\le A-1\) 与 \(2\le t\le A-1\)。\(d\)、\(\rho\)、\(j\) 与 \(t\)
都没有全局上界，不能把这一局部收缩误写成 QC1。见
[\(k=3\) primitive fiber reduction](../claims/type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md)。
generic actual-root cyclotomic identity 还把 shared factor 与 primitive quotient 精确分开：写
\(a=gA\)、\(e-1=gB\)、\(h=g\alpha\)、\(k=g\kappa\)，则
\(e^2\alpha+e(A-2B)+\kappa=gA^2(p^2+p+1)/h\)。因此所有 quotient-only
素因子只能留在 \(\kappa\)。进一步，对每个 \(q\mid\kappa,\ q\nmid h\)，令
\(v=(p^2+p+1)/h\)，则精确有
\[
q\mid v
\quad\Longleftrightarrow\quad
q\mid e\ \text{or}\ B\equiv(p+1)A\pmod q.
\]
这只把 quotient-only 因子分为 cyclotomic-complement 与非 complement 两支，仍不产生
source、lift 或 target。在 \(k=3\) core primitive system 中
\(h\mid p^2+p+1\) 本已自动恢复，且必有 \(B\equiv t\equiv2A+1\pmod3\)；
这不是额外 admission filter，不提供
physicalization、lift 或 parameter bound，故 QC1 保持开放；见
[primitive quotient normalization](../claims/type-I-root-capacity-stutter-primitive-quotient-normalization.md)。
此外，保持 \(A,M\) 并把 \(B\) 换为该方程另一 Vieta 根 \(j\) 的直接递降已经被
第二整数门排除：它不能连同一个整数 \(p_j\)，所以不是可补 E1--E5 的 target。该结论
只消除这一条重图表尝试，不排空 \(k=3\) 或 QC1；见
[Vieta companion obstruction](../claims/type-I-root-capacity-stutter-k-three-vieta-companion-obstruction.md)。

### 4.3 c=8 residual 只在实际可达且未被抢占时处理

c=8 / \(q_\star=103\) 的四次整除门可作为必要条件记录，但不能单独作为 T6 exit。只有在
actual provenance、terminal-first 和 target receipt 都保留后，才应继续尝试导出 terminal 或
带 T5 ticket 的 successor。

## 5. 本轮复核后的技术状态

| 技术项 | 结论 | 证据等级 |
|---|---|---|
| 初始 \(q=1\) 根 terminal-or-edge 分派 | 对每个核心 \(p\) 完成 frozen p-only root serialization；命中 \(2\pmod3\) 素因子时终端，否则接入 q=1 G full-carrier edge | `established`, `internal_review`；不构成全局 T6 |
| \(q=1\) G full-carrier handoff | 已建立，范围不扩张 | `established`, `independent_review` |
| ordinary positive-\(q\) G universal handoff | 对 actual terminal-first ordinary source 相对闭合 | `established`, `internal_review` |
| \(c=h\) 奇距离 translated-square fan | named family 在 actual proper-root scope 内全称 no-go | `established`, `internal_review` |
| proper-root \(k=1\) quotient | actual 子域全称为空；无有限扫描 | `established`, `internal_review` |
| proper-root \(\gcd(a,e-1)\) 对齐 | 公共因子只可落在 \(\gcd(h,k)\)；拆开 h-supported 与 quotient-only residual | `established`, `internal_review`；不构成 edge |
| proper-root primitive quotient 正规化 | 除去全部 shared \(g\) 后得到 exact primitive system、actual-root cyclotomic saturation identity，以及 quotient-only \(q\) 的 cyclotomic-complement 分流；quotient-only 因子只能留在 \(\kappa\) | `established`, `internal_review`；只收缩 QC1 provenance，不构成 edge |
| proper-root \(k=3\) fixed-\(d\)/fixed-\(\rho\)/fixed-\(j\)/fixed-\(t\) fibers | 四种等价 primitive divisor 约化；core primitive system 自动恢复 \(h\mid p^2+p+1\) 并给 \(B\equiv t\equiv2A+1\pmod3\)；fixed-\(j\) 消去旧 gate 的冗余因子 \(3\)，fixed-\(t\) 给出 \(A<m<B\) 与 \(2\le t\le A-1\)，同-\(M\) Vieta companion 的第二整数门被排除，且共享 \(A=1,d=1\) 边界重现已排除的 \((m,a)=(6,3)\) 行 | `established`, `internal_review`；无全域 parameter bound，QC1 仍开放 |
| proper-root \(m=3\) 双二次范数 slice | 写 \(A_3=a/3\)、\(h=3u\) 后得到精确互锁 gates \(A_3\mid3u^2-u+1\)、\(u\mid7A_3^2+A_3+1\)；actual core congruence 强制 \(A_3\equiv3\pmod {24}\)、\((a,e-1)=3\)、\(k=3\kappa\equiv21\pmod {72}\)、\(k\ge93\)、\(W-\eta\ge13\)，fixed-\(\kappa\) fiber 满足 \(A_3\mid9(27\kappa^2+8\kappa+1)\)。whole \(d=(W-\eta,k)\) carrier 满足 \(d\mid p^2-p+1\) 且 \(\gcd(d,h(p^2+p+1)D)=1\)；其 \(d>1\) natural fan 还满足 \(C_d\ge40\)、\(s_d\le(p-40)/39\)。canonical \(q_\star\equiv7\pmod {12}\) 因而严格分为 root-supported、\(\Phi_6\)-fan 与 d-free quotient-only 三路；\(D\) 的 native quadratic form 判别式为 \(-11\)，并强制 native raw Type II menu 为空 | `established`, `internal_review`；曲线坐标 \(A_3\) 与 root-chart support 必须分开；该项压缩 \(m=3\) 的新 adapter 输入并排除一个完整 Type II terminal chart，不给 E1--E5，QC1/TR1 仍开放 |
| proper-root \(m=3\) transverse overlap | 以 root-capacity 坐标 \(\varrho\)（不等于 \(-27\) 范数商）计，\(D_H=(D,h^2-1)\in\{1,5\}\)；\(D_H=5\) 当且仅当 \(p\equiv1\pmod5,u\equiv3\pmod5\)。并有 \(D_*>(2p+1)/5\)、\(D_*\mid2\varrho+3\)，故 \(\varrho>(p-7)/5\)，而 \(D_H=1\) 时 \(\varrho\ge p\) | `established`, `internal_review`；真实高-root 输入收缩，不构成 terminal 或 TR1 edge |
| proper-root \(m=3\) automatic low-gap factor gate | 对任意允许 \(A_0\) 的 positive root-residue gate，及同一 general-\(A_0\) quadratic fan 的 low-gap negative linear-factor specialization，\(\Delta_s=3s^2-s+1\) 的逐项分解都只留下 \((s,q)=(3,5)\)。正根给出 direct Type II terminal；负根仅为既有 \(p-1,h+1,m+2\) overlap | `established`, `internal_review`；排空这个 fixed low-gap family，不构成 TR1 |
| proper-root \(m=3\) residual \(q=5\) | terminal-first 后 \(5\mid D_*\) 当且仅当 \(v_5(3u^2-u+1)\ge v_5(A)+2\)，即 \(u\) 落在 \(-11\) norm 的唯一 \(5\)-进 Hensel 管；这强制 \(p\equiv11\pmod{25}\)、\(h\equiv9\pmod{25}\)、\(u\equiv3\pmod{25}\)，且 \(v_5(p-1)=v_5(h+1)=v_5(m+2)=1\)。更精确地 \(\varrho\equiv11\pmod{25}\) 当且仅当 \(v_5(T)\ge2\)；唯一未定向 leaf 为 \(v_5(D_*)=v_5(T)=1\)、\(5\nmid E\)、\(v_5(R-h)=2\)，且它强制存在一个非 \(5\) 的 pure-\(T\) 素因子 \(\ell\mid D_*/5\)。更强地，\(L_5=D_*/5\) 的任意非平凡除子都不命中 general-\(A_0\) positive whole-divisor Type II terminal fan，且每个 \(\ell\mid L_5\) 都避开 reflected negative ray | `established`, `internal_review`；把既有 \((3,5)\) overlap 转化为明确的 pure-\(T\) physicalization 输入，并排除两类 variable-gap Type II terminal family；不构成 terminal 或 TR1 |
| relative total-cofactor typed adapter | 已实现 source/target retyping、F/G/hit 与 local-drop receipt | `established`, `internal_review`；仅消费外部 registration，不证明 actual reachability |
| Eisenstein quotient \(k\) 的 EQ1--EQ6 | 由已知 stutter 恒等式可推的代数包 | `analysis_evidence`；不构成 edge |
| canonical low chart from \(k>1\) | 图表存在 | 缺 E1--E4/provenance，不构成 edge |

最小 \(q=5\) leaf 还有一个新近固定的边界：对每个 \(1<J\mid L_5\)，
\(D/J\) 的 cofactor 虽严格，却不可能重建同一 \((\mathcal A,K,R-h)\) 的 canonical
maximal receipt。因此它不能作为 E1 的 factor-deletion rebase。对
\(\ell\mid L_5\)，只有 \(\ell\mid E\) 的分支在当前 endpoint 已有 raw
overcapacity，并可追加到已知 universal root raw word；但该 word 仍不支付
persistent E1 root-policy。更精确地，这条 actual raw deflation 的 lcm support 为
\(\mathcal A E/\ell\)，canonical cofactor 为 \(p-\ell\)。并且它有一个完整、无需搜索的
complete-excess 分流：写 child 为 \(x+y=R\)，则其一侧满足
\(E_x=E/\ell,D_x=D\)，且两侧皆 p-free。若 \(y\beta_x\mid K\)，它已满足单侧
bundle 的全部算术 kernel，并以 \(p-\ell\) 严格支付 E5；若不满足，则另一侧的
maximal block 必有 \(Q_y>1\)，从而精确进入 atomic split kernel。令
\(F_y=Q_y/(\mathcal A,Q_y)\)，split support 为 \(\mathcal A(E/\ell)F_y\)，其 rank stutter
**当且仅当** \(F_y\equiv\ell\pmod p\)；除此一个同余外，split 也严格支付 E5。
若该唯一 stutter 真的发生，写 \(D_y\) 为另一侧 canonical residual，则它还被压到
\(D_y\mid\gcd(K/D,eD/\ell-1)\)、\(\ell D_y\equiv1-D/\ell\pmod p\) 和
\(F_y=\ell+2ps\ (s\ge1)\) 的 child-compatibility normal form；其中第二个
divisibility form 是固定 raw child 后的等价重写，不是独立 no-go 门，仍未证明残余为空。
更进一步，写 \(E=1+p\sigma\)、\(D=\ell D_1\)，rank stutter 的两个 lift 参数满足
\(n_y+sD_y=1+\sigma(\ell-1)D_1/2\)。因此 \(D_y\) 必落入由
\(\gcd(K/D,eD/\ell-1)\) 的除子、\((D_yF_y,DE)=1\)、两个显式整性条件和该上界定义的有限
source-data-only candidate menu；反向候选仍须通过 child 的 canonical complete-excess 重算，故这不是空性或 edge。
proper-root 尺度还给出残余尺寸门：\(n_y=0\) 时 \(D_y\ge5\)，\(n_y\ge1\) 时
\(D_y\ge23\)；特别地 \(D_y=1,3\) 都不可能。因此 rank-stutter 必携带一个奇的、
非平凡 residual divisor。
所以这一 raw child 不再有未分类的 complete-excess 算术障碍。其余 \(\ell\) 在当前
endpoint 已处于容量内，必须寻找新的 occurrence 或新的 physical adapter。未提供下段所述
source-bound path 的上述两支仍缺 persistent E1 root-policy、terminal-first、typed target/
normal form 和全域 lift，故这缩小了 TR1 的下一条构造命题，但不构成 terminal 或 edge。

这里的 E1 边界现可进一步精确化：universal raw word 不能**创建** persistent root source，
但若一个已入队 source 的回执已经把实际 raw path 绑定到 \((z,h)\)，则
\(\ell=\min\operatorname{Prime}((E,L_5))\) 的 raw deflation 是该 source 的正向 suffix。
在 child terminal-first miss 后，单侧分支或 \(F_y\not\equiv\ell\pmod p\) 的 atomic split
分支已有 E1 witness 与严格 E5；既有 adapter 的 validator 条件满足时可继续支付 E2--E4。
这没有证明每个 actual proper-root stutter 保存该 path、满足 \((E,L_5)>1\)，或避开
\(F_y=\ell+2ps\) 的 rank stutter，故 TR1 和 T6 仍开放；但 “缺 E1” 现在准确地只剩
source-path coverage，而不是这条确定 raw suffix 本身。

rank-stutter 本身也不再是“没有下一条 raw action”：因为
\(F_y\equiv\ell\not\equiv1\pmod p\)，它必有一个确定的最小素因子
\(q_\star\mid F_y\)、\(q_\star\not\equiv1\pmod p\)。把 \((x,y)\) 定向为 \((y,x)\)
后，\(q_\star\) 是 actual overcapacity label，故可实际走到
\((y/q_\star,R-y/q_\star)\)，且无 gcd reduction。若原 path 已 source-bound，这仍是同一
source 的正向 suffix。形式支撑 \(M_{\rm split}/q_\star\) 的 cofactor 为
\(\langle-q_\star\rangle_p\le p-2\)。不过 companion 可能重生新的 complete-excess block，
所以该形式支撑还不是 canonical target 或 verified edge；当前最小的剩余命题正是证明或
反驳 second-child canonicalization / companion non-reintroduction。

更强地，对 \(y\) 完整容量剥离的 selected-side endpoint 精确为
\((y,K)=D_y(Q_y,p-1)\)，且 \((Q_y,p-1)\mid F_y\)。故当前 rank-stutter 精确分成
\((Q_y,p-1)=1\) 的 fresh-residual branch 与一个显式 \(p-1\) overlap branch；这是 raw
occurrence 的二分，不是 terminal 或 verified edge。

并行地，atomic split stutter 的 canonical arithmetic target 已被精确识别为新的完整乘积
\(d=1\) 饱和行。若
\[
L=\frac{M_{\rm split}}{\mathcal A}=\frac E\ell F_y=1+p\theta,
\qquad
\theta=\sigma+2s_yE/\ell,
\]
并以原 root 的 \(d=1\) normalisation
\((p+1)/2=g a_0,(N+1)/2=g b_0\) 表示，则 target normalisation 的公共因子精确为
\(\gamma=(a_0,L)\)。它的 ordinary \(d=1\) dispatch 因而完全由 source 数据决定：
raw-\(p\) source failure、\(p\)-free failure、canonical regeneration 和严格 capacity drop
分别对应四个显式模 \(p\) 类。结合既有 d=1 结果，若这个 target 真能作为 guarded
checkpoint 接入，仍会落入未闭合的 \(a=1\) \(p\)-primary hard branch 当且仅当
\[
a_0\mid L,
\qquad
b_0\equiv a_0(\theta-1)\pmod p.
\]
这是新的精确 residual gate，而非 E1--E5 edge：atomic target 的 provenance、typed
normal form、terminal-first 和全域 lift 仍须在同一宏内完成。它与第二 child 的
canonicalization 问题并列，给出了下一步可直接证明或证伪的两条最小命题。

对 \(m=3\) 本身，还有一个更强的 root-level 收缩。写
\[
N=\frac{4\mathcal A+1}{p},\qquad E=1+p\sigma,\qquad D+h=3p+1,
\]
则 root identity 强制
\[
\lambda_0=\frac{\sigma D+5}{p-1}\in\mathbb Z,\qquad
N=p\lambda_0-2,\qquad \lambda_0\equiv3\pmod4.
\]
故 \(N\equiv-2\pmod p\)、\(R\equiv1\pmod p\)：原 root 的 ordinary \(d=1\) bundle
已经精确落在 \(p\)-free failure，而非 raw-\(p\) source failure。若相应 persistent
macro 的前提能够接入，既有 peeled construction 已处理 \(a_0>1\) 的严格容量出口；
剩余必须有 \(a_0=1\)。这个子纤维等价于
\[
\lambda_0=2r(p+1)-1,\qquad
b_0=2pr-1,\qquad
\sigma D=2r(p^2-1)-p-4\quad(r\ge1),
\]
并强制 \(\sigma(h+2)\equiv3\pmod{p+1}\)。在该 \(a_0=1\) 残余中，上述 atomic
target 再次进入 \(p\)-primary hard branch 当且仅当
\[
L\equiv1\pmod{p^2}.
\]
这没有关闭 TR1：它把下一条 \(m=3\) 证明精确收缩为二阶 congruence 的排空，或将该
congruence 族接入具备完整 E1--E5 的 guarded macro。

在这个 \(a_0=1\) 子纤维再附加 minimal \(q=5\) leaf 时，约束进一步相互锁定：
\(D=25L_5\)、\(5\nmid L_5\)，而从 \(D\mid3p^2+p+1\) 和
\(\sigma D=2r(p^2-1)-p-4\) 可得
\[
D\mid(2r+3)(p+4).
\]
任一 \(\ell\mid L_5\) 若整除 \(p+4\)，则 pure-\(T\) 的
\(2\varrho+3\) 与 \(h^2-h-2\varrho\) 两条整除会强制 \(\ell\mid135\)，矛盾。
因此 \((L_5,p+4)=1\)；再用 \(v_5(p+4)=1\)，得到
\[
5L_5\mid2r+3,\qquad
2r+3=5L_5w,\qquad
w\frac{p^2-1}{5}=\sigma+e+p.
\]
特别有 \(r>(p-7)/5\)、\(r\equiv1\pmod5\) 及
\(\sigma+e+p\equiv0\pmod{48}\)。这把 pure-\(T\) carrier 直接绑到 d=1 residual
参数上，但 \(w\) 仍无界，故并未排空 \(L\equiv1\pmod{p^2}\) 或完成 E1--E5。

该 minimal leaf 现在还有一个更细的 root-support 分解。记 \(\Xi=5\sigma+w\)，则
\[
4\mathcal A=5L_5(p+1)\Xi,
\qquad
\frac KD=\frac{(p^2-1)\Xi}{20}.
\]
这不是形式重写：canonical complete-excess 的逐赋值规则强制
\[
(E,\mathcal A)=(E,L_5),
\qquad
(E,p+1)=(E,\Xi)=2,
\qquad v_2(\Xi)=1.
\]
所以触发 root deflation 的任意 \(\ell\mid(E,L_5)\) 必避开 \(\Xi\)，而 split-stutter
child 的 residual 已从一般 \(K/D\) 因子收缩为
\[
D_y\mid
\gcd\!\left(\frac{(p^2-1)\Xi}{20},eD_1-1\right),
\qquad (D_y,25L_5E)=1.
\]
更重要的是，\(E\) 的所有奇素因子都已落在 \(L_5\) 上；故先前 source-bound suffix 所需的
\((E,L_5)>1\) 现在等价于 \(E\) 不是纯二幂。唯一新隔离出的 \(E=2^a\) boundary
不能自动调用现有 pure-dyadic half-power 结果，因为后者还需要本 receipt 未提供的 Jacobi
F-state / half-power source data。
不过它也不是 raw-suffix dead end：记 \(\lambda=v_2(p-1)\)，complete-excess 的逐赋值
定义给出 \(a>\lambda\)，而 \(2^a\equiv1\pmod p\) 排除唯一临界值
\(a=\lambda+1\)。故 \(a\ge\lambda+2\)，实际 \(q=2\) raw deflation 后的 selected-side
normalisation 精确为 \(E_x=E/2,D_x=D,M_x=\mathcal A E/2\)，cofactor 为 \(p-2\)。
所以无论 \(E\) 是否有奇素因子，都已有一个确定的 actual raw deflation label；尚未关闭的
仅是 companion 的 complete-excess 重生、atomic admission 与完整 E1--E5，而不是 multiplier
本身没有可选 physical raw move。
对 rank-stutter 后的 second suffix，所选 \(q_\star\) 自身的 companion reintroduction 也已
缩成一个 exact unit-excess gate：写 \(b=v_{q_\star}(y)\)、\(y'=y/q_\star\)，则
\(q_\star\mid R-y'\) 当且仅当 \(b=1\) 且 \(R\equiv y'\pmod {q_\star}\)。该情形自动有
\(q_\star\nmid K\)、\(q_\star\parallel F_y\)、\(q_\star\nmid D_y\)；若 \(b\ge2\)，
companion 不含 \(q_\star\)，相对原 root support 新鲜重算的 joined support 的该素数指数不超过 formal
\(M_{\rm split}/q_\star\) 指数。尚未处理的是其它新素数的 companion excess，而不是
\(q_\star\) 的任意层都可能回流。companion 的 \(p\)-block 也不是隐藏例外：它恰在
\(q_\star\equiv1-D_1\pmod p\) 时出现；因此 p-free admission 的失败门同样已显式化。
更一般地，second child 的其它新素数不再需要逐一猜测：对
\((y/q_\star,R-y/q_\star)\) 的两侧重算唯一完整 excess blocks \(Q_-,Q_+\)，便有严格穷尽：
两块皆空给 Type I terminal；恰一块非空给 single-side bundle；两块皆非空给 atomic split。
在 p-free gate 通过后，所有 companion correction 都被一个 canonical
\(L_2=\operatorname{lcm}(\mathcal A,Q_-,Q_+)/\mathcal A\) 吸收；E5 失败当且仅当
\(L_2\equiv1\pmod p\)。所以 second-child 的最小剩余已是 source-path/typed receipt、
\(q_\star\equiv1-D_1\pmod p\) 和 \(L_2\equiv1\pmod p\) 三个明确义务，不再是未分类因子。
其中 p-block 义务也已有二阶的精确 dispatch，而不是一个笼统的失败类：令
\(\Theta_j\equiv yR^{-1}\pmod {p^j}\)，则 \(p^j\mid R-y/q_\star\) 当且仅当
\(q_\star\equiv\Theta_j\pmod {p^j}\)。在首层，\(p^2\mid R-y/q_\star\) 与
“剥掉唯一一层 \(p\) 后互补坐标重新含 \(p\)”分别是两个不同的模 \(p^2\) 类；其余
首层 lift 回到双侧 p-free raw node。所有三支都保留一个从同一 source 出发的 actual
raw suffix，但尚未成为 terminal 或 E1--E5 macro。
更强地，p-block 不再是这个 raw policy 的必要分支。把 \(y\)-side 的真实可剥离
prime occurrences 从 \(p-1\) overlap 中分开后：若存在 residue 既非 \(1\) 亦非
\(1-D_1\) 的 occurrence，就选最小的一个；否则全部 bad occurrence 都为
\(\delta=1-D_1\)，且严格至少有两个。后一情形连续剥离两个 occurrence，所得乘子
为 \(\delta^2\)，它同时避开 \(\delta\)（故 companion p-free）和 \(1\)（故 formal
cofactor 严格）。因此可确定地在至多两条 actual raw 边后回到 p-free primitive node；
剩余的不再是 p-block，而是该最终 node 的 canonical complete-excess multiplier、其
rank-restoration gate 以及 E1--E4 receipt。
若把 \(y\) 侧全部真实 excess 一次剥尽，则得到 \(Y_K=(y,K)=D_yJ_y\)。其唯一
p-block residue 是 \(\mathcal W_y\equiv1-D_1\pmod p\)；其余情形该 endpoint 是
p-free，且由于 \(Y_K\mid K\)，只能是 Type I terminal 或 single-side bundle，不能再
是 atomic split。更重要的是 \(\mathcal W_y\not\equiv1\pmod p\) 已被严格排除，故
full-capacity word 的 selected-side formal cofactor 总严格。此分流为后续 canonical
companion 分析提供了一个较窄的单侧入口，但仍不替代 E1--E5 admission。
合并两条分流后，rank-stutter 现有一个只读取当前 receipt 的确定 p-free raw policy：
若 \(\mathcal W_y\not\equiv1-D_1\)，走 full-capacity word；否则走至多两步的
bad-residue word。两者都保留严格 formal cofactor；差别仅在前者的 nonterminal endpoint
已是单侧、后者仍可能为 atomic。这消除了 p-block 作为必要 raw-policy branch，但没有
解决最终 canonical lcm 的 rank gate 或 E1--E4。
若它还重复进入 \(L\equiv1\pmod{p^2}\) 的 \(a_0=1\) hard branch，写
\(L=1+p^2\chi\)，则实际 child 还必须满足一条新的模 \(p^2\) lifted congruence
\[
\ell D_y\equiv
1-D_1+p\left[3+\sigma((\ell-2)D_1+1)\right]\pmod{p^2}.
\]
这将残余压到原 finite source-data divisor menu 的一个附加 \(p^2\) 条件子菜单；并未证明该菜单为空，
也没有补上 atomic checkpoint 的 E1--E4 或 second-child canonicalization。因此 TR1 与
T6 仍保持 `OPEN`，但下一条证明对象已不再是未结构化的二阶同余。

补充：在 actual \(m=3\)、whole-\(d\)、\(s_d=3\) 子分支中，双范数门与 exact
primitive content 强制 \(d=13\)、\(\rho=160+234z\)、\(A=52t-1\)，并使 primitive
quotient \(q\) 的全部素因子落在 \(1\pmod3\)，且最小 leaf \(q=1\) 全称为空。这排除了从
\(q\) 自身抽取 gap-\(3\) natural-fan residue 的路线；进一步由 \(-11\) divisor gate
与 high-gap primitive norm，实际剩余满足 \(t\ge13\)、
\(q\equiv13\pmod {24}\)、\(q\ge2893\)：奇 \(z\) 支已强制 \(z\ge17,\sigma\ge955\)，
偶 \(z\) 支更强制 \(z\ge108,\sigma\ge5869\)。primitive norm 仍强制
\(\tau>\sigma\)（即 \(W-\eta>\eta+1\)）与 \(A<\rho\)。再令
\(S=(7\rho^2+4\rho+1)/u\)，则 \(S\equiv3\pmod6\)，并有 exact composite defect
\(R_{q,S}=91q-12S>0\)、\(R_{q,S}\equiv7\pmod {12}\)。该 defect 目前尚未连回
\(u,d,D_*\) 或 \(\kappa\)，所以这些都是局部输入收缩，不是 terminal、E1--E5 edge、
QC1 或 T6 的闭合。同一 high-gap 子支还满足 \(p>2h\)，故 actual \(D_*\) 也不能直接
充当既有 odd-distance even-source fan 的距离：\(D_H=1\) 时 \(D_*>p\)，而 \(D_H=5\)
时 \(c=D_*\) 给出的偶源 \(p-c\) 已严格小于 \(c\)，与该 fan 的首个因子参数矛盾。
这只排除一个 named lift family，不使 TR1 闭合。

`T6-V1.md` 的原始公式分隔符已修复，并把上述证据等级明确写入。原
\(p=20\,065\,847\,377\) 数值线索已被精确反解：它不满足 actual root divisibility，且有
gap-3 Type II terminal，被 terminal-first 抢占，故已从 proper-root evidence 中删除。

## 6. 下一批可判真假的问题

1. 从 positive-\(q\) 已接入的首条 local edge 继续证明后续 Type-I totality。
2. 将 high-support dispatch 表限制在已知实际 state class，逐行产出 terminal、完整 E1--E5
   receipt 或唯一的 `MINIMAL_SELECTOR_GAP`。
3. 对 \(k>1\)，证明某个 \(q\mid k\) 的 provenance/physicalization，或从 \(D_*\) 构造
   合法 terminal / E1--E5 successor；仅构造 \((p,R_k,K_k)\) 不够。
4. 对每个 actual c=8 parent，证明 high-\(q\) double-low label 或其它 verified outgoing edge
   存在；有限 controls 中没有 dead end 不能替代该量词。

## 7. 参考入口

- [T6 证明工作包复核与合并记录](T6-proof-workfiles-package-audit-2026-08-18.md)
- [T6 全闭合尝试审计](T6-closure-attempt-audit-2026-08-17.md)
- [T2/T5 合并复核](T2-T5-full-integration-review-2026-08-17.md)
- [旗舰证明纲领](../concepts/flagship-proof-program-2026-08-16.md)
- [状态合同](../concepts/denominator-escape-state-contract.md)
- [初始 \(q=1\) 根 terminal-or-edge 分派](../claims/type-II-initial-q-one-root-terminal-or-full-carrier-dispatch.md)
- [T5 全局良基合同](../concepts/t5-global-well-foundedness-contract-v2.md)
- [q=1 G full-carrier phase-root claim](../claims/type-II-q-one-full-carrier-phase-root-entry.md)
- [positive-q G full-carrier phase-root claim](../claims/type-II-positive-q-G-full-carrier-phase-root-entry.md)
- [当前 named graph 的 T2/T3 coverage audit](T6-actual-reachable-coverage-audit-2026-08-17.md)
- [proper-root 最小缺口审计](T6-proper-root-minimal-gap-audit-2026-08-17.md)
- [proper-root k=1 全称排除](../claims/type-I-root-capacity-stutter-k-one-universal-exclusion.md)
- [proper-root \(k=3\) primitive fiber reduction](../claims/type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md)
- [proper-root \(k=3\) Vieta companion obstruction](../claims/type-I-root-capacity-stutter-k-three-vieta-companion-obstruction.md)
- [proper-root \(m=3\) 双二次范数约化](../claims/type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction.md)
- [proper-root 公共因子对齐](../claims/type-I-root-capacity-stutter-common-divisor-alignment.md)
- [proper-root primitive quotient 正规化](../claims/type-I-root-capacity-stutter-primitive-quotient-normalization.md)
- [proper-root stutter 的 Eisenstein 支撑](../claims/type-I-root-capacity-stutter-eisenstein-support.md)
