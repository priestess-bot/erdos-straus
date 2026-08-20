---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure
title: H4 clean q-bridge 的修正版 E1–E5 相对宏闭包
statement: >-
  设 P 是已经通过现有 19-phase H4 source/provenance 验证器的 persistent parent，
  Lambda_p^#(P)=(0,p-1)，且版本化的较早 priority prefix 已给出 miss receipt。
  对 actual proper-overlap top-capacity a_alt=1 H4 receipt，令 clean q-word 到达
  primitive endpoint (x_q,y_q)，并相对 K_4 取唯一 maximal complete-excess 分解
  x_q=Q_x beta_x、y_q=Q_y beta_y。统一定义修正后的目标支撑
  M_q=lcm(M_4,Q_x,Q_y)。则 actual endpoint 只有 Q_x=1<Q_y 的 single-side
  或 Q_x,Q_y>1 的 atomic-split 两类；现有 universal first-stutter closure 给出
  c_q=< (4M_q)^(-1) >_p <= p-2。以 M_q 构造 canonical target
  K_q=M_q c_q、R_q=(4K_q-1)/p，并把 target 序列化为 pending_dispatch、禁止继承
  F/G/hit 标签，则 P 到该 target 的 H4 clean-q macro 满足 E1--E5：E1 的 actual
  source/path/maximality 可重算，E2 target 为确定整数构造，E3 canonical state/edge/
  owner receipt 唯一且后续类型必须重算，E4 是 Sol(p) 上恒等 lift，E5 有
  (0,c_q)<(0,p-1)。因此在上述 upstream actual-H4 receipt 与 priority-prefix miss
  前提下，H4 clean q-bridge 已闭合为 verified decreasing macro；若较早 priority
  命中 verified terminal/edge，则该分支更早闭合。本结论不重新证明 upstream
  19-phase H4 provenance，也不推出整个 H4、q=1 G handoff 或 Erdős--Straus 猜想闭合。
claim_status: established
proof_provenance: mixed
review_status: internal_review
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - complete-excess
  - persistent-macro
  - solution-lift
  - well-founded-rank
  - e1-e5
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-rank-and-composed-macro-discipline
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-endpoint-payload
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: corrected-unified-support-multiplier-and-unique-stutter-gate
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
    role: universal-first-stutter-exclusion
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: canonical-atomic-owner-and-e5-boundary
  - concept: denominator-escape-state-contract
    role: e1-e5-state-lift-and-rank-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py
    role: generic-relative-macro-verifier-and-receipt-serializer
visibility: public
last_checked: '2026-08-17'
depends_on:
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - denominator-escape-state-contract
---

# H4 clean q-bridge 的修正版 E1–E5 相对宏闭包

## 1. 证明边界

本卡关闭的是一个**相对宏**。它的输入不是任意整数，而是：

1. 一个已经由现有 19-phase H4 source/provenance 机制承认的 actual H4 receipt；
2. 原 persistent parent \(P\) 满足
   \[
   \Lambda_p^\sharp(P)=(0,p-1);
   \]
3. 进入 H4 macro 以前的版本化 priority prefix 已产生 `miss` receipt。

本卡不重新证明这些 upstream premises，也不允许用本卡反向制造 H4 provenance。

## 2. 修正后的支撑公式

令
\[
x_q=Q_x\beta_x,\qquad y_q=Q_y\beta_y
\]
为相对 \(K_4\) 的唯一 maximal complete-excess decomposition。

无论 endpoint 是 single-side 还是 atomic-split，都统一定义
\[
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
\]

这是必要的。actual single-side 已知是
\[
Q_x=1<Q_y.
\]
若仍使用旧公式 \(\operatorname{lcm}(M_4,Q_x)\)，就会退化为 \(M_4\)，完全漏掉唯一非平凡块 \(Q_y\)。

设
\[
L_q=M_q/M_4,
\qquad
E_x=\frac{Q_x}{(M_4,Q_x)},
\qquad
E_y=\frac{Q_y}{(M_4,Q_y)}.
\]
若 \(Q=Q_{K_4}(z)\)、\(L_0=\operatorname{lcm}(M_4,Q)/M_4\)，则 clean q-word 给
\[
Q_y=Q/q,
\qquad
E_y=L_0/q,
\]
且 endpoint primitive 给 \((Q_x,Q_y)=1\)，所以
\[
\boxed{L_q=E_xE_y=(L_0/q)E_x}.
\]

## 3. endpoint 完整二分

已有 clean-carrier、interior-prefix、actual-carry、p-primary exclusion 和 y-block nonempty 结果给出：

- \((q,K_4)=1\)；
- canonical q-word 可完整重放；
- 每个真前缀都保留一个不在 \(K_4\) 中的 q-prime，故不是 full-excess sink；
- actual carry 有 \(h=2d\)、\(hq=p+1\)；
- \(p\nmid Q_xQ_y\)；
- \(Q_y>1\)。

因此最终只可能是
\[
Q_x=1<Q_y
\]
的 single-side，或
\[
Q_x,Q_y>1
\]
的 atomic-split。

## 4. stutter 已完全排除

修正支撑下定义
\[
c_q=\left\langle(4M_q)^{-1}\right\rangle_p.
\]
由 top-capacity congruence 与上面的 multiplier identity，
\[
\boxed{c_q\equiv-qE_x^{-1}\pmod p}.
\]
因此
\[
c_q=p-1
\iff
E_x\equiv q\pmod p.
\]

single-side 有 \(Q_x=1\)，故 \(E_x=1\)，立即得到
\[
c_q=p-q\le p-2.
\]
atomic-split 的唯一 stutter gate 已由 universal source-D gate closure 与其 phase/valuation finite closures 完全排除。因此所有 actual endpoints 都有
\[
\boxed{1\le c_q\le p-2}.
\]

## 5. E1：source、path、maximality

E1 由 actual H4 receipt 加 canonical replay 完成：

- source state 与 persistent parent ID 固定；
- source-tree scope 固定为 `charged_history_only`；
- q-word 按 q 的素因子多重集确定性重放；
- 每一步检查所除素数在当前坐标的赋值严格高于 \(K_4\)；
- \(Q_x,Q_y\) 用 canonical maximal complete-excess 公式从整数重新计算；
- single-side 检查 \(x_q\beta_y\mid K_4\)；
- atomic-split 检查 \(\beta_x\beta_y\mid K_4\)、\((Q_x,Q_y)=1\) 与 p-free 条件。

所以 E1 不需要搜索或猜测候选 decomposition。

## 6. E2：canonical target

定义
\[
M=M_q,
\qquad
c=\langle(4M)^{-1}\rangle_p,
\]
\[
K'=Mc,
\qquad
R'=\frac{4K'-1}{p}.
\]

因为 \(p\nmid M\)，\(c\) 存在。由定义 \(4Mc\equiv1\pmod p\)，所以 \(R'\in\mathbb Z_{>0}\)，并且
\[
pR'+1=4K'.
\]
又因 \(p\equiv1\pmod4\)，有 \(R'\equiv3\pmod4\)。故 canonical target 的整数 chart 确定存在。

## 7. E3：canonical serialization 与 deferred dispatch

本宏的 edge validity 不依赖 target 的 F/G/hit 类型，而 marked set 始终是 \(\operatorname{Sol}(p)\)。因此 E3 采用如下严格约定：

1. target state ID 只由 canonical raw integers \((p,R',K',M)\)、scope/origin 与版本生成；
2. 不继承任何 source/H4 的 F/G/hit 标签；
3. target 明确标记 `dispatch_status=pending_dispatch`；
4. 下一条任何依赖 F/G/hit 的 selector action 在使用 target 前必须从这些 canonical integers 重新运行完整 classifier；
5. atomic endpoint 的 owner 由 adapter version、source state ID、canonical q-path、endpoint 与 maximal blocks 的 canonical digest 唯一确定；single-side 同理生成 canonical bundle ID；
6. priority-prefix receipt 的 policy version、source state ID 与 `miss` 状态写入 edge receipt。

这叫**延迟重算**，不是标签继承。pending 字段不得参与 E5。

## 8. E4：全域 solution lift

source parent 和 target 都使用
\[
W_P=W_T=\operatorname{Sol}(p).
\]
因此定义
\[
\Phi:W_T\to W_P,
\qquad
\Phi(u)=u.
\]
这是全域恒等映射，自动保持正整数分母和 \(4/p\) 的单位分数恒等式。因此 E4 完成。

## 9. E5：严格全局 rank

必须比较原 persistent parent 与最终 target，而不是比较中间 H4 checkpoint。

原 parent 有
\[
\Lambda_p^\sharp(P)=(0,p-1).
\]
由于 \(M_q\ge M_4>B_p=(p-1)^2/4\)，target 的第一 rank 坐标仍为 0；第二坐标为 \(c_q\)。而 stutter closure 给
\[
c_q\le p-2.
\]
因此
\[
\boxed{
\Lambda_p^\sharp(T)=(0,c_q)<(0,p-1)=\Lambda_p^\sharp(P).
}
\]
E5 完成。

## 10. 结论

若版本化的较早 priority action 已命中一个 verified terminal/edge，则 H4 分支已提前关闭；否则 priority-prefix miss 后，canonical H4 clean-q macro 满足 E1--E5，输出 `verified_edge`。

因此，在已经验证的 actual H4 provenance 与 priority-prefix premise 下，H4 clean q-bridge 不再是 active proof gap。

这只关闭该相对宏，不证明：

- upstream 19-phase H4 provenance 的全部来源；
- q=1 G 到 fresh Type I 的全称 handoff；
- 整个 global selector；
- Erdős--Straus 猜想。

## 11. 机器验证器

通用 verifier：

```text
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --input receipt.json
```

局部 arithmetic regression controls：

```text
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --verify-controls
```

controls 只测试该宏的整数重算与 serializer，不替代 upstream H4 provenance 证明。
