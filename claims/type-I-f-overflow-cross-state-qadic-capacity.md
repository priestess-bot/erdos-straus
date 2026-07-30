---
kind: claim
claim_id: type-I-f-overflow-cross-state-qadic-capacity
title: 同状态重复与异状态未配型的跨状态 q 进压力边界
statement: 对历史重复高度代理筛出的165个F状态，脚本把448个(p,q)坐标归并为433组：按总超额层收费得到需求1348、代理高度1039和218/433组数值超载；再次减需求状态当前块最高高度后得到代理需求886和121/433组数值超载。奇q处需求状态自身的当前块高度已经包含在K_R中，再次抵扣属于直接重复；窗口内R'不等于R的块高度则属于另一K_{R'}，只能视为尚未配型的潜在外部资源，不能仅由饱和恒等式排除，也不能在缺少合法转移、相位匹配、资源竞争和有界重复度证明时计为真实容量。因此这些有限数字只是混合了同状态重复与异状态未配型资源的条件性账本，不是选择不变容量、跨状态资源超载或递降证书。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-cross-state-q-adic-capacity-bound
  - type-I-f-current-block-saturation-and-signed-denominator-defect
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

# 同状态重复与异状态未配型的跨状态 q 进压力边界

## 审计对象

输入是[方向编码下的 F 溢出反事实重复高度审计](type-I-f-overflow-all-assignment-height-upper-bound.md)。
只保留历史字段 `no_assignment_can_carry_all_excess` 的 165 个状态。该字段来自每个
物理源对的两个方向编码以及重复当前高度的比较，不再解释为穷尽合法物理分配后的真实
容量缺口。对每个状态的每个
`universally_unsupported_excess` 坐标 ((q,e_q))，记录：

1. 总溢出需求 (e_q)；
2. 再次减去该状态当前块最高高度 \(h_q^{max}\) 后的历史代理值
   \(e_q-h_q^{max}>0\)；
3. 一个仅表示“该状态需要 q 载体”的单位需求。

共得到 448 个坐标需求，按核心素数和 (q) 归并为 433 组，涉及 108 个核心素数。

## 同状态重复与异状态未配型账本

对固定组 ((p,q))，取该组出现的模数窗口
([R_{min},R_{max}])。在窗口内枚举 (p) 的完整线性源状态
((a,s,R'))，并令

[
h_q(a,s,R')=max{v_q(aR'+1),v_q(sR'+1)}.
]

将所有有序源状态的 \(h_q\) 相加，得到历史字段 `ordered_layer_capacity`。这项总和必须
按资源状态与需求状态是否相同分开解释：

- 当资源记录就是需求记录的同一 (R)、同一物理源对时，
  \((aR+1)(sR+1)=4K_R\)，奇 (q) 高度已经包含在 (K_R) 中；从 (e_q) 再扣一次是
  直接重复。
- 当资源来自 (R'\ne R) 或并未出现在需求记录中的另一源状态时，其高度包含在
  (K_{R'}) 而非 (K_R)。它可能在另行构造的合法跨状态提升中成为外部资源，但当前
  脚本没有给出状态转移、相位匹配、解提升、共同竞争或有界重复度，因而只能称为未配型
  候选高度，不能计作已证明可用容量。

原算法还作了以下额外放宽：

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

上述数值超载不能直接推出选择器定理，也不能作为真实容量矛盾：账本同时混有同状态
直接重复和异状态未配型候选。真正缺少的桥梁是一个
从带符号分母缺陷到 \(K\) 外新资源或合法新状态的算术映射：

> 若目标仿射格的一个定向分母缺陷需要额外 \(q^e\)，则构造必须在 \(K\) 外引入满足
> 模 \(q^{\nu_q+e}\) 清分母剩余类的新乘子或合法新状态，或者产生独立证书或严格下降。

当前数据只冻结了旧代理的数值分组；它没有证明盒外坐标与外部资源之间的算术对应。
因此：

- 总溢出层超载只是混合代理账本中的数值压力；
- 单位需求无超载说明不能只用“每个失败状态占一个槽位”的粗模型；
- 对异状态高度必须先证明合法转移、相位合同和资源有界重复度；若无法实现外部
  \(q\)-进提升剩余类，应优先寻找把未付分母层转成严格可提升下降的公式。

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
