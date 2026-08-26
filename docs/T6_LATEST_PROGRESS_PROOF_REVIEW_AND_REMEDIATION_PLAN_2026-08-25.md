# T6 最新进展深入复查、证明验证与整治推进规划

> 仓库：`priestess-bot/erdos-straus`  
> 复查日期：2026-08-25  
> 当前 `main` 审计锚点：`232b186485f077bda044610938bf115d2911ef7a`  
> 目标：恢复可信验证基线，关闭 F1 的活动准入缺口，并以可审计、可并行的方式推进 F2/F3 至零 residual，为 F4 selector assembly 提供冻结边集。  
> 状态纪律：本文不宣称 F1、F2、F3、T6 或 Erdős–Straus 猜想已经关闭。

---

## 2026-08-26 执行附记

Gate 0 与 Gate 1 已在 `main` 的精确提交
`4dc68b462bd55ae337692b8a6007c41bb898a940` 上完成。GitHub Actions run
`32901203777` 的 Gate 0 与 live snapshot job 均成功；Gate 0 manifest 记录
1372 项测试、恰好 13 项冻结的可选大文件 skip，以及 9/9 命令通过。该 HEAD 的 live
snapshot 为 `VERIFIED_HEAD`，但 `current_digest_audit=MISSING` 且
`status_upgrade_allowed=false`，所以没有数学状态升级。

Phase 2 目前只完成零权限基础：HEAD-bound evidence inventory、五个空 role
subregistry、零 COMPLETE schedule 的 production terminal registry、不可签发的 complete
terminal miss 类型边界，以及 reserved typed fields 的 acyclic V2 bundle。它们没有授权
producer、validator、projector、terminal scheduler 或 T5 ticket，也没有接入活动 queue。
现有 runtime 仍接受 legacy E1--E4 boolean validation，完整 terminal replay 与独立
validator authority 仍缺失。因此下文 Gate 2 的验收项一项也不能勾选，F1/F2/F3/T6
状态保持开放。本附记记录 8 月 26 日执行结果，不改写下文 8 月 25 日历史审计判断。

随后增加的 V2 zero-authority runtime 已把 production-facing migration 入口收紧为
0 initializer、0 successor route 和不可变空 queue；旧 V1/raw/bool/terminal-miss 输入在该
入口均不能获得权限。独立 q=1 phase-root 数学 replay 也已从原始整数重推 G 判据、唯一
full-carrier chart、fresh source、Sol(p) 恒等 lift 和 T5 phase drop。两项仍是
evidence-only：前者没有正向 route，后者没有 complete terminal、common E3 owner 或
validator role grant，所以 Gate 2 验收状态不变。

远程 `main` 的阶段提交 `61399a35c4473b7dcf1c3ea93a33939dc07a8faa` 已由 GitHub
Actions run `32918731224` 在精确 HEAD 上验证：1480 项测试通过，仍只有 13 项冻结的
可选大文件 skip；Gate 0 与 live snapshot job 均成功。其后本地继续建立 terminal scope
taxonomy 和 q=1 gaps 3/7/11 完整 divisor-prefix evidence。这里必须区分：prefix miss 只
覆盖 coordinator 将来可能注册的有限优先前缀；全自然缺口 miss 在语义验证后会报告根反例，
永远不能成为 producer continuation。当前两类都无 issuer/E1/queue authority，Gate 4
仍未验收。

下一层已把两个必要接口分开建立：coordinator registry v2 只授权固定 prefix scheduler 和
独立 coverage verifier 的 exact-HEAD 代码身份，并以 tracked blob/AST/closure/semantic pins
阻止代码静默继承权限；其 issuer、initializer、E1、queue、producer、T5 权限仍全为 0。
同时，q=1 root source 已改用无环 envelope：initializer anchor 先于 state ID 生成，terminal
decision 只能作为后置 sidecar，不能进入 state identity。两者尚未由 issuer 串接，因此仍是
Gate 4 的前置闭合，不是 production terminal receipt。

在此之上，exact-HEAD non-authorizing decision assembler 已完成 root state -> derived domain ->
scheduler -> independent coverage -> HIT/MISS sidecar 的实际纵向执行。为排除 stale import，它
不调用预加载依赖，而从 requested HEAD blobs fresh compile/exec 四个 dependency；命中与 miss
controls 均通过。输出仍将 source actualness、initializer/issuer/terminal/E1/queue 权限固定为
false，所以这一步关闭的是装配与哈希依赖，不是 issuer 或 Gate 4。

随后完成的 registry v3 与 production issuer/replayer 又闭合了一层更窄的 authority 子门。
V3 对 parentless ordinary q=1 G root 分离授予 initializer、issuer、scheduler、coverage verifier
四个角色，并把 assembler 与 post-issuance replayer 保持为 non-role dependencies。所有 artifact
除 blob/symbol/closure/semantic pin 外，还逐 dependency 传递 semantic pins；三个 exact-HEAD
loader 的 helper、caller、path constants 和调用表也由固定 AST contract 约束。该结论只针对
当前冻结 bytes/policy；显式改写 resolver/loader contract/pins 是新的 authority policy，不能自动
继承本轮证明。

production issuer 现可将 `p=73,193,241441` 的已验证前缀 HIT 签发为 root-terminal receipt，
并将 `p=1201,2521` 签发为 scope-bound registered-prefix MISS。独立 replayer 从同一 HEAD 与 raw
q=1 G input 重建 actualness、assembler decision 和最终 wire；它明确拒绝 local serializer 可接受
的 coherent body/anchor/state 换链重封。两种 receipt 都固定 common owner、E1、queue、producer
continuation 为 false，MISS 还固定 global exhaustion 为 false。因此本轮没有完成完整 Gate 4，
也没有满足 Gate 2/3/5 或全局 goal checklist；下一步是为 production prefix MISS 建立 common
owner 与 scope-aware E1 consumer，而不是把它误写成 `MISS_COMPLETE`。

上述“下一步”现已由 active coordinator registry v4 在严格局部范围内完成。V4 只增加
`COMMON_ROOT_OWNER_CLASSIFIER`、`INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR` 和
`REGISTERED_PREFIX_E1_CONSUMER` 三个 exact-HEAD 角色；orchestrator 与 post-issuance replayer
保持 non-role。对 `p=1201,2521`，同一 source 的 V3 prefix MISS 可生成确定性 full-carrier
phase-root `ROOT_SOURCE_SCOPED_E1`；对 `p=73,193,241441`，terminal HIT 必须在 E1 前退出。
common owner 的 normalized facts、15-family precedence 与 owner digest 已和冻结 V1 实现逐项
等价。三套聚焦测试共 32/32 通过，独立复核结论为 `ACCEPT`。

这没有完成下文 Gate 2：V4 receipt 明确令 generic/successor `e1_authority=false`，也没有
target owner、E2--E5、producer、admission、re-entry 或 queue 权限。新的最小推进目标因此改为：
只针对该唯一 q=1 phase-root candidate，构造由 source occurrence 绑定的 E2 projection、common
target owner/E3 normal form、identity E4 与 T5 phase-drop E5，最后经共享 admission path 形成
首条可独立重放的完整非终止边。全局 checklist 继续保持未勾选。

随后对对象层的三路独立复核表明，这个顺序还缺一个必须前置的 base gate。V4 source 是
`persistent_admission=false` 的 `RawRootSourceStateV2`；现有 V1 runtime 只允许已进入 admitted
set 的 V1 state 作为普通 successor source。E2/E3 的 target formulas/唯一 owner、E4 恒等 lift
和 E5 七元 phase drop 的全称数学核都可证明，但若直接从 V4 state 发 successor，运行时应以
`SOURCE_NOT_ADMITTED` 拒绝。

该 base gate 现由 V5 在严格条件下完成。active V5 registry 固定 12 个 artifact，只授予
`Q1_ROOT_V1_BASE_MATERIALIZER` 与
`INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER` 两个 role：`p=1201,2521` 在 V3
registered-prefix MISS 和独立 V4 owner/scope replay 后可得到 V1
`ROOT_INITIALIZER_OUTPUT` 的 base admission；`p=73,193,241441` 的 terminal HIT 在此之前
preempt。V1 state 的 semantic origin 排除所有 V4 E1/candidate 字段，V2-to-V1 owner digest 重新
锚定，canonical root potential 只作 evidence，绝不构成 T5 authority。receipt 的
`persistent_admission=true` 仍不是 enqueue 或 successor：queue/enqueue、producer、E1--E5、T5、
global、re-entry 均为 false。

这条 V5 claim 准确保持 `conditional` / `internal_review`。exact-HEAD pin、worktree drift、Git
replace 和 routing 控制已经复核，但仓库选定的 commit 本身尚需外部不可变或签名信任锚；同时
更换 registry/pin/role bytes 是新的 authority policy，不能自动继承该结论。因此下一步不再是
“物化 V1 source”，而是在满足 selected-commit trust condition 的 exact HEAD 上，把 V4
`ROOT_SOURCE_SCOPED_E1` 重新绑定到该 admitted V1 source ID；再按次序建立 target-bound
terminal scope、E2、target owner/E3、E4、E5 和 shared target admission。精确复核记录见
`docs/audits/T6_Q1_ROOT_V1_BASE_ADMISSION_CONDITIONAL_REVIEW_2026-08-27.md`；历史对象层数学
边界仍见 `docs/audits/T6_Q1_PHASE_ROOT_OBJECT_LAYER_AND_E2_E5_REVIEW_2026-08-26.md`。

---

## 0. 执行摘要

当前仓库已经完成了一轮高密度的 F1/F2/F3 合并，`main` 已吸收 F1 reachability contract、F2 post-G/H4、F2 overflow/high-support、F2 c8/atomic，以及 F3 high endpoint、TR1、QC1、proper-root physicalization 等分支。数学 residual 的确比 `c851bd2` 时显著收窄，且多项新增局部定理在其**明确声明的局部量词域**内可以独立复算通过。

但当前不能把“合并完成”解释为“证明链闭合”。最新状态存在五个高优先级问题：

1. **最新 `main` 的 GitHub Actions 为红色。** 当前失败发生在 verifier lint 步骤；因此最新合并基线尚无绿色 CI 证明。
2. **CI 覆盖范围落后于 wave1 代码面。** 现有 workflow 的路径过滤和执行步骤主要覆盖旧 pre-T6 内核，没有系统覆盖 `data/t6-wave1/**`、新 runtime、所有新 reproductions、完整测试发现、生成物一致性和当前 constructor audit。
3. **F1 仍只有局部 q=1 可执行切片。** 当前 runtime 有一个真实 queue mutation，也要求 common admission，但只注册两个 q=1 route，最终到 `DEAD_END`；四个 F1 unknown 仍在，不能承载全体 F2/F3 producer。
4. **proof-carrying runtime 的证据边界仍过弱。** `TransitionValidationV1` 以 `E1/E2/E3_pre_admission/E4: bool` 和自由形式 `evidence_ids` 表示证明，runtime 只检查布尔值为真、ID 非空以及 source/branch/projection digest 对齐。这不足以防止 track-local validator 自授权、伪造 actualness 或用未绑定内容的字符串充当证明。
5. **当前 residual frontier 明确报告零个活动 wave1 verified producer。** 现状仍是 F1=`OPEN_MINIMAL_GAPS`、F2=`OPEN`、F3=`OPEN_MINIMAL_GAPS`、T6=`OPEN`，并保留 4 个 F1 unknown、5 个 F2 residual group、10 个 F3 residual group。

因此最短可信路径不是继续横向堆积更多局部同余，而是先完成一次“验证基础设施整治”，再激活一个窄而完整的 producer 作为架构样板，随后并行关闭 F2/F3 residual。

本规划采用两波执行：

- **整治波 R**：恢复绿色 CI、建立实时 HEAD 审计快照、把 E1–E5 改造成结构化且内容绑定的 receipt、关闭 F1 四个 unknown、建立全域 terminal schedule 证明框架。
- **数学波 M**：在冻结 admission/receipt/terminal 接口后，以 7 个互斥量词域并行处理 F2/F3 residual。

最终接受条件不是“新增定理很多”，而是：

```text
F1 unknown = 0
F2 residual = 0
F3 residual = 0
active producer 的每条非终止边均有结构化 E1–E5 + re-entry
CI 在精确 HEAD 上全绿
独立 verifier 不复用被审计 producer 的结论
所有状态、ledger、frontier、README 与机器收据一致
```

---

## 1. 复查范围与证据等级

### 1.1 本次复查覆盖

本次复查重点检查了：

- `main` 的最新提交链和已合并分支；
- GitHub Actions 最新运行状态与 workflow 覆盖范围；
- `docs/T6_F2_F3_GATE_AUDIT_2026-08-25.md`；
- `data/t6-wave1/t6-f2-f3-residual-frontier-v1.json`；
- `data/t6-constructor-inventory-v1.json`；
- `data/t6-wave1/family-grammar-freeze-v1.json`；
- `data/t6-wave1/q1-full-carrier-runtime-slice-v1.json`；
- `scripts/t6_persistent_selector_runtime_v1.py`；
- F2 的 R=3 hard-core、mixed-D、high-support normalizer、q=1 root landing；
- F3 的 QC1 endpoint deflation、TR1 fresh split/dyadic、R6 companion、m=3,q=5 接口边界；
- 相关 cross-audit、handoff、machine receipt 和 residual 记录。

### 1.2 证据等级

本文对结论采用三种等级：

| 等级 | 含义 |
|---|---|
| `V-A` | 已独立做符号推导、精确整数复算或小规模穷举反控；不只依赖仓库自述 |
| `V-B` | 已逐行审查声明、实现与 receipt 的逻辑接口，但未在本地完整 checkout 上运行全套测试 |
| `V-C` | 依赖 GitHub 当前 commit、Actions、仓库生成物或自报测试结果 |

### 1.3 重要限制

本次环境尝试直接 clone 仓库时遭遇 DNS 解析失败，未能在本地容器执行当前 `main` 的完整测试套件。因此：

- 代数与整数恒等式可以独立复算的部分，按 `V-A` 报告；
- runtime、schema、receipt、workflow 的逻辑审查，按 `V-B` 报告；
- 当前 HEAD 的完整可执行性，必须以修复后的 GitHub Actions 或一份可复现的干净 checkout run manifest 重新确认。

这也是为什么“恢复精确 HEAD 上的绿色 CI”必须成为 Gate 0，而不是普通维护任务。

---

## 2. 当前最新基线

### 2.1 `main` 最新提交

当前 `main` 顶端为：

```text
232b186485f077bda044610938bf115d2911ef7a
Merge remote-tracking branch 'origin/sol/f3-qc1-quotient-only'
Date: 2026-08-25
```

同日已合并的主要分支包括：

```text
3b52a81  sol/f3-high-endpoint
aa478ed  sol/f3-h-supported-tr1
3e6e714  sol/f2-post-g-h4-totality
b0feb38  sol/f2-overflow-high-support-totality
e9c5934  sol/f2-c8-atomic-closure
eb2fd6f  sol-ultra/f3-proper-root-physicalization
da73e0d  codex/f1-reachability-contract
4e88f8e  integration/t6-f2-f3-wave1 -> mainline
```

此外，8 月 25 日之前的集成分支上已经连续加入 q=1 runtime slice、C9 收缩、F2/F3 hard-core residual 收窄、high-support 修正、proper-root provenance、terminal preemption 等提交。

### 2.2 当前 theorem status

以当前 residual frontier 和 gate audit 为准：

| 模块 | 当前状态 | 可接受解释 |
|---|---|---|
| F1 | `OPEN_MINIMAL_GAPS` | 局部 runtime/admission 架构存在，但未形成 all-constructor producer projection、全 queue/no-bypass、全 target re-entry |
| F2 | `OPEN` | 已有多个局部空性、终止、normalizer 或 macro；5 个 residual group 未闭合 |
| F3 | `OPEN_MINIMAL_GAPS` | proper-root 域已细分并显著收窄；10 个 residual group 未闭合 |
| T6 | `OPEN` | 尚无覆盖全部 reachable nonterminal states 的单一确定 selector |
| 猜想 | `OPEN` | 无全局证明闭合 |

当前机器计数为：

```text
F1 explicit unknown items                 = 4
F2 open residual groups                   = 5
F3 open residual groups                   = 10
active verified wave1 producers           = 0
active pending queue states allowed       = 0
conditional actual edges admitted         = 0
T5 ticket failures admitted               = 0
```

“零活动 producer”是当前最重要的治理信号之一：大量数学候选尚未被错误登记，这是好的；但也说明尚未完成从局部定理到活动递归边的物理化。

### 2.3 当前 CI 状态

最新 workflow run 对应 `232b186`，状态为 `Failure`，总时长约 25 秒。失败注释显示进程退出码为 1，当前可见失败阶段是：

```text
Lint the new verifier
```

同时 workflow 对 GitHub Actions 的旧 Node 运行时版本给出升级警告。

更严重的问题不是单次 lint，而是 workflow 覆盖面明显不足。当前 path filter 主要绑定旧的 pre-T6 文件；执行步骤只覆盖：

```text
kb validate
旧 T6 ledger replay
初始 q=1 root serializer replay
pre-T6 frozen-kernel audit
两个旧 verifier 文件的 ruff lint
```

它没有系统执行：

```text
kb build + 生成物无差异检查
完整 unittest discovery
wave1 residual/frontier 审计
constructor inventory audit
F1 runtime-specific tests
新 F2/F3 reproductions
新 transition/terminal/receipt mutation tests
所有修改 Python 的 py_compile
全仓或 T6 范围 ruff
正常的 git diff --check
HEAD-bound artifact manifest 验证
```

因此，即使现有 workflow 变绿，也不能单独证明 wave1 合并内容完整通过。

---

## 3. 当前工程与证明架构复查

### 3.1 已建立的正面基础

当前 `PersistentSelectorRuntimeV1` 已具备若干正确设计：

1. **存在单一真实 queue mutation**：`_enqueue_admitted_target_v1` 最终执行 `self._queue.append`。
2. **bootstrap 与 successor 路径都先经过 common admission**。
3. **producer 不能直接提供 owner、family、normal form、recursive eligibility 或 queue 权限字段**。
4. **dispatch registry 会校验 producer/branch 的精确匹配**。
5. **target 的 T5 potential 由 runtime 重新计算，而不是直接相信 producer**。
6. **T5 ticket 在 common admission 前被验证**。
7. **target owner 和 owner digest 由共同 classifier/admission 产生**。
8. **最终 transition receipt 包含 source、producer、branch、projection、owner、T5 ticket 等摘要字段**。

这些基础说明当前方向是正确的：活动边需要通过一个共同、fail-closed 的 runtime，而不是各 track 自行入队。

### 3.2 F1 的真实边界

当前 gate audit 明确说明：

- 唯一实例化 runtime 只注册两个 q=1 route；
- 该局部路径最终到 `DEAD_END`；
- local terminal schedule 不是完整的 p-level terminal oracle；
- 一个明确的 gap-11 terminal 示例不在局部 schedule 中；
- 仍有四个 genuine F1 unknown；
- 九个 source signal 被裁定为 nonruntime control，但未来若作为 producer 集成，必须重新打开。

四个 F1 unknown 可概括为：

| ID | 缺口 |
|---|---|
| `U-A0-01 RUNTIME` | 尚无全 constructor runtime/source completeness；只有 q=1 局部实例 |
| `U-A0-02 ENQUEUE` | 尚未证明所有 constructor 都只能通过该 queue mutation；no-bypass 未全局成立 |
| `U-A0-03 REENTRY` | classifier 存在，但未证明所有 target schema 都回到同一 runtime/classifier |
| `U-A0-08 E3` | 多数 overflow/track-local builder 仍使用局部描述，而非共享 persistent schema |

因此 F1 不能关闭，也不能发布最终 grammar freeze。

### 3.3 proof-carrying runtime 的关键薄弱点

当前 `TransitionValidationV1` 大致包含：

```python
source_state_id
producer_id
branch_id
projection_digest
E1: bool
E2: bool
E3_pre_admission: bool
E4: bool
evidence_ids: tuple[str, ...]
```

runtime 的 `_validate_transition_v1` 主要检查：

- validator 是否存在；
- 返回对象类型正确；
- source/producer/branch/projection digest 对齐；
- `E1/E2/E3_pre_admission/E4` 全部为真；
- evidence IDs 满足最低格式要求。

随后 runtime 自己验证 T5 ticket，再生成 transition receipt 并入队。

这仍然存在一个严重信任边界：**布尔值为真不等于证明内容已被绑定和重放。** 如果某 track 能注册自己的 validator、临时 ProducerRule、terminal schedule，或者仅通过修改 `evidence_class` 把 control 标成 `ACTUAL_PERSISTENT`，它就可能生成形式上通过的 receipt。

QC1 cross-audit 已经实际展示了这一类风险：在 composite-p control 上仅改变 evidence class，局部 harness 就能够报告 E1 complete、recursive eligible、common admission accepted；其原因不是数学定理突然成立，而是 source actualness、ProducerRule、terminal schedule 和 validator 权限没有被强制绑定到 coordinator-owned registry 与真实前序链。

这不是普通测试不足，而是证明对象模型需要升级。

### 3.4 历史基线与实时 frontier 混用

当前 `t6-f2-f3-residual-frontier-v1.json` 的 `baseline_sha` 仍指向历史 integration SHA，而 `main` 已前进到 `232b186`。`family-grammar-freeze-v1.json` 也保留历史 audited SHA 和协议提交。

保留历史 workpack 信息本身没有问题；问题在于同一文件同时被用作“当前状态”。必须拆分：

```text
workpack_origin_sha        历史起点，永久不变
integration_audited_sha    某次集成审计点
last_verified_head_sha     最近完整绿色验证的 HEAD
current_observed_head_sha  当前仓库 HEAD
```

若 `current_observed_head_sha != last_verified_head_sha`，状态必须显示 `UNVERIFIED_HEAD_ADVANCE`，禁止把旧 audit 继承到新 HEAD。

---

## 4. 数学证明独立验证结果

本节只验证声明在其局部量词域内是否自洽；不把局部定理自动升级为 F2/F3 totality。

### 4.1 F2：R=3 的 D-contact boundary

#### 4.1.1 核心不等式复算

仓库中的核心约束可整理为：

\[
4ACK-1\le 3K+2A.
\]

若 \(C\ge 2\)，左侧增长使该不等式与正整数参数约束冲突，因此只需考虑 \(C=1\)。此时：

\[
(4A-3)K\le 2A+1.
\]

对正整数 \(A,K\) 精确枚举可得候选：

\[
(A,C,K;h)
\in
\{(1,1,1;3),(1,1,2;7),(1,1,3;11),(2,1,1;7)\}.
\]

再施加 \(h\mid(3K+2A)\)，仅保留：

\[
(1,1,3;11),\qquad (2,1,1;7).
\]

该压缩是正确的。

#### 4.1.2 gap-7 terminal 恒等式

对 \(p=7B-2\)，独立符号检查确认：

\[
\frac4p
=
\frac1{2B}
+
\frac1{2p}
+
\frac1{pB}.
\]

因此 gap-7 分支确有直接终止模板。

#### 4.1.3 h=11 分支

仓库对 h=11 与 p+4 hard core 的冲突推导在声明条件内成立。结论应保持为：该特定 contact leaf 被排除，而不是整个 C=1 family 自动终止。

#### 4.1.4 验证结论

```text
等级：V-A
局部定理：通过
可升级内容：R=3 D-contact residual 被压缩为精确小分支
不可升级内容：F2 C=1 totality、全局 terminal schedule、E1/E3/re-entry
```

### 4.2 F2：mixed-D completion parameterization

独立检查确认下列关系一致：

\[
D+T=2hm,
\]

\[
T=4ACL-3h,
\]

\[
h(Km-A)=Kp+A,
\]

\[
D-hm=4AC(B-A)-(m+3).
\]

仓库给出的三个正控制也满足相应 quotient/gcd/order 约束：

```text
p=769,   A=1, B=14, C=14, K=1, m=15, g=5,  D=1535,  h=55
p=21937, ...                                      g=19, D=43871, h=95
p=20809, ...                                      g=35, D=41615, h=175
```

在扩展的精确整数枚举中，未发现违反当前 local claim 的 core counterexample；小的非正/退化例外与仓库排除条件一致。

prime-D stratum 的空性结论在给定量词下成立；但 composite-D 仍有实际正控制，因此只得到一个 terminal-search reduction，而不是全称 terminal theorem。

```text
等级：V-A
局部参数化：通过
prime-D empty：通过
composite-D totality：未建立
```

### 4.3 F2：high-support canonical normalizer

对控制：

\[
(p,R,K;A)=(73,5551,101306;1369),
\]

独立复算得到：

\[
C=K/A=74=1+73\cdot1,
\]

因此 canonical residue \(c=1\)、\(t=1\)。normalizer 给出：

\[
R^\circ=75,
\qquad
K^\circ=1369,
\]

并满足：

\[
73R^\circ+1=4K^\circ,
\qquad
73<R^\circ<4A.
\]

这验证了：

- canonical/noncanonical 分割是必要的；
- 非 canonical branch 的 E2/E4 算术和局部 E5 可以成立；
- 不能把任意 \(C\ge p\) 直接送入 determinant-dual C=1/C>1 定理。

但该控制中的 post-hoc determinant identity 不能作为 actual E1 source receipt。

```text
等级：V-A
normalizer 算术：通过
E1 actualness：未建立
E3/re-entry：未建立
```

### 4.4 q=1 canonical root direct landing

对 \(p=73\) 的控制，独立复算确认：

```text
A* = 590150 = 638 × 925
c  = 24
K  = 15312
R  = 839
```

并满足：

\[
4ac=pR+1,
\]

\[
\operatorname{lcm}(638,25,37)=590150,
\]

\[
\gcd(25,814)=1,
\qquad
814=37\cdot22,
\qquad
22\mid K.
\]

因此 root-landing 的局部 lcm/valuation 和 low-support filter 是可信的。它仍然缺少一条 actual fresh source path、完整 terminal priority、common admission 和 re-entry。

```text
等级：V-A
算术 landing kernel：通过
活动 producer：未建立
```

### 4.5 F3：QC1 endpoint-excess deflation

#### 4.5.1 valuation 复算

对源端点中 \(q\)-进赋值，仓库的两种情况是自洽的：

- 若 \(b\ge k+2\)，endpoint excess 的 \(q\)-指数下降 1；
- 若 \(b=k+1\)，则移除 \(q^{r+1}\) block；
- 对应 target multiplier 形如 \(AE/q^\mu\)。

仓库使用的 residue exclusion：

\[
q^{r+1}\not\equiv1\pmod p
\]

在其前提下推导成立。

#### 4.5.2 不能升级为活动 QC1

QC1 当前有两个不能混用的 target shape：

```text
norm-ideal proposal          Aq_perp, residue <-q_perp^{-1}>
endpoint-excess deflation    AE/q_perp^mu, residue <-q_perp^mu>
```

ideal factor 不是 raw integer occurrence。endpoint-excess deflation 只有在真实 source-bound \(q_\perp\mid E\) occurrence 存在时才有 E1。

cross-audit 的伪造试验进一步证明：当前 harness 允许通过改变 evidence class 和 track-local registration 得到形式上的 admission，因此不能接纳 QC1 closure。

```text
等级：局部算术 V-A；runtime/receipt V-B
valuation theorem：通过
QC1 physical producer：拒绝升级
主要 blocker：E1、coordinator-owned registry、typed projector、E4/re-entry
```

### 4.6 F3：TR1 fresh split 与 dyadic boundary

独立逐素数检查显示，fresh split 的 primewise exponent 公式与 product reconstruction 一致。

2-adic child 边界中，若：

\[
E=2^{\lambda+1},
\qquad
E\equiv1\pmod p,
\]

结合当前量词约束推出 \(p=3\) 的排除逻辑是成立的。

R4 中 `m=3` 导致 D 为奇数，从而 dyadic-fresh subleaf 为空，也与当前 gate audit 一致。

发现一处非数学性格式问题：某 claim 中一行 TeX 的 `\quad` 缺反斜杠，应修复以免生成物和审阅工具误读。

```text
等级：V-A / V-B
局部算术：通过
actual transcript、E3、universal lift、re-entry：未建立
```

### 4.7 F3：R6 dyadic companion exclusion

仓库对 companion residue 的分类按：

```text
mu = 1
mu = lambda + 1
J = 1
J = 3
J >= 5
```

进行。独立复算确认，在输入假设下：

\[
p\mid H+2^{\mu+1}L
\]

及相应大小约束可排除 full-capacity \(W_y=(h+1)/2\) 的坏 residue。于是 arithmetic endpoint 被压到 p-free、terminal-or-single-side。

该结论仍不提供：

- source-bound prefix replay；
- canonical final rank；
- common admission；
- recursive re-entry。

```text
等级：V-A
局部 exclusion：通过
TR1 persistent transition：未建立
```

### 4.8 m=3,q=5 与 p² gate

本次没有发现足以推翻现有局部正规形的代数错误；但当前 source-bound macro 接受任意 state ID/scope 作为 digest 输入，这不构成 admitted-source proof。

现有主要边界仍是：

- R1 endpoint path 未绑定到活动 source；
- R2 serializer 未形成；
- nonminimal q=5、regeneration p-free failure 未关闭；
- one-sided 与 genuine two-sided \(p^2\) leaf 未被 EMPTY、TERMINAL 或 paid successor 关闭；
- second-child 的固定 T5 E5 未完成。

继续推出更高阶同余，若不能直接关闭上述某一 leaf，不应计作 closure progress。

### 4.9 总体数学审查结论

| 方向 | 局部数学 | 活动 E1 | E3 | 固定 T5 | re-entry | 总体裁定 |
|---|---:|---:|---:|---:|---:|---|
| F2 R=3 D-contact | 通过 | 不适用/局部 | 缺 | 局部 | 缺 | 保留 established-local |
| F2 mixed-D | 通过 | 缺 | 缺 | 未全域 | 缺 | prime-D empty；composite open |
| high-support normalizer | 通过 | 缺 | 缺 | 局部通过 | 缺 | arithmetic-only |
| q=1 root landing | 通过 | 缺 | 缺 | 局部通过 | 缺 | candidate kernel |
| QC1 deflation | 通过 | 缺/可伪造 | 缺 | 未形成完整边 | 缺 | closure rejected |
| TR1 split/dyadic | 通过 | 缺 | 缺 | 未形成完整边 | 缺 | arithmetic-only |
| R6 companion | 通过 | 缺 | 缺 | 未形成完整边 | 缺 | local exclusion |
| m3q5 p² | 未发现局部反例 | 缺 | 缺 | 关键 leaf 缺 | 缺 | open |

最重要的判断是：**当前主要瓶颈不是这些局部代数普遍错误，而是它们没有被连接成 actual source → terminal-first → deterministic target → common admission → fixed T5 → re-entry 的连续链。**

---

## 5. 根因分类

### 5.1 证明对象层

当前很多 track 的“证明”仍以布尔值、字符串 ID、自由 payload 或 track-local registry 表达，缺乏以下内容绑定：

```text
source state hash
parent transition hash
actual occurrence coordinates
terminal schedule hash
claim version/hash
reproduction program hash
independent verifier hash
projector hash
grammar hash
producer registry hash
T5 taxonomy hash
```

因此，验证器知道“某人声称 E1=True”，但不知道该 E1 是否确实是这个 source、这条 occurrence、这个 branch、这版 claim 的独立重放结果。

### 5.2 actualness 层

高频错误模式包括：

- divisor existence 替代 raw integer occurrence；
- post-hoc identity 替代 source receipt；
- fixture/control 通过字符串字段升级为 actual；
- 从 prime 重构 parent，而不是消费前序 serialized state；
- track-local ProducerRule 自行授予 dispatch 权限。

### 5.3 terminal-first 层

local terminal schedule 的 `MISS` 只能说明“局部列出的模板未命中”，不能说明“全局所有优先终止都未命中”。任何 F2/F3 producer 若依赖 local MISS，都不能获得完整 E1/E3 权限。

### 5.4 E3/re-entry 层

target shape 设计已经出现多个不兼容版本，典型如 QC1 norm-ideal 与 endpoint-excess。没有统一 projector/owner/normal form 时，family label 不能替代 E3。

### 5.5 T5 层

局部参数下降、checkpoint drop、selected-coordinate nonrepeat、phase-local capacity inequality，均不自动等于固定 \(\mathbb N^7\) potential 的 parent-to-final strict descent。

### 5.6 治理层

- 当前 HEAD 无绿色 CI；
- historical baseline 和 live HEAD 未分离；
- workflow 未覆盖新代码面；
- theorem ledger 中大量 `established` 仍是 internal/local provenance，不能当作独立审查完成；
- 合并成功没有被严格阻断于状态更新之前。

---

## 6. 整治总原则

1. **先恢复验证可信度，再激活更多边。**
2. **历史 workpack 不重写；新增 live audit snapshot。**
3. **E1–E5 必须是结构化 receipt，而不是布尔声明。**
4. **producer、validator、terminal scheduler 的注册权归 coordinator。**
5. **所有 actual source 必须来自已验证 predecessor chain 或 root initializer。**
6. **local terminal MISS 不得获得全局 terminal-first 权限。**
7. **先用一个窄 producer 完成端到端架构证明，再批量接入。**
8. **每个 residual 只能以 `FAMILY_EMPTY`、`TERMINAL` 或 `VERIFIED_SUCCESSOR` 关闭。**
9. **有限搜索只能做反控和范围探索，不能代替全称证明。**
10. **状态升级由独立审计结果驱动，不由 commit 数量、claim 数量或合并数量驱动。**

---

## 7. 分阶段整治 Gate

## Gate 0 — 恢复精确 HEAD 上的绿色 CI

### 目标

使 `main` 当前精确 SHA 在一套覆盖 wave1 全部活动面向的 workflow 上通过，并输出可审计 run manifest。

### 必做任务

1. 修复当前 ruff 失败；不得通过删除 lint 步骤规避。
2. 更新 workflow 使用的 GitHub Actions 主版本，消除 Node 20 deprecated warning。
3. 扩大 path filter，至少覆盖：

```text
README.md
claims/**
concepts/**
data/t6-wave1/**
data/interface-requests/**
data/t6-constructor-inventory-v1.json
docs/T6_*.md
docs/handoffs/**
scripts/kb.py
scripts/t6_*.py
reproductions/**
tests/**
.github/workflows/**
```

4. workflow 至少执行：

```bash
python scripts/kb.py validate
python scripts/kb.py build
git diff --exit-code -- index/

python reproductions/pre_t6_contract_kernel_audit.py \
  --root . --require-full-tree
python scripts/audit_t6_constructor_inventory_v1.py

python -m unittest discover -s tests -p 'test_*.py' -v

ruff check scripts reproductions tests
python -m compileall -q scripts reproductions tests

git diff --check
```

5. 生成：

```text
data/t6-wave1/ci-run-manifest-v1.json
```

字段至少包括：

```json
{
  "head_sha": "...",
  "workflow_run_id": "...",
  "python_version": "...",
  "kb_claim_set_digest": "...",
  "runtime_source_digest": "...",
  "producer_registry_digest": "...",
  "grammar_hash": "...",
  "test_manifest_digest": "...",
  "commands": [],
  "results": [],
  "status": "PASS"
}
```

### 验收标准

- 当前精确 HEAD workflow 全绿；
- `kb build` 后无未提交生成物；
- full test discovery 通过；
- constructor audit 通过；
- run manifest 的 `head_sha == git rev-parse HEAD`；
- manifest 中所有摘要由 CI 在 checkout 后计算，不能由提交者手写。

### 阻断规则

Gate 0 未通过时：

```text
禁止 theorem status 升级
禁止声明 integration baseline verified
允许修复性和审计性提交
允许继续研究局部数学，但不得注册活动 producer
```

---

## Gate 1 — 建立 live audit snapshot v2

### 目标

把历史起点、某次集成审计点和当前验证 HEAD 完全分离。

### 新文件

```text
data/t6-wave1/t6-live-audit-snapshot-v2.json
```

### 建议 schema

```json
{
  "schema_id": "t6_live_audit_snapshot_v2",
  "observed_at": "2026-08-25T...Z",
  "workpack_origin_sha": "...",
  "integration_audited_sha": "...",
  "current_observed_head_sha": "...",
  "last_verified_head_sha": "...",
  "head_relation": "EQUAL|ADVANCED_UNVERIFIED|DIVERGED",
  "claim_set_digest": "...",
  "runtime_source_digest": "...",
  "producer_registry_digest": "...",
  "terminal_schedule_digest": "...",
  "grammar_hash": "...",
  "t5_taxonomy_digest": "...",
  "test_manifest_digest": "...",
  "independent_review_digest": "...",
  "status": {
    "F1": "...",
    "F2": "...",
    "F3": "...",
    "T6": "..."
  }
}
```

### 规则

- v1 residual/frontier 文件作为历史输入保留；
- v2 snapshot 才代表“当前已验证状态”；
- 任意摘要变化均使 `last_verified_head_sha` 失效，直到 full audit 重跑；
- README/ledger/frontier 状态只可引用 v2 verified snapshot。

### 验收标准

- historical baseline 不再冒充 current HEAD；
- CI 自动验证所有 digest；
- `ADVANCED_UNVERIFIED` 会让状态升级任务失败；
- snapshot 与 README、ledger、residual frontier 一致。

---

## Gate 2 — 将 E1–E5 升级为结构化、内容绑定的 receipts

### 目标

消除“布尔真值即证明”的信任漏洞。

### 2.1 新 receipt 类型

建议建立：

```text
E1OccurrenceReceiptV1
E2ProjectionReceiptV1
E3TypingReceiptV1
E4LiftReceiptV1
E5TicketReceiptV1
VerifiedTransitionBundleV1
```

### 2.2 E1 receipt 最小字段

```json
{
  "receipt_type": "E1OccurrenceReceiptV1",
  "source_state_id": "...",
  "source_state_digest": "...",
  "parent_transition_id": "...|ROOT_INITIALIZER",
  "producer_id": "...",
  "branch_id": "...",
  "scope": "...",
  "occurrence_path": [],
  "occurrence_value": "...",
  "provenance_digest": "...",
  "source_terminal_schedule_digest": "...",
  "source_terminal_result": "MISS_COMPLETE",
  "claim_id": "...",
  "claim_digest": "...",
  "reproduction_id": "...",
  "reproduction_digest": "...",
  "independent_verifier_id": "...",
  "independent_verifier_digest": "..."
}
```

E1 必须证明：

- source 是 root initializer 或已验证 predecessor 的 target；
- occurrence 在 source serialized payload 中有可重放路径；
- source 未被完整 terminal schedule 抢先终止；
- scope 与 claim 量词一致。

### 2.3 E2 receipt

必须绑定：

```text
source digest
candidate witness digest
projector version/hash
tie-break rule
canonical target payload
target projection digest
```

禁止只提供 family label 或自由 payload。

### 2.4 E3 receipt

必须绑定：

```text
target schema version
normal-form verifier hash
family predicate results
precedence table hash
owner
owner digest
grammar hash
admission gate version
```

### 2.5 E4 receipt

不能只写 `lift_evidence_id`。至少要包含：

```text
source equation interface
target equation interface
lift map version/hash
universal quantifier statement
symbolic verifier/reproduction hash
negative mutation IDs
```

### 2.6 E5 receipt

必须由 runtime 计算并绑定：

```text
source potential receipt
target potential receipt
ticket type
taxonomy hash
strict comparison coordinates
parent-to-final target assertion
```

### 2.7 注册权隔离

必须拆分：

```text
coordinator-owned producer registry
coordinator-owned terminal schedule registry
independent validator registry
projector registry
T5 ticket registry
```

约束：

- track 不能在自己的 harness 中注入活动 ProducerRule；
- track 不能把 local terminal predicate 注册为 complete schedule；
- validator 不能调用 producer 的“已验证”结论；
- validator 与 producer 必须来自不同模块、不同 digest；
- actual source 类型不能通过字符串字段或布尔值改变。

### 2.8 负控

至少新增：

```text
CONTROL_AS_ACTUAL_BY_LABEL
LOCAL_MISS_AS_GLOBAL_MISS
SELF_REGISTERED_PRODUCER
SELF_REGISTERED_VALIDATOR
SOURCE_DIGEST_SWAP
OCCURRENCE_PATH_SWAP
CLAIM_HASH_DRIFT
PROJECTOR_HASH_DRIFT
GRAMMAR_HASH_DRIFT
T5_TAXONOMY_DRIFT
PARENT_TRANSITION_REPLAY_BREAK
```

### 验收标准

- runtime 不再接受裸 E1–E4 bool；
- `evidence_ids` 不能替代结构化 receipt；
- QC1 cross-audit 的“改 evidence class 即 admission”攻击必须失败；
- 任意 claim/reproduction/validator/grammar/taxonomy hash 改动会使旧 receipt 失效；
- producer 与 validator 权限隔离有静态测试和运行时测试。

---

## Gate 3 — 关闭 F1 四个 unknown

### 目标

完成 `PRODUCER_PROJECTION_AND_EXCLUSIVE_ADMISSION_V1`，并发布真正可用的 grammar/registry freeze。

### 3.1 全 source signal 裁定

对 constructor inventory 中每个信号，必须永久选择：

```text
ACTIVE_PRODUCER
NONRUNTIME_CONTROL
TERMINAL_ONLY
OBSOLETE/UNREACHABLE_WITH_PROOF
```

任何 `UNKNOWN` 数量必须为 0。

### 3.2 producer guard partition

每个 ACTIVE_PRODUCER 必须有：

```text
source owner/domain
complete source terminal schedule
guard leaves
mutual exclusivity proof
coverage proof
TERMINAL / REJECT / CANDIDATE target disposition
allowed target families
projector ID
validator ID
T5 ticket types
```

### 3.3 no-bypass

静态审计与运行时审计共同证明：

- 所有 persistent queue mutation 只有一处；
- 没有直接 `list.append`、deque append、hidden buffer、fixture promotion 绕过；
- bootstrap 与 successor 共用 admission；
- 所有 target 都重新经过 family classifier；
- 所有 producer 只能通过 coordinator registry 调用。

### 3.4 全 target re-entry

建立 trace induction：

```text
Base: root initializer -> admitted persistent state or terminal
Step: admitted state -> terminal or admitted lower-potential state
```

每个 target schema 必须投影为同一 `PersistentSelectorStateV1` envelope，禁止 track-local persistent object。

### 验收标准

```text
F1 unknown = 0
all_enqueue_gates_found = true
all_queue_mutations_exclusive = true
all_nonterminal_targets_reenter_one_classifier = true
all_active_producers_registry_bound = true
all_active_sources_terminal_complete = true
```

只有此时才允许：

```text
F1 = CLOSED
producer registry hash frozen
grammar hash frozen
```

---

## Gate 4 — 完整 terminal schedule 框架

### 目标

把“模板列表”升级为“在精确 owner-domain 上覆盖全部优先终止的定理”。

### 4.1 schedule contract

每个 schedule 必须声明：

```text
schedule_id
owner-domain quantifier
ordered terminal families
coverage theorem
mutual precedence
certificate verifier
lift verifier
schedule digest
```

`MISS_COMPLETE` 只有在 coverage theorem 已重放时才可产生。2026-08-26 的实现复查进一步
要求把该旧名字拆开：有限 schedule 只能产生 scope-bound 的
`MISS_REGISTERED_PRIORITY_COMPLETE`，并明确 `global_exhaustion=false`；若完整自然缺口
宇宙在语义重放后确实全 miss，结论是根反例而不是 producer continuation。单纯携带 opaque
digest 的 universe mapping 只能标为 evidence-only shape，不能写成 certified counterexample。

### 4.2 必须加入的 adversarial controls

至少包括：

- 已知 gap-11 terminal：`p=241441, x=60363, d=1083`；
- Bradford/其它已知终止模板的 precedence mutation；
- 一个 local predicate 全部 miss、但全局 terminal 命中的反例；
- terminal/producer 同时命中时，terminal 必须抢先；
- target terminal preemption 与 source terminal preemption 分开验证。

### 验收标准

- local schedule 不能产生 `MISS_COMPLETE`；prefix-complete schedule 也必须绑定其有限 scope；
- 每个 active producer 的 source schedule 有全域 coverage theorem；
- terminal certificate 可提升回 root；
- schedule digest 被 E1 和 transition bundle 同时绑定。

---

## Gate 5 — 激活一个窄 producer 作为架构样板

### 目标

在批量接入 F2/F3 前，选择一个量词窄、算术已充分验证的 q=1 producer，完成真正的端到端活动边。

### 推荐候选

优先从现有 q=1 full-carrier / C9 已收缩切片选择，但必须满足：

- exact source domain；
- complete source terminal schedule；
- structured E1–E5；
- independent validator；
- common projector/admission；
- target re-entry；
- strict fixed T5；
- mutation suite。

### 验收标准

```text
active_verified_wave1_producers = 1
该 producer 的所有 guard leaves = EMPTY / TERMINAL / VERIFIED_SUCCESSOR
无 local MISS 权限
无 track-local registry
从 root 或已验证 predecessor 可连续 replay
```

只有 pilot 完成，才批量开放其余 producer admission。

---

## Gate 6 — F2 residual 清零

当前五组 F2 residual 应按依赖排序处理。

### F2-1 post-G / C9 连续 runtime

当前 q=1 局部链已覆盖部分 C9 R=23 subray，但其余 R=23/35/11 行、高 owner、完整 terminal schedule、registered route、最终 re-entry 仍不完整。

目标：

```text
G endpoint
-> full-carrier root
-> first Type-I child
-> second anchor
-> C9/H4/terminal
-> admitted re-entry
```

验收：每个 row 均 EMPTY、TERMINAL 或 structured successor。

### F2-2 C8/H4 atomic actualization

现有数学 trichotomy 已收窄，但 harness 仍可能是 synthetic/local。需要：

- actual parent-bound source receipt；
- complete source terminal schedule；
- shared atomic target projector；
- H4 与 C8 不再各自输出 pending shape；
- atomic F/G target 进入活动 family；
- c8 other branch 不留 residual。

### F2-3 noncanonical high-support

已有 normalizer 的 E2/E4/局部 E5。需要二选一：

1. 证明该 branch 在 actual reachable graph 中为空；或
2. 给出 source normalizer producer 的 E1、E3、terminal-first、re-entry。

不能用 post-hoc determinant identity 作为 source receipt。

### F2-4 C=1 composite-D

prime-D stratum 已 empty；composite-D 有正控制。下一最小定理应是：

```text
完整 quotient/cofactor/order/gcd gate
-> terminal scheduler
或
-> deterministic non-upward successor
```

需要特别避免把精确参数化误报为 terminal theorem。

### F2-5 C>1 empty-improvement

必须得到：

```text
FAMILY_EMPTY
或 root TERMINAL
或 outer-rank / phase / protocol 严格下降 successor
```

当前 saturation route 缺 actual E1 和 fixed E5，不能激活。

### F2 关闭标准

```text
f2_open_residual_groups = 0
所有 F2 producer 均在 frozen registry
所有 source schedule complete
所有 target 通过 common E3
所有非终止边有 parent-to-final fixed T5
所有 target re-enter
```

---

## Gate 7 — F3 residual 清零

F3 应先建立共同 endpoint-path receipt，再分支处理。

### 7.1 共同接口：`F3ProperRootEndpointPathReceiptV1`

字段至少包括：

```text
actual root state
root owner
proper-factor witness
height regime
terminal schedule result
raw endpoint path
selected factor occurrence
path precedence digest
endpoint payload digest
routing leaf ID
```

QC1、TR1、high endpoint、m3q5 都只能从该 receipt 或其严格扩展开始。

### F3-1 QC1 q|E

局部 deflation 已通过。需要：

- source-bound integer occurrence；
- endpoint-excess 专用 projector；
- independent E4 lift；
- fixed T5 ticket；
- target re-entry。

### F3-2 QC1 q∤E

不能用 ideal factor 替代 occurrence。必须：

- 构造真实 carrier occurrence；或
- 证明该 leaf terminal/empty；或
- 确定性转入另一个已关闭域。

### F3-3 TR1

先完成：

- `Q | u` 的完整 terminal prefix；
- fresh `D*` integer occurrence；
- R4/R6 source-bound split；
- terminal-or-single-side 后的 canonical rank；
- common admission/re-entry。

### F3-4 high strict carry

当前 arithmetic carry 可以局部成立，但缺 source binding、E3 和 re-entry。需要建立 high-only normal form，禁止偷用 low-height `k,D*` 字段。

### F3-5 high stutter K=1

当前形成 Pell-like residual。需要把它推进为：

```text
empty
terminal
或 deterministic lower-potential successor
```

### F3-6 high stutter odd k>=3

需要 high-only physical carrier 和 target serializer，不得仅给 divisor gate。

### F3-7 m=3,q=5 runtime binding

完成 R1 actual source-path coverage；state ID/scope 不能只是 digest 输入，必须来自 active predecessor chain。

### F3-8 nonminimal q=5

给出精确 routing：terminal、empty 或 paid successor，不得默认最小 q。

### F3-9 regeneration p-free failure

关闭 regeneration 后不能得到 p-free endpoint 的 residual。

### F3-10 p² one-sided / two-sided

分别证明：

```text
EMPTY
TERMINAL
VERIFIED_SUCCESSOR
```

并完成 second-child 的 parent-to-final E5。禁止把更多必要同余本身当作 closure。

### F3 关闭标准

```text
f3_open_residual_groups = 0
QC1/TR1/m3q5/high-endpoint 均从真实 endpoint-path receipt 开始
无 ideal factor 伪装 occurrence
无任意 state ID/scope 伪装 admitted source
每个 final target 有 structured E1–E5 + re-entry
```

---

## Gate 8 — 独立审计、状态升级与 F4 handoff

### 独立审计要求

- verifier 不得调用被审计 producer 的内部“已验证”函数；
- producer/validator/claim/reproduction hashes 全部独立；
- 从干净 checkout 重放；
- 构造逻辑和审计逻辑分模块；
- 每条 closure-critical claim 至少有一份 independent review receipt；
- mutation suite 必须证明旧的伪造方式会失败。

### 状态升级顺序

```text
F1 CLOSED
then F2 CLOSED and F3 CLOSED
then freeze complete edge set
then F4 selector assembly
then F5 independent global audit
then only consider T6 status
```

关闭 F2/F3 不能直接把 T6 标为 CLOSED。

---

## 8. 高并发执行架构

当前 1 个主线程 + 7 个 subagent 的配置适合采用两波并发，而不是让所有代理立即攻击数学 hard core。

## 8.1 整治波 R

| 线程 | 责任 | 交付物 |
|---|---|---|
| Coordinator | shared schema/runtime/registry/frontier/status；合并；最终裁定 | Gate 0–4 集成基线、共享 API、live snapshot |
| Agent R1 | CI 修复和扩面 | workflow patch、完整命令矩阵、CI manifest generator |
| Agent R2 | live audit snapshot v2 | snapshot schema、digest generator、staleness tests |
| Agent R3 | structured E1–E5 receipts | dataclasses/schema、canonical serialization、hash binding tests |
| Agent R4 | terminal schedule completeness | schedule contract、gap-11 等 adversarial controls、coverage verifier |
| Agent R5 | constructor/no-bypass/F1 | source inventory 清零、queue static audit、re-entry induction |
| Agent R6 | F2 独立复核 | 把本文 V-A 推导写成 reproduction；检查 F2 claim 量词和反控 |
| Agent R7 | F3 独立复核 | QC1 forgery regression、TR1/R6 verifier、m3q5 source-binding audit |

### 整治波合并顺序

```text
R1 CI baseline
R2 live snapshot
R3 receipt schemas
R4 terminal schedule
R5 F1/no-bypass
R6/R7 independent proof controls
Coordinator Gate 0–4 full replay
```

Gate 2/3 未通过前，数学 agent 只提交 claims/reproductions/interface requests，不提交活动 producer registration。

## 8.2 数学波 M

| Agent | 互斥责任域 |
|---|---|
| M1 | F2 post-G/C9 连续 runtime 和 remaining rows |
| M2 | F2 C8/H4 actual atomic producer 和 shared target serializer |
| M3 | F2 C=1 composite-D terminal/non-upward exit |
| M4 | F2 C>1 empty-improvement + noncanonical high-support |
| M5 | F3 QC1/TR1 actual occurrence 与 endpoint-path receipt |
| M6 | F3 high strict carry + K=1 stutter + odd k stutter |
| M7 | F3 m3q5 runtime binding、nonminimal、regeneration、p² one/two-sided |

Coordinator 继续独占：

```text
producer registry
terminal schedule registry
family grammar
T5 taxonomy
frontier/ledger/README
shared runtime
status changes
final merge
```

---

## 9. 文件所有权与合并纪律

### Coordinator 独占

```text
README.md
index/**
data/t6-proof-frontier-v2.json
data/t6-selector-obligation-ledger-v1.json
data/t6-constructor-inventory-v1.json
data/t6-wave1/t6-live-audit-snapshot-v2.json
data/t6-wave1/family-grammar-*.json
scripts/t6_persistent_selector_runtime_v1.py
共享 receipt/schema/registry 模块
共享 terminal schedule 模块
共享 T5 taxonomy
.github/workflows/**
```

### Subagent 默认只新增

```text
claims/<track-prefix>-*.md
data/t6-wave1/<track-prefix>-*.json
reproductions/<track-prefix>_*.py
tests/test_<track-prefix>_*.py
docs/handoffs/<TRACK>_HANDOFF.md
data/interface-requests/<track-prefix>-*.json
```

### 规则

- subagent 不直接改状态；
- 不提交生成的 `index/**` 冲突，统一由 coordinator build；
- 每个 commit 只表达一个 theorem、一个 runtime interface 或一组直接相关 tests；
- 活动 registry 改动必须单独 commit；
- cherry-pick 后 coordinator 重跑 full suite；
- CI red 时不继续堆叠数学 merge 到 `main`。

---

## 10. 每个数学 track 的强制预交付

在长证明前，每个 track 先提交三份机器可审计文件。

### 10.1 Scope freeze

```json
{
  "track_id": "...",
  "base_verified_sha": "...",
  "exact_quantifier": "...",
  "included_leaves": [],
  "excluded_leaves": [],
  "allowed_established_claims": [],
  "forbidden_inferences": []
}
```

### 10.2 Residual matrix

每个 guard leaf 包含：

```json
{
  "leaf_id": "...",
  "predicate": "...",
  "coverage_proof_id": "...",
  "mutually_exclusive_with": [],
  "current_fact": "...",
  "planned_closure": "FAMILY_EMPTY|TERMINAL|VERIFIED_SUCCESSOR",
  "missing_E": ["E1", "E3"],
  "target_shape": "..."
}
```

### 10.3 Target-shape proposal

必须声明：

```text
existing/new family
normal form
owner precedence
mark behavior
terminal schedule requirement
projector requirement
T5 ticket type
re-entry owner
```

Coordinator 收齐 proposal 后冻结 grammar；未冻结前不得注册 producer。

---

## 11. Definition of Done

每个 track 必须通过：

| 编号 | 验收项 |
|---|---|
| D1 | exact actual-state quantifier，未静默缩域 |
| D2 | guard partition 互斥且穷尽 |
| D3 | structured E1 绑定 source、parent、occurrence、terminal schedule |
| D4 | deterministic E2，固定 tie-break，无 oracle |
| D5 | common E3，normal form、owner、grammar、admission 全绑定 |
| D6 | universal E4，非样本/非单点 lift |
| D7 | fixed global N⁷ parent-to-final strict T5 |
| D8 | target re-entry 到活动 selector domain |
| D9 | adversarial negative controls 全部 fail closed |
| D10 | independent replay 不复用 producer 内部结论 |
| D11 | current verified HEAD manifest 对齐 |
| D12 | claim/frontier/ledger/README 状态一致 |

---

## 12. 禁止性规则

以下做法一律不能构成 closure：

```text
从 registry 数量推 constructor 穷尽
从 recursive_edge_eligible=True 推 actualness
从 evidence_class 字符串推 actualness
从 divisor 推 raw occurrence
从 family label 推 E3
从 local terminal MISS 推 global terminal-first MISS
从 checkpoint/local rank drop 推 fixed T5 E5
从 prime 或 fixture 重造 parent
track 自行注入活动 ProducerRule/validator/scheduler
有限搜索无反例推 family empty
把 L1 的 p² gate 移植到 Lomega
high endpoint 使用 low-height k/D* 定理
历史 baseline SHA 冒充当前 verified HEAD
CI 红色时升级 theorem status
以新增 claim 数量替代 residual 清零
```

研究止损规则：一个新算术结论只有在至少完成以下之一时才进入关键路径：

```text
关闭一个完整 guard leaf
证明 family-empty
证明 terminal
给出 deterministic structured successor
严格缩小一个有 ID 的 residual theorem
```

单纯得到更高阶同余、更多整除性、更强下界或更大有限检验范围，不计作 closure。

---

## 13. 建议的最终验证命令

```bash
set -euo pipefail

python scripts/kb.py validate
python scripts/kb.py build
git diff --exit-code -- index/

python reproductions/pre_t6_contract_kernel_audit.py \
  --root . --require-full-tree
python scripts/audit_t6_constructor_inventory_v1.py

python -m unittest discover -s tests -p 'test_*.py' -v

ruff check scripts reproductions tests
python -m compileall -q scripts reproductions tests

git diff --check

python scripts/t6_emit_live_audit_snapshot_v2.py --verify-head
python scripts/t6_verify_receipt_registry_v1.py --require-independent
python scripts/t6_verify_terminal_schedules_v1.py --require-complete
python scripts/t6_verify_active_producer_registry_v1.py --require-frozen
python scripts/t6_verify_residual_frontier_v2.py --require-zero-if-closed
```

最后生成：

```text
data/t6-wave1/final-f1-f2-f3-closure-receipt-v1.json
```

其 counters 必须为：

```json
{
  "f1_unknown": 0,
  "f2_residual": 0,
  "f3_residual": 0,
  "unknown_actual_producers": 0,
  "conditional_actual_edges": 0,
  "unadmitted_targets": 0,
  "pending_persistent_targets": 0,
  "terminal_schedule_gaps": 0,
  "t5_ticket_failures": 0,
  "independent_review_gaps": 0
}
```

---

## 14. 状态升级政策

### 可以升级 F1 的唯一条件

- 四个 unknown 清零；
- all-constructor producer projection 完成；
- no-bypass 完成；
- complete terminal schedules；
- common structured E1–E5；
- 全 target re-entry；
- exact HEAD CI green；
- independent audit 通过。

### 可以升级 F2/F3 的唯一条件

- 对应 residual count 为 0；
- 每个 leaf 是 EMPTY、TERMINAL 或 VERIFIED_SUCCESSOR；
- 无 arithmetic-only/conditional/local/pending leaf；
- 所有 active edges 已进入 frozen registry；
- 全部通过 fixed T5 和 independent replay。

### 不能升级 T6 的情形

即便 F1/F2/F3 关闭，仍需：

```text
F4 single deterministic selector assembly
F5 independent whole-selector audit
```

因此 F2/F3 closure 后只生成 F4 handoff，不直接改 T6。

---

## 15. 可直接交给 Codex + sol max 的 Master Goal

```text
GOAL ID:
T6-REMEDIATE-VERIFY-AND-CLOSE-F2-F3-2026-08-25

AUTHORITATIVE SPECIFICATION:
docs/T6_LATEST_PROGRESS_PROOF_REVIEW_AND_REMEDIATION_PLAN_2026-08-25.md

MISSION:
Execute the authoritative specification exactly. First restore a trustworthy,
HEAD-bound verification baseline; then harden the proof-carrying runtime;
then close the four F1 unknowns; finally run the seven mutually exclusive F2/F3
mathematical tracks in parallel until every registered residual leaf is EMPTY,
TERMINAL, or a VERIFIED_SUCCESSOR with structured E1-E5 and recursive re-entry.

CURRENT OBSERVED HEAD:
232b186485f077bda044610938bf115d2911ef7a

CURRENT STATUS:
F1 = OPEN_MINIMAL_GAPS
F2 = OPEN
F3 = OPEN_MINIMAL_GAPS
T6 = OPEN

NON-NEGOTIABLE FIRST GATE:
The current main CI is red. Fix the failure, expand the workflow to cover the
wave1 runtime, residual data, all tests, constructor inventory, KB build
consistency, lint, compile and diff checks, and emit a machine-generated
HEAD-bound run manifest. Do not promote any theorem status while this gate is
red or while the observed HEAD differs from the last verified HEAD.

COORDINATOR OWNS:
- shared runtime and state envelope
- structured E1-E5 receipt schemas
- producer, validator, projector and terminal-schedule registries
- family grammar and precedence
- T5 taxonomy
- live audit snapshot
- shared files, generated index, frontier, ledger, README
- all active registry changes
- merge order and theorem-status decisions

REMEDIATION WAVE:
1. Restore and broaden CI.
2. Create live audit snapshot v2 separating historical workpack SHAs from the
   current verified HEAD.
3. Replace E1/E2/E3/E4 booleans and free evidence IDs with structured,
   content-hashed receipts bound to source, parent transition, actual
   occurrence, complete terminal schedule, claim, reproduction, independent
   verifier, projector, grammar and taxonomy.
4. Prevent track-local self-registration of active producers, validators and
   terminal schedules.
5. Make the QC1 evidence-class forgery control fail closed.
6. Close all four F1 unknowns and prove exclusive queue admission plus global
   target re-entry.
7. Establish complete owner-domain terminal schedules with adversarial terminal
   controls.
8. Activate exactly one narrow q=1 producer end-to-end as an architecture pilot.

MATHEMATICAL WAVE:
Run seven concurrent, mutually exclusive tracks:
- F2 post-G/C9 continuous runtime.
- F2 C8/H4 actual atomic closure.
- F2 C=1 composite-D terminal or non-upward exit.
- F2 C>1 empty-improvement and noncanonical high support.
- F3 QC1/TR1 actual occurrence and endpoint-path receipts.
- F3 high strict-carry and high-stutter residuals.
- F3 m=3,q=5 source binding, nonminimal q5, regeneration and p2 one/two-sided.

FOR EVERY LEAF:
The only accepted final dispositions are FAMILY_EMPTY, TERMINAL, or
VERIFIED_SUCCESSOR. A verified successor must carry structured actual E1,
deterministic E2, common admitted E3, universal E4, exact parent-to-final fixed
N^7 E5, and recursive re-entry.

FORBIDDEN:
- fixture/control promoted to actual by labels or booleans
- divisor treated as an occurrence
- local terminal MISS treated as globally complete
- self-injected ProducerRule, validator or terminal scheduler
- family label treated as E3
- local checkpoint descent treated as T5
- finite search treated as a universal proof
- historical baseline treated as current verified HEAD
- theorem-status promotion while CI is red

FINAL ACCEPTANCE:
- exact HEAD CI green
- live snapshot matches HEAD and all artifact digests
- F1 unknown = 0
- F2 residual = 0
- F3 residual = 0
- active producers all registry-bound
- no conditional actual edges
- no pending persistent targets
- all complete terminal schedules verified
- all structured receipts independently replayed
- all T5 tickets valid in the fixed global potential
- all negative controls pass
- KB/frontier/ledger/README consistent

On success, freeze the complete F2/F3 edge set and create the F4 handoff.
Do not mark T6 closed before F4 assembly and F5 independent whole-selector audit.

On failure, do not report approximate closure. Return the smallest exact
residual package with its quantifier, discharged guards, remaining guard,
source requirements, strongest current theorem, exact missing E-stage,
reproducible obstruction, and next minimal theorem.
```

---

## 16. 最终判断

当前项目已经从“缺少局部结构”推进到“拥有大量局部结构但缺少可信物理化”的阶段。这个阶段最危险的误判是继续把 arithmetic success、local macro、测试 harness admission 或合并数量当作 selector closure。

本次复查没有发现足以整体否定当前数学方向的普遍代数错误；相反，R=3 D-contact、mixed-D 参数化、high-support normalizer、QC1 deflation、TR1 dyadic split、R6 companion 等局部结果大多可以在其精确量词下复算成立。真正阻塞 T6 的是：

```text
actual source chain
complete terminal-first schedule
content-bound independent E1-E4
common E3
fixed parent-to-final T5
recursive re-entry
HEAD-bound independent replay
```

因此整治的核心不是“降低证明标准”，而是把已经获得的数学成果转化为不可伪造、可复放、可组合的活动证明边。完成 Gate 0–5 后，F2/F3 的高并发数学推进才会真正累积，而不是继续产生无法登记的 candidate package。
