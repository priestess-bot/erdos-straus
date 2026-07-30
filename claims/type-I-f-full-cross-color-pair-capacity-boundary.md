---
kind: claim
claim_id: type-I-f-full-cross-color-pair-capacity-boundary
title: 完整 F 谱的双颜色共享模数容量边界
statement: 在冻结完整线性谱中，291 个无法同色承载两个活跃方向的 F 状态产生 582 个定向双颜色需求组；共享 R 的精确容量没有超载，最高需求/容量比为 1，全部组恰好饱和。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-full-spectrum
  - type-I-f-same-color-subset-capacity-boundary
  - type-I-linear-two-color-carrier-intersection-capacity
topics:
- type-I
- F-state
- finite-fourier
- q-adic
- capacity
- colored-capacity
- cross-state
- full-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 完整 F 谱的双颜色共享模数容量边界

## 主张

在冻结的 200 个完整线性谱中，2748 个达标 Fourier F 状态中有 2687 个至少双活跃；
其中 291 个在宽松的逐方向高度需求下没有可承载两个方向的同色块。对这 291 个状态，
枚举所有可行的定向分色对

\[
(q_a,aR+1),\qquad(q_s,sR+1),
\]

并按 ((p,q_a,q_s)) 分组，在共享 (R)-窗口内比较需求

\[
\sum h_{q_a}h_{q_s}
\]

与全部线性源状态的精确容量

\[
\sum_R v_{q_a}(aR+1)v_{q_s}(sR+1).
\]

得到 582 个定向分色需求组，全部有容量，0 个超载，最高需求/容量比为 1；582 组
全部达到恰好饱和。因而即使把双颜色的共享 (R) 约束保留下来，单纯的双方向
(q)-进容量仍不能产生跨状态矛盾。

## 口径

这是冻结完整谱上的有限负面边界。分色方向选择只针对同色容量无法承载的状态，且
使用了宽松的逐素数高度需求；结果不证明任意 Fourier 证书都必须采用这些方向，也不
证明一般双颜色桥。它说明下一步必须加入相位投影、目标纤维空缺、Fourier 半径或可
提升代价，才能把恰好饱和的容量槽排除或转成严格下降。

## 复现

```text
python3 reproductions/type_i_f_full_cross_color_pair_capacity.py
```

结果文件：

```text
reproductions/type-i-f-full-cross-color-pair-capacity-results.json
```
