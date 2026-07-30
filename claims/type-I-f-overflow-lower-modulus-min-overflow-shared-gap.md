---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-min-overflow-shared-gap
title: 低模数最小溢出纤维的共享缺口 Type II 覆盖边界
statement: 对冻结的 42 个 lower-modulus F-box miss，成本 9 壳层已给出 36 个状态的精确单位权最小溢出 Omega_1。完整重枚举这 36 个状态的 204 个并列最优向量后，字典序规范向量的共享缺口 Type II 旁路覆盖 14/36 个状态，而全部并列最优向量的并集覆盖 18/36 个状态（17 个不同素数）；新增 4 个状态仅由非规范并列向量命中。其余 18 个已审计状态在整个最小层上无命中；另 6 个状态的 Omega_1 后续虽已精确补齐为 10--18，但其更高最小层尚未纳入本共享缺口审计，不能计为失败。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-profile
  - type-I-f-overflow-lower-modulus-shared-gap-type-II-lift
  - type-II-coprime-factor-normal-form
  - type-I-f-overflow-repair-transition-potential-boundary
topics:
- type-I
- F-state
- lower-modulus
- minimum-overflow
- tied-minimizers
- shared-gap
- type-II
- normal-form
- finite-audit
- proof-program
sources:
- claim: type-I-f-overflow-lower-modulus-weighted-cost-profile
  role: exact-minimum-shell-input
- claim: type-I-f-overflow-lower-modulus-shared-gap-type-II-lift
  role: shared-gap-interface
- claim: type-II-coprime-factor-normal-form
  role: complete-Type-II-test
- claim: type-I-f-overflow-repair-transition-potential-boundary
  role: exact-unit-cost-completion-beyond-cap-nine
visibility: public
last_checked: '2026-07-30'
---

# 低模数最小溢出纤维的共享缺口 Type II 覆盖边界

## 审计对象

对一个低模数 F-box miss，设

\[
\Omega_1(t)=\min\left\{
 \sum_i(|z_i|-\nu_i)_+:
 \prod_iq_i^{z_i}\equiv-1\pmod t
\right\}.
\]

作为本脚本冻结输入的有限剖面已精确求出 36 个状态的 \(\Omega_1\)，其余 6 个当时
只知道 \(\Omega_1\ge10\)。本次对每个已解析状态重新枚举**整个精确最小层**，而不是
只读取保存的字典序向量。对每个最优向量写

\[
\frac ab=\prod_iq_i^{z_i},\quad (a,b)=1,\quad t\mid a+b.
\]

随后枚举全部

\[
h\mid a+b,\quad h\equiv3\pmod4,\quad 3\le h\le p-2,
\tag{1}
\]

并对 \(x_h=(p+h)/4\) 独立枚举全部 \(d\mid x_h^2\)、\(d\le x_h\)，检查

\[
h\mid x_h+d.
\tag{2}
\]

每个命中还恢复互素正规形

\[
x_h=ABC,\quad d=A^2C,\quad (A,B)=1,\quad A\le B,\quad h\mid A+B,
\]

并直接验证三项单位分数恒等式。因此 (1) 只负责生成共享缺口候选，Type II 命中始终
由 (2) 和正规形独立确认。

## 规范向量与全部并列最优向量

冻结的 36 个精确状态共有 204 个最优向量。对合
\(z\mapsto-z\) 保持目标关系和溢出代价，并交换 \(a,b\)，所以这些向量组成 102 对，
每对有同一个 \(a+b\)。逐状态共有 102 个不同和；跨状态合并后有 101 个不同整数。

审计统计为：

~~~text
resolved_minimum_state_count: 36
unresolved_minimum_state_count: 6
minimum_vector_count: 204
minimum_inverse_pair_count: 102
canonical_candidate_gap_count: 344
all_minimum_candidate_gap_count: 774
distinct_prime_gap_check_count: 731

canonical_state_hit_count: 14
canonical_prime_hit_count: 13
all_minimum_state_hit_count: 18
all_minimum_prime_hit_count: 17
tied_minimum_only_state_hit_count: 4
resolved_minimum_layer_miss_count: 18
~~~

这给出一个严格的选择器结论：只保留字典序代表会漏掉 4 个状态；若把整个
\(\Omega_1\)-最小纤维作为选择对象，覆盖从 \(14/36\) 提升到 \(18/36\)。四个新增
状态为：

| \(p\) | 方向 | \(t\) | \(\Omega_1\) | 非规范向量命中的共享缺口 |
|---:|:---:|---:|---:|:---|
| 223474729 | reverse | 233 | 8 | 19, 63 |
| 306963409 | forward | 125 | 1 | 367 |
| 549401449 | reverse | 617 | 2 | 19, 27 |
| 570621769 | reverse | 113 | 8 | 83, 87, 119, 1559 |

## 全部 18 个命中状态

| \(p\) | 方向 | \(t\) | \(\Omega_1\) | 最优向量数 | 规范向量命中 | 全纤维命中缺口 |
|---:|:---:|---:|---:|---:|:---:|:---|
| 106050289 | forward | 97 | 1 | 6 | 是 | 31 |
| 152498329 | reverse | 9377 | 7 | 4 | 是 | 151 |
| 155533849 | forward | 89 | 1 | 4 | 是 | 51 |
| 171292489 | forward | 1149 | 1 | 4 | 是 | 115, 383 |
| 171292489 | reverse | 2681 | 1 | 2 | 是 | 383 |
| 223474729 | reverse | 233 | 8 | 12 | 否 | 19, 63 |
| 236164009 | reverse | 2793 | 1 | 2 | 是 | 171 |
| 306963409 | forward | 125 | 1 | 16 | 否 | 367 |
| 331117609 | forward | 15413 | 4 | 2 | 是 | 31 |
| 356491249 | reverse | 43865 | 5 | 2 | 是 | 31 |
| 373561609 | reverse | 737 | 1 | 2 | 是 | 51, 67 |
| 408626089 | forward | 177 | 1 | 6 | 是 | 59 |
| 473173969 | reverse | 32581 | 2 | 2 | 是 | 31 |
| 507599689 | reverse | 813 | 6 | 4 | 是 | 51 |
| 542688169 | reverse | 5617 | 4 | 4 | 是 | 39 |
| 549401449 | reverse | 617 | 2 | 8 | 否 | 19, 27 |
| 559650361 | reverse | 329 | 2 | 4 | 是 | 47 |
| 570621769 | reverse | 113 | 8 | 42 | 否 | 83, 87, 119, 1559 |

25 个“状态—缺口”命中共对应 57 张状态内 Type II 正规形证书；消除同一素数不同
状态间的重复后，是 24 个不同的 \((p,h)\) 和 56 张不同证书。

## 完整性证据

复现脚本与结果：

~~~text
reproductions/type_i_f_overflow_lower_modulus_min_overflow_shared_gap.py
reproductions/type_i_f_overflow_lower_modulus_min_overflow_shared_gap_results.json
~~~

冻结的加权剖面输入及 SHA-256：

~~~text
type-i-f-overflow-lower-modulus-weighted-cost-results.json
e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82
~~~

本次脚本与结果 SHA-256：

~~~text
script: 5557ec9d3cc989a92e22d0e624f306c92d66184a854feb6ff45b4495ace10352
result: 085a65615fcd2cc1e30330e4039483f36491871c41cad11d54123514a3f2852f
~~~

完整性检查分四层：

1. 按精确溢出层重新枚举并验证目标同余，且断言字典序首向量与冻结代表一致；
2. 每个 \(a+b\) 的因子分解先精确重构，再对小素因子做试除证明，对较大素因子递归生成
   Lucas \(n-1\) 素性证书；本次共有 250 个试除叶和 135 个递归 Lucas 证书；
3. 从已证明的完整素因子分解生成所有因子，因此 774 个逐状态合法缺口候选不是限界试除；
4. 对 731 个不同 \((p,h)\) 完整枚举 \(x_h^2\) 的可采纳除子，并核对正规形和单位分数
   恒等式。

复现命令：

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_min_overflow_shared_gap.py
~~~

## 六个未纳入最小层审计的状态

下列状态在本脚本的成本 9 输入中没有精确最小层，所以没有被当成旁路失败：

~~~text
(p, t, orientation)
(62704849, 649, forward)
(75056809, 21113, reverse)
(310002289, 107977, reverse)
(312918169, 16649, forward)
(366108649, 11057, forward)
(373561609, 208577, forward)
~~~

后续 Cayley 图算法已经精确求出其单位权最小值，按上表顺序分别为
\(12,11,18,10,12,15\)。但知道标量 \(\Omega_1\) 不等于已经枚举该层的全部并列
目标向量；本卡尚未对这六个更高最小层执行共享缺口 Type II 完整审计。

**后续更新（2026-07-30）**：
[六个高成本状态的完整单位最小面与共享缺口边界](type-I-f-overflow-lower-modulus-high-cost-minimum-face.md)
已经完整枚举这六层的 36 个最小向量。它们不再是“未解析最小面”；其中 3 个状态命中、
3 个状态完整最小面遗漏。原卡此处保留的是当时脚本的审计边界。

## 证明边界与研究含义

本卡证明的是冻结样本上的**最小溢出纤维有限覆盖边界**，不是全称提升定理。对 18 个
已解析未命中状态，可以严格排除整个 \(\Omega_1\)-最小层的这一共享缺口接口；仍不能
排除更高溢出层、不同权重、因子重分配或其它递降。本卡自己的脚本没有枚举六个高成本
状态的全部并列最小向量；该缺口现已由上面的后续主张卡补齐，但同样不排除更高层或其它
证书机制。

另一方面，4 个仅由非规范并列向量命中的状态说明：规范单向量不是稳定的统一选择器。
下一步若继续沿这条路线，应把“目标纤维的最小面”或 Pareto 最小集合保留下来，再在该
集合上使用 Type II 碰撞或 \(q\)-进容量作为第二级选择准则；仅更换字典序 tie-break 不会
得到选择不变的证明。
