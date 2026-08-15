---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-17-adic-carrier-pruning
title: H4 q0 re-entry 最小 D 射线的 17-adic exact-carrier 剪枝
statement: >-
  在 q=1 high C=2 19-phase H4 q0>1 re-entry 的 large-p minimal-D supermenu 中，
  H3 terminal-first 后保留的三条 d=17 射线分别为 (u,a)=(15,431)、(83,1723)、
  (117,2046)。每条上 p=-1 (mod 17)，H3 selector-free pre-capacity 恒有 M3=6
  (mod 17)，且 c3=(1536+ap)/2261 分别恒为 14、11、6 (mod 17)。由
  p q3+(p+1)/2=2M3c3 和 q3=(R3-1)/2，得到 q3=2、4、13 (mod 17)，均非零。
  最大 H3-to-H4 completion 满足 M4=M3(q3/lambda)，故 17 不整除 M4；但这三条
  射线均要求 d=gcd((p+1)/2,M4)=17，矛盾。因此三条 whole rays 都不可能承载 actual
  q0 re-entry，先前的 10 条 residual rays 缩为 7 条。此结论不排除 d=221 的含 17
  射线，也不替代 remaining payload、typed、atomic 或 persistent guards。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
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
  - p-adic
  - finite-sieve
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning
    role: terminal-pruned-ten-ray-supermenu
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: exact-maximal-H3-to-H4-completion-and-lambda-identity
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H3-precapacity-and-H4-carrier-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_17_adic_carrier_pruning.py
    role: whole-ray-modulo-17-receipt
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 最小 \(D\) 射线的 17-adic exact-carrier 剪枝

## 1. 不能把 \(d\mid\lvert1536-a\rvert\) 当作 carrier equality

此前的 H3 terminal-first 剪枝把 minimal-\(D\) 的 17 条必要 phase rays 压到
10 条。其中有三条仍标为 \(d=17\)：

| \(u\) | \(a\) | \(d\) | \(p_0\) | \(P\) |
|---:|---:|---:|---:|---:|
| 15 | 431 | 17 | 2,037,302,065 | 2,071,908,048 |
| 83 | 1723 | 17 | 557,367,745 | 2,071,908,048 |
| 117 | 2046 | 17 | 853,354,609 | 2,071,908,048 |

每条表示 \(p=p_0+jP\)（\(j\ge0\)）。它们来自 source-side 的必要
\(D\)-residue 条件；actual H4 re-entry 还必须满足 exact carrier equality

\[
d=\left(\frac{p+1}{2},M_4\right).
\tag{1}
\]

这里 \(17\mid2261\)，所以先前用于 \((d,2261)=1\) 情形的
\(d\mid c_3\) 不能适用。相反，必须保留 \(c_3\) 的一阶 17-adic 信息。

## 2. H3 的 selector-free 17-adic carrier

令

\[
q_3=\frac{R_3-1}{2},\qquad w=\frac{p+1}{2}.
\tag{2}
\]

每条表中射线有 \(p\equiv-1\pmod{17}\)。H3 的前三个 anchor 只用到分母
\(8,3,19\)，它们均是模 \(17\) 的单位。把其递推在 \(p=-1\pmod{17}\) 下逐项
约化，得到

\[
\begin{array}{c|ccccccccc}
 &M_0&Q_0&c_1&M_1&Q_1&c_2&M_2&Q_2&M_3\\ \hline
\pmod {17}&1&13&12&13&11&10&7&13&6.
\end{array}
\tag{3}
\]

因此对三条完整 progression 都有

\[
\boxed{M_3\equiv6\pmod {17}.}
\tag{4}
\]

另一方面 \(P\) 被 \(17\cdot2261\) 整除。由

\[
c_3(p+P)-c_3(p)=\frac{aP}{2261}
\tag{5}
\]

可知 \(c_3\pmod {17}\) 沿每条 ray 恒定。对其首项作一次精确约化即可得到：

\[
\begin{array}{c|c|c|c}
u&a&c_3\pmod {17}&q_3\pmod {17}\\ \hline
15&431&14&2\\
83&1723&11&4\\
117&2046&6&13
\end{array}
\tag{6}
\]

最后一列不是经验计算。H3 恒等式 \(pR_3+1=4M_3c_3\) 等价于

\[
p q_3+w=2M_3c_3.
\tag{7}
\]

在 \(p=-1\)、\(w=0\)、\(M_3=6\pmod {17}\) 下，式 (7) 给

\[
q_3\equiv-12c_3\equiv5c_3\pmod {17},
\tag{8}
\]

正好给出 (6) 的 \(2,4,13\)。所以每条射线均有

\[
\boxed{17\nmid q_3.}
\tag{9}
\]

## 3. exact H4 carrier 矛盾

最大 complete-excess completion 的精确恒等式为

\[
M_4=M_3\frac{q_3}{\lambda},
\qquad \lambda\mid q_3.
\tag{10}
\]

由 (4) 和 (9)，右侧两个因子都不被 \(17\) 整除，故

\[
17\nmid M_4.
\tag{11}
\]

但表中的 source ray 已有 \(17\mid w\)，且其候选 carrier 正是 \(d=17\)。式
(1) 因而不可能成立。故三条射线对每个 \(j\ge0\) 都被排除。

结合已有的七条 H3 terminal-first 删除，minimal-\(D\) 的尚未关闭 source
supermenu 现为七条：

\[
(15,65),\ (15,221),\ (19,953),\ (26,53),\ (27,1409),\ (57,353),\ (104,29).
\tag{12}
\]

## 4. 边界

本论证专门利用了 \(d=17\) 和 \(17\mid2261\)。它不能推广为“每个含 \(17\)
的射线都空”：例如 \((u,d)=(15,221)\) 仍须单独满足 full carrier equality 以及
actual q0 payload 条件。式 (12) 仍然只是 source-provenance 的必要菜单，不是 H4
receipt，也不构成全局 Type I/II 出口。

## 5. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_17_adic_carrier_pruning.py --verify
```

回执只重建 17 条既有 CRT rays 中的三条 \(d=17\) progression，验证 H3 的模
\(17\) 递推、\(c_3\) 的整条射线不变性和式 (7) 的精确余数；不扫描 primes、H4
payload、分母或 Reach history。
