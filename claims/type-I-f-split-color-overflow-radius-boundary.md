---
kind: claim
claim_id: type-I-f-split-color-overflow-radius-boundary
title: 分色 F 状态的有限指数盒溢出半径边界
statement: 对冻结完整线性谱中 291 个分色 F 状态，目标仿射格均不在原指数盒内；首次进入半径 1、2、3、4 的状态数为 87、73、36、27，另有 68 个半径大于 4（按半径上限 4 截断）。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- q-adic
- capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
depends_on:
  - type-I-f-full-cross-color-pair-capacity-boundary
  - type-I-f-split-color-relation-certificate
---

# 分色 F 状态的有限指数盒溢出半径边界

## 主张

对 291 个无法同色承载两个活跃方向的 F 状态，令 delta 为目标仿射格第一次进入
扩张盒 B_(nu+delta) 的半径。精确 meet-in-the-middle 审计在 delta <= 4 内得到：

```text
delta=1: 87
delta=2: 73
delta=3: 36
delta=4: 27
delta>4: 68
```

这说明所有状态至少存在一个单位盒缺口，且 204 个状态的缺口至少为 2。

## 口径

溢出半径是关系格—指数盒的几何缺陷，不等同于 q 进载体高度。若能证明每增加一层
溢出必然消耗一个跨状态可比较的载体高度，则由于双颜色容量组已经全部恰好饱和，
可立即得到容量超载；目前这一步仍是开放桥梁。

## 复现

```text
python3 reproductions/type_i_f_split_color_overflow_radius.py
```

结果文件：

```text
reproductions/type-i-f-split-color-overflow-radius-results.json
```
