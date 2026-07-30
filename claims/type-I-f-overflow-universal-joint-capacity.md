---
kind: claim
claim_id: type-I-f-overflow-universal-joint-capacity
title: 普适多坐标溢出的联合层容量压力边界
statement: 对冻结的 165 个普适高度缺口状态，将每个状态的普适溢出向量 e 按联合层需求 prod_q e_q 收费，并在完整线性源状态中允许每个坐标独立选择两个载体块的较高 q 进高度。165 个状态归并为 164 个支持组，其中 143 个状态有至少两个普适缺口坐标；联合需求为 15659，而这种独立颜色放宽容量为 358，142/164 组超载，最大需求/容量比为 937.5。该结果是条件性跨状态压力边界，不证明溢出向量必然消耗同一 q 进载体，也不构成全称选择器。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-linear-multi-active-joint-divisor-capacity
  - type-I-linear-cross-label-independent-joint-capacity
  - type-I-f-overflow-universal-support-profile
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- multi-active
- q-adic
- capacity
- cross-state
- descent
- proof-program
sources:
- claim: type-I-linear-multi-active-joint-divisor-capacity
  role: same-block-joint-capacity-interface
visibility: public
last_checked: '2026-07-30'
---

# 普适多坐标溢出的联合层容量压力边界

## 审计范围

输入锁定为全部合法载体分配的普适高度缺口结果：

```text
input: type-i-f-overflow-all-assignment-height-upper-bound-results.json
sha256: 62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

只保留 `no_assignment_can_carry_all_excess` 的 165 个状态。每个状态的普适缺口坐标
\(q\) 有一个超额层数 \(e_q\ge1\)，并令其联合需求为

\[
D_{\mathrm{joint}}(e)=\prod_{q\in S}e_q.
\]

这是把各坐标的层数看成同时出现的联合层元组；它比逐坐标的
\(\sum_qe_q\) 收费更强，也与多活跃联合层析的乘法结构相匹配。需要注意，165 个状态中
有 22 个只有一个普适缺口坐标，真正的多坐标普适缺口为 143 个状态、142 个支持组；
它们之外的 22 个状态仍作为退化基线保留。

## 容量模型

对同一核心素数 \(p\)、同一支持集合 \(S\) 的状态，取其 \(R\) 的最小闭区间。对区间内
每个完整线性源状态 \((a,R,s)\)，写

\[
h_q^a=v_q(aR+1),\qquad h_q^s=v_q(sR+1).
\]

使用三种容量作边界比较：

\[
C_{\mathrm{ind}}
=
\sum_{(a,R,s)}\prod_{q\in S}\max(h_q^a,h_q^s),
\]

其中每个坐标可以独立选择较高的颜色；这是最乐观的容量放宽，甚至不要求所有坐标
来自同一块；

\[
C_{\mathrm{same}}
=
\sum_{(a,R,s)}\max\left\{
\prod_{q\in S}h_q^a,
\prod_{q\in S}h_q^s
\right\},
\]

要求一整个联合层来自同一块；以及每个模数只保留最佳源状态的容量，用来区分有序状态
重复计数造成的影响。

## 结果

```text
universal_gap_state_count: 165
single-coordinate universal-gap states: 22
multi-coordinate universal-gap states: 143
group_count: 164
multi-coordinate group_count: 142
support_size_histogram: 1: 22, 2: 53, 3: 46, 4: 35, 5: 8

joint_demand: 15659
independent_color_capacity: 358
same_block_capacity: 102
distinct_modulus_independent_capacity: 179

independent-color overloads: 142/164
independent-color maximum ratio: 937.5
same-block overloads: 25/164
same-block maximum ratio: 75
distinct-modulus independent overloads: 164/164
distinct-modulus maximum ratio: 1875

multi-coordinate joint_demand: 15614
multi-coordinate independent_color_capacity: 312
multi-coordinate same_block_capacity: 56
multi-coordinate independent-color overloads: 142/142
```

这里的独立颜色模型已经允许每个坐标分别使用 \(aR+1\) 或 \(sR+1\) 中较高者，仍有
142 个支持组超载。因此，若能证明一个普适的“联合溢出层 => 联合载体层”
映射，单坐标容量桥将被严格增强为多坐标容量矛盾。

## 逻辑边界

本审计不能直接推出跨状态矛盾，必须保留以下缺口：

1. 关系格盒外向量的多个坐标未证明必须同时消耗 \(\prod_qe_q\) 个载体层；
2. 独立颜色容量是放宽模型，真实载体可能需要同块或固定颜色；
3. 按 \(R\) 区间聚合会把不同状态的需求放在同一账本中，尚未证明这些状态必须竞争同一
   个算术资源；
4. 165 个状态来自半径六以内的冻结见证，不能解释为所有可能见证的穷尽。

所以可靠结论是：普适缺口的自然下一对象是“带符号的联合溢出映射”，而不是继续把
每个坐标独立收费。若该映射不能建立，应转向从联合关系向量构造严格可提升的算术下降。

## 复现

```bash
python3 reproductions/type_i_f_overflow_universal_joint_capacity.py
```

结果文件为：

```text
reproductions/type-i-f-overflow-universal-joint-capacity-results.json
```

结果文件 SHA-256：

```text
23d44907d7e01884e00ccb7ffbd2dd93b0376a4c755ca1315e26f41cc0df2aa2
```
