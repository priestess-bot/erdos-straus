---
kind: claim
claim_id: local-reproduction-2026-07-23
title: 关键恒等式与除子证书的小尺度复现
statement: 精确整数实现复现了经典模约化、模 840 六残余类、n<=1000 的因子对证书及 p<=10000 的 Bradford 除子证书。
claim_status: computationally_reproduced
topics:
- reproduction
- exact-arithmetic
- computation
sources:
- salez2014
- bradford2024
visibility: public
last_checked: '2026-07-23'
---

# 关键恒等式与除子证书的小尺度复现

## 结论

精确整数实现复现了经典模约化、模 840 六残余类、n<=1000 的因子对证书及 p<=10000 的 Bradford 除子证书。

## 推理与来源

脚本不用浮点数：三个经典恒等式各核对 1000 组；S5/S7 与 1 mod24 的 CRT 补集恰为 1,121,169,289,361,529；因子对恒等式覆盖 2..1000；Bradford 条件覆盖 10000 内 1229 个素数。

- reproductions/esc_reproduce.py and generated results.json.
- Unit tests independently re-evaluate exact Fraction identities on smaller ranges.

## 边界

这是算法接口与公式的有限交叉核对，不是 10^17 或 10^18 的全量复现，也不能证明猜想。
