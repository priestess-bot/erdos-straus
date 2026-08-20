# 证明包展开索引

这里是 `archive/proof-packages/raw/` 中七个原始 ZIP 的完整展开视图。每个 `payload/`
目录由对应 ZIP 直接解压得到，保留包内的 Markdown、JSON、补丁、脚本、测试、工作流和
记录输出；raw ZIP 仍是字节级权威来源。归档中出现的 claim、patch 或 generated ledger
都是历史证据，除非下表明确说明，否则不覆盖主仓库的活动文件。

| 包 | payload | 完整性/复核 | 当前处置 |
|---|---|---|---|
| F1 reachable-state exhaustion | [payload](f1-reachable-state-exhaustion-all-outputs-2026-08-20/payload/) | ZIP 与内部清单通过 | `ARCHIVED_UNACCEPTED_CANDIDATE`；F1 仍 `OPEN`。 |
| M-H final-two resolution | [payload](mh-final-two-resolution-2026-08-20/payload/) | ZIP、patch check、两个聚焦 verifier 和 4 个测试通过 | M 仅为条件性 E3 适配器；H 仅接纳 C=1 同协议 no-go。 |
| T6 proof workfiles | [payload](t6-proof-workfiles-2026-08-17/payload/) | ZIP 与内部清单通过 | 已选择性合入；T6 仍 `OPEN`。 |
| pre-T6/T6 boundary overlay | [payload](pre-t6-t6-boundary-overlay/payload/) | ZIP 通过；包内无 detached manifest | 历史 overlay；冻结 v1 边界以当前活动文档为准。 |
| T2/T5 full | [payload](t2-t5-full-2026-08-17/payload/) | ZIP 与内部清单通过 | T2 phase-local、T5 contract-level 结论已接纳。 |
| H4 closure release | [payload](h4-closure-release-2026-08-17/payload/) | ZIP 与 `MANIFEST.sha256` 通过 | 仅 H4 clean-q relative closure。 |
| q=1 fresh handoff | [payload](q1-fresh-handoff-proof-47fedc2/payload/) | ZIP 通过；内部 `SHA256SUMS` 仅自身条目失配 | ordinary q=1 G relative closure；self-hash 不作权威完整性依据。 |

完整的逐包数学裁定见
[证明包综合复核](../../proof-package-consolidation-2026-08-21.md)。
