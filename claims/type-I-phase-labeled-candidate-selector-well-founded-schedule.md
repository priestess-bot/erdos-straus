---
kind: claim
claim_id: type-I-phase-labeled-candidate-selector-well-founded-schedule
title: 重图表与形式吸收的不可逆两阶段良基调度
statement: 固定 s 因子前向边与其降 R 代数逆边在未增广图表图中形成精确二环，完整 m=1 形式图还含 terminal-free 自环，因此不存在沿这些无阶段全边同时严格下降的状态势。若把候选选择器增广为不可逆 PRE->ABSORB 两阶段：PRE 只允许降 a 的固定 s 边，ABSORB 固定 min 或 max 方向并只允许降 R 重图表及相应形式剪枝，则 phase-tagged 势 PRE=(1,a,0,0)、ABSORB=(0,R,m,r_epsilon) 严格下降；更小 equation rank 可置于最外层并重置阶段。该定理只提供 E5 调度，formal 边仍须独立补足 E1--E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-source-factor-transfer-rigidity
  - type-I-canonical-complete-support-rechart-g-obstruction
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - denominator-escape-state-contract
topics:
  - type-I
  - selector
  - state-machine
  - rechart
  - formal-target-pair
  - well-founded-potential
  - phase
  - proof-boundary
sources:
  - claim: type-I-linear-source-factor-transfer-rigidity
    role: PRE-fixed-s-edge
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: ABSORB-formal-pruning
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: m-one-cycle-and-self-loop-boundary
  - claim: denominator-escape-state-contract
    role: E1-through-E5-acceptance-contract
visibility: public
last_checked: '2026-07-31'
---

# 重图表与形式吸收的不可逆两阶段良基调度

## 1. 未分阶段的全边系统不可能良基

设一张线性源图表满足

\[
p=a+s+asR.
\tag{1}
\]

若 \(Q>1\)、\(Q\mid a\)、\(Q\equiv1\pmod s\)，固定 \(s\) 因子边为

\[
X=(a,s,R)\longrightarrow
Y=\left(\frac aQ,s,QR+\frac{Q-1}{s}\right).
\tag{2}
\]

它严格降低 \(a\)，但增大 \(R\)。若同一个全局图又允许 (2) 的降 \(R\) 代数逆边，
就立即得到

\[
X\longrightarrow Y\longrightarrow X.
\tag{3}
\]

两步后不仅 \(a,s,R\) 恢复，\(K\)、支撑、Fourier 类型和从图表重算的缺陷字段也全部
恢复。因此不存在任何只依赖未增广算术图表状态、并沿 (3) 两边都严格下降的良基势。

一个核心实例是

\[
p=73,
\]

\[
X=(2,1,35,K=639)
\longrightarrow
Y=(1,1,71,K=1296).
\tag{4}
\]

前向边在 (2) 中取 \(Q=2\)。反向写 \(p=4t+1,t=18,u=t/Q=9\)，则

\[
R_X=4u-1=35,
\qquad
K_X=u(p-Q)=639,
\tag{5}
\]

精确返回 \(X\)。若两端标记集都取图表无关的 \(\operatorname{Sol}(73)\)，两边提升映射
都是恒等映射；二环问题纯粹发生在 E5，而不是 E4。

还有一个独立障碍。对

\[
(p,R,K)=(1009,3,757),
\tag{6}
\]

中心 Type I 谱 miss，但完整 \(m=1\) 形式节点满足

\[
\{1,2\}\xrightarrow{2}\{1,2\}.
\tag{7}
\]

所以即使删去图表逆边，只要 ABSORB 阶段仍允许全部 \(m=1\) 形式边，严格势仍然不存在。
必须固定 \(\min\) 或 \(\max\) 的一个剪枝方向；被拒边只能做一步直接终端前瞻。

## 2. 增广的两阶段状态

候选选择器增加一个不可逆阶段标签

\[
\mathrm{phase}\in\{\mathrm{PRE},\mathrm{ABSORB}\}.
\tag{8}
\]

ABSORB 状态还记录一次性选择的方向

\[
\varepsilon\in\{\min,\max\}
\tag{9}
\]

以及形式 cursor \((A,B,m)\)。允许边严格限定如下。

### 2.1 PRE 阶段

PRE 只允许 (2) 的固定 \(s\) 因子前向边，因此 \(a\) 严格下降。可以在每个图表做全部
terminal-first 核验，但不允许任何降 \(R\) 的代数逆边或 absorption rechart。

### 2.2 唯一的阶段提交

选择器可以恰好一次从 PRE 提交到 ABSORB。提交可重建形式 cursor 并选择
\(\varepsilon\)，但禁止任何 ABSORB 到 PRE 的无成本返回。

### 2.3 ABSORB 内的固定图表边

固定 \(R\) 时：

1. 若 \(m>1\)，保留全部 formal \(q\) 边，因为每条边都严格降低 \(m\)；
2. 若 \(m=1\)，只保留严格降低

   \[
   r_{\min}=\min(A,B)
   \quad\text{或}\quad
   r_{\max}=\max(A,B)
   \tag{10}
   \]

   中已选 \(r_\varepsilon\) 的边；不降低的边只执行一步 terminal lookahead；
3. 同一 ABSORB 图表中不能切换 \(\varepsilon\)。两个方向应作为两棵独立分支运行。

### 2.4 ABSORB 内的跨图表边

只允许已经独立通过其它合同项、且满足

\[
R_{\mathrm{new}}<R
\tag{11}
\]

的 rechart。由于 (11) 先严格下降，新图表可以重置 cursor 和 \(\varepsilon\)。ABSORB
禁止固定 \(s\) 前向边以及任何增 \(R\) 边。

## 3. phase-tagged 良基势

在字典序 \(\mathbb N^4\) 中定义分型势

\[
\Pi(S)=
\begin{cases}
(1,a,0,0),&S\text{ 位于 PRE},\\
(0,R,m,r_\varepsilon),&S\text{ 位于 ABSORB}.
\end{cases}
\tag{12}
\]

每类允许边都严格降低 (12)：

1. PRE 内由 \(a'<a\) 下降；
2. PRE 到 ABSORB 由首分量 \(1\to0\) 下降；
3. ABSORB 内固定 \(R\) 的高层边降 \(m\)，底层剪枝边降 \(r_\varepsilon\)；
4. ABSORB rechart 先降 \(R\)，故可安全重置后续字段。

因此增广后的候选边系统良基。等价的序数和写法是：PRE 使用独立的 \(a\) 段，
ABSORB 使用 \((R,m,r_\varepsilon)\) 段，并把整个 ABSORB 段置于 PRE 段之下。

若另有真正的较小 equation target 或 marked rank \(\rho\)，可把它放在最外层：

\[
\Pi_{\mathrm{all}}(S)=(\rho(S),\Pi(S)).
\tag{13}
\]

任何严格降低 \(\rho\) 的合法 E4 边都可以重置阶段、图表与 cursor。

## 4. 为什么普通字段重排不够

普通的 \(\operatorname{lex}(m,\mathrm{phase},R,as)\) 不成立，因为降 \(R\) rechart 后的
新 cursor 可以有更大的 \(m\)；把 \(m\) 放在 \(R\) 前会拒绝合法候选。统一使用
\((R,a)\) 也不成立：PRE 边增大 \(R\)，而 ABSORB 逆边可能增大 \(a\)。必须让字段的
解释依赖 phase，而不是只重排同一组无类型坐标。

若允许 ABSORB 无成本返回 PRE，(3) 会重新出现为增广周期。除非另有一个置于 phase
之前、每次 reset 都严格下降的自然数预算，否则禁止返回是必要条件。当前 support
deficit 不能充当该预算，因为已有重图表会使素数退出后重新进入，仓库尚无“退出永久”
定理。

## 5. 与 E1--E5 合同的关系

本卡严格解决的是调度层的 E5 兼容性：一条候选边若已经有合法后继、正规形和全域解
提升，就可以按所在 phase 使用 (12) 验证严格下降。

它不解决以下缺口：

1. formal cursor 边仍没有独立的 equation target 和 marked solution set；
2. formal 边仍没有 \(W_T\to W_S\) 的全域提升；
3. phase 提交本身不证明 ABSORB 中必有终端或降 \(R\) rechart；
4. 两个剪枝方向的并集不能当作一棵共同良基递归树。

所以这是一张 phase-labeled candidate selector 的良基调度定理，不是猜想的递降闭合。
聚焦边界由

~~~bash
python3 reproductions/type_i_formal_linear_chart_slab_boundaries.py --verify
~~~

中的图表二环与 terminal-free 二进自环共同复现。
