# 自包含性与 established-evidence 核对记录

**更新日期：** 2026-08-29。  
**对象：** 22 个 SP dossiers、manifest 和已列 verification artifacts。

## 判定规则

一个 dossier 必须在正文内定义对象、域、量词、特殊术语、结论、反例控制和完成证据；不得把另一个 SP 或仓库函数作为未声明逻辑前提。`ESTABLISHED` 还要求正文含完整证明，并列出可独立重放的 immutable-path evidence；状态只适用于精确量词作用域。

## 结果

| 检查项 | 结果 |
|---|---|
| dossier 文件数 / manifest 条目数 | 22 / 22 |
| 自包含定义和完成证据 | 22 / 22 |
| proposition-to-proposition 隐式逻辑引用 | 0 |
| SP-02 | ESTABLISHED（条件有限模型） |
| SP-04 | ESTABLISHED（M23 registered prefix） |
| SP-21 | ESTABLISHED（签名 decidable q=1,G policy domain） |
| SP-22 | ESTABLISHED（该域每个 actual admitted source） |
| OPEN_PROPOSITION 总数 | 18 |

SP-21/SP-22 的证明正文自行给出 abstract prefix theorem、完整 concrete policy、overlap partition、Bradford terminal soundness、全称 local totality、uniform phase-root formulas、target terminal proof、E1--E5/R 和 scope/global distinction。代码、签名、artifact lock、evidence、independent replay 和测试只是审计证据，不是数学证明的隐含前提。

## 独立实现核对

constructor 和 replayer 没有相互 import。前者按素因子指数笛卡尔积枚举平方除数，后者按平方根扫描和互补因子枚举。独立 replayer 可对任意域内 source 重建 prefix decision，不调用 selected producer；对 `p=21169` 另行重建完整 edge、admission、queue/re-entry 和 seals。外部 authority statement 覆盖 authority ID、base commit、policy digest、artifact-lock digest 和 mutation prohibitions。

## 状态边界

SP-21/SP-22 只建立隔离签名 research slice。以下仍不可替代且保持开放：production-wide SP-03；全 constructor/source F1 coverage；post-G/F2/F3 totality；T6；Erdős--Straus 猜想。有限 bounded census 只作回归，不替代全称证明。
