---
kind: claim
claim_id: bello-fab-window-reported
title: fab 小参数窗口覆盖 10^14 内相关素数是计算报告
statement: Bello-Hernandez 等报告所有 p=1 mod4、p<10^14 可由 fab(p,a,b) 在 1<=a,b<=11 内检测，但未证明窗口对所有素数有统一界。
claim_status: computationally_reported
topics:
- divisor-parametrization
- computation
- bounded-window
sources:
- bello2026
visibility: public
last_checked: '2026-07-23'
---

# fab 小参数窗口覆盖 10^14 内相关素数是计算报告

## 结论

Bello-Hernandez 等报告所有 p=1 mod4、p<10^14 可由 fab(p,a,b) 在 1<=a,b<=11 内检测，但未证明窗口对所有素数有统一界。

## 推理与来源

Theorem 5 给出参数化完整性，计算备注则限制在有限窗口；Theorem 8 还说明固定有限参数机制不能以简单有限同余覆盖完成全部工作。

- Bello-Hernandez et al. 2026, Theorems 5 and 8, Remarks 9 and 23-25.

## 边界

计算窗口现象不应提升为全称短证书猜想，除非另行明确提出并证明。
