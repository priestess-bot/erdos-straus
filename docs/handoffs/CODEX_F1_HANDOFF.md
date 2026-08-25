# Codex F1 handoff：可达状态闭世界的非循环合同与最小阻断项

## BASELINE

- Base commit: `c851bd213936b3bc8b3103b469292c139d229e97`
- Branch: `codex/f1-reachability-contract`
- Result date: `2026-08-23`
- Result commit: 见本分支本轮提交；本文件在提交前生成，不用自引用 SHA 充当证明。

## CLAIMED RESULT

- Exact result: 建立了不预设 owner/normal form 的 `PersistentSelectorStateV1` header、
  独立 family predicates、固定 precedence、owner digest、两类 queue gate 和 fail-closed
  admission；同时从活动源码重建 constructor/serializer 信号清单，并对 initializer 给出
  terminal/G 符号分区。
- Quantifier domain: 送入新 admission API 的 v1 header，以及满足 B（initializer 接入）、
  S（逐 constructor 重入）和 X（无 queue 旁路）三个外部前提的有限 persistent trace。
- Status: `OPEN_MINIMAL_GAPS`。

这次结果修复了旧 F1 包的定义循环，但没有证明 B、S、X。当前已有一个仅覆盖 q=1
局部路径的 selector runtime 和 queue mutation；全局 persistent queue/re-entry 仍未证明。
18 个源码递归语义信号中有 4 个 unresolved disposition，另有 9 个被明确标成 nonruntime
controls。
因此没有发布 F1 grammar freeze，F1、F2、F3、F4、F5、T6 和猜想状态均不升级。

## EVIDENCE

- Claim: `claims/t6-f1-reachable-state-closed-world-v1.md`
- Concept: `concepts/t6-persistent-selector-state-v1.md`
- Inventory: `data/t6-constructor-inventory-v1.json`
- Proof receipt: `data/t6-f1-reachability-proof-receipt-v1.json`
- Source/data audit: `docs/audits/T6_CONSTRUCTOR_INVENTORY_V1.md`
- Inventory verifier: `scripts/audit_t6_constructor_inventory_v1.py`
- Admission kernel: `scripts/t6_persistent_selector_state_v1.py`
- Focused tests: `tests/test_t6_constructor_inventory_v1.py`,
  `tests/test_t6_persistent_selector_state_v1.py`,
  `tests/test_t6_f1_negative_controls_v1.py`

## ESTABLISHED LEMMAS

1. Header extraction does not call a family predicate or consume owner/normalizer caches. An extracted
   header may still fail with `FAMILY_NO_MATCH`.
2. A nonempty family-hit set with only declared overlaps has a unique owner under fixed precedence.
3. Inputs that actually enter the new gate fail closed on unknown schema, producer, branch, target,
   malformed receipt, zero hit, illegal overlap or invalid ticket.
4. The root initializer has a symbolic, exhaustive terminal/G partition; its G target has the declared
   full-carrier chart and unique candidate owner.
5. Under B, S and X, path-length induction gives unique ownership for every admitted trace state.

## MINIMAL FAILURES

1. `type_i_overflow_total_cofactor_typed_adapter.py` can be fed a fixture-manufactured
   `persistent_queue=True` and return `relative_verified_edge`, but it has no upstream enqueue producer
   or frozen registry mapping. The new gate correctly rejects it as `UNKNOWN_PRODUCER`.
2. `verified_fixed_n_edge` self-reports a recursive output at
   `(p,R,K,A)=(409,11,1125,125)` without parent registration, terminal-first digest or enqueue
   provenance; its overflow label is also incompatible with `R<p`.
3. The C=2 macro reaches symbolic `H_3`, but the active implementation returns only arithmetic fields.
   The taxonomy leaves it at nonrecursive `pending_dispatch`; no persistent serializer re-enters F1.
4. The earliest root path already breaks the required runtime induction: the q=1 full-carrier
   `first_type_i_step` is a rail dictionary, and the second-anchor macro reconstructs a parent from
   `prime` rather than consuming a commonly serialized predecessor.

## ACCEPTANCE MATRIX

| Criterion | Verdict | Evidence |
|---|---|---|
| inventory 双向一致且未知项为零 | **FAIL** | data surface 双向一致；仍有 4 个 unresolved signals |
| 合法状态不依赖 normalizer/owner | **PASS** | noncircular extractor and zero-hit control |
| 所有真实 enqueue gates 已发现 | **FAIL** | 已发现一个局部 runtime queue anchor，但无法证明全局无旁路 |
| 每个 constructor 有完整 guard partition | **FAIL** | 仅 initializer 完整；其余 15 项缺共同 serializer/partition |
| 所有 nonterminal target 可由 extractor 重分类 | **FAIL** | C=2/H4/c=8/overflow 等没有统一 target projection |
| 固定 precedence 下 owner 唯一 | **PASS, conditional** | nonempty legal hit-set theorem |
| 未知/未登记状态在 queue 前失败 | **PASS, inside gate** | stable reason-code tests；不证明所有旧路径调用 gate |
| 迹归纳含 initializer 与 successor | **PASS, conditional** | B/S/X induction kernel；B/S/X 尚未接入 |
| 负控触发预期失败 | **PASS** | 13 个指定 mutation classes |
| 未修改 `archive/` | **PASS** | 本分支无 archive 修改 |
| 未升级 F2/F3/F4/F5/T6/猜想 | **PASS** | claim 和 receipt 均保持 OPEN |
| 全部要求的仓库命令 | **PASS** | KB、pre-T6 audit、1143 项 unittest 与 diff-check 均通过 |
| handoff 列明命题、依赖、非结论和下一定理 | **PASS** | 本文件 |

## NON-RESULTS

- 没有证明活动 constructor 集在语义上穷尽。
- 没有证明现有 15 个 registry row 都是 executable persistent producers。
- 没有证明所有历史 serializer 必经新 gate。
- 没有证明每个 E3 target 至少命中一个 family。
- 没有发布可供 F3 集成的 grammar hash/freeze。
- 没有证明任何 F2/F3 family totality、T6 或 Erdős--Straus 猜想。

## RESIDUALS

- Smallest remaining quantified gap: 对每个活动 source signal 给出唯一 disposition，并对每个
  登记 producer 的全部 source guards 证明 terminal/reject/nonterminal 互斥穷尽；每个
  nonterminal target 必须由同一 serializer 投影并实际通过新 gate。
- Next theorem: `Producer Projection and Exclusive Admission Theorem v1`。
- Grammar freeze: `BLOCKED_NOT_PUBLISHED`，直到 inventory unknown 为零且 B/S/X 全部成立。

## VALIDATION

本轮只运行新增接口的 focused checks 和目标文档要求的一次最终验收；没有重复压力扫描。

```text
python3 scripts/audit_t6_constructor_inventory_v1.py                       PASS
python3 -m unittest <three focused F1 modules> -v                          39/39 PASS
python3 -m py_compile <modified Python files>                              PASS
python3 scripts/kb.py validate                                             PASS (1394 docs)
python3 scripts/kb.py build                                                PASS
python3 reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
                                                                             PASS
python3 -m unittest tests.test_pre_t6_contract_kernel_audit -v             16/16 PASS
python3 -m unittest discover -s tests -p 'test_*.py'                        1143/1143 PASS
git diff --check                                                           PASS
```

## INTEGRATION NOTES

- Shared frontier/README/T6 status: 未修改。
- New constructors/families: 无；新合同只定义候选 admission API。
- Firewall implication: 它能拒绝送入 API 的未知对象，但在 runtime 接线完成前不能宣称
  `all writes pass firewall`。
- F3 implication: 由于 grammar freeze 未发布，F3 新 target 只能保留为 candidate receipt，
  不得登记活动边。
