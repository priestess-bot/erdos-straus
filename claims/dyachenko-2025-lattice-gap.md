---
kind: claim
claim_id: dyachenko-2025-lattice-gap
title: Dyachenko 2025 的对角格窗口命中论证有缺口
statement: Theorem 9.21 的无条件存在性依赖 Proposition 9.25，但其证明错误地用同一个对角平移参数命中两个独立选取的坐标。
claim_status: claimed_with_gap
topics:
- proof-audit
- affine-lattice
- critical-gap
sources:
- dyachenko2025
visibility: public
last_checked: '2026-07-23'
---

# Dyachenko 2025 的对角格窗口命中论证有缺口

## 结论

Theorem 9.21 的无条件存在性依赖 Proposition 9.25，但其证明错误地用同一个对角平移参数命中两个独立选取的坐标。

## 推理与来源

若 p0=(u0,v0) 且 w=(d',d')，由 u* 决定 m=(u*-u0)/d' 后，第二坐标是 v0+md'；它一般不等于独立选取的 v*。同时 Lemma 9.24 把一个秩一对角陪集写成所有固定双坐标剩余类的格点，等号无一般依据。

- Dyachenko 2025, Lemmas 9.22-9.24 and Proposition 9.25.
- Theorem 9.21 explicitly invokes this window-hitting step.

## 边界

这不否定论文中的所有代数恒等式或算法样例，但阻断了对每个 P 的全称存在性。
