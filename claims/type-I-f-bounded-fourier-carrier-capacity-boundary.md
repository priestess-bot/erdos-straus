---
kind: claim
claim_id: type-I-f-bounded-fourier-carrier-capacity-boundary
title: 冻结 F 状态规范 Fourier 载体容量边界
statement: 对冻结的 45 个 F 型关系格状态，规范有界 Fourier 选择产生 141 个实际正载体方向。逐条用线性源 U=sR+1、V=aR+1 重算 q 进高度，并在同一核心素数的同色纤维及混色并集中检查标签--模数整除和混合容量界；同色有 113 组（15 个非单例），混色有 100 组（21 个非单例），所有 128 次两两整除检查和两类容量界均通过，没有容量超载。该结果是有限负边界：角色阶、相位预算尚未转化为额外跨状态高度需求，因此没有得到全称选择器或递归边。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-certificate
  - type-I-linear-multi-active-fourier-carrier-vector
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
topics:
- type-I
- F-state
- finite-fourier
- linear-source
- carrier
- q-adic
- capacity
- cross-state
- proof-boundary
- proof-program
sources:
  - claim: type-I-f-bounded-fourier-certificate
    role: canonical-Fourier-input
  - claim: type-I-linear-hybrid-label-modulus-q-adic-capacity
    role: exact-capacity-bound
visibility: public
last_checked: '2026-08-02'
---

# 冻结 F 状态规范 Fourier 载体容量边界

## 复核对象

输入是
`reproductions/type-i-f-bounded-fourier-certificate-results.json`，其 SHA-256 为

```text
97bd474f82271b3d6a1eb5260fc49b7d48551c4fc2872402b74759f3d817bd68
```

对每个记录，脚本重新调用线性源枚举器，恢复

\[
U=sR+1,\qquad V=aR+1,
\]

并验证 Fourier 记录中的颜色、载体素数 \(q\) 和高度确实等于
\(v_q(U)\) 或 \(v_q(V)\)。这一步不把相位分母、角色阶或 Fourier 质量冒充整数块高度。

## 精确结果

复现脚本
`reproductions/type_i_f_bounded_fourier_carrier_capacity.py --verify` 输出：

| 字段 | 数值 |
|---|---:|
| F 状态数 | 45 |
| 载体方向数 | 141 |
| 同色 \((p,q,\mathrm{label})\) 组 | 113 |
| 同色非单例组 | 15 |
| 混色 \((p,q)\) 组 | 100 |
| 混色非单例组 | 21 |
| 两两整除检查 | 128 |
| 整除失败 | 0 |
| 容量超载组 | 0 |

对同一核心素数和固定 \(q\)，若两条方向的标签不同，检查

\[
q^{\min(h_i,h_j)}\mid |t_i-t_j|;
\]

若标签相同，检查

\[
q^{\min(h_i,h_j)}\mid |R_i-R_j|,
\]

其中 \(h_i=v_q(t_iR_i+1)\)。随后对每个组应用

\[
\sum_i h_i\le
\frac{M_tM_R}{q^2-1}+\frac{M_t+M_R}{q-1}+H.
\]

所有检查均以整数整除和有理数比较完成。包含单例组时容量比的最大值为 1，这是
\(M_t=M_R=0\) 时右侧恰为 \(H\) 的平凡饱和；排除单例后，同色最大比为
\(12835/186111\)，混色最大比为 \(38505/4787548\)，均远未达到超载。

## 逻辑边界

这项复核确立了一个精确的负边界：规范 Fourier 证书的载体字段能够无损地投影到
实际线性块，并满足现有容量账本，但在冻结样本中没有产生跨状态容量矛盾。因此下列
推理仍然无效：

- 把角色阶或相位债务直接加到 \(h_i\)；
- 因为 Fourier 证书非平凡就要求所有状态重复同一 \(q\) 和颜色；
- 把容量通过解释为标记集非空、解提升或 E1--E5 递归边。

若要沿这条路线推进全称选择器，必须新增一个独立的相位—载体匹配定理：它要么把
非空投影的相位缺口转成有方向的额外高度需求，要么把高阶/空投影证书转成一个已经
证明非空且势严格下降的 support-switch。当前结果只登记为
`analysis_evidence`，不承担递归。

## 复现

```bash
python3 reproductions/type_i_f_bounded_fourier_carrier_capacity.py --verify
```

结果文件为
`reproductions/type-i-f-bounded-fourier-carrier-capacity-results.json`。
