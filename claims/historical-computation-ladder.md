---
kind: claim
claim_id: historical-computation-ladder
title: 计算验证应按来源和复现状态读取
statement: 可核查的历史资料记录了从 Oblath 的 106128、Rosati 的 141648、Terzi 的 10^8 到 Mihnea-Dumitru 报告的 10^18 的计算阶梯；这些数值不是单调的独立纪录链，也不能一概视为完整复现。
claim_status: computationally_reported
topics:
- computation
- history
- reproducibility
- records
sources:
- elsholtz_tao2013
- bello2012
- salez2014
- mihnea_dumitru2025
visibility: public
last_checked: '2026-07-23'
---

# 计算验证应按来源和复现状态读取

## 结论

可核查的历史资料记录了从 Oblath 的 106128、Rosati 的 141648、Terzi 的 10^8 到 Mihnea-Dumitru 报告的 10^18 的计算阶梯；这些数值不是单调的独立纪录链，也不能一概视为完整复现。

## 推理与来源

Elsholtz-Tao 的 Table 1 同时列出早期已发表、未发表和二手转述的范围，并警告 Franceschine 的 10^8 记载并非对 Terzi 的独立验证；其后的 Swett、Bello-Hernandez et al.、Salez 和 Mihnea-Dumitru 则各自报告更高的有限检查范围。

- Elsholtz-Tao 2013, Introduction and Table 1, including the warning below the table.
- Bello-Hernandez et al. 2012, reported 2 times 10^14; Salez 2014, reported 10^17; Mihnea-Dumitru 2025, reported 10^18 with public code.

## 边界

表中的范围只说明各来源声称或历史表归属的有限验证。除本库的小尺度复现外，不能把它们写成已由本库或独立团队逐一重跑的结果；未发表的 Elsholtz-Roth 范围也不应混入公开可审计纪录。
