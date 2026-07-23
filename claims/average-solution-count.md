---
kind: claim
claim_id: average-solution-count
title: 素数平均解数为 N log^2 N 量级至 log log 损失
statement: Elsholtz-Tao 证明 N(log N)^2 << sum_{p<=N} f(p) << N(log N)^2 log log N。
claim_status: established
topics:
- solution-counting
- mean-value
sources:
- elsholtz_tao2013
visibility: public
last_checked: '2026-07-23'
---

# 素数平均解数为 N log^2 N 量级至 log log 损失

## 结论

Elsholtz-Tao 证明 N(log N)^2 << sum_{p<=N} f(p) << N(log N)^2 log log N。

## 推理与来源

上下界分别由 Type I/II 参数化、除数和及素数算术级数估计得到。

- Elsholtz-Tao 2013, Theorem 1.1.

## 边界

平均和的正下界不推出每个 p 的 f(p)>0；少数零值可被其他素数的大量解掩盖。
