---
kind: claim
claim_id: type-I-linear-general-b-two-block-hit-profile-500m
title: 线性一般 B 命中的源块与仿射块混合剖面
statement: 对四个全局线性B=1失败点的12个一般B线性目标命中及其20个定向源，写线性源诱导的K为K=gamma*L，其中gamma来自源因子sR+1、L来自仿射因子aR+1。精确枚举两块各自的中心化平方除子谱后，16个定向命中必须混合两块素因子；仅2个由源块单独命中、2个由仿射块单独命中。12个目标的最小非零中心化素数坐标数精确分布为2个二坐标、4个三坐标、4个四坐标、2个五坐标。特别地，p=3942409的全部4个线性一般B命中均为混合型且至少三坐标。故单块或双因子对选择器均在此冻结完整源谱中失败，但混合乘积仍给出原目标所需的有效K平方命中。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- source-square
- factorization
- target-square-divisor
- finite-product
- boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性一般 \(B\) 命中的源块与仿射块混合剖面

## 两块分解

在线性源

\[
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod4 \tag{1}
\]

中，令

\[
\lambda=
\begin{cases}
4,&s\equiv1\pmod4,\\
2,&s\equiv3\pmod4,
\end{cases}
\qquad
\eta=\frac4\lambda,
\]

\[
\gamma=\frac{sR+1}{\lambda},\qquad
L=\frac{aR+1}{\eta}. \tag{2}
\]

则

\[
K=\frac{pR+1}{4}=\gamma L. \tag{3}
\]

对任意因子块 \(N\) 定义其中心化平方除子谱

\[
\mathcal C_R(N)=
\left\{\prod_{q\mid N}q^{z_q}\bmod R:
-\nu_q(N)\le z_q\le\nu_q(N)\right\}. \tag{4}
\]

若 \(-1\in\mathcal C_R(\gamma)\)，则乘上 \(L\) 可直接构造 \(K^2\) 的目标因子；
\(L\) 的情形同理。若两者都不含 \(-1\)、但 \(-1\in\mathcal C_R(K)\)，则任何该
状态的目标命中都需要两块的混合指数贡献。

## 冻结命中的精确分割

对[全局线性 \(B=1\) 失败的一般 \(B\) 剖面](type-I-global-linear-b1-failure-general-b-profile-500m.md)
中的12个命中 \(R\)，逐个恢复其全部20个定向 \((a,s)\) 源，并独立枚举 (4)：

| \(p\) | 定向命中源数 | 源块单独 | 仿射块单独 | 混合两块 |
| ---: | ---: | ---: | ---: | ---: |
| 3,942,409 | 4 | 0 | 0 | 4 |
| 62,588,089 | 5 | 0 | 0 | 5 |
| 297,640,249 | 7 | 0 | 0 | 7 |
| 477,015,289 | 4 | 2 | 2 | 0 |
| **合计** | **20** | **2** | **2** | **16** |

例如 \(p=3942409\) 的四个完整线性一般 \(B\) 命中模数

\[
R=171,\ 199,\ 391,\ 10951 \tag{5}
\]

均满足

\[
-1\notin\mathcal C_R(\gamma),\qquad
-1\notin\mathcal C_R(L),\qquad
-1\in\mathcal C_R(\gamma L). \tag{6}
\]

上游审计已经完整枚举该素数的38个线性 \(R\)，而 (5) 正是全部命中。因此在这个
完整线性源谱内，不存在可替代的单块目标命中。

## 含义与边界

这排除一种自然但过强的证明收缩：

\[
\text{“对某个成功线性源，\(\gamma\) 或 \(L\) 必单独提供 \(-1\)”。} \tag{7}
\]

它不反驳一般 \(B\) 线性选择器，恰恰相反，16 个混合状态仍在 \(K^2\) 中给出有效目标
因子和 Type I 终端桥。它说明后续跨源理论必须处理两块实际素因子的**联合积集**；
只对源平方块或仿射块分别施加饱和/角色论证，会漏掉这里占多数的成功机制。

## 最小中心化坐标复杂度

对每个命中 \((R,K)\)，定义

\[
w_R(K)=\min\left\{
\#\{q:z_q\ne0\}:
\prod_{q\mid K}q^{z_q}\equiv-1\pmod R,\quad
-\nu_q(K)\le z_q\le\nu_q(K)
\right\}. \tag{8}
\]

程序完整枚举每个 \(K^2\) 的中心化指数盒，保存所有达到该最小值的向量数及其字典序首个
见证。12 个目标模数的分布为：

| \(p\) | \(w=2\) | \(w=3\) | \(w=4\) | \(w=5\) |
| ---: | ---: | ---: | ---: | ---: |
| 3,942,409 | 0 | 2 | 1 | 1 |
| 62,588,089 | 0 | 1 | 1 | 0 |
| 297,640,249 | 0 | 1 | 2 | 1 |
| 477,015,289 | 2 | 0 | 0 | 0 |
| **合计** | **2** | **4** | **4** | **2** |

因此，除了两条 \(p=477015289\) 的目标外，其余十条都不能以一对非零中心化素数坐标完成。
更强地，\(p=3942409,R=10951\) 满足 \(w_R(K)=5\)，而该素数所有四个线性目标命中均有
\(w_R(K)\ge3\)。于是“找一对跨块因子使其积为 \(-1\)”同样不是可推广的线性子选择器。

## 可复现检查

~~~bash
python3 reproductions/type_i_linear_general_b_two_block_hit_profile_500m.py
python3 -m unittest tests.test_type_i_linear_general_b_two_block_hit_profile_500m -v
~~~
