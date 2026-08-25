# Erdős–Straus 猜想研究知识库

本目录按时间顺序整理 Erdős–Straus 猜想的直接研究文献、关键技术依赖、
可核查数学主张和计算复现。`研究进展综述.md` 是阅读入口；`papers/`、
`claims/`、`concepts/` 中的 Markdown/YAML 文件是知识库的事实源。

当前文献快照审计至 2026-07-31；当前证明前沿和本轮旗舰命题核验至 2026-08-25。论文卡、
主张卡、概念卡及各状态的实时数量以 `python scripts/kb.py status` 和自动生成的
`index/theorem-ledger.md` 为准，不在入口文档手工复制。其中被撤回论文和存在关键证明
缺口的预印本仍会收录，但用独立状态标出。

## 当前旗舰命题（合同内核核验至 2026-08-20）

对核心素数 \(p\equiv1\pmod{24}\)，最终目标是下列双出口命题：

\[
\mathrm{F0}(p):\qquad
\mathrm{Type\ II}(p)\ \lor\ \mathrm{Type\ I\text{-}even\text{-}terminal}(p).
\]

第二出口采用已核验的 normal form：存在
\(m\equiv3\pmod4\)、\(3\le m\le p-2\)、\(x=(p+m)/4\) 及正整数 \(e,E\)，使

\[
e\mid x^2,\quad e\equiv-4^{-1}\pmod m,\quad
R=\frac{4e+1}{m},\quad K=xR-e,
\]
\[
E\mid4K^2,\quad E\equiv1\pmod R,\quad 2\mid E,\quad E\le4K-2R.
\]

这里 \(4^{-1}\) 在模 \(m\) 下取逆元。该 normal form 的代数等价性已经建立；对每个
核心素数选择 Type II 或该 Type I 证书仍是开放问题。后续主线维护下列六条可判真假的
旗舰命题：

| ID | 状态 | 核心断言 |
|---|---|---|
| T1v1 H4 clean-q closure | `CLOSED_RELATIVE` | 对 actual proper-overlap、top-capacity、\(a_{\rm alt}=1\) receipt，已验证 upstream provenance 与 priority miss 后，clean \(q\)-macro 给出书面 guard 下的 phase-local terminal 或 E1--E5 candidate；其它 H4 branch 由 T6-F2 接管。 |
| T2v1 Atomic-Admission | `CLOSED_PHASE_LOCAL` | 冻结 H4 `a=1` actual arm 与 c=8 double-low conditional arm 的有限 receipt grammar；不声称所有 c=8 parent、所有 raw path 或未来 atomic constructor 已覆盖。 |
| T3v1 Mark Invariant | `CLOSED_CURRENT_GRAPH` | initializer 与当前 15 个 registered edge generators 均不产生 nontrivial mark，故冻结具名图中该 family 不可达；新增 marked constructor 会自动重开义务。 |
| T4v1 Fresh-G-Handoff | `CLOSED_RELATIVE` | ordinary \(q\ge1\) G endpoint 在书面 guard 下进入 target-independent full-carrier fresh root 并完成首条严格 segment；post-handoff Type I totality 仍属 T6-F2。 |
| T5v1 Well-Founded Admission | `CLOSED_CONTRACT_LEVEL` | 所有合同认可的 `verified_edge` 都携带固定 ticket，并严格降低 \(\mathbb N^7\) 势；不推出每个非终端状态都存在 edge。 |
| T6 Global-Selector | `OPEN` | 确定性 selector 在每个核心 prime / actual reachable legal state 输出 terminal 或一条可提升、严格下降的 verified edge。 |

这些编号现在指向冻结的 pre-T6 合同内核。历史强版本 `T1*--T3*` 不再与已闭合的
v1 命题共用状态：未覆盖的 H4、raw atomic 和 future mark 量词分别由 T6 的 family-totality、
reachable-state exhaustion 与 constructor admission firewall 接管。精确迁移和 closed-world
证明见 [`docs/pre-T6-contract-kernel-closure-2026-08-20.md`](docs/pre-T6-contract-kernel-closure-2026-08-20.md)，
机器事实源见 [`data/pre-t6-contract-kernel-v1.json`](data/pre-t6-contract-kernel-v1.json)。

六条命题的历史推导、证据和反证标准仍见
[`concepts/flagship-proof-program-2026-08-16.md`](concepts/flagship-proof-program-2026-08-16.md)。
T1v1 与 T4v1 都只是限定输入域的相对闭包；T2v1 是有限 grammar；T3v1 是冻结图不变量；
T5v1 只提供 edge-admission 良基性。它们都不提供 selector totality。T4 的独立冻结证明包复核见
[`docs/q1-fresh-handoff-proof-package-audit-2026-08-17.md`](docs/q1-fresh-handoff-proof-package-audit-2026-08-17.md)；
T2/T5 的本次合并边界见
[`docs/T2-T5-full-integration-review-2026-08-17.md`](docs/T2-T5-full-integration-review-2026-08-17.md)。
当前 named graph 的 T2/T3 reachability 边界见
[`docs/T6-actual-reachable-coverage-audit-2026-08-17.md`](docs/T6-actual-reachable-coverage-audit-2026-08-17.md)。
本轮 T6 全闭合尝试、新增子定理与仍缺量词见
[`docs/T6-closure-attempt-audit-2026-08-17.md`](docs/T6-closure-attempt-audit-2026-08-17.md)。

### T6 近期进展截面与证明边界（2026-08-20）

T6 仍为 `OPEN`。已闭合的完整局部 selector 项是每个核心素数的规范初始状态 serializer：
取 \(q=1\)、\(m=3\)、\(X=(p+3)/4\)，若 \(X\) 有 \(2\pmod3\) 的素因子则给出
直接 Type II terminal；否则得到 ordinary G receipt，并进入既有 full-carrier
Type I handoff。该分派只闭合初始根，不声称 handoff 后的 Type I 路径 total。

本次还机械闭合了冻结 transition surface 的 inventory、当前图 nontrivial-mark unreachability
以及 future atomic/marked constructor 的 admission firewall。后者把原 O4 从一个悬空流程
缺口改为“未补 T2/T3、serializer、lift 和 T6 owner 就拒绝合并”的可执行规则；它只对冻结
v1 有效，新增构造器时自动重开。

本轮进一步收缩了 proper-root \(m=3\)、\(q=5\) rank-stutter 子分支。对其中的实际
raw occurrence，现有确定性策略至多消费两个因子即可到达 p-free primitive node；full-capacity
支若非 terminal 则只剩 single-side bundle。重算 canonical complete-excess support 后，
新的重复 \(a=1\) hard branch 被压缩为


\[
L_\omega\equiv1\pmod{p^2}.
\]

这消除了 p-block 作为必要 raw-policy 分支，也将 companion 的未分类算术压缩为规范
complete-excess 重算；但尚未提供连续的 E1--E4 receipt 或全称 QC1/TR1 exit。因此它不是
T6、O2 或全局 selector 的闭合结论。

### 最新证明包复查、归档与边界（2026-08-21）

`T6-F1-REACHABLE-STATE-EXHAUSTION` 的候选闭合包已完整解压、逐项复查并归档。复查结果
没有新增已闭合定理：包中把 `legal persistent selector state` 预先定义为 normalizer 已成功
给出 owner 的状态，又据此推出所有状态有 owner；同时它把 producer 穷尽限制为预设的 15 条
registry edge，未从当前全部 constructor 独立导出。因此 F1 仍是 `OPEN`，T6 的全局 selector
状态不变。

本次可保留的实质性进展是把 F1 的证明门收紧为可执行的四步：先独立定义 persistent queue、
header extractor 和拒绝路径；再枚举每个实际 constructor 的 guard partition；随后证明每个
nonterminal E3 target 至少命中一个 family predicate；最后才用 target re-entry 与 trace induction
把该覆盖提升到全部可达状态。包中的 O1 分解、future-constructor 重开规则和“已知命中时的
first-match 唯一性”被保留为这条路线的设计约束，而不冒充 F1 closure。

原始证据包与完整解压源码分别在
[`archive/proof-packages/raw/`](archive/proof-packages/raw/) 和
[`docs/archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/`](docs/archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/)；
逐引理裁定见
[`docs/F1-reachable-state-exhaustion-package-review-2026-08-20.md`](docs/F1-reachable-state-exhaustion-package-review-2026-08-20.md)，
规范 frontier 见
[`docs/T6-proof-boundary-2026-08-20.md`](docs/T6-proof-boundary-2026-08-20.md)。

本轮已将所有七份近期证明包统一展开并归档，逐包的完整性结果、数学处置和 payload 索引见
[`docs/proof-package-consolidation-2026-08-21.md`](docs/proof-package-consolidation-2026-08-21.md)。
新 M-H 包只带来两个受限结果：低支撑 marked F/G 的 complete-excess 构造已给出 E1 source
algebra、E2、root-wide E4 与 `LOCAL_DROP`，但没有全称 E3 owner/re-entry，故仍是条件性
adapter；高支撑结论只建立 `C=1` 同协议局部最小元，并未关闭一般 `C>1` 空改善分支。因而
F1、F2、F3、T6 与猜想本身的状态均不提升。

精确的冻结 family/edge 清单、立即闭合项和五个剩余 frontier theorem 见
[`data/t6-proof-frontier-v2.json`](data/t6-proof-frontier-v2.json) 与
[`docs/T6-proof-boundary-2026-08-20.md`](docs/T6-proof-boundary-2026-08-20.md)。原始 acceptance-gate
账本仍保留在 [`data/t6-selector-obligation-ledger-v1.json`](data/t6-selector-obligation-ledger-v1.json)；
v2 不删除其中任何数学 gap，只把 O4 流程义务改造成 admission firewall，并把其余八项唯一
映射到 F1--F3。该 p-free policy 及其 \(p^2\) canonical gate 的完整推导见
[`claims/type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction.md`](claims/type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction.md)
和 [`docs/T6-current-progress-2026-08-17.md`](docs/T6-current-progress-2026-08-17.md)。

### Wave1 高端点边界（2026-08-25）

F3 high-stutter 的两条 actual divisor gate 现已作出更强的负向澄清：固定
\((p,h,D)\) 后，`D | K` 仅将 root parameter \(\omega\) 限制在一个 CRT
同余类，且该类给出无穷多个保持两 gate 的形式 root lift。进一步的显式子列连 canonical
maximal-receipt divisor \(D\) 与 root-bottom terminal miss 也一并保持。因此不能再把
附加的同类 divisor-gate 算术或“\(D\) 已 canonical”当作 high Pell 或 odd-\(k\)
残余的 family-empty 证明。真正需要的是已证明对该子列非重复的**完整** valuation predicate、
完整 terminal-first schedule 或 actual source/path/admission 限制；F3、T6 与猜想的状态均不改变。精确命题与控制见
[`type-I-t6-f3-high-endpoint-root-lift-saturation-boundary`](claims/type-I-t6-f3-high-endpoint-root-lift-saturation-boundary.md)。

同日，F2 high-support \(C=1\) 的 `R=3 G` hard core 也得到一个更精确的算术分割：
\(P=p+4\) 与 \(N=(3p+1)/4\) 互素，并满足
\(\left(\frac{33}{N}\right)=\left(\frac P{11}\right)\)；当 \(P\) 合成时，其最小
素因子还确定一张完整的 mixed-residue gap screen。控制 \(p=118801\) 表明这两项仍可
共同 miss，因此它们没有改变 F2/T6 的开放状态。见
[`type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition`](claims/type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition.md)。

q1 full-carrier 的首段也完成了一项协议层澄清：两条 parity child 在其 target-local
terminal miss 后都应以 `TYPEI/ABSORB` 而非旧的 `CHARGED/LOCAL_DROP` 记入，且都有
canonical cursor \((1,R-1,1)\) 与 N7 `PHASE_DROP`。这只闭合 pre-admission 的
E3/type 层；actual runtime producer、terminal schedule 与 ABSORB re-entry 仍开放。见
[`type-II-q-one-full-carrier-first-child-absorb-entry`](claims/type-II-q-one-full-carrier-first-child-absorb-entry.md)。

进一步地，首 child 不应在进入第二-anchor macro 前持久化，否则会造成同 rank 的
`ABSORB -> CHARGED` 回升。现有 parity quotient-fold 可改为直接从 full-carrier root
到 final target 的 checkpoint contraction：high final target 由 root 的 support rank 支付
`LOCAL_DROP`，low final target 则以 `PHASE_DROP` 进入 ABSORB。该收缩尚缺 terminal
receipt、T2/admission 处置和 final re-entry，因而没有改变 T6 状态。见
[`type-II-q-one-full-carrier-root-second-anchor-contraction`](claims/type-II-q-one-full-carrier-root-second-anchor-contraction.md)。

该收缩现已在 shared runtime 的局部 slice 中实际执行：`q=1` initializer 会先返回
gap-3 terminal 或 content-addressed G state，随后依次经过 full-carrier handoff 与
checkpoint contraction，并以 common state classifier 入队 final target。odd low-final 的
\(p\equiv265\pmod {336}\) 子类（包括 \(p=601\)）现由 gap-7 terminal 在入口预占；
\(p=73\) 覆盖一般 overflow/`LOCAL_DROP`，\(p=1033\) 覆盖第三-anchor 的 C=9
overflow/`LOCAL_DROP`。两者的 final state 都被显式验证为 `DEAD_END`，所以这只是可重放的 producer slice，
并不宣称 post-G re-entry 已经解决。见
[`type-II-q-one-full-carrier-runtime-slice`](claims/type-II-q-one-full-carrier-runtime-slice.md)。

对 \(p\equiv25\pmod {336}\) 的 C=9 high target，进一步的确定性 r-side dual 会落到
\(R=23,35,11\) 三张固定低图表（依 \(k\bmod3\) 而定），并有 `PHASE_DROP` 到
ABSORB 的预准入 ticket。这让后续研究可以直接复用固定-R terminal/descent families；其
全域 re-entry 尚未建立。见
[`type-II-q-one-c9-high-r-side-dual-small-chart`](claims/type-II-q-one-c9-high-r-side-dual-small-chart.md)。

### Wave1 复核边界（2026-08-25）

本轮独立复核没有新增 F2、F3 或 T6 闭合，但修正了四个会影响后续证明方向的边界。

1. QC1 中的 \(q_\perp\mid N(a-b\omega)\) 和有向 Eisenstein ideal 因子并不定位一个
   可消费的 raw complete-excess side。现有 nonactual 控制甚至满足 \(q_\perp\mid N\)，
   但 \(q_\perp\nmid R-h,D,E,K\)。因此下一条 QC1 定理必须建立 path-bound side occurrence
   与 one-use charge conservation，不能再从 norm/ideal data 直接跳到 E1。
2. TR1 的 R6 \(k=3\) 子叶不能跳过 root-capacity menu。primitive reduction 强制
   \(u=h/3>1\)，所以所有 \(1<Q\mid u\) 的 menu 必须先按固定顺序重放；之后才可讨论
   \(D_*\)。同时，\(D_*\) 的最小算术因子可能已 capacity-saturated，未来 physical rule
   只能选取已独立验证为 fresh raw occurrence 的最小因子。
3. m=3,q=5 的 strict endpoint 在 \(L_\omega\equiv-1\pmod p\) 时精确落入
   high-support \(C=1\) target，并有条件性的 `LOCAL_DROP`；它只是转交 F2 的 R=3-G
   hard core，不提供 re-entry。
4. q1 C=9 source 的 \(L=2M\) fixed-\(n\) target 确有严格 `LOCAL_DROP`，但它不是现有
   generic selector 的 canonical output，且 target 当前无 dispatch。因此只保留为
   source-specific local candidate，不计入 Gate 3 或任何 residual closure。
   其精确量词和 non-admission 边界见
   [`docs/T6_F2_F3_WAVE1_C9_FIXED_N_CANDIDATE.md`](docs/T6_F2_F3_WAVE1_C9_FIXED_N_CANDIDATE.md)。

Freeze B 已包含精确的 `type_i_absorb_marked_residual` **type-space** owner。所有旧的
“没有 ordinary ABSORB owner”表述均应理解为“没有已注册 producer、shared serializer、common
admission 或 re-entry”；type-space owner 本身不支付 E3。H4 的 `C=1` source-gate 排除同样
只覆盖 retained `H4_A1` actual clean-q atomic arm，不覆盖其它 H4/future producer 或全局
high-support `C=1` trace。机器可读 frontier 见
[`data/t6-wave1/t6-f2-f3-residual-frontier-v1.json`](data/t6-wave1/t6-f2-f3-residual-frontier-v1.json)，
TR1 修正见 [`docs/handoffs/F3_TR1_HANDOFF.md`](docs/handoffs/F3_TR1_HANDOFF.md)。

### Wave2 严格缩减（2026-08-25）

第二轮没有使 F2/F3 通过 Gate 3，但删除了若干此前仍可能被误当作出口的完整候选分支。

- q1 C=9 的 R=23 行在 \(p\equiv1033\pmod{11088}\) 上有直接固定尾 Type I
  terminal：
  \[
  4/p=1/(K/22)+1/K+1/(pK),\qquad K=(23p+1)/4.
  \]
  这只覆盖该终端子射线，剩余 R=23/35/11 行仍开放。见
  [q1 C9 R23 fixed-tail terminal ray](claims/type-II-q-one-c9-r23-fixed-tail-terminal-ray.md)。
- c=8 的 actual \(q_\star=103\) source 在 complete terminal-first miss 的前提下
  被压到两条 \(34608\) 模射线；但现有 \(p=157393\) local control 自身有未被 local
  slice 检查的 p-level terminal，因而不能当作 actual MISS。完整 parent trace 与 shared
  admission 仍缺失。
- high-support C=1 的 canonical R=3 anchor continuation 必由 ABSORB 升回 CHARGED，
  且相对原 high parent 增大 charged outer coordinate，故不是 T5 可接纳的 re-entry。
  C>1 的 \(A\mapsto A\,\operatorname{spf}(C)\) 同样既不是 fixed-\(n\) 除子边，
  也不是同图表 full-excess 边。见
  [C1 R3 anchor no-reentry](claims/type-I-f2-high-support-c1-r-three-anchor-no-reentry.md)
  和
  [C>1 SPF saturation provenance barrier](claims/type-I-f2-high-support-cgt1-spf-saturation-provenance-barrier.md)。
- QC1 现在在 \(q_\perp\mid E\) 子域有 canonical endpoint-excess raw deflation 与严格
  arithmetic rank target；仍需 verified persistent source path、common admission 和
  re-entry。真正 two-sided \(p^2\) canonical target 则只是根参数增大的 rechart，不能
  作为 paid macro。见
  [QC1 endpoint-excess deflation](claims/type-I-t6-f3-qc1-endpoint-excess-deflation.md)
  和
  [m3 q5 p2 canonical rechart boundary](claims/type-I-t6-f3-m3-q5-p2-canonical-rechart-boundary.md)。
- F3 high-stutter 的 refined lift 还保持每个只依赖
  \(\Theta=(p,h,u,D)\) 的 terminal predicate，包括 \(Q\mid u\) external menu 与
  fixed-\(D_*\) fan。因而这种谓词不能打破 root-lift 周期；真正的 high terminal
  机制必须使用变化的 \(R,K,z,Q,\beta,E\) 数据，或建立新的 high-source bridge。

因此下一步的真实瓶颈仍是：把仍存的 terminal MISS 绑定到 actual source path，经过同一
Gate-3 producer/admission surface，并为每个 admitted target 提供非上升 re-entry。任何
只增加局部同余、因子或 checkpoint 的结果都不会改变 F1/F2/F3/T6 的开放状态。

### 第三轮证明复核（2026-08-25）

本轮没有新增 active producer，也没有改变 `F1=OPEN`、`F2=OPEN`、`F3=OPEN` 或
`T6=OPEN`。其价值是把若干潜在误桥精确排除，并修复 shared type space 的一个语义错误：
`is_overflow` 现在严格表示 \(R>p\) 的 chart 几何，而 `C8_PARENT`、`PROPER_ROOT` 保留为
来源谱系；proper-root header 还必须从 \((p,r)\) 重算完整 \((A,K,R)\) 图表。该修复不产生
C8 relay、fresh scope、E1 或 re-entry。

- F2 high-support \(C=1\) 的 R=3 hard core 中，universal raw source 的非 \(p\) 首 label
  完全由 \(2p-3\) 的因子给出。hard-core control \(p=2521\) 有 \(2p-3=5039\) 为素数，
  所以不存在“必有 non-anchor 首边”的全称证明；当前 full-excess formal route 仍只会回到
  已拒绝的 anchor loop。
- F2 \(C>1\) 的当前 full-excess external rechart 一律仍是 CHARGED overflow；在
  empty-improvement 叶它既不能转为 ABSORB，也不能支付 `LOCAL_DROP`。
- F3 high default tree 的第三个 canonical full-product fold 不能抵达 canonical high root；
  single-side/atomic complete-excess 仍开放，且需要实际 source path。
- F3 QC1 的 first atomic rank-stutter 有 deterministic 第二 raw deflation；TR1 的
  \(D_*\) 因子则精确分为 fresh \((D_*,E)>1\) 与 capacity-saturated 两类。两项均仍缺
  source-bound transcript、child terminal priority、E3 与 re-entry。

下一份必须完成的材料不是新的裸同余筛，而是
[`f3_proper_root_endpoint_path_receipt_v1`](data/interface-requests/f3-proper-root-endpoint-path-receipt-v1.json)：
它要把 admitted parent、immutable source scope、完整 root chart、ordered raw word 与每个
prefix 的 terminal-first receipt 绑定到同一 target。详见
[`docs/T6_F2_F3_THIRD_WAVE_PROOF_REVIEW_2026-08-25.md`](docs/T6_F2_F3_THIRD_WAVE_PROOF_REVIEW_2026-08-25.md)。

### 第四轮数学收缩（2026-08-25）

后续推导进一步缩小了三条剩余路线，但仍没有新增 selector edge。

- F2 R=3 hard core 中，\(D=2p-3\) 不能整体充当新的 Type II AC defining factor：唯一
  两个整数可能分别被 gap-7 terminal 和 \(p+4\) hard-core 条件排除。剩余 Type II 机制
  必须是 \(q\mid D\) 的 mixed cofactor completion，同时满足两条显式同余；固定 Type I
  模板也满足 \(m\mid D\iff m\mid2A+3B\)。
- canonical q=1 root 的 direct single-side/atomic landing 已有完整 lcm/maximality 与 E5
  门。大 root prime-power sector 为空，但 \(p=73\) 的静态 atomic countercontrol 表明
  不能用 carrier bound 把整个 smooth sector 删除。
- TR1 dyadic-fresh \(2\mid(D_*,E)\) 强制精确 2-adic 正规形；R6 的 full-capacity
  \(W_y\)-word 已排除 atomic-companion bad residue，child 算术输出缩为 terminal 或
  one-sided macro，仍缺 source-bound transcript、canonical rank 与 admission。

这三条结论及下一步的 proof order 见
[`docs/T6_F2_F3_FOURTH_WAVE_BOUNDARIES_2026-08-25.md`](docs/T6_F2_F3_FOURTH_WAVE_BOUNDARIES_2026-08-25.md)。

### Gate 审计更新（2026-08-25）

当前共享 runtime 的唯一 queue mutation 已被 source audit 精确识别，但它只覆盖两条 q=1
局部 route，terminal schedule 也不是完整 p-level oracle；因此 F1 仍有 4 个真正 unknown
（另有 9 个信号已明确归类为 nonruntime controls），
不能把该 runtime MISS 当 C8/H4/F3 的 complete terminal-first receipt。F2 high-support
同时补入 canonical/noncanonical 分流：仅 \(1\le K/A<p\) 可调用现有 C=1/C>1
determinant-dual 定理，\(K/A\ge p+1\) 是独立的 E1/E3-open normalizer residual。QC1
endpoint-excess deflation 也获得独立 target-shape request，不能复用 norm-ideal target。
F2 R=3 hard-core 的 \(D\)-contact 现已精确分为 prime-\(D\) 空子叶与 composite-D
参数化残余；R6 dyadic companion 的 full-capacity bad-residue gate 也已排除，但最终
canonical rank 与 admission 仍开放。详见 [T6 F2/F3 Gate Audit](docs/T6_F2_F3_GATE_AUDIT_2026-08-25.md)。

对固定核心素数 \(p\)，R=3 composite-\(D\) 的 AC normal form 现在有一个有限除子表
scheduler：逐项重算 \(K,m,B\)，顺序或互素性失败归为 FAMILY_EMPTY，
\(1<\gcd(h,2p-3)<h\) 的项直接给出 Type-II TERMINAL。该结果只关闭固定-p 的
arithmetic coverage；actual source/E1、terminal-first 全局调度和 runtime admission
仍是 F2 残差。见
[type-I-f2-r-three-d-fixed-prime-arithmetic-scheduler](claims/type-I-f2-r-three-d-fixed-prime-arithmetic-scheduler.md)。

本轮随后又补上两条可复用的算术边界：

- \(R=3\) composite-\(D\) 有显式 mixed-D terminal ray
  \(p=769+1320t\)（素数点由固定商系统重构 Type-II 证书），同时有
  \(p=505+1272t\) 的 \(q=53\) partial-contact ray；后者的 \(h/q=59\) cofactor
  只在 \(t\equiv56\pmod{59}\) 时通过，\(p=1777\) 给出 hard-core
  `COFACTOR_EMPTY` 控制。partial congruence 不再被当作 terminal 证书。
- F2-05a 的 noncanonical high-support 若已有
  \(M=Ab,\ K=M(p-d)\) source-bound determinant receipt，则 \(b\ge2\)，应先走
  same-chart canonical target \(C_T=p-d<p\)；当前可执行 q=1 runtime 也只产生
  \(A=1\) 或 \(C<p\)。这只收缩到未注册/未 admission 的语义 producer，不关闭全局 F2。

对应证明卡见
[`type-I-f2-r-three-d-composite-terminal-ray`](claims/type-I-f2-r-three-d-composite-terminal-ray.md)、
[`type-I-f2-r-three-d-partial-contact-cofactor-obstruction-family`](claims/type-I-f2-r-three-d-partial-contact-cofactor-obstruction-family.md)
和
[`type-I-f2-high-support-noncanonical-registered-surface-boundary`](claims/type-I-f2-high-support-noncanonical-registered-surface-boundary.md)。

最新独立复核进一步固定了三条边界：C8 \(q_\star=103\) 射线只反驳 Bradford
列出的有限同余表，不能反驳完整的 factor-dependent fixed-gap cover；
F3 high/QC1 的高 \(k=1\) Pell 叶新增精确整除门但仍缺 actual source；
\(m=3,q=5\) genuine two-sided \(p^2\) canonical image 只有 \(c=p-1\) 的增大
root rechart，不能支付 E5。F1 admission 目前为 18/18 source anchors、
9 个 nonrecursive controls、4 个真正 unknown；任何 arithmetic scheduler 仍须
经过共同 source/projector/validator/admission/re-entry 链。TR1 还明确排除了两类
优先级更高的 \(D_*\) 直接 Type-I/Type-II terminal 子域，必须在 freshness 选择前执行。
详见
docs/handoffs/F3_HIGH_QC1_INDEPENDENT_REVIEW_2026-08-25.md、
docs/handoffs/AGENT7_F3_M3_Q5_P2_WAVE2_TWO_SIDED.md 和 C8 handoff 三件套。

## 快速使用

```bash
python scripts/kb.py validate
python scripts/kb.py build
python scripts/kb.py search "half dimensional sieve"
python scripts/kb.py status
python reproductions/pre_t6_contract_kernel_audit.py --root .
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
```

`build` 生成：

- `index/timeline.md`：按首次公开日期排列的完整文献时间线；
- `index/citation-graph.mmd`：论文引用图；
- `index/theorem-ledger.md`：从主张卡自动生成的数学状态、证明来源与审阅状态账本；
- `index/catalog.json`：供其他工具消费的结构化目录；
- `index/kb.sqlite`：带 FTS5 全文检索的 SQLite 数据库。

主张卡用三个互不替代的字段记录证据状态：`claim_status` 表示数学结论状态；
可选的 `proof_provenance` 表示证明或证据来自原始文献、仓库推导、计算复现或混合来源；
可选的 `review_status` 表示卡片中的论证是否经过仓库内、独立或外部复核。旧卡缺少后两个
字段仍然有效，构建时统一显示为 `unspecified`，不会从 `claim_status` 自动推断。允许值见
`schemas/document-types.yaml`；新卡从 `templates/claim-note.md` 创建并应主动填写。

`proof_provenance` 的语义为：`external_primary_source` 指精确陈述和证明锚定到所列原始
来源，`repository_derivation` 指证明写在本仓库，`computational_reproduction` 指证据来自
可复现程序和产物，`mixed` 指结论实质依赖多类证据，`not_applicable` 用于未声称已有证明
的开放问题等，`unspecified` 表示尚未完成分类。`review_status` 中，`unreviewed` 表示没有
记录第二轮复核，`internal_review` 表示完成仓库内复核，`independent_review` 表示存在独立
证明或独立实现的复核，`external_review` 表示存在仓库外审阅记录；后三者应在卡片正文给出
可核查锚点，`unspecified` 只表示尚未分类。

研究方法、已确立结论和逐点证明缺口的历史导航见
[`concepts/research-directions-and-proof-gap.md`](concepts/research-directions-and-proof-gap.md)；
当前证明前沿、下一阶段目标及其依赖顺序见
[`concepts/current-frontier-2026-07-29.md`](concepts/current-frontier-2026-07-29.md)。

常用检索过滤器：

```bash
python scripts/kb.py search "parametrization" --type paper --year-from 2010
python scripts/kb.py search "计算验证" --type claim --tag computation
```

公开副本由 `python scripts/kb.py publish` 生成到 `public/`。该命令不会复制
内部工作日志、原始来源文件或标记为 `visibility: internal` 的文档；发布前还会扫描
内部检索标记和本机路径。公开版包含候选文献清单、BibTeX 和小尺度复现材料。

## 增量研究流程

1. 把新发现写入 `bibliography/candidates.yaml`，先作纳入、归并或排除判断。
2. 对纳入论文建立 `papers/<citation_key>.md`，分别记录出版状态与数学核查状态。
3. 将可复用结论拆成 `claims/`，将术语和方法拆成 `concepts/`。
4. 运行 `validate`、测试、`build` 和 `publish`；检索日期与未取得原文的缺口写入
   `bibliography/search-log.md`。

有限复现入口为 `python reproductions/esc_reproduce.py`。它核对经典恒等式、模
840 残余类、因子对证书和 Bradford 的 Type I/II 除子对应，不是对已报告
`10^17` 或 `10^18` 搜索的全量复现。

`python reproductions/short_certificate.py` 另行按 \(m=4x-p\) 搜索 Type I/II
的最小首分母缺口，用于检验“短证书或递降”研究计划中的候选短界；它同样是
有限实验。

## 证据纪律

- 同行评议状态与数学核查状态分别记录。
- 每个实质性主张必须指向原始论文及页码、定理号或公式号。
- 预印本、计算报告、启发式和存在关键缺口的证明声称不能混写。
- 未取得原文时明确标记，不以二手摘要冒充精读。
- “文献全集”是带截止日期的可审计语料，不声称永久穷尽。

本知识库使用 AI 辅助进行检索、格式化、代码实现和初步数学核查。最终数学
结论以链接的原始文献为准，争议性结论保留明确的核查状态与限制说明。
