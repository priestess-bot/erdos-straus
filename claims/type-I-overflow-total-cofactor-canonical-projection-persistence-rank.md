---
kind: claim
claim_id: type-I-overflow-total-cofactor-canonical-projection-persistence-rank
title: 整体余因子折叠的 canonical 投影、精确容量秩与持久化门
statement: >-
  固定 p≡1 (mod 24) 与 charged support A。任一满足 pn=4Md+1、A|M、
  M=Ab 的 determinant chart，在整体余因子折叠 bd=ph+delta 后都投影到只由
  (p,A) 决定的唯一 canonical chart。若 C_A 是 (4A)^{-1} mod p 的最小正代表，
  则目标为 K_A=AC_A、R_A=(4AC_A−1)/p，源容量 C_S=K_S/A 唯一写成
  C_S=C_A+pt，且 K_S−K_A=Ap t、R_S−R_A=4A t。因而 queued source 上
  t>0 等价于严格 K/A 下降，t=0 等价于 canonical stutter；由此在固定 p、只含
  paid outer-rank、既有 direct-cofactor 与 support-preserving queued canonical
  descent 的子图上，(floor(B_p/A),K/A) 是严格良基秩。但该下降只能比较真实持久
  source 与 target：若 determinant chart 只是 parent 内部 receipt，必须比较
  parent->target。若对仓库 p=1201 的内部 receipt 尝试备选整体折叠，容量
  874888->560 却精确投影回 parent chart (R,K;A)=(1839,552160;986)，故
  persistence gate 不可删除；这不是原宏记录的 proper-cofactor target。本卡不补 target
  的 E1--E4，也不授权跨 p、forgetful RESET 或内部 receipt 的伪递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-mod-p-fold-r-descent
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - total-cofactor
  - canonical-projection
  - residual-capacity
  - charged-support
  - persistence-gate
  - well-founded-descent
  - selector
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-mod-p-fold-r-descent
    role: total-cofactor-arithmetic-fold
  - claim: type-I-high-anchor-cofactor-outer-rank-composition
    role: paid-outer-and-direct-cofactor-edge-contract
  - claim: type-I-high-anchor-cofactor-macro-e1-e4-admission
    role: persistent-anchor-transient-intermediate-recorded-target-semantics
  - reproduction: reproductions/type_i_overflow_total_cofactor_canonical_projection_rank.py
    role: focused-projection-rank-and-persistence-boundary
  - reproduction: reproductions/type-i-high-anchor-cofactor-macro-replay-results.json
    role: existing-p1201-anchor-and-transient-provenance-for-derived-alternative-fold
visibility: public
last_checked: '2026-08-09'
---

# 整体余因子折叠的 canonical 投影、精确容量秩与持久化门

## 1. 由 \((p,A)\) 决定的唯一目标

令 \(p\equiv1\pmod {24}\) 为素数，并考虑一个 determinant chart

\[
pn=4Md+1,
\qquad 1\le d<p,
\qquad A\mid M,
\qquad M=Ab.
\tag{1}
\]

由 (1) 可知 \(p\nmid A\)。记

\[
C_A:=\langle(4A)^{-1}\rangle_p\in\{1,\ldots,p-1\},
\tag{2}
\]

即 \(C_A\) 是 \((4A)^{-1}\bmod p\) 的最小正代表。对整体余因子作 Euclidean
分解

\[
bd=ph+\delta,
\qquad h\ge0,
\qquad 1\le\delta<p.
\tag{3}
\]

式 (1) 给出 \(4Abd\equiv-1\pmod p\)，所以

\[
\delta\equiv-(4A)^{-1}\equiv-C_A\pmod p.
\tag{4}
\]

由两边均取标准代表，得到

\[
\boxed{\delta=p-C_A.}
\tag{5}
\]

总折叠的目标

\[
(M_T,d_T,n_T;A_T)
=\left(A,\delta,n-4Ah;A\right)
\tag{6}
\]

因而具有唯一 canonical 坐标

\[
\boxed{
K_A=AC_A,
\qquad
R_A=\frac{4AC_A-1}{p},
\qquad
n_A=4A-R_A,
\qquad
d_A=p-C_A.
}
\tag{7}
\]

特别地，目标不依赖产生 source receipt 的临时 \(M,d,n\)；它只是 \((p,A)\) 的
canonical normal form。式 (2) 还给出 \(pR_A+1=4K_A\)，且
\(0<R_A<4A\)、\(R_A\equiv3\pmod4\)，所以 (7) 确为合法算术图表。

## 2. 精确 charged-capacity 商与幂等性

源 canonical 坐标为

\[
R_S=4M-n,
\qquad
K_S=M(p-d).
\tag{8}
\]

定义源的 residual charged capacity

\[
C_S:=\frac{K_S}{A}=b(p-d).
\tag{9}
\]

由 (3) 有

\[
\begin{aligned}
C_S
&=bp-bd\\
&=p(b-h)-\delta\\
&=C_A+p(b-h-1).
\end{aligned}
\tag{10}
\]

故存在唯一 \(t\in\mathbb N_0\) 使

\[
\boxed{
C_S=C_A+pt,
\qquad
t=b-1-\left\lfloor\frac{bd}{p}\right\rfloor.
}
\tag{11}
\]

结合 \(pR+1=4K\)，得到精确差值

\[
\boxed{
K_S-K_A=Ap\,t,
\qquad
R_S-R_A=4A\,t.
}
\tag{12}
\]

因此整体折叠在 residual capacity 上就是取同余类 \(C_A\bmod p\) 的最小正代表：

\[
C_S\longmapsto C_A.
\tag{13}
\]

把 (13) 扩展到 \(b=1\) 的 normal-form 操作后，它是幂等投影。严格性边界也完全
精确：

\[
\boxed{
t=0\iff C_S=C_A<p
       \iff (R_S,K_S;A)=(R_A,K_A;A),
}
\tag{14}
\]

\[
\boxed{
t>0\iff C_S>p
       \iff R_A<R_S
       \iff K_A/A<K_S/A.
}
\tag{15}

这也重新解释了旧门 \(b(p-d)>p\)：它恰是 charged capacity 尚未处于最小正代表的
条件，而不是一个偶然的 \(R\) 不等式。

## 3. 适用于真实 queued 边的统一精确秩

令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
\Pi_p(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{16}
\]

考虑固定 \(p\) 的**持久状态子图**：每个顶点都是内容寻址、可实际进入递归队列的
合法 charged state

\[
pR+1=4K,\qquad A\mid K,\qquad R>0,
\]

但不要求 source 已经是相对 \(A\) 的 normal form。事实上，(12) 表明任何严格总折叠
source 都满足 \(R_S=R_A+4At>4A\)，所以加入这个错误要求会把全部严格 `C` 边排除。
每条非终端边仍须独立通过 E1--E4，且只允许是：

1. `O`：已证明 \(\Pi_p(A_T)<\Pi_p(A_S)\) 的 paid outer-rank 边；
2. `D`：既有 high-anchor direct-cofactor 边，并抑制完整 \(c=1,h=0\) 自环；
3. `C`：保持 \(A_T=A_S\) 且严格满足 \(K_T<K_S\) 的 queued charged descent，
   包括通过 (15) 的整体余因子投影，以及既有严格因子转移或交换。

则

\[
\boxed{
\Lambda_p^\sharp(S)
=\left(\Pi_p(A_S),\frac{K_S}{A_S}\right)
\in\mathbb N_0\times\mathbb N
}
\tag{17}
\]

是每条边上的严格良基秩。

证明只需逐类核对。`O` 由第一坐标支付。`C` 保持第一坐标并严格降低第二坐标。
对 `D`，正相位与 \(A\le B_p\) 的严格零相位均按已有定理严格降低
\(\Pi_p\)；若 \(A>B_p\)，严格零相位满足

\[
K_T=K_S,
\qquad
A_T=cA_S,
\qquad c>1,
\tag{18}
\]

故 \(K_T/A_T=(K_S/A_S)/c<K_S/A_S\)。唯一不下降的 \(c=1,h=0\) 已按定义不入队。
字典序 \(\mathbb N_0\times\mathbb N\) 良基，定理得证。

相较旧秩 \((\Pi_p(A),\Omega(K/A))\)，精确商不能被素因子重数替代。例

\[
(p,A,M,d,n)=(73,58,116,14,89)
\tag{19}
\]

中，总折叠使

\[
K/A:118=2\cdot59\longmapsto45=3^2\cdot5.
\tag{20}
\]

所以 \(K/A\) 严降，而 \(\Omega\) 反从 \(2\) 增至 \(3\)。

## 4. persistence gate 不能删除

式 (12) 比较的是 determinant receipt \(S\) 与其投影 \(T\)。E5 的 source 却必须是
真实递归边的持久 source。若 \(S\) 只是 parent adapter 内部生成、从未作为独立状态
入队的 bundle receipt，则实际宏步是

\[
H\longrightarrow T,
\tag{21}
\]

而不是 \(S\to T\)。此时必须重算 \(\Lambda_p^\sharp(H)\) 与
\(\Lambda_p^\sharp(T)\)；临时 receipt 的下降没有 E5 资格。

仓库已有 \(p=1201\) 宏回执提供一个真实 anchor--transient 链。parent anchor 为

\[
H=(R,K;A)=(1839,552160;986),
\qquad K/A=560.
\tag{22}
\]

其不入队的内部 complete-excess receipt 是

\[
(M,d,n;A)=(906134,249,751465;986),
\tag{23}
\]

对应

\[
(R_S,K_S;A)=(2873071,862639568;986),
\qquad b=919,
\qquad C_S=874888.
\tag{24}
\]

因为

\[
bd=919\cdot249=1201\cdot190+641,
\tag{25}
\]

若在这个已记录 transient 上**另行尝试**保持 \(A=986\) 的整体余因子折叠，则得到

\[
(M_T,d_T,n_T;A_T)=(986,641,2105;986)
\tag{26}
\]

和

\[
(R_T,K_T;A_T)=(1839,552160;986)=H.
\tag{27}
\]

这是由已有 anchor/intermediate 推导出的 `derived_alternative_target`，不是原宏 JSON
记录的 proper-cofactor target。原宏取 \(g=34\)，记录的 target 是

\[
(R,K;A)=(1839,552160;27608),
\qquad
\Lambda_{1201}^\sharp:(365,560)\longmapsto(13,20),
\tag{28}
\]

并不 stutter。相反，若 selector 试图把上述**备选总折叠 action** 注册为宏，则内部比较
虽有 \(874888\to560\) 的巨大下降，真实持久端点却是 \(H\to H\)，故 (17) 完全相等。
这个例子严格排除了“只要 transient \(R\) 或 \(K/A\) 下降就登记该 action”的升级规则，
同时不否定现有 proper-cofactor 宏的严格秩。

## 5. 仍未支付的合同

本卡把整体折叠的 E5 问题精确分成两类：

- source 本身是 queued/content-addressed state 时，(15) 加 (17) 支付 E5；
- source 是 parent 内部 receipt 时，必须先通过 persistence gate，并按真实
  parent--target 端点重新证明严格性。

它没有自动生成 target 的 source/path/node scope、F/G、hit、纤维、`state_id`、
terminal-first 结果或全域解提升，因此不补 E1--E4。它也不覆盖跨 \(p\)、未付款
RESET、raw/noncanonical carrier 或 capability-changing 同算术自环。当前整体余因子
折叠仍是 `candidate_transition`；下一项是实现具名 target-state adapter，并在回执中
显式保存 `persistence_source_state_id`、`arithmetic_receipt_id` 与真实端点的
\(\Lambda_p^\sharp\) 前后值。

聚焦复现：

```bash
python3 reproductions/type_i_overflow_total_cofactor_canonical_projection_rank.py --verify
```
