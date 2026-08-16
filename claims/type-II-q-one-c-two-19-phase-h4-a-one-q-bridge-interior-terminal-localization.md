---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
title: H4 clean q-bridge 的内部 full-excess Type I terminal 局部化
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 的 clean
  q bridge 中，令 canonical q-word 的任一真前缀除数为 e|q、e<q，并写
  (x_e,y_e)=(R4-z/e,z/e)。则 y_e 不整除 K4，故 x_e y_e 不整除 K4；该 primitive
  raw checkpoint 不会是 full-excess Type I sink。因而由完整超额 sink 所给的 Type I
  terminal 不会在 q-word 内部出现，只可能在 q endpoint 的 Q_x=Q_y=1 分派出现。
  再结合 endpoint p-primary 排除与首层 capacity-stutter 的全域关闭，actual nonterminal
  endpoint 只剩 p-free single-side 或 p-free atomic-split 的严格容量 pre-receipt，均有
  c_q<=p-2。该结论不把 state-level terminal/alternate priority、typed target、serializer
  或 atomic owner/ledger guard 自动升级为通过。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - raw-path
  - terminal-first
  - complete-excess-bundle
  - atomic-split
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-endpoint-taxonomy
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: actual-endpoint-p-free-domain
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
    role: all-actual-first-capacity-stutters-absent
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: full-excess-sink-to-Type-I-terminal-equivalence
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: two-sided-conditional-E1-to-E4-contract
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-rank-(0,p-1)
  - concept: denominator-escape-state-contract
    role: typed-edge-priority-and-lift-boundary
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py
    role: focused-prime-and-composite-q-prefix-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge 的内部 full-excess Type I terminal 局部化

## 1. 设置

保留 actual \(q=1\) high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) 的 clean \(q\)-bridge 记号：

\[
z=R_4-h,
\qquad
q>1,
\qquad
q\mid z,
\qquad
(q,K_4)=1.
\tag{1}
\]

后一个互素性来自 clean-carrier 引理。按 \(q\) 的规范素因子顺序，每个前缀乘积
\(e\mid q\) 给 primitive raw node

\[
\{x_e,y_e\}
=
\left\{R_4-\frac ze,\frac ze\right\}.
\tag{2}
\]

当 \(e=q\) 时，这正是已定义的 q endpoint \((x_q,y_q)\)。本卡只讨论 raw
form 的 full-excess terminal，不把任意 state-level terminal 或 alternate policy 偷换成
由 (2) 自动穷尽的对象。

## 2. 真前缀不可能是 full-excess sink

### 引理 1（clean q-word 的内部非汇性）

若 \(e\mid q\) 且 \(e<q\)，则

\[
\boxed{y_e=\frac ze\nmid K_4.}
\tag{3}
\]

**证明。** 取任意素数 \(\ell\mid q/e\)。由 \(q\mid z\)，

\[
v_\ell(y_e)=v_\ell(z)-v_\ell(e)
\ge v_\ell(q)-v_\ell(e)>0.
\tag{4}
\]

另一方面，\((q,K_4)=1\) 给 \(v_\ell(K_4)=0\)。所以 \(\ell\mid y_e\) 而
\(\ell\nmid K_4\)，即得 (3)。\(\square\)

尤其，\(e=1\) 的 small-anchor source 本身也不可能是 full-excess sink；这不是只对
中间素数 edge 的观察。

### 推论 2（内部 Type I terminal 不出现）

每个 (2) 中的 raw pair 都 primitive。由完整超额形式图的汇点刻画，full-excess
Type I terminal 恰要求

\[
x_e y_e\mid K_4.
\tag{5}
\]

对 \(e<q\)，(3) 已排除 (5)。故

\[
\boxed{
\text{clean q-word 的所有真前缀均不是 full-excess Type I terminal。}
}
\tag{6}
\]

这不是“原始 word 从未命中任何证书”的全称断言；它精确排除了由 `full-excess sink`
verifier 产生的 Type I 叶。若项目增加依赖 raw prefix 的其它 terminal/alternate
verifier，它仍须在 versioned priority policy 中单独列出。

## 3. 端点的严格容量 normal form

在 \(e=q\) 处写 maximal complete-excess 分解

\[
x_q=Q_x\beta_x,
\qquad
y_q=Q_y\beta_y.
\tag{7}
\]

已有 endpoint p-primary 排除给

\[
p\nmid Q_xQ_y.
\tag{8}
\]

若 \(Q_x=Q_y=1\)，则 \(x_qy_q\mid K_4\)，此时 (5) 给出 endpoint 的
full-excess Type I terminal。否则端点是 p-free nonterminal。已有 complete-excess
分派把它唯一送入单侧 payload 或双色 atomic-split payload；首层 source \(D\)-gate
闭包又给

\[
\boxed{c_q\le p-2.}
\tag{9}
\]

因此，若 \(P\) 是既有 19-phase persistent parent，则所有 nonterminal endpoint 的
算术势付款已经统一为

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_q).
\tag{10}
\]

注意这里没有残留的 q-bridge p-primary 或 capacity-stutter 条件；(8)--(10) 只使用
actual H4 source 与 endpoint 的算术信息。

## 4. 被局部化的 guard，与仍然开放的语义门

该结果给出一张精确的 q-word guard map：

| q-word 位置 | full-excess Type I terminal | 算术容量 | 尚未由本卡支付的内容 |
|---|---|---|---|
| \(e<q\) 的真前缀 | 由 (6) 自动否定 | 不作为 macro endpoint | raw-prefix 以外的新 priority verifier，若未来注册，仍须显式处理 |
| \(e=q, Q_x=Q_y=1\) | 直接 Type I terminal | N/A | 无；由 \((K_4/y_q,K_4/x_q,pK_4)\) 确定性输出 |
| \(e=q\)，恰一块非平凡 | 不为 full-excess sink | (9) 严格 | source/target typed state、priority prefix、serializer/scope |
| \(e=q, Q_x,Q_y>1\) | 不为 full-excess sink | (9) 严格 | 上述内容，加 atomic owner tuple、ledger 与 adapter validator |

所以 `full-excess` terminal-first 的 raw-path 检查不必沿 q 的每个内部 raw edge
逐一支付：其真前缀输出已由 (6) 数学地固定为 `no_output`。这缩小的是 guard 的
**范围**，不是把 guarded candidate 误登记为 `verified_edge`。

仍必须独立获得的回执是：

1. macro source 的 state-level terminal/alternate priority prefix；
2. source 和 canonical target 的完整 typed reclassification 与 scope 连续性；
3. canonical serializer、state/edge digest；双侧时还包括 atomic owner 与 ledger；
4. target 的 `pending_dispatch` 入口及后续 priority policy。

endpoint terminal 的直接 serializer 见
[endpoint full-excess sink 的 Type I terminal 证书](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-endpoint-terminal-serializer.md)。
单侧分支的 residual divisibility 已由 q endpoint 的算术自动给出；双侧分支不能拆成
两个旧单侧 action，必须调用既有 atomic-split contract。所有状态的 equation target
仍为 \(4/p\)，故当上述 guards 成功时 E4 是 \(\operatorname{Sol}(p)\) 的恒等提升，
而 (10) 支付 E5。

## 5. 聚焦回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py --verify
```

该回执仅检查既有 \(q=37\) 与 \(q=11^2\) local H4 controls 的全部真前缀都保留一个
不在 \(K_4\) 中的 q 因子。它不扫描素数区间、分母、历史 Reach 或 global selector。
