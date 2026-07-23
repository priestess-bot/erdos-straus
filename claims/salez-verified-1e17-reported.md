---
kind: claim
claim_id: salez-verified-1e17-reported
title: Salez 报告验证到 10^17
statement: Salez 2014 报告模筛计算覆盖所有 n<=10^17，并公开 C++ 程序；本库未重跑该完整范围。
claim_status: computationally_reported
topics:
- computation
- modular-sieve
- reproducibility
sources:
- salez2014
visibility: public
last_checked: '2026-07-23'
---

# Salez 报告验证到 10^17

## 结论

Salez 2014 报告模筛计算覆盖所有 n<=10^17，并公开 C++ 程序；本库未重跑该完整范围。

## 推理与来源

报告给出七个参考方程、候选周期、候选数与运行时间，使算法可审查。

- Salez 2014, Abstract and Sections 4-5.
- Reported G7=892371480 and |R7|=147348.

## 边界

公开代码不等于第三方完整复现；正确措辞是“论文报告验证”。
