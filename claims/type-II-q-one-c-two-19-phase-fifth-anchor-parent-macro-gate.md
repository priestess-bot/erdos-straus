---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
title: q=1 高 C=2 19 相位 H4 到 H5 的 parent-macro 准入门
statement: >-
  设 q=1 high C=2 19 相位的既有 persistent macro 已从 P 经过 H4，且
  Lambda_p^sharp(P)=(0,p-1)。令 Q5 是 H4 anchor R4-1 相对于 K4 的唯一最大
  complete-excess block，M5=lcm(M4,Q5)=M4L5，c5 是 M5 的 canonical capacity。
  若 R4 既非 0 也非 1 (mod p)，并且 c5<=p-2，则 H4 的 p-source、anchor 与 p-free
  bundle 都可作为原 P macro 的一个额外内部 checkpoint；在 terminal-first 与 H4,H5 的
  typed reclassification 均通过时，P=>H5 的端点秩严格从 (0,p-1) 降到 (0,c5)，从而满足
  E1--E5。这个 parent-macro 条件只要求 c5<p-1，不要求 c5<c4；所以 H4 的局部 capacity
  上升不必然阻断第五 anchor。它不证明上述两个算术门对所有相位素数成立，也不把自由
  universal p-parent 误当成新 root-entry。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fifth-anchor
  - persistent-macro
  - high-support
  - complete-excess
  - source-provenance
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-and-endpoint-rank
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: H4-maximal-bundle-and-canonical-carrier
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-overlap-height-and-carry-boundaries
  - claim: type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
    role: finite-p-source-and-p-free-gate-reduction
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-high-support-carry-gate
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: raw-p-source-versus-root-policy-distinction
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py
    role: exact-H4-H5-source-and-carry-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 H4 \(\Rightarrow\) H5 parent-macro 准入门

## 1. 为什么局部 \(c_5<c_4\) 不是唯一的 E5 比较

已有的 q=1 high \(C=2\) persistent macro 从 charged parent \(P\) 出发，并以

\[
\Lambda_p^\sharp(P)=(0,p-1)
\tag{1}
\]

作为真正的递归端点秩。H0、H1、H2 已是同一宏内的 checkpoint：其中局部 capacity 可以上升，
只在终点与 \(P\) 比较 E5。H3 \(\Rightarrow\) H4 的 maximal-bundle 延长也保持这个
结构，且 \(1\le c_4\le p-2\)。

因此，H4 的下一个 canonical bundle 有两种不同用法：若把 H4 单独入队，目标必须满足
\(c_5<c_4\)；若把它附回同一个固定长度 parent macro，则正确的端点门是

\[
\boxed{c_5<p-1.}
\tag{2}
\]

后者严格更弱，且不需要重置 charged support。

## 2. 第五 anchor 的精确算术门

令

\[
Q_5=Q_{K_4}(R_4-1),\qquad
R_4-1=Q_5\beta_5,
\qquad
M_5=\operatorname{lcm}(M_4,Q_5)=M_4L_5,
\tag{3}
\]

其中 \(Q_{K_4}\) 取相对于 \(K_4\) 的唯一完整素数幂 excess。令 \(c_5\in\{1,\ldots,p-1\}\)
满足

\[
c_5\equiv c_4L_5^{-1}\pmod p,
\qquad
K_5=M_5c_5,
\qquad
pR_5+1=4K_5.
\tag{4}
\]

假设

\[
\boxed{R_4\not\equiv0,1\pmod p,\qquad c_5\le p-2.}
\tag{5}
\]

第一个条件的两个角色不能合并。\(R_4\not\equiv0\pmod p\) 使

\[
(U,V,m)=\bigl(p,\ R_4(p-1)-p,\ p-1\bigr)
\tag{6}
\]

成为实际 primitive p-source：\(V>0\)、\((U,V)=(p,R_4)=1\)，其唯一 p-edge 以
shift \(1\) 到达 \((1,R_4-1,1)\)。\(R_4\not\equiv1\pmod p\) 则保证
\(p\nmid(R_4-1)\)，故 \(p\nmid Q_5\)。

而 H4 overlap 恒等式给出

\[
(R_4-1,K_4)=2\left(\frac{p+1}{2},c_3-s_4\right)\le p+1.
\tag{7}
\]

但 \(R_4-1>p+1\)（由 \(R_4>p^3/2-1/p\) 及 \(p\ge73\)），所以 \(R_4-1\nmid K_4\)，从而 \(Q_5>1\)。因此 (3)
是一个非平凡、p-free 的 canonical complete-excess bundle。

## 3. 条件性宏准入

在 terminal-first 已检查 H4，且 H4、H5 的独立 typed reclassification 都被 verifier
接受时，把 (6) 的 raw source、anchor 与 (3) 作为原 \(P\Rightarrow H_4\) macro 的
最后一个内部 word。它没有创建新的 root-entry：source 绑定于已存在的 persistent parent
及其 scope，H4 只是同一固定长度宏内的 checkpoint。

| 合同 | 回执 |
|---|---|
| E1 | (5)--(6) 的实际 p-source 与 anchor；其前缀是已有 \(P\Rightarrow H_4\) receipt。 |
| E2 | (3)--(4) 的完整 excess、lcm carrier 与 canonical target。 |
| E3 | 既有 parent digest，加上 H4 source/anchor/bundle payload 与 H5 的独立 typed reclassification。 |
| E4 | 全程 equation target 为 \(4/p\)，以 \(\operatorname{Sol}(p)\) 恒等 lift。 |
| E5 | 由 (1)、(2) 得 \(\Lambda_p^\sharp(P)=(0,p-1)>(0,c_5)=\Lambda_p^\sharp(H_5)\)。 |

故 (5) 是把 H4\(\Rightarrow\)H5 接回已有 strict macro 的充分准入门。重点在于 E5
比较真实 persistent parent 和最终端点，而非 H4 的内部 capacity。

## 4. 两个相反局部方向的正控制

下列控制都满足 \(R_4\not\equiv0,1\pmod p\)、\(p\nmid Q_5\)、\(c_5\le p-2\)，并且
均避开 \(p+1\) 的 \(3\pmod4\) 因子 terminal：

| \(p\) | \(R_4\bmod p\) | \(c_4\) | \(c_5\) | H4 局部方向 | parent macro E5 |
|---:|---:|---:|---:|---|---|
| \(14449\) | \(4039\) | \(13391\) | \(12552\) | 下降 | 严格 |
| \(665617\) | \(333704\) | \(20388\) | \(94177\) | 上升 | 严格 |

第二行表明 \(c_5>c_4\) 不能被当作第五 anchor 的自动失败：它只排除将 H4 单独作为
高支撑递归端点的那种解释，并不排除固定 parent macro。

## 5. 范围

本卡没有证明 \(c_5\le p-2\) 对所有 19-phase 素数成立，也没有替代 H4/H5 的 terminal-first
或 typed reclassification。H4 的 \(R_4\equiv0,1\pmod p\) 两个 source/p-free 障碍已被
[有限 p-adic 例外界](type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound.md)压缩到一个
显式有限残余。\(c_5=p-1\) 也不再是未分类的 top-capacity 条件：它被
[H5 顶容量 d=1 handoff](type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff.md)
精确归入 d=1 suffix，而原来的 \(a=1,\omega=-1\) p-free return 已由
[H5 a=1 全重叠有限筛完成](type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion.md)
排除实际 H3--H4 predecessor。因此在所有实际 checkpoint guards 通过时，top-capacity
也有 guarded strict capacity endpoint。该完成仍不能替代全局 selector 或未验证的 typed guards；
H4 前置门或其它 G/Type I 残余才需要 rank-aware sink-bundle candidate map、Type II short
certificate 或带独立全局势的 paid reset。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py --verify
```
