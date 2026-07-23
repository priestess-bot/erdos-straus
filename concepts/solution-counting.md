---
kind: concept
concept_id: solution-counting
title: 解计数与枚举复杂度
summary: f(n) 计数有序正整数解；参数化既用于平均阶估计，也用于输出全部解的算法。
topics:
- solution-counting
- algorithms
used_by:
- average-solution-count
sources:
- elsholtz_tao2013
- elsholtz_planitzer2020
visibility: public
last_checked: '2026-07-23'
---

# 解计数与枚举复杂度

f(n) 计数有序正整数解；参数化既用于平均阶估计，也用于输出全部解的算法。

## 数学说明

Type I/II 参数把解计数转成约束因子元组。现代结果给出素数平均和、逐点上界及固定 m 的 O(n^(3/5+epsilon)) 上界。

## 常见误读

- 有序与无序解相差置换因子，重合分母时需小心。
- 上界和平均值都不保证 f(p)>0。
