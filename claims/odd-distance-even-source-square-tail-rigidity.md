---
kind: claim
claim_id: odd-distance-even-source-square-tail-rigidity
title: 奇距离偶源公式的平方尾刚性
statement: 在奇距离偶源状态中，令 (r,M)=1、e=-M mod r 且 e|M^L。原尾公式 u=(M+e)/r、v=Mu/e 满足 v 为整数当且仅当 e|M^2。因此把平方尾的因子条件直接放宽到 M^L（L>2）不能产生同一公式下的新递降证书。
claim_status: established
topics:
- type-I
- descent
- even-source
- divisor-residues
- rigidity
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源公式的平方尾刚性

在奇距离偶源的固定状态中，令

\[
(r,M)=1,\qquad e\equiv-M\pmod r,\qquad e\mid M^L
\]

并沿用原尾公式

\[
u=\frac{M+e}{r},\qquad v=\frac{Mu}{e}. \tag{1}
\]

因为 \(e\mid M^L\) 和 \((r,M)=1\)，有 \((r,e)=1\)。由 \(ru=M+e\)，可得

\[
e\mid Mu
\Longleftrightarrow
e\mid rMu
\Longleftrightarrow
e\mid M(M+e)
\Longleftrightarrow
e\mid M^2. \tag{2}
\]

故

\[
v\in\mathbb Z\Longleftrightarrow e\mid M^2. \tag{3}
\]

这说明 \(M^2\) 在这条公式中不是可任意放宽的经验界，而是尾分母整性的精确门槛。
高次 \(M^L\) 的残数命中可以作为“额外重数需要多少”的诊断，但无法直接转化为同一
偶源提升的单位分数解。更强地，固定源端首项 \(1/(dM)\) 时所有两尾分解都已由
\((ru-M)(rv-M)=M^2\) 穷尽，见
[奇距离偶源固定首项的两尾完备性](odd-distance-even-source-fixed-first-tail-completeness.md)。

在十亿 H19 的 40 个有限积集型状态中，首次高次残数命中的 338 个因子候选全部使
\(v\) 非整数，其中有 32 个甚至满足 \(e\le M\)。这与式 (3) 的刚性完全一致。

因此任何利用指数缺口的正向方案必须改变尾部公式、构造不同源解，或使用多步带标记
提升；单纯把原引理中的 \(M^2\) 替换为 \(M^L\) 不会前进。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_finite_product_exponent_profile.py
python3 reproductions/type_ii_h19_tail_exponent_rigidity.py
python3 -m unittest tests/test_type_ii_h19_tail_exponent_rigidity.py -q
~~~
