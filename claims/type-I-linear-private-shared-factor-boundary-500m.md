---
kind: claim
claim_id: type-I-linear-private-shared-factor-boundary-500m
title: 线性一般 B 命中的私有与共享素因子边界
statement: 在四个五亿内全局线性 B=1 失败点的完整线性 R 谱中，称 q|K_R 为私有素因子若 q 不整除同一素数其它任何线性 K_R'。12 个一般 B 命中中，没有一个由私有块的中心化平方除子谱单独命中 -1；4 个由共享块单独命中，余下 8 个必须混合私有与共享块。故“一个源状态私有素因子必单独释放目标”的选择器在此冻结完整谱中失败。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- target-square-divisor
- prime-support
- private-factor
- subgroup-character
- finite-product
- terminal-bridge
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性一般 \(B\) 命中的私有与共享素因子边界

## 定义与范围

输入是[五亿全局 \(p-1\) 遗漏的线性 \(B=1\) 失败与一般 \(B\) 剖面](type-I-global-linear-b1-failure-general-b-profile-500m.md)
的四个冻结素数。对其中一个固定的 \(p\)，令 \(\mathcal R_p\) 为其全部线性源诱导的不同
模数 \(R\)，并写

\[
K_R=\frac{pR+1}{4}.
\]

若素数 \(q\mid K_R\)，且对每个 \(R'\in\mathcal R_p\setminus\{R\}\) 都有
\(q\nmid K_{R'}\)，则称 \(q\) 对 \((p,R)\) 是**谱内私有**的。其余 \(K_R\) 素因子
称为共享素因子。这个定义只量化冻结的同一 \(p\) 的完整线性谱；它不是关于所有核心素数
的绝对私有性。

将 \(K_R\) 的因子分解为

\[
K_R=P_R S_R,
\]

其中 \(P_R\) 收集谱内私有素因子的全部幂，\(S_R\) 收集共享素因子的全部幂。对任一块
\(N\) 使用中心化平方除子谱

\[
\mathcal C_R(N)=
\left\{\prod_{q\mid N}q^{z_q}\bmod R:
-\nu_q(N)\le z_q\le\nu_q(N)\right\}. \tag{1}
\]

一般 \(B\) 目标是 \(-1\in\mathcal C_R(K_R)\)。本页只问该目标能否已经落在
\(\mathcal C_R(P_R)\) 或 \(\mathcal C_R(S_R)\)。

## 完整有限结果

四个素数的全部线性模数分别为 \(38,52,55,46\) 个；它们的 12 个一般 \(B\) 命中精确
分为：

| \(p\) | 命中 \(R\) 数 | 私有块单独命中 | 共享块单独命中 | 私有--共享混合必需 |
| ---: | ---: | ---: | ---: | ---: |
| 3,942,409 | 4 | 0 | 2 | 2 |
| 62,588,089 | 2 | 0 | 0 | 2 |
| 297,640,249 | 4 | 0 | 1 | 3 |
| 477,015,289 | 2 | 0 | 1 | 1 |
| **合计** | **12** | **0** | **4** | **8** |

“混合必需”表示

\[
-1\notin\mathcal C_R(P_R),\qquad
-1\notin\mathcal C_R(S_R),\qquad
-1\in\mathcal C_R(P_RS_R). \tag{2}
\]

因而任一目标见证都必须同时使用两块的非零中心化坐标。四个共享块单独命中则说明私有因子
在这些状态里完全不是目标命中的必要来源。

## 含义与边界

一个自然的下一步设想是：不同线性源带来一个新的私有素因子，而这个私有因子应单独打破
所有既有角色障碍。上表精确否定了这个设想的最直接版本：12 个命中中私有块单独命中的数目
为零；其中 8 个甚至需要私有与共享素因子的联合积集。

这不排除利用私有因子与共享因子的**联合**分布来证明选择器，也不反驳线性一般 \(B\)
猜想。它只给出一个有限但完整的设计约束：跨源对象不能把新出现的素因子当作独立的
“单因子逃逸开关”，而必须保留其与旧因子在中心化指数盒中的相互作用。

## 可复现检查

~~~bash
python3 reproductions/type_i_linear_private_shared_factor_boundary_500m.py
python3 -m unittest tests.test_type_i_linear_private_shared_factor_boundary_500m -v
~~~
