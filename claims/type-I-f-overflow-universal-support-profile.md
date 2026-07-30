---
kind: claim
claim_id: type-I-f-overflow-universal-support-profile
title: 普适高度缺口的多坐标和混合符号边界
statement: 对冻结的 165 个全部合法载体分配仍无法承载全部溢出的 F 状态，半径六以内的首个目标仿射见证均至少包含两个溢出坐标；溢出支持大小为 2/3/4/5/6 的状态数分别为 22/55/56/25/7。114 个见证为正负混合符号，49 个全负，2 个全正；152 个状态含规范活跃支持之外的溢出素因子。因此单坐标 q 进桥、单符号桥或只使用规范 Fourier 支撑的桥不能覆盖这批严格缺口。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-f-overflow-active-support-boundary
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- multi-support
- q-adic
- descent
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 普适高度缺口的多坐标和混合符号边界

## 结果

对全部合法载体分配仍无法承载全部溢出的 165 个状态，复用半径六以内的首个目标仿射
格见证，得到：

```text
overflow support size: 2 -> 22, 3 -> 55, 4 -> 56, 5 -> 25, 6 -> 7
single-coordinate witnesses: 0
sign classes: all_negative 49, mixed 114, all_positive 2
active-support classes: all_active 13, has_inactive 152
total witness excess: 1512
universal unsupported excess layers: 1348
minimum total excess: 3
maximum total excess: 23
```

因此在当前冻结见证中，严格高度缺口从第一层就是多坐标问题；不能把它约化为一个
单独素因子 (q) 的高度不足。绝大多数状态还同时包含规范 Fourier 支撑之外的素因子，
而且符号通常混合，不能只分析正溢出或只分析负溢出。

## 对证明桥梁的限制

该边界不证明更大半径中不存在单坐标见证，也不证明目标仿射格没有其它表示。它的可靠
含义是：在已经锁定的严格缺口集上，下一条容量或递降引理必须允许

1. 至少两个素因子坐标的联合需求；
2. 正负指数同时出现时的方向耦合；
3. 非活跃素因子进入载体或下降映射。

这与[普适盒溢出坐标的跨状态 q 进容量压力边界](type-I-f-overflow-cross-state-qadic-capacity.md)
相结合，说明单位 q 需求没有超载并非偶然，而是需求必须保留多坐标溢出量的直接结果。

## 复现

```bash
python3 reproductions/type_i_f_overflow_universal_support_profile.py
```

结果文件：

```text
reproductions/type-i-f-overflow-universal-support-profile-results.json
```

输入哈希：

```text
assignment 62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
support    93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1
```

结果文件 SHA-256：

```text
c965936db508f5ccd553b79c94eb1b422b74ae4a78e51972306c7ebc7ad257a0
```
