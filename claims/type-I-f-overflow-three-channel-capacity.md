---
kind: claim
claim_id: type-I-f-overflow-three-channel-capacity
title: F 溢出的块—模数差—标签差三通道反事实压力边界
statement: 对历史重复高度代理筛出的165个状态，脚本把完整源谱块高度、模数差和标签差三类数值通道独立叠加，得到标量需求1348对代理容量4396及85/433组数值超载，联合需求15659对代理容量12338及56/164组数值超载。块通道中与需求同状态的部分直接重复K_R中的因子，异状态部分则只是K_{R'}中的未配型潜在外部资源；差值通道同样没有分母缺陷注入或真实迁移边。因此这些有限数字只描述高度放宽的条件性压力，不能证明资源超载、收费析取或递降，也不能仅凭当前块饱和排除异状态资源的后续用途。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-universal-joint-capacity
  - type-I-cross-state-q-adic-capacity-bound
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
  - type-I-linear-cross-label-independent-joint-capacity
  - type-I-f-current-block-saturation-and-signed-denominator-defect
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

# F 溢出的块—模数差—标签差三通道反事实压力边界

## 输入与通道

输入锁定为历史方向编码和重复当前高度代理筛出的 165 个状态：

```text
input: type-i-f-overflow-all-assignment-height-upper-bound-results.json
sha256: 62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

对每个代理缺口坐标 \((p,q)\)，历史需求为其所有首见证溢出层数之和。对同一核心素数的
完整线性源谱，脚本给每个有序源状态三个独立的数值通道：

1. **块通道**：
   (max(v_q(aR+1),v_q(sR+1)))；
2. **模数差通道**：当前 (R) 与完整源谱其它模数的
   (q)-进差值高度最大值；
3. **标签差通道**：当前块标签 (a,s) 与完整源谱其它标签的 (q)-进差值高度最大值。

块通道中，与需求记录相同的 (R) 和物理源对所给高度已经包含在 (K_R) 中，不能再次
支付该记录的盒外分母缺陷；来自 (R'\ne R) 的块高度则包含在 (K_{R'})，是尚未证明
可通过合法转移调用的潜在外部资源，而不是由饱和恒等式自动排除的同一因子。模数差和
标签差通道只记录差值赋值，同样没有建立两端实际载体或解提升。三者均使用整个核心素数
的完整源谱而不限制在当前需求的 (R) 窗口内，因此这里只是明显放宽的应力模型。标量
模型把三通道相加；
联合模型对一个支持集合
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

把三种数值通道完全相加并允许每个联合坐标独立选择后，旧账本仍在 56 个支持组中数值
超载。这只说明该反事实模型不能自动吸收冻结首见证，不说明三个真实资源池存在或竞争。

## 逻辑边界

该结果不能直接推出跨状态选择器，原因是：

1. 同状态块通道已经排除为可重复支付；异状态块高度、模数差和标签差都尚未通过合法
   转移与分母缺陷配型；
2. 三通道相加会重复计数同一算术资源，联合乘积还进一步允许不相容的通道组合；
3. 模数差、标签差高度取自完整源谱，可能对应不同的状态对，尚未建立需求与资源的
   唯一匹配；
4. 输入只覆盖半径六以内冻结见证的普适缺口。

因此可靠结论只是：若要恢复容量路线，必须从带符号缺陷推导一个满足精确 \(q\)-进提升
剩余类的外部通道，并证明真实迁移和有界重复度。若该映射不存在，就应把联合缺陷转成
严格可提升的算术下降。

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
