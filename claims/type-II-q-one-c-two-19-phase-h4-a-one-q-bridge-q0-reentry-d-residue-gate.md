---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
title: H4 q0 re-entry 的归一化小除子残数门与 carrier d=1 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap a=1 clean q bridge 的 q0>1
  re-entry 中，令 w=(p+1)/2=qd、h=2d，D=(M4,Q_x) beta_x。既有 source-normalized
  endpoint identity、R4=1 (mod p) 与 D|(ph-q+1) 强制
  D=2d(4d^2-2d+1) (mod p)。因而令 d_{p,d} 为该残数的最小正代表，每个 actual D
  都必须同时满足 D=d_{p,d}+jp、0<=j<=2d-1 及
  D|(2d-1)((2d+1)q-1)。实际 phase 还给 d|abs(1536-a(p))<=1535，故这是每个
  phase input 至多 2d 个的 provenance-aware divisor gate。特别地，原 H4 carrier
  d=1 时 d_{p,1}=6，而 D=6 或 p+6 均不可能整除 (3p+1)/2；因此 carrier d=1
  不存在 q0>1 re-entry。这里的 carrier d 不等同于 re-entry target 重新分类后的
  ordinary full-product d=1 标签。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
topics:
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q0-reentry
  - source-provenance
  - divisor-gate
  - residue-class
  - carrier-d
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
    role: actual-h-equals-2d-source-normal-form-endpoint-identity-and-D-divisibility
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: q0-reentry-parameterization
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-H4-R4-and-K4-contract
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: finite-phase-selector-and-d-provenance
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_d_residue_gate.py
    role: residue-gate-and-carrier-d-one-exclusion-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 的 \(D\) 残数门

## 1. 实际 source identity 给出一个额外模门

保留 actual \(q_0>1\) re-entry 的记号：

\[
w=\frac{p+1}{2}=qd,
\qquad h=2d,
\qquad p=2dq-1,
\qquad q=\gamma q_0.
\tag{1}
\]

令

\[
D=(M_4,Q_x)\beta_x,
\qquad
\xi=(\gamma+pt)D.
\tag{2}
\]

这里 \(D\mid K_4\)、\((D,q_0)=1\)。实际 q-word/re-entry 不是一个静态
complete-excess 图表；它保留以下两条 source identity：

\[
(q-1)R_4=\gamma q_0^2\xi-h,
\qquad
D\mid ph-q+1.
\tag{3}
\]

又 H4 receipt 给 \(R_4\equiv1\pmod p\)。把 (2)--(3) 模 \(p\) 约化，得到

\[
q-1\equiv\gamma^2q_0^2D-2d=q^2D-2d\pmod p,
\tag{4}
\]

即

\[
q^2D\equiv q+2d-1\pmod p.
\tag{5}
\]

因为 \(2dq=p+1\)，有 \(q^{-1}\equiv2d\pmod p\)。因此 (5) 的精确归一化形式是

\[
\boxed{
D\equiv\delta_d:=2d(4d^2-2d+1)\pmod p.
}
\tag{6}
\]

这一步只使用 actual H4 provenance 已提供的 source identity；它不能从 q-lock 的
endpoint 同余或 ordinary full-product target 单独推出。

## 2. 有界的 provenance-aware divisor menu

令 \(d_{p,d}\in\{1,\ldots,p\}\) 是 \(\delta_d\) 模 \(p\) 的最小正代表。由 (3)
及 \(q>1\)，

\[
0<D\le ph-q+1<ph=2dp.
\tag{7}
\]

故 (6) 强制

\[
\boxed{
D=d_{p,d}+jp,
\qquad 0\le j\le2d-1.
}
\tag{8}
\]

另一方面，(1) 使 (3) 的被除数化为

\[
ph-q+1
=2dp-q+1
=\boxed{(2d-1)\bigl((2d+1)q-1\bigr)}.
\tag{9}
\]

因此每个 actual re-entry 都必须通过以下有限 gate：

\[
\boxed{
D\in\{d_{p,d},d_{p,d}+p,\ldots,d_{p,d}+(2d-1)p\},
\qquad
D\mid(2d-1)\bigl((2d+1)q-1\bigr).
}
\tag{10}
\]

实际 19-phase receipt 还给 \(d\mid\lvert1536-a(p)\rvert\le1535\)。故 (10) 不是
对 \(D\) 的无界因子搜索：一旦 selector 和 carrier \(d\) 被 source receipt 固定，
它最多留下 \(2d\le3070\) 个候选。这个结论本身不把每个候选宣称为可达，更不替代
typed、atomic 或 persistent guards。

## 3. carrier \(d=1\) 的完整排除

### 推论 1

在核心素数域，不存在 original H4 carrier \(d=1\) 的 \(q_0>1\) re-entry。

**证明。** 此时

\[
q=\frac{p+1}{2},
\qquad
\delta_1=6,
\qquad
ph-q+1=\frac{3p+1}{2}.
\tag{11}
\]

核心素数 \(p\ge73\)，而 \((3p+1)/2<2p\)，故 (8) 仅容许

\[
D=6\quad\text{或}\quad D=p+6.
\tag{12}
\]

写 \(p=24m+1\)。则 \((3p+1)/2=36m+2\) 不被 \(3\) 整除，故 \(6\nmid(3p+1)/2\)。
若 \(p+6\mid(3p+1)/2\)，则 \(p+6\mid3p+1\)，但

\[
3p+1\equiv-17\pmod{p+6},
\tag{13}
\]

这要求 \(p+6\mid17\)，与 \(p\ge73\) 矛盾。两种可能均空。\(\square\)

这里被排除的是 H4 carrier 参数 \(d=(w,M_4)\)，不是 q-lock re-entry target
在重新分类后出现的 ordinary full-product \(d=1\) 行；后者仍由已有 countdown/root-fan
路由处理。

## 4. 定向算术回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_d_residue_gate.py --verify
```

回执核对 (6)--(10) 的固定 local-H4 raw control \((p,d,q,D)=(769,5,77,141)\)，包括
\(pR_4+1=4K_4\)、\(h=(R_4-1,K_4)=2d\)、source identity 与 \(D\mid K_4\)。它还核对
\(p=73,d=1\) 的两个唯一候选均不能整除 (11) 的 divisor。这个 local control 不声称有
actual H3 predecessor，也不把 \(D\) 的 static 取值登记为 complete-excess payload。
