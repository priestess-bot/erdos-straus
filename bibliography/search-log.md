# 检索日志

## 2026-07-23：启动轮次

- 起始语料：`研究进展综述.md` 中的 17 条参考文献。
- 已确认需要补回的历史入口：Erdős、Obláth、Rosati、Schinzel、Bernstein、
  Yamamoto、Webb、Terzi、Jollensten、Yang、Sander 1997、Kotsireas、Swett。
- 已确认需要重新普查的现代入口：Ionascu–Wilson、Jia、Subburam–Togbé，以及
  2025–2026 年题名直接包含本猜想但未进入原综述的预印本。
- 状态：检索进行中；当前计数不是最终 PRISMA 式流量统计。

## 2026-07-23：参考文献回溯与前向普查

- 以 Elsholtz–Tao 2013 的 89 条参考文献为第一轮回溯入口，恢复了 1950–2000
  年直接研究链和早期计算纪录。
- 以 OpenAlex、arXiv、Crossref/DOI 页面、作者主页和出版社页面做题名前向检索；
  Semantic Scholar API 本轮持续返回限流错误，因此未把它当作完成判据。
- 对 arXiv/期刊/Zenodo 版本按“一个智力工作一张卡”归并；对 2026 年自存档的
  “完全证明”声称全部保留筛选记录，但不因题名或摘要自述提升数学核查等级。
- 截止 2026-07-23，`bibliography/candidates.yaml` 记录 50 余个纳入、归并、
  待审、背景或排除决定。当前语料仍是“有截止日期的系统普查”，不宣称永久穷尽。

## 2026-07-23：递归补录与状态纠错

- 由 Bradford 2021/2025 的引文链补入 Bradford–Ionascu 2015，并由 2026 年前向
  检索补入 Chamberland 的 *Integers* A42 正式论文。
- 确认 Ionascu–Wilson 已发表于 *Revue Roumaine* 56(1)，Gionfriddo–Guardo 已
  发表于 *Journal of Interdisciplinary Mathematics* 24(8)，不再误标为预印本。
- 确认 arXiv:1107.6039 是 Jia 2012 期刊论文的公开版本；arXiv:1107.5394 是另一篇
  短注，二者不能合并。
- 确认 Subburam–Togbé 的 DOI、卷页和出版社摘要；全文仍受访问限制，数学内容保持
  `unverified`。
- 补入 Rios 2013。该文已由作者因公式 (3)、(5) 的关键符号错误撤回，故作为负面
  研究记录纳入并标为 `contradicted`，不沿用其渐近结论。
- 对 Bradford 2026 与 Dyachenko 2025 的全称证明声称分别定位到覆盖系统缺口和
  仿射格共同平移参数的相容性缺口。

## 待补检索缺口

- Subburam–Togbé 2016 的付费正文；
- 早期 Mathesis、Boll. UMI、Congressus Numerantium 原文页像；
- 2026 年 Zenodo/OSF/ResearchGate 同名证明声称的版本聚类和逐一定理审查；
- MathSciNet/zbMATH 的完整前向引用导出（当前仅使用可公开页面交叉核对）。

## 2026-07-23：最终前向监测

- 对 2026-01-01 以来的 OpenAlex 记录执行自动监测，返回 26 个原始记录；Semantic
  Scholar API 仍为 HTTP 429。这里的 26 是提供者记录数，不是论文数。
- 聚类后识别出 Zenodo 概念 DOI/版本 DOI、同一稿件多次上传、Xu 论文的代码数据集
  和已纳入论文的重复记录；这些均标为 `merge_version`，不重复计数。
- 新增明确候选包括 Linear-Ratio Ansatz、Audigé divisor-lattice、Residual Divisor
  Certificates、Liu modulo-6 proof、Uygun 的 \(840q+529\) 模 47 分析，以及若干有限
  统计或全称证明声称。它们已逐项留下筛选记录，但在原文证明主链完成核查前不进入
  已确立进展。
- 7 月 10 日的 Fractal Correction Engine 上传是 3 月 Zenodo 概念记录的后续版本；
  作者明确声明只作有限统计研究、不声称证明，故归为背景材料。

## 2026-07-23：路线综合复核

- 以 Elsholtz--Tao 2013 的 Table 1 逐项复核早期计算范围，并保留该表对
  Franceschine 二手转述和未发表 Elsholtz--Roth 计算的警告；计算史不再写成单调的
  独立纪录链。
- 用 Salez 2014 与 Bradford 2021/2025、Chamberland 2026、Bello-Hernandez 等
  2026 的参考链补入 Mordell 1969 专著，定位为 Rosati 型经典公式的二手书目枢纽，
  不作为原始优先权或未核对定理的依据。
- 对截至截止日的 arXiv 题名检索作抽查，Xu、Ventas、Bradford 2026 和 Bello-Hernandez
  等 2026 均已在现有语料；未发现需要新增且已完成定理审查的直接研究工作。
- 新建“研究路线总图与逐点证明缺口”概念卡，将同余构造、解析例外集、Type I/II 与
  除子参数、解计数、计算、几何和一般化问题的结论范围分开记录。
