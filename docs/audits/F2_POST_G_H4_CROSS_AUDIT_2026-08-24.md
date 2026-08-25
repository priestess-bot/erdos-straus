# F2 post-G/H4 独立交叉复核

审查对象：`sol/f2-post-g-h4-totality` 的不可变提交
`3e69b4d55163d06fa7479b1744ad756fa29d211a`，含 preliminary scope commit
`84ad06eb05bf1d95eb10cced1346cd352db00fe7`。

审查者分支：`sol/f2-c8-atomic-closure`。本复核没有调用
`f2_post_g_*.py` 作为证明证据；只读取命题、机器回执、冻结 graph 和既有 upstream
claims，并独立重建关键代数与量词边界。

## 1. 结论

```text
POST_G_LOW_CHART_SUPPORT_DOUBLING = SOUND_RELATIVE_TO_COMMON_ADMISSION
C2_NON19_IN_Q1_IMMEDIATE_IMAGE = FAMILY_EMPTY
H4_ARITHMETIC_PARTITION = SOUND_UNDER_STATED_ACTUAL_H3_H4_GUARDS
H4_TARGET_OVERFLOW_OWNER_SHAPE = SOUND
POSITIVE_Q_G_PRUNING = ONLY_FROZEN_GRAPH_CONDITIONAL
FINAL_E3_AND_REENTRY = OPEN
H4_CAPACITY_ONE = POSSIBLE_NOT_CLOSED
TRACK_STATUS = OPEN_MAJOR_INTEGRATION_BLOCKERS
```

未发现能够直接推翻 low-chart、C2 rigidity 或 H4 residue 分派代数的反例。发现一个
coordinator-facing interface 矛盾、两个 closure-blocking 量词问题，以及两个应在整合前收紧的
边界。

## 2. Findings

### CRITICAL-1：positive-q G 的“无 source”不能在 F1 闭合前升级为实际量词

位置：

- `claims/f2-post-g-ordinary-g-producer-pruning-v1.md:57`
- `data/interface-requests/f2-post-g-g-producer-disposition-v1.json:18`
- `data/interface-requests/f2-post-g-h4-target-shapes-resolution-v1.json:27`
- `data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json:37`

冻结 frontier 的结构归纳本身成立：initializer 只给 q=1 G/terminal，当前两个 relation
target producer 都要求 F source，且当前图没有 F seed。因此在**冻结 selected graph** 中
positive-q G 不可达，c=3 alternate 也可被 q=1 full-carrier-first precedence 支配。

但当前活动 constructor audit 明确为：

```text
closure_ready = false
unresolved source signals = 9
concrete queue mutation API = absent
```

所以 frozen registry 还不是 actual reachable constructor 的闭世界。若 coordinator 现在按
interface request 撤销 `positive_q_g_full_carrier_phase_root` 的 queue right，一个尚未被 F1
盘点出的 positive-q seed 会失去已存在的相对 handoff。

处理要求：在 Gate 3 之前只保留
`ESTABLISHED_FOR_FROZEN_SELECTED_GRAPH`。F1 若证明无新 Type-II seed，才可 prune；否则必须
把 positive-q relative theorem 编译成 common-admitted producer。提交本身已在 minimal
residual 中承认该条件，所以这是**阻断整合**，不是指控该相对命题为假。

### CRITICAL-2：final E3/common admission/re-entry 尚未建立，不能激活 fused producer

位置：

- `claims/f2-post-g-c2-fused-h4-macro-reduction-v1.md:153`
- `data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json:48`
- `data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json:94`

parent-to-final 的 E5 组合是正确方向：persistent parent 的 CHARGED capacity 为
`p-1`，所有 live H4 final capacities 至多 `p-2`，不能比较内部 H0--H4 的局部涨落。
E4 的 `Sol(p)` identity 也不预设未知解。

然而 snapshot 没有对最终 non-atomic target 构造 `PersistentSelectorStateV1`，没有 sealed
producer/source receipt，没有运行 common queue gate，也没有 replay recursive owner。atomic
目标在该 snapshot 中也仅是外部依赖。故 `q_one_d_one_c2_19_h4_fused_exit_v1` 现在只能是
proposal，不能登记 `VERIFIED_SUCCESSOR`。

Agent 3 的后续 commits `916e349`、`14e1217`、`7183983` 已为 actual admitted H4_A1
atomic output 提供同步非持久 serializer、full-`K_T` fiber replay 和 existing overflow owner
重入；coordinator 仍须把 source-specific H4 producer rule 与该接口连接。non-atomic final
target 仍需独立接 common gate。

### MAJOR-1：fused producer target-owner request 与同提交的 queue discipline 矛盾

位置：

- `data/interface-requests/f2-post-g-c2-fused-macro-v1.json:11`
- `data/interface-requests/f2-post-g-h4-target-shapes-resolution-v1.json:57`

前一文件仍把以下对象列入 producer `target_owners`：

```text
t2_v1_atomic_pending_target
direct_terminal_leaf
```

但后一 resolution 明确规定：

```text
AtomicPendingTargetV1 = synchronous nonpersistent, queue forbidden, no owner
direct terminal = queue external
```

这不是单纯措辞差异。如果 target set 被编译成 `ProducerRuleV1`，pending target 会重新成为
持久 owner，而 terminal 根本不可能通过 persistent family classifier。

处理要求：从 persistent `target_owners` 删除这两项。atomic 分支应只在 normalization 后声明
`type_i_a_gt_one_overflow_residual` / 有真实 sink receipt 时的
`type_i_high_support_sink`；terminal 应作为 queue-external disposition。若还保留
`h4_non_v1_branch_or_descendant`，必须说明它是哪一种最终非 atomic state，而不是 H4 内部
checkpoint。

### MAJOR-2：H4 final capacity-one 仍可能发生，不能继承 immediate-image C1 空结论

位置：

- `claims/f2-post-g-h4-target-high-support-owner-v1.md:62`
- `data/t6-wave1/f2-post-g-h4-target-owner-v1.json:8`
- `data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json:73`
- `data/interface-requests/f2-post-g-h4-target-shapes-resolution-v1.json:78`

`type-II-q-one-full-carrier-d-one-capacity-one-exclusion` 的量词只覆盖 q=1 immediate d=1
receiver 的**第一 canonical complete-excess target**。它正确给出该 immediate image 的
`C>=2`，但不能传播到经过 H0--H4 后的新 multiplier。

H4 clean-q final formula 为

\[
c_q\equiv-qE_x^{-1}\pmod p,
\]

所以

\[
\boxed{c_q=1\iff E_x\equiv-q\pmod p.}
\]

现有 source-D closure 排除的是 stutter 类 `E_x=q (mod p)`，没有排除负号类。写

\[
p=2dq-1,
\qquad
\delta_d=2d(4d^2-2d+1),
\]

同一 source identity 给出 C1 的必要门

\[
D\equiv-\delta_d\pmod p,
\qquad
D\mid(2d-1)((2d+1)q-1),
\qquad
0<D<2dp,
\]

外加 actual 31-phase 条件 `d | abs(1536-a(p))`、parent/path、payload、priority 和
admission。纯算术负残数门并非自动矛盾，例如
`(d,q,p,D)=(23,47,2161,4140)`、`(35,71,4969,9660)`；这两行**不是** actual
H4 witness，只说明不可从当前正号 stutter theorem 推出 C1 空。

处理要求：给 Agent 2 的 handoff 明列
`H4_C1=POSSIBLE_NOT_CLOSED`。若实际 H4 C1 被 admission，它落入既有 A>1/high-support
owner，但 `TYPEI/CHARGED` local rank 已是 `(0,1,0,0)`，必须由 terminal、lower
protocol/phase 或 family-empty 退出。当前 minimal residual 的 Agent-2 量词包含所有 A>1
targets，因此逻辑上尚未漏掉它；interface 文本仍应显式区分 immediate C1-empty 与 H4
C1-open，避免下游错误收缩量词。

### MAJOR-3：clean-q live branch 还写成 single-side/atomic，未使用已有 single-side 空定理

位置：

- `claims/f2-post-g-h4-arithmetic-totality-reduction-v1.md:187`
- `data/t6-wave1/f2-post-g-h4-arithmetic-reduction-v1.json` 的
  `H4-R4-MOD-1-PROPER-TOP-A-1-CLEAN-Q`

该 claim 使用 y-block nonempty、p-primary exclusion 和 stutter closure，得到
`Q_x=1<Q_y` 或 `Q_x,Q_y>1`。但仓库已有更晚的 established theorem
`type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion`，它在相同 actual
high-H4 scope 中证明 `Q_x>1`。因此所有 nonterminal clean-q endpoints 实际只剩 atomic
split。

当前写法不是假命题，但它人为保留一个 non-atomic serializer residual，并使 fused producer
target set 更宽。处理要求：加入 single-side-exclusion dependency，将 live branch 收紧为
`terminal | H4_A1 atomic final target`。这也使 Agent 3 的 common atomic serializer 精确覆盖
该叶。

### MAJOR-4：全称 closure 仍依赖 Agent 2 的 overflow descendant totality

位置：

- `claims/f2-post-g-h4-target-high-support-owner-v1.md:136`
- `data/t6-wave1/f2-post-g-h4-minimal-residual-v1.json:73`

H4 final target 的 owner-shape 证明成立：`M_T>M_4>B_p`，`c_T>=1` 且
`R_T=3 mod 4` 可推出 `R_T>p`；F/G 只是 certificate context。没有 sink receipt 时会命中
`type_i_a_gt_one_overflow_residual`，有真实 sink receipt 时可命中更窄 high-support owner。

但 owner 命中只证明 re-entry shape，不证明下一步存在。Agent 2 未关闭 A>1/high-support
terminal-or-successor totality前，H4 F/G descendants 的全量词仍开着。snapshot 对此表述准确；
coordinator 不得把“无需新 H4-F/G family”误读成“F/G descendant 已关闭”。

### MINOR-1：preliminary proposal 与 resolution 同时保留，机器消费者必须认 supersession

`data/interface-requests/f2-post-g-h4-target-shapes-v1.json` 仍把 atomic pending 描述成既有
persistent family match；新 resolution 才将其改为同步、非持久。建议 coordinator 只消费
resolution，或在 preliminary artifact 增加 machine-readable `superseded_by`，避免简单聚合器
同时读到相反请求。

### MINOR-2：snapshot 的 `git diff --check` 有两处 Markdown 行尾空格

`docs/f2-post-g-h4-wave1-handoff-2026-08-24.md:3` 和 `:4` 使用 Markdown hard-break 空格，
会使仓库 merge gate 的 `git diff --check` 失败。改为普通换行或显式 HTML break。

## 3. 独立正向核验

### 3.1 Frozen G graph

直接读取 `data/t6-proof-frontier-v2.json` 得：initializer target 为 q=1 G/terminal；唯一能
产生 relation F/G target 的两个 edge 均要求 F source。故 Agent 1 的 frozen-graph induction
成立。独立 constructor audit 的 `closure_ready=false` 同时证明该结论尚不能升级为语义闭世界。

### 3.2 Low-chart support doubling

对 `3<=R<=p-2`，

\[
K=(pR+1)/4\le(p-1)^2/4=B_p,
\qquad A\le K.
\]

universal p-source 是 primitive，因为 `p` 不整除 `RK(R-1)`。若 `R-1|K`，anchor
`(1,R-1)` 直接给 centered Type-I terminal。否则 maximal block `Q>1` 且 `Q|R-1<p`，
故 p-free；`M=lcm(A,Q)>=2A`。只要 target 仍 low，就有 `M<=B_p`，所以 support 至少
翻倍的内部链必在有限步内 terminal 或越入 `R>p,A>1`。E5 应比较 initial/final 或每个
已 admission endpoint；common admission 尚是外部义务。

### 3.3 C2 non-19

upstream rigidity theorem 的量词正是 q=1 immediate d=1 receiver，并给
`c=2 iff even,g=1,j=8,q_star=19,p=912u+769`；因此该 image 中 C2 non-19 确实为空。
capacity-one exclusion 也只在这个 immediate image 上成立，不能外推到 H4 final target。

### 3.4 H4 guard partition and E5

在写明的 actual H3=>H4 guards 下，`R4 mod p` 的 `0/1/other` 三分穷尽；`R4=1`
内部的 full/proper overlap、top/nontop、`a=1/a>1` 和 clean carrier 都有对应 upstream
claim。所有 live final capacities 至多 `p-2`，而 persistent parent capacity 是 `p-1`，
所以 parent-to-final CHARGED rank 严降；没有使用内部 checkpoint 的局部涨落收费。

### 3.5 Target owner

`M_T>M_4>p^4/8>B_p` 且 `c_T>=1` 给
`R_T=(4M_Tc_T-1)/p>p`。因此 target 是 A>1 high-support overflow；F/G 重分类不改变
owner facts。此 shape 结论与 Agent 3 的 atomic normalization 一致。

## 4. Gate verdict

| Gate | Verdict |
|---|---|
| D1 exact quantifier | PARTIAL：written scope 完整，但 positive-q actualness 依赖 F1 freeze |
| D2 exhaustive partition | PASS_ARITHMETIC_CONDITIONAL；semantic constructor totality 未过 |
| D3 E1 | PASS_RELATIVE_TO_STATED_ACTUAL_RECEIPTS |
| D4 E2 | PASS |
| D5 E3 | FAIL_OPEN：producer projection/common admission 未安装 |
| D6 E4 | PASS：`Sol(p)` identity |
| D7 E5 | PASS_RELATIVE：parent-to-final N7，非 checkpoint-local |
| D8 re-entry | FAIL_OPEN：atomic需整合 Agent 3，non-atomic和downstream overflow仍开 |
| D9 negative controls | PARTIAL：shared runtime negatives 尚未绑定本 producer |
| D10 independent replay/review | PASS_WITH_MAJOR_FINDINGS（本文件） |

最终建议：`3e69b4d` 可作为数学 reduction input 合并，但不能作为 F2 closure receipt。先修
MAJOR-1/2/3，等待 F1 grammar freeze、common producer admission 与 Agent 2 overflow totality；
之后再评估 `GAP-O1-POST-G-TYPE-I` 和 `GAP-O1-H4-OTHER-BRANCHES` 是否可清零。

## 5. Re-review: `849ad0f`

作者在 follow-up `849ad0fac17dbed063df0f353ae60037128eb438` 中逐项修正了本审查的
integration findings。只读复核确认：

1. positive-q disposition 已明确延后到 F1 grammar freeze；若出现 seed，必须激活现有 relative
   handoff，而不是静默删除 producer；
2. fused producer request 已移除 `t2_v1_atomic_pending_target` 与 terminal 作为 persistent
   target owner；AtomicPending 被标为 synchronous/nonpersistent；
3. H4 final C1 现在明确为 `POSSIBLE_NOT_CLOSED`，并交给 Agent 2 的 high-support owner；
4. live clean-q endpoint 已引用 established single-side exclusion，收紧为 atomic-only；
5. preliminary target-shape request 带 `superseded_by`，机器消费者可确定采用 resolution。

因此上文的 MAJOR-1/2/3 作为 snapshot `3e69b4d` 的 findings 已修复。仍保持开放的
`R-EXT-F1-GRAMMAR-FREEZE`、common admission、atomic serializer integration 与 Agent 2
overflow totality 是正确的研究边界，不应被解释成 Agent 1 的局部代数错误。
