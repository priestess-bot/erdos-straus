---
kind: claim
claim_id: type-I-linear-cross-modulus-gcd-rigidity
title: 线性源模数之间的公因子刚性与共享指数层
statement: 对同一奇素数 p 的两个不同线性源模数 R,R'=3 mod4，令 K_R=(pR+1)/4、K_R'=(pR'+1)/4，则 gcd(K_R,K_R')=gcd(K_R,abs(R-R')/4)。因此在任一有限线性源谱中，每个 K_R 的所有跨模数可共享素因子幂恰由 K_R 与其它源模数差的四分之一最小公倍数决定；K_R 的中心化平方除子谱精确分解为该共享指数层与其余指数层的乘积谱。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- factorization
- gcd-rigidity
- shared-factors
- finite-product
- target-square-divisor
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性源模数之间的公因子刚性与共享指数层

## 定理

固定奇素数 \(p\)，取同一 \(p\) 的两个不同线性源模数

\[
p=a+s+asR=a'+s'+a's'R',
\qquad R\equiv R'\equiv3\pmod4,
\]

并记

\[
K_R=\frac{pR+1}{4},\qquad K_{R'}=\frac{pR'+1}{4}. \tag{1}
\]

则 \(4\mid R-R'\)，且有精确恒等式

\[
\boxed{
\gcd(K_R,K_{R'})
=\gcd\left(K_R,\frac{\lvert R-R'\rvert}{4}\right)
=\gcd\left(K_{R'},\frac{\lvert R-R'\rvert}{4}\right).} \tag{2}
\]

故不是源于模数差 \((R-R')/4\) 的素因子幂，不可能在两个不同的 \(K\) 中同时出现。

## 证明

由 (1) 直接相减，

\[
K_R-K_{R'}=\frac{p(R-R')}{4}. \tag{3}
\]

又

\[
4K_R=pR+1\equiv1\pmod p,
\]

所以 \(\gcd(K_R,p)=1\)。利用 \(\gcd(x,y)=\gcd(x,y-x)\)，得到

\[
\begin{aligned}
\gcd(K_R,K_{R'})
&=\gcd\left(K_R,\frac{p(R-R')}{4}\right)\\
&=\gcd\left(K_R,\frac{R-R'}4\right).
\end{aligned}
\]

取绝对值并交换 \(R,R'\) 即得 (2)。该论证只使用 (1)，所以对所有不同的线性源状态都成立；
同一 \(R\) 的多种定向 \((a,s)\) 不会制造新的 \(K\)，应先合并为一个模数状态。

## 有限源谱的精确层分解

令 \(\mathcal R\) 是固定 \(p\) 的有限个不同线性源模数。对 \(R\in\mathcal R\)，定义

\[
J_R=\operatorname{lcm}_{R'\in\mathcal R,\ R'\ne R}
\frac{\lvert R-R'\rvert}{4},
\qquad
S_R=\gcd(K_R,J_R),\qquad
P_R=\frac{K_R}{S_R}, \tag{4}
\]

其中空最小公倍数约定为 \(1\)。由 (2) 和逐素数赋值，

\[
\boxed{
S_R=
\operatorname{lcm}_{R'\ne R}\gcd(K_R,K_{R'}).} \tag{5}
\]

更明确地，若 \(q^\nu\Vert K_R\)，则 \(S_R\) 中 \(q\) 的指数为

\[
\min\left(
\nu,
\max_{R'\ne R}v_q\left(\frac{\lvert R-R'\rvert}{4}\right)
\right). \tag{6}
\]

它恰好是可在某个其它 \(K_{R'}\) 的公因子中出现的最高指数层。注意 \(S_R\) 与
\(P_R\) 未必互素：同一个素数可以在其它状态中以较低指数出现，而 \(P_R\) 保存其无法跨模数
共享的剩余指数层。

对任意正整数 \(N=\prod q^{\nu_q}\)，记中心化平方除子谱

\[
\mathcal C_R(N)=
\left\{\prod_{q\mid N}q^{z_q}\pmod R:
-\nu_q\le z_q\le\nu_q\right\}. \tag{7}
\]

因为每个指数区间 \([-\nu_q,\nu_q]\) 是 \(S_R\) 与 \(P_R\) 的相应指数区间之和，
有精确的积集恒等式

\[
\boxed{
\mathcal C_R(K_R)=\mathcal C_R(S_R)\,\mathcal C_R(P_R).} \tag{8}
\]

这里右端表示所有两边残数的乘积集，不要求 \(S_R,P_R\) 互素。故一般 \(B\) 的目标
\(-1\in\mathcal C_R(K_R)\) 可逐状态精确区分为共享层单独命中、剩余层单独命中或必须混合。

## 四点全谱剖面

在[五亿全局 \(p-1\) 遗漏的线性 \(B=1\) 失败与一般 \(B\) 剖面](type-I-global-linear-b1-failure-general-b-profile-500m.md)
的四个完整线性谱中，所有 \(191\) 个源模数对都逐对复核 (2)。对其中 \(12\) 个一般 \(B\)
目标命中，按 (4)--(8) 的精确分割为：

| \(p\) | 命中 \(R\) 数 | 共享层单独命中 | 必须混合两层 |
| ---: | ---: | ---: | ---: |
| 3,942,409 | 4 | 1 | 3 |
| 62,588,089 | 2 | 0 | 2 |
| 297,640,249 | 4 | 1 | 3 |
| 477,015,289 | 2 | 1 | 1 |
| **合计** | **12** | **3** | **9** |

没有一个命中只由 \(P_R\) 的跨模数独有指数层完成。例如
\(p=3942409,R=199\) 的命中必须混合

\[
S_R=40768,\qquad P_R=4811,
\]

而同一素数在 \(R=171\) 的命中已由 \(S_R=37345\) 单独完成。

这比[私有与共享素因子边界](type-I-linear-private-shared-factor-boundary-500m.md)
更细：后者按“一个素数是否曾在另一状态出现”划分，本页按每个素数的**可共享指数上限**
划分。两种分割都显示单一新因子层不是通用逃逸开关；但 (2) 提供了真正的跨源算术约束，
可作为后续研究共同因子、混合积集或跨源递降的输入。

该有限剖面不证明目标 \(-1\) 必命中，也不排除所有状态的角色或有限指数障碍。它的作用是
把跨源“共享”从经验标签改写为完全由源模数差控制的可验证量。

## 复现

~~~bash
python3 reproductions/type_i_linear_cross_modulus_layer_profile_500m.py
python3 -m unittest tests.test_type_i_linear_cross_modulus_layer_profile_500m -v
~~~
