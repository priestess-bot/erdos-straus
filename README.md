# Erdős–Straus 猜想研究知识库

本目录按时间顺序整理 Erdős–Straus 猜想的直接研究文献、关键技术依赖、
可核查数学主张和计算复现。`研究进展综述.md` 是阅读入口；`papers/`、
`claims/`、`concepts/` 中的 Markdown/YAML 文件是知识库的事实源。

当前文献快照审计至 2026-07-31；当前证明前沿和本轮旗舰命题核验至 2026-08-17。论文卡、
主张卡、概念卡及各状态的实时数量以 `python scripts/kb.py status` 和自动生成的
`index/theorem-ledger.md` 为准，不在入口文档手工复制。其中被撤回论文和存在关键证明
缺口的预印本仍会收录，但用独立状态标出。

## 当前旗舰命题（核验至 2026-08-17）

对核心素数 \(p\equiv1\pmod{24}\)，最终目标是下列双出口命题：

\[
\mathrm{F0}(p):\qquad
\mathrm{Type\ II}(p)\ \lor\ \mathrm{Type\ I\text{-}even\text{-}terminal}(p).
\]

第二出口采用已核验的 normal form：存在
\(m\equiv3\pmod4\)、\(3\le m\le p-2\)、\(x=(p+m)/4\) 及正整数 \(e,E\)，使

\[
e\mid x^2,\quad e\equiv-4^{-1}\pmod m,\quad
R=\frac{4e+1}{m},\quad K=xR-e,
\]
\[
E\mid4K^2,\quad E\equiv1\pmod R,\quad 2\mid E,\quad E\le4K-2R.
\]

这里 \(4^{-1}\) 在模 \(m\) 下取逆元。该 normal form 的代数等价性已经建立；对每个
核心素数选择 Type II 或该 Type I 证书仍是开放问题。后续主线维护下列六条可判真假的
旗舰命题：

| ID | 状态 | 核心断言 |
|---|---|---|
| T1 H4-Closure | 相对闭包已建立 | 对 actual proper-overlap、top-capacity、\(a_{\rm alt}=1\) receipt，已验证的 upstream provenance 与 priority miss 之后，clean \(q\)-macro 给出 E1--E5 的 phase-local `candidate_transition`；其它 H4 selector branch 与全局 admission 仍须覆盖。 |
| T2 Atomic-Admission | 开放 | canonical maximal atomic split 的 ownership、typed target、priority 与 serializer 准入可由 actual provenance 完整推出，或证明全局 one-use 不必作为额外公理。 |
| T3 Marked-Terminal | 开放 | Type II gcd-shadow 产生的普通 terminal 满足相应 marked solution-set membership，或转为下一条严格合法状态边。 |
| T4 Fresh-G-Handoff | 开放 | 每个 \(q=1\) G endpoint 都有不复用 Type II source support、且不读取未知目标解的有限 fresh-source lineage，通向 Type I 或 terminal。 |
| T5 Global-Well-Foundedness | 开放 | 所有进入最终 proof graph 的递归边共享一个全局良基势 \(\Pi\)，并严格下降。 |
| T6 Global-Selector | 开放 | 确定性 selector 在每个核心 prime / legal state 输出 terminal 或一条可提升、严格下降的 verified edge。 |

六条命题的精确量词、现有证据、尚缺合同、反证标准、依赖顺序和其余次级研究方向见
[`concepts/flagship-proof-program-2026-08-16.md`](concepts/flagship-proof-program-2026-08-16.md)。
T1 的上述结论是相对宏闭包，不重建 H4 provenance，也不推出 q=1 G handoff、全局 selector
或猜想本身；T2--T6 仍为开放研究命题。

## 快速使用

```bash
python scripts/kb.py validate
python scripts/kb.py build
python scripts/kb.py search "half dimensional sieve"
python scripts/kb.py status
```

`build` 生成：

- `index/timeline.md`：按首次公开日期排列的完整文献时间线；
- `index/citation-graph.mmd`：论文引用图；
- `index/theorem-ledger.md`：从主张卡自动生成的数学状态、证明来源与审阅状态账本；
- `index/catalog.json`：供其他工具消费的结构化目录；
- `index/kb.sqlite`：带 FTS5 全文检索的 SQLite 数据库。

主张卡用三个互不替代的字段记录证据状态：`claim_status` 表示数学结论状态；
可选的 `proof_provenance` 表示证明或证据来自原始文献、仓库推导、计算复现或混合来源；
可选的 `review_status` 表示卡片中的论证是否经过仓库内、独立或外部复核。旧卡缺少后两个
字段仍然有效，构建时统一显示为 `unspecified`，不会从 `claim_status` 自动推断。允许值见
`schemas/document-types.yaml`；新卡从 `templates/claim-note.md` 创建并应主动填写。

`proof_provenance` 的语义为：`external_primary_source` 指精确陈述和证明锚定到所列原始
来源，`repository_derivation` 指证明写在本仓库，`computational_reproduction` 指证据来自
可复现程序和产物，`mixed` 指结论实质依赖多类证据，`not_applicable` 用于未声称已有证明
的开放问题等，`unspecified` 表示尚未完成分类。`review_status` 中，`unreviewed` 表示没有
记录第二轮复核，`internal_review` 表示完成仓库内复核，`independent_review` 表示存在独立
证明或独立实现的复核，`external_review` 表示存在仓库外审阅记录；后三者应在卡片正文给出
可核查锚点，`unspecified` 只表示尚未分类。

研究方法、已确立结论和逐点证明缺口的历史导航见
[`concepts/research-directions-and-proof-gap.md`](concepts/research-directions-and-proof-gap.md)；
当前证明前沿、下一阶段目标及其依赖顺序见
[`concepts/current-frontier-2026-07-29.md`](concepts/current-frontier-2026-07-29.md)。

常用检索过滤器：

```bash
python scripts/kb.py search "parametrization" --type paper --year-from 2010
python scripts/kb.py search "计算验证" --type claim --tag computation
```

公开副本由 `python scripts/kb.py publish` 生成到 `public/`。该命令不会复制
内部工作日志、原始来源文件或标记为 `visibility: internal` 的文档；发布前还会扫描
内部检索标记和本机路径。公开版包含候选文献清单、BibTeX 和小尺度复现材料。

## 增量研究流程

1. 把新发现写入 `bibliography/candidates.yaml`，先作纳入、归并或排除判断。
2. 对纳入论文建立 `papers/<citation_key>.md`，分别记录出版状态与数学核查状态。
3. 将可复用结论拆成 `claims/`，将术语和方法拆成 `concepts/`。
4. 运行 `validate`、测试、`build` 和 `publish`；检索日期与未取得原文的缺口写入
   `bibliography/search-log.md`。

有限复现入口为 `python reproductions/esc_reproduce.py`。它核对经典恒等式、模
840 残余类、因子对证书和 Bradford 的 Type I/II 除子对应，不是对已报告
`10^17` 或 `10^18` 搜索的全量复现。

`python reproductions/short_certificate.py` 另行按 \(m=4x-p\) 搜索 Type I/II
的最小首分母缺口，用于检验“短证书或递降”研究计划中的候选短界；它同样是
有限实验。

## 证据纪律

- 同行评议状态与数学核查状态分别记录。
- 每个实质性主张必须指向原始论文及页码、定理号或公式号。
- 预印本、计算报告、启发式和存在关键缺口的证明声称不能混写。
- 未取得原文时明确标记，不以二手摘要冒充精读。
- “文献全集”是带截止日期的可审计语料，不声称永久穷尽。

本知识库使用 AI 辅助进行检索、格式化、代码实现和初步数学核查。最终数学
结论以链接的原始文献为准，争议性结论保留明确的核查状态与限制说明。
