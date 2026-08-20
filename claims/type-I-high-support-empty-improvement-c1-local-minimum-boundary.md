---
kind: claim
claim_id: type-I-high-support-empty-improvement-c1-local-minimum-boundary
title: 高支撑 C=1 的固定协议局部最小元与付费退出边界
statement: >-
  对 fixed-p TYPEI/CHARGED 高支撑状态 H=(p,R,K;A) 满足 A>B_p、K=A、eta_p=0，
  T5 local tuple 为 (0,1,0,0)，是同 rho、同 TYPEI/CHARGED protocol 层的最小元。
  因此 complete-excess 的 CHARGED endpoint 只能 stutter 或上升，任何同层 finite macro
  也不能支付 parent-to-final E5；total-cofactor 在 C=1 时为 identity，natural determinant
  duals 丢失旧 charged support。本卡只建立 C=1 同协议 no-go；它不把 C>1 的
  terminal-first-miss 空改善分支归约为 C=1，也不关闭 high-support family、F2、T6 或
  Erdős--Straus 猜想。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-high-support-rank-aware-sink-bundle-selector
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-high-anchor-direct-c1-finite-menu-exhaustion
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - high-support
  - empty-improvement
  - cofactor-one
  - local-minimum
  - phase-reset
  - no-go
  - proof-boundary
sources:
  - claim: type-I-high-support-rank-aware-sink-bundle-selector
    role: nonempty-improvement-edge-and-empty-family-boundary
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: exact-canonical-carry-formula-and-p73-control
  - claim: type-I-overflow-total-cofactor-canonical-projection-persistence-rank
    role: canonical-projection-stutter-boundary
  - concept: t5-global-well-foundedness-contract-v2
    role: fixed-protocol-order-and-local-rank
  - reproduction: reproductions/type_i_high_support_c1_local_minimum_boundary.py
    role: symbolic-C1-boundary-and-p73-two-bundle-control
visibility: public
last_checked: '2026-08-21'
---

# 高支撑 C=1 的固定协议局部最小元与付费退出边界

## 1. 精确范围

固定核心素数 \(p\equiv1\pmod{24}\)，令

\[
B_p=\frac{(p-1)^2}{4}.
\]

本卡讨论一个已经有 actual persistent receipt 的高支撑状态

\[
H=(p,R,K;A,\sigma),\qquad A>B_p,\qquad A\mid K,
\]

并额外假定

\[
C=K/A=1,\qquad \eta_p=0.
\tag{1}
\]

它不声称此类 chart 对每个 \(p\) actual reachable，也不假定所有高支撑空改善状态均有
\(C=1\)。

## 2. 固定 T5 下的 no-go

在固定 \((p,\rho,\mathrm{TYPEI},\mathrm{CHARGED})\) 层，T5 local tuple 是

\[
\lambda(H)=\left(\left\lfloor\frac{B_p}{A}\right\rfloor,C,\eta_p,0\right)
=(0,1,0,0).
\tag{2}
\]

这是该层的字典序最小元。任一 complete-excess CHARGED endpoint 的 support \(M>A\)
和 cofactor \(c\ge1\) 给出 local tuple \((0,c,0,0)\)，故

\[
c=1\Longrightarrow\text{stutter},\qquad
c>1\Longrightarrow\text{strict rise}.
\tag{3}
\]

无论是否插入不入队的中间 chart，E5 都比较真实 parent 和最终 persistent endpoint，
所以同一 protocol 内的 finite macro 不能以内部先升后降替代 (3)。对于 \(C=1<p\)，
total-cofactor 公式 \(C_S=C_A+pt\) 强制 \(C_A=1,t=0\)，也只给出 canonical identity。

## 3. 显式 C=1 chart 与支撑冲突

刚刚越过 \(B_p\) 的最小 C=1 chart 是

\[
A_1=\frac{(p+1)^2}{4},\qquad
H_1(p)=\left(p,p+2,\frac{(p+1)^2}{4};\frac{(p+1)^2}{4}\right).
\tag{4}
\]

它的两个 determinant dual chart 为

\[
(R_d,K_d)=(p-2,B_p),\qquad
(R_r,K_r)=\left(3,\frac{3p+1}{4}\right).
\tag{5}
\]

二者的 natural support 都小于旧承诺 \(A_1\)。保留 joined support 时
\(\operatorname{lcm}(A_1,t)\nmid K_t\)，所以它们至多是需要独立 payment 的 forgetful
reset 候选，不能作为同层 CHARGED edge。

对 (4) 的 universal anchor，完整超额首块为 \(Q=2\)，其 canonical target 的 cofactor
为 \((p+1)/2>1\)，正是 (3) 的严格上升实例。它反驳了“仅凭 universal source 即有 C=1
下降 bundle”的过强论断。

## 4. 控制与开放量词

\(p=73\) 的两 bundle 算术控制确实能从 \(C=2\) 经一个不入队 checkpoint 到达 \(C=1\)，
并在真实 parent/target 间有 local rank 下降；但该素数已有 root terminal，且该 macro 未在冻结
surface 注册。因此它是 `analysis_evidence`，不是 selector edge。

本卡真正关闭的是

```text
H-C1-CHARGED-LOCAL-MINIMUM = ESTABLISHED
H-C1-SAME-PROTOCOL-BUNDLE-OR-TOTAL-COFACTOR-EXIT = IMPOSSIBLE
```

仍需为 actual、terminal-first-miss 的 C=1 状态证明 root terminal、outer-rank drop、
带 recursively total owner 的 lower-protocol/phase target，或 family-empty。更一般地，
\(C>1\) 且 improvement set 为空的 terminal-first-miss 高支撑状态仍属于
`GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY`；本卡没有把它们归约掉。

```text
T6-F2-NONPROPER-DISPATCH-TOTALITY = OPEN
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```

聚焦整数控制：

```bash
python3 reproductions/type_i_high_support_c1_local_minimum_boundary.py --verify
```
