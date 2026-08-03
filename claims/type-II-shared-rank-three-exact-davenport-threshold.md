---
kind: claim
claim_id: type-II-shared-rank-three-exact-davenport-threshold
title: 共享 Type II 秩三精确 Davenport 阈值与 no-force 边界
statement: 设合法缺口 m 已有 Type II 证书，且 p+m 中与 m 互素的素因子残数生成子群具有不变因子 C_2 直和 C_{2a} 直和 C_{2ab}。则精确 Davenport 阈值为 D=2a+2ab；若单位素因子多重序列长度 t>=D，则存在非空共享除子 D_I=1 mod m，并可重建 scaled-first marked witness。若 t<D，则仅得到 Davenport 阈值未触发的 no-force 边界，不推出没有更短零积。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-shared-higher-rank-sequence-short-profile
  - type-II-shared-rank-two-davenport-threshold
  - type-II-two-tail-deflation-descent
topics:
- type-II
- shared-divisor
- finite-abelian-groups
- rank-three-groups
- davenport-constant
- zero-sum-theory
- marked-lift
- proof-boundary
sources:
  - paper: girard_schmid2019_direct_zero_sum_rank_three
    locator: "Theorem 2.7"
    role: exact rank-three Davenport formula
  - paper: schmid2011_c2_squared_c2n
    locator: "Section 3.5"
    role: independent m=1 subfamily source
  - reproduction: reproductions/type_ii_automatic_residual_k1_funnel.py
    role: invariant-factor recovery and marked-witness reconstruction
  - result: reproductions/type-ii-automatic-residual-rank-three-exact-davenport-profile-10m-results.json
    role: focused 10M threshold profile
visibility: public
last_checked: '2026-08-04'
---

# 共享 Type II 秩三精确 Davenport 阈值与 no-force 边界

## 精确群论输入

若单位残数生成子群具有不变因子

\[
H\simeq C_2\oplus C_{2a}\oplus C_{2ab},
\quad a,b\ge1,
\]

Girard--Schmid 的 Theorem 2.7 给出

\[
D(H)=2a+2ab.
\]

把 \(p+m\) 中与 \(m\) 互素的素因子按重数视为 \(H\) 中的序列。若序列长度至少为
\(D(H)\)，Davenport 定理给出非空子序列积为单位元，即存在

\[
D_I>1,\quad D_I\mid p+m,\quad D_I\equiv1\pmod m.
\]

和已有 Type II 证书组合后，现有 scaled-first 重建器给出 marked witness。

## 当前压力点

10M、\(m\le239\) 的 19 个秩三缺口全部属于两种群：

| 不变因子 | 参数 | 精确阈值 | 当前状态 |
|---|---:|---:|---|
| \(C_2\oplus C_2\oplus C_{30}\) | \(a=1,b=15\) | \(32\) | 17 个均未达到 |
| \(C_2\oplus C_4\oplus C_{12}\) | \(a=2,b=3\) | \(16\) | 2 个均未达到 |

因此本 profile 的阈值命中数为 0；这不是反例，而是严格说明当前这些有限序列不能
依靠 Davenport 阈值自动产生共享除子。现有动态短零积 profile 的 4 个命中仍然是
低于阈值的额外结构，须与本阈值分支分开登记。

## 边界

该卡只闭合一个精确群论分支。它不处理其它秩三群、阈值以下的短零积、跨缺口联合
避靶，也不把 marked Type II 表示升级为无标记递降。因而它收紧了 Type II 余项的
分类，但不关闭 overflow 或 Erdős--Straus 猜想。

## 复现

```bash
python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
  --limit 10000000 --gap-cap 239 \
  --rank-three-exact-davenport-profile \
  --output reproductions/type-ii-automatic-residual-rank-three-exact-davenport-profile-10m-results.json
```
