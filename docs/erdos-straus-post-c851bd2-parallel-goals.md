# erdos-straus：c851bd2 之后的并行执行 Goals

## 0. 基线与不可越界约束

- 唯一工作基线：`c851bd213936b3bc8b3103b469292c139d229e97`（`Archive proof packages and clarify T6 boundary`）。
- 所有工作从该提交新建分支，不得直接改 `main`：
  - Codex：`codex/f1-reachability-contract`
  - sol-ultra：`sol-ultra/f3-proper-root-physicalization`
- `archive/` 仅为证据保全区，不是活动证明源；不得直接应用归档补丁，不得让归档中的旧状态覆盖活动 claims、concepts、data 或 README。
- 当前允许的状态结论：T1v1–T5v1 保持各自既有相对/局部闭合状态；T6、F1、F2、F3、F4、F5 和 Erdos–Straus 猜想保持 OPEN，除非本任务列出的全部门槛被逐条满足。
- 禁止把以下任一事实当作 T6 或 F3 已闭合：
  - 存在算术候选；
  - 某个局部宏满足 E2/E4；
  - 有限计算未发现反例；
  - 当前 registry 中只出现既有 family；
  - 所有“已登记”边下降；
  - `L_omega ≡ 1 (mod p^2)` 已被进一步提升到 `mod p^3`，但没有终止或下降票据。
- 新 constructor、新 family、新 serializer 或新 target 只能经 admission firewall 纳入：登记 source/target、补 T2/T3、给出 serializer 与 lift、指定 T6 owner、通过独立审计。
- 每个阶段必须形成小而可审计的提交。按仓库 `AGENTS.md` 执行提交和分支推送；不得合并到 `main`。

## 1. 当前阶段总目标

不是“立即证明 T6”，而是同时完成两个阻塞性里程碑：

1. **Codex 关闭或精确反驳 F1**：从真实 constructor/serializer 出发，建立非循环的可达持久状态闭世界、family 分类、owner 决定与重入归纳。
2. **sol-ultra 关闭或最小化 F3**：在不假设 F1 已成立、不引入未审计状态的前提下，把 proper-root `k>1` 通道从算术候选推进为真实 E1–E5 选择器边，并处置 `p^2` 残余门。

两条线可以并行研究，但任何 F3 新 target 在 F1 grammar freeze 前都只能作为候选证据，不得登记为活动边。

---

# GOAL A — Codex：F1 可达状态闭世界与分类合同

## A.1 单一目标

证明或精确反驳以下命题：

> 对每个从真实 initializer 和已准入 successor serializer 递归可达的、非终止、合法持久状态，存在且仅存在一个按固定优先级决定的活动 family owner；每个真实 constructor 的每个非终止 E3 target 都能通过同一 admission/normalization 路径重新进入该分类域。

本分支只处理 F1。不得顺带宣称 F2、F3、F4、F5、T6 或猜想闭合。

## A.2 执行包

### A0. 从源码重建真实 constructor/serializer inventory

创建：

- `data/t6-constructor-inventory-v1.json`
- `docs/audits/T6_CONSTRUCTOR_INVENTORY_V1.md`
- `scripts/audit_t6_constructor_inventory_v1.py`
- `tests/test_t6_constructor_inventory_v1.py`

每个 inventory 条目至少包含：

- 稳定 ID；
- 实现文件与符号；
- source state kind/family；
- terminal-first 分支；
- 非终止 target schema；
- 是否产生 persistent queue item；
- 实际 enqueue/serializer 入口；
- E3 typing/normal-form 前置条件；
- 当前 owner 或 `UNASSIGNED`；
- registry 对应项；
- T2/T3 覆盖项；
- 证据引用。

inventory 必须由活动源码和活动数据双向核对，不能从“当前 registry 恰有 15 个 producer”反推源码完备性。

### A1. 定义非循环的持久状态合同

建立一个独立于 normalizer 成功、owner digest 或 family 识别结果的最小合法状态定义，例如 `PersistentSelectorStateV1`。合法状态的定义只能依赖可直接验证的字段、来源收据和 schema 约束。

必须实现或明确绑定：

- `extract_verified_selector_header_v1` 或等价真实接口；
- 活动 normalizer 的全部输入；
- family predicates；
- owner precedence；
- owner digest；
- 所有真实 persistent enqueue gates；
- reject-before-queue 路径与稳定 reason codes。

禁止在“合法持久状态”的定义中预先要求“已经获得 owner/normal form”，否则仍属循环论证。

### A2. 为每个 constructor 建立 guard partition

对 inventory 中每个真实 constructor/serializer，给出完整、互斥或经固定优先级消歧的 guard partition：

1. terminal 分支；
2. reject-before-queue 分支；
3. 每个可产生非终止 E3 target 的分支；
4. target 进入 family predicates 的证明；
5. target 重新通过 admission/normalization 的证明；
6. 没有遗漏 H4、atomic、overflow、post-G、marked 或未知 residual。

无限域覆盖必须有符号证明；测试只能验证实现与证据清单一致，不能把有限枚举当作全称证明。

### A3. 建立 family totality、唯一性与重入归纳

必须分别证明：

- **覆盖性**：每个已准入非终止 target 至少命中一个活动 family predicate；
- **决定性**：固定 precedence 后 owner 唯一；
- **失败闭合**：零命中、非法多命中、未知 header、未登记 constructor 一律在入队前拒绝；
- **重入性**：所有已准入非终止 target 回到同一 F1 域；
- **迹归纳**：initializer 基础步 + 每个 constructor 的 successor 步，得到所有实际可达持久状态均被覆盖。

### A4. 做真正的负控和变异测试

测试必须把变异对象送进真实 audit/admission 路径，而不是只检查 JSON 常量。至少包括：

- 缺失 constructor；
- registry 多出或少掉 producer；
- 未知 header/version；
- malformed source receipt；
- 空 owner；
- owner overlap；
- precedence 改动；
- 未登记 target；
- serializer 绕过 admission；
- 新 family 未补 T2/T3；
- archive 文本试图污染活动状态；
- 新 constructor 加入后 audit 必须 fail closed。

### A5. 更新活动知识库，但只按证据升级

交付：

- 一份 F1 claim；
- 一份 F1 reproduction/audit；
- 一份 machine-readable proof receipt；
- 必要的 concept/data/test/CI 更新；
- `docs/handoffs/CODEX_F1_HANDOFF.md`。

只有 A0–A4 全部通过，才能把 F1 更新为 `ESTABLISHED` 或项目采用的等价闭合状态。否则必须保持 OPEN，并输出最小缺口或最小反例。

## A.3 Codex 验收标准

Codex 分支只有在以下条件全部满足时才算通过：

- [ ] inventory 与活动源码、registry、T2/T3 双向一致，未知项为零；
- [ ] 合法状态定义不依赖 normalizer/owner 结论；
- [ ] 所有真实 enqueue gates 已发现并纳入；
- [ ] 每个 constructor 有完整 guard partition 和符号覆盖证明；
- [ ] 所有非终止 target 都能被实际 extractor 读取并重新分类；
- [ ] owner 在固定 precedence 下唯一；
- [ ] 未知或未登记状态在 persistent queue 前失败；
- [ ] 迹归纳包含 initializer 基础步和全部 successor 步；
- [ ] 负控实际触发预期失败；
- [ ] 未修改 `archive/`；
- [ ] 未升级 F2/F3/F4/F5/T6/猜想状态；
- [ ] 全部仓库校验命令通过；
- [ ] handoff 明确列出“已证命题、依赖、未证命题、文件、命令、commit SHA”。

若任一项失败，合格输出不是模糊“部分完成”，而是：

- 保持 F1 OPEN；
- 给出最小未分类 target、缺失 constructor 或循环依赖；
- 提供可复现失败收据和下一条最小定理。

---

# GOAL B — sol-ultra：F3 proper-root k>1 物理化与 p² 门处置

## B.1 单一目标

在真实 terminal-first survivor 域上，证明或精确反驳：

> 每个 proper-root `k>1` 状态都能通过确定、可计算、无 oracle 的规则，被路由到 terminal、QC1/TR1、已覆盖 slice，或一个满足 E1–E5 且带严格 T5 下降票据的已准入 successor；所有 successor 递归回到 F1 域。

本分支不得假设“当前 family 列表已语义穷尽”，不得把 `m=3,q=5` 的局部化简外推成所有 proper-root 状态。在 Codex 发布 F1 grammar freeze 以前，本分支只能形成可复用的数学定理和 candidate receipts，不得升级 F3 或登记新边。

## B.2 执行包

### B-1. 对 F1 做独立语义交叉审查

在不读取 Codex 生成的 inventory 结论字段的前提下，从活动源码独立列出：initializer、所有可能产生 persistent target 的 constructor/serializer、terminal-first 分支及 target schema。随后只比较两份清单的差异。

交付 `docs/audits/SOL_ULTRA_F1_INDEPENDENT_DELTA.md`，至少报告：

- Codex inventory 遗漏项；
- sol-ultra 遗漏项；
- registry/source/T2/T3 不一致；
- 可能产生当前 family predicates 之外 target 的 guard；
- 无法从源码证明穷尽的动态或间接 constructor。

任何 unresolved delta 都阻止 F1 closure 和 F3 集成，但不阻止继续研究不依赖该 delta 的局部算术。

### B0. 精确定义真实研究域

创建一份域规范，明确：

- actual root receipt；
- terminal-first 过滤顺序；
- proper-root 与 `k>1` 的定义；
- 当前 `m=3,q=5` slice 在全域中的位置；
- 所有已知出口、未知 residual 和前置 owner 条件；
- 哪些对象是 actual、conditional adapter、analysis-only。

不得把 debug/workfile artifact 当成 actual source path。

### B1. 全域 routing theorem

证明每个 proper-root `k>1` 输入恰落入以下之一：

1. terminal；
2. QC1；
3. TR1；
4. 已经由活动定理覆盖的 slice；
5. 明确定义且互不遗漏的 residual family。

若第五类非空，必须给出最小参数化描述或最小反例，不能用“其他情况类似”略过。

### B2. E1：真实 source/path 收据

把每个候选算术因子、分母或宏绑定到真实父状态中的实际对象：

- 来源 occurrence；
- support/provenance；
- 消耗规则；
- terminal-first 后仍存活的证明；
- 不能被别的分支先行消费的优先级证明。

仅有整除性或同余式不构成 E1。

### B3. E2–E4：确定 target、类型和普适 lift

对每个非终止出口证明：

- E2：target 由输入确定，tie-break 完整；
- E3：target 满足活动 schema、normal form 和候选 owner 条件；
- E4：lift 对该分支全域有效，而不是样本或有限范围有效；
- terminal branch 总是优先于 enqueue；
- 不依赖未声明 oracle、搜索上界或人工选因子。

若 target 不属于当前 F1 grammar，只能提交 `NEW_FAMILY_CANDIDATE`：必须附 source/target schema、guard、serializer、lift、T2/T3 需求和 owner proposal；不得自行登记。

### B4. checkpoint/second-child 与 E5

必须给出：

- checkpoint 的确定选择规则；
- second-child 的确定 tie-break；
- 非重复/不回到同一未付费状态的证明；
- target typing 和 lift；
- 一张固定、可核验的 T5 下降票据；
- 与其他出口的 precedence。

### B5. 关闭 `L_omega ≡ 1 (mod p^2)` 残余门

在 actual divisor-source 域上，将该分支证明为下列三种之一：

1. **EMPTY**：在真实来源约束下无解；
2. **TERMINAL**：必然直接终止并给出 lift；
3. **PAID_SUCCESSOR**：产生已准入 successor，满足 E1–E5 和严格 T5 下降。

只把同余提升到 `mod p^3`、或只给有限搜索证据，不算关闭。

优先寻找“实际 divisor source 的分类定理”，而不是继续堆叠无来源的同余必要条件。

### B6. 递归 closure 与可复现产物

交付：

- F3 总 claim 或一组可组合子 claims；
- 符号推导文档；
- machine-readable routing/receipt 数据；
- verifier；
- 单元测试和反例/负控 corpus；
- `docs/handoffs/SOL_ULTRA_F3_HANDOFF.md`。

verifier 必须区分：

- 符号证明检查；
- 实现一致性检查；
- 有限探索性计算。

有限探索不得被报告为全称证明。

## B.3 sol-ultra 验收标准

- [ ] 已完成独立 F1 constructor delta 审查，所有影响 F3 target 的差异均已解决或显式阻断集成；
- [ ] 量词域覆盖所有 actual proper-root `k>1` survivor，而非仅 `m=3,q=5`；
- [ ] routing 分支完整且 precedence 确定；
- [ ] 每条非终止边有真实 E1 source/path receipt；
- [ ] E2、E3、E4 对全分支成立；
- [ ] checkpoint/second-child 有确定规则、非重复证明和 E5；
- [ ] `p^2` residual 被证明 EMPTY、TERMINAL 或 PAID_SUCCESSOR；
- [ ] 所有 successor 要么属于当前活动 F1 grammar，要么以未登记 candidate 形式触发 firewall；
- [ ] 不使用有限验证替代无限域证明；
- [ ] 不把 conditional adapter 登记成 actual edge；
- [ ] 未修改共享 frontier 状态或 README 的 T6 结论；
- [ ] 全部仓库校验命令通过；
- [ ] handoff 明确列出“已证命题、失败分支、最小 residual、依赖、文件、命令、commit SHA”。

若无法关闭 F3，合格输出必须是一个严格缩小后的、带显式量词和真实 source receipt 的最小 residual theorem；不得仅报告更多实验数据。

---

# 2. 并行协作与合并检查点

## 2.1 文件所有权

### Codex 独占修改

- 活动 state contract/normalizer/admission；
- constructor inventory；
- family predicates/owner precedence；
- F1 audit、tests、CI；
- 活动 frontier 的 F1 字段（仅在验收后）。

### sol-ultra 独占修改

- 新 F3 claims/reproductions；
- proper-root routing 数据；
- p² residual 推导与 verifier；
- F3 反例 corpus；
- candidate-family proposal 文件。

### 集成阶段才允许修改

- README 总状态；
- `data/t6-proof-frontier-*.json` 的跨轨状态；
- theorem ledger；
- selector 全局 precedence；
- T6 状态。

## 2.2 F1 grammar freeze 检查点

Codex 完成 A0–A3 后发布一个可审计的 grammar hash/manifest。sol-ultra 逐条把 B 轨所有 target 对照该 manifest：

- 全部 target 可分类：继续 B3–B6；
- 出现未分类 target：sol-ultra 只提交 candidate；Codex 通过 firewall 决定纳入或拒绝；
- 纳入新 family 后，F1、T2、T3 和相关 audit 必须重新运行；
- 不得通过重命名或强行映射把未知 target 塞进现有 family。

## 2.3 第一波完成定义

第一波只有三种合法结果：

1. F1 closed + F3 closed；
2. F1 closed + F3 缩小为一个或少数真实 residual；
3. F1 被最小反例/refutation 阻断，F3 输出仍可独立复用的局部定理。

“代码通过但量词未闭合”不算 theorem closure。

---

# 3. 第二波并行 Goals（F1 grammar freeze 后启动）

## GOAL C — Codex：F2 工程型 family totality

优先处理已经具有局部算术或局部宏、但缺少 admission/E3/re-entry/owner 的分支：

1. post-G Type-I continuation；
2. A>1 overflow target 的 typing、owner、re-entry；
3. atomic outcome 的 target closure；
4. 低支持和 A=1 局部结果向总 family 出口的组合；
5. M conditional adapter：只有 F1 证明其 source 实际可达且 admission firewall 全部通过时才登记；否则保留 conditional。

每个 family 只允许三种 closure 形式：family-empty、terminal、或 E1–E5 paid successor。每关闭一个 family，都必须有独立 claim、receipt、负控和 T5 票据。

## GOAL D — sol-ultra：F2 数学硬核 residual

集中处理：

1. high-support C=1：证明 actual family-empty、root terminal、outer-rank 下降或 lower-protocol paid reset；当前局部最小/无改进结果本身不够；
2. high-support C>1：构造严格 empty-improvement 或证明 family-empty；
3. c8 outgoing existence；
4. H4-other 与 c2_19 的全量出口；
5. 对 Codex 已接纳的 F2 宏做独立数学审查。

同样必须满足 EMPTY / TERMINAL / E1–E5 PAID_SUCCESSOR 三分标准。

---

# 4. 最终顺序：F4 → F5 → T6

只有 F1、F2、F3 全部闭合后，才启动：

## F4 selector assembly

- 单一确定 precedence；
- 所有 initial/reachable state；
- 每个非终止 leaf 有 E1–E5；
- terminal lift 完整；
- 每条边使用同一 `N^7` 势函数并严格下降；
- 无 OPEN、pending、analysis-only 或未登记 family；
- selector 可计算、无 oracle、无人工选取。

## F5 independent full-checkout audit

由另一代理从干净 checkout 独立重放：

- 不复用作者生成的中间缓存；
- 重建 KB 与 receipts；
- 运行全测试和负控；
- 核对 claims、concepts、data、README、ledger、CI 完全一致；
- 对每个 E1–E5 和 T5 ticket 做独立复核。

只有 F5 通过，才允许更新 T6。猜想本身的状态更新还必须单独核对从 T6 到全 conjecture 的完整定理链，不得自动继承。

---

# 5. 所有分支必须运行的验收命令

至少运行：

```bash
python scripts/kb.py validate
python scripts/kb.py build
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

对新增/修改 Python 文件另运行：

```bash
python -m py_compile <modified_python_files>
```

若仓库现有 CI、lint 或 goal 文档要求更多命令，以更严格者为准。任何失败都必须记录完整命令、退出码和最小复现。

---

# 6. 每个代理最终报告模板

```text
BASELINE
- Base commit:
- Branch:
- Final commit:

CLAIMED RESULT
- Exact theorem/contract statement:
- Quantifier domain:
- Status: ESTABLISHED | OPEN_MINIMAL_GAPS | REFUTED_CONTRACT

EVIDENCE
- Claims:
- Concepts:
- Data/receipts:
- Reproductions/verifiers:
- Tests/negative controls:

ACCEPTANCE MATRIX
- Criterion 1: PASS/FAIL + evidence
- ...

NON-RESULTS
- Statements explicitly not proved:
- Conditional/analysis-only artifacts retained:

RESIDUALS
- Smallest remaining quantified gap:
- Minimal counterexample or failing receipt:
- Next smallest theorem:

VALIDATION
- Commands and exit codes:

INTEGRATION NOTES
- Shared files touched:
- New constructors/families proposed:
- Firewall implications:
- Status files that must not be updated yet:
```
