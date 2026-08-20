# T6 之前的合同内核闭包（2026-08-20）

> 基线提交：`ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0`
> 结论：`T1v1--T5v1 = CLOSED_WITH_EXPLICIT_SCOPE`。
> 非结论：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`，`F0 = OPEN`，Erdős--Straus 猜想仍开放。

## 1. 本次修复的问题

此前文档同时使用 `T1`、`T2`、`T3` 表示两种不同强度的命题：一方面是已经有证明包的
有限或相对命题，另一方面是对所有未来 H4、atomic 或 marked 构造器的强全称版本。相同
编号承载不同量词会产生三类错误：

1. 把“在书面 guard 下有一条合法相对边”误读成“整个 family 已有 total selector”；
2. 把“当前具名图没有 mark seed”误读成“任意未来 marked state 都已闭合”；
3. 把 T2 的有限 receipt grammar 误读成所有 raw path 的全域 atomic admission。

本次把 T6 之前真正已经完成的内核冻结为 `T1v1--T5v1`。历史强版本记为
`T1*--T3*`，不再作为含糊的“半闭合前置层”；它们尚未覆盖的实际状态全部由 T6 的
可达性和 family-totality 量词接管。机器可读事实源为：

- `data/pre-t6-contract-kernel-v1.json`；
- `data/t6-proof-frontier-v2.json`；
- `reproductions/pre_t6_contract_kernel_audit.py`。

这是一项量词和合同闭包，不是通过改名消除数学缺口。任何尚未证明存在 successor 的状态
仍保持为 T6 的 `OPEN` family。

## 2. 冻结内核

### 2.1 T1v1：H4 clean-\(q\)、\(a_{\rm alt}=1\) 的相对宏闭包

**精确输入域。** 输入必须是一个 actual、parent-anchored、proper-overlap、top-capacity
H4 receipt，满足 `a_alt=1`，并已经携带可重放的 upstream provenance 和 terminal-priority
miss。

**已闭合结论。** 在该 guard 下，clean-\(q\) macro 给出书面声明的 phase-local
terminal，或给出满足该局部 claim 的 E1--E5 candidate transition。该 candidate 经 T2v1 的
normal-form/state admission 与 T5v1 的 ticket 接口组合后，是冻结 v1 图中的 contract-admitted
局部边；这不增加其它 H4 branch 或 target descendant 的存在量词。

**不包含。** 其它 H4 selector branch、该 target 之后的 total continuation、所有 H4
后继的全局 admission 都不属于 T1v1。它们归入 `T6-F2-NONPROPER-DISPATCH-TOTALITY`。

### 2.2 T2v1：有限 atomic receipt grammar

冻结 atomic surface

\[
\mathcal A_{v1}=\mathcal A_{H4,a=1}\sqcup\mathcal A_{C8,\mathrm{double\mbox{-}low}}.
\]

T2v1 证明这两个具名 arm 有确定的 receipt grammar：H4 arm 是 actual，c=8 arm 是在
qualifying double-low receipt 已经给定时的 conditional arm。grammar 的有限性、字段类型、
owner/scope 和可重放入口由已有 claim/verifier 负责。

T2v1 不证明：

- 每个 c=8 parent 都产生 double-low receipt；
- 每条 raw H4 path 都进入 `a=1` arm；
- 未来新增的 atomic constructor 自动获准。

因此 `T2*` 的全域量词没有被宣称为已证。未覆盖 parent 的 outgoing totality 属于 T6-F2；
未来 constructor 受第 4 节 admission firewall 约束。

### 2.3 T3v1：冻结具名图中的 nontrivial mark 不可达

这是一个可以完整闭合的 closed-world 图不变量。其证明只使用冻结清单，不使用“taxonomy
看起来穷尽”这样的语义假设。

**基例。** 初始 serializer 的根标记为

\[
W_0=\operatorname{Sol}(p).
\]

它只输出 `type_ii_relation_g_endpoint` 或 `direct_terminal_leaf`，不生成
`generic_nontrivial_marked_state`。

**归纳步。** `data/t6-proof-frontier-v2.json` 登记的 15 个 edge generator 中，每个
`source_family_ids` 和 `target_family_ids` 都属于冻结的 16 个 family；没有任何 target 是
`generic_nontrivial_marked_state`。ordinary G handoff 使用
\(W_S=W_T=\operatorname{Sol}(p)\) 的恒等 lift。直接 terminal 关闭根证书分支，不创建递归
后继。

**结论。** 对“由该 initializer 和这 15 个 edge generator 生成的有限语法图”作路径长度
归纳，nontrivial marked family 不可达。

该定理不证明 actual semantic reachable set 已被这张图穷尽，也不证明未来 mark 的抽象
membership theorem。任何拟新增的 marked target 会被 CI 拒绝，并自动重开 T3/T6 义务。

### 2.4 T4v1：ordinary \(q\ge 1\) G fresh-source handoff

对 actual、terminal-first-surviving、ordinary G endpoint，且当前 mark 为
\(\operatorname{Sol}(p)\)，已有 q=1 和 positive-q 两个 receipt adapter。它们进入同一个
与未知 target 无关的 full-carrier Type I fresh root，并登记书面 guard 下的首条严格局部
segment。

T4v1 关闭 handoff 的 E1--E5 相对合法性；它不关闭 handoff 之后的 Type I 子树，也不处理
nontrivial mark。后继 totality 由 T6-F2 负责。

### 2.5 T5v1：合同认可边的 \(\mathbb N^7\) 良基性

设合同认可的固定势为

\[
\Pi_{T5}(S)=(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4)\in\mathbb N^7.
\]

T5v1 的精确结论是

\[
\operatorname{verified\_edge}(S,T)
\Longrightarrow
\Pi_{T5}(T)<_{\mathrm{lex}}\Pi_{T5}(S),
\]

其中一条边只有携带 `OUTER_RANK_DROP`、`PHASE_DROP` 或 `LOCAL_DROP` 才可进入
`verified_edge` registry。因而合同认可图不存在无限下降路径。

T5v1 不提供以下存在量词：

\[
S\text{ 非终端}\Longrightarrow \exists T\;\operatorname{verified\_edge}(S,T).
\]

这个存在量词正是 T6，而不是 T5 的推论。

## 3. 历史强版本的处置

| 历史强版本 | 当前处置 | 精确 owner |
|---|---|---|
| `T1*`：所有 H4 branch 和 descendants | 研究扩展；不属于已闭合内核 | `T6-F2` |
| `T2*`：所有 actual raw path 和所有未来 atomic surface | 研究扩展；不属于已闭合内核 | `T6-F1` 与 `T6-F2` |
| `T3*`：任意未来 nontrivial mark 的抽象 membership/lift | 研究扩展；默认禁止进入冻结图 | constructor admission firewall |

这样处理后，T6 之前不存在状态为“既闭合又全域开放”的同名命题。已有证明保留，未证量词
不被抹去，而是进入唯一的 T6 frontier owner。

## 4. constructor admission firewall

`GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY` 对冻结 v1 不再是一个需要等待数学突破的开放状态，
而被改写为可执行的准入规则：

任何新增 constructor 或 edge，只要产生新的 atomic family 或 nontrivial marked family，
合并前必须同时完成：

1. 注册 source family 与 target family；
2. 视情况扩展 T2 或 T3；
3. 给出 serializer、normal form、scope/owner 和 lift；
4. 为该 family 指派一个 T6 frontier obligation，或直接给出 family-empty/terminal/verified
   successor 闭包；
5. 通过结构审计和测试。

不满足这些条件的变更不是“暂时进入图再以后补证明”，而是直接拒绝 admission。该闭包只对
冻结 v1 有效；一旦新增构造器，O4 自动重开。

## 5. q=1 冻结包的 provenance 修复

既有 q=1 handoff archive 的内部 `SHA256SUMS` 包含自身，因此自指条目不可能作为同一文件
内容的普通 SHA-256 固定点；原审计也已经记录该条目不匹配。此后采用以下证据层级：

1. 外层 archive SHA-256 固定归档字节；
2. ZIP 完整性测试固定容器可读性；
3. detached payload digest 或逐 payload digest 固定包内实质文件；
4. 内部 manifest 的非自指 payload 条目可作辅助交叉检查；
5. 内部 manifest 的 self-hash 明确标记为 non-authoritative，不再出现“内部 manifest 全部
   通过”的表述。

这是 provenance 闭包，不改变 T4v1 的数学范围。

## 6. 机械闭包与审计

本次新增审计固定并核对：

- 同一完整 40 位 baseline SHA；
- 恰好 `T1v1--T5v1` 五个 scoped kernel theorem；
- 16 个具名 state family；
- 15 个既有 edge generator 的 source/target/guard 与 v1 ledger 一致；
- initializer 和所有 edge 均不生成 nontrivial mark；
- 8 个 active mathematical legacy gap 恰好各有一个 F1--F3 owner；
- O4 只以 frozen-v1 firewall 方式关闭；
- 所有 \(m=3,q=5\) 新结论保持 `ESTABLISHED_ARITHMETIC_ONLY`，不得升级为 edge；
- T6、F0 和猜想状态必须保持 `OPEN`。

复现命令：

```bash
python reproductions/pre_t6_contract_kernel_audit.py --root .
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
```

在完整 checkout 中还应运行：

```bash
python scripts/kb.py validate
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
```

## 7. 闭包后的唯一边界

T6 之前的可用前提现在是一个明确的条件内核：

\[
\boxed{
T1v1+T2v1+T3v1+T4v1+T5v1
}
\]

它允许 T6 直接使用已有相对宏、有限 atomic grammar、当前图 mark invariant、fresh handoff
和固定良基势。它不允许 T6 假设 reachable-state exhaustion、post-handoff totality、所有 H4
或 c=8 parent 的出口，以及 proper-root \(k>1\) 的 physical edge。后者全部列在
`docs/T6-proof-boundary-2026-08-20.md`。
