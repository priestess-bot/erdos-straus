# H4 Closure Release Audit (2026-08-17)

## 原始来源

本次归档的来源包为
[`h4_closure_release_2026-08-17.zip`](h4_closure_release_2026-08-17.zip)，其 SHA-256 为：

```text
625ed074b82ce51c38916523128058c513faa3bafc4eb6fde1876a8882594692
```

已执行 `unzip -t`，并在解包根目录执行 `sha256sum -c MANIFEST.sha256`；所有列出的
文件均通过完整性检查。

## 数学核验结论

release 建立的是下列**相对**闭包，而不是无条件重证 H4：若输入已经具有
`verified_actual_h4_provenance` 与 `verified_priority_prefix_miss` receipt，且属于
actual proper-overlap、top-capacity、\(a_{\rm alt}=1\) H4 域，则 corrected clean
\(q\)-macro 以

\[
M_q=\operatorname{lcm}(M_4,Q_x,Q_y)
\]

构造 target，并完成 E1--E5 的相对证明。它不重建 \(P\Rightarrow H_4\) provenance，
不解决其它 H4 selector branch、\(q=1\) G handoff、global selector 或 ESC。

当前仓库已有更强的
[parent-anchored checkpoint 收缩宏](../claims/type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction.md)：
它在其域内重放完整 persistent lineage 和 fully typed target。release 的相对宏被保留为
修正 support 公式、独立局部 verifier 与 E1--E5 论证的规范版本，而不替代这条强宏。

## 集成与修正

| release 内容 | 主仓库归档或编辑位置 | 处理 |
|---|---|---|
| 完整证明 | [h4-clean-q-e1-e5-relative-macro-closure-2026-08-17.md](h4-clean-q-e1-e5-relative-macro-closure-2026-08-17.md) | 完整导入；将两个控制字符修复为 LaTex `\frac`。 |
| 相对闭包 theorem card | [type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md](../claims/type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md) | 纳入，并声明与 stronger parent-anchored macro 的关系。 |
| relative macro verifier | [type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py](../reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py) | 纳入；receipt scope 区分真实 provenance 与本地 control。 |
| focused tests | [test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py](../tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py) | 纳入并扩展：控制样例不可递归、lazy fields 不进 state identity、错误 provenance claim 被拒绝。 |
| old support formula | [type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge.md](../claims/type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge.md) | 修正为统一 lcm 公式，并保留旧 single-side 公式为何错误的记录。 |
| E3 lazy dispatch contract | [denominator-escape-state-contract.md](../concepts/denominator-escape-state-contract.md) | 加入受限 `pending_dispatch` 正规化：队列字段不进 state identity，未正规化 target 不可被 type-specific selector 消费。 |
| frontier / reproduction / CI | [current-frontier-2026-07-29.md](../concepts/current-frontier-2026-07-29.md)、[reproductions README](../reproductions/README.md)、[research-kb-ci.yml](../.github/workflows/research-kb-ci.yml) | 加入相对闭包说明、运行入口和 focused CI test/lint。 |
| 旗舰地图 | [README.md](../README.md)、[flagship-proof-program-2026-08-16.md](../concepts/flagship-proof-program-2026-08-16.md) | T1 标为 scoped relative closure；T2--T6 保持开放。 |

## 验证边界

release 原有 p=73、p=241 fixtures 通过 E1--E5 的相对整数重算，但它们不是 actual-H4
provenance。规范 verifier 现在将这些输出标记为 `control_only` 和
`recursive_edge_eligible=false`。同时携带受认可 upstream/priority receipt status 的输入
输出 phase-local `candidate_transition`；在 global selector 与全局良基势接纳前，仍不输出
`verified_edge`。

这一区分修复了原 release 中“control 数据可产生 verified-edge 标签”的语义歧义；它不改变
相对数学推导，也不将局部样例误作全称 provenance 证明。相应 canonical verifier 的
input/output schema 与 adapter 已升为 v2；v1 receipt 必须显式迁移并补齐 premise
validation status，不能静默复用。
