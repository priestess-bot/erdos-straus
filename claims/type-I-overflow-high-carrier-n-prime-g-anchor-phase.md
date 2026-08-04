---
kind: claim
claim_id: type-I-overflow-high-carrier-n-prime-g-anchor-phase
title: 高载体 n=p G-anchor bundle 的精确相位二分
statement: 设核心素数 p=1 (mod 24)，B_p=(p-1)^2/4，Q=(p-3)/2，且 A|B_p、B_p/A>=2。令 c=(p-1)/6，并令 t_A 为 0<=t_A<A 中满足 c+p*t_A=0 (mod A) 的唯一整数。则 M=AQ 的 canonical chart 满足 R_M=R_Q+4Q*t_A、R_Q=(p-4)/3、K_M=Q(c+p*t_A)。因此 R_M<p 当且仅当 A|(p-1)/6；此时 M<=B_p 且该算术分支是 conditional bundle marked-absorb 候选。若 A 不整除 (p-1)/6，则 R_M>p；若同时 M<=B_p，已有同图表支撑升级只需来源回执即可条件支付，若 M>B_p 才进入真正的 high-carrier bundle overflow。两支都不自动提供 source provenance、标记提升或 E1--E5 递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-n-prime-normal-form
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-same-chart-support-promotion
topics:
- type-I
- overflow
- high-carrier
- n-equals-p
- G-state
- anchor
- bundle
- phase
- canonical-chart
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact G-anchor phase classifier and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: synthetic arithmetic phase profiles
visibility: public
last_checked: '2026-08-04'
---

# 高载体 \(n=p\) G-anchor bundle 的精确相位二分

## 1. 规范输入

由高载体 \(n=p\) 正规形，G 图表为

\[
K_r=B_p=\frac{(p-1)^2}{4},
\qquad R_r=p-2.
\]

令

\[
Q=\frac{p-3}{2},
\qquad c=\frac{p-1}{6}.
\]

因为 \(p\equiv1\pmod {24}\)，有

\[
\gcd(Q,B_p)=1,
\qquad
R_Q=\frac{p-4}{3},
\qquad
K_Q=Qc.
\tag{1}
\]

考虑一个已携带的 proper support \(A\mid B_p\)，满足 \(B_p/A\ge2\)。将 G-anchor 的
完整超额块并入支撑，令

\[
M=AQ.
\]

这里把 \(A\) 作为来源合同的输入；本卡不从任意 \(n=p\) 算术边界自动构造该来源。

## 2. 精确相位公式

令 \(t_A\) 是区间 \(0\le t_A<A\) 中满足

\[
c+p t_A\equiv0\pmod A
\tag{2}
\]

的唯一整数。唯一性来自 \(p\nmid A\)。由 (1) 有

\[
p(R_Q+4Qt_A)+1=4Q(c+p t_A),
\]

所以 \(M=AQ\) 的规范图表恰为

\[
\boxed{
R_M=R_Q+4Qt_A,
\qquad
K_M=Q(c+p t_A).
}
\tag{3}
\]

右端 \(K_M\) 被 \(AQ\) 整除正是 (2) 的支付条件。由于

\(0\le t_A<A\) 且 \(0<R_Q<4Q\)，(3) 落在 canonical chart 的唯一代表区间内。

## 3. 低相位与 overflow 二分

若 \(t_A=0\)，则 \(A\mid c=(p-1)/6\)，且

\[
R_M=R_Q=\frac{p-4}{3}<p,
\qquad
M=AQ\le cQ<B_p.
\]

因此该行满足同图表 marked-absorb 所需的算术容量条件

\[
A\mid M,\qquad M/A=Q\ge2,\qquad M\le B_p,\qquad R_M<p.
\]

若 \(t_A\ge1\)，则

\[
R_M\ge R_Q+4Q>p
\]

（核心素数 \(p\ge73\)），所以该行精确进入 bundle overflow。于是

\[
\boxed{
R_M<p\iff t_A=0\iff A\mid\frac{p-1}{6}.
}
\tag{4}
\]

相位二分还必须与 carrier domain 分开记录。若 \(t_A\ge1\) 但 \(M=AQ\le B_p\)，则

\[
A\mid M,\qquad M/A=Q\ge2,\qquad M\le B_p,\qquad
R_M>p,
\]

在来源回执已经携带 \(A\) 的前提下，现有同图表支撑升级可支付一个保持图表的
overflow 后继；它不是终端，但外层支撑势严格下降。只有 \(AQ>B_p\) 时，才进入真正的
高载体 overflow 残差，需要另一个载体、直接证书、容量或不可重置外层秩。

低相位只说明“若来源回执确实携带 \(A\)，则同图表 E1--E5 具有可支付的算术形状”；
它不提供来源路径、标记集、全域解提升或严格势下降的完整证据。选择器因此将两种相位都
保存为 `analysis_evidence`，而不是递归边。

## 4. 聚焦算术回执

统一选择器用没有 raw Reach provenance 的合成 supports 重算两组 profile：

| \(p\) | supports | 低相位 | 同图表 overflow | 真高载体 |
|---:|---|---:|---:|---:|
| 73 | \(1,2,3,4,6,8,12,18,48\) | 6 | 2 | 1 |
| 97 | \(1,2,3,4,6,8,9,16,64\) | 5 | 3 | 1 |

例如 \(p=97\) 时 \(Q=47,c=16\)：\(A=16\) 给 \(t_A=0,R_M=31<p\)，而
\(A=3\) 给 \(t_A=2,R_M=407>p\)。这些 profile 只验证 (1)--(4)，不声称对应的
support 已由某条完整来源路径产生。

另有一条真实来源锚定回执：原始高载体
\[
(p,M,d,n)=(73,1332,1,73)
\]
的对偶 G 图表是 \((R,K)=(71,1296)\)，其 G_marked_absorb source/anchor 记录给出
\(A=1,Q=35,R_Q=23\) 的低相位行。这里必须区分原始 carrier \(M=1332\) 与对偶图表
\(K=B_{73}=1296\)；回执含 raw source/anchor provenance，但仍没有完整 E1--E5，
所以状态保持 analysis_evidence。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

## 5. 研究边界

该二分把 exact \(n=p\) 高载体族从未分类参数压成一个确定的 G-anchor phase。真正的
后续问题是：对来源可达的 \(A\)，低相位能否补齐 source bundle 的 E1--E5 回执；对
\(A\nmid(p-1)/6\) 的高相位，能否找到 alternate、直接 Type I/II 或跨状态良基秩。
公式本身不是这些全称结论的替代物。
