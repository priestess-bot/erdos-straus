---
kind: claim
claim_id: type-II-q-one-full-carrier-second-anchor-overflow
title: q=1 full-carrier 首 child 的第二 anchor 低重图表严格 no-go
statement: >-
  设 p=24t+1 是 ordinary q=1 G full-carrier root 已经以其唯一首个严格 Type I
  dispatch 送出的 child。若在该 child 的 universal anchor R-1 上按完整超容量幂块
  Q 重建 M=lcm(A,Q) 并取 canonical chart pR_M+1=4K_M、1<=R_M<4M，则无论 t
  奇偶都有 R_M>p。奇数 t 时 Q=10t+1 且低 R 同余类只含原 chart；偶数 t=2s 时
  所有低 R 同余类只有原 chart 与 p-2，而 Q 必含一个 q|6s-1、q 不整除
  B_p=(p-1)^2/4 的素因子，排除后者。故 root 的首个 child 不可能通过第二次
  anchor complete-excess rechart 再产生 low marked-absorb state；任何此机制的继续
  必进入 high-overflow interface。该结论是严格的局部 no-go，不给出该 overflow 的
  E1--E5 递降、终端或全局 exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-type-I-carrier-rail-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - complete-excess
  - anchor
  - overflow
  - low-rechart-no-go
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: admitted-root-and-first-strict-child
  - claim: type-II-q-one-type-I-carrier-rail-dispatch
    role: parity-child-formulas
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: anchor-complete-excess-definition
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: canonical-chart-and-low-marked-edge-contract
  - reproduction: reproductions/type_ii_q_one_full_carrier_second_anchor_overflow.py
    role: focused-parity-identity-and-low-candidate-verifier
visibility: public
last_checked: '2026-08-15'
---

# \(q=1\) full-carrier 首 child 的第二 anchor 低重图表严格 no-go

## 1. 问题与精确范围

固定一个已经由
[full-carrier phase-root 准入](type-II-q-one-full-carrier-phase-root-entry.md)
送入 Type I tree、并执行完其强制首个 dispatch 的 ordinary \(q=1\) G root。对所得
child chart \((p,R,K;A)\)，universal source 的 anchor 为 \((1,R-1,1)\)。记

\[
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},
\qquad
\beta=\frac{R-1}{Q},
\qquad
M=\operatorname{lcm}(A,Q).
\tag{1}
\]

这里 \(Q\) 是完整超容量素数幂块，而不是 \((R-1)/(R-1,K)\) 的简写。令

\[
1\le R_M<4M,
\qquad
pR_M\equiv-1\pmod {4M},
\qquad
K_M=\frac{pR_M+1}{4}.
\tag{2}
\]

若 \(R_M<p\)，则 \(R_M\equiv3\pmod4\)，故它是一个新的 low marked-rechart
候选。下面证明这个候选在两个首 child 中都不可能出现。

本卡只处理 (1)--(2) 的确定性 anchor 算术。它不把 child 的 target-side universal
raw source 自动提升为一条新的 recursive edge，也不声称 (2) 的 high-overflow 已有
终端、全域 lift 或严格良基下降。

## 2. 奇 \(t\)：低同余窗只含原 chart

设 \(t\) 为奇数。首 child 是

\[
R_o=20t+3,
\qquad
K_o=(8t+1)(15t+1),
\qquad
A_o=16t+2=2(8t+1).
\tag{3}
\]

其 anchor 为

\[
R_o-1=2(10t+1).
\tag{4}
\]

有

\[
\begin{aligned}
(10t+1,8t+1)&=(10t+1,2t)=1,\\
(10t+1,15t+1)&=(10t+1,5t)=1.
\end{aligned}
\tag{5}
\]

又因 \(t\) 为奇数，\(v_2(R_o-1)=1\le v_2(K_o)\)。所以 (1) 精确化为

\[
\boxed{Q_o=10t+1,\qquad\beta_o=2,\qquad
M_o=2(8t+1)(10t+1).}
\tag{6}
\]

特别地 \(M_o\nmid K_o\)。任何 (2) 的候选与原 chart 都满足

\[
R_M\equiv R_o\pmod {4A_o}.
\tag{7}
\]

但

\[
R_o-4A_o=-44t-5<3,
\qquad
R_o+4A_o=84t+11>p-2.
\tag{8}
\]

因而在低区间 \([3,p-2]\) 中，(7) 唯一可能的值是 \(R_o\) 本身；这会要求
\(M_o\mid K_o\)，与 (6) 矛盾。故

\[
\boxed{R_{M_o}>p.}
\tag{9}
\]

这也可由 \(M_o=160t^2+36t+2>B_p=144t^2\) 直接看出，但 (7)--(8) 更明确地
排除了“同一低 chart 重放”。

## 3. 偶 \(t\)：唯一额外低 chart \(p-2\) 被新超额因子排除

设 \(t=2s\)。由于 \(p=48s+1\) 是核心素数，\(s=1\) 给出合数 \(49\)，故
\(s\ge2\)。首 child 是

\[
R_e=12s-1,
\qquad
K_e=9s(16s-1),
\qquad
A_e=9s,
\tag{10}
\]

anchor 为

\[
R_e-1=2(6s-1).
\tag{11}
\]

**引理。** \(Q_e\) 必含某个素数 \(q\mid6s-1\)。

**证明。** 若没有 \(6s-1\) 的素数幂超过 \(K_e\) 容量，则 \(6s-1\mid K_e\)。又

\[
(6s-1,9s)=1,
\tag{12}
\]

故 \(6s-1\mid16s-1\)。但

\[
16(6s-1)-6(16s-1)=-10,
\tag{13}
\]

这将推出 \(6s-1\mid10\)，与 \(s\ge2\) 矛盾。证毕。

该 \(q\) 与 \(6s\) 互素，故

\[
q\nmid B_p=\frac{(p-1)^2}{4}=576s^2,
\qquad q\mid Q_e\mid M_e.
\tag{14}
\]

另一方面，所有低 chart 必满足

\[
R_M\equiv R_e\pmod {4A_e} \pmod {36s}.
\tag{15}
\]

在 \([3,p-2]=[3,48s-1]\) 中只有两个可能值：

\[
R_e=12s-1,
\qquad
R_e+36s=48s-1=p-2.
\tag{16}
\]

第一值会要求 \(M_e\mid K_e\)，这违背 \(Q_e\) 的完整超容量定义。第二值对应

\[
K_{p-2}=\frac{p(p-2)+1}{4}=B_p,
\tag{17}
\]

但 (14) 表明 \(M_e\nmid B_p\)。所以没有任何低候选，且

\[
\boxed{R_{M_e}>p.}
\tag{18}
\]

## 4. 结论与研究后果

由 (9)、(18)，从 full-carrier root 的两个强制首 child 出发，第二个 anchor
complete-excess rechart 都必进入 \(R_M>p\) 的 high-overflow interface。

这排除了一个看似自然但错误的全局化设想：通过连续 low marked-absorb 支撑累积让
full-carrier tree 自动终止。这个 no-go 本身只确定接口；它不应被误读成 overflow
没有后继。该接口现已由
[第二 anchor overflow 的固定-\(n\) 严格宏出口](type-II-q-one-full-carrier-second-anchor-fixed-n-macro.md)
用 parity-specific 的闭式 carrier 接上。这里保留的结论仍是：不能再把同一 anchor
机制当作第二个 low rechart。

聚焦验证：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_second_anchor_overflow.py --verify
~~~
