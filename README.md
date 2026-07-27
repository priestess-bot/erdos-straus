# Erdős–Straus 猜想研究知识库

本目录按时间顺序整理 Erdős–Straus 猜想的直接研究文献、关键技术依赖、
可核查数学主张和计算复现。`研究进展综述.md` 是阅读入口；`papers/`、
`claims/`、`concepts/` 中的 Markdown/YAML 文件是知识库的事实源。

当前截止日为 2026-07-24。语料包含 58 张论文卡、91 张主张卡和 11 张概念卡；
其中被撤回论文和存在关键证明缺口的预印本仍会收录，但用独立状态标出。

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
- `index/catalog.json`：供其他工具消费的结构化目录；
- `index/kb.sqlite`：带 FTS5 全文检索的 SQLite 数据库。

研究方法、已确立结论和逐点证明缺口的导航见
[`concepts/research-directions-and-proof-gap.md`](concepts/research-directions-and-proof-gap.md)。

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
