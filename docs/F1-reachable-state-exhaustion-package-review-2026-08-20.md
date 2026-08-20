# F1 reachable-state exhaustion 包复核（2026-08-20）

> 输入包：[`../archive/proof-packages/raw/erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip`](../archive/proof-packages/raw/erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip)
> 输入 SHA-256：`2a7d2744cf72c23fa163c9f75979cd4eb7e92dd9c69b7a74430fa9c6c062eb0c`
> 声明基线：`d3b3b6a39595d9fdc369a8648e821294a19e04c1`
> 处置：`NOT_ADMITTED_AS_F1_CLOSURE`
> 规范状态：`T6-F1-REACHABLE-STATE-EXHAUSTION = OPEN`
> 归档：[`archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/`](archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/)

## 1. 输入完整性与审查范围

包内 `SHA256SUMS` 对其列出的 payload 全部通过，且 ZIP 容器通过完整性检查。该结果只说明
输入字节完整，不能证明其中的 F1 数学或合同结论。

本复核只判断包中下列声称能否接入当前仓库的规范 frontier：

```text
T6-F1-REACHABLE-STATE-EXHAUSTION = CLOSED_CONTRACT_LEVEL
```

包正确保留了 `F2`、`F3` 和 `T6` 为开放状态；争议不在于它是否错误宣布了猜想成立，
而在于它是否已经证明当前合同下的 F1 classification quantifier。

## 2. 接纳的内容

下列区分是正确且应保留的：

\[
\text{O1}=
\text{reachable-state classification}
\land
\text{classified-family exit totality}.
\]

后者仍由 `T6-F2` 与 `T6-F3` 处理，不能从 T5 的逐边严格下降推出。包给出的重开条件也
是有用的设计约束：新增 persistent constructor、改变 target family、让 raw/pending/analysis
artifact 获得递归资格、或改变 normalizer precedence 时，都必须重新检查 F1。

这些内容与现有 [T6 证明边界](T6-proof-boundary-2026-08-20.md) 的 F1--F3 分工一致，
但不需要把 F1 状态升级为已闭合。

## 3. 不接纳 F1 闭合的原因

### 3.1 定义循环而非独立总性证明

包把一个 `legal persistent selector state` 定义为已经满足：

1. `normalize_selector_family_v1` 已经返回唯一 owner；
2. `selector_family_owner_digest` 已经验证。

其主结论再断言每个这样的 state 都有唯一 owner。因此该定义本身预先排除了 normalizer
失败或未分类 target，不能证明对独立给定的 E3 legal target 的 normalizer 总性。first-match
只在至少一个 predicate 已命中时给出唯一性；它不能证明所有允许 header 至少命中一个 predicate。

### 3.2 所需合同接口并未进入当前仓库

当前 [状态合同](../concepts/denominator-escape-state-contract.md) 的 T5 准入规则要求 E1--E5
和 ticket，constructor admission firewall 要求 future constructor 注册与审查；但它尚未定义或
实现包所依赖的：

- `extract_verified_selector_header_v1`；
- `normalize_selector_family_v1` 的输入字段、16 个实际 predicate 及 residual proof；
- `selector_family_owner_digest`；
- 两个唯一 persistent enqueue gate；
- `reject_before_persistent_queue` 的可重放 serializer 行为。

所以包的 manifest 与 audit 不能反证当前合同中某个合法 E3 target 会落在这 16 个 family
之外。先把 classification 成功列为准入前提，再据此证明已分类，不满足 F1 所要求的独立
constructor induction。

### 3.3 producer 穷尽只是假设冻结 registry

包把 producer 集预设为 M0 root serializer 加 15 个已登记 edge。当前 F1 的最低验收条件明确
要求从全部 legal state constructor 与 successor serializer 出发，独立证明 H4、atomic、overflow、
post-G、marked 和 raw 输出没有漏项，而不是从 registry 的 15 项倒推语义可达域。

admission firewall 能拒绝未来未注册 constructor；它不能单独证明当前所有实际 constructor
已经被发现、被建模，或其所有 target guard 已完成分类。这个差别正是 F1 尚开放的量词。

### 3.4 包内测试不验证上述缺口

包的 audit 只检查自身 JSON 是否仍等于写死的常量。其 mutation tests 对复制出的 manifest
改变字段后直接断言该字段不等于旧值，没有把修改后的对象传回 audit，也没有读取当前
`data/t6-proof-frontier-v2.json`、state contract 或实际 claim/serializer。它们因此能发现
package 文件被静态改写，却不能验证 producer 穷尽、normalizer 总性或 target re-entry。

此外，交付 patch 把当前仓库的 `README.md` 作为 `/dev/null` 新文件创建，`git apply --check`
在真实基线失败；它没有修改上述所需合同接口。故该 patch 不能作为本仓库 F1 定理的实现。

### 3.5 解压主证明的逐项裁定

下表复查解压材料
[`archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/payload/erdos-straus-f1/docs/F1-reachable-state-exhaustion-closure-2026-08-20.md`](archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/payload/erdos-straus-f1/docs/F1-reachable-state-exhaustion-closure-2026-08-20.md)
的各个证明单元，而不是只检查其 manifest 的自洽性。

| 包内单元 | 裁定 | 原因与可保留内容 |
|---|---|---|
| 第 1 节 state / `Reach_p` 定义 | 不可作为 F1 前提 | `legal persistent selector state` 已要求 normalizer 返回 owner 与 digest 验证；因此它把未分类 E3 target 排除在论域外。 |
| F1-L1 producer exhaustion | 未建立 | M3 firewall 是对未来合并的 fail-closed 政策，不是当前全部 constructor 与 successor serializer 的独立枚举。 |
| F1-L2 nonpersistent isolation | 仅条件性成立 | 若两个实际 enqueue gate、artifact tag 与 receipt schema 已被定义并强制，则隔离结论成立；当前合同尚无该完整机制。 |
| F1-L3 verified-header extraction | 未构造 | 包只有函数名和输入意图，没有 header schema、extractor、异常/拒绝语义或对所有 E3 target 的总性证明。 |
| F1-L4 normalizer totality | 未建立 | 16 个 owner 名称不是 16 个谓词；包没有给出 `V_i`、guard partition 或 residual branch 的全称覆盖证明。 |
| F1-L5 first-match uniqueness | 条件性正确 | 一旦已知集合 `A_S = {i : V_i(S)}` 非空，最小下标规则确实给出唯一 owner。这是可复用的组合引理，不是 totality。 |
| F1-L6 target re-entry | 未建立 | admission 在写队列前要求 normalizer 成功，因而只能得到“已经分类的 target 重新分类成功”，不能排除未知 target。 |
| 第 8 节 trace induction | 仅加强合同下有效 | 归纳步骤依赖 L1、L3、L4、L6；在这些作为公理的封闭队列模型中形式上无误，但没有从 actual legal successor 到该模型的桥梁。 |
| 第 10、12 节 | 接纳为项目组织结论 | O1 分解、F1 与 F2/F3 的边界、以及新增 constructor 必须重开 F1，均可作为后续证明的治理规则。 |

因此，包中真正已证明的数学核最多是条件性组合命题

\[
A_S\ne\varnothing
\quad\Longrightarrow\quad
\exists!j=\min A_S,
\]

而 F1 所需的非平凡方向是对每个独立产生的 legal E3 target 证明
\(A_S\ne\varnothing\)。该方向未在包内给出。

## 4. 规范处置、归档及后续可接纳形式

本包不作为 `t6-proof-frontier-v3.json`、`f1-reachable-state-exhaustion-v1.json` 或 F1 closure
claim 合入。现有 `data/t6-proof-frontier-v2.json` 保持 F1 为 `OPEN`，且不删除任何 active gap。

原始 ZIP 已作为字节级证据保留在
[`../archive/proof-packages/raw/erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip`](../archive/proof-packages/raw/erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip)；
完整解压的可检索源码视图和输入完整性说明在
[`archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/`](archive/proof-packages/f1-reachable-state-exhaustion-all-outputs-2026-08-20/)。
归档进入项目历史并不等于接纳其 theorem status；规范进展仍以本报告、
[T6 证明边界](T6-proof-boundary-2026-08-20.md) 和根目录 README 为准。

未来若要将 F1 降为真正的 `CLOSED_CONTRACT_LEVEL`，至少需要：

1. 在状态合同中先于 F1 结论定义 persistent queue、header extraction、family predicates、
   owner digest 和 reject path，且 legal state 的定义不得预设 normalizer 成功；
2. 对每个已存在 constructor/serializer 给出独立 guard partition，并证明其 nonterminal E3 target
   经 extractor 后至少命中一个 family；
3. 用 current registry 与实际 constructor 交叉检查 producer 穷尽，而非由 15 个名称构造前提；
4. 对 malformed header、unknown target、overlapping predicates、empty residual 和新增 constructor
   写 focused negative controls；
5. 证明每个 admitted target 的重新分类，再把该证明接入 F1 trace induction。

在这些条件满足前，包中关于 queue、first-match 和 re-entry 的材料只能作为 `F1_CONTRACT_CANDIDATE`
设计笔记，而不是可递归使用的闭合引理。
