---
kind: claim
claim_id: type-I-overflow-fixed-n-gap-dual-obstruction
title: overflow 固定-n 因子间隙与双对偶支撑阻碍的 typed 负边界
statement: 对满足 pn=4Md+1、A|M 的 overflow fixture，固定-n 支撑增长候选恰由 t|Md/A、t>1 且 n<4At<p+n 给出；双对偶旧支撑保持恰由两个局部通道的 chart_R<p、严格载体增长和 q-进阻碍为 1 同时满足给出。若固定-n 候选为空且两通道均不满足，则可登记 hard_core_fixed_n_gap_and_dual_obstruction；该标签只否定当前有限菜单，不否定其它载体、直接证书或合法递归后继。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-qadic-obstruction-transfer
topics:
- type-I
- overflow
- fixed-n
- q-adic
- obstruction
- typed-receipt
- negative-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact fixture classification and replayable receipts
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: frozen hard-core menu output
visibility: public
last_checked: '2026-08-03'
---

# overflow 固定-\(n\) 因子间隙与双对偶支撑阻碍的 typed 负边界

## 1. 精确菜单

设 overflow 满足

\[
pn=4Md+1,
\qquad A\mid M,
\qquad S=Md.
\]

固定-\(n\) 候选写成 \(L=At\)。行列式图谱的合法窗口等价于

\[
t\mid \frac{S}{A},
\qquad t>1,
\qquad n<4At<p+n.
\tag{1}
\]

因此只要枚举 \(S/A\) 的精确因子，就能得到一个可重放的有限因子间隙回执。回执保存
素因子分解、全部 \(t\) 及开区间两侧的最近因子；`eligible_t=[]` 且
`empty_verified=true` 只表示 (1) 没有解。

## 2. 双对偶判据

写 \(M=kp+r\)，\(0<r<p\)。对 \(d\)-通道和 \(r\)-通道分别记录载体、规范图表
余数、严格载体增长以及逐 \(q^a\parallel A\) 的支付高度。根据双对偶支撑判据，通道
只有在

\[
R_t<p,
\qquad \frac{t}{\gcd(A,t)}>1,
\qquad O_t=1
\tag{2}
\]

时才是保持旧 \(A\) 的候选；其中 \(O_t\) 是所有未支付 \(q\)-幂的乘积。若某个素数幂
仍留在 \(O_t\)，或者规范图表本身是 overflow，则该通道只能作为 support-reset 候选，
不能登记为旧支撑递归边。

## 3. hard-core 标签

对每个 fixture 定义：

```text
fixed_n_window_nonempty
    若 (1) 有解；
dual_support_preserving
    若 (1) 无解但 (2) 至少一个通道成立；
hard_core_fixed_n_gap_and_dual_obstruction
    若 (1) 无解且两个通道均不成立。
```

第三类只是一条负边界。它同时证明了当前固定-\(n\) 分支没有出口、当前两个对偶载体
没有旧支撑保持边；它没有证明：

- 其它 source/path/node 载体不存在；
- 直接 Type I/II 证书不存在；
- 丢弃 \(A\) 的 phase reset 不可良基；
- 任意标记纤维为空；
- Erdős--Straus 猜想存在反例。

## 4. 当前回执

聚焦输入含 12 个 overflow fixture：

| 分类 | 数量 |
|---|---:|
| `fixed_n_window_nonempty` | 3 |
| `dual_support_preserving`（固定-\(n\) 为空后才计入） | 0 |
| `hard_core_fixed_n_gap_and_dual_obstruction` | 9 |

q-adic 双通道总计有 3 个 `support_preserving_edge`；它们全部落在上述 3 个
固定-\(n\) 非空 fixture 中，因此按选择器的优先级没有另计为
`dual_support_preserving`。9 个 hard-core 行分别保存 \(S/A\) 的因子分解、开窗口两侧的最近因子、两个对偶通道
的 chart 与完整 \(q\)-幂 deficit。它们全部是
`selector_status=analysis_evidence`、`recursive_edge_eligible=false`。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果保存在
`reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`overflow_menu.hard_core_receipts`。

## 5. 研究含义

这条回执把当前最窄余项从“两个菜单都失败”提升为可检索、可重算的算术对象，但没有
关闭全称选择器。下一步必须把 hard-core 行送入新的 alternate carrier、直接证书或
带独立良基势的 support reset；不能把负边界本身当作递归下降证明。
