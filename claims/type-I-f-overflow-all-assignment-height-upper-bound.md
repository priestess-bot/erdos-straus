---
kind: claim
claim_id: type-I-f-overflow-all-assignment-height-upper-bound
title: 方向编码下的 F 溢出反事实重复高度审计
statement: 对冻结的253个平方终端F状态，脚本记录506个满足活跃方向基线的有向编码；冻结输入中每个状态只有一个无序物理源对及其两个方向编码，故506=253×2，不是506个独立物理选择。脚本随后忽略方向标签，并让每个溢出素因子读取同一源对两块中较高的q进高度；固定(a,s)时这条逐q最大向量可同时实现，但这些高度已经包含在K中，且没有建立从overflow到这些高度的代数注入。历史字段仍给出165个no_assignment状态、88个some_assignment状态，以及1701层中的1348层unsupported；这些数字只是不改变数据的反事实重复高度应力测试，不能解释为选择不变的容量缺口或严格下降。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-multi-support-height-boundary
  - type-I-f-square-terminal-overflow-support-alignment
  - type-I-f-current-block-saturation-and-signed-denominator-defect
topics:
- type-I
- F-state
- overflow-radius
- q-adic
- capacity
- source-selection
- descent
- proof-program
sources:
- claim: type-I-f-overflow-multi-support-height-boundary
  role: deterministic-height-boundary
- claim: type-I-f-square-terminal-relation-certificate
  role: finite-box-certificate
visibility: public
last_checked: '2026-07-30'
---

# 方向编码下的 F 溢出反事实重复高度审计

## 编码语义与历史模型

输入是 253 个平方终端 F 状态及其半径不超过 6 的首个目标仿射格见证。脚本枚举同一
核心素数、同一模数 \(R\) 下满足 Fourier 活跃方向最低高度要求的源/方向编码。对冻结
输入的审计表明，每个状态恰有一个无序物理源对 \(\{a,s\}\)，以及交换源方向和活跃
方向得到的两个有向编码。因此

\[
506=253\times2
\]

是方向编码数，不是 506 个独立物理源选择。后续高度循环把方向变量解包为
`_directions` 后不再使用，所以同一状态的两个编码产生完全相同的高度判定；结果中的
176 个 `assignment_can_carry_all_excess` 也正是 88 个状态各重复计数两次。

对每个溢出素因子 (q)，不强制它使用 (q_a) 或 (q_s) 的指定颜色，而是允许它在
两个源块中自由选择高度较高者：

\[
h_q^{\max}(a,s)=
\max\bigl(v_q(aR+1),v_q(sR+1)\bigr).
\]

固定 \((a,s)\) 时，全部 \(h_q^{\max}\) 都由同一对源块同时确定。因此逐 \(q\) 混合
颜色读取最大值虽然不再是一条指定颜色的载体分配，却没有跨坐标的物理源不相容问题。

但它也不是已证明的真实载体能力上界。记

\[
U=aR+1,\qquad V=sR+1.
\]

在这些平方终端上 \(UV=4K\)，故对每个奇支撑素数 \(q\)，

\[
v_q(K)=v_q(U)+v_q(V).
\]

见证 overflow 是超过 \(v_q(K)\) 的指数层；再把
\(\max(v_q(U),v_q(V))\) 当作可承担的额外高度，会重复使用已经吸收到 \(K\) 的当前块
因子。脚本没有构造把 overflow 层注入这些高度的代数映射。因此这里的比较只能称为
反事实重复高度应力测试，不能推出真实载体的充分性或必要性。

## 结果

结果文件
`reproductions/type-i-f-overflow-all-assignment-height-upper-bound-results.json` 的
SHA-256 为

```text
62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5
```

摘要为：

```text
state_count: 253
total_admissible_assignment_count: 506
overflow_layer_count: 1701
universally_unsupported_excess_layer_count: 1348
state_category_counts:
  no_assignment_can_carry_all_excess: 165
  some_assignment_can_carry_all_excess: 88
assignment_can_carry_all_excess_count: 176
assignment_can_carry_baseline_plus_excess_count: 0
```

全部 253 个状态都有两个满足活跃基线的有向编码。历史分类中，165 个状态的两个编码
都落入 `no_assignment_can_carry_all_excess`，88 个状态的两个编码都落入
`some_assignment_can_carry_all_excess`；这解释了总计 176 条“可承担”编码。字段
`universally_unsupported_excess_layer_count: 1348` 同样按原算法和命名保留。这里的
`overflow_layer_count: 1701` 按 253 个物理状态各计一次；下游逐方向高度审计中的
(3402=2\times1701) 则把每个状态的两个等价方向编码都计入，二者不是不同的溢出样本。

这些标签应按脚本的反事实模型阅读：165/88 是同一物理源对的重复高度比较结果，不是
在多个独立源选择之间得到的选择不变量；“unsupported”也不表示已经证明真实容量不足。

## 研究含义与边界

这项审计仍可作为有限应力测试：它保留了哪些首见证在反事实重复高度尺度上较远，并可
用于选择后续例子。但它没有给出选择不变的载体缺口，更没有把缺口转化为跨状态容量
矛盾或严格下降。若要恢复容量含义，必须另行给出来自新状态或外部资源的高度，以及从
盒外关系向量到该资源的显式代数注入。

该审计只覆盖已在半径 6 内找到首见证的 253 个状态。逐坐标最大高度能够由固定源对
同时读出，所以“忽略不同溢出坐标之间的竞争”不是这里的决定性缺陷；决定性缺陷是
当前高度已经包含在 \(K\) 中且缺少 overflow 注入。故它既不是选择不变的必要性边界，
也不是最终容量定理。

## 复现

```text
python3 reproductions/type_i_f_overflow_all_assignment_height_upper_bound.py
```

脚本锁定 Fourier、分色、溢出、平方终端四个输入哈希，并枚举每个状态的源/方向编码。
本页保留脚本输出的历史字段名，但不再把 `assignment`、`carry` 或 `unsupported` 解释为
已经建立的物理载体语义。
