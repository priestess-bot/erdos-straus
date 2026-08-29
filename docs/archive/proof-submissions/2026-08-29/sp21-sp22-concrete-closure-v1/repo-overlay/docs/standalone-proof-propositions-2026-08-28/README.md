# Erdős–Straus 独立证明命题包

本目录把证明缺口拆成可独立交给数学家、形式验证器或软件审计者处理的命题。每个 dossier 自包含定义对象、量词、结论、反例控制和完成证据；导航标签和外部路径不是逻辑前提。

## 共同边合同

状态 \(S\) 具有方程接口 \(\mathsf{Eq}(S)\)、有限整数编码和解集 \(\mathsf{Sol}(S)\)。递归边 \(S\to T\) 必须同时建立：

```text
E1 actual source occurrence and lineage
E2 deterministic target projection
E3 common legal persistent typing/admission
E4 universal solution-set lift Sol(T) -> Sol(S)
E5 strict decrease in one fixed well-founded N^7 potential
R  target re-enters the same selector domain
```

局部恒等式、有限样本、analysis-only target、scope MISS 或布尔字段均不能替代这些义务。

## 命题目录

| ID | 命题 | 状态与精确边界 |
|---|---|---|
| SP-01 | 结构化 E1--E5 边的抽象良基归纳 | OPEN |
| SP-02 | constructor/source 条件有限模型 | ESTABLISHED；不等于 concrete inventory |
| SP-03 | 全局唯一准入、无绕过和 re-entry | OPEN |
| SP-04 | q=1 根 M23 全除子 terminal schedule | ESTABLISHED；registered prefix，不是 global universe |
| SP-05 | q=1 complete-terminal nonterminal edge | OPEN；complete MISS 具有反例边界 |
| SP-06 | post-G/C9 全分派 | OPEN |
| SP-07 | C8/H4 actual atomic closure | OPEN |
| SP-08--10 | F2 high-support residuals | OPEN |
| SP-11--20 | F3 residuals | OPEN |
| SP-21 | scope-bound terminal-first admissibility | **ESTABLISHED** 于签名 decidable q=1,G policy domain |
| SP-22 | actual scoped q=1,G phase-root edge | **ESTABLISHED** 于该域的每个 externally admitted source |

完整逐项状态见 `manifest.json`。

## SP-21/SP-22 新证据

冻结 source policy 为 M23 六个 prior terminal、index 6 phase-root producer 和 index 7 明确 later gap-31 terminal。离线外部 coordinator 签名 policy 与完整 artifact lock；actual source receipt 绑定 root lineage、source occurrence、policy digest 和 branch；独立 replayer 不导入 producer，并可对任意域内 source 重建 prefix decision。

对该 predicate domain，有限终端前缀与 total producer 构成全称二分：最早 HIT terminal，或六项 MISS 后产生统一 E1--E5/R successor。`p=21169` 提供完整 admitted/re-entered 正向 trace；gap 31 解保留为 scope-MISS 负控。两个实现还独立复核了 `p<100000` 的全部 606 个域内 roots，但有限 census 不是全称证明的依据。

证据位于：

```text
data/t6-sp21-q1-p21169/
scripts/t6_sp21_q1_p21169_concrete_selector_v1.py
scripts/t6_sp21_q1_p21169_independent_replayer_v1.py
reproductions/sp21_q1_p21169_concrete_selector_v1/
tests/test_t6_sp21_q1_p21169_concrete_selector_v1.py
```

## 状态纪律

当前 22 个 dossiers 中，SP-02、SP-04、SP-21、SP-22 在各自精确作用域为 `ESTABLISHED`；其余 18 个为 `OPEN_PROPOSITION`。SP-21/SP-22 使用一次性研究 authority 和隔离 pilot runtime，不激活仓库现有 production runtime，也不关闭 production-wide SP-03、F1/F2/F3、T6 或 Erdős--Straus 猜想。
