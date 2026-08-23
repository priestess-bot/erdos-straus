# T6 constructor inventory v1：活动源码与活动 data 的双向清单

日期：2026-08-23

基线：`c851bd213936b3bc8b3103b469292c139d229e97`
结论：`STRUCTURALLY_AUDITED_F1_OPEN`

## 1. 本审计回答什么

本审计只做 A0：从活动源码独立发现可能产生递归状态的实现信号，再与活动
`t6-proof-frontier-v2.json`、`t6-selector-obligation-ledger-v1.json` 双向比较。它不把
“两个 registry 都有 15 条边”当作源码完备性证明，也不把归档包当作活动实现。

机器清单为
[`data/t6-constructor-inventory-v1.json`](../../data/t6-constructor-inventory-v1.json)，
独立审计入口为
[`scripts/audit_t6_constructor_inventory_v1.py`](../../scripts/audit_t6_constructor_inventory_v1.py)。

活动源码侧采用保守语法信号：

1. `recursive_edge_eligible` 的值不是字面 `False`；
2. 函数接受 `persistent_queue` 参数；
3. 调用点向 `persistent_queue` 传入非 `False` 值；
4. 另行扫描真实 `enqueue`、`put`、`put_nowait` queue mutation call。

这不是语义完备的 constructor marker。它的用途是 fail closed：新增这类信号而未更新
inventory 时，审计立即失败。由于仓库尚无统一 constructor protocol，A0 不能据此证明
所有数学 constructor 都被发现。

## 2. 三个必须分开的集合

### 2.1 冻结 data surface

活动 data 声明：一个 initializer、16 个 family、15 个 registered edge。frontier 与 ledger
的 edge ID、source/target family、guard class 当前逐项一致。这个结论只是 data-to-data
一致性，不是 source completeness。

### 2.2 活动实现 surface

15 个 registered edge 都能找到至少一个活动 Python 文件与顶层符号，但实现强度差异很大：

| 条目 | 主符号 | 实现层级 | 实际 enqueue |
|---|---|---|---|
| initializer | `initial_dispatch` | root terminal/edge receipt builder | 无 |
| proper endpoint | `proper_endpoint_dispatch` | conditional receipt builder | 无 |
| gcd-shadow endpoint | `gcd_shadow_dispatch` | receipt builder | 无 |
| q=1 G handoff | `phase_root_entry` | content-addressed local receipt | 无 |
| positive-q G handoff | `phase_root_entry` | conditional control，明确不可递归 | 无 |
| c=3 lineage relay | `phase_relay` | conditional typed-fiber receipt | 无 |
| second-anchor macro | `odd_macro` / `even_macro` | family-formula receipt | 无 |
| same-chart promotion | `overflow_same_chart_support_promotion` | fixture-atlas receipt | 无 |
| joined-support reset | `overflow_outer_rank_reset` | fixture-atlas receipt | 无 |
| A=1 dual reset | `overflow_a_one_dual_reset_family` | fixture-atlas receipt | 无 |
| high-carrier fixed-n | `overflow_fixed_n_bounded_divisor_outer_rank` | fixture-atlas receipt | 无 |
| high-support sink | `verify_rank_aware_selector` | focused p=73 control | 无 |
| q=1 d=1 relay | `complete_excess_relay` | fixed-fixture receipt | 无 |
| C=2 three-anchor macro | `macro_data` | arithmetic fields only | 无 |
| H4 atomic macro | `derive_local_suffix` | terminal-preempted conditional suffix control | 无 |
| c=8 atomic macro | `suffix_capacity_data` | conditional interface control | 无 |

因此“有 verifier symbol”不等于“有 constructor runtime”。尤其：

- positive-q control 自己写明 actual source receipt 与 terminal-first receipt 均未供应，
  `recursive_edge_eligible=False`；
- C=2 `macro_data` 只返回容量与 `R_3`，没有 source state、target state 或 serializer；H3
  在现有 taxonomy 中只能落到 nonrecursive `pending_dispatch`；
- H4 的两个活动 control 都先被 direct terminal 抢占，没有演示 pending target 序列化；
- c=8 control 没有命中 double-low guard，因此没有构造 atomic target；
- 多个 overflow builder 只输出各自的 minimal descriptor，不共享一个可重入 schema。

### 2.3 真正的 queue/admission surface

没有发现活动 `enqueue`、`put` 或 `put_nowait` queue mutation call。也没有统一的：

- `PersistentSelectorStateV1`；
- canonical header extractor；
- target normalizer/reclassifier；
- global enqueue firewall；
- constructor registration marker。

`type_i_overflow_total_cofactor_typed_adapter.py` 看似最接近 admission：它的
`registration(..., persistent_queue=True)` 能让 `verify_transition` 返回
`relative_verified_edge`。但 `True` 只在该文件的 `verify()` fixtures 中人工传入；没有活动
upstream enqueue producer，也没有 frozen 15-edge registry 对应项。该 adapter 因而在清单中是
`UNREGISTERED_RELATIVE_ADAPTER_INPUT`，owner、constructor mapping 与 enqueue gate 均为
`UNASSIGNED`，不能静默并入某条 registered edge。

## 3. 源码侧多出的信号

AST census 得到 18 个保守信号。9 个不能作为已登记 constructor 关闭：

1. total-cofactor adapter 的 `persistent_queue` 参数；
2. total-cofactor fixtures 对该参数传入 `True`；
3. `overflow_fixed_n_outer_rank`；
4. `overflow_fixed_s_bounded_divisor_outer_rank`；
5. `overflow_fixed_s_outer_rank`；
6. `smooth23_k_one_fixed_n_saturation`；
7. `smooth23_low_k_fixed_n_cofactor`；
8. `verified_fixed_n_edge`；
9. H4 clean-q verifier 对 `recursive_edge_eligible` 的未解析传播。

其中 `verified_fixed_n_edge` 给出一个特别清楚的最小断点：控制项把

\[
(p,R,K,A)=(409,11,1125,125)
\]

标为 `recursive_edge_eligible=true`，但没有 parent registration、terminal-first digest 或 enqueue
provenance；同时 receipt 的 overflow phase/state label 与 `R<p` 不相容。它可以作为算术 identity
control，不能作为合法持久 successor。

另有两个 high-R `same_chart_parent_replay` 是已登记 same-chart edge 的独立实现别名；它们不增加
registry edge 数，但进一步说明“一个 registry ID 对应一个实现符号”并不成立。

## 4. E3、T2/T3 与 owner 边界

每个 inventory entry 都记录了 source family、terminal-first 状态、observed target schema、E3
前置条件、owner 与 T2/T3 coverage。当前结论是：

- owner 在 data 层可由 source family 读出，但没有 runtime classifier 实际重算 owner；
- H4、c=8 在 data 层指向 `t2_v1_atomic_pending_target`，因而分别绑定 `T2v1_A_H4`、
  `T2v1_A_C8`；它们的非终止 target serializer 仍缺失；
- T3v1 只证明 frozen registered graph 没有 nontrivial-mark target；源码多出的 eligible producer
  在登记以前不能借用该结论；
- 没有任何条目已经展示“target -> 同一 extractor -> family predicate -> owner -> enqueue”的完整链。

## 5. 精确结论

本次 A0 已经建立的是一个忠实、可变异、fail-closed 的 inventory baseline：活动 data 漂移、活动
source signal 漂移、缺失实现符号、archive 污染、atomic target 缺 T2、marked target 缺 T3 都会被
审计器拒绝。

本次没有建立：

- source semantic completeness；
- 所有真实 enqueue gate 已发现；
- 所有 target 具有共同 E3 normal form；
- target re-entry；
- family totality / uniqueness；
- F1、F2、F3、T6 或 Erdos-Straus 猜想闭合。

因此当前合法状态仍是：

```text
inventory structural audit = PASS
closure_ready              = false
F1 reachable exhaustion    = OPEN
T6 global selector         = OPEN
```

下一条最小工作不是增加 registry 条目数，而是先在 A1 建立非循环的持久状态 header、真实 extractor
与唯一 admission/enqueue gate；随后逐条把现有 receipt builder 接到这个接口。只有所有源码信号都
有明确 disposition，且所有非终止 target 实际重入同一分类域，A0 的 unknown 才可能归零。

## 6. 复现

```bash
python3 scripts/audit_t6_constructor_inventory_v1.py
python3 scripts/audit_t6_constructor_inventory_v1.py --require-closure-ready
python3 -m unittest tests.test_t6_constructor_inventory_v1 -v
```

第一条应结构通过并报告 `closure_ready=false`；第二条应以退出码 2 fail closed，而不是错误升级
F1；第三条只检查本 A0 接口及少量关键变异，不承担全仓历史审计。
