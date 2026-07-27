---
kind: claim
claim_id: type-II-h19-external-source-conditional-escape
title: H19 加六条完整平方因子外部源递降的条件性逃逸
statement: 令 Q19=77597520，r=8328961，并取 p=3Q19*m+r。对 H19 的二层一私有因子分支与 k=1,2,3,4,5,6 的外部源余商，存在 26 条原始且可采纳的正仿射线性型。若它们同时为素数，则前十九条规范 Type II 射线全部失败，且六条完整平方因子外部源递降的除子残数目标也全部缺失。故在 Dickson 素数元组猜想或相应 Schinzel 假设下，无穷多个核心素数同时逃过 H19 和这六条严格递降族。这不构成 Erdős--Straus 猜想的条件性反例。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- admissibility
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 加六条完整平方因子外部源递降的条件性逃逸

## 分支

令

\[
Q=Q_{19}=77\,597\,520,\qquad r=8\,328\,961,\qquad
p=3Qm+r. \tag{1}
\]

该 \(r\) 是 H19 一层安全剩余类；取二层 \(n\equiv0\pmod3\)，H19 的 \(p\) 和
19 个射线余商给出 20 条可采纳线性型。

对

\[
k\in\{1,2,3,4,5,6\},\qquad q_k=4k-1,
\]

外部源为

\[
n_k=\frac{q_kp+1}{4k}=D_kL_k(m), \tag{2}
\]

其中 \(L_k\) 是如下额外线性型的值：

| \(k\) | \(D_k\) | \(L_k(m)\) |
|---:|---:|---|
| 1 | 13 | \(13430340m+480517\) |
| 2 | 11 | \(18517590m+662531\) |
| 3 | 1 | \(213393180m+7634881\) |
| 4 | 1 | \(218243025m+7808401\) |
| 5 | 7 | \(31593276m+1130359\) |
| 6 | 1 | \(223092870m+7981921\) |

对充分大的 \(m\)，若 \(L_k(m)\) 为素数，它不与固定 \(kD_k\) 有公共素因子。
令 \(M_k=kD_kL_k(m)\)。完整平方因子递降要求

\[
-M_k\in\mathcal D(M_k^2;q_k). \tag{3}
\]

下表给出 (3) 的目标及实际残数支撑：

| \(k\) | 目标 \(-M_k\bmod q_k\) | \(\mathcal D(M_k^2;q_k)\) |
|---:|---:|---|
| 1 | 2 | \(\{1\}\) |
| 2 | 5 | \(\{1,2,4\}\) |
| 3 | 8 | \(\{1,3,9\}\) |
| 4 | 11 | \(\{1,2,4,8\}\) |
| 5 | 14 | \(\{1,4,5,6,7,9,11,16,17\}\) |
| 6 | 17 | \(\{1,2,3,4,6,9,12,13,18\}\) |

每一行的目标都不在支撑中，故六条完整平方因子外部源递降全部失败。这里已枚举
\(M_k^2\) 的**全部**除子残数，所以不是只排除了某种固定因子子族。

## 可采纳性与条件性推论

将 H19 的 20 条线性型与表中的 6 条 \(L_k\) 合并，有限域根覆盖检查得到：

\[
\text{covering primes}=\varnothing. \tag{4}
\]

所以这 26 条正仿射线性型构成可采纳组。假定 Dickson 素数元组猜想或相应的
Schinzel 假设，存在无穷多个 \(m\) 使它们同时为素数。对充分大的这些 \(m\)：

1. H19 中每个 \(p+4s\) 都是其固定因子乘一个新素数，故前十九条规范 Type II 射线失败；
2. (3) 对 \(k=1,\ldots,6\) 同时失败，故六条完整平方因子外部源严格递降均不存在。

运行

```bash
python3 reproductions/type_ii_h19_external_source_conditional_escape.py
python3 -m unittest tests/test_type_ii_h19_external_source_conditional_escape.py -q
```

会重建全部因子、除子残数和 26 型可采纳性检查。

## 边界

该结论排除的只是固定组合

\[
\{\text{H19 规范 Type II 射线}\}
\cup
\{\text{完整外部源 }k=1,\ldots,6\}.
\]

它不排除更大的或随 \(p\) 变化的 \(k\)，新增规范移位、其它 Type I/II 证书，或其他
严格递降族；因此不是 Erdős--Straus 猜想的条件性反例。它的正向含义是：任何有效的
混合选择器必须至少允许尺度或 Type II 扇的自适应扩张，并利用超出有限可采纳性的信息。
