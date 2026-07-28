---
kind: claim
claim_id: type-I-finite-exponent-dilation-boundary-297640249
title: Type I 有限指数障碍的五十层中心化盒边界
statement: 在线性一般 B 的冻结剖面中，p=297640249、R=148820123 的 K=3*37*127*97651*8044331 是有限指数障碍：-1 属于素因子残数生成子群，却不属于原始中心化平方除子谱。将每个中心化指数界从 [-nu_q(K),nu_q(K)] 同比放大到 [-c*nu_q(K),c*nu_q(K)] 后，-1 对所有 1<=c<=49 仍缺失，并恰在 c=50 首次出现。该放大入口对应 K 的一百次幂除子，不是原 Type I 选择器允许的 K 平方除子，故不构成新证书。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- finite-exponent
- exponent-saturation
- target-square-divisor
- boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 有限指数障碍的五十层中心化盒边界

## 状态与放大谱

从[四个全局线性 \(B=1\) 失败点的一般 \(B\) 剖面](type-I-global-linear-b1-failure-general-b-profile-500m.md)
冻结状态

\[
p=297640249,\qquad R=148820123,
\]

\[
K=\frac{pR+1}{4}
=3\cdot37\cdot127\cdot97651\cdot8044331. \tag{1}
\]

其原始中心化平方除子谱

\[
\mathcal C_{R,1}(K)
=\left\{\prod_{q\mid K}q^{z_q}\bmod R:
-\nu_q(K)\le z_q\le\nu_q(K)\right\} \tag{2}
\]

不含 \(-1\)，但 \(-1\) 属于相同素因子生成的单位群子群。因此这是
[中心化谱障碍二分](type-I-general-b-centered-square-spectrum.md)中的有限指数障碍，
而非角色障碍。

为量化该缺口，对 \(c\ge1\) 定义纯诊断性的放大盒

\[
\mathcal C_{R,c}(K)
=\left\{\prod_{q\mid K}q^{z_q}\bmod R:
-c\nu_q(K)\le z_q\le c\nu_q(K)\right\}. \tag{3}
\]

这里 \(c=1\) 才是原问题：它等价于 \(d\mid K^2\) 与
\(dK^{-1}\equiv-1\pmod R\)。一般 \(c\) 则对应

\[
d\mid K^{2c},\qquad dK^{-c}\equiv-1\pmod R, \tag{4}
\]

所以绝不能把 \(c>1\) 的入口解释为原 Type I 终端桥。

## 精确边界

对每个 \(1\le c\le50\)，程序以二因子对三因子的 MITM 穷尽 (3)，得到

\[
\boxed{
-1\notin\mathcal C_{R,c}(K)\quad(1\le c\le49),\qquad
-1\in\mathcal C_{R,50}(K).} \tag{5}
\]

首次入口的中心化指数向量，按 (1) 的五个素因子顺序为

\[
(-23,49,-25,47,-50). \tag{6}
\]

直接有

\[
3^{-23}37^{49}127^{-25}97651^{47}8044331^{-50}
\equiv-1\pmod {148820123}. \tag{7}
\]

等价地，(4) 中 \(c=50\) 可取的正指数向量为

\[
(27,99,25,97,0), \tag{8}
\]

即它确实落在 \(K^{100}\) 的因子盒中，但不落在任何较小的
\(K^{2c}\) 因子盒中。

## 含义与边界

这给出了一个可重算的反例，排除下列有限样本上的低复杂度设想：

\[
\text{“每个有限指数障碍在固定 }c\le49\text{ 的中心化放大盒中消失”。} \tag{9}
\]

它尤其说明有限指数障碍不能在这类状态上被当作“一次或少数次重复素因子即可补齐”的浅层
现象。另一方面，(5) 没有给出原选择器的新证书，也不说明一般有限指数障碍的放大深度有界或
无界。该核心素数在其它线性 \(R\) 上本来就有一般 \(B\) 命中；因此真正可推进原猜想的机制
仍应是**切换源状态或模数**，而不是把同一失败状态的 \(K^2\) 无限制增幂。

## 可复现检查

~~~bash
python3 reproductions/type_i_finite_exponent_dilation_boundary_297640249.py
python3 -m unittest tests.test_type_i_finite_exponent_dilation_boundary_297640249 -v
~~~
