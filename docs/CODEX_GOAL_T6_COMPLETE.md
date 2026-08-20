# Codex Goal：彻底闭合 T6 Global Selector

## 一句话任务

在 `priestess-bot/erdos-straus` 中，从当前 T6 工作基线继续研究和实现，构造并严格证明一个对所有核心素数及所有实际递归可达 legal state 都有定义的、无需读取未知解的确定性 selector；完成完整 E1–E5、reachable-state 穷尽、递归闭包和 T5 严格下降证明。只有全部验收门通过后，才把 `T6_GLOBAL_SELECTOR_TOTALITY` 从 `OPEN` 改为 `ESTABLISHED`。

## 起始基线

- 上游基线：`203716ba6f6478ded538674e34f214384d15fd1b`。
- 本轮 T6 工作最终提交：`1caa7db4d82d23baa000f833687e4246708a57c6`。
- T6 工作包已完整展开并归档在 [`archive/proof-packages/t6-proof-workfiles-2026-08-17/payload/`](archive/proof-packages/t6-proof-workfiles-2026-08-17/payload/)；原始字节包在 [`../archive/proof-packages/raw/erdos-straus-T6-proof-workfiles-2026-08-17.zip`](../archive/proof-packages/raw/erdos-straus-T6-proof-workfiles-2026-08-17.zip)。当前主线已包含该轮选择性接纳的内容，开始新工作前只应阅读归档和现有活动文件，不重复应用旧补丁。
- 开始前阅读仓库的 `AGENTS.md`（如有）、`README.md`、`concepts/flagship-proof-program-2026-08-16.md`、`concepts/denominator-escape-state-contract.md`、`concepts/t5-global-well-foundedness-contract-v2.md`、`docs/T6-current-progress-2026-08-17.md`、`docs/T6-closure-attempt-audit-2026-08-17.md`、`docs/T6-proper-root-minimal-gap-audit-2026-08-17.md` 和 `docs/T6-actual-reachable-coverage-audit-2026-08-17.md`。
- 保留用户已有改动。不要强制重置、覆盖无关文件、推送远端或创建 PR，除非用户明确要求。

## 最终必须证明的命题

对每个核心素数

\[
p\equiv1\pmod {24}
\]

以及由冻结后的初始状态和 verified edges 实际递归可达的每个 legal state
\(S\in\mathcal R_p\)，定义一个可计算的确定性 selector

\[
\Sigma(p,S)
\]

使其输出且只输出以下二者之一：

1. `Terminal(cert)`：一个可直接核验的 Type I 或 Type II terminal certificate；或
2. `Edge(T, receipt, lift, ticket)`：一个确定 successor \(T\)，满足

\[
E1(S,T)\land E2(T)\land E3(T)\land E4(T\to S)
\land \Pi_{T5}(T)<\Pi_{T5}(S).
\]

其中：

- E1 必须重放 actual source/path occurrence、provenance、terminal-first miss 和所消费 support；
- E2 必须给出完全确定、可序列化且不依赖未知目标解的 target；
- E3 必须证明 target 满足对应 normal form 与全部 legal-state guards；
- E4 必须给出对整个 target solution set 有效的显式、可计算 lift \(W_T\to W_S\)，不能只处理样本解；
- E5 必须从实际计算的 source/target 七元势得到固定的 `OUTER_RANK_DROP`、`PHASE_DROP` 或 `LOCAL_DROP` ticket，不能把“下降”仅写入 `verified_edge` 的定义；
- 每个 successor 必须仍属于 \(\mathcal R_p\)，因此 selector 可递归继续调用；
- selector 不得询问“哪个候选最终存在解”，不得使用未知 Erdős–Straus 分解作为 oracle，也不得依赖一个没有证明覆盖全域的有限搜索上界。

最终需得到

\[
\forall p\equiv1\pmod{24}\ \forall S\in\mathcal R_p:\quad
\operatorname{terminal}(S)\ \lor\
\operatorname{verified\_edge}(S,\Sigma(p,S)).
\tag{T6}
\]

再与 T5 的良基性组合，证明 selector 路径必定有限终止于可核验 terminal。

## 必须关闭的开放义务

### O1. 全局 reachable-state exhaustion

不能把当前 named-edge taxonomy 当成 state-space 的穷尽证明。必须从初始状态、状态合同、所有实际 constructor 和 successor serializer 出发，给出独立、无循环的 case split，证明每个 actual reachable nonterminal state 必落入某个已闭合 selector family。

至少覆盖：

- 其它 H4 selector branches 及 H4 后续 F/G 出口；
- ordinary positive-\(q\) G handoff 的首条 local edge 之后的完整 Type-I totality；
- 一般 \(A>1\) overflow；
- high-support/root-capacity states；
- proper-root stutter；
- c=8 parent、atomic target 及其后续状态；
- taxonomy 中所有当前实际 source family，以及本任务新增 edge family 的 targets。

需要建立两条独立归纳：初始状态属于 \(\mathcal R_p\)，以及 selector 的每个 target 仍属于 \(\mathcal R_p\)。不能通过把未覆盖状态从定义中删除来“证明”穷尽。

### O2. Proper-root `k>1` physicalization

令 \(\mathcal S_{\rm pr}\) 为 actual、terminal-first 后仍非终端的 proper-root stutter states。`k=1` actual 子域已经全称排空；必须对所有 \(k(S)>1\) 关闭至少一条足够路线：

\[
\operatorname{terminal}(S)
\ \lor\
\exists q\mid k(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T),
\tag{QC1}
\]

或

\[
\operatorname{terminal}(S)
\ \lor\
\exists q\mid D_*(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T).
\tag{TR1}
\]

形式 low chart、\(q\mid K_q\)、小商、q-adic 同余或 `analysis_evidence` 都不是 physical edge。必须把所选因子连回 actual source occurrence，正确处理旧 charged support，并给出完整 E1–E5。

已知 fixed finite same-\(q\) gap menu 受 Dirichlet–CRT no-go 限制；不要重复把这一已否定路线包装成全称证明。应考虑可变 gap、不同 carrier、多因子结构、canonical maximality 或新的合法 phase/outer-rank source。

### O3. c=8 outgoing existence

对每个 terminal-first-surviving actual c=8 parent \(P\)，证明

\[
\operatorname{terminal}(P)
\ \lor\
\exists q\in\mathcal Q_V(P):
q>2(p-1),\ 1\le c_a(q),c_\Sigma(q)\le7
\ \lor\
\exists T\;\operatorname{verified\_edge}_{\rm other}(P,T).
\tag{C8}
\]

已有 double-low theorem 只说明 receipt 一旦实际出现即可产生 strict macro；它没有证明 receipt 总存在。有限范围内没有 dead end、marker 的局部相容性、roughness 必要条件或一个 non-\(p\) V-side prime 的存在都不能替代上述全称析取。

### O4. 新增 family 引起的 T2/T3 义务

当前 closed-world audit 只证明现有 named graph 保持 \(W=\operatorname{Sol}(p)\)，且 atomic surface 恰为 H4 与 c=8 两个 v1 arms。

- 如果新增 atomic arm，必须同步扩展并证明 T2 admission grammar、one-use/pooled-capacity 约束和输入覆盖。
- 如果新增 nontrivial marked state，必须重开 T3，证明 terminal membership 或为每个失败状态给出合法 strict edge，并实现 serializer 与 total lift。
- 只有在给出对新 selector graph 的不变量证明后，才能继续把 nontrivial mark 标为 unreachable。

## 证明或否定的规则

对每个 state family，只允许以下三种闭合方式：

1. 全称证明该 actual family 为空；
2. 为该 family 构造全称 terminal；
3. 为该 family 构造全称 verified successor。

否定某个 candidate action、named fan 或有限菜单本身并没有关闭 state family；必须同时证明该 family 为空，或提供另一条 total exit。有限扫描、随机搜索和 SMT/计算机代数输出可用于发现公式、找反例和回归测试，但不能单独承担无限全域证明。

如果找到一个完全合法、actual reachable、terminal-first miss 且对冻结后的全部 admissible actions 都无 verified edge 的 state，则这是否定当前 T6 的反例：应把状态标为 `REFUTED`，保存完整 replayable receipt，并修订合同或新增合法 edge family后继续研究。绝不能把反例或 no-go 写成 `T6=CLOSED`。

## 实现顺序

1. 建立 machine-readable obligation ledger，逐项列出 source family、量词、guards、terminal、edge constructor、E1–E5、target family、T5 ticket、证明文件和 verifier；初始状态不得遗漏 `OPEN`。
2. 先完成 O1 的 state-family 骨架，列出所有叶节点；任何未覆盖叶节点即为 `MINIMAL_SELECTOR_GAP`。
3. 优先解决 O2、O3 和 handoff 后的 Type-I continuation；每解决一项立即补 claim、verifier、tests、taxonomy 和状态合同。
4. 对每条新边做 adversarial audit：检查 provenance、support consumption、target normal form、全域 lift、rank ticket、recursive reachability 和 terminal-first 顺序。
5. 在所有 family 都有 total exit 后，冻结 selector 的确定性优先级。多个 witness 可用时，定义只读取 state 数据的 canonical choice，例如对已证明非空且可有效枚举的 witness 集取字典序最小者，并证明搜索必停。
6. 证明 selector totality、successor closure 和 T5 强归纳终止；再进行一次与实现作者分离的独立审计。
7. 最后才同步 README、flagship program、state contract、T5 integration、taxonomy、theorem ledger、T6 status page 和 CI。

## 必须交付的仓库产物

文件名可按仓库惯例调整，但功能上必须包含：

- T6 global-selector totality 的主 claim，写出完整量词和证明；
- reachable-state exhaustion claim；
- QC1 或 TR1 的闭合 claim；
- C8 outgoing-existence claim；
- 确定性 selector contract、实现和稳定 serialization；
- machine-readable selector taxonomy/obligation ledger；
- 每个新全称引理的 focused verifier 与 unittest；
- 全局 selector verifier，逐 family 检查 E1–E5、target closure 和 T5 ticket；
- 终止性/强归纳整合证明；
- 独立 closure audit，明确列出所有量词及证据；
- README、concepts、docs、theorem ledger、source metadata 和 CI 的一致更新；
- 可重放的冻结证明包及 SHA-256。

所有 controls 必须标明 `actual`、`conditional_adapter_control` 或 `analysis_only`。不得让 synthetic control 冒充 actual reachable receipt。

## 验收门

只有以下各项全部为真，才允许写 `T6_GLOBAL_SELECTOR_TOTALITY = ESTABLISHED`：

- [ ] 对每个核心 prime 的合法初始状态有证明和 serializer。
- [ ] 全局 reachable-state case split 已证明穷尽，且不依赖当前 named-edge closed world 的循环假设。
- [ ] 每个非终端叶节点都有全称 terminal、family-empty proof 或完整 E1–E5 successor。
- [ ] QC1 或 TR1 已在 actual proper-root `k>1` 全域闭合。
- [ ] C8 已在全部 actual terminal-first-surviving parents 上闭合。
- [ ] ordinary q=1/positive-q G handoff 后的 Type-I 路径递归 total。
- [ ] 新 atomic/marked family 的 T2/T3 义务已关闭，或对最终 selector graph 严格证明不可达。
- [ ] selector 是确定、可计算、无需未知解 oracle，并对自己的所有 successor 继续有定义。
- [ ] 每条 recursive edge 都逐项通过 E1、E2、E3、E4、E5；E4 是全域 lift。
- [ ] 每条 edge 的实际七元 T5 势严格下降，且强归纳终止证明完成。
- [ ] terminal 输出均可直接核验并正确 lift 回原始 \(4/p\) 目标。
- [ ] 没有 `OPEN`、`pending`、`analysis_evidence` 或仅 finite-control 的项被纳入 closure theorem。
- [ ] 文档、claims、taxonomy、ledger、tests 和 CI 对状态的表述一致。
- [ ] 独立审计没有 blocking issue。

最低验证命令包括：

```bash
python3 scripts/kb.py validate
python3 scripts/kb.py build
python3 reproductions/type_i_t5_transition_surface_audit.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 <新增的每个 focused verifier> --verify
python3 <T6 global selector verifier> --verify
git diff --check
```

对本任务新增/修改的 Python 文件运行 Ruff 和 `py_compile`。把 T6 verifiers 纳入启用且可复现的 CI；依赖要固定或有明确兼容范围。不得用跳过测试、降低断言、删除 negative controls 或缩窄量词来获得绿灯。

## 最终报告格式

最终报告必须按以下顺序给出：

1. 精确结论：`ESTABLISHED`、`OPEN` 或 `REFUTED`；
2. 主定理及量词；
3. obligation ledger，逐项说明如何关闭；
4. selector 的确定性规则；
5. E1–E5 与 T5 下降的全局证明链；
6. 运行过的验证及结果；
7. 变更文件和提交；
8. 仍然开放的内容。

如果任一验收门未通过，结论必须保持 `OPEN`，并把剩余问题压缩成最小、可判真假的量词；不要用“基本完成”“数值上成立”或“只剩工程工作”代替证明。

## 工作原则

持续推进实现、证明、反例搜索和审计，不要在每个小步骤等待确认。可以用并行研究或独立审阅提高效率，但最终主代理必须逐条复核数学推导、状态合同和代码。优先提交小而可重放的闭合引理；任何时候都以证据边界为准，不以目标措辞为由制造过度声明。
