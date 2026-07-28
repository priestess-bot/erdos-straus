---
kind: claim
claim_id: type-I-linear-f-cross-source-pullback-profile-600m
title: 七个完整线性谱中 F 状态的跨源共享层拉回剖面
statement: 对七个完整线性压力谱的68个有限指数F状态和105个有向源，逐状态定义跨源共享层 S_R=gcd(K_R,lcm_{R'!=R}|R-R'|/4)。共享层差集与块目标拉回的原始交集只出现在8个方向共100个残类，进入仿射块子群的有6个方向共80个残类，进入实际有限指数盒的方向为0；p=64214329,R=359的一条方向产生60个子群可见但有限盒外的残类，是当前扩展样本的集中边界。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- cross-modulus
- shared-layer
- finite-exponent
- centered-spectrum
- block-alignment
- seven-spectrum
- negative-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 七个完整线性谱中 F 状态的跨源共享层拉回剖面

## 定义与范围

对固定核心素数 \(p\) 的完整线性源模数集合 \(\mathcal R_p\)，记

\[
K_R=\frac{pR+1}{4},
\qquad
J_R=\operatorname{lcm}_{R'\in\mathcal R_p,\ R'\ne R}
\frac{|R-R'|}{4},
\qquad
S_R=\gcd(K_R,J_R).
\]

对有向源分解 \(K_R=\gamma L\)，令

\[
D_R(X)=\mathcal A_R(X)\mathcal A_R(X)^{-1},
\qquad
T_\gamma=\{-x^{-1}:x\in D_R(\gamma)\},
\qquad
H_L=\langle D_R(L)\rangle.
\]

本审计比较

\[
P_{\rm raw}=D_R(S_R)\cap T_\gamma,
\qquad
P_{\rm sub}=P_{\rm raw}\cap H_L,
\qquad
P_{\rm finite}=P_{\rm raw}\cap D_R(L).
\]

输入为七个已冻结的完整线性谱，共 278 个源模数，其中 68 个被分类为有限指数 F 状态。
每个 F 状态的全部有向源都重新恢复，不使用首达证书作为代理。

## 完整结果

对全部 \(5853\) 个跨模数源对逐项验证

\[
\gcd(K_R,K_{R'})
=\gcd\!\left(K_R,\frac{|R-R'|}{4}\right).
\]

105 个有向 F 源的汇总为：

| 层级 | 非空有向源数 | 残类总数 |
| --- | ---: | ---: |
| \(P_{\rm raw}\) | 8 | 100 |
| \(P_{\rm sub}\) | 6 | 80 |
| \(P_{\rm finite}\) | 0 | 0 |

按核心素数分组：

| \(p\) | F 状态数 | 有向源数 | \(P_{\rm raw}\) 方向 | \(P_{\rm sub}\) 方向 |
| ---: | ---: | ---: | ---: | ---: |
| 214,729 | 8 | 13 | 1 | 1 |
| 878,089 | 2 | 4 | 0 | 0 |
| 2,210,569 | 4 | 5 | 0 | 0 |
| 13,782,409 | 9 | 17 | 1 | 1 |
| 64,214,329 | 18 | 26 | 4 | 2 |
| 105,295,129 | 10 | 13 | 2 | 2 |
| 536,944,489 | 17 | 27 | 0 | 0 |
| **合计** | **68** | **105** | **8** | **6** |

所有 105 个方向都满足

\[
D_R(L)\cap T_\gamma=\varnothing.
\]

因此共享层即使把残类送入 \(H_L\)，也没有在这七个完整谱中直接完成有限指数块对齐。

## 集中边界

最大的一行出现在

\[
p=64{,}214{,}329,\qquad R=359,\qquad (a,s)=(7154,25).
\]

该方向的 \(P_{\rm raw}\) 与 \(P_{\rm sub}\) 都有 60 个残类，但
\(P_{\rm finite}=\varnothing\)。这不是单个偶然残类，而是一个大规模的“子群可见、指数盒
不可见”边界。

其它非空方向较小：\(p=214729,R=159\) 有 16 个原始类、8 个子群类；
\(p=13782409,R=335\) 有 2 个原始类；\(p=105295129\) 的两个状态分别产生
12 和 6 个原始类。\(p=878089\) 这个真实对抗点在本七谱审计中没有任何共享层拉回。

## 研究含义

七谱结果把四核心的负边界推广为一个更稳定的模式：

1. 跨模数 gcd 刚性确实能产生大量可追踪的共享指数层；
2. 共享层偶尔能把目标类送入仿射块的生成子群；
3. 但有限指数预算仍是独立障碍，不能由子群成员关系替代。

所以“找到共享因子”还不是选择器证明。真正需要的新引理应控制共享指数在
\(D_R(L)\) 中的**有限坐标预算**，或证明当预算不足时可以改变源分解并严格递降。

该剖面是七个有限谱上的完整负边界，不是全称反例，也不证明 Erdős--Straus 猜想。

## 复现

~~~bash
python3 reproductions/type_i_linear_f_cross_source_pullback_profile_600m.py
python3 -m unittest tests.test_type_i_linear_f_cross_source_pullback_profile_600m -q
~~~

结果文件：
[type-i-linear-f-cross-source-pullback-profile-600m-results.json](../reproductions/type-i-linear-f-cross-source-pullback-profile-600m-results.json)

规范记录摘要为
e97e13c805fc5a7bfe99f1ad108252fb3dd0f3c1282576dded9466f798ba56dc。
