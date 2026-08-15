---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-finite-low-p-source-gate-closure
title: H4 q0 re-entry 的有限低 p source-gate 关闭
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap a=1 clean q bridge 的
  q0>1 p-free re-entry 中，不存在 p<=delta_d=2d(4d^2-2d+1) 的实例。写
  p=2dq-1、S_d=4d^2-2d+1，则 p<=2dS_d 强制 2<=q<=S_d；31 条 exact phase
  progression 又把 q 固定为 2dq=912u+770 (mod 108528)。遍历 213 个 selector/divisor
  对的 109 个 odd d，只留下 28 个有界 q progressions、2,204 个 q 值。对每个值，
  actual source identity 的必要门 D=delta_d (mod p)、D|ph-q+1，连同
  0<D<2dp，只留下总计 4,475,827 个明确 D 候选；没有一个整除
  ph-q+1=(2d-1)((2d+1)q-1)。因此低-p 分支为空。结合已关闭的 p>delta_d 分支，
  此 H4 q0>1 re-entry route 在整个 actual 19-phase domain 中为空。该内部 route
  closure 不证明整体 Erdős--Straus 猜想，也不自动处理其它 Type I/G 出口状态。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q0-reentry
  - source-provenance
  - carrier-d
  - finite-sieve
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure
    role: p-greater-than-delta-branch-closure
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
    role: actual-source-D-residue-and-divisibility-menu
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: d-divides-selector-delta-and-finite-phase-domain
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: exact-thirty-one-phase-progressions
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_low_p_finite_source_gate.py
    role: bounded-q-and-D-menu-receipt
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 的有限低 \(p\) source-gate 关闭

## 1. 从 \(p\)-界转成小 \(q\) 菜单

保留 actual re-entry 的 source normal form

\[
p=2dq-1,
\qquad
\delta_d=2dS_d,
\qquad
S_d=4d^2-2d+1.
\tag{1}
\]

large-\(p\) closure 后只需讨论 \(p\le\delta_d\)。由 (1)，

\[
2dq-1\le2dS_d
\quad\Longrightarrow\quad
\boxed{2\le q\le S_d.}
\tag{2}
\]

这里并不扫描所有 \(p\le28,925,021,170\)。actual H3 phase 对某个
\(u\in\mathcal U_{31}\) 强制

\[
p\equiv912u+769\pmod {108528},
\]

所以 \(q\) 必须满足一条线性同余

\[
\boxed{2dq\equiv912u+770\pmod {108528}.}
\tag{3}
\]

此外 \(d\) 是 \(\lvert1536-a(u)\rvert\) 的奇除子。对固定 \((u,d)\)，令
\(g=(2d,108528)\)。若 \(g\nmid912u+770\)，(3) 无解；否则它给出唯一的
\(q\pmod {108528/g}\) 类。再与 (2) 相交即可完全列出 low-\(p\) source menu。

## 2. D-residue 门的有限空表

对每个 (3) 的候选 \(q\)，令

\[
A=ph-q+1=(2d-1)((2d+1)q-1).
\tag{4}
\]

actual source identity 强制

\[
D\equiv\delta_d\pmod p,
\qquad D\mid A,
\qquad 0<D<2dp.
\tag{5}
\]

令 \(r_d\in\{1,\ldots,p\}\) 为 \(\delta_d\) 的正剩余。于是每个必要 \(D\) 恰为

\[
D=r_d+jp,
\qquad
0\le j\le2d-1,
\qquad D\le A.
\tag{6}
\]

这给出不含 factorization 或 primality test 的有限整数 menu。精确回执的计数是：

| 项目 | 数量 |
|---|---:|
| phase classes | 31 |
| selector/divisor pairs | 213 |
| odd \((u,d)\) pairs | 109 |
| 可解的 (3) pairs | 82 |
| 与 \(2\le q\le S_d\) 相交的 pairs | 28 |
| \(q\) candidates | 2,204 |
| (6) 的 \(D\) candidates | 4,475,827 |
| 满足 \(D\mid A\) 的 candidates | 0 |

最后一行在仍未要求 \(p\) 为素数、\(D\mid K_4\)、q-lock、payload 或 typed guards
时已经为空，故它安全地排除所有 actual re-entry 的子集。

## 3. 整个 q0 route 的关闭

large-\(p\) minimal-\(D\) closure 已排除 \(p>\delta_d\)，本卡排除
\(p\le\delta_d\)。所以：

\[
\boxed{
\text{在此 actual H4 q-bridge scope 中，不存在 }q_0>1\text{ re-entry。}
}
\tag{7}
\]

这不是把 q-lock、source row 或 static controls 误当作矛盾；它使用的是 actual
H4 carrier/source receipt 所给的 \(D\)-residue 与整除门。由于空表出现于这些必要条件，
无需构造或枚举潜在 H4 predecessor。

## 4. 边界

式 (7) 关闭的是一个明确的 H4 \(q_0>1\) p-free re-entry route。它不声称
q0=1、其它 H4 typed action、其它 Type I overflow 或退出到 G 的全局选择器已关闭，
更不等价于 Erdős--Straus 猜想的证明。其价值在于删除此前唯一仍可能从 clean q-bridge
返回 \(a=1\) q-lock/root route 的无界 source-provenance 分支。

## 5. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_low_p_finite_source_gate.py --verify
```

回执只枚举由 (2)--(3) 强制的 2,204 个 \(q\) 值和 (6) 的 4,475,827 个整数
候选；不扫描素数区间、分母、H4 payload 或 Reach history。
