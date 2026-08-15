---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-minimal-d-ray-h3-terminal-pruning
title: H4 q0 re-entry 最小 D 射线的 H3 terminal-first 剪枝
statement: >-
  在 H4 q0>1 p-free re-entry 的 large-p minimal D 分支中，17 条 prior necessary
  phase rays 都满足 p=2dq-1、d|abs(1536-a) 与 a=selector_a(p)。若 gcd(d,2261)=1
  且 d 含有一个 3 mod4 素因子 ell，则 d|gcd((p+1)/2,c3)，其中
  c3=(1536+ap)/2261；因此 ell 已在 H3 terminal-first 给出 Type II 证书，H4 q0
  re-entry 不会发生。现有 17 条射线中恰有 7 条被此引理全射线删除，余下 10 条的
  d 的全部素因子均为 1 mod4。三个首项为素数的 ray point 也均非 actual q0 re-entry：
  u=78,d=11 与 u=85,d=179 已在 H3 terminal 截断，而 u=15,d=65 的 exact maximal
  H3=>H4 completion 满足 gcd((p+1)/2,M4)=1 而非 65。该结论不声称余下 10 条射线
  可达或已排除，也不绕过 q0 re-entry 的 maximality、payload、typed 或 persistent guards。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
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
  - terminal-first
  - type-II-certificate
  - finite-sieve
  - phase-ray
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
    role: minimal-D-seventeen-ray-map-and-exact-phase-progression
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: H3-gcd-w-c3-terminal-first-dispatch
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: exact-H3-to-H4-maximal-carrier-construction
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_h3_terminal_pruning.py
    role: symbolic-ray-pruning-and-three-prime-first-point-audit
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 最小 \(D\) 射线的 H3 terminal-first 剪枝

## 1. 射线参数已强制进入 H3 overlap

保留 large-\(p\) minimal 分支的记号。此前的 \(D\)-gate 给出

\[
D=2d(4d^2-2d+1),
\]

并将所有尚未排除的 necessary phase candidate 写成 17 条 progression

\[
p=p_0+jP,\qquad j\ge0,
\tag{1}
\]

其中 \(P\) 是 phase period \(912\cdot119\) 与 minimal-\(D\) 模数的公倍数。每条
射线固定 H3 selector \(a\)，并满足

\[
p\equiv-1\pmod {2d},
\qquad
d\mid\lvert1536-a\rvert.
\tag{2}
\]

H3 的 canonical capacity 为

\[
c_3=\frac{1536+ap}{2261},
\qquad
g=\left(\frac{p+1}{2},c_3\right).
\tag{3}
\]

若 \((d,2261)=1\)，则 (2) 在模 \(d\) 下给出

\[
1536+ap\equiv1536-a\equiv0pmod d.
\tag{4}
\]

故

\[
\boxed{d\mid c_3,\qquad d\mid\frac{p+1}{2},\qquad d\mid g.}
\tag{5}
\]

这里不是只检查 ray 的首项：\(P\) 同时保留 (2) 和 selector \(a\)，所以 (4)--(5)
对 (1) 的每个整数参数 \(j\) 成立。

## 2. 七条射线在 H3 已有短证书

若 \(d\) 有 \(\ell\equiv3\pmod4\) 的素因子，则 (5) 给 \(\ell\mid g\)。H3
terminal-first dispatch 对这个因子直接给出 Type II raw-ray certificate；因此任何素数
点在进入 H4 前已被截断。现有射线中满足 \((d,2261)=1\) 的此类记录恰为：

| \(u\) | \(a\) | \(d\) | 选取的 \(\ell\equiv3\pmod4\) |
|---:|---:|---:|---:|
| 8 | 2027 | 491 | 491 |
| 34 | 925 | 611 | 47 |
| 43 | 963 | 191 | 191 |
| 78 | 1096 | 11 | 11 |
| 83 | 1723 | 11 | 11 |
| 85 | 1894 | 179 | 179 |
| 104 | 260 | 11 | 11 |

所以原 17 条 pre-H3 supermenu 被压缩为下列 10 条仍未由此论证删除的射线：

| \(u\) | \(a\) | \(d\) |
|---:|---:|---:|
| 15 | 431 | 17 |
| 15 | 431 | 65 |
| 15 | 431 | 221 |
| 19 | 583 | 953 |
| 26 | 317 | 53 |
| 27 | 127 | 1409 |
| 57 | 830 | 353 |
| 83 | 1723 | 17 |
| 104 | 260 | 29 |
| 117 | 2046 | 17 |

这些 \(d\) 的素因子均为 \(1\pmod4\)。特别地，不能把“没有 H3 \(3\pmod4\)
因子”误读为 H4 re-entry 已实现；它只说明这里的 terminal-first 路由不再截断。

## 3. 三个首项素数的 exact-prefix 复核

17 条 progression 的首项中有三个素数。直接用 exact H3 maximal-complete-excess
construction 复核，得到：

| \(p\) | ray \((u,d)\) | exact prefix 结果 |
|---:|---|---|
| 2,025,421,441 | \((78,11)\) | H3 的 \(g\) 含 11，terminal-first 直接给 Type II certificate。 |
| 430,576,893,658,129 | \((85,179)\) | H3 的 \(g\) 含 179，terminal-first 直接给 Type II certificate。 |
| 7,606,503,424,129 | \((15,65)\) | H3 是 nonterminal \(q=1\) mask，但 exact maximal H4 carrier 有 \(\lambda=65\) 且 \(\bigl((p+1)/2,M_4\bigr)=1\ne65\)。 |

第三行说明仅满足旧的弱条件 \(d\mid\lvert1536-a\rvert\) 远不等于 actual H4
carrier equality \(d=((p+1)/2,M_4)\)。因此此前为 source-row CRT 边界构造的三条
ray-prime 静态控制仍然有效地反驳“纯 \(t\)-同余矛盾”，但它们绝不是 actual H4 receipt
的近似实例。

## 4. 下一接口与范围

本卡给出的新残余是 10 条经过 H3 terminal-first 的 minimal-\(D\) phase rays。下一步
应使用 exact H3 \(\Rightarrow\) H4 carrier equality

\[
d=\left(\frac{p+1}{2},M_4\right),
\tag{6}
\]

而不只是 \(d\mid\lvert1536-a\rvert\)，并再叠加 \(q_0\) source row 的 retained
complete-excess / \(E_\zeta\) 条件。本文没有声称 (6) 已在 10 条无穷 progression 上
完成筛除，也没有宣称 q-lock、root-capacity、typed 或 persistent guards 已闭合。

## 5. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_minimal_d_ray_h3_terminal_pruning.py --verify
```

回执只重建 17 条已有 progression 的模论剪枝，并对其中固定的三个首项素数执行 exact
H3/H4 prefix 复核；不扫描 prime ranges、分母、Reach history 或潜在 H4 predecessor。
