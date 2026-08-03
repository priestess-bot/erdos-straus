---
kind: claim
claim_id: type-I-overflow-defect-unit-phase-capacity
title: overflow 缺陷单位的条件性相位胞与容量边界
statement: 对双对偶支撑阻碍中 q^a||A 的未支付高度 h>0，若通道余数标签 ell 的 q 进赋值为 b，则规范缺陷单位 eta=(ell/q^b) mod q^h 是 q 进单位。只有额外假设不同状态的 eta 满足 eta_i=eta_j (mod q^min(h_i,h_j)) 时，它们才形成可用于相位树容量的等价胞；冻结的 17 条阻碍幂记录形成 5 个 q 组、13 个胞，条件性容量无超载。这否定把原始阻碍因子自动视为共享相位资源，但不否定带有真实状态转移的相位匹配定理。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-phase-clearing-cell-capacity-contract
topics:
- type-I
- overflow
- q-adic
- phase
- capacity
- defect-unit
- cross-state
- proof-boundary
- proof-program
sources:
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: local-obstruction-height-and-residue-label
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: nested-phase-tree-capacity
  - claim: type-I-representation-dual-capacity-selector-contract
    role: typed-support-debt-phase-bridge
visibility: public
last_checked: '2026-08-03'
---

# overflow 缺陷单位的条件性相位胞与容量边界

## 1. 缺陷单位的规范化

设一个双对偶通道的旧支撑素数幂满足

\[
q^a\parallel A,
\qquad
u=v_q(t),
\qquad
b=v_q(\ell),
\]

其中 \(t=d\) 或 \(r\)，而 \(\ell=k+1\) 或 \(dn-1\) 是相应 determinant 余数标签。
若局部未支付高度

\[
h=(a-u-b)_+>0,
\]

定义规范缺陷单位

\[
\eta=\frac{\ell}{q^b}\pmod {q^h},
\qquad
1\le\eta<q^h.
\tag{1}
\]

由于 \(b<a-u\)，\(\eta\) 与 \(q\) 互素。它保存了在去除载体支付和标签已有 q 进层后，
剩余 determinant 标签的首个单位残基；它不是一个已经存在的 marked lift。

## 2. 何时能进入相位树容量

对同一个 q 的两个 obstruction rows \(i,j\)，定义缺陷单位兼容为

\[
\eta_i\equiv\eta_j
\pmod {q^{\min(h_i,h_j)}}.
\tag{2}
\]

若一个 alternate/source-switch 构造确实要求其 q 进清分标签 \(s_i\) 满足

\[
s_i\equiv\eta_i\pmod {q^{h_i}},
\tag{3}
\]

那么 (2) 立即给出已有相位树合同的嵌套同余前提。取 (1) 的最小正代表作为诊断标签，
若一个兼容胞的标签区间宽度为 \(M_c\)、标签最大重复度为 \(\mu_c\)，则

\[
\sum_{i\in c}h_i
\le
\mu_c\sum_{k=1}^{H_c}
\left(\left\lfloor\frac{M_c}{q^k}\right\rfloor+1\right),
\qquad H_c=\max_{i\in c}h_i.
\tag{4}
\]

更一般地，若同胞在高层继续分裂，右侧应乘以每层的相位残基数 \(D_{c,k}\)。这只是
已有 phase-tree capacity 的直接代入；关键的新条件是 (3)，它必须由实际 alternate
算术证明，不能从局部 obstruction 定义自动推出。

## 3. 冻结回执的负边界

验证器
    python3 reproductions/type_i_overflow_defect_unit_phase_capacity.py --verify
读取逐素数幂支付账本中的非零阻碍行：

| 字段 | 数值 |
|---|---:|
| 阻碍幂行 | 17 |
| q 分组 | 5 |
| 条件性相位胞 | 13 |
| 非单例胞 | 3 |
| 两两兼容对 | 5 |
| 两两检查 | 31 |
| 容量超载胞 | 0 |

因此当前回执不能支持“同一 q 的所有 overflow 阻碍自动共享相位”这一强化命题。例
如 \(q=19\) 的阻碍单位分成多个胞；重复单位只形成小胞，没有达到容量超载。

这个负边界不是对统一选择器的反例。它只说明跨状态证明必须另外提供至少一项：

1. alternate/source-switch 的真实 congruence 把不同 obstruction rows 映入同一缺陷
   相位胞；
2. 一个不同于 \(\eta\) 的算术标签，但能证明其与 \(\eta\) 有有界、可重复控制的映射；
3. 不走相位容量，而把缺陷单位直接转成 Type I/II 终端或严格下降的 marked edge。

## 4. 逻辑边界

本卡的“相位胞”和容量上界是条件性的。局部双对偶账本只给出 \(h\) 和 \(\eta\)，不
给出 (3)、标签正性、非空标记集、全域解提升或 E1--E5 势下降。因此它的正确类型是
analysis_evidence / candidate_transition，不能承担统一递归。

## 复现

    python3 reproductions/type_i_overflow_defect_unit_phase_capacity.py --verify

结果文件为
reproductions/type-i-overflow-defect-unit-phase-capacity-results.json。
