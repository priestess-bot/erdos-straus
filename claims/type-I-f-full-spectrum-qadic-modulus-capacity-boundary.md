---
kind: claim
claim_id: type-I-f-full-spectrum-qadic-modulus-capacity-boundary
title: 完整 F 谱的宽松 q 进模数容量排除边界
statement: 对冻结 200 压力素数完整线性谱中 2748 个达到 Fourier 下界的 F 状态，按 (p,q) 聚合 8526 个活跃方向。以每个方向的宽松需求 ceil((v_q(K)+2*1_{q=2})/2) 与该核心素数全部线性模数的总 v_q(K) 容量比较，6429 个分组没有发生超载，最大有限谱比值为 1；以模数差粗容量比较也没有超载，最大比值约为 0.42857。这排除了仅靠单素数、无颜色、无相位权重的容量方案，不能推出全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- finite-fourier
- q-adic
- capacity
- modulus-collision
- full-spectrum
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 完整 F 谱的宽松 \(q\) 进模数容量排除边界

## 审计对象

从 200 个冻结压力素数的完整线性谱中取 2748 个达到 Fourier 下界的 F 状态。
每个有界 Fourier 角色的每个活跃素数 \(q\) 都给出一个宽松高度需求

\[
h_{p,R,q}
=
\left\lceil
\frac{v_q(K)+2\mathbf 1_{q=2}}2
\right\rceil.
\]

该需求只使用
\(v_q(U)+v_q(V)=v_q(4K)\)
给出的高载体下界，不指定载体颜色，也不要求 Fourier 相位在不同状态中相同。

总计得到

\[
8526
\]

个活跃 \((p,R,q)\) 记录，按 \((p,q)\) 聚合为

\[
6429
\]

组。

## 两种宽松容量

第一种容量使用同一核心素数的完整线性模数集合，令

\[
\mathsf C_{p,q}
=
\sum_{R\ \mathrm{in\ complete\ spectrum}}v_q\!\left(\frac{pR+1}4\right).
\]

将该容量与同组需求之和比较，2748 个状态的 6429 组中没有超载；最大比值为
\(1\)，其中部分分组达到精确饱和。

第二种容量只使用模数差的粗上界

\[
\mathsf C^{\mathrm{coarse}}_{p,q}
\le
\frac{R_{\max}-R_{\min}}{4(q-1)}+H_{\max}.
\]

该更宽松的比较同样没有超载，最大需求/容量比约为
\(0.4285714\)。

## 逻辑含义

这个负面边界排除了一个过于简单的全局方案：

\[
\text{“每个 Fourier 活跃 }q\text{ 贡献半个 }v_q(K)
\text{，然后按 }(p,q)\text{ 独立装箱”。}
\]

要得到真正的容量矛盾，至少还需要加入一种不能被该宽松容量吸收的结构：

1. 载体颜色及标签—模数混合约束；
2. 多个活跃方向的联合高度；
3. Fourier 幅度/盒半径/相位预算形成的额外整数需求；
4. 目标纤维稀疏度或可提升终端成本。

因此，本卡把当前缺口从“有没有 \(q\) 进容量”收紧为“如何把对偶质量转成超过宽松
容量的联合需求”。它是完整冻结谱上的排除性边界，不是跨状态选择器定理。

## 复现

~~~bash
python3 reproductions/type_i_f_full_spectrum_qadic_modulus_capacity.py
~~~
