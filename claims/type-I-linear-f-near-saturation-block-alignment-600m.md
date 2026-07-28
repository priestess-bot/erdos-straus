---
kind: claim
claim_id: type-I-linear-f-near-saturation-block-alignment-600m
title: 近饱和 F 型状态的两块反足点对齐边界
statement: 若线性状态的正规化因子满足 K=gamma*L，定义 D_R(X)=A_R(X)A_R(X)^(-1)，则有精确恒等式 D_R(K)=D_R(gamma)D_R(L)，且一般 B 目标 -1 命中当且仅当 D_R(L) 与 {-x^(-1):x属于D_R(gamma)} 相交。对四个真实对抗核心中差集缺额不超过100的全部六个F型状态及十个有向源，逐项复核该恒等式和对齐判据；十个对齐交集均为空。最大差集覆盖状态 (p,R)=(26034649,375) 的两种方向分别给出 (|D_gamma|,|D_L|)=(15,51) 与 (41,33)，乘积均覆盖192/200个生成子群元素，目标374仍缺失。该结果是块级有限负边界，不证明跨源选择器反例或定理。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- centered-spectrum
- divisor-lattice
- difference-set
- block-alignment
- adversarial-core
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 近饱和 F 型状态的两块反足点对齐边界

## 精确块级判据

设 \(\gcd(K,R)=1\)，并写

\[
\mathcal A_R(X)=\{d\bmod R:d\mid X\},
\qquad
\mathcal D_R(X)=\mathcal A_R(X)\mathcal A_R(X)^{-1}.
\]

若 \(K=\gamma L\)，则逐素数指数区间相加给出

\[
\mathcal A_R(K)=\mathcal A_R(\gamma)\mathcal A_R(L).
\]

由于单位群交换，进一步有精确恒等式

\[
\boxed{
\mathcal D_R(K)=
\mathcal D_R(\gamma)\mathcal D_R(L).
}
\tag{1}
\]

因此一般 \(B\) 的目标条件等价于

\[
\begin{aligned}
-1\in\mathcal D_R(K)
&\Longleftrightarrow
\exists x\in\mathcal D_R(\gamma),\ y\in\mathcal D_R(L):xy=-1\\
&\Longleftrightarrow
\boxed{
\mathcal D_R(L)\cap
\{-x^{-1}:x\in\mathcal D_R(\gamma)\}\ne\varnothing.
}
\end{aligned}
\tag{2}
\]

式 (2) 是两块分析需要检查的**对齐条件**。单独知道两块的差集大小、生成子群大小或
各自没有 \(-1\)，都不能替代这个交集检查。

在线性源

\[
p=a+s+asR,
\qquad
K=\frac{pR+1}{4},
\]

按 \(s\pmod4\) 的正规化取

\[
\lambda=\begin{cases}4,&s\equiv1\pmod4,\\2,&s\equiv3\pmod4,\end{cases}
\qquad
\gamma=\frac{sR+1}{\lambda},
\qquad
L=\frac{aR+1}{4/\lambda},
\]

总有 \(K=\gamma L\)。

## 六个近饱和状态

输入是四个一般 \(B\) 唯一命中且全谱无 \(B=1\) 的对抗核心。先前的 45 个 F 型状态中，
差集缺额

\[
\delta_R=|\mathcal H_R(K)|-|\mathcal D_R(K)|
\]

不超过 100 的状态恰有六个。它们的完整块级结果为：

| \(p\) | \(R\) | \(|\mathcal H_R(K)|\) | \(|\mathcal D_R(K)|\) | 缺额 | 各有向源的 \((|D_\gamma|,|D_L|)\) |
| ---: | ---: | ---: | ---: | ---: | --- |
| 26,034,649 | 375 | 200 | 192 | 8 | (15,51), (41,33) |
| 57,399,241 | 59 | 58 | 39 | 19 | (9,5) |
| 57,399,241 | 83 | 82 | 61 | 21 | (27,9), (9,27) |
| 57,399,241 | 455 | 288 | 246 | 42 | (54,5) |
| 57,399,241 | 155 | 120 | 59 | 61 | (3,33), (33,3) |
| 283,319,689 | 131 | 130 | 63 | 67 | (3,27), (27,3) |

六个状态的十个有向源均满足：

\[
\mathcal D_R(L)\cap
\{-x^{-1}:x\in\mathcal D_R(\gamma)\}
=\varnothing.
\]

在最接近饱和的 \((p,R)=(26{,}034{,}649,375)\) 中，目标
\(-1\equiv374\pmod{375}\) 仍是八个缺失类之一：

\[
127,133,172,251,254,313,344,374.
\]

这说明 96% 的差集覆盖仍不能转化为目标对齐。两种源方向的块大小不同，但乘积差集均为
同一个 192 元集合；因此简单的“选定源方向”并未消除该 F 型障碍。

## 研究边界

这项审计确认了一个可直接使用的块级判据，但没有发现六个近饱和状态共享的简单缺失类
公式。当前可排除的过强路线是：

\[
\text{“某一块差集足够大”}
\Longrightarrow
\text{“两块必自动命中 }-1\text{”。}
\]

后续应研究缺失类在商群中的位置、碰撞/过剩指数层对对齐交集的影响，以及同一核心素数
其它 \(R\) 状态能否提供跨源拉回；不能只继续提高单状态差集密度下界。

## 复现

~~~bash
python3 reproductions/type_i_linear_f_near_saturation_block_alignment_600m.py
python3 -m unittest tests/test_type_i_linear_f_near_saturation_block_alignment_600m.py -v
~~~
