---
kind: claim
claim_id: type-I-bounded-monotone-support-phase-rank
title: 固定素数的有界单调支撑相位秩
statement: 固定 \(p\equiv1\pmod {24}\)，令 \(B_p=(p-1)^2/4\)。在任一对全部非终端后继闭合的 Type I 状态子图中，若每个状态的 absorbed support 满足 \(1\le A\le B_p\)，且每条递归边严格满足 \(A_S<A_T\)，则 \(H_p(S)=B_p-A_S\in\mathbb N_0\) 是严格良基 E5 秩。它严格细化该子图上的 \(\Pi_p(A)=\lfloor B_p/A\rfloor\)：\(\Pi_p(A_T)<\Pi_p(A_S)\) 蕴含 \(H_p(T)<H_p(S)\)，反向一般不成立。该秩不适用于支撑可越过 \(B_p\)、可下降或可经 forgetful RESET 重入的路径，因而不能单独把 cofactor r-chart 升格为递归 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - denominator-escape-state-contract
  - type-I-overflow-phase-reset-cycle-boundary
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-overflow-cofactor-r-chart-support
topics:
- type-I
- overflow
- absorbed-support
- well-founded-descent
- phase-rank
- proof-boundary
sources:
  - reproduction: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: existing box-exit and RESET-cycle boundary receipts
  - reproduction: reproductions/type-i-high-r-chart-two-anchor-results.json
    role: bounded-support high-r candidate receipt
visibility: public
last_checked: '2026-08-06'
---

# 固定素数的有界单调支撑相位秩

## 1. 定义与定理

固定素数 \(p\equiv1\pmod {24}\)，写

\[
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

考虑固定 \(p\) 的一个状态子图 \(\mathcal G_p^\uparrow\)。这里的“闭合”只指：
每条被调度为继续递归的非终端边，其后继仍在 \(\mathcal G_p^\uparrow\) 中；终端证书
允许离开该图。设每个状态 \(S\) 的已吸收支撑为 \(A_S\)，并假设

\[
1\le A_S\le B_p,\qquad
S\longrightarrow T\ \Longrightarrow\ A_S<A_T.
\tag{2}
\]

定义

\[
H_p(S)=B_p-A_S.
\tag{3}
\]

则 \(H_p(S)\in\mathbb N_0\)，并且每条递归边满足

\[
H_p(S)-H_p(T)=A_T-A_S\ge1.
\tag{4}
\]

故 \(H_p\) 是 \(\mathcal G_p^\uparrow\) 上的严格良基秩；从 \(S\) 出发的递归路径
长度至多为 \(B_p-A_S\)。

这一定理的限制条件是实质性的。它不要求临时 overflow carrier \(M\le B_p\)，只约束
状态中持久化的 absorbed support \(A\)。因此一个高载体中间图表仍可被此秩处理，
前提是调度器没有丢弃旧支撑并且下一个持久化支撑仍在盒内。

## 2. 与既有容量势的关系

既有局部容量势为

\[
\Pi_p(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{5}
\]

在 (2) 的图内，

\[
\Pi_p(A_T)<\Pi_p(A_S)
\Longrightarrow A_T>A_S
\Longrightarrow H_p(T)<H_p(S).
\tag{6}
\]

第二个蕴含不能反推为第一个。以 \(p=73\)、\(B_p=1296\) 为例，

\[
A:1000\longmapsto1001
\tag{7}
\]

使 \(H_p\) 从 \(296\) 降到 \(295\)，但 \(\Pi_p\) 在两端均为 \(1\)。
所以 (3) 在有界单调图上允许比 floor 跳变更细的 E5 付款。

若 \(A\mid A'\) 且 \(A'>A\)，则 \(A'\ge2A\)，既有 \(\Pi_p\) 已严格下降。
因此本秩不扩大 bundle、lcm 或 same-chart support promotion 的这一部分覆盖；
它真正新增的是那些 \(A<A'\le B_p\) 但不保证 \(\Pi_p\) 跳变的、已带明确
不重置 ledger 的候选。

## 3. 对高 \(R\) r-chart 的精确作用

\(p=1201\) 的两锚点 r-chart 有

\[
B_p=360000,\qquad A_S=986,\qquad A_T=27608.
\tag{8}
\]

故

\[
H_p(S)=359014>332392=H_p(T).
\tag{9}
\]

虽然中间 overflow carrier 是

\[
M=906134>B_p,
\tag{10}
\]

它不是该秩的状态支撑；(9) 依然有效。这说明局部 r-chart 的势下降不是因为
\(M\) 落在容量盒内，而是因为持久化的 \(A\) 严格上升。

然而 (9) 不能自行给出全局 E5。要把该例升级为递归边，调度器仍必须证明：每个以后
非终端分支都保持 (2)，或在离开 \(\mathcal G_p^\uparrow\) 前先给出 Type I/II
终端或另一条已验证的外层递降。

## 4. 必要边界

盒外分支不能被 (3) 覆盖。现有 \(p=73\) fixed-\(n\) 回执含

\[
A=66\longmapsto1518>B_{73}=1296.
\tag{11}
\]

此时形式值 \(H_{73}(1518)=-222\) 不在 \(\mathbb N_0\)，即使原有
\(\Pi_{73}\) 已从 \(19\) 降为 \(0\)。因此 \(H_p\) 不能替代所有既有的
容量势分支。

forgetful RESET 也会破坏单调性。聚焦的 \(p=73\) 回执有 continuation 环

\[
132\longmapsto330\longmapsto132.
\tag{12}
\]

相应 \(H_{73}\) 取值为

\[
1164\longmapsto966\longmapsto1164.
\tag{13}
\]

所以禁止支撑下降和重入不是表述上的附加条件，而是 (3) 成为 E5 秩的必要闭包门。

## 5. 研究接口

该引理把 cofactor r-chart 的全局化问题缩成一个可检验的接口：

\[
\text{每个后续非终端分支}\quad
\Longrightarrow\quad
\bigl(A_T>A_S,\ A_T\le B_p\bigr)
\quad\text{或}\quad\text{终端/其他已验证外层秩}.
\tag{14}
\]

证明 (14) 才会把局部的高 \(R\) 候选接入统一递归；在此之前，它仍保持
candidate_transition 与 recursive_edge_eligible=false。
