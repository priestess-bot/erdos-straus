---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-large-p-minimal-d-closure
title: H4 q0 re-entry 的 large-p minimal-D complete-excess 关闭
statement: >-
  在 actual q=1 high C=2 19-phase H4 q0>1 p-free re-entry 中，不存在满足
  p>delta_d=2d(4d^2-2d+1) 的实例。既有 D-residue 筛已排除 D>delta_d；其余
  D=delta_d 的 17 条 necessary phase rays 由 H3 terminal-first 删除 7 条、17-adic
  exact-carrier 删除 3 条。对最后七条，每条可选 ell|d 且 ell 与 H3 分母互素，使
  nu_ell((p+1)/2)=nu_ell(c3)=nu_ell(q3)=1 且 ell 不整除 M3，沿整条 ray 恒定。
  因而 ell 在 R3-1 和 K3 的赋值相等，不属于 maximal complete-excess Q*，却以一次幂
  进入 lambda；于是 ell 不整除 M4=M3*q3/lambda，与 ell|d|gcd((p+1)/2,M4) 矛盾。
  因此每个 actual q0 re-entry 必须满足 p<=delta_d。这是对 large-p source-provenance
  分支的全称排除，不处理这个有限低-p 区域，也不构成全局 Type I/II 出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-17-adic-carrier-pruning
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
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
  - complete-excess
  - valuation
  - finite-sieve
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
    role: large-p-D-split-and-seventeen-minimal-D-rays
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning
    role: seven-terminal-ray-deletions
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-17-adic-carrier-pruning
    role: three-denominator-overlap-carrier-deletions
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: maximal-complete-excess-lambda-and-H4-carrier-identity
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_complete_excess_valuation_pruning.py
    role: seven-whole-ray-valuation-receipts
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 的 large-\(p\) minimal-\(D\) complete-excess 关闭

## 1. 最后七条射线的局部赋值引理

写 H3 maximal completion 的记号为

\[
w=\frac{p+1}{2},\qquad
q_3=\frac{R_3-1}{2},\qquad
K_3=M_3c_3,
\tag{1}
\]

并令 \(Q^*=Q_{K_3}(R_3-1)\)、\(\beta=(R_3-1)/Q^*\)、
\(o=(M_3,Q^*)\)。此前的 exact completion 给出

\[
\lambda=\frac{\beta o}{2},
\qquad
M_4=M_3\frac{q_3}{\lambda}.
\tag{2}
\]

### 引理 1（一次共享赋值不会进入第四 carrier）

设奇素数 \(\ell\) 满足

\[
\nu_\ell(w)=\nu_\ell(c_3)=\nu_\ell(q_3)=1,
\qquad \ell\nmid M_3.
\tag{3}
\]

则 \(\ell\nmid M_4\)。

**证明。** 由 (3)，

\[
\nu_\ell(K_3)=1,
\qquad
\nu_\ell(R_3-1)=\nu_\ell(2q_3)=1.
\]

所以 \(\ell\) 不是相对 \(K_3\) 的 complete-excess 素数：它不出现在 \(Q^*\) 中，
却以一次幂出现在 \(\beta\) 中。因而 \(\ell\nmid o\)、
\(\nu_\ell(\lambda)=1\)。式 (2) 于是给

\[
\nu_\ell(M_4)=0+1-1=0.
\]

证毕。\(\square\)

这个引理说明：一个同时出现在 \(w,c_3,q_3\) 中、但没有超过 \(K_3\) 的因子，
恰恰会被 maximal completion 的 \(\lambda\) 移出新 carrier。它不能仅由
\(d\mid\lvert1536-a\rvert\) 看出。

## 2. 七条 whole-ray 赋值回执

H3 terminal-first 与 17-adic exact-carrier 剪枝后，余下的 seven-ray supermenu 是

\[
(u,d)=(15,65),(15,221),(19,953),(26,53),(27,1409),(57,353),(104,29).
\tag{4}
\]

对每条选择下表的 \(\ell\mid d\)。其 step \(P\) 被 \(\ell^2\) 整除，同时也保持
selector \(a\)。所选 \(\ell\) 与 \(2\cdot3\cdot19\cdot2261\) 互素，因此 H3 的
递推式可直接在 \(\ell^2\) 下进行；所有分母均为单位。表中后三列是单位商的模
\(\ell\) 余数。

| \(u\) | \(a\) | \(d\) | \(\ell\) | \(p\bmod\ell^2\) | \(w/\ell\) | \(c_3/\ell\) | \(q_3/\ell\) | \(M_3\bmod\ell\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 431 | 65 | 5 | 4 | 3 | 2 | 2 | 4 |
| 15 | 431 | 221 | 13 | 103 | 4 | 3 | 9 | 10 |
| 19 | 583 | 953 | 953 | 1,905 | 1 | 261 | 538 | 826 |
| 26 | 317 | 53 | 53 | 105 | 1 | 43 | 10 | 19 |
| 27 | 127 | 1409 | 1409 | 2,817 | 1 | 551 | 102 | 1,290 |
| 57 | 830 | 353 | 353 | 705 | 1 | 335 | 215 | 104 |
| 104 | 260 | 29 | 29 | 57 | 1 | 16 | 17 | 14 |

每一格均非零。因此不只是 ray 首项，而是每个
\(p=p_0+jP\) 都满足 (3)。例如，\(P\equiv0\pmod {\ell^2}\) 保持
\(p\pmod {\ell^2}\)，而 \(P\equiv0\pmod {2261}\) 保持 selector；H3 的模
\(\ell^2\) 递推遂保持 \(M_3,c_3,q_3\) 的所有表中余数。

对每行由引理 1 得 \(\ell\nmid M_4\)。但 source-side minimal-\(D\) ray 同时有
\(\ell\mid d\) 和 \(\ell\mid w\)，所以不可能满足 actual carrier equality

\[
d=(w,M_4).
\tag{5}
\]

故 (4) 的七条 whole rays 全部为空。

## 3. large-\(p\) 分支关闭

在 \(p>\delta_d=2d(4d^2-2d+1)\) 时，既有 \(D\)-residue 分类只有两类：

| 分支 | 结果 |
|---|---|
| \(D>\delta_d\) | 有界 \((d,k,\ell)\) phase screen 全空。 |
| \(D=\delta_d\) | 17 条 necessary rays：H3 terminal-first 删除 7 条，17-adic carrier 删除 3 条，本卡的引理 1 删除 7 条。 |

第二行已经穷尽 \(7+3+7=17\) 条 CRT rays。因此：

\[
\boxed{
\text{actual }q_0>1\text{ H4 re-entry}
\quad\Longrightarrow\quad
p\le\delta_d.
}
\tag{6}
\]

又 \(d\mid\lvert1536-a\rvert\le1535\)，且 \(\delta_d\) 随正 \(d\) 严格递增，故有
统一的有限界

\[
\boxed{p\le\delta_{1535}=28,925,021,170.}
\tag{7}
\]

## 4. 边界

式 (6)--(7) 是 large-\(p\) source-provenance 分支的完整关闭。后继的
[有限低-\(p\) source-gate 关闭](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-finite-low-p-source-gate-closure.md)
已在不扫描 prime interval 的前提下排除 \(p\le\delta_d\)，从而关闭整个这条
\(q_0>1\) re-entry route。本卡仍不把这一局部 H4 re-entry 排除误称为整个
Erdős--Straus 猜想的证明。

## 5. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_complete_excess_valuation_pruning.py --verify
```

回执固定 seven-ray menu，并逐行在 \(\ell^2\) 上重放 H3 递推，核对其与 exact H3
整数 receipt 一致；它不扫描 prime ranges、分母、H4 payload 或 Reach history。
