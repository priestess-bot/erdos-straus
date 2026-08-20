# q=1 Fresh Handoff Proof Package Audit (2026-08-17)

## 原始来源与完整性

本次同步保留用户提供的冻结包
[q1_fresh_handoff_proof_47fedc2.zip](q1_fresh_handoff_proof_47fedc2.zip)，其外层 SHA-256 为：

```text
18bac61ee7976ce3c32aabd94a6f37ab50e5f8a229a33d8bf4ae91552d41ba4a
```

包声明的基线为提交 `47fedc2b772d6acf28a306bdbe9b1e5d5a49bfff`
(`Archive H4 clean q relative closure`)。`unzip -t` 已通过。在 2026-08-17 原审计基线，
包内保存的六份 upstream Markdown 快照均与当时 `HEAD` 逐字一致。2026-08-20 对 flagship
文档和 state contract 加入了版本化边界/准入附录，因此这两份 current copy 不再要求与冻结
snapshot 字节相同；数学证明仍由 archive digest、payload digest 和冻结 claim/contract 内容固定：

| 快照 | SHA-256 | 结果 |
|---|---|---|
| `type-I-type-II-mod-three-double-g-exit-obstruction` | `fcfa22aa...f003d3` | frozen = current |
| `type-I-universal-p-source-capacity-anchor-orbit` | `08e8349d...1df421` | frozen = current |
| `type-II-q-one-canonical-root-slice-support-disjointness` | `372b6111...3cafab8` | frozen = current |
| `type-II-q-one-full-carrier-phase-root-entry` | `38692de5...9ae340` | frozen = current |
| `denominator-escape-state-contract` | `88712307...f573f` | frozen = 2026-08-17 audit baseline；current 新增 2026-08-20 admission-firewall 附录 |
| `flagship-proof-program-2026-08-16` | `64b41f6b...bd02b` | frozen = 2026-08-17 audit baseline；current 含 2026-08-20 boundary addendum |

包的 `UPSTREAM_MANIFEST.md` 所列 core/first-child/downstream 依赖在 2026-08-17 审计时
均未发生自 `47fedc2` 起的实质内容变更。后续文档边界更新不改变冻结包的 provenance，且不应
再用“整个 current HEAD 与 archive 全部逐字一致”作为持续不变量。

包内 `SHA256SUMS` 对除其自身外的 payload 条目通过；它同时包含自身的 hash，而该自指条目不匹配。
因此不能写成“内部 manifest 全部通过”。这里以外层 archive hash、成功的压缩测试和逐个
payload hash 为 provenance；该元数据缺陷不改变证明文件或验证器的内容。

### 2026-08-20 detached provenance 规则

该 archive 的权威完整性链固定为：

1. 外层 archive SHA-256；
2. `unzip -t` 容器完整性；
3. 每个非 manifest payload 的 detached/逐文件 SHA-256；
4. 内部 `SHA256SUMS` 的非自指条目只作辅助交叉检查；
5. `SHA256SUMS` 对自身的条目明确为 non-authoritative。

CI 或文档不得再声称“内部 manifest 全部通过”。这关闭的是证据 provenance 的歧义，不会
升级或降级 handoff 的数学结论。

为使内容进入知识库全文检索，包内 `PROOF.md` 已按字节复制为
[q=1 fresh handoff 完整证明](q1-fresh-handoff-proof-2026-08-17.md)；其 SHA-256 是
`d5dd9936c60f5c5290d617b8ae5c93424a26c2d40278f6899a8db7f358ffec13`，与 archive 中的
payload hash 一致。

## 接纳的数学范围

接纳的不是一个新的重名 claim，而是现有
[q=1 G full-carrier phase-root 准入](../claims/type-II-q-one-full-carrier-phase-root-entry.md)
的独立证明与实现复核。对 ordinary 输入

\[
S=(p,q=1,\mathrm G;W_S=\operatorname{Sol}(p)),\qquad p=24t+1,
\]

其核心结论是

\[
q=1\ \mathrm G
\longrightarrow
T_X=(R_X,K_X),
\qquad
X=\frac{p+3}{4},\quad R_X=16t+3,\quad K_X=X(16t+1),
\]

其中 \(4K_X=pR_X+1\)，且 \(T_X\) 是唯一低 full-carrier chart。显式 fresh source

\[
\bigl(p,R_X(p-1)-p,p-1\bigr)
\longmapsto
(1,R_X-1,1)
\]

支付 E1；ordinary 两端同取 \(\operatorname{Sol}(p)\)，故 E4 为恒等 lift；已声明的单向
phase policy 支付此 handoff 的 E5。再由
\(\gcd(R_X-1,K_X)=1\)，奇 \(t\) 直接进入 marked-absorb，偶 \(t\) 经 overflow 和
fixed-\(n\) fold 进入 identity-lift edge，均给出首个严格 Type I local segment。

因此仓库 T4 的准确状态是：**ordinary relative closure established**。这不主张
nontrivial marked membership、T5 的全局良基势、T6 的 total selector、后续
\(c=8,q_*=103\) Type I image totality，或 Erdős--Straus 猜想。

## 独立复核

在解包根目录重放了包自己的独立实现：

```bash
python3 verification/run_all.py
python3 -m unittest discover -s tests -v
```

结果为 `status: verified`，五个测试 `OK`。实现只导入 Python 标准库与 `sympy`，不导入
本仓库 module；它重算 full-carrier root、odd/even first child、fixed-\(n\) quotient fold、
counterexample controls、source/anchor 以及 E1--E5 的 shape。报告的有限 sanity scan 到
\(p\le200000\)，覆盖 2,212 个核心素数和其中 1,106 个 `q=1 G` 输入；该扫描只用于发现
公式或实现错误，绝不作为全称证明。

独立代码对 E5 只能检查已声明 phase rank 的局部不等式，不能凭自身建立 global policy。
本次接纳 E5 的理由是 2026-08-17 冻结
[状态合同第 6.8 节](../concepts/denominator-escape-state-contract.md) 已明确纳入同一
不可回返 policy。2026-08-20 的 current contract 只在后续新增 constructor admission
firewall，没有改写该冻结段；因此数学依据仍由 archive payload 固定，但不再声称整份 current
文件与快照字节一致。这正是为什么结论仍限定为 relative closure。

## 仓库同步决策

| proof package 内容 | 同步处理 |
|---|---|
| 完整 ZIP 与原始输出 | 原样保留为可复核冻结 artifact。 |
| 包内 `PROOF.md` | 以字节一致的 Markdown 镜像导入，供全文检索与直接阅读。 |
| `PROPOSED_CLAIM_type-II-q-one-fresh-handoff-ordinary-closure` | 不重复导入；现有 core claim 的 statement、sources 与边界更完整，且快照逐字一致。 |
| ordinary T4 状态 | 同步到 README 与旗舰文档，明确为 relative closure。 |
| 独立代数证明与 verifier | 将现有 core claim 更新为 `independent_review`，并链接本审计。 |
| nontrivial marks、T5、T6、\(c=8,q_*=103\) | 明确保留为未闭合问题，不在本次状态调整中升级。 |
