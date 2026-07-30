---
kind: claim
claim_id: type-I-f-overflow-cross-state-qadic-capacity
title: 普适盒溢出坐标的跨状态 q 进容量压力边界
statement: 对冻结的 165 个在全部合法载体分配下仍无法承载全部溢出的 F 状态，普适缺口包含 448 个 (p,q) 坐标并归并为 433 个核心素数—q 组。按每个溢出坐标的总超额层收费，需求总量为 1348；在允许有序完整线性源状态重复计数、每个状态使用两块中较高 q 进高度的乐观容量中，可用层数为 1039，218/433 组超载，最大需求/容量比为 3。按相对于全局最佳载体高度的正缺口收费，需求为 886，121/433 组超载，最大比值为 2.5。该结果仍是条件性容量压力：尚未证明关系格盒外溢出层必须逐层消耗同一 q 进载体高度。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-cross-state-q-adic-capacity-bound
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- q-adic
- cross-state
- capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-and-linear-carrier-context
visibility: public
last_checked: '2026-07-30'
---

# 普适盒溢出坐标的跨状态 (q) 进容量压力边界

## 审计对象

输入是[全部合法载体分配下的 F 溢出高度上界](type-I-f-overflow-all-assignment-height-upper-bound.md)。
只保留 `no_assignment_can_carry_all_excess` 的 165 个状态。对每个状态的每个
`universally_unsupported_excess` 坐标 ((q,e_q))，记录：

1. 总溢出需求 (e_q)；
2. 在该状态全部合法分配中可达到的最高高度 (h_q^{max}) 后仍缺少的
   (e_q-h_q^{max}>0) 层；
3. 一个仅表示“该状态需要 q 载体”的单位需求。

共得到 448 个坐标需求，按核心素数和 (q) 归并为 433 组，涉及 108 个核心素数。

## 乐观容量

对固定组 ((p,q))，取该组出现的模数窗口
([R_{min},R_{max}])。在窗口内枚举 (p) 的完整线性源状态
((a,s,R'))，并令

[
h_q(a,s,R')=max{v_q(aR'+1),v_q(sR'+1)}.
]

将所有有序源状态的 (h_q) 相加，得到 `ordered_layer_capacity`。这比实际可用容量宽松：

- 每个需求可以独立选择两块中高度较高的一块；
- 忽略不同 q 之间的颜色冲突；
- 保留 ((a,s)) 与 ((s,a)) 两个有序方向；
- 窗口内未被需求使用的完整源状态也计入容量。

另外记录按每个不同模数只取一次最大高度的去重容量，但主压力结论使用更宽松的有序容量。

## 结果

```text
universal_gap_state_count: 165
universal_gap_coordinate_count: 448
group_count: 433
group_prime_count: 108

total excess demand: 1348
ordered layer capacity: 1039
ordered excess overload groups: 218 / 433
maximum ordered excess ratio: 3

total positive deficit demand: 886
ordered deficit overload groups: 121 / 433
maximum ordered deficit ratio: 2.5

unit demand overload groups: 0 / 433
```

若按不同模数去重，层容量降为 539，溢出层超载组为 429/433，最大比值为 6；这只是
更紧的诊断，不作为主结论，因为同一模数可能有多个合法有序源状态。

## 逻辑边界

上述超载不能直接推出选择器定理。尚缺的唯一关键桥梁是一个选择不变的算术映射：

> 若目标仿射格的最小表示在 q 坐标上超出指数预算 (e_q) 层，则任何合法的目标—终端
> 选择、源重分配或可提升递降，必须在同一核心素数的线性载体上消耗至少相应的 q 进高度，
> 或者产生一个严格下降的替代状态。

当前数据只证明了高度缺口对固定状态和颜色选择具有普适性；它没有证明盒外坐标与载体
高度之间的算术对应，也没有排除把溢出转移到另一个模数、标签或源族。因此：

- 总溢出层超载是一个条件性跨状态容量压力；
- 单位需求无超载说明不能只用“每个失败状态占一个槽位”的粗模型；
- 若无法证明逐层收费，应优先寻找把未收费层转成严格可提升下降的公式。

## 复现

```bash
python3 reproductions/type_i_f_overflow_cross_state_qadic_capacity.py
```

输入哈希：

```text
62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

结果文件：

```text
reproductions/type-i-f-overflow-cross-state-qadic-capacity-results.json
```

结果文件 SHA-256：

```text
822c7aa344271b272d51503f79fd52b9199cf34cf2c7b9b2ba84434cc6a38ccd
```
