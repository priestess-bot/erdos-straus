---
kind: claim
claim_id: type-I-linear-multiblock-kneser-terminal-selector
title: 线性多层除子积集的 Kneser 终端选择判据
statement: 设 gcd(K,R)=1 且 K=N_1...N_r。令 A_i=A_R(N_i)、H=H_R(K)、T=Stab_H(A_1...A_r)。则 A_R(K)=A_1...A_r。若 -1∈H 但 -1∉C_R(K)，则 Σ_i|A_iT|−(r−1)|T|≤|H|/2，等价于商群中 Σ_i|A_iT/T|−(r−1)≤|H/T|/2。反向严格不等式必命中 -1∈C_R(K)；对线性源再结合 E=sR+1 得到偶终端桥。该判据可用于四标签层，但不证明至多三层子积必命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- multi-block
- divisor-residues
- additive-combinatorics
- Kneser-theorem
- terminal-bridge
- mixed-selector
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: multi-summand-Kneser-input
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-29'
---

# 线性多层除子积集的 Kneser 终端选择判据

## 多层设置

设 (R) 为奇数、(gcd(K,R)=1)，并给出一个不要求两两互素的因子分解

$$
K=N_1N_2\cdots N_r.
$$

定义每一层的普通除子残数集、总生成子群和总乘积集

$$
\mathcal A_i=\mathcal A_R(N_i),
\qquad
\mathcal H=\mathcal H_R(K),
\qquad
\mathcal A=\mathcal A_1\mathcal A_2\cdots\mathcal A_r.
$$

令

$$
T=\operatorname{Stab}_{\mathcal H}(\mathcal A).
$$

## 多层 Kneser 判据

有精确分解

$$
\mathcal A=\mathcal A_R(K).
$$

若

$$
-1\in\mathcal H,
\qquad
-1\notin\mathcal C_R(K),
\qquad
\mathcal C_R(K)=\mathcal A_R(K)\mathcal A_R(K)^{-1},
$$

则

$$
2|\mathcal A|\le|\mathcal H|.
$$

多层 Kneser 定理给出

$$
\boxed{
\sum_{i=1}^r|\mathcal A_iT|-(r-1)|T|
\le|\mathcal A|.}
$$

所以所有未命中的 F 型状态都满足必要不等式

$$
\boxed{
\sum_{i=1}^r|\mathcal A_iT|-(r-1)|T|
\le\frac{|\mathcal H|}{2}.}
$$

写

$$
\overline{\mathcal A_i}=\mathcal A_iT/T,
\qquad
\overline{\mathcal H}=\mathcal H/T,
$$

则同一条件等价于

$$
\boxed{
\sum_{i=1}^r|\overline{\mathcal A_i}|-(r-1)
\le\frac{|\overline{\mathcal H}|}{2}.}
$$

因此，只要找到一个层分解使

$$
\sum_{i=1}^r|\mathcal A_iT|-(r-1)|T|
>\frac{|\mathcal H|}{2},
$$

就必有

$$
-1\in\mathcal C_R(K).
$$

## 证明

逐素数写 (v_q(N_i)=e_{i,q})。若 (d\mid K)，则

$$
0\le v_q(d)\le\sum_i e_{i,q}.
$$

可把 (v_q(d)) 分配成 (r) 个整数 (f_{i,q})，满足

$$
0\le f_{i,q}\le e_{i,q},
\qquad
\sum_i f_{i,q}=v_q(d).
$$

于是 (d=d_1\cdots d_r)、(d_i\mid N_i)，故

$$
\mathcal A_R(K)\subseteq\mathcal A_1\cdots\mathcal A_r.
$$

反向包含显然成立，得到第一条积集恒等式。

在 F 型假设下，中心化谱的反足点刻画给出

$$
\mathcal A\cap(-\mathcal A)=\varnothing,
$$

从而 (2|\mathcal A|\le|\mathcal H|)。

将 (mathcal H) 商掉总乘积集的稳定子群 (T)。商群中的总乘积集无非平凡稳定子群；
否则其逆像会给出比 (T) 更大的原稳定子群。商群中每个真前缀乘积也无非平凡稳定子群，
因为若某个前缀存在非平凡平移稳定性，加上剩余层后总乘积仍保持该平移稳定性。
因此可反复应用无周期形式的 Kneser 不等式，得到

$$
|\overline{\mathcal A_1}\cdots\overline{\mathcal A_r}|
\ge\sum_i|\overline{\mathcal A_i}|-(r-1).
$$

乘回 (|T|) 即得多层不等式。与 F 型的半群大小上界联立即得必要条件及其反向充分
条件。证毕。

## 对线性源和原目标的作用

在线性源状态

$$
p=a+s+asR,
\qquad s\text{ 为奇数},
\qquad R\equiv3\pmod4,
\qquad K=\frac{pR+1}{4},
$$

可把 (K) 按源碰撞、源私有、仿射碰撞、仿射私有四层分解。上面的判据对这四层直接
给出一个全层密度证书。若另有端点 (t\equiv3\pmod4) 且
(-1\in\langle2\bmod R\rangle)，则二残数注入先保证 (-1\in\mathcal H)，多层密度严格
不等式随后直接推出目标平方除子命中。

一旦命中，互补因子可取 (d\le K)，并由线性源同时取

$$
E=sR+1,
\qquad E\mid4K,
\qquad E\equiv1\pmod R,
\qquad 2\mid E,
\qquad E\le4K-2R,
$$

从而得到原混合终端选择器要求的 Type I 正规形和偶因子。

这条判据并不证明“至多三层子积必命中”：它允许只有四层联合积才越过半密度阈值。
因此它与三标签层重选猜想的关系是：

* 三层子积命中是更强的、带层数上界的目标；
* 多层 Kneser 违反半密度是当前已证明的充分条件；
* 若四层判据也失败，则未命中状态必须在稳定子群商中保留明确的半密度缺口。

下一步应研究这些缺口是否能沿标签层逐层消耗，或是否能被另一个线性模数状态的层分解
打破；这才是从局部多层判据走向全称混合终端选择器的跨状态步骤。
