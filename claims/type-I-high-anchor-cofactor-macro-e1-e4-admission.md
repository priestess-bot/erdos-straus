---
kind: claim
claim_id: type-I-high-anchor-cofactor-macro-e1-e4-admission
title: 高锚点 direct cofactor 宏步的 E1--E4 准入合同
statement: 固定核心素数 p。设一个已收费的 canonical 高锚 H=(p,R,K;A) 由精确父边 P->H 给出，并显式满足 high-R raw-source 的原始性 \(p\nmid R\)。确定性 high-R complete-excess bundle 从 H 构造 transient overflow S=(p,R_M,K_M;A)，而通过 A/gcd(A,C)|r gate 的 cofactor 构造从 S 得到 canonical 高 target T=(p,R_T,K_T;lcm(A,C))。若三段回放具有连续的 state/scope/content hash，且 H,S,T 均重新验证为 typed F/G/hit 状态并以图表无关的 Sol(p) 作恒等解提升，则组合宏步 H=>T 满足 E1--E4。此为宏级准入定理；它不把 transient S 伪装成父边的直接 successor，也不单独给出 E5。E5 由高锚 direct-cofactor 与外层支撑秩的既有 Lambda_p 拼接另行支付。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-same-chart-support-promotion
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-direct-cofactor-lexicographic-rank
  - type-I-high-anchor-cofactor-outer-rank-composition
  - denominator-escape-state-contract
topics:
  - type-I
  - high-carrier
  - r-chart
  - cofactor
  - macro-edge
  - charged-support
  - source-provenance
  - F-state
  - G-state
  - solution-lift
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_cofactor_macro_replay.py
    role: independent H-to-S-to-T macro replay with E1--E5/Lambda_p checks
  - result: reproductions/type-i-high-anchor-cofactor-macro-replay-results.json
    role: p=1201 h=0 F-F-F and p=60913 h=2 G-G-F verified macro receipts
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: legacy S-to-T cofactor verifier and deliberately empty charged-parent registry
  - reproduction: reproductions/type_i_high_r_chart_two_anchor.py
    role: F-to-F macro parent, bundle, and cofactor replay at p=1201
  - reproduction: reproductions/type_i_high_r_chart_p3793_audit.py
    role: Legendre-G parent to F-to-F macro replay at p=3793
  - reproduction: reproductions/type_i_high_r_chart_60913_h2_nonreturn.py
    role: CRT-G-to-G-to-F macro replay at p=60913
  - result: reproductions/type-i-high-r-chart-two-anchor-results.json
    role: p=1201 E1--E4 and terminal-first receipt
  - result: reproductions/type-i-high-r-chart-p3793-audit-results.json
    role: p=3793 E1--E4 and terminal-first receipt
  - result: reproductions/type-i-high-r-chart-60913-h2-nonreturn-results.json
    role: p=60913 E1--E4 and terminal-first receipt
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 direct cofactor 宏步的 E1--E4 准入合同

## 1. 正确的边形状

high-cofactor 的收费来源不是当前 overflow carrier 自己，而是其此前的高 canonical
锚。正确对象因而是三段宏，而非把中间状态当成父边的 successor：

\[
P\xrightarrow{\mathsf{parent}}H
\xRightarrow{\mathsf{bundle}}S
\xrightarrow{\mathsf{cofactor}}T.
\tag{1}
\]

其中 (P\to H) 是已验证的 charged-support 父边；(H\Rightarrow S) 是不入队的确定性
构造回执。尚未经过 terminal/alternate 优先门和 E5 支付时，(H\Longrightarrow T)
只是候选宏回执；只有在两项额外门都通过后，才可登记为 direct-cofactor 宏边：

\[
\boxed{H\Longrightarrow T.}
\tag{2}
\]

设

\[
H=(p,R,K;A),\qquad p<R<4A,\qquad pR+1=4K,\qquad A\mid K.
\tag{3}
\]

此外 high-\(R\) raw source 的原始性必须作为独立输入重放：

\[
R\ge3,\qquad R\equiv3\pmod4,\qquad p\nmid R.
\tag{3a}
\]

其中同余可由 chart 方程重算，但 \(p\nmid R\) 不由 (3) 推出。例如
\(R\) 可以是 \(p\) 的非零倍数；这时 raw \(p\)-source 的
\(\gcd(p,R)=1\) 条件失败，不能进入本宏。

父边必须精确结束于 (H)，即其 content-addressed `successor_state` 等于 (H) 的完整
状态，而不能等于下文重新构造出的 (S)。最常见的充分父边是
`overflow_same_chart_support_promotion_v1`：它保持 ((R,K)) 而把较小 support 提升到
(A)。也允许其它具名父 adapter，但它必须有自己的确定性回放器和完整 E1--E5 回执。

从 (H) 取 high-\(R\) raw source 和完整超额 bundle

\[
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},\qquad
\beta=(R-1)/Q,\qquad M=\operatorname{lcm}(A,Q).
\tag{4}
\]

要求 bundle 回执重新验证 (Q>1)、\(\beta\mid K\)、\((Q,\beta)=1\)、\(Q\nmid K\)、
\(p\nmid Q\)，以及其 raw source 的原始性。它确定给出 transient overflow

\[
S=(p,R_M,K_M;A),\qquad
K_M=MC,\quad C=p-d,\quad n=4M-R_M,
\quad pn=4Md+1,
\tag{5}
\]

并要求 (A\mid M)、(R_M>p)、
\(\operatorname{canonical\_chart}(p,M)=(R_M,K_M)\)。(S) 保留 (H) 的 charged
support (A)，但一般改变 ((R,K))，所以它不是 same-chart parent 的 successor。

写 (M=kp+r)，(1\le r<p)，并令

\[
g=(A,C),\qquad a=A/g,\qquad A_T=\operatorname{lcm}(A,C)=Ca,
\tag{6}
\]
\[
s=\frac{4rd+1}{p},\qquad R_T=4r-s,\qquad K_T=rC.
\tag{7}
\]

cofactor target 的代数 gate 为

\[
a\mid r
\quad\Longleftrightarrow\quad
A_T\mid K_T.
\tag{8}
\]

还要求 (s\in\mathbb Z_{>0})、(R_T>p)，以及

\[
\operatorname{canonical\_chart}(p,A_T)=(R_T,K_T).
\tag{9}
\]

令 (C_T=r/a)、(d_T=p-C_T)、(n_T=4A_T-R_T)，则 target 正规形必须逐项重算为

\[
K_T=A_TC_T,\qquad pn_T=4A_Td_T+1,
\qquad T=(p,R_T,K_T;A_T).
\tag{10}
\]

## 2. 宏回执的充分接口

下面的数据是使 (2) 成为 E1--E4 候选宏回执的充分合同。它也是未来注册宏 adapter 的
最小接口；它**不是**修改旧 `S -> T` verifier 的理由。

```text
certificate_type = high_anchor_cofactor_macro
parent_receipt      = verified P -> H edge
anchor_state        = exact H
bundle_receipt      = deterministic H -> transient S construction
intermediate_state  = exact S
cofactor_receipt    = deterministic S -> T construction
target_state        = exact T
source_tree_scope   = one propagated scope
marked_solution_lift = {source: Sol(p), successor: Sol(p),
                         lift: identity, direction: T_to_H}
macro_edge_id       = hash(parent_receipt_digest, parent adapter/verifier version,
                           H, bundle adapter/digest, S, cofactor derivation/version,
                           T, scope, typed-fibre digests, marked_solution_lift)
```

验证器须同时检查以下三种状态等式，而不是只比较一个父 successor：

\[
\begin{aligned}
&\mathsf{parent.successor}=H,\\
&\mathsf{bundle.source}=H,\qquad \mathsf{bundle.output}=S,\\
&\mathsf{cofactor.source}=S,\qquad \mathsf{cofactor.target}=T.
\end{aligned}
\tag{11}
\]

此外，完整 `parent_receipt_digest`（而不是只有其端点 `edge_id`）、
所有状态 ID、bundle/cofactor 内容摘要、三个 adapter/verifier version、
`marked_solution_lift` 和 `source_tree_scope` 必须重算。当前三个专用例都在
`fresh_source_tree_only` 内；这只能沿 (11) 传播，不能被宏回执制造，也尚未证明
适用于任意 `charged_history_only` 祖先。

在该接口下，E1--E3 的证明是直接的。

| 检查 | 由宏回执重放的内容 |
|---|---|
| E1 | (P\to H) 的 charged-support 来源、(3)、(3a) 的 high canonical 与 raw-source 原始锚、以及 (4)--(5) 的 raw-source/bundle 构造。 |
| E2 | (6)--(10) 的余因子、gate、canonical target 和 target overflow determinant。 |
| E3 | (11) 的连续状态等式、所有 hash、scope 和具名 parent/bundle/cofactor verifier。 |

因此 E3 的本质不是一个 `selector_status` 字符串，而是可从 (P,H,S,T) 重新执行的
组合证明。若把任一内容摘要换成另一个 bundle 或另一个 fiber 证书，`macro_edge_id` 必须
改变，旧回执不能沿用。

## 3. F/G typed 恒等提升

为得到 E4，宏的三个可分析图表都取同一个图表无关标记集：

\[
W_H=W_S=W_T=\operatorname{Sol}(p),\qquad
\Phi_{T\to H}=\operatorname{id}.
\tag{12}
\]

这不是“复制一份旧 fiber”。每个 (X\in\{H,S,T\}) 都必须按自己的
((R_X,K_X)) 重新分类并通过有类型验证：

| 类别 | 必需的局部证书 |
|---|---|
| `hit` / `F` | canonical witness、全局定向的 signed defect，及该图表上的重算。 |
| `G` | `target_fiber.status=empty`、其 `emptiness_certificate` 为对所有 (q\mid K_X) 平凡而对 (-1) 非平凡的 canonical separating character；`signed_defect.status=not_applicable`。 |

于是 F/G/hit 是 `certificate_context`，不是 (12) 的标记集定义。即使某一 G 图表的
局部 target fiber 为空，(12) 仍给出集合恒等映射；它不声称
\(\operatorname{Sol}(p)\) 为空。反之，若 (W_X) 被定义成该图表的中心 fiber，则 G
态的 (W_X) 为空，恒等映射不能作为这种标记的 nonemptiness lift。这是本准入合同中
图表无关 marking 的必要语义条件。

回执必须把 (12) 的 `marked_solution_lift` 连同方向 \(T\to H\) 纳入内容摘要；
它与 parent 的 `marked_solution_set={source:Sol(p), successor:Sol(p), lift:identity}`
是不同层级的对象，二者均不可省略。由 (12) 和逐图表 typed reclassification，E4 在
所有下列类型转移中成立：F-to-F、G-to-F、F-to-G、G-to-G；实际可用的 G 角色族仍须由
其各自 verifier 确定。故“只接受 F/hit”只是旧实现的能力限制，不是 direct cofactor
宏的数学条件。

## 4. 宏 E1--E4 准入定理

**定理。** 若 (3)--(11) 的 parent、bundle、cofactor 回放均成功，且 (12) 的 typed
fiber 与 `marked_solution_lift` 条件在 (H,S,T) 全部重算成功，则
(H\Longrightarrow T) 是一张满足 E1--E4 的 direct high-cofactor 候选宏回执。

**证明。** parent 回执把 charged support (A) 的合法性精确固定在 (H)，high-\(R\)
bundle 从该精确锚重放出 (5)，故 E1 成立。式 (6)--(10) 给出 gate、canonical target
和后继 overflow 正规形，故 E2 成立。式 (11) 使 parent、transient carrier 和 target
成为一条可重放的有向组合，且 scope 与 content hash 未被替换，故 E3 成立。最后，(12)
在同一方程 (4/p) 的解集上是恒等映射，而 F/G 证书均为逐图表重新验证的辅助分析
数据，故 E4 成立。证毕。

该定理故意不把严格势混入其中。只有 terminal/alternate 子菜单已完全检查且没有更高
优先级输出，并且 E5 已按 (H\to T) 的持久状态支付时，候选宏回执才可入队。若
(A_T>A)，可按具体相位由
[高锚点 direct cofactor 宏步的 token-Omega 良基秩](type-I-high-anchor-direct-cofactor-lexicographic-rank.md)
及 [高锚点 direct cofactor 与外层支撑秩重置的词典序拼接](type-I-high-anchor-cofactor-outer-rank-composition.md)
支付 E5；(h=0,c=1) 的完整 state/action identity 则必须作为 stutter 抑制，不能因本卡
的 E1--E4 结论而入队。

## 5. 三个已闭合控制宏

| (p) | ((H,S,T)) 的 fiber 类型 | 宏回放与 E1--E4 | terminal-first 结果 |
|---|---|---|---|
| 1201 | F, F, F | (P:(1839,552160;1)\to H:(1839,552160;986))，high bundle 给 (S=(2873071,862639568;986))，cofactor 给 (T=(1839,552160;27608))。专用回放的 `local_e1_e5` 全真，故 E1--E4 全真。 | 同 bundle 耗尽后的 formal low chart 给 Type I `terminal_leaf`；结果明确标记 `preempts_high_r_candidate_for_p1201=true`。 |
| 3793 | G, F, F | Legendre-19 G 同图表 parent 结束于 (H=(7011,6648181;1811))，bundle 给 (S=(48491103,45981688420;1811))，target 为 (T=(14255,13517304;3622))。`candidate_e1_e5` 全真。 | gap-7 直接 Type I `terminal_leaf`。 |
| 60913 | G, G, F | CRT discrete-log parity G parent 结束于 (H=(72259,1100378117;18647))，bundle 给 (S=(4949657351,75374619555366;18647))，(h=2) target 为 (T=(221435,3372067539;55941))。`candidate_e1_e5` 全真。 | gap-7 直接 Type I `terminal_leaf`。 |

三例目前仍由专用复现器标为 `candidate_transition`，不是因为 E1--E4 缺失：p=1201 的
旧整合状态把全局 E5 置为 false，另外两例尚未注册到统一 selector。独立
`high_anchor_cofactor_macro_replay_v1` 已对 p=1201 与 p=60913 重算 E1--E5，但二者
仍标为 `analysis_evidence`、`recursive_edge_eligible=false`；三例都已被
terminal-first 的 Type I 叶抢占。它们是宏准入证据，不是三个需要继续递归的困难余项。

## 6. 为什么旧 S-to-T registry 不能泛化

`registered_cofactor_charged_parent_replay(parent_state, source_state)` 的旧 schema 要求

\[
\mathsf{parent.successor}=\mathsf{source\_state}.
\tag{13}
\]

它适合一个真正直接的 (P\to S\to T) 结构，且目前故意以 `return False` 保持注册表
为空，防止一个序列化 status 被误当作 E3 证明。对 (1) 的 high macro，(13) 是错误的
对象等式。

(p=1201) 已给出具体反例：same-chart parent 的 successor 是

\[
H=(1201,1839,552160;986),
\]

但 bundle 的 intermediate source 是

\[
S=(1201,2873071,862639568;986).
\]

显然 (H\ne S)。因此把该已闭合宏塞入 (13) 会必然拒绝它；放宽 (13) 又会丢失
parent 到 bundle 的连续性。这不是缺少一个布尔开关，而是旧接口的边形状不同。正确的
升级方式是注册第 2 节的宏 verifier，并保留旧函数给真正的直接 (S\to T) 回执。

还有三个不能删除的边界：

1. (p=409,A=5) 的 generic control 已有 E1、E2、E4 和局部 E5，却因
   `charged_history_only` 的父回执没有已注册的确定性 replay 而 E3=false。support 数值或
   `serialized_charged_support_parent` 状态不能替代 parent verifier。
2. (p=60913) 的 G-to-G-to-F 宏有有效 CRT 分离角色并通过 E4。故 generic selector
   中只接受 F/hit endpoint 的检查不是必要条件；统一 adapter 需要 typed-G verifier。
3. (p=1201) 的 (S) 因子分解为
   \(2^4\cdot7\cdot17^2\cdot29\cdot919\)，而 (T) 为
   \(2^5\cdot5\cdot7\cdot17\cdot29\)。两端 F witness 甚至维数和坐标都不同，不能从
   source 复制至 target。任何省略 reclassification 的“identity lift”都不是 E4 证明。

当前真正未闭合的统一化缺口因此很窄：实现并审计一个具名的
`high_anchor_cofactor_macro_replay_v1`，把 (11) 和 typed F/G verifier 接入 selector，
并为 `charged_history_only` 另行提供可回放的父链。它不应改写旧
`registered_cofactor_charged_parent_replay` 的直接 (S\to T) 语义。
