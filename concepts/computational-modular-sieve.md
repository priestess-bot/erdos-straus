---
kind: concept
concept_id: computational-modular-sieve
title: 计算模筛与可复现性
summary: 模筛先用已证明恒等式排除绝大多数候选，只对逃逸剩余类做精确素性与分解检查。
topics:
- computation
- modular-sieve
- reproducibility
used_by:
- salez-verified-1e17-reported
- verification-1e18-reported
sources:
- salez2014
- mihnea_dumitru2025
visibility: public
last_checked: '2026-07-23'
---

# 计算模筛与可复现性

模筛先用已证明恒等式排除绝大多数候选，只对逃逸剩余类做精确素性与分解检查。

## 数学说明

过滤器 S_m、缩短过滤器、CRT 周期 G_i 和残余集合 R_i 是核心对象。可复现报告还需版本、代码、整数溢出策略、批次边界与最终逃逸候选证书。

## 常见误读

- 代码公开不等于完整运行已独立复现。
- 有限计算不能证明无穷全称命题。
