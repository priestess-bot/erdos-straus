---
kind: claim
claim_id: type-I-f-overflow-three-channel-capacity
title: F 溢出的块—模数差—标签差三通道容量边界
statement: 对冻结的 165 个普适高度缺口状态，同时允许 q 进需求使用当前块高度、完整源谱模数差高度或标签差高度三类通道，并允许各通道独立叠加。标量需求 1348 对应的最乐观三通道容量为 4396，仍有 85/433 个组超载；联合需求 15659 对应的逐坐标通道和容量为 12338，仍有 56/164 个支持组超载，最大比值 37.5。该结果是高度放宽下的条件性压力边界，不证明盒外关系向量必须支付任一通道。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-universal-joint-capacity
  - type-I-cross-state-q-adic-capacity-bound
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
  - type-I-linear-cross-label-independent-joint-capacity
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- q-adic
- capacity
- label-collision
- modulus-collision
- cross-state
- descent
- proof-program
sources:
- claim: type-I-cross-state-q-adic-capacity-bound
  role: nested-difference-capacity-interface
- claim: type-I-linear-hybrid-label-modulus-q-adic-capacity
  role: label-modulus-collision-interface
visibility: public
last_checked: '2026-07-30'
---

# F 溢出的块—模数差—标签差三通道容量边界

## 输入与通道

输入锁定为全部合法载体分配下的 165 个普适高度缺口状态：

```text
input: type-i-f-overflow-all-assignment-height-upper-bound-results.json
sha256: 62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

对每个普适缺口坐标 ((p,q))，需求为其所有状态的溢出层数之和。对同一核心素数的
完整线性源谱，给每个有序源状态三个独立的乐观高度通道：

1. **块通道**：
   (max(v_q(aR+1),v_q(sR+1)))；
2. **模数差通道**：当前 (R) 与完整源谱其它模数的
   (q)-进差值高度最大值；
3. **标签差通道**：当前块标签 (a,s) 与完整源谱其它标签的 (q)-进差值高度最大值。

模数差和标签差通道均使用整个核心素数的完整源谱，而不限制在当前需求的 (R) 窗口
内，因此已经是明显放宽的容量模型。标量模型把三通道相加；联合模型对一个支持集合
(S) 使用

\[
\prod_{q\in S}(h_q^{\mathrm{block}}
+h_q^{\mathrm{mod}}
+h_q^{\mathrm{label}}),
\]

允许每个坐标独立选择任意通道及其组合。

## 结果

```text
universal_gap_state_count: 165
scalar_group_count: 433
joint_group_count: 164

scalar demand: 1348
block capacity: 1039
modulus-difference capacity: 1547
label-difference capacity: 1810
three-channel additive capacity: 4396
three-channel additive overloads: 85/433
maximum scalar ratio: 3

joint demand: 15659
joint three-channel capacity: 12338
joint overloads: 56/164
maximum joint ratio: 37.5

coordinatewise max-channel joint capacity: 1204
coordinatewise max-channel overloads: 109/164
maximum ratio: 360
```

即使把块、模数差、标签差三个资源池完全相加，并允许每个联合坐标独立选择通道，
联合需求仍在 56 个支持组中超过容量。这比只使用当前块高度的压力边界更宽松，说明
简单地把缺口转移到已有标签差或模数差资源，不能自动消除当前冻结的多坐标缺口。

## 逻辑边界

该结果不能直接推出跨状态选择器，原因是：

1. 尚未证明关系格盒外坐标必须支付块、模数差或标签差中的任何一个通道；
2. 三通道相加会重复计数同一算术资源，联合乘积还进一步允许不相容的通道组合；
3. 模数差、标签差高度取自完整源谱，可能对应不同的状态对，尚未建立需求与资源的
   唯一匹配；
4. 输入只覆盖半径六以内冻结见证的普适缺口。

因此可靠结论是：容量桥的剩余困难已经从“是否有足够的资源”缩小为“能否证明联合
关系向量至少收费某一通道，并控制不同通道的重复使用”。若该收费映射不存在，就应
把这类无法匹配的联合向量转成严格可提升的算术下降。

## 复现

```bash
python3 reproductions/type_i_f_overflow_three_channel_capacity.py
```

结果文件：

```text
reproductions/type-i-f-overflow-three-channel-capacity-results.json
```

结果文件 SHA-256：

```text
71cd0a5ad435ee4339e98181b3c9123813b1ba3fbfe2b2662a08c0998dd90204
```
