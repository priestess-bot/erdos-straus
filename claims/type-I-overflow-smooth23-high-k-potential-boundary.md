---
kind: claim
claim_id: type-I-overflow-smooth23-high-k-potential-boundary
title: 2,3-光滑 overflow 高 k 的外层势硬边界
statement: 对 P=2^a 3^b、p=4P+1、r=2、d=P/2、M=kp+2、A=M 且 B_p=(p-1)^2/4，若 M>B_p/2，则当前外层势 Phi(A)=floor(B_p/A)=1，任何 M<L<=B_p 都不可能给出严格势下降。若 B_p/3<M<=B_p/2，则 Phi(M)=2，任何严格目标必须满足 L>B_p/2。q=2 的 multiple-M 候选失败自动进入势硬尾；q=3 时先出现 Phi=2 中间带，再进入 Phi=1 硬尾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-smooth23-low-k-fixed-n-cofactor
  - type-I-overflow-fixed-n-bounded-divisor-saturation
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: outer-potential E5 contract
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact threshold receipts
topics:
  - type-I
  - overflow
  - smooth-support
  - high-k
  - outer-rank
  - fixed-n
  - proof-boundary
visibility: public
last_checked: '2026-08-04'
---

# 2,3-光滑 overflow 高 \(k\) 的外层势硬边界

## 1. 外层势

设

\[
B_p=\frac{(p-1)^2}{4},\qquad
M=kp+2,\qquad
A=M,\qquad
\Phi(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

如果

\[
M>\frac{B_p}{2},
\]

则 \(1<B_p/M<2\)，从而

\[
\Phi(M)=1.
\]

任意当前 fixed-\(n\) 候选若要严格下降，必须满足 \(M<L\le B_p\) 和
\(\Phi(L)<\Phi(M)\)。但正整数势不可能小于 1，因此不存在任何满足当前 E5
势条件的 fixed-\(n\) 支撑增长或 support-reset 边。

这条结论与 \(L\) 是否为 \(M\) 的倍数无关；它是整个当前外层势的硬边界。

## 2. 中间带

若

\[
\frac{B_p}{3}<M\le\frac{B_p}{2},
\]

则

\[
\Phi(M)=2.
\]

此时严格下降的目标必须满足

\[
\Phi(L)\le1
\quad\Longleftrightarrow\quad
L>\frac{B_p}{2}.
\]

因此任何 \(L\mid Md\) 的候选都被压缩到窄区间

\[
\frac{B_p}{2}<L\le B_p.
\]

对 \(a=1\) 的参数族，\(d=3^b\)、\(q=3\)，低-\(k\) cofactor 候选在
\(3M>B_p\) 后失效；剩余先落入这条 \(\Phi=2\) 中间带，随后在
\(2M>B_p\) 后进入 \(\Phi=1\) 硬尾。对 \(a\ge2\)，\(q=2\)，
\(2M>B_p\) 与 multiple-\(M\) 候选失效同步。

## 3. 研究含义

高-\(k\) 硬尾不能再用当前
\[
\Phi(A)=\left\lfloor B_p/A\right\rfloor
\]
支付任何 fixed-\(n\) 严格递降。要继续推进，必须引入：

1. 不依赖 \(A\) 的 Type I/II 直接证书；
2. 保持不同支撑语义的 alternate carrier；
3. canonical-\(R\)、q-进相位或其它不可重置的第二良基秩；
4. 跨状态容量矛盾。

本卡不声称高-\(k\) 状态可达，也不声称它们是 Erdős--Straus 反例；它只精确说明
当前 fixed-\(n\)+外层势合同在何处失效。

统一 selector 在五个种子上重算 \(B_p\)、全局 \(k\) 区间、\(B_p/3\) 与
\(B_p/2\) 阈值，并将 \(\Phi=2\) 中间带和 \(\Phi=1\) 硬尾写入
outer_potential_boundary 回执。

重放命令：

python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

