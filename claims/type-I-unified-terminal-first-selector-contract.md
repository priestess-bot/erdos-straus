---
kind: claim
claim_id: type-I-unified-terminal-first-selector-contract
title: Type I 终端优先的近邻—广义二进—对偶统一选择器合同
statement: 对合法 Type I 状态，终端优先选择器按直接 Type I/II、目标纤维近邻、广义 2^j 偶前驱和固定层商 Fourier 的顺序输出 typed 回执；近邻与广义二进回执精确验证偶数前驱的整除、同余、范围和标准偶解，但在没有非空标记解及 E1--E5 前统一保持 analysis_evidence、recursive_edge_eligible=false。该合同统一了三类状态内证据，但不声称每个核心素数必命中或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-neighbor-terminal
  - type-I-general-dyadic-terminal-transfer
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-I-fixed-layer-stabilizer-defect-reduction
  - denominator-escape-state-contract
topics:
- type-I
- selector
- terminal-first
- target-fiber
- dyadic
- finite-fourier
- typed-certificate
- proof-boundary
- proof-program
sources:
- claim: type-I-target-fiber-neighbor-terminal
  role: near-pair-even-predecessor
- claim: type-I-general-dyadic-terminal-transfer
  role: dyadic-even-predecessor
- claim: type-I-fixed-layer-stabilizer-defect-reduction
  role: quotient-dual-evidence
visibility: public
last_checked: '2026-08-01'
---

# Type I 终端优先的近邻—广义二进—对偶统一选择器合同

## 1. 选择顺序

固定合法状态

\[
4K=pR+1,
\qquad R\equiv3\pmod4,
\qquad K=\prod_iq_i^{\nu_i}.
\]

选择器只按以下顺序登记状态内输出：

1. 已有直接 Type I/II 命中；
2. 目标指数纤维中的逐坐标近邻对；
3. 独立的广义 \(2^j\) 除子比值碰撞；
4. 固定层稳定子商上的规范 Fourier/格对偶证书。

前两类是算术偶前驱接口，第四类是对偶分析接口。选择顺序不把“有一个较小偶数”
误写成原状态已有解，也不允许用 Fourier 幅度替代终端或递降边。

## 2. 近邻回执

给定两个目标指数向量 \(z,w\)，验证

\[
|z_i|,|w_i|\le\nu_i,
\qquad
\prod_iq_i^{z_i}\equiv\prod_iq_i^{w_i}\equiv-1\pmod R,
\qquad
|z_i-w_i|\le\nu_i.
\]

定向后令

\[
\rho=\prod_iq_i^{z_i-w_i}=u/v<1,
\qquad
U=K\rho,
\qquad E=4U,
\qquad n=(4K-E)/R.
\]

回执必须重算 \(U\in\mathbb N\)、\(U\mid K^2\)、\(E\equiv1\pmod R\)、
\(E\le4K-4R\) 和 \(0<n<p\)。近邻引理还给出 \(4\mid n\)；统一回执同时保存
标准偶方程解

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\]

该解只属于较小方程。除非另有全域标记提升，否则回执为
`certificate_type=target_fiber_neighbor_terminal`、`selector_status=analysis_evidence`、
`terminal_kind=even_predecessor`、`lift_status=unproved`。

## 3. 广义二进回执

令 \(L=2K\)，给定互素 \(a,b\mid L\)、\(j\ge1\)，验证

\[
a\equiv2^jb\pmod R,
\qquad
1\le j\le v_2(L)+v_2(a)-v_2(b),
\qquad
a<2^jb.
\]

重新计算

\[
E_j=2^{1-j}L\frac ab,
\qquad
n=(2L-E_j)/R.
\]

必须检查 \(E_j\in\mathbb N\)、\(E_j\) 偶、\(E_j\mid L^2\)、
\(E_j\equiv1\pmod R\)、\(0<n<p\) 和 \(2\mid n\)，并保存同一个标准偶方程解。
回执为 `certificate_type=generalized_dyadic_terminal`，但在没有非空标记集和全域提升
之前仍为 `analysis_evidence`，不得登记 `verified_edge`。

对 finite-exponent F 状态，若采用自然分母 \(\alpha=nK/E_j\)，已有等价定理说明其
非空标记源恰等价于当前中心 Type I 命中。因此这类回执不能绕过 F 缺口；必须改用
新的标记集、改变尾项，或转入 external/capacity 分支。

## 4. 对偶回执

若前面没有直接算术输出，固定层稳定子 \(P\) 的商 Fourier 回执至少记录

```text
certificate_type = fixed_layer_quotient_fourier
selector_status = analysis_evidence
phase = DUAL_CERTIFICATE
finite_order_debt_fraction = [numerator, denominator]
carrier_mapping_status = unproved
recursive_edge_eligible = false
```

它可以保存商阶、稳定子阶、精确谱范数平方和相位债务，但不能独立承担 E4 解提升或
E5 良基下降。只有将角色阶/相位映射为带方向的算术载体，并完成状态合同的 E1--E5，
才可升级为 `verified_edge`。

## 5. 聚焦复现与边界

统一回执脚本为

```bash
python3 reproductions/type_i_unified_terminal_selector.py --verify
```

它从既有近邻、非近邻广义二进和固定层 Fourier 结果中重算三个 typed receipt；当前
示例分别给出 \(n=5596368\)、\(n=235724824\) 和角色阶债务 \(1/36\)。这些数值验证
接口一致性，不构成对所有核心素数的全称选择器定理。剩余全称缺口仍是：如何从
terminal-first 失败的 F/G 状态得到带颜色的 \(q\)-进容量超载，或得到满足 E1--E5 的
严格可提升递降。
