---
kind: claim
claim_id: type-I-overflow-phase-reset-cycle-boundary
title: overflow RESET 局部载体下降与重入循环边界
statement: 在聚焦的 p=73 RESET 回执中，每条 reset 都严格降低局部载体 support，但普通 anchor/lcm continuation 形成 132 与 330 的二环；因此 carrier-size 只能作为局部 RESET 秩，不能单独作为全局良基势。该回执的 E1--E4 已重算、E5 被循环见证拒绝，选择器必须标为 candidate_transition 而非 verified_edge。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-phase-labeled-candidate-selector-well-founded-schedule
topics:
- type-I
- overflow
- phase-reset
- well-founded-potential
- cycle
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: typed reset-cycle receipt and E5 boundary
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: frozen 38-132-330-132 witness
visibility: public
last_checked: '2026-08-03'
---

# overflow RESET 局部载体下降与重入循环边界

## 1. 局部算术边

对每个聚焦 RESET 行，源 overflow carrier 为 \(M\)，小对偶图表的 reset support 为
\(t\)，后续 ordinary anchor/lcm carrier 为 \(M'\)。回执重算：

\[
t<M,
\qquad
4K_M=pR_M+1,
\qquad
4K_t=pR_t+1,
\qquad
4K_{M'}=pR_{M'}+1.
\]

源、reset 和后继仍使用同一个 equation target \(4/p\)，标记集取图表无关的
\(\operatorname{Sol}(p)\)，因此恒等映射给出聚焦的 E1--E4。局部载体字段满足严格
\(t<M\)，但这只描述 RESET 的瞬时边。

## 2. 重入见证

在 \(p=73\) 上，规范 continuation 为：

\[
38\xrightarrow{\mathrm{RESET}\,+\,\mathrm{anchor/lcm}}132
\xrightarrow{\mathrm{RESET}\,+\,\mathrm{anchor/lcm}}330
\xrightarrow{\mathrm{RESET}\,+\,\mathrm{anchor/lcm}}132.
\]

其中 reset supports 依次为 \(12,30,12\)，中间 anchor bundle 都是 \(Q=11\)，
reset 图表为 \((R,K)=(23,420)\)。因此

\[
M_{\mathrm{next}}<M_{\mathrm{source}}
\]

并不对每条完整 continuation 成立；\(M=132\to330\) 甚至严格上升。循环节点
\(\{132,330\}\) 是 carrier-size 不能作为全局秩的精确反例。

## 3. typed 选择器边界

`selector_status=candidate_transition`
`recursive_edge_eligible=false`
E1=true, E2=true, E3=true, E4=true, E5=false
`missing_conditions=[E5]`

E5 的缺失不是局部算术错误，而是没有不可重置的外层 phase rank。因而选择器不得
把 \(t<M\) 的局部下降自动升级为递归边。

## 4. 研究含义

要把 RESET 纳入统一递归，至少需要以下之一：

1. 禁止 RESET 后的普通 anchor/lcm 增载边；
2. 证明 reset phase 只进入封闭的终端或已验证降 \(R\) 分支；
3. 引入一个每次 RESET 严格下降、且不会被 continuation 重置的外层 rank。

当前回执只排除“carrier-size 单独良基”的过强合同，不排除带新外层秩的 support
reset，也不构成 Erdős--Straus 反例。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于
`reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`phase_reset_receipts`。
