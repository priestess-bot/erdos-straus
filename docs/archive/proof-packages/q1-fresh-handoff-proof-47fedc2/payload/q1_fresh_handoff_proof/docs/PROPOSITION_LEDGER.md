# q=1 Fresh-Source Handoff 命题账本

本账本把“方向 3”拆成互相可判真的命题。状态以本证明包为准，基线为仓库提交 `47fedc2`。

| ID | 命题 | 结论 | 说明 |
|---|---|---|---|
| G1 | `q=1 Type II G` 当且仅当 `X=(p+3)/4` 的每个素因子都为 `1 mod 3` | 证明 | 直接来自模 3 生成群 |
| G2 | `q=1 G` 强制 `R=3 Type I` 非 G | 否定 | `p=241`, `X=61`, `N=181` 双 G |
| G3 | 旧 canonical root 可直接继承 Type II `X`-support | 否定 | 旧 root 有 `(X,K)=1` |
| G4 | 存在唯一 low full-carrier Type I root | 证明 | `R_X=16t+3`, `K_X=X(16t+1)` |
| G5 | full-carrier root 有 target-independent fresh actual source | 证明 | universal `p`-source 一步到 `(1,R_X-1,1)` |
| G6 | ordinary root-entry 满足 E1--E5 | 证明 | E4 identity；E5 phase `2→1` |
| G7 | T4 ordinary 字面量词成立 | 证明 | lineage 长度可取 1 |
| G8 | 当前 `v1` 自动支持任意 nontrivial mark | 否定 | `v1` 明确限定 `Sol(p)` |
| G9 | portable mark 可逐字搬运到 fresh root | 条件证明 | 需新增 mark-preserving normal form/serializer |
| G10 | root 后必有第一条真正 strict Type I edge | 证明 | odd/even 两支闭式 |
| G11 | 首 child 的第二 anchor 仍可低重图表 | 否定 | odd/even 都强制 high overflow |
| G12 | 第二 anchor high overflow 有确定性 strict fixed-`n` 宏 | 证明 | odd `L=2(10t+1)`；even `L=9s q_*` |
| G13 | q=1 immediate `d=1` receiver 可能落入 p-free failure | 否定 | 奇支有限同余矛盾；偶支 `j mod 3` 矛盾 |
| G14 | q=1 immediate `d=1` regeneration 可无限重复 | 否定 | odd 不再生；even 只可能 `q_*=23`, `g=1`, `j=20` 且只再生一次 |
| G15 | q=1 专属模块可在统一有限步后离开专属 regeneration tail | 证明（组合） | downstream claims 组合，详见 `DOWNSTREAM_Q1_MODULE.md` |
| G16 | `c=8` 下任意 non-`p` raw prime 都自动降低 capacity | 否定 | 仓库已有实际控制产生大 capacity |
| G17 | `c=8,q_*=103` image 已全称终止 | 未证明 | 属于 T6，不属于 T4 |

## 推荐状态语义

### 已证明

这里的“证明”分两类：

1. `PROOF.md` 中重新给出完整代数证明的命题；
2. 下游模块中由 `47fedc2` 已建立 claim 组合，并由本包独立程序重算其关键闭式的命题。

### 否定

“否定”要求明确反例或全称 no-go。不能把“扫描没找到”记为否定。

### 条件证明

`G9` 的条件不是数论未知量，而是状态 schema 条件：mark 必须可以在 fresh tree 中逐字重序列化，且不引用旧 physical charged occurrence。

---

# 建议把研究问题从 T4 改写成后续接口

T4 ordinary 已闭合后，后续核心问题应写成：

> **Q1-Image-Totality**：对 q=1 full-carrier module 产生的 reachable Type I image，尤其 `c=8,q_*=103` 层，是否总有 terminal 或下一条 strict E1--E5 edge？

这是 T6 的子问题，而不是 Fresh-G-Handoff 本身。
